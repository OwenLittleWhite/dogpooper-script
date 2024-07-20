import cv2
import numpy as np

def load_images(main_image_path, template_image_path):
    main_image = cv2.imread(main_image_path)
    template_image = cv2.imread(template_image_path)
    return main_image, template_image

def split_image(image, rows, cols):
    height, width = image.shape[:2]
    region_height = height // rows
    region_width = width // cols
    regions = []
    for i in range(rows):
        for j in range(cols):
            x_start, x_end = j * region_width, (j + 1) * region_width
            y_start, y_end = i * region_height, (i + 1) * region_height
            regions.append((x_start, y_start, x_end, y_end))
    return regions

def detect_and_compute(image, detector):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    keypoints, descriptors = detector.detectAndCompute(gray_image, None)
    return keypoints, descriptors

def match_features(descriptors_target, descriptors_region, matcher, threshold):
    matches = matcher.knnMatch(descriptors_target, descriptors_region, k=2)
    good_matches = []
    for m, n in matches:
        if m.distance < threshold * n.distance:
            good_matches.append(m)
    return good_matches

def disgust_pic(main_image_path, template_image_path, threshold=0.4):
    main_image, template_image = load_images(main_image_path, template_image_path)
    
    # Split the main image into 3x5 regions
    rows, cols = 3, 5
    regions = split_image(main_image, rows, cols)

    # Create SIFT detector
    sift = cv2.SIFT_create()

    # Detect and compute keypoints and descriptors for the template image
    keypoints_target, descriptors_target = detect_and_compute(template_image, sift)

    # Create FLANN matcher
    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # List to store matching region center points
    matching_region_centers = []

    # Iterate over each region and perform feature matching
    for (x_start, y_start, x_end, y_end) in regions:
        region = main_image[y_start:y_end, x_start:x_end]
        keypoints_region, descriptors_region = detect_and_compute(region, sift)
        try:
            good_matches = match_features(descriptors_target, descriptors_region, flann, threshold)
            
            if len(good_matches) > 10:
                center_x = (x_start + x_end) // 2
                center_y = (y_start + y_end) // 2
                matching_region_centers.append((center_x, center_y))
        except:
            pass

    return matching_region_centers

# if __name__ == "__main__":
#     main_image_path = 'cropped_screenshots/cropped_screenshot.png'
#     template_image_path = 'pooper_items/1.png'
#     matched_centers = main(main_image_path, template_image_path, threshold=0.7)
#     print(matched_centers)

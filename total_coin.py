baseCoin = 3276.7
baseLevel = 15
levels = [15,16,21,24]
totalCoin = 72510
for i in levels:
    diff = i - baseLevel
    print(i, ":",baseCoin * (2 ** diff))
    totalCoin += baseCoin * (2 ** diff)
print(totalCoin)
print(f"incr: {totalCoin - 1945953.2}")

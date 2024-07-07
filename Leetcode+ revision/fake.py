a = [2, 9, 31, -4, 21, 7]
k = 3

# Initialize window sum and maximum sum
wSum = 0
mSum = float('-inf')

# Calculate the sum of the first k elements
for i in range(k):
    wSum += a[i]

# Initialize maximum sum with the first window sum
mSum = wSum

# Slide the window from k to the end of the array
for i in range(k, len(a)):
    wSum = wSum - a[i - k] + a[i]
    mSum = max(wSum, mSum)

print(mSum)

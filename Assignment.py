def max_area(h):
    max_water = 0
    left = 0
    right = len(h) - 1

    while left < right:
        # Calculate the current area between the lines
        current_water = min(h[left], h[right]) * (right - left)
        max_water = max(max_water, current_water)

        # Move the pointers
        if h[left] < h[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Take user input for height list
h = list(map(int, input("Enter heights of vertical lines separated by space: ").split()))

# Call the function and print the result
result = max_area(h)
print("Maximum amount of water the container can store:", result)
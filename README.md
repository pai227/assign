# assign
Problem Statement: Given an integer array height representing the heights of n vertical lines, the task is to find two lines that, together with the x-axis, form a container that holds the most water. The function max_area() calculates and returns the maximum amount of water the container can store without slanting it.

Approach: The script employs a two-pointer approach to efficiently calculate the maximum water capacity. It iterates through the list with two pointers, left and right, initially pointing to the start and end of the list, respectively. The algorithm continuously calculates the area between the lines, updates the maximum water capacity, and moves the pointers based on the height of the lines to determine the optimal water-holding configuration.

Usage: The script prompts the user to input a list of integer heights separated by spaces. Upon receiving the input, the script computes and displays the maximum amount of water that the container formed by the provided heights can hold. Running the Script: To run the script:

Clone the repository containing the Python script. Open the terminal and navigate to the script's directory. Execute the script using Python 3. Follow the prompt to input the heights, e.g., 1 8 6 2 5 4 8 3 7. The script calculates and displays the maximum amount of water that can be contained based on the provided heights

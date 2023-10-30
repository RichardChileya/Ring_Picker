# Ring_Picker
A simple program that outputs the different patterns that 4 rings could be worn. matching the parameters. 
The code generates all possible combinations of wearing rings on different fingers and prints the combinations.

# How it works
The rings and fingers are defined as lists.
A loop iterates through each finger and each ring to generate combinations.
Certain conditions are checked to filter out invalid combinations:
If the finger is the right ring finger (index 3), but the ring is not a diamond or a citrine, the combination is skipped.
If the finger is the thumb (index 0) or the right ring finger (index 3) with a diamond ring (index 1), the combination is skipped.
If the ring is a diamond and there are already two diamond rings worn, the combination is skipped.
Valid combinations are stored in a list.
Finally, the program prints each combination in the format "Wearing [ring] ring on [finger] finger".
# Usage
To use this code, simply run it in a Python environment. The combinations will be printed to the console log.


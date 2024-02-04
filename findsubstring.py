"""In this challenge, the user 
enters a string and a substring. 
You have to print the number of times that
the substring occurs in the given string. 
String traversal will take place from left
to right, not from right to left."""

import re


def count_substring(string, substring):
    count = 0
    start = 0
    # Search through the string till we reach the end of it
    while start < len(string):
        # Check if a substring is present from start position till the end
        pos = string.find(substring, start)

        if pos != -1:
            # If subsring is present, move start to next position of substring
            start = pos + 1
            # Increment the count
            count += 1
        else:
            # If no other substring is present
            break
    return count


# Driver code
if __name__ == "__main__":
    string = input("Enter string to check: ").strip()
    sub_string = input("Enter substring to check: ").strip()

    count = count_substring(string, sub_string)
    print(count)

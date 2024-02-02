def merge_the_tools(s, k):

    n = len(s)

    for i in range(0, n, k):
        # Extract a substring of length k
        substring = s[i : i + k]

        # Remove duplicate characters in the substring while maintaining the order
        unique_chars = ""
        for char in substring:
            if char not in unique_chars:
                unique_chars += char

        # Print the result
        print(unique_chars)


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)

rows = int(input("Enter number of rows (outer loop): "))
columns = int(input("Enter number of columns (inner loop): "))
symbol = input("Enter character to print: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()

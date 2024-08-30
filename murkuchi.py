#This is multiplication table of 1 to 12.

def printmultiplication(start, end):
    # Create a list to store the results
    table = []

    # Fill the table with formatted results
    for i in range(start, end + 1):
        row = [f"{i} * {j} = {i * j}" for j in range(start, end + 1)]
        table.append(row)

    # Print the table in a vertical format
    # Calculate the maximum length of the items in the column
    col_width = max(len(item) for row in table for item in row)

    for j in range(len(table[0])):
        # Print each column
        for i in range(len(table)):
            print(f"{table[i][j]:{col_width}}", end='  ')
        print()

printmultiplication(1, 10)


    




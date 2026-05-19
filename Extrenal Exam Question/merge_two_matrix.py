rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# First matrix
print("\nEnter elements of First Matrix:")
matrix1 = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Matrix1[{i}][{j}] = "))
        row.append(value)
    matrix1.append(row)

# Second matrix
print("\nEnter elements of Second Matrix:")
matrix2 = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Matrix2[{i}][{j}] = "))
        row.append(value)
    matrix2.append(row)

# Merge matrices
merged_matrix = matrix1 + matrix2

# Display merged matrix
print("\nMerged Matrix:")
for row in merged_matrix:
    print(row)
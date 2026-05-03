# 4. Write a program to print the summation of the following series upto n terms:1-2+3-4+5- 6+7	n

n = int(input("Enter number of terms (n): "))

sum_series = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_series -= i  # Even terms are negative
    else:
        sum_series += i  # Odd terms are positive

print(f"Sum of series up to {n} terms: {sum_series}")

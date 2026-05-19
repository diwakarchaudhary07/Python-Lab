principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Display result
print("\n----- Result -----")
print("Principal Amount :", principal)
print("Rate of Interest :", rate)
print("Time :", time, "years")
print("Simple Interest :", simple_interest)
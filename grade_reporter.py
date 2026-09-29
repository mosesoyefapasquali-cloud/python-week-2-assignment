```python
scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F" 

    print("Score:", score, "Grade:", grade)

    total = total + score

    if score >= 50:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / len(scores)

print("Passed:", passed)
print("Failed:", failed)
print("Average:", round(average, 1))
```
# Simple Bill Calculator

# Ask the user for the price of one item
price = float(input("Enter the price of one item: "))

# Ask the user for the quantity
quantity = int(input("Enter the quantity: "))

# Calculate the total
total = price * quantity

# Display the result using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
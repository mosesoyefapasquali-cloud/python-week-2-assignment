count = 1
total = 0

# BUG 1 FIX: Added the missing colon to the while condition.
while count <= 5:
    total = total + count
    count = count + 1

# BUG 2 FIX: Converted total to a string before joining it with text.
print("Sum of 1 to 5 is: " + str(total))

# BUG 3 FIX: The loop condition allows the program to add numbers from 1 to 5.

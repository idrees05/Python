# loops used to repeat set of instructions till you set some condtition to stop it
# two main types of loops, 'while' & 'for'
# 'for' to iterate of sequences - strings, lists, tuples

finalSum = 0
number = 0

while number <= 100:
    finalSum += number  # the order in which you write the code is important
    number += 1

print("This is the total of all the numbers up to 100:", finalSum)


#You can also use a forloop to do the same thing

total_sum = 0

# Step 2: Use a loop to iterate from 1 to 100
for num in range(1, 101):
    # Step 3: Add each number to the sum
    total_sum += num

# Step 4: Print the sum
print("The sum of numbers from 1 to 100 is:", total_sum)



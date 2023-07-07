# For the following list of numbers:

numbers = [1, 6, 99, 2, 2, 1, 3, 7, 6, 13, 7]

# 1. Print out a list of the even integers:

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


# 2. Print the difference between the largest and smallest value:

# numbers.sort()
difference = numbers[8] - numbers[0]

print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.


def search_for_twos(list):
    length = len(list)
    for box in list:
            if box < length:
                if box == list[box+1] and box == 2:
                    return True

print(search_for_twos(numbers))


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

power = True
total = 0

def weird_sum_tool(list):
    total = 0
    power = True
    for digit in numbers:
        if digit == 6:
            power = False
        elif digit == 7:
            power = True
            if power == True:
                continue
        elif power == False:
            continue
        else:
            total += digit
            
weird_sum_tool(numbers)

print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 



def unlucky_number_function(list):
    total = 0
    round = 0
    max_round_number = len(list)
    while round < max_round_number: # basically saying until you get to the end of list!
        if list[round] == 13:
            round += 2
        else:
            total += list[round]
            round += 1 # this is moving the "round" up
    return total


print(unlucky_number_function(numbers))









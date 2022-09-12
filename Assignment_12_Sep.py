#Assignment 1


"""Function to input a natural number and output the digits in it without converting it into a string"""


def dig_count(input_number):
    digit_count = 0
    while input_number != 0:
        input_number = int(input_number/10)
        digit_count += 1
    return digit_count


if __name__ == '__main__':
    get_input = int(input("Enter your Number: "))
    print(f"Number of digits in the input number is {dig_count(get_input)}")


#Assignment 2
"""Function that takes a natural number as input and output the reverse of it. Conversion of the number into
a string is not allowed"""


def number_reverse(input_number):
    reversed_number = 0
    while input_number>0:
        digit = input_number%10
        reversed_number = reversed_number*10 + digit
        input_number = input_number//10
    return reversed_number


if __name__ == '__main__':
    get_input_number = int(input("Enter your Number: "))
    print(f"Reverse of your number is {number_reverse(get_input_number)}")

#Assignment 3
'''Write function where user will enter a natural number as input and output returns the number
    of zeros in the end of the factorial of that number. Conversion of number to a string is
    not allowed'''


def factorial(input_number):
    result = 1
    if input_number > 1:
        for i in range(1, input_number + 1):
            result = result*i
        return result
    else:
        return None


def count_zero(input_number):
    count = 0
    while input_number%10 == 0:
        count+=1
        input_number = int(input_number / 10)
    return count


if __name__ == '__main__':
    get_input = int(input("Enter your number: "))
    print(f"Result factorial of your number {get_input} is {factorial(get_input)} and count of zeroes at the end are {count_zero(factorial(get_input))}")


#Assignment 4
'''Function to take 2 list as input and return a dictionary from it'''
list1 = ["India", "England", "Spain"]
list2 = ["Delhi", "London", "Madrid"]


def create_dict(country_list, capital_list):
    result_dict = dict(zip(country_list, capital_list))
    return result_dict


if __name__ == '__main__':
    print(f"Result dictionary is {create_dict(list1,list2)}")


#Assignment 5
'''Write code to create dictionary using the given dictionary'''
places = {
    ("19.07'53.2", "72.54'51.0"): "Mumbai",
    ("28.33'34.1", "77.06'16.6"): "Delhi"
}
location_list = [{"Latitude":list(places.keys())[0][0], "Longitude": list(places.keys())[0][1]},
                 {"Latitude":list(places.keys())[1][0], "Longitude": list(places.keys())[1][1]}]

print(dict(zip(list(places.values()), location_list)))



#Assignment 6
'''Using loop, find sum of all even numbers in the given list'''
mylist = [3,5,4,6,9,10,2,8,7,1]
sum_of_even_numbers = 0
for item in mylist:
    if item%2 == 0:
        sum_of_even_numbers += item
print(f"Sum of even numbers in your list is {sum_of_even_numbers}")



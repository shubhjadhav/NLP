# print(50 * '-' + '\n' + 20 * ' ' + 'NLP - Homework 2\n' + 50 * '-')
#
# # ----------------------------------------------------------------
# # HW Q1:
# # Write a python script that reads a string from the user input and print the following
# # i. Number of uppercase letters in the string.
# # ii. Number of lowercase letters in the string
# # iii. Number of digits in the string
# # iv. Number of whitespace characters in the string
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW Q1' + 20 * '-')
#
# # Input string from user - Ex: Natural Language Processing is 1 or 2 or 3 overall ranking SUBJECT
# user_input = input("Enter a string: ")
#
# # Initialize the counters
# upper_cnt = lower_cnt = digit_cnt = spaces_cnt = 0
#
# # Iterate over the string
# for char in user_input:
#     if char.isupper():
#         upper_cnt += 1
#     elif char.islower():
#         lower_cnt += 1
#     elif char.isdigit():
#         digit_cnt += 1
#     elif char.isspace():
#         spaces_cnt += 1
#
# # Print the results
# print("\nNumber of uppercase letters:", upper_cnt)
# print("Number of lowercase letters:", lower_cnt)
# print("Number of digits:", digit_cnt)
# print("Number of whitespace characters:", spaces_cnt)
#
# # Using list comprehension (not optimised)
# # sum(char.isupper() for char in password)
#
# print(20 * '-' + 'End HW Q1' + 20 * '-')
#
#
# # ----------------------------------------------------------------
# # HW Q2:
# # Write a python script that accepts a string then create a new string
# # by shifting one position to left.
# # Example: input : class 2021 output: lass 2021c
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW Q2' + 20 * '-')
#
# # Input string from user
# user_input = input("Enter a string: ")
#
# # Shift first character to last
# str_shift = user_input[1:]+user_input[0]
#
# print("The updated string: " + str_shift)
#
# print(20 * '-' + 'End HW Q2' + 20 * '-')
#
#
# # ----------------------------------------------------------------
# # HW Q3:
# # Write a python script that a user input his name and program display its initials.
# # Hint: Assuming, user always enter first name, middle name and last name.
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW Q3' + 20 * '-')
#
# # Input string from user
# user_input = input("Enter a string: ")
#
# # Shift first character to last
# split_str_arr = user_input.split()
#
# initials = ''
#
# for word in split_str_arr:
#     initials += word[0]
#
# print("The initials are : " + initials)
#
# print(20 * '-' + 'End HW Q3' + 20 * '-')


# # ----------------------------------------------------------------
# # HW Q4:
# # Write a python script that accepts a string to set up a passwords.
# # The password must have the following requirements
# # i.   The password must be at least eight characters long.
# # ii.  It must contain at least one uppercase letter.
# # iii. It must contain at least one lowercase letter.
# # iv.  It must contain at least one numeric digit.
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW Q4' + 20 * '-')
#
# # Input string from user
# password = input("Enter a password: ")
#
# # Initialize the check
# has_upper = has_lower = has_digit = 0
#
# # condition 1
# if len(password) >= 8:
#     # Iterate over the string
#     for char in password:
#         if char.isupper() and ~has_upper:
#             has_upper = 1
#         elif char.islower() and ~has_lower:
#             has_lower = 1
#         elif char.isdigit() and ~has_digit:
#             has_digit = 1
#
# if has_upper + has_lower + has_digit == 3:
#     print("The input successfully meet the password requirements")
# else:
#     print("The input does not meet the password requirements")
#
# print(20 * '-' + 'End HW Q4' + 20 * '-')


# # ----------------------------------------------------------------
# # HW Q5:
# # Write a python script that reads a given string character by character and count
# # the repeated characters then store it by length of those character(s).
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW Q5' + 20 * '-')
#
# # Input string from user
# user_input = input("Enter a string: ")
#
# char_len_dict = {}
#
# # Iterate over the string
# for char in user_input:
#     if char in char_len_dict:
#         char_len_dict[char] += 1
#     else:
#         char_len_dict[char] = 1
#
# for char, cnt in char_len_dict.items():
#     print(char + ': ' + str(cnt))
#
# print(20 * '-' + 'End HW Q5' + 20 * '-')


# # ----------------------------------------------------------------
# # HW Q6:
# # Write a python script to find all lower and upper case combinations of a given string.
# # Example: input: abc output: 'abc', 'abC', 'aBc', ...
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW Q6' + 20 * '-')
#
# # Input string from user
# user_input = input("Enter a string: ")
#
# comb_lst = []
#
#
# def generate_case_combinations(input_string, current_index, current_combination, comb_lst):
#     if current_index == len(input_string):
#         comb_lst.append(current_combination)
#         return
#
#     char = input_string[current_index]
#
#     # Generate combinations with the current character in lowercase
#     generate_case_combinations(input_string, current_index + 1, current_combination + char.lower(), comb_lst)
#
#     # Generate combinations with the current character in uppercase
#     generate_case_combinations(input_string, current_index + 1, current_combination + char.upper(), comb_lst)
#
#
# # Generate the lowercase and uppercase combinations
# generate_case_combinations(user_input, 0, "", comb_lst)
#
# print('There are ' + str(len(comb_lst)) + ' combinations')
# print('Combinations: ' + str(comb_lst))
#
# print(20 * '-' + 'End HW Q6' + 20 * '-')


# # ----------------------------------------------------------------
# # HW Q7:
# # Write a python script that:
# # i.   Read first n lines of a file.
# # ii.  Find the longest words.
# # iii. Count the number of lines in a text file.
# # iv.  Count the frequency of words in a file.
# # Hint: first create a test.txt file and dump some textual data in it.
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW Q7' + 20 * '-')
#
# # Read text file
# f = open("Data/APrincessOfMars.txt", 'r', encoding='utf-8-sig')
#
# # i.   Read first n lines of a file.
#
# # Input number of lines from user
# n_lines = int(input("How many lines you want to read? "))
#
# for line in range(n_lines):
#     print('Line ' + str(line + 1) + ': ' + f.readline())
#     if line + 1 == n_lines:
#         f.seek(0)
#
# # ii.  Find the longest words.
#
# # Getting the list of words of a file
# word_list = [word.strip('.,!?()[]{}";:\'') for word in f.read().split()]
# f.seek(0)
#
# # finding the length of the longest word in the above words list
# longest_word_len = len(max(word_list, key=len))
#
# # find words with the longest length
# result = [word for word in word_list if len(word) == longest_word_len]
#
# print('The length of the longest word in the text is :' + str(longest_word_len))
# print('And the words are: ' + str(result))
#
# # iii. Count the number of lines in a text file.
# print('\nThe number of lines in the text: ' + str(len(f.readlines())))
# f.seek(0)
#
# # iv.  Count the frequency of words in a file.
# word_freq = {}
#
# for word in word_list:
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1
#
# for word in word_freq:
#     print(word + ': ' + str(word_freq[word]))
#
# print(20 * '-' + 'End HW Q7' + 20 * '-')


# # ----------------------------------------------------------------
# # HW Q8.1:
# # Write a function that prints all the chars from string1 that appears in string2.
# # Note: Just use the strings functionality no other packages should be used.
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW Q8.1' + 20 * '-')
#
# # Input string from user
# string_1 = input("Enter first string: ")
# string_2 = input("Enter second string: ")
# repeating_char = set()
#
# for char in string_1:
#     if char in string_2:
#         repeating_char.add(char)
#
# print('The repeating character from string1 that appear in string2 are ' + str(repeating_char))
#
# print(20 * '-' + 'End HW Q8.1' + 20 * '-')


# ----------------------------------------------------------------
# HW Q8.2:
# Write a function that counts the numbers of a particular letter in a string.
# For example count the number of letter "a" in abstract.
# Note: Compare your function with a count method.
# ----------------------------------------------------------------
print('\n\n' + 20 * '-' + 'Begin HW Q8.2' + 20 * '-')

# Input string from user
string_input = input("Enter a string: ")
char_input = input("Enter a character to for in " + string_input + ": ")

print("The string " + string_input + " has " + str(string_input.count(char_input)) + " character " + char_input)

print(20 * '-' + 'End HW Q8.2' + 20 * '-')

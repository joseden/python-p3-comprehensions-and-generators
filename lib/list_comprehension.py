#!/usr/bin/env python3
def return_evens(num_list):
    # Create an empty list to store even numbers
    evens_list = [num for num in num_list if num % 2 == 0]
    return evens_list

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = return_evens(numbers)
print(result)


    
        
def make_exclamation(sentence_list):
    if not sentence_list:
        return []  
    
    exclamation_list = [sentence + '!' for sentence in sentence_list]
    
    return exclamation_list
sentences = ['I like computers!', 'I require coffee!', 'Live long and prosper!']
exclamation_result = make_exclamation(sentences)
print("Sentences with exclamation:", exclamation_result)

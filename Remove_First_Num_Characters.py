# Remove first n characters from a string

# pseudocode

# Define the function to remove chars up to number 
def remove_chars_up_to_number(input_str, number):
    return input_str[number:]

# Create an example and print it
original_string="Hindi ko na kaya ko to!"
result_string=remove_chars_up_to_number(original_string, 12)
print(result_string)
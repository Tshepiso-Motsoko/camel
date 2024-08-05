def camel_to_snake(camel_str):
    # Initialize an empty string to store the converted snake case string
    snake_str = ''

    # Iterate over each character in the camel case string
    for char in camel_str:
        # If the character is uppercase (except the first character), add an underscore
        # and convert the character to lowercase, then add it to the snake case string
        if char.isupper():
            snake_str += '_' + char.lower()
        else:
            # If the character is not uppercase, simply add it to the snake case string
            snake_str += char

    # Return the snake case string after converting the camel case input
    return snake_str

def main():
    # Prompt the user to enter a camel case variable name
    camel_case = input("camelCase: ")

    # Call the camel_to_snake function to convert the input to snake case
    snake_case = camel_to_snake(camel_case)

    # Print the resulting snake case variable name
    print("snake_case:", snake_case)

if __name__ == "__main__":
    main()

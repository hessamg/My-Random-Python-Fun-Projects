
# This function separates removes the nth 
# strings from the string until the length 
# of the string is less than n

def myFunc(string_input,n):
    if len(string_input) >= n:
        print(string_input)
        new_string = str()
        for i in range (len(string_input)):
            if i%n == n-1:
                print(string_input[i], end='', flush=True)
            else:
                new_string += string_input[i]
        string_input = new_string
        print()
        print()

        myFunc(string_input,n)
    else:
        print(string_input)

myFunc("abcdefg",3)
# program which takes a string and gets the first and last number of each line
def Trebuchet(textPath):
    read = open(textPath, "r")
    stack = []
    number = ""
    result = ""
    for line in read:
        for char in line:
            if char.isdigit():
                number += char
            if char == '\n':
                if(len(number) == 1):
                    result = number[0] + number[0]
                    number = ""
                    stack.append(result)
                    break
                elif(len(number) > 1):
                    result = number[0] + number[len(number)-1]
                    stack.append(result)
                    number = ""
                    break   
        if(len(number) == 1):
            result = number[0] + number[0]
            number = ""
            stack.append(result)
            break
        elif(len(number) > 1):
            result = number[0] + number[len(number)-1]
            stack.append(result)
            number = ""
            break   
    stack = [int(i) for i in stack]
    print(sum(stack))
    

# Test the function with some input data
Trebuchet('feed.txt')
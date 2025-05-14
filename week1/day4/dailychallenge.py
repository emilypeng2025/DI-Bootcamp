
#step 1
MATRIX = [
    ['7','i','i'],
    ['T','s','x'],
    ['h','%','?'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%']
]
message = ""
prev_was_space = False

for col in range(len(MATRIX[0])): #loop through each colomn, from left to right starting at index [0]
    for row in range(len(MATRIX)): #loop through each row (top to bottom) within the current colomn 
        char = MATRIX[row][col] #extract char according to the order of iteration at position [row][list]
        if char.isalpha(): #if the char extracted is a letter
            message += char #add it to the message string, which was empty created at the beginning
            prev_was_space = False 
        else:
            if not prev_was_space:
                message += " "
                prev_was_space = True
print(message)

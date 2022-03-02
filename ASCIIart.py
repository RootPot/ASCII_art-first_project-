letters = {' ':['     ','     ','     ','     ','     ','     ','     ']}
#This dict will hold all our letters
#I also added a 'space' character manually
#also if you want to add something that may have a blank line in the middle you
#will have to manually add it :(

with open('Letters.txt') as L:
    linenum= 0 
    #linenum will keep track of which line we are on in the file Letter.txt
    
    for line in L.readlines():
        linenum+=1
        
        if linenum==1:
            continue
        #skips first line (requirements in txt)
        #checks line for Char Key
        LinesKey=''
        for char in line:
            if char.isspace() == False:
                LinesKey=char
                break
        #This will check which 'key' (or letter if you perfer) the
        #line/row needs to be assigned to in the dict
        
        letters.setdefault(LinesKey,[]).append(line)
        #This adds the line/row to said key/letter

LetterInput= input('Type Away! You Egg!\n')
#input from user

LengthOfInput = len(str(LetterInput))
#checks the length of input

RowNum = 0
#keeps up with which row/line we are on in the code below

for num in range(7):
    #Each letter had a max of 7 rows/lines so we will run this 7 times for each row
    
    Row = letters[LetterInput[0]][RowNum].strip('\n')

    #First I made the variable Row so we can add on to it later,
    #of course the first row will start with the first character from the input.
    #So I set the letter input to 0 for the first character

    for CharNum in range(1, LengthOfInput):
        RowToAdd = letters[LetterInput[CharNum]][RowNum].strip('\n')
        #here we iterate through the character (skipping the first one as we set it above)
        
        Row += ' ' + RowToAdd
        #Adding the Row

    print(Row)  
    #This prints the individual row created above :)

    RowNum = RowNum+1 if RowNum!=7 else 0
    #since the max amount of rows/lines per letter is 7, once we reach that point we
    #reset it back to 0
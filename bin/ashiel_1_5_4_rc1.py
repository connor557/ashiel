import os
import sys
import string
import random
''' This chatbot will parrot/mimick verbatim any response to
a previous line of conversation. It is fully funtional granted
that the following in true.
--- a sub directory named '/memory/' exists...
--- inside this director a file named '@counts' exists, with 
line 1 and 2 of the file printed with only the integer 1. This 
will be created if it does not exist.
--- a text file with any name in /memory/ exists, granted that
all letters are lowercase, and the text file contains line
delimited responses no longer than 100 characters with the last
line of that file being a blank line. If this does not exist, a
crude file of this description will be created.

Any string entered as a response to the bot is striped and
lower cased. This bot will respond to you only if it has a
response memorized from a previous conversation. Expect a couple
hundred responded before a result will become visible.

Simply type 'quit' to restart the program.'''

# Reads lines from file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i

# Restarts program in windows os
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
            
# Creates memory if none exists
if not os.path.exists('memory'):
    os.makedirs('memory')
    counted = open('memory/@counts.txt', 'w')
    counted.write(str(1) + '\n')
    counted.write(str(1) + '\n')
    counted.close()
    
    filed = open('memory/hello.txt', 'w')
    filed.write('how is your day\n')
    filed.close()
    
# User Interface
filec = open('memory/@counts.txt', 'r')
flines = filec.readlines()
filec.close()

flines[0] = flines[0].strip('\n')
flines[1] = flines[1].strip('\n')
avg_max = int(flines[1])+0.0
avg_min = int(flines[0])
    
print ' ------------------------------------------------------------------------------'
print '       A.S.H.I.E.L - Ordered Testing - 0.5.4'
print ' ------------------------------------------------------------------------------'
print '                                                                 Dev Console   '
print '  ' + str(flines[0]) + ' Files Containing ' + str(flines[1]) + ' Responses [' + str(round(avg_max / avg_min,4)) + ' Per File]'
print ''

# Current user and string organization variables
usr_name = 'User'
cur_user = usr_name
prg_runn = True
cur_line = ''
prv_line = ''
cur_user = 'User'
round = 0

# While loop makes program run until closed
while prg_runn == True :
    prv_line = cur_line
    
    # Checks to see if user is the human one
    if cur_user == usr_name :
        
        ## Text Processing
        # The user will enter data
        cur_line = raw_input('  [' + str(cur_user) + ']: ')
        
        # Striping text from input
        x = "".join([c for c in cur_line if c in string.letters or c in string.whitespace or c in string.digits]) 
        x = x.lower()
        x = x.strip(' ')

        # Checks to see if line contains 'name' as an attempt to not remember converastion about names
        # Wordfind exists but is not used, this actually serves only that purpose
        if len(x) <= 100 and prv_line != '' and prv_line != 'my name is ashiel':
            z = list(x) # + ('_' * (99-len(x))))
            cur_line = ''.join(z[0:])
            wordfind = x.split(' ')
            
            same = False
            
            # If the user types 'quit' everything refreshes
            if cur_line == 'quit':
                os.system('cls')
                restart_program()
            
            # Checks to see if memory is equal to a line in the memory file
            if os.path.exists('memory/' + str(prv_line) +'.txt'):
            
                filec = open('memory/' + str(prv_line) +'.txt', 'r')
                flines = filec.readlines()
            
                for each in flines:
                    test = cur_line + '\n'
                    if test == each:
                        same = True
                    elif same == True:
                        break
                    else:
                        same = False
            
                filec.close()
             
            # String was not already in file, so it is being added and will count add 1 to the file and response counts
            if same == False:
            
                # If the file already exists, don't count a new file
                if os.path.exists('memory/' + str(prv_line) + '.txt') :
                    f = open('memory/' + str(prv_line) +'.txt', 'a')
                    f.write(str(cur_line) + '\n')
                
                    f.close()
            
                    counted = open('memory/@counts.txt', 'r+')
                    flines = counted.readlines()
                    flines[0] = flines[0].strip('\n')
                    flines[1] = flines[1].strip('\n')
                    counted.close()
                    counted = open('memory/@counts.txt', 'w')
                    counted.write(str(int(flines[0])) + '\n')
                    counted.write(str(int(flines[1])+1) + '\n')
                    counted.close()
                   
                # Count a new file and responses
                else:
                    f = open('memory/' + str(prv_line) +'.txt', 'a')
                    f.write(str(cur_line) + '\n')
                
                    f.close()
            
                    counted = open('memory/@counts.txt', 'r+')
                    flines = counted.readlines()
                    flines[0] = flines[0].strip('\n')
                    flines[1] = flines[1].strip('\n')
                    counted.close()
                    counted = open('memory/@counts.txt', 'w')
                    counted.write(str(int(flines[0])+1) + '\n')
                    counted.write(str(int(flines[1])+1) + '\n')
                    counted.close()
            
            # If it is the same, ignore all memory
            else:
                cur_user = 'ASHIEL'
        
        # This text has been saved to memory, and it is ASHIEL's turn to speak
        cur_user = 'ASHIEL'
        
    # Checks if user in bot
    elif cur_user == 'ASHIEL' :
    
        if round == 0 :
            round += 1
            bot_response = prv_line
        
        # If the user tries to talk about names, ASHIEL will say her name instead
        elif 'name' in cur_line:
            bot_response = 'my name is ashiel'
            
        # If no filename is equal to the human response, generate a random file and pick a random response in that file.
        elif not os.path.exists('memory/' + cur_line +'.txt'):
        
            good = False
            
            while good == False:
                bot_response = random.choice(os.listdir("memory/"))
                
                if '@' in bot_response:
                    good = False
                    
                else:
                    with open('memory/' + bot_response,'r') as inf:
                        lines = inf.readlines()
                        inf.close()
                    
                        y = "".join([c for c in lines[random.randint(0,file_len('memory/' + bot_response))] if c in string.letters or c in string.whitespace or c in string.digits])
                        bot_response = y
                        bot_response = bot_response.strip('\n')
                    
                    good = True
                    print ''
        
        # Otherwise, read the file
        else:
            with open('memory/' + cur_line +'.txt','r') as inf:
                lines = inf.readlines()
                inf.close()
                
            # Then pick a randomw response in that file
            y = "".join([c for c in lines[random.randint(0,file_len('memory/' + cur_line +'.txt'))] if c in string.letters or c in string.whitespace or c in string.digits])
            bot_response = y
            bot_response = bot_response.strip('\n')
        
        #Then print the selected response in both cases.
        print '  [' + str(cur_user) + ']: ' + str(bot_response) # [ASHIEL]: how are you doing today
        cur_line = bot_response
        cur_user = usr_name
        
    # User selection indent
    
# Program loop indent

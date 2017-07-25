import sys # For command lne arguments

global stack # Declare stack to keep track of nested indentation style
global tests # Use this if we everything is correct
global TAB_WIDTH
stack = [] # Declare an empty list
tests = [] # Empty list
TAB_WIDTH = int(sys.argv[2])
def appendToStack():
    stack.append(stack[len(stack) - 1] + TAB_WIDTH) # If we are in a nested style, then we need to add another TAB WIDTH (Which is 2 in this case)

def checkIndentation(whiteSpace, lNumber):
    match = (whiteSpace == stack[len(stack) - 1])
    if (match == True):
        tests.append(True)
    else:
        tests.append(False)
        print ("Incorrect indentation at line %d. You should have %d spaces, but you have %d spaces" % (lNumber, stack[len(stack) - 1], whiteSpace))

def parse(fileObject, startPoint, lineNumber):
    fileObject.seek(startPoint)
    lNumber = lineNumber
    while (stack != []):

        for l in fileObject:
            lNumber += 1
            if (l.find("{") != -1):
                appendToStack() # Found '{' so push new requirement onto the stack!
            else: # Check for actual indentation!
                if (l == '\n'):
                    continue # Don't care if it is just an empty line
                if (l.find("}") != -1):
                    stack.remove(stack[len(stack) - 1]) # Found matching '}' so pop from stack
                whiteSpace = 0
                for char in l:
                    if (char.isspace() == True): #Find trailing whitespaces to match with correct number of spaces
                        whiteSpace += 1
                    else:
                        break
                checkIndentation(whiteSpace, lNumber) # Check if whitespaces match
        stack.remove(stack[len(stack) - 1]) # Pop from stack

def main():
    fo = open(sys.argv[1], "r") # Create file Object to read in cpp file
    stack.append(0) # No spaces at the beginning!
    lineNumber = 0 # Keep track of line number to print out errors
    jumpOffset = 0 # To jump to the first occurence of a {
    for line in fo: # Initial parse
        lineNumber += 1
        jumpOffset += len(line)
        pos = line.find("{") # Find first occurence of a curly brace because we indent from here!
        if (pos != -1):
            appendToStack() # Append
            break
    parse(fo, jumpOffset, lineNumber)
    if (False not in tests):
        print ("Everything is indented correctly!")

main()

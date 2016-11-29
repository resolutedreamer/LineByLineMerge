'''
LineByLineMerge.py
FILE_MODE = 0
For the files in the same folder as this script, perform a TopBottomMerge on the files that match 'expression'
FILE_MODE = 1
For the files passed in at the commandline, perform a TopBottomMerge on those files
PROCESS_MODE = 0
Perform a line by line merge with lines seperated by seperator
PROCESS_MODE = 1
Perform a top bottom merge
'''
import sys
import os
FILE_MODE = 0
PROCESS_MODE = 0
expression = ''
seperator = ''

def main():
    fileHandlers = []
    fileNames = []
    foundFileNames = []
    
    if FILE_MODE == 0:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            print f
            if f.find(expression) != -1:
                foundFileNames.append(f)
        for argument in foundFileNames:
            try:
                f = open(argument, 'r+')
                fileHandlers.append(f)
                print f.closed
            except:
                print "open " + argument + "failed"
    elif FILE_MODE == 1:
        print "no files matching 'expression' found, checking passed in arguments"
        if len(sys.argv) < 2:
            print "Not enough args"
            sys.exit(1)
        else:
            print str(len(sys.argv)) + " arguments"
            # remove the path to this python file
            sys.argv.pop(0)
        
        print fileNames
        # open all the files given to argv    
        for argument in sys.argv:
        try:
            f = open(argument, 'r+')
            fileHandlers.append(f)
            print f.closed
        except:
            print "open " + argument + "failed"
    if PROCESS_MODE == 0:
        line_by_line_merge(fileHandlers)
    elif PROCESS_MODE == 1:
        top_bottom_merge(fileHandlers)
    return 0

def top_bottom_merge(fileHandlers):
    filename = 'merged_' + sys.argv[0]
    with open(filename, 'w+') as out:
        print "Writing to " + filename
        for handler in fileHandlers:    
            for line in handler:
                out.write(line)
            out.write('\n\n')
        # manually close other files when done
        for handler in fileHandlers:
            handler.close()

def line_by_line_merge(fileHandlers):
    # closes 'out' automatically
    filename = 'merged_' + sys.argv[0]
    with open(filename, 'w+') as out:
        exitFlag = True
        i = 1
        while(exitFlag):
            print "Appending row " + str(i)
            for index, handler in enumerate(fileHandlers):
                # get just one row from each file
                currentLine = handler.readline()
                if not currentLine:
                    # determined by shortest file
                    exitFlag = False
                    break
                else:
                    # need to remove the newlines
                    currentLine = currentLine.rstrip()
                    print currentLine
                    out.write(currentLine)
                    if index == 0:
                        out.write(seperator)
            # add a newline to indicate done with row
            if exitFlag:
                out.write('\n')
            i += 1
        # manually close other files when done
        print "out of while loop"
        for handler in fileHandlers:
            handler.close()


if __name__ == "__main__":
    main()
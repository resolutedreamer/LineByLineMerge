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
PROCESS_MODE = 2
Extract lines that come after lines starting with 'start'
'''
import sys
import os
FILE_MODE = 0
PROCESS_MODE = 0
expression = ''
seperator = ''
start = ''

def main():
    fileHandlers = []
            
    if FILE_MODE == 0:
        foundFileNames = []
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
        output_filename = 'merged_' + files[0]
    elif FILE_MODE == 1:
        fileNames = []
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
        line_by_line_merge(fileHandlers, output_filename)
    elif PROCESS_MODE == 1:
        top_bottom_merge(fileHandlers, output_filename)
    elif PROCESS_MODE == 2:
        extract_subsequent_line(fileHandlers, output_filename)
    return 0

def extract_subsequent_line(fileHandlers, output_filename):
    output_this = False
    with open(output_filename, 'w+') as out:
        print "Writing to " + output_filename
        for handler in fileHandlers:
            for line in handler:
                if output_this:
                    out.write(line)
                    output_this = False
                else:
                    if line.startswith(start):
                        # next line
                        output_this = True
    

def top_bottom_merge(fileHandlers, output_filename):
    with open(output_filename, 'w+') as out:
        print "Writing to " + output_filename
        for handler in fileHandlers:    
            for line in handler:
                out.write(line)
            out.write('\n\n')
        # manually close other files when done
        for handler in fileHandlers:
            handler.close()

def line_by_line_merge(fileHandlers, output_filename):
    with open(output_filename, 'w+') as out:
        print "Writing to " + output_filename
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
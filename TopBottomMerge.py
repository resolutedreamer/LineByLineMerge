'''
TopBottomMerge.py

Can be used two ways:
1. For the files in the same folder as this script, perform a TopBottomMerge on the files that match 'expression'
2. For the files passed in at the commandline, perform a TopBottomMerge on those files
'''
import sys
import os
expression = ''

def main():
    fileHandlers = []
    fileNames = []
    foundFileNames = []

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        print f
        if f.find(expression) != -1:
            foundFileNames.append(f)
    if (len(foundFileNames) == 0):
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
    else:
        for argument in foundFileNames:
            try:
                f = open(argument, 'r+')
                fileHandlers.append(f)
                print f.closed
            except:
                print "open " + argument + "failed"

    # closes 'out' automatically
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
    
if __name__ == "__main__":
    main()
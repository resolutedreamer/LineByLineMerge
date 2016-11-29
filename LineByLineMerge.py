##
import sys
seperator = ''

def main():
    fileHandlers = []
    if len(sys.argv) < 2:
        print "Not enough args"
        sys.exit(1)
    else:
        print str(len(sys.argv)) + " arguments"
        # remove the path to this python file
        sys.argv.pop(0)
    
    # open all the files given to argv    
    for argument in sys.argv:
        try:
            f = open(argument, 'r+')
            fileHandlers.append(f)
            print f.closed
        except:
            print "open " + argument + "failed"

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
        return 0
    
if __name__ == "__main__":
    main()
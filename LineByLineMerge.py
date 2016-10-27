import sys

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
    with open('output.txt', 'w') as out:
        exitFlag = True
        i = 1
        while(exitFlag):
            print "Appending row " + str(i)
            for handler in fileHandlers:
                # get just one row from each file
                currentLine = handler.readline()
                if not currentLine:
                    # determined by shortest file
                    exitFlag = False
                    break
                print currentLine
                # need to remove the newlines
                currentLine = currentLine.rstrip('\n')
                print currentLine
                out.write(currentLine)
            # add a newline to indicate done with row
            out.write('\n')
            i += 1
        # manually close other files when done
        for handler in fileHandlers:
            handler.close()
    
if __name__ == "__main__":
    main()
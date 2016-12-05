'''
LineByLineMerge.py
'''
import sys
import os

FILE_MODE = 0
PROCESS_MODE = 0
expression = ''
seperator = ''
start = ''


class TxtFileProcessor:
    def __init__(self):
        self.filePaths = []
        self.output_filename = "output.txt"

    def load_from_folder(self, expression, folder_path):
        print os.listdir(folder_path)
        all_files = [f for f in os.listdir(folder_path) if os.path.isfile((folder_path + f))]
        all_file_paths = [folder_path + file_name for file_name in all_files]
        for f in all_file_paths:
            if f.find(expression) != -1:
                self.filePaths.append(f)
        self.output_filename = 'merged_' + all_files[0]
        return len(self.filePaths)
        
    def load_from_args(self):
        fileNames = []
        if len(sys.argv) < 2:
            print "Not enough args"
            sys.exit(1)
        else:
            print str(len(sys.argv)) + " arguments"
            # remove the path to this python file
            sys.argv.pop(0)
        
        print fileNames
        # put argv arguments into filePaths
        for argument in sys.argv:
            self.filePaths.append(argument)
        self.output_filename = 'merged_' + sys.argv[0]
        return len(self.filePaths)
    
    def unload(self):
        self.filePaths = []
        self.output_filename = "output.txt"
    
    def extract_subsequent_line(self, start):
        fileHandlers = []
        output_this = False
        with open(self.output_filename, 'w+') as out:
            print "Writing to " + self.output_filename
            for argument in self.filePaths:
                try:
                    f = open(argument, 'r+')
                    fileHandlers.append(f)
                    print f.closed
                except:
                    print "open " + argument + "failed"
            for handler in fileHandlers:
                for line in handler:
                    if output_this:
                        out.write(line)
                        output_this = False
                    else:
                        if line.startswith(start):
                            # get next line
                            output_this = True
        
    
    def top_bottom_merge(self):
        fileHandlers = []
        with open(self.output_filename, 'w+') as out:
            print "Writing to " + self.output_filename
            for argument in self.filePaths:
                try:
                    f = open(argument, 'r+')
                    fileHandlers.append(f)
                except:
                    print "open " + argument + "failed"
            print fileHandlers
            for handler in fileHandlers:
                fileContents = handler.read()
                print fileContents
                out.write(fileContents)
                out.write('\n')
    
    def line_by_line_merge(self, seperator = ''):
        fileHandlers = []
        exitFlag = True
        i = 1
        with open(self.output_filename, 'w+') as out:
            print "Writing to " + self.output_filename
            for argument in self.filePaths:
                try:
                    f = open(argument, 'r+')
                    fileHandlers.append(f)
                except:
                    print "open " + argument + "failed"
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

if __name__ == "__main__":
    myProcessor = TxtFileProcessor()
    if FILE_MODE == 0:
        myProcessor.load_from_folder(expression)
    elif FILE_MODE == 1:
        myProcessor.load_from_args()
    if PROCESS_MODE == 0:
        myProcessor.line_by_line_merge(seperator)
    elif PROCESS_MODE == 1:
        myProcessor.top_bottom_merge()
    elif PROCESS_MODE == 2:
        myProcessor.extract_subsequent_line(start)
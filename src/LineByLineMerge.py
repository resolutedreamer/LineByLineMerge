'''
LineByLineMerge.py
'''
import sys
import os
import codecs


FILE_MODE = 0
PROCESS_MODE = 0

class TxtFileProcessor:
    def __init__(self):
        self.filePaths = []
        self.output_filename = "output.txt"

    def load_from_folder_tree(self, expression = '.txt', folder_path = './'):
        self.filePaths = [os.path.join(root, name)
                    for root, dirs, files in os.walk(folder_path)
                    for name in files
                    if (name.find(expression) != -1)]
        return len(self.filePaths)

    def load_from_folder(self, expression = '.txt', folder_path = './'):
        print os.listdir(folder_path)
        all_files_in_folder = [f for f in os.listdir(folder_path) if os.path.isfile((folder_path + f))]
        all_files_matching = [f for f in all_files_in_folder if f.find(expression) != -1]
        all_file_paths = [folder_path + file_name for file_name in all_files_matching]
        for f in all_file_paths:
            self.filePaths.append(f)
        self.output_filename = all_files_matching[0]
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
        self.output_filename = sys.argv[0]
        return len(self.filePaths)
    
    def extract_subsequent_line(self, start = ''):
        if len(self.filePaths) == 0:
            raise Exception("No files loaded")
        fileHandlers = []
        self.output_filename = 'xtracted_' + self.output_filename
        output_this = False
        with codecs.open(self.output_filename, 'w+') as out:
            print "Writing to " + self.output_filename
            for argument in self.filePaths:
                try:
                    f = codecs.open(argument, 'r+')
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
        if len(self.filePaths) == 0:
            raise Exception("No files loaded")
        fileHandlers = []
        self.output_filename = 'merged_' + self.output_filename
        with codecs.open(self.output_filename, 'w+') as out:
            print "Writing to " + self.output_filename
            for argument in self.filePaths:
                try:
                    f = codecs.open(argument, 'r+')
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
        if len(self.filePaths) == 0:
            raise Exception("No files loaded")
        fileHandlers = []
        self.output_filename = 'merged_' + self.output_filename
        exitFlag = True
        i = 1
        with codecs.open(self.output_filename, 'w+') as out:
            print "Writing to " + self.output_filename
            for argument in self.filePaths:
                try:
                    f = codecs.open(argument, 'r+')
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

    def unload(self):		
        self.filePaths = []		
        self.output_filename = "output.txt"

if __name__ == "__main__":
    path = './'
    if len(sys.argv) == 2:
        path = sys.argv[1]
    expression = ''
    start = ''
    myProcessor = TxtFileProcessor()
    if FILE_MODE == 0:
        myProcessor.load_from_folder(expression, path)
    elif FILE_MODE == 1:
        myProcessor.load_from_folder_tree(expression, path)
    elif FILE_MODE == 2:
        myProcessor.load_from_args()
    if PROCESS_MODE == 0:
        myProcessor.line_by_line_merge()
    elif PROCESS_MODE == 1:
        myProcessor.top_bottom_merge()
    elif PROCESS_MODE == 2:
        myProcessor.extract_subsequent_line(start)
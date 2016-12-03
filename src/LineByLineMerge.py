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
    fileHandlers = []
    output_filename = "output.txt"

    def unload(self):
        for handler in self.fileHandlers:
            handler.close()

    def load_from_folder(self, expression, folder_path):
        matching_file_paths = []
        print os.listdir(folder_path)
        all_files = [f for f in os.listdir(folder_path) if os.path.isfile((folder_path + f))]
        all_file_paths = [folder_path + file_name for file_name in all_files]
        for f in all_file_paths:
            print f
            if f.find(expression) != -1:
                matching_file_paths.append(f)
        for argument in matching_file_paths:
            try:
                f = open(argument, 'r+')
                self.fileHandlers.append(f)
                print f.closed
            except:
                print "open " + argument + "failed"
        self.output_filename = 'merged_' + all_file_paths[0]
        return len(self.fileHandlers)
        
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
        # open all the files given to argv
        for argument in sys.argv:
            try:
                f = open(argument, 'r+')
                self.fileHandlers.append(f)
                print f.closed
            except:
                print "open " + argument + "failed"
        self.output_filename = 'merged_' + sys.argv[0]
        return len(self.fileHandlers)
    
    def extract_subsequent_line(self, start):
        output_this = False
        with open(self.output_filename, 'w+') as out:
            print "Writing to " + self.output_filename
            for handler in self.fileHandlers:
                for line in handler:
                    if output_this:
                        out.write(line)
                        output_this = False
                    else:
                        if line.startswith(start):
                            # next line
                            output_this = True
        self.unload()
        
    
    def top_bottom_merge(self):
        with open(self.output_filename, 'w+') as out:
            print "Writing to " + self.output_filename
            for handler in self.fileHandlers:    
                for line in handler:
                    out.write(line)
                out.write('\n\n')
            # manually close other files when done
        self.unload()
    
    def line_by_line_merge(self, seperator):
        with open(self.output_filename, 'w+') as out:
            print "Writing to " + self.output_filename
            exitFlag = True
            i = 1
            while(exitFlag):
                print "Appending row " + str(i)
                for index, handler in enumerate(self.fileHandlers):
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
            self.unload()
    

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
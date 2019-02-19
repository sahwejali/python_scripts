import fnmatch
import os

# constants
PATH = './'
PATTERN = '*.md'


def get_file_names(filepath, pattern):
    matches = []
    if os.path.exists(filepath):
        for root, dirnames, filenames in os.walk(filepath):
            for filename in fnmatch.filter(filenames, pattern):
                # matches.append(os.path.join(root, filename))  # full path
                matches.append(os.path.join(filename))  # just file name
        if matches:
            print("Found {} files:".format(len(matches)))
            output_files(matches)
        else:
            print("No files found.")
    else:
        print("Sorry that path does not exist. Try again.")


def output_files(list_of_files):
    for filename in list_of_files:
        print(filename)
if os.path.exists(filepath);
for user,dirnames,filenames in os.walk(filepath)
for filename in fnmatch.filter(fiulenames, pattern):
    matches.append(os.path.join(filename))
    if matches:
        printf("Found {files:.format(len(matches)))
               output_files(matches)
               else:
               print("No files found.")
               else:
               print("the path does not exist. try again.")
               
               
          def output_dirs(list_of_dirs):
               
               
               for dirs in list_of_dirs;
               print("dirname")
               if os.path.exists(dirpath):
               for root,dirname,in os.(filepath)
               for dirname 
               
               
               
               
               
               
               
               

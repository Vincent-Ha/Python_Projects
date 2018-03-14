# Project 1
# Name: Vincent Ha                  Student ID: 14788488
# Name: Uuganbayar Temuujin         Student ID: 12803733


from pathlib import Path
import os
import shutil

# Comparators
# -----------
# The comparators help narrow down the files that the user wants to look at
# according to certain criteria.


def allow_all_files(file : Path, information_key : str) -> bool:
# This function shows that all files are of interest to the user
    return True

def name_comparison(file : Path, information_key : str) -> bool:
# This function searches for files with the same name as what the user typed in.
    return file.name == information_key

def extension_comparison(file : Path, information_key : str) -> bool:
# This function searches for files with a certain extension that the user typed
# in.
    return file.suffix == information_key

def text_search(file : Path, information_key : str) -> bool:
# This function looks for files that can be read and contain text provided by
# the user.  
    if file.is_dir():
        return False
    
    text = file.open('r')
    try:
        for line in text:
            if information_key in line:
                return True
        return False
    except UnicodeDecodeError:
        return False
    finally:
        text.close()

def less_than_byte_comparison(file : Path, information_key : str) -> bool:
# This function searches for files and directories with a byte size less than
# what the user has given.
    return os.path.getsize(file) < information_key

def greater_than_byte_comparison(file : Path, information_key : str) -> bool:
# This function searches for files and directories with a byte size greater than
# what the user has given
    return os.path.getsize(file) > information_key


# The dictionary is what is used to determine which of the comparator functions
# will be used after obtaining the input from the user.
comparison_dict = { 'A' : allow_all_files, 'N' : name_comparison,
                    'E' : extension_comparison, 'T' : text_search,
                    '<' : less_than_byte_comparison,
                    '>' : greater_than_byte_comparison}



# Modifiers
# ---------
# The modifiers are the functions that are performed once the user narrows down
# what files and directories they want to work with.


def print_first_lines(file_list : list) -> None:
# This function opens and reads files. It then prints the first line of each
# file it is able to read
    for file in file_list:
        if file.is_file():
            text = file.open('r')
            try:
               print(text.readline(), end = '')
            except UnicodeDecodeError:
                print('NOT TEXT')
            finally:
                text.close()

def duplicate_files(file_list : list) -> None:
# This function duplicates files and adds the .dup extension to the copies
    for file in file_list:
        if file.is_file():
            shutil.copyfile(file, Path(str(file) + '.dup'))
        else:
            print('NOT TEXT')

def change_timestamp(file_list : list) -> None:
# This function changes the timestamp on files to the current time when this
# function is used.
    for file in file_list:
        os.utime(f3ile)

# This dictionary dictates the function used based on the input of the user
modifier_dict = { 'F' : print_first_lines, 'D' : duplicate_files,
                  'T' : change_timestamp }



# Lexiographical Sorting Method
# ------------------------------

def path_ordering(paths : list) -> list:
# This function uses a simple lambda expression to sort the paths in the correct
# order. The order is primarily based on the number of "parents" within the path
# and secondily by lexiographic order. The fewer the number of parents, the
# further up the files go on the list.
    sorted_paths = sorted(paths, key = lambda x : len(x.parents))
    return sorted_paths



# Main Functions
# --------------
# These functions are the main functions that are called by the UI function.


def input_handling(key_characters: list) -> tuple:
# Function handles user input. Checks for general input format correctness and
# raises an exception if not in proper form

    user_input = input() + ''
    first_choice = user_input[0]
    second_choice = user_input[2:]
    
    # This is a special case in that A does not require other inputs other than
    # the initial A. This case tells the program that all files found are of
    # interest
    if first_choice == 'A':
        if (len(second_choice) == 0):
            return (first_choice, '')
        else:
            raise ValueError('Incorrect input')

    if (second_choice == '' or not user_input[1] == ' '
        or first_choice not in key_characters):
        raise ValueError('Incorrect input')
    
    return (first_choice, second_choice)

def list_paths(path_of_interest : Path, recursion_key : str,
               method_key : str = 'A', information_key : str = '') -> list:
# This function complies a list of Paths based on constraints given by the user.
# These constraints include whether to use the files within the sub-directories
# and the circumstances in which the comparators from the functions above would
# be used

    if not path_of_interest.exists():
        raise FileNotFoundError('Path does not exist')

    paths = []
    path_iter = path_of_interest.iterdir()
    for file in path_iter:
        if file.is_dir():
            if recursion_key == 'R':
                # Looks if the files in the subdirectories would be considered
                paths.extend(list_paths(file, recursion_key, method_key,
                                        information_key))
        else:
            if comparison_dict[method_key](file, information_key):
                paths.append(file)
    return paths



# UI Functions
# ------------
# Functions that handle the user interface


def uI_list_paths() -> tuple:
# This function handles the initial listing of files from a path specified
# by the user. It also determines whether or not the files within the
# subdirectories should be considered.
    choices = tuple()
    # The loops continues until the proper input is given by the user.
    while(choices == ()):
        try:
            choices = input_handling(['D', 'R'])
            recursive_key = choices[0]
            path_of_interest = Path(choices[1])
            paths = list_paths(path_of_interest, recursive_key)
        except FileNotFoundError:
            choices = ()
            print('ERROR')
        except ValueError:
            choices = ()
            print('ERROR')

    # The lists are sorted then printed onto the console screen.
    ordered_paths = path_ordering(paths)
    
    for path in ordered_paths:
        print(path)
     
    return (path_of_interest, recursive_key)
        # Returns the necessary path and directory choice required for the
        # program to continue.
                            
def uI_narrow_done_list(path_of_interest : Path, recursive_key : str) -> list:
# The function narrows down the files to a list of ones that the user has
# interest in.
    filter_choice = tuple()
    while (filter_choice == ()):
        try:
            filter_choice = input_handling(['A', 'N', 'E', 'T', '<', '>'])
            if (filter_choice[0] == '<' or filter_choice[0] == '>'):
                information_key = int(filter_choice[1])
            elif (filter_choice[0] == 'E' and not filter_choice[1][0] == '.'):
                information_key = '.' + filter_choice[1]
            else:
                information_key = filter_choice[1]
                  
            paths = list_paths(path_of_interest, recursive_key,
                               filter_choice[0], information_key)
        except FileNotFoundError:
            filter_choice = ()
            print('ERROR')
        except ValueError:
            filter_choice = ()
            print('ERROR')

    ordered_paths = path_ordering(paths)
    
    for path in ordered_paths:
        print(path)

    return ordered_paths 
        # Returns the paths that the program has narrow the list down to.
        
def uI_modify_paths(path_list : list) -> None:
# This function handles the last part of the function where the files of
# interest are modified according to the user. If there are no files of
# interest, the function will not run.
    if not len(path_list) == 0:
        modify_choice = ''
        possible_choices = ['F', 'D', 'T']
        while(modify_choice == ''):
            modify_choice = input()
            if (not len(modify_choice) == 1 or
                modify_choice not in possible_choices):
                print('ERROR')
                modify_choice = ''
                
        modifier_dict[modify_choice](path_list)           

def uI_run():
# This function encapsulates all the UI functions that run within this program
# into a single function
    path_and_recursive_key = uI_list_paths()
    path_list = uI_narrow_done_list(path_and_recursive_key[0],
                                    path_and_recursive_key[1])
    uI_modify_paths(path_list)

    
# "Main" 
if __name__ == '__main__':
  uI_run()

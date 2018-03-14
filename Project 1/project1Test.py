from pathlib import Path

def _get_input() -> str:

    while True:
        checked_list = _check_input()
        _print(checked_list)
        checked_list_2 = _check_input_2(checked_list)
        _print(checked_list_2)
    return

def _check_input() -> list:
    while True:
        user_input = input("1:")
        if user_input[:2] == "R ":
            return _file_global(user_input[2:])
        elif user_input[:2] == "D ":
            return _file_directory(user_input[2:])
        else:
            pass
        
def _check_input_2(list_of_files:list) -> list:
    while True:
        user_input = input("2:")
        if user_input == "A":
            pass
        elif user_input[:2] == "N ":
            return _search_exactly(list_of_files,user_input[2:])
        elif user_input[:2] == "E ":
            return _search_desired_extension(list_of_files,user_input[2:])
        elif user_input[:2] == "T ":
            return _search_text_file(list_of_files,user_input[2:])
        elif user_input[:2] == "< ":
            return _search_size_less(list_of_files,int(user_input[2:]))
        elif user_input[:2] == "> ":
            return _search_size_more(list_of_files,int(user_input[2:]))
        else:
            print("File 2 Chine Alga")

def _file_directory(x:str) -> list:
    try:
        path = Path(x)
        if path.exists() == True:
            return list(path.iterdir())
        else:
            print("File doesn't exist _file_directory")
    except:
        print("File is not here")

def _file_global(x:str) -> list:
    try:
        path = Path(x)
        if path.exists() == True:
            return list(path.glob("**/*"))
        else:
            print("File doesn't exist")
    except:
        print("File is not here")
        
def _print(files:list) -> None:
    try:
        for file in sorted(files):
            print(file)
    except:
        print("Yuuch Bolhq bn Lalara")

def _search_exactly(files:list,name:str) -> list:
    match = []
    for file in files:
        if file.parts[-1] == name:
            match.append(file)
    return match

def _search_desired_extension(files:list,extension:str) -> list:
    match = []
    if extension.startswith(".") == False:
        extension = "." + extension
    length_extension = len(extension)
    for file in files:
        try:
            if file.parts[-1][-length_extension:] == extension:
                match.append(file)
        except:
            pass
    return match

def _search_text_fil(files:list,text:str) -> list:
    the_file = None
    match = []
    try:
        for file in files:
            the_file = open(file,"r")
            for line in the_file:
                if text in line:
                    match.append(file)
        return match
    except UnicodeDecodeError:
            pass
    finally:
        if the_file != None:
            the_file.close()
            
def _search_text_file(files:list,text:str) -> list:
    the_file = None
    match = []
    for file in files:
        try:
            the_file = open(file,"r")
            for line in the_file:
                if text in line:
                    match.append(file)
        except:
            pass
        finally:
            if the_file != None:
                the_file.close()
    return match
            
def _search_size_less(files:list,size:int) -> list:
    match = []
    for file in files:
        if file.stat().st_size<size:
            match.append(file)
    return match

def _search_size_more(files:list,size:int) -> list:
    match = []
    for file in files:
        if file.stat().st_size>size:
            match.append(file)
    return match

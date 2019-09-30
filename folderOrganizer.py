from pathlib import Path

# Find directory
def findDirectory()->Path:
    '''Returns directory'''
    pathInput = input("Enter folder directory: ")
    path = Path(pathInput)

    if path.exists() == False or not path.is_dir():
        print("Directory not found!")
        findDirectory()
    else:
        print("Directory Found!\n")
    
    return path

# Organizes a specified file type within a directory
def organizeByOneType(p: Path):
    '''Takes user desired file type to group and organize within directory'''
    fileType = input("\nEnter file type to organize (EX: pdf): ")

    print("ORGANIZING...")

    fileType = "." + fileType

    newPath = p.joinpath(fileType)

    ''' CHANGE LATER TO MAKE A NEW FILE WITH INDEX '''
    newPath.mkdir(exist_ok = True)
    
    for file in p.iterdir():
        if file.suffix == fileType:
            file.rename(newPath.joinpath(file.name))

    print("ORGANIZATION DONE")

# Organizes all file types within a directory
def organizeByAllTypes(p: Path):
    '''Organizes all files within directory by file type'''
    print("ORGANIZING...")
    
    for file in p.iterdir():
        newPath = p.joinpath(file.suffix)
        ''' CHANGE LATER TO MAKE A NEW FILE WITH INDEX '''
        newPath.mkdir(exist_ok = True)
        file.rename(newPath.joinpath(file.name))

    print("ORGANIZATION DONE")

# Organizes all files with specified name
def organizeByName(p: Path):
    '''Organizes files within directory by specified name'''
    fileName = input("\nEnter file name to organize by: ")
    
    print("ORGANIZING...")

    newPath = p.joinpath(fileName)
    
    ''' CHANGE LATER TO MAKE A NEW FILE WITH INDEX '''
    newPath.mkdir(exist_ok = True)
    
    for file in p.iterdir():
        if fileName in file.name and Path(file) != newPath:
            file.rename(newPath.joinpath(file.name))

    print("ORGANIZATION DONE")
    
if __name__ == '__main__':
    path = findDirectory()

    ''' ADD RECURSIVE OPTION TO GO THROUGH ALL DIRECTIORIES WITHIN A DIRECTORY '''
    
    print("CHOOSE ORGANIZATION TYPE")
    print("(1) Organize one file type")
    print("(2) Organize all file types")
    print("(3) Organize by specified name")

    conventionChoice = input("\nEnter organization type: ")

    if conventionChoice == "1":
        organizeByOneType(path)
    elif conventionChoice == "2":
        organizeByAllTypes(path)
    elif conventionChoice == "3":
        organizeByName(path)

from pathlib import Path

# Find directory
def findDirectory()->Path:
    '''Returns directory'''
    pathInput = input("Enter folder directory: ")
    path = Path(pathInput)

    if path.exists() == False or not path.is_dir():
        print("Directory not found!")
        findDirectory()
        
    print("Directory Found!\n")
    
    return path

# Organizes a specified file type within a directory
def organizeByOneType(p: Path):
    '''Takes user desired file type to group and organize within directory'''
    fileType = input("\nEnter file type to organize (EX: pdf): ")

    print("ORGANIZING...")

    tempPath = p

    newPath = tempPath.joinpath(fileType)

    ''' CHANGE LATER TO MAKE A NEW FILE WITH INDEX '''
    newPath.mkdir(exist_ok = True)
    
    fileType = "." + fileType
    
    for file in p.iterdir():
        if file.suffix == fileType:
            file.rename(newPath.joinpath(file.name))

    print("ORGANIZATION DONE")
    
if __name__ == '__main__':
    path = findDirectory()
    
    print("CHOOSE ORGANIZATION TYPE")
    print("(1) Organize one file type")
    print("(2) Organize all file types")
    print("(3) Organize by name")

    conventionChoice = input("\nEnter organization type: ")

    if conventionChoice == "1":
        organizeByOneType(path)
    '''elif conventionChoice == "2":
        organizeByAllTypes(path)
    elif conventionChoice == "3":
        organizeByName(path)'''

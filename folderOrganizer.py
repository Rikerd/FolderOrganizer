from pathlib import Path

# Find directory
def findDirectory()->Path:
    '''Returns directory'''
    pathInput = input("Enter folder directory: ")
    path = Path(pathInput)

    if path.exists() == False or not path.is_dir():
        print("Directory not found!")
        return findDirectory()
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
        if file.suffix.lower() == fileType:
            file.rename(newPath.joinpath(file.name))

    print("ORGANIZATION DONE")

# Organizes all file types within a directory
def organizeByAllTypes(p: Path):
    '''Organizes all files within directory by file type'''
    print("ORGANIZING...")
    
    for file in p.iterdir():
        newPath = p.joinpath(file.suffix.lower())
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

# Organizes all image files into a folder
def organizeImages(p: Path):
    '''Organizes files within directory by image file types'''
    imageFileTypes = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"]
    
    print("ORGANIZING...")

    newPath = p.joinpath("Pictures")
    ''' CHANGE LATER TO MAKE A NEW FILE WITH INDEX '''
    newPath.mkdir(exist_ok = True)
    
    for file in p.iterdir():
        if (file.suffix.lower() in imageFileTypes):
            file.rename(newPath.joinpath(file.name))

    print("ORGANIZATION DONE")

# Organizes all video files into a folder
def organizeVideos(p: Path):
    '''Organizes files within directory by video file types'''
    videoFileTypes = [".mkv", ".flv", ".ogg", ".avi", ".mov", ".wmv", ".mp4", ".mpg", ".m4v", ".svi", ".mkv"]
    
    print("ORGANIZING...")

    newPath = p.joinpath("Videos")
    ''' CHANGE LATER TO MAKE A NEW FILE WITH INDEX '''
    newPath.mkdir(exist_ok = True)
    
    for file in p.iterdir():
        if (file.suffix.lower() in videoFileTypes):
            file.rename(newPath.joinpath(file.name))

    print("ORGANIZATION DONE")

# Organizes all music files into a folder
def organizeMusic(p: Path):
    '''Organizes files within directory by music file types'''
    musicFileTypes = [".aa", ".aac", ".aax", ".flac", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".voc", ".vox", ".wav", ".wma", ".wv"]
    
    print("ORGANIZING...")

    newPath = p.joinpath("Music")
    ''' CHANGE LATER TO MAKE A NEW FILE WITH INDEX '''
    newPath.mkdir(exist_ok = True)
    
    for file in p.iterdir():
        if (file.suffix.lower() in musicFileTypes):
            file.rename(newPath.joinpath(file.name))

    print("ORGANIZATION DONE")

# Select desired organization type
def selectOrganizationType(p: Path):
    '''ADD RECURSION'''
    
    print("CHOOSE ORGANIZATION TYPE")
    print("(1) Organize one file type")
    print("(2) Organize all file types")
    print("(3) Organize by specified name")
    print("(4) Organize all images")
    print("(5) Organize all videos")
    print("(6) Organize all musics")
    
    conventionChoice = input("\nEnter organization type: ")

    if conventionChoice == "1":
        organizeByOneType(p)
    elif conventionChoice == "2":
        organizeByAllTypes(p)
    elif conventionChoice == "3":
        organizeByName(p)
    elif conventionChoice == "4":
        organizeImages(p)
    elif conventionChoice == "5":
        organizeVideos(p)
    elif conventionChoice == "6":
        organizeMusic(p)
    else:
        print("INVALID INPUT\n")
        selectOrganizationType(p)
    
if __name__ == '__main__':
    path = findDirectory()

    selectOrganizationType(path)
    
    

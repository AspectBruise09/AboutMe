# Add Letter Contain specificationOfCube Values To Get Better Result And Selecting Accesibility
import math


specificationOfCube = input("Which Of The Specification Of The Cube Do You Know Now:? [1. Length Of Side | 2. Volume | 3. None | 4. Other] --> ")
additionalVolume = input("Enter The Additional Volume / CM³ --> ")
while True:
    try:
        additionalVolume = float(additionalVolume)
        break
    except ValueError:
        print("You should use a number, not a string or letters")
        additionalVolume = input("Enter The Additional Volume / CM³ --> ")
while specificationOfCube == "None":
    print("Please get one of the specifications")
    specificationOfCube = input("Which Of The Specification Of The Cube Do You Know Now:? [1. Length Of Side | 2. Volume | 3. None | 4. Other] --> ")
while specificationOfCube == "Other":
    print("Please get one of the specifications")
    specificationOfCube = input("Which Of The Specification Of The Cube Do You Know Now:? [1. Length Of Side | 2. Volume | 3. None | 4. Other] --> ")
while specificationOfCube in ["Length Of Side", "Volume", "None", "Other"] == False: ##########
    print("Please Choose One Of These")
    specificationOfCube = input("Which Of The Specification Of The Cube Do You Know Now(I Will Add More Options Soon..!):? [1. Length Of Side | 2. Volume | 3. None | 4. Other] --> ")
if specificationOfCube == "Length Of Side":
    lengthOfSide = input("Enter The Length Of The Side Of The Cube / CM --> ")
    while True:
        try:
            lengthOfSide = float(lengthOfSide)
            break
        except ValueError:
            print("You should use a number, not a string or letters")
            lengthOfSide = input("Enter The Length Of The Side Of The Cube / CM --> ")
    volumeOfSide = additionalVolume / 6
    length = round(lengthOfSide, 1)
    width = round(lengthOfSide, 1)
    heigth = round(volumeOfSide / (length * width), 1) 
    print(f"Length = {length} | Width  = {width} | Height = {heigth}")
if specificationOfCube == "Volume":
    volumeOfCube = input("Enter The Volume Of The Cube / CM³ --> ")
    while True:
        try:
            volumeOfCube = float(volumeOfCube)
            break
        except ValueError:
            print("You should use a number, not a string or letters")
            volumeOfCube = input("Enter The Volume Of The Cube / CM³ --> ")
    lengthOfSide = math.cbrt(volumeOfCube)
    volumeOfSide = round(additionalVolume / 6)
    length = round(lengthOfSide, 1)
    width = round(lengthOfSide, 1)
    heigth = round(volumeOfSide / (length * width), 1)
    print(f"Length = {length} | Width  = {width} | Height = {heigth}")

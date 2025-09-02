import os
import fileTypeReader
from conversions import imgConversion
from optimizations import imgOptimization
from PIL import Image

def read_file_name():
    file_name = fileTypeReader.file_name_parser()
    return file_name
# Moving the conversion functions into their own methods

'''
def img_convert_file_type(file_name, convert_type):
    try:
        temp =  file_name
        # Check to see if the file name is valid
        if temp is None or len(temp) != 2:
            return OSError
        # Get the location of the input file and type
        input_file = temp[0] + "." + temp[1]
        # Same location as input and different type
        output_file = temp[0] + "." + convert_type
        old_image = Image.open(input_file)

        if input_file is output_file:
            print("Same file type")
        else:
            # Conversion
            print("Converting...")
            with old_image as new_image:
                new_image.save(output_file)
            print("Converted ", input_file, " to ", output_file)
            return new_image

        print("Failed to convert ", input_file, " to ", output_file)
        return None
    # Catch the OSError to alert a invalid file
    except OSError as ose:
        print("Invalid file\n", ose.errno)
        return ose
'''
'''
def img_optimization(file_name):
    try:
        temp_name = file_name
        # Check to see if the file name is valid
        if temp_name is None:
            return OSError
        img = Image.open(temp_name)
        img.save(file_name, optimize = True)
    except OSError as ose:
        print("Invalid file\n", ose.errno)
        return ose
    except:
        print("Failed to decrease file size.")
        return None
'''

def main():
    userActive = True
    while userActive == True:
        operation = input("> ")
        match operation:
            case "file conversion":
                to_Type = input("Please enter what file type you wish to convert to: ")
                name_and_type = read_file_name()
                imgConversion.convertImage(name_and_type, to_Type)
                print("Done!")
            case "optimize":  
                file_name = input("Enter file location: ")
                imgOptimization.img_optimization(file_name)
                print("Done!")
            case "color correct":
                file_name = input("Enter file location: ")
                
            case "quit":
                userActive = False
                print("Ending program, goodbye!")
            case default:
                print("Please choose an operation.")

if __name__ == '__main__':
    main()
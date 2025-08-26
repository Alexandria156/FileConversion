import os
import fileTypeReader
from conversions import imgConversion
from PIL import Image
import ffmpeg

def read_file_name():
    file_name = fileTypeReader.file_name_parser()
    return file_name
# Moving the conversion functions into their own methods
def video_convert_file_type(file_name, convert_type):
    try:
        temp = file_name
        if temp is None or len(temp) != 2:
            return OSError
        input_file = temp[0] + "." + temp[1]
        output_file = temp[0] + "." + convert_type

        if input_file is output_file:
            print("Same file type")
        else:
            # Conversion
            print("Converting...")
            ffmpeg.input(input_file).output(output_file).run()
            print("Converted ", input_file, " to ", output_file)
            return True

        print("Failed to convert ", input_file, " to ", output_file)
        return None
        
    except OSError as ose:
        print("Invalid file\n", ose.errno)
        return ose
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
# Coming back to fix this 
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

def video_optimization(file_name):
    try:
        temp_name = file_name
        # Check to see if the file name is valid
        if temp_name is None:
            return OSError
        
    except OSError as ose:
        print("Invalid file\n", ose.errno)
        return ose

def main():
    #name_and_type = read_file_name()
    #imgConversion.convertImage(name_and_type, "png")
    #img_convert_file_type(name_and_type, "png")
    #Taking bytes
    print("Image optimization")
    img_optimization("test_media\\jp.png")
    #video_convert_file_type(name_and_type, "wmv")
    print("Done!")

if __name__ == '__main__':
    main()
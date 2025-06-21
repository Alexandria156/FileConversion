import fileTypeReader
from PIL import Image

def read_file_name():
    file_name = fileTypeReader.file_name_parser()
    return file_name

def video_convert(file_name, convert_type):
    pass

def img_convert(file_name, convert_type):
    try:
        temp = file_name
        if temp is None or len(temp) != 2:
            return OSError
        input_file = temp[0] + "." + temp[1]
        output_file = temp[0] + "." + convert_type
        old_image = Image.open(input_file)
        if input_file is output_file:
            print("Same file type")
        else:
            with old_image as new_image:
                new_image.save(output_file)
            print("Converted ", input_file, " to ", output_file)
            return new_image
        print("Failed to convert ", input_file, " to ", output_file)
        return None
    except OSError as ose:
        print(ose.errno)
        return ose



def main():
    pass;

if __name__ == '__main__':
    main()
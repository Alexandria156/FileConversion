from PIL import Image
'''
def main():

    try:
        temp =  file_name
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
        print("Invalid file\n", ose.errno)
        return ose
'''
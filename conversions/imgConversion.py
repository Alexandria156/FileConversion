from PIL import Image

def convertImage(file_name, convert_type):
    try:
        temp_name = file_name
        if temp_name is None or len(temp_name) !=2:
            return OSError
        
        # Get the location of the input file and type
        input_file = temp_name[0] + "." + temp_name[1]
        # Same location as input and different type
        output_file = temp_name[0] + "." + convert_type
        old_img = Image.open(input_file)

        if input_file is output_file:
            print("Duplicate files of the same type")
        else:
            print("Converting your file...")
            with old_img as new_img:
                new_img.save(output_file)

            print("Successfully converted ", input_file, " to ", output_file)
            return 1
        print("Failed to convert ", input_file)
        return 0
    
    except OSError as ose:
        print("Invalid file,", ose.errno, "\n")
        return ose

    except ValueError as ve:
        print("Failed to convert file,", ve.with_traceback,"\n")
        return 0
    

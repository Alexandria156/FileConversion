import fileTypeReader
import ffmpeg

def videoConvertType(file_name, convert_type):
    try:
        temp = file_name
        if temp is None or len(temp) != 2:
            return OSError
        input_file = temp[0] + "." + temp[1]
        output_file = temp[0] + "." + convert_type

        temp = file_name
        if temp is None or len(temp) != 2:
            return OSError
        input_file = temp[0] + "." + temp[1]
        output_file = temp[0] + "." + convert_type
        
    except OSError as ose:
        print("Invalid file\n", ose.errno)
        return ose
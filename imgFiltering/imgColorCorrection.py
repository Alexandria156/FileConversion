from PIL import ImageColor
from PIL import Image

def color_shift(file_name):
    try:
        temp_name = file_name
        # Check to see if the file name is valid
        if temp_name is None:
            return OSError
    except OSError as ose:
        print("Invalid file\n", ose.errno)
        return ose
    except:
        print("Failed to decrease file size.")
        return None
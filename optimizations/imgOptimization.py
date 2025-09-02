from PIL import Image

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
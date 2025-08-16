
def file_name_parser():
    check = False
    # placeholder for user input from a different function
    name_type = input("Enter file location: ")
    name = ""
    f_type = ""
    file_name = []
    for character in name_type:
        # split file name from file type
        if character == ".":
            check = True
            continue
        elif check == False:
            # while the name is still being read, 
            name = name + character
        else:
            f_type = f_type + character
    file_name.append(name)
    file_name.append(f_type)
    return file_name

def main():
   file_name = file_name_parser()
   if len(file_name) >= 2 or len(file_name) <= 1:
       print("Invalid file name")
   else:
        print(file_name[0])
        print(file_name[1])

if __name__ == "__main__":
    main()
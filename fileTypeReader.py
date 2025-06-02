
def file_name_parser():
    check = False
    name_type = input()
    name = ""
    f_type = ""
    file_name = ["", ""]
    for character in name_type:
        if character == ".":
            check = True
            continue
        elif check == False:
            name = name + character
        else:
            f_type = f_type + character
    file_name[0] = name
    file_name[1] = f_type
    return file_name

def main():
   file_name = file_name_parser()
   print(file_name[0])
   print(file_name[1])

if __name__ == "__main__":
    main()
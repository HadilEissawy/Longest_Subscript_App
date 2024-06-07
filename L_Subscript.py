import os
import sys
print('lets start')

def longest_subscript_in_dic(input_directory):
    if not os.path.isdir(input_directory):   # check if the directory is valid
        print('The directory ' +  input_directory  + ' is not a valid path in your system')
        return "The directory " + input_directory + " is not a valid path in your system"
    max_sub_direct = ""

    for direct, sub_dir, file_names in os.walk(input_directory):  # iterate through the directory
        for cur_sub_dir in sub_dir:  # check the length of each subdirectory "string"
            # print(cur_sub_dir)
            if len(cur_sub_dir) > len(max_sub_direct):
                max_sub_direct = cur_sub_dir

    if max_sub_direct == "":
        print("The directory does not contain sub_directories")
        return "The directory does not contain sub_directories"

    print("The Subscript with the longest name is " + max_sub_direct)

if __name__ == "__main__":
    # directory = input("Enter the directory path: ")
    print(sys.argv[1])
    longest_subscript_in_dic(sys.argv[1])



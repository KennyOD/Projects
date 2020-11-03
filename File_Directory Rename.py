import os
from os.path import expanduser as ex
import re
from pathlib import Path
import sys


def menu():
    print("""
    Select from the following...
    1. Absolute Path (A)
    2. Current Path [Location of the .py file] (B)
    3. Exit (X)
    """)


def finalize_changes(old, new, error):
    if not error:
        print("\nFiles renamed successfully!!!\nDo you want to undo your changes? After now, changes cannot be undone!")
    else:
        print("\nChanges were made but some errors were encountered... would you like to undo made changes?")
    print("\nPlease ensure folders are accessible to avoid more errors...")
    while True:
        final_change = input("Select enter or yes(Y) to undo, no(N) to finish changes\n-->")
        if final_change.strip().upper() == 'Y' or final_change == '':
            for x in range(len(new)):
                try:
                    os.rename(new[x], old[x])
                except FileNotFoundError as F:
                    print(re.findall('^\\[.+] (.+)$', str(F))[0])
                    continue
                except OSError as OSE:
                    print(re.findall('^\\[.+] (.+)$', str(OSE))[0])
                    continue
                except StopIteration:
                    print("The folder specified cannot be accessed!")
            print("Changes made have been undone... Thank you!")
            sys.exit()
        elif final_change.strip().upper() == 'N':
            print("Changes made have been saved! Thank you!")
            sys.exit()
        else:
            pass
    # exit() or quit() are useful for safely exiting a code but not good for production code/real programs
    # instead, use sys.exit()


def final_name_change(path, old, new):
    err = False
    os.chdir(path)
    for x in sorted(range(len(old)), reverse=True):
        try:
            os.rename(old[x], new[x])
        except FileNotFoundError as F:
            print(re.findall('^\\[.+] (.+)$', str(F))[0])
            err = True
            continue
        except OSError as OSE:
            print(re.findall('^\\[.+] (.+)$', str(OSE))[0])
            err = True
            continue
        except StopIteration:
            print("The folder specified cannot be accessed!")
            err = True
    finalize_changes(old, new, err)


def final_ext_change(path, files, extension):
    err = False
    name_old = []
    name_new = []
    os.chdir(path)
    for x in range(len(files)):
        try:
            part = files[x]
            if files[x].count('.') > 0:
                part = re.findall('(.+)\\..+$', files[x])[0]
                # To get the filename instead of the extension
            os.rename(files[x], f'{part}{extension}')
            name_old.append(files[x])
            name_new.append(f'{part}{extension}')
        except FileNotFoundError as F:
            print(re.findall('^\\[.+] (.+)$', str(F))[0])
            err = True
            continue
        except OSError as OSE:
            print(re.findall('^\\[.+] (.+)$', str(OSE))[0])
            err = True
            continue
        except StopIteration:
            print("The folder specified cannot be accessed!")
            err = True
    finalize_changes(name_old, name_new, err)


def view_panel(path, items, final_name, start_pos, zero_fill, inc_val):
    name_old = []
    name_new = []
    os.chdir(path)
    zero_fill += len(start_pos)
    new_name = final_name.split('*')
    for x in range(len(items)):
        part = ""
        if items[x].count('.') > 0:
            part = re.findall('.+(\\..+)', items[x])[0]
        name_new.append(f'{new_name[0]}{start_pos.zfill(zero_fill)}{new_name[1]}{part}')
        name_old.append(items[x])
        start_pos = str(int(start_pos) + inc_val)
    print("Save the following changes?")
    for x in range(len(name_old)):
        print(f"{name_old[x]} --> {name_new[x]}")
    while True:
        print("Continue - Enter/(Y)\n"
              "Redo name selection - (N)\nGo back to file selection - (X)")
        confirm = input("--> ")
        if confirm.strip().upper() == 'Y' or confirm == '':
            final_name_change(path, name_old, name_new)
        elif confirm.strip().upper() == 'N':
            break
        elif confirm.strip().upper() == 'X':
            # uses exit_stat to break out of both loops when (X) condition is raised
            # exit_stat2 = False
            print("Exiting...")
            break
        else:
            print("Not a valid option...\n")


def ext_select(path, selected_files, selected_exts):
    exit_stat3 = True
    print("NOTE THAT YOUR INPUT WILL NOT BE SCALED TO LOWER OR UPPERCASE... WHAT YOU TYPE WILL BE REFLECTED AS SUCH")
    while exit_stat3:
        print("Type in new file extension to be used...Type in a single dot '.' to remove current extension")
        start = input("-->").strip()
        if len(start) > 0:
            if re.match('[^/|"?:<>*\\\\]+', start):
                if (start.count('.') == 1 and start.startswith('.')) or (len(start) > 0 and start.count('.') == 0):
                    if start == '.':
                        start = ""
                    elif start.count('.') == 0:
                        start = '.' + start
                    while exit_stat3:
                        print("Save the following changes?\nContinue - Enter/(Y)\n"
                              "Redo name selection - (N)\nGo back to file selection - (X)")
                        print("Extension(s) to be replaced...")
                        for num in range(len(selected_exts)):
                            if len(selected_exts[num]) == 0:
                                print(f"{num + 1}. <No extension>")
                                continue
                            print(f"{num + 1}. {selected_exts[num][1:]}")
                        if len(start) > 0:
                            print("New extension to be used:", start[1:])
                        else:
                            print("New extension to be used: <No extension>")
                        confirm = input("--> ")
                        if confirm.strip().upper() == 'Y' or confirm == '':
                            final_ext_change(path, selected_files, start)
                        elif confirm.strip().upper() == 'N':
                            print("NOTE THAT YOUR INPUT WILL NOT BE SCALED TO LOWER OR UPPERCASE... "
                                  "WHAT YOU TYPE WILL BE REFLECTED AS SUCH")
                            break
                        elif confirm.strip().upper() == 'X':
                            # uses exit_stat to break out of both loops when (X) condition is raised
                            exit_stat3 = False
                            print("Exiting...")
                        else:
                            print("Not a valid option...\n")
                else:
                    print("Incorrect naming sequence detected:", start)
            else:
                print("Unsupported characters found in string!\n")
        else:
            print("No input made... select enter or (Y) to retry and any key to return to the selection menu")
            stop = input("-->").strip()
            if stop.upper() == 'Y' or stop == '':
                pass
            else:
                break


def sort_files(name_sort, file_list):
    match = dict()
    not_match = dict()
    for file in file_list:
        if re.search(name_sort, file):
            x = str(file).replace(name_sort, '')


def name_select(path, selected_items):
    exit_stat2 = True
    while exit_stat2:
        try:
            print("Type in a new name to use... place an '*' wherever you want the incrementation to take place")
            start = input("--> ").strip()
            if len(start) > 0:
                if re.match('[^/|"?:<>\\\\]+', start):
                    # checks for unsupported filename characters
                    if start.count("*") == 1:
                        start_num = int(input("Specify start digit(s)\n--> ").strip())
                        increment = input("Specify increment value... press enter for default\n-->")
                        if increment == '':
                            increment = 1
                        elif int(increment) == 0:
                            increment = 1
                        else:
                            increment = int(increment)
                        ex_zero = input("Specify number of leading 0's to add. Select enter to set to default(1)\n--> ")
                        if ex_zero == '':
                            ex_zero = 1
                        else:
                            ex_zero = int(ex_zero)
                        # test_string = start.split("*")[0] + '#'.zfill(ex_zero + len(str(start_num))) + start.split("*")[1]
                        # new_string = start
                        view_panel(path, selected_items, start, str(start_num), ex_zero, increment)

                    elif start.count("*") > 1:
                        # the character * is also not supported but it must be used only once for the numbering
                        print("Incorrect string sequence detected... please use the '*' only once...\n")
                    else:
                        print("No * was found in string... Try again?")
                        print("Select enter or (Y) to retry and any other key to return to the selection menu...")
                        close = input("-->").strip()
                        if close.upper() == 'Y' or close == '':
                            pass
                        else:
                            break
                else:
                    print("Unsupported characters found in string!\n")
            else:
                print("Name cannot be empty!\n")
        except ValueError:
            print("Invalid integer sequence detected...\n")


def folder_select(path):
    while True:
        try:
            folder_list = sorted(next(os.walk(path))[1])
            type_to_rename = input("Rename all files in directory? \nContinue - Enter/(Y)"
                                   "\nRedo selection - (N)\nBack to main menu - (X)\n-->)")
            if type_to_rename.strip().upper() == 'Y' or type_to_rename == '':
                print("Files to be renamed... continue?\n")
                for f in range(len(folder_list)):
                    print(f"{f + 1}.[{folder_list[f]}]")
                while True:
                    rename = input("Press enter to continue and (X) to go back...\n-->")
                    if rename == '':
                        name_select(path, folder_list)
                        break
                    elif rename.upper().strip() == 'X':
                        break
                    else:
                        pass
            elif type_to_rename.strip().upper() == 'N':
                for f in range(len(folder_list)):
                    print(f"{f + 1}.[{folder_list[f]}]")
                print("Select folders(space with a comma) or press enter to continue...")
                print("Sample: '1, 3-7, 10, 12-13'")
                select = input("--> ").strip()
                if len(select) == 0:
                    name_select(path, folder_list)
                else:
                    # the same procedure as for selecting extensions is used here
                    select = [i for i in select.split(",") if i.strip() != '']
                    select_2 = []
                    for s in select:
                        if '-' in s:
                            k = [x for x in s.split("-") if x.strip() != '']
                            select_2.extend(range(int(k[0]), int(k[1]) + 1))
                        else:
                            select_2.append(s)
                    if (len(set(select_2)) <= len(folder_list)) & (max([int(x) for x in set(select_2)]) <= len(folder_list)):
                        folders = [folder_list[int(x) - 1] for x in set(select_2)]
                        name_select(path, folders)
                    else:
                        print("Invalid number(s) present in selection!")
            elif type_to_rename.strip().upper() == 'X':
                print("Returning...")
                break
            else:
                print("Invalid option...\n")
        except ValueError:
            print("Invalid character specified in selecting extensions/files to rename!")
        except OSError as OSE:
            print(re.findall('^\\[.+] (.+)$', str(OSE))[0])
        except StopIteration:
            print("The path specified cannot be accessed!")


def file_and_ext_select(path, rename_type):
    while True:
        try:
            ext = []
            files_list = sorted(next(os.walk(path))[2])
            for file in files_list:
                ext_type = ""
                # checks for a dot in the file and appends the characters after it to serve as the extension
                # appends characters after the last occurring dot including the dot
                if file.count(".") > 0:
                    ext_type = re.findall('.*(\\..+)', file.lower())[0]
                if ext_type not in ext:
                    ext.append(ext_type)
            type_to_rename = input("Rename all files in directory? \nContinue - Enter/(Y)"
                                   "\nRedo selection - (N)\nBack to main menu - (X)\n-->")
            if type_to_rename.strip().upper() == 'Y' or type_to_rename == '':
                print("Files to be renamed... continue?\n")
                for f in range(len(files_list)):
                    print(f"{f + 1}.[{files_list[f]}]")
                while True:
                    rename = input("Press enter to continue and (X) to go back...\n-->")
                    if rename == '':
                        if rename_type == 'F':
                            name_select(path, files_list)
                            break
                        elif rename_type == 'E':
                            ext_select(path, files_list, ext)
                            break
                    elif rename.upper().strip() == 'X':
                        break
                    else:
                        pass
            elif type_to_rename.strip().upper() == 'N':
                print("\nThe following extensions were found... which type would you like to rename?")
                for num in range(len(ext)):
                    if len(ext[num]) == 0:
                        print(f"{num + 1}. <No extension>")
                        continue
                    print(f"{num + 1}. {ext[num][1:]}")
                print("Insert a comma after each number for multiple file types...")
                print("Sample: '1, 3-7, 10, 12-13'")
                select = input("--> ").split(",")
                select = [i for i in select if i.strip() != '']
                select_2 = []
                for s in select:
                    if '-' in s:
                        k = [x for x in s.split("-") if x.strip() != '']
                        select_2.extend(range(int(k[0]), int(k[1]) + 1))
                        # after splitting using -, the range of the two numbers are found (hence the addition of 1)
                        # extend is used so that each value is added separately and not the whole range set
                    else:
                        select_2.append(s)
                if (len(set(select_2)) <= len(ext)) & (max([int(x) for x in set(select_2)]) <= len(ext)):
                    # checks if the max number specified in the set is greater than the number of extensions found
                    # also checks if the number of unique numbers specified is greater than the number of extensions
                    ext_selected = [ext[int(x) - 1] for x in set(select_2)]
                    files = []
                    # uses selected extensions to add files that end with it
                    for file in files_list:
                        for e in ext_selected:
                            if e == "":
                                if file.count(".") == 0:
                                    files.append(file)
                            elif file.lower().endswith(e):
                                files.append(file)
                    for f in range(len(files)):
                        print(f"{f + 1}.[{files[f]}]")
                    print("Proceed? Select files(space with a comma) or press enter to continue...")
                    print("Sample: '1, 3-7, 10, 12-13'")
                    select = input("--> ").strip()
                    if len(select) == 0:
                        if rename_type == 'F':
                            name_select(path, files)
                        elif rename_type == 'E':
                            ext_select(path, files, ext_selected)
                    else:
                        # the same procedure as for selecting extensions is used here
                        select = [i for i in select.split(",") if i.strip() != '']
                        select_2 = []
                        for s in select:
                            if '-' in s:
                                k = [x for x in s.split("-") if x.strip() != '']
                                select_2.extend(range(int(k[0]), int(k[1]) + 1))
                            else:
                                select_2.append(s)
                        if (len(set(select_2)) <= len(files)) & (max([int(x) for x in set(select_2)]) <= len(files)):
                            files_select = [files[int(x) - 1] for x in set(select_2)]
                            if rename_type == 'F':
                                name_select(path, files_select)
                            elif rename_type == 'E':
                                ext_select(path, files_select, ext_selected)
                        else:
                            print("Invalid number(s) present in selection!")
                else:
                    print("Invalid selection!")
            elif type_to_rename.strip().upper() == 'X':
                print("Returning...")
                break
            else:
                print("Invalid option...\n")
        except ValueError:
            print("Invalid character specified in selecting extensions/files to rename!")
        except OSError as OSE:
            print(re.findall('^\\[.+] (.+)$', str(OSE))[0])
        except StopIteration:
            print("The path specified cannot be accessed!")


def existence_check(path):
    exit_stat1 = True
    # checks if there are files/folders in the selected directory
    while exit_stat1:
        check = input("Rename files(F), extensions(E), or folders(D)? Select X to go back\n-->").upper().strip()
        if check == 'F' or check == 'E':
            if len(next(os.walk(path))[2]) > 0:
                file_and_ext_select(path, check)
                exit_stat1 = False
            else:
                print("There are no files in the selected directory!")
        elif check == 'D':
            if len(next(os.walk(path))[1]) > 0:
                folder_select(path)
                exit_stat1 = False
            else:
                print("There are no folders in the selected directory!")
        elif check == 'X':
            print("Back to main menu...")
            exit_stat1 = False
        else:
            pass


# For all the error handles that print out messages, re.findall is used to print the message and leave out the OS specs
print("Welcome to your file rename beta test...\nThis is a one-shot thing so no going back!")
while True:
    try:
        menu()
        choice = input("--> ").strip()
        if choice.upper() == 'A':
            path_abs = input(r"Select path: ")
            if len(path_abs) > 0:
                if path_abs.count(":") == 0:
                    # checks if a relative path was specified
                    path_abs = ex('~') + '\\' + path_abs
                if Path(path_abs).exists():
                    existence_check(path_abs)
                else:
                    print("Invalid directory path!", path_abs, "\n")
            else:
                print("No path was specified!")
        elif choice.upper() == 'B':
            path_cur = os.getcwd()
            existence_check(path_cur)
        elif choice.upper() == 'X':
            print("Thank you for your time!")
            sys.exit()
        else:
            print("Wrong option!...")
    except OSError as OS:
        print(re.findall('^\\[.+] (.+)$', str(OS))[0])
    except StopIteration:
        print("The path specified cannot be accessed!")
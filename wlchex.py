import shutil
import os
import random
import sys
import time

# Function to print a stylish, large logo banner with the name "Welcome Hacker HEX Tool"
def print_banner():
    # Clear the screen first
    os.system('clear')
    
    banner =
 _______  _______  _       _________ ______  
(  ____ )(  ___  )| \    /\\__   __/(  ___ \ 
| (    )|| (   ) ||  \  / /   ) (   | (   ) )
| (____)|| (___) ||  (_/ /    | |   | (__/ / 
|     __)|  ___  ||   _ (     | |   |  __ (  
| (\ (   | (   ) ||  ( \ \    | |   | (  \ \ 
| ) \ \__| )   ( ||  /  \ \___) (___| )___) )
|/   \__/|/     \||_/    \/\_______/|/ \___/ 
                                             


    =========================================
            Welcome RK RAKIB Tool
    =========================================
    """
    # Add color to the banner (Green & Yellow)
    print("\033[1;32m" + banner)  # Green text
    time.sleep(2)  # Wait for 2 seconds to show the banner

    # Stylish and nice message
    print("\033[1;34mStarting the tool... Please wait...\033[0m")
    time.sleep(2)  # Wait before showing the options

# Function to handle file cloning
def file_cloning():
    try:
        source = input("\033[1;34mEnter Source File Path: \033[0m")
        if not os.path.isfile(source):
            print("\033[1;31mError: Source file does not exist!\033[0m")
            return

        destination = input("\033[1;34mEnter Destination File Path: \033[0m")
        shutil.copy(source, destination)
        print(f"\033[1;32mSuccess: File cloned to {destination}\033[0m")
    
    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")

# Function to handle random file cloning
def random_file_cloning():
    try:
        # Get list of files in current directory
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        if len(files) == 0:
            print("\033[1;31mError: No files found in the current directory!\033[0m")
            return
        
        source_file = random.choice(files)
        destination_file = f"cloned_{source_file}"

        shutil.copy(source_file, destination_file)
        print(f"\033[1;32mSuccess: Random file cloned: {source_file} to {destination_file}\033[0m")
    
    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")

# Main function to select options
def main():
    try:
        print_banner()  # Show the styled banner at the start
        
        print("\033[1;34m=====================================\033[0m")
        print("\033[1;34m1.Random\033[0m")
        print("\033[1;34m2. Random File Cloning\033[0m")
        print("\033[1;34m3. File Cloning\033[0m")
        print("\033[1;34m4. Exit\033[0m")
        print("\033[1;34m=====================================\033[0m")

        choice = input("\033[1;34mEnter your choice (1, 2 or 3): \033[0m")
1
        if choice == '1':
            random_cloning()
        elif choice == '2':
            file_cloning()
        elif choice == '3':
            print("\033[1;33mExiting...\033[0m")
            sys.exit(0)
        else:
            print("\033[1;31mInvalid choice! Please select a valid option.\033[0m")

    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")
        sys.exit(1)

# Run the main function
if __name__ == "__main__":
    main()

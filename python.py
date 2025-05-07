def read_and_modify_file():
    try:
        # Ask the user for a filename (Error Handling Lab)
        input_file = input("Enter the filename to read from: ")
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Modify content — example: convert to uppercase (File Read & Write Challenge)
        modified_lines = [line.upper() for line in lines]

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.writelines(modified_lines)

        print(f"Modified content saved to '{output_file}'.")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except IOError:
        print(" Error: File could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_modify_file()

while True:
    source = input("Enter the source filename or type 'quit' to exit: ").strip()
   
    if source == "":
        print("Source name can't be empty. Try again.")
        continue
    
    if source.lower() in ["quit", "exit"]:
        print("Exiting because source was not provided.")
        break
    
    destin = input("Enter the destination filename to write or type 'quit' to exit: ").strip()
    
    if destin == "":
        print("Destination name can't be empty. Try again.")
        continue
    
    if destin.lower() in ["quit", "exit"]:   # 🔧 You checked `source` again — should be `destin`
        print("Exiting because destination was not provided.")
        break

    try:
        with open(source, "r") as file1, open(destin, "w") as file2:
            for line in file1:
                if 'error' in line.lower() or 'warning' in line.lower():
                    file2.write(line)
        print(f"Filtered lines have been written to '{destin}'.\n")
    except FileNotFoundError:
        print("Source file not found. Please enter a valid filename.")
    except Exception as e:
        print(f"An error occurred: {e}")


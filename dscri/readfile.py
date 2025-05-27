while True:
    filename = input("Enter the filename you want to check or exit to quit : ").strip()
    if filename == "":
        print("Filename cannot be empty. Please enter a valid filename or exit to quit ")
        continue
    if filename.lower() in ["quit", "exit"]:
        break
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
filename = input("Enter the filename you want to check: ").strip()

if filename == "":
    print("Filename cannot be empty. Please run the script again and provide a valid filename.")
    exit()

    try:
        if fname.lower() in ["quit","exit"]:
            break
        with open(fname, "r") as file:
            content=file.read()
            print(content)
    except FileNotFoundError:
        print("File is not found enter again")
    except Exception as e:
        print(f"An error occured {e}")


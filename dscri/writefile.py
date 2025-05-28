while True:
    filename = input("Enter the filename (or type 'exit' to quit): ").strip()

    if filename == "":
        print("Filename cannot be empty. Please enter a valid filename.")
        continue

    if filename.lower() in ["quit", "exit"]:
        break

    try:
        with open(filename, "w") as file:
           content=input("Enter contents ") 
           file.write(content)
           
    except Exception as e:
        print(f"An error occurred: {e}")

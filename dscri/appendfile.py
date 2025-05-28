while True:
    
    fname = input("Enter the filename you want to write to : ").strip()
    
    if fname == "":
        print("Filename cannot be empty. Please enter a valid filename.")
        continue
    
    if fname.lower() in ["quit", "exit"]:
        break
    
    try: #code here
        with open(fname, "a") as file:
            content=input("Enter content to write ")
            while content.lower() != 'save':
                file.write(content + '\n')
                content = input("")
        
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
    except Exception as e:
        print(f"An error occurred: {e}")



    




while True:
    import os
    fname=input("Enter file name or exit to quit ").strip()
    if fname=="":
        print("File name cant be empty type again or 'exit' to quit ")
        continue
    if fname.lower() in ["quit","exit"]:
        print("Exiting the program.")
        break
    if os.path.exists(fname):
        
        ui=input("File exists........ \n type 'yes' to read or 'skip' to check other files 'quit' to exit ").strip()
        
        if ui.lower() in ["yes", "ok"]:
            
            with open(fname, "r") as file:
                print(file.read())
                
        elif ui.lower() in ["quit","exit"]:
            break
        
        elif ui.lower() in ["skip"]:
            continue
        else:
                print("Invalid choice. Please type 'yes', 'skip', or 'quit'.")
                
    else:
        print("File does not exist !!!!!!!!!! ")
        continue

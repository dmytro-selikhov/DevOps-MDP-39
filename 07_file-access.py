devices = []
file = open("devices.txt", "a")


while True:
    newItem = input("Enter device name: ")
    if newItem == 'exit':
        print("All done!")
        break
    else:
        file.write(newItem + "\n")
        print(newItem)

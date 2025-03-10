def main():
    response = "I got that! Anything else?"
    
    while True:
        message = input("Speak your mind: ")
        if message.strip().upper() == "STOP":
            print("Alright, stopping now!")
            break
        print(response)

if __name__ == "__main__":
    main()

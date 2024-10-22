def encode(to_encode): #Grace Wang
    holder = ""
    for i in to_encode:
        holder +=str(int(i)+3)
    print(holder)
    return holder


if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3.Quit")
        option = float(input("Please enter an option: "))
        if option == 1:
            encode_info = input("Please enter your password to encode: ")
            encode(encode_info)
        elif option == 2:
            #decode function here
            pass
        elif option == 3:
            break
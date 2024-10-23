def encode(to_encode): #Grace Wang
    holder = ""
    for i in to_encode:
        holder +=str(int(i)+3)
    print("Your password has been encoded and stored!")
    return holder

def decode(encoded):
    decoded = ""
    for i in encoded:
	    decoded += str(int(i)-3)
    print(f"The encoded password is {encoded}, and the original password is {decoded}")
    return decoded

if __name__ == '__main__':
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3.Quit")
        option = float(input("Please enter an option: "))
        if option == 1:
            encode_info = input("Please enter your password to encode: ")
            encoded_password = encode(encode_info)
        elif option == 2:
            decode(encoded_password) 
        elif option == 3:
            break

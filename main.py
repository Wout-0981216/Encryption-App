from cryptography.fernet import Fernet

stop = False
while not stop:
  print("\nWhat do you want to do?\n1. Encrypt a message\n2. Decrypt a message\nQ - quit")
  menu_input = input("\nenter 1,2 or q: ")
  menu_input = menu_input.lower()

  if menu_input == "1":
    print("Enter a line of text to be encrypted:\n")
    message = input()
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(str.encode(message))
    print("Key: ", str(key).strip("b").strip("'"))
    print("Encrypted message: ", str(encrypted_message).strip("b").strip("'"))

  elif menu_input == "2":
    print("\nFirst enter the encrypted message you want to decrypt, then enter the encryption key:")
    message_to_decrypt = input("message: ")
    encryption_key = input("key: ")
    try:
      f = Fernet(encryption_key)
      decrypted_message = f.decrypt(str.encode(message_to_decrypt))
      print("\nDecrypted message: ", str(decrypted_message).strip("b").strip("'"))
    except Exception as e:
      print(e)

  elif menu_input == "q":
    stop = True

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image

ENCRYPTION_MARKER = "ENCRYPTED"

def encrypt_image(image_path, encryption_key, file_format='JPEG'):
    try:
        img = Image.open(image_path)
        width, height = img.size

        pixels = img.load()
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                r, g, b = pixel if len(pixel) == 3 else (pixel[0], pixel[1], pixel[2]) 
                r ^= encryption_key
                g ^= encryption_key
                b ^= encryption_key

                pixels[x, y] = (r, g, b)
        img.info['ENCRYPTION_MARKER'] = ENCRYPTION_MARKER

        encrypted_image_path = image_path.replace('.jpg', '_encrypted.jpg')
        img.save(encrypted_image_path, format=file_format)
        print("Image encrypted and saved as", encrypted_image_path)

        return img
    except Exception as e:
        print("Error encrypting image:", str(e))
        return None
def decrypt_image(encrypted_image, decryption_key):
    try:
        decrypted_img = encrypted_image.copy()
        width, height = decrypted_img.size

        pixels = decrypted_img.load()
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                if len(pixel) == 4:  
                    r, g, b, a = pixel
                    r ^= decryption_key
                    g ^= decryption_key
                    b ^= decryption_key
                    pixels[x, y] = (r, g, b, a)
                else:  
                    r, g, b = pixel
                    r ^= decryption_key
                    g ^= decryption_key
                    b ^= decryption_key
                    pixels[x, y] = (r, g, b)

        return decrypted_img
    except Exception as e:
        print("Error decrypting image:", str(e))



if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")

    while True:
        choice = input("What would you like to do?\n1. Encrypt\n2. Decrypt\n3. Exit\nChoice: ")

        if choice == '1':
            encryption_key = int(input("Enter the encryption key (an integer): "))
            file_format = input("Enter the file format (e.g., JPEG, PNG): ")

            encrypted_image = encrypt_image(image_path, encryption_key, file_format)

            if encrypted_image:
                black_image = Image.new('RGB', encrypted_image.size, (0, 0, 0))
                black_image.show()

                decrypt_choice = input("Would you like to decrypt the image? (yes/no): ")
                if decrypt_choice.lower() == 'yes':
                    decryption_key = int(input("Enter the decryption key: "))

                    decrypted_image = decrypt_image(encrypted_image, decryption_key)
                    if decrypted_image:
                        decrypted_image.show()

        elif choice == '2':
            decryption_key = int(input("Enter the decryption key: "))

            encrypted_image = Image.open(image_path)
            decrypted_image = decrypt_image(encrypted_image, decryption_key)
            if decrypted_image:
                decrypted_image.show()
            print("Image decrypted succesfully")

        elif choice == '3':
            break

        else:
            print("Invalid choice.")


# In[ ]:





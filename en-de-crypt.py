# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:38:53 2025

@author: Swaraj R C
"""

"""
Menu-Driven Shift Cipher Program

"""
import random
def shift_cipher():
    # Overview
    print("---------------------------------------------------")
    print("\t\t\t\t\t\t\t****Context**** \n\
2 People Alice and Bob are communicating with each other{Public Channel} \
over the Internet ")
    print("A Hacker(say Oscar) is trying to access \
what they both are communicating")
    print("---------------------------------------------------")

    # OG_List
    lis = [chr(val) for val in range(97, 123)]
    k = 11

    # Input Message
    msg = input("Type message for Alice: ")
    print(".\n.\n.\n.\n.\n.\n.\n.\n---------------------------------------------------")
    print(f"If Shift Cipher is not used Oscar will see the message:\n \
----->  {msg}")
    msg = msg.lower()
    resurk = msg.split()
    original_msg = msg  # Save for special char tracking
    msg = msg.replace(" ", "")
    letters = list(msg)

    # Track special characters with index
    special_chars = []
    clean_letters = []
    for idx, ch in enumerate(letters):
        if ch in lis:
            clean_letters.append(ch)
        else:
            special_chars.append((idx, ch))  # save index + char

    print("---------------------------------------------------")
    print("---------------Oscar Viewing a Public Channel------------")
    print("---------------------------------------------------\n")
    print("               After using Shift Cipher             \n")

    # Encryption
    E = []
    special_chars = []

    for idx, letter in enumerate(letters):
        if letter in lis:
            index = lis.index(letter)
            E.append(index)
        else:
            special_chars.append((idx, letter))  # Save index + original char

    C = []
    for num in E:
        encrypt = (num + k) % 26
        C.append(encrypt)

    cipher_text = ''
    e_idx = 0  # Index for encrypted letters
    for idx in range(len(letters)):
        if any(idx == sc[0] for sc in special_chars):
            cipher_text += '#'  # Replace non-alphabet with #
        else:
            cipher_text += lis[C[e_idx]]
            e_idx += 1


    print(f"This is what Oscar will be able to see \n------>'{cipher_text}'")
    print("---------------------------------------------------")
    print(f"But Bob cannot understand this message hence we need to decrypt it \n\
back to the original message using special key i.e K={k}")
    print("---------------------------------------------------")

    choice = input("\nDo you want Bob to decrypt the message? (yes/no): ").strip().lower()

    if choice in ['yes', 'y']:
        print("              #Decryption              ")

        # Extract just the encrypted alphabet letters
        encrypted_letters = []
        for ch in cipher_text:
            if ch in lis:
                encrypted_letters.append(ch)

        # Decrypt only those letters
        D = []
        for ch in encrypted_letters:
            index = lis.index(ch)
            decrypted = (index - k) % 26
            D.append(lis[decrypted])

        # Rebuild the decrypted message with original special characters
        og_txt_list = []
        d_idx = 0
        for idx in range(len(letters)):
            if any(sc[0] == idx for sc in special_chars):
                # Insert original special char
                sc_char = next(sc[1] for sc in special_chars if sc[0] == idx)
                og_txt_list.append(sc_char)
            else:
                og_txt_list.append(D[d_idx])
                d_idx += 1

        og_txt = ''.join(og_txt_list)

        # Reconstruct message using original word spacing
        i = 0
        og_msg = ""
        while i < len(og_txt):
            for word in resurk:
                word_len = len(word)
                segment = og_txt[i:i + word_len]
                if segment.lower() == word:
                    og_msg += segment + " "
                    i += word_len
                    break

        print("\n ------>", og_msg)
    else:
        denial_msgs = [
            "\n Bob refused to decrypt. Oscar is now sniffing packets and praying to the cyber gods... :)",
            "\n Bob said 'nah', and Oscar just bought a decryptor from the dark web for 0.01 BTC. 0_0",
            "\n Decryption declined. Bob switched to Morse code and vanished into the matrix. *_*",
            "\n Bob skipped decryption. Oscar rage-quit and now plays hacking simulators. ",
            "\n Decryption denied. Oscar launched ChatGPT in safe mode to guess the message."
        ]
        print(random.choice(denial_msgs))

# ---------------- Main Menu ---------------- #

def main():
    while True:
        print("\n===============================")
        print(" 🔐 Shift Cipher Communication ")
        print("===============================")
        print("1. Simulate Alice–Bob Communication")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            shift_cipher()
        elif choice == '2':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
    
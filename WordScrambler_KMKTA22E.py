import tkinter as tk
import re

def load_words(file_name):
    with open(file_name, 'r') as file:
        words = file.read().splitlines()
    return {"".join(sorted(word)): word for word in words}

def unscramble(word, word_dict):
    return word_dict.get("".join(sorted(word)), "No ei leia sellist söna ")

def unscramble_input(input_str, word_dict):
    scrambled_words = re.findall(r'\b[a-zA-Z]{5,12}\b', input_str)
    unscrambled_words = [unscramble(word, word_dict) for word in scrambled_words]
    return ', '.join(unscrambled_words)

def show_unscrambled():
    unscrambled = unscramble_input(entry.get(), word_dict)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "Copy ja paste öiged sönad: " + unscrambled)


word_dict = load_words(r'C:\\wordlist.txt') #Lisa directory

# Lambi GUI
root = tk.Tk()
root.title("Ultimaatum Word Scrambler HTS LVL1 2023 ")
label = tk.Label(root, text="Sisesta sassis sõnad:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()
button = tk.Button(root, text="Un-sassista vms ", command=show_unscrambled)
button.pack()
result_text = tk.Text(root, width=50, height=10)
result_text.pack()
root.mainloop()

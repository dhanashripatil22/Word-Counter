import tkinter as tk
from tkinter import messagebox

def word_counter(text):
    if not text:
        return 0
    words = text.split()
    return len(words)

def count_words():
    input_text = text_entry.get("1.0", "end-1c")  # Get text from the Text widget
    word_count = word_counter(input_text)
    result_label.config(text=f"Word count: {word_count}")

def clear_text():
    text_entry.delete("1.0", "end")  # Clear the Text widget
    result_label.config(text="Word count: 0")

# Create main window
window = tk.Tk()
window.title("Word Counter")
window.geometry("600x500")  # Set window size

# Set background color
window.configure(bg="#f5f5f5")

# Set custom font
title_font = ("Helvetica", 18, "bold")

# Create and place widgets with color, adjusted positions, and font styling
title_label = tk.Label(window, text="Word Counter", font=title_font, bg="#3498db", fg="white", padx=10, pady=10)
title_label.pack(fill="x")

label = tk.Label(window, text="Enter a sentence or paragraph:", bg="#f5f5f5", fg="#333", font=("Helvetica", 12))
label.pack(pady=10)

text_entry = tk.Text(window, height=10, width=50, bg="#ecf0f1", font=("Helvetica", 11), padx=10, pady=10, bd=2, relief="solid")
text_entry.pack(pady=10)

count_button = tk.Button(window, text="Count Words", command=count_words, bg="#2ecc71", fg="white", padx=10, pady=5)
count_button.pack(pady=10)

clear_button = tk.Button(window, text="Clear Text", command=clear_text, bg="#e74c3c", fg="white", padx=10, pady=5)
clear_button.pack(pady=10)

result_label = tk.Label(window, text="Word count: 0", font=("Helvetica", 14, "bold"), bg="#f5f5f5", fg="#333")
result_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()

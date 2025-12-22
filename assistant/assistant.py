import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
from google import genai

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from assistant_api import send_message as ai_send_message, load_user_profile

emotions = {
    "neutral":("neutral.png", "#ffffff"),
    "happy":("happy.png", "#aaffff"),
    "sad": ("sad.png", "#ffaaaa")
}

root = tk.Tk()
root.title("AI Assistant")
root.geometry("400x600")

avatar_label = tk.Label(root)
avatar_label.pack(pady=10)

dialog_frame = tk.Frame(root)
dialog_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

dialog_text = tk.Text(dialog_frame, height=15, wrap=tk.WORD, state=tk.DISABLED)
dialog_text.pack(fill=tk.BOTH, expand=True)

input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, padx=10, pady=5)

message_entry = tk.Entry(input_frame, width=30)
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

def send_message():
    message = message_entry.get().strip()
    if message:
        add_to_dialog("Ви: " + message)
        message_entry.delete(0, tk.END)
        
        update_avatar("neutral")
        
        try:
            user_profile = load_user_profile()
            response = ai_send_message(message, user_profile)
            add_to_dialog("AI: " + response)
            
            if "😊" in response or "👍" in response or "добре" in response.lower():
                update_avatar("happy")
            elif "😢" in response or "погано" in response.lower():
                update_avatar("sad")
            else:
                update_avatar("neutral")
                
        except Exception as e:
            add_to_dialog("AI: Помилка з'єднання: " + str(e))
            update_avatar("sad")

def add_to_dialog(text):
    dialog_text.config(state=tk.NORMAL)
    dialog_text.insert(tk.END, text + "\n")
    dialog_text.config(state=tk.DISABLED)
    dialog_text.see(tk.END)

send_button = tk.Button(input_frame, text="Надіслати", command=send_message)
send_button.pack(side=tk.RIGHT)

def update_avatar(emotion):
    img_path, bg_color = emotions.get(emotion, emotions["neutral"])
    root.configure(bg=bg_color)
    avatar_label.configure(bg=bg_color)
    try:
        full_path = os.path.join(os.path.dirname(__file__), img_path)
        img = Image.open(full_path)
        img = img.resize((100, 100), Image.Resampling.LANCZOS)
        avatar_image = ImageTk.PhotoImage(img)
        avatar_label.configure(image=avatar_image)
        avatar_label.image = avatar_image
    except Exception as e:
        print(f"Error loading image: {e}")
        
message_entry.bind("<Return>", lambda event: send_message())

update_avatar("neutral")
root.mainloop()

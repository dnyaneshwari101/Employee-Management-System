from customtkinter import *
from PIL import Image  # PIL is the Python Image Library
from tkinter import messagebox

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    if not username or not password:
        messagebox.showerror('Error', 'All fields are required')
    else:
        messagebox.showinfo('Success','Login successful!')
        root.destroy()
        import ems

root = CTk()
root.geometry('733x550')
root.resizable(0, 0)  # Disable maximize button
root.title('Login page')

# Import the background image
image = CTkImage(Image.open('bg_image.jpeg'), size=(733, 550))
imageLabel = CTkLabel(root, image=image, text='')  # Create label and add image to it
imageLabel.place(x=0, y=0)

# Create a frame (box) around the entry fields with white background
entry_frame = CTkFrame(imageLabel, width=400, height=250, corner_radius=15, fg_color='white')
entry_frame.place(x=200, y=150)  # Adjust the position of the frame

# Username label and entry placement inside the frame
usernameLabel = CTkLabel(entry_frame, text='Username:', font=("Arial", 14))
usernameLabel.place(x=30, y=30)
usernameEntry = CTkEntry(entry_frame, placeholder_text='Enter your username', width=220,border_color='black')
usernameEntry.place(x=130, y=30)

# Password label and entry placement inside the frame
passwordLabel = CTkLabel(entry_frame, text='Password:', font=("Arial", 14))
passwordLabel.place(x=30, y=100)
passwordEntry = CTkEntry(entry_frame, placeholder_text='Enter your password', width=220, show="*", border_color='black')
passwordEntry.place(x=130, y=100)

# Login button inside the frame
loginButton = CTkButton(entry_frame, text='Login', width=220, cursor='hand2', command=login, border_color='black')
loginButton.place(x=100, y=170)

root.mainloop()

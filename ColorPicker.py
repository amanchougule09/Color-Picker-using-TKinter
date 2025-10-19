import tkinter as tk
from tkinter import colorchooser

# ====== Update Color Function ======
def update_color():
    """Update color display using RGB slider values."""
    r, g, b = r_scale.get(), g_scale.get(), b_scale.get()
    color = f'#{r:02x}{g:02x}{b:02x}'
    color_display.config(bg=color)
    color_hex_label.config(text=f"Hex: {color.upper()}")

# ====== Choose Custom Color ======
def choose_color():
    """Open color palette and update display."""
    color_code = colorchooser.askcolor(title="Choose Color")[1]
    if color_code:
        color_display.config(bg=color_code)
        color_hex_label.config(text=f"Hex: {color_code.upper()}")

# ====== Predefined Color Selection ======
def set_predefined_color(value):
    """Set display color from dropdown."""
    if value != "Select Color":
        color_display.config(bg=value)
        color_hex_label.config(text=f"Hex: {value.upper()}")

# ====== Hover Effects ======
def on_enter(e):
    choose_btn.config(bg="#0B8E81")

def on_leave(e):
    choose_btn.config(bg="#059C9B")

# ====== Main Window ======
root = tk.Tk()
root.title("🎨 Color Picker App")
root.geometry("620x500")
root.configure(bg="#D9F3F1")

# ====== Menu Bar (with border) ======
menu_bar = tk.Menu(root, bg="#059C9B", fg="white", activebackground="#0B8E81", relief="solid", bd=1)
file_menu = tk.Menu(menu_bar, tearoff=0, bg="#E9FDFB", fg="#046865", relief="solid", bd=1)
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# ====== Main Frame ======
main_frame = tk.Frame(root, bg="#FFFFFF", bd=1, relief="solid")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=520, height=420)

# ====== Title ======
title_label = tk.Label(main_frame, text="🎨 Professional Color Picker", 
                       font=("Segoe UI", 14, "bold"), fg="#046865", bg="#FFFFFF")
title_label.pack(pady=15)

# ====== Predefined Color Dropdown ======
color_options = [
    "Select Color", "#FF0000", "#00FF00", "#0000FF", "#FFFF00",
    "#FFA500", "#800080", "#000000", "#FFFFFF", "#808080", "#00CED1"
]
selected_color = tk.StringVar(value="Select Color")

dropdown = tk.OptionMenu(main_frame, selected_color, *color_options, command=set_predefined_color)
dropdown.config(font=("Segoe UI", 11), bg="#F0F0F0", fg="#046865", relief="solid", bd=1,
                highlightthickness=0, width=20, cursor="hand2", activebackground="#E0FFFF")
dropdown.pack(pady=10)

# ====== Choose from Palette Button (with border) ======
choose_btn = tk.Button(main_frame, text="🎨 Choose Custom Color", font=("Segoe UI", 10, "bold"), 
                       bg="#059C9B", fg="white", activebackground="#0B8E81", activeforeground="white",
                       relief="solid", bd=1, padx=15, pady=6, cursor="hand2", command=choose_color)
choose_btn.pack(pady=10)

choose_btn.bind("<Enter>", on_enter)
choose_btn.bind("<Leave>", on_leave)

# ====== RGB Sliders ======
rgb_frame = tk.Frame(main_frame, bg="#FFFFFF")
rgb_frame.pack(pady=5)

r_scale = tk.Scale(rgb_frame, from_=0, to=255, orient="horizontal", label="Red", length=300,
                   command=lambda x: update_color(), fg="#AA0000", bg="#FFFFFF", highlightthickness=0)
r_scale.pack(pady=3)

g_scale = tk.Scale(rgb_frame, from_=0, to=255, orient="horizontal", label="Green", length=300,
                   command=lambda x: update_color(), fg="#007A00", bg="#FFFFFF", highlightthickness=0)
g_scale.pack(pady=3)

b_scale = tk.Scale(rgb_frame, from_=0, to=255, orient="horizontal", label="Blue", length=300,
                   command=lambda x: update_color(), fg="#0000AA", bg="#FFFFFF", highlightthickness=0)
b_scale.pack(pady=3)

# ====== Color Display Box ======
color_display = tk.Label(main_frame, text="", bg="#F4F4F4", width=30, height=6, bd=1, relief="solid")
color_display.pack(pady=15)

# ====== HEX Code Label ======
color_hex_label = tk.Label(main_frame, text="Hex: #FFFFFF", font=("Segoe UI", 11, "bold"), bg="#FFFFFF", fg="#046865")
color_hex_label.pack(pady=5)

# ====== Footer ======
footer_label = tk.Label(root, text="Designed by Aman", font=("Segoe UI", 9), bg="#D9F3F1", fg="#046865")
footer_label.pack(side="bottom", pady=5)

# ====== Run App ======
root.mainloop()

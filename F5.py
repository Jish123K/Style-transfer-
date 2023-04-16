# Add a way for the user to preview the generated image before saving it

import tkinter as tk

# Create the main window

window = tk.Tk()

# Create a label for the image

label = tk.Label(image=generated_image)

# Create a button to preview the image

button = tk.Button(

    text="Preview",

    command=lambda: preview_image(generated_image),

)

# Add the label and button to the main window

label.pack()

button.pack()

# Define a function to preview the image

def preview_image(image):

    # Create a new window

    new_window = tk.Toplevel()

    # Create a label for the image

    label = tk.Label(image=image)

    # Add the label to the new window

    label.pack()

    # Show the new window

    new_window.mainloop()

# Show the main window

window.mainloop()

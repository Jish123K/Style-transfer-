# Add a button to allow the user to save the generated image

import tkinter as tk

# Create the main window

window = tk.Tk()

# Create a label for the button

label = tk.Label(text="Save generated image")

# Create a button

button = tk.Button(

    text="Save",

    command=lambda: save_image(generated_image),

)

# Add the label and button to the main window

label.pack()

button.pack()

# Define a function to save the generated image

def save_image(image):

    # Get the filename from the user

    filename = tk.filedialog.asksaveasfilename(

        filetypes=[("JPEG", "*.jpg")],

        defaultextension=".jpg",

    )

    # Save the image to the file

    tf.io.write_file(filename, image)

# Show the main window

window.mainloop()

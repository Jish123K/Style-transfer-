# Add a checkbox to allow the user to choose between different style images

import tkinter as tk

# Create the main window

window = tk.Tk()

# Create a label for the checkbox

label = tk.Label(text="Choose a style image")

# Create a checkbox

checkbox = tk.Checkbutton(

    text="Mona Lisa",

    variable=var,

    command=lambda: update_style(var.get()),

)

# Add the label and checkbox to the main window

label.pack()

checkbox.pack()

# Define a function to update the style image

def update_style(style):

    # Get the current value of the checkbox

    if style == 1:

        style_image = tf.io.read_file('mona_lisa.jpg')

        style_image = tf.image.decode_jpeg(style_image)

        style_image = tf.image.resize(style_image, [256, 256])

    else:

        style_image = tf.io.read_file('starry_night.jpg')

        style_image = tf.image.decode_jpeg(style_image)

        style_image = tf.image.resize(style_image, [256, 256])

    # Train the model with the new style image

    generated_image = train(content_image, style_image, iterations=100, learning_rate=0.01)

    # Save the new image

    tf.io.write_file('generated.jpg', generated_image)

# Show the main window

window.mainloop()
# Add a label to display the generated image

import tkinter as tk

# Create the main window

window = tk.Tk()

# Create a label for the image

label = tk.Label(image=generated_image)

# Add the label to the main window

label.pack()

# Show the main window

window.mainloop()

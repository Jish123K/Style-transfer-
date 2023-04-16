# Add a slider to control the strength of the style transfer

import tkinter as tk

# Create the main window

window = tk.Tk()

# Create a label for the slider

label = tk.Label(text="Strength of style transfer")

# Create a slider

slider = tk.Scale(

    from_=0,

    to=100,

    orient=tk.HORIZONTAL,

    command=lambda x: update_strength(x),

)

# Add the label and slider to the main window

label.pack()

slider.pack()

# Define a function to update the strength of the style transfer

def update_strength(x):

    # Get the current value of the slider

    strength = x / 100.0

    # Train the model with the new strength

    generated_image = train(content_image, style_image, iterations=100, learning_rate=strength)

    # Save the new image

    tf.io.write_file('generated.jpg', generated_image)

# Show the main window

window.mainloop()

# Add a progress bar to show the user how far along the style transfer is

import tkinter as tk

# Create the main window

window = tk.Tk()

# Create a label for the progress bar

label = tk.Label(text="Style transfer in progress")

# Create a progress bar

progress_bar = tk.ttk.Progressbar(orient=tk.HORIZONTAL, length=200)

# Add the label and progress bar to the main window

label.pack()

progress_bar.pack()

# Define a function to update the progress bar

def update_progress(progress):

    # Set the progress bar value

    progress_bar.configure(value=progress)

# Start the style transfer

for i in range(iterations):

    # Update the progress bar

    update_progress(i / iterations)

    # Train the model

    generated_image = train(content_image, style_image, learning_rate=0.01)

# Save the generated image

tf.io.write_file('generated.jpg', generated_image)

# Show the main window

window.mainloop()

import os

import tensorflow as tf

from tensorflow.keras import layers

from tensorflow.keras.applications import vgg19

# Load the VGG19 model

vgg = vgg19.VGG19(include_top=False, weights='imagenet')

# Define the content loss function

def content_loss(content_image, generated_image):

    content_layer = 'block5_conv2'

    content_features = vgg.get_layer(content_layer).output

    content_loss = tf.reduce_mean(tf.square(content_features - generated_image))

    return content_loss

# Define the style loss function

def style_loss(style_image, generated_image):

    style_layers = ['block1_conv2', 'block2_conv2', 'block3_conv3', 'block4_conv3', 'block5_conv3']

    style_targets = []

    for layer in style_layers:

        style_features = vgg.get_layer(layer).output

        style_gram = tf.matmul(style_features, style_features, transpose_b=True)

        style_targets.append(style_gram)

    style_loss = tf.reduce_mean(tf.square(style_targets - generated_image))

    return style_loss

# Define the total loss function

def total_loss(content_image, generated_image, style_image, alpha=1.0, beta=10.0):

    content_loss = content_loss(content_image, generated_image)

    style_loss = style_loss(style_image, generated_image)

    return alpha * content_loss + beta * style_loss

# Define the optimization function

def train(content_image, style_image, iterations=100, learning_rate=0.01):

    # Initialize the generated image

    generated_image = tf.random.normal([content_image.shape[0], content_image.shape[1], content_image.shape[2], content_image.shape[3]])

    # Define the optimizer

    optimizer = tf.optimizers.Adam(learning_rate=learning_rate)

    # Iterate over the number of iterations

    for i in range(iterations):

        with tf.GradientTape() as tape:

            # Calculate the loss

            loss = total_loss(content_image, generated_image, style_image)
# Backpropagate the loss

        gradients = tape.gradient(loss, generated_image)

        # Update the generated image

        optimizer.apply_gradients([(gradients, generated_image)])

        # Print the loss

        print(loss)

    # Return the generated image

    return generated_image

# Load the content image

content_image = tf.io.read_file('content.jpg')

content_image = tf.image.decode_jpeg(content_image)

content_image = tf.image.resize(content_image, [256, 256])

# Load the style image

style_image = tf.io.read_file('style.jpg')

style_image = tf.image.decode_jpeg(style_image)

style_image = tf.image.resize(style_image, [256, 256])

# Generate the new image

generated_image = train(content_image, style_image, iterations=100, learning_rate=0.01)

# Save the new image

tf.io.write_file('generated.jpg', generated_image)

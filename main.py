# Import necessary libraries
import streamlit as st
import os
from PIL import Image


# Define a function to list image files in a directory
def list_image_files(directory):
    image_files = []
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            image_files.append(os.path.join(directory, filename))
    return image_files


# Create a Streamlit app
def main():
    st.title("Image Gallery with Descriptions")

    # Define the directory where your images are located
    image_directory = './Images'

    # List all image files in the directory
    image_files = list_image_files(image_directory)

    # Display the selected image and its description
    if not image_files:
        st.error("No image files found in the specified directory.")
    else:
        st.sidebar.title("Image Selection")
        selected_image_index = st.sidebar.selectbox("Select an Image", image_files, index=0)

        # Display the selected image
        image = Image.open(selected_image_index)
        st.image(image, caption='Selected Image', use_column_width=True)

        # Define a dictionary with image descriptions or metadata (you can customize this)
        image_descriptions = {
            'img01.jpg': 'Description for Image 1',
            'img02.jpg': 'Description for Image 2',
            'img03.jpg': 'Description for Image 3',
        }

        # Display the image description
        image_filename = os.path.basename(selected_image_index)
        if image_filename in image_descriptions:
            st.write(f"**Image Description:** {image_descriptions[image_filename]}")
        else:
            st.warning("No description found for this image.")


if __name__ == '__main__':
    main()

import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Load the InceptionV3 model
model = tf.keras.models.load_model('C:\\Users\\aksha\\OneDrive\Desktop\\Pest_Prediction\\model_inception.h5')

# Define a list of labels for your classes
labels = ['ants', 'bees', 'beetle', 'caterpillar', 'earthworms', 'earwig', 'grasshopper', 'moth', 'slug', 'snail', 'wasp', 'weevil']

# Create a dictionary of pest-related information
pest_info = {
    'ants': 'Pesticide: Borax-based ant baits or liquid ant baits.\nTechnique: Place ant baits near ant trails.',
    'bees': 'Technique: Instead of using pesticides to control bees, consider promoting bee-friendly practices.',
    'beetle': 'Pesticide: Use insecticides specific to the type of beetle you\'re dealing with.',
    'caterpillar': 'Pesticide: Bt (Bacillus thuringiensis) is effective against caterpillars.',
    'earthworms': 'Technique: Earthworms are beneficial for soil health, so it\'s not recommended to use pesticides.',
    'earwig': 'Pesticide: Contact insecticides can be used to control earwigs.',
    'grasshopper': 'Pesticide: Use chemical insecticides, such as pyrethroids.',
    'moth': 'Pesticide: Specific chemical insecticides are available for moth control.',
    'slug': 'Pesticide: Slug and snail baits containing iron phosphate or metaldehyde.',
    'snail': 'Pesticide: Slug and snail baits containing iron phosphate or metaldehyde.',
    'wasp': 'Pesticide: Wasp and hornet sprays.\nTechnique: Use the spray to target wasp nests or individual wasps.',
    'weevil': 'Pesticide: Use insecticides specific to stored product pests.'
}

# Create the main window
window = tk.Tk()
window.title("Pest Prediction")
window.geometry("600x600")
window.configure(bg="#f2f2f2")  # Set background color

# Create a function to browse and display an image
def browse_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((250, 250))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
        classify(file_path)

# Create a label to display the selected image
image_label = tk.Label(window, bg="#ffffff")
image_label.pack(pady=20)

# Create a "Browse" button
browse_button = tk.Button(window, text="Browse Image", command=browse_image, bg="#336699", fg="white")
browse_button.pack()

# Create a function to select a pest and display information about it
def select_pest():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    pest_choice = simpledialog.askstring("Pest Prediction", "Select a pest from the list:", initialvalue="ants", parent=root)
    if pest_choice:
        if pest_choice in pest_info:
            pest_info_text.config(text=pest_info[pest_choice], fg="#336699")
        else:
            pest_info_text.config(text="No information available for the selected pest.")
    root.destroy()

# Create a "Select Pest" button
select_pest_button = tk.Button(window, text="Select Pest", command=select_pest, bg="#336699", fg="white")
select_pest_button.pack()

# Create a label to display pest-related information
pest_info_text = tk.Label(window, text="", wraplength=400, justify="left", bg="#f2f2f2")
pest_info_text.pack(pady=20)

# Create a label for predictions
predictions_label = tk.Label(window, text="Top 5 Predictions:", bg="#f2f2f2", font=("Arial", 14))
predictions_label.pack()

# Create a text widget to display predictions
predictions_text = tk.Text(window, height=10, width=40, bg="#ffffff")
predictions_text.pack()

# Define a function to classify the image
def classify(image_path):
    img = tf.image.decode_image(tf.io.read_file(image_path))
    img = tf.image.resize(img, [236, 236])
    img = tf.keras.applications.inception_v3.preprocess_input(img)
    img = img[None, ...]
    prediction = model.predict(img).flatten()
    class_probabilities = {labels[i]: float(prediction[i]) for i in range(len(labels))}
    top_classes = dict(sorted(class_probabilities.items(), key=lambda item: item[1], reverse=True)[:5])
    predictions_text.delete(1.0, tk.END)  # Clear the previous predictions
    for class_name, probability in top_classes.items():
        predictions_text.insert(tk.END, f"{class_name}: {probability:.2%}\n")

# Create the main loop
window.mainloop()

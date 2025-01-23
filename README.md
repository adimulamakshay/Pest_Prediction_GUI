# **Pest Prediction GUI**

This project is designed to identify and classify different types of pests from images. It utilizes a pre-trained InceptionV3 model for image classification and outputs the top 5 most probable pest categories along with their confidence scores. This Jupyter Notebook implements a deep learning model for classifying tomato leaf diseases from images. It leverages transfer learning with a pre-trained InceptionV3 model and fine-tunes it on a custom dataset.

**Project Structure:**

* `leaf_disease_detection.ipynb`: Jupyter Notebook containing the code for training and evaluating the model.
* `dataset/`: Directory containing the training and validation image datasets. (Assuming this directory structure)
    * `train/`: Subdirectory containing images of tomato leaves with different diseases (organized into class folders).
    * `val/`: Subdirectory containing validation images for model evaluation.
* `model_inception.h5`: The saved TensorFlow model file (trained InceptionV3 model for pest classification).
* `Pest_Model.py`: Main Python script containing the graphical user interface (GUI) and image classification logic.

**Dependencies:**

* TensorFlow
* Keras
* Pillow (PIL Fork)
* tkinter
* numpy

**Running the Project:**

1. **Mount Google Drive:**
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. **Install Dependencies:**
   ```bash
   !pip install tensorflow keras Pillow matplotlib numpy
   ```

3. **Navigate to the Project Directory:**
   ```python
   import os
   os.chdir('/content/drive/MyDrive/YourProjectPath') # Replace with your actual project directory
   ```
*Make sure to replace `'/content/drive/MyDrive/YourProjectPath'` with the actual path to your project directory in Google Colab.

4. **Run the Jupyter Notebook:**
   * Open the `leaf_disease_detection.ipynb` notebook in Google Colab or a local Jupyter environment.
   * Execute the cells in the notebook sequentially.

**Code Overview:**

* **Import Libraries:** Imports necessary libraries for TensorFlow, Keras, image processing, and data manipulation.
* **Set GPU Memory Allocation:** Configures GPU memory usage for training (optional, adjust as needed).
* **Load Pre-trained Model:** Loads the InceptionV3 model pre-trained on ImageNet, excluding the top classification layers.
* **Freeze Pre-trained Layers:** Freezes the pre-trained layers of InceptionV3 to prevent them from being updated during training.
* **Add Custom Layers:** Adds a new classification layer with the number of outputs matching the number of disease classes in your dataset.
* **Compile Model:** Defines the loss function (categorical cross-entropy), optimizer (Adam), and metrics (accuracy) for model training.
* **Data Augmentation:** Creates ImageDataGenerator objects for training and validation sets, applying random transformations (shear, zoom, horizontal flip) for data augmentation.
* **Load Data:** Loads training and validation image datasets using flow_from_directory with appropriate target sizes and batch sizes.
* **Train Model:** Trains the model on the training dataset with validation on the validation dataset for a specified number of epochs.
* **Visualize Training Results:** Plots training and validation loss and accuracy curves to monitor model performance.
* **Save Model:** Saves the trained model as `model_inception.h5`.
  ![image](https://github.com/user-attachments/assets/f047caaf-78d0-44b4-99e3-18dbb4163099)
  ![image](https://github.com/user-attachments/assets/b2c07ada-fcf4-4c36-a1a7-78d8aa4f4bb5)

1. **Install Dependencies:**
   ```bash
   pip install tensorflow keras Pillow tkinter numpy
   ```

2. **Download the Pre-trained Model:**
   * You'll need to download the pre-trained InceptionV3 model weights and place them in the `model_inception.h5` file. Pre-trained models can be found online from various sources.

3. **(Optional) Create Pest Information File:**
   * The `Pest_Model.py` file is optional and provides a way to include information about control methods for each pest category.

4. **Run the Script:**
   ```bash
   python Pest_Model.py
   ```

**Using the GUI:**

1. Click the "Browse Image" button to select an image file containing a pest.
2. The selected image will be displayed in the window.
3. Click the "Select Pest" button to open a dialog where you can choose a pest category from a list. (If `pest_info.py` exists)
   * Selecting a pest will display relevant control methods information in the window.
4. The "Top 5 Predictions" section will display the model's predictions for the uploaded image, including the most likely pest categories and their corresponding confidence scores.

**Note:**

* This is a basic implementation and can be further enhanced with features like:
    * Support for different image classification models.
    * Training a custom model on a pest image dataset.
    * Expanding the pest information database.
    * More comprehensive GUI elements for user interaction.
    * Training with a larger and more balanced dataset.
    * Experimenting with different hyperparameters (learning rate, epochs, etc.) for potentially better performance.
    * Implementing a custom image pre-processing pipeline for improved image normalization or noise reduction.

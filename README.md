# **Pest Prediction GUI**

This project is designed to identify and classify different types of pests from images. It utilizes a pre-trained InceptionV3 model for image classification and outputs the top 5 most probable pest categories along with their confidence scores.

**Project Structure:**

* `Pest_Model.py`: Main Python script containing the graphical user interface (GUI) and image classification logic.
* `model_inception.h5`: The saved TensorFlow model file (trained InceptionV3 model for pest classification).
* `labels.txt`: A text file containing labels (pest categories) corresponding to the model's output classes. (Assuming this file exists)
* `pest_info.py` (Optional): A Python script containing a dictionary mapping pest categories to information about control methods (pesticides and techniques).

**Dependencies:**

* TensorFlow
* Keras
* Pillow (PIL Fork)
* tkinter
* numpy

**Running the Project:**

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

I hope this README provides a clear understanding of your project. If you have the `pest_info.py` file, you can include it in the project structure description and mention its functionality in the Using the GUI section.

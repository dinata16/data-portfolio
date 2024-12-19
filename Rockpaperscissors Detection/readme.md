# Rock-paper-scissors Classification using TensorFlow

This project demonstrates a deep learning approach to classify hand gestures for the game Rock-Paper-Scissors using TensorFlow. The model is trained to recognize images of hands making rock, paper, and scissors gestures and predict the corresponding label.

## Highlights:
- Dataset is split into training and validation sets (80%-20%).
- Data augmentation techniques are applied to improve generalization.
- The model achieves an accuracy above 90% on the validation set.
- Includes functionality for users to upload and predict their own images.

## Dataset
The dataset contains labeled images of hands making rock, paper, and scissors gestures. It was downloaded from the [Dicoding Rock-Paper-Scissors dataset](https://github.com/dicodingacademy/assets/releases/download/release/rockpaperscissors.zip).

### Preprocessing Steps:
1. The dataset is extracted and split into training (80%) and validation (20%) subsets.
2. Data augmentation (e.g., flipping, rotation) is applied to increase dataset diversity.
3. Images are resized and normalized for model compatibility.

## Model Architecture
The classification model is built using TensorFlow's Sequential API. The architecture includes:
- Convolutional layers for feature extraction.
- MaxPooling layers to reduce spatial dimensions.
- Dense layers with ReLU activation for classification.
- A final Dense layer with Softmax activation to output probabilities for three classes.

## Results
The model achieves:
- **Training Accuracy:** ~90%
- **Validation Accuracy:** ~85%

### Training and Validation Performance Analysis
![Model Accuracy and Loss](https://github.com/user-attachments/assets/97b2ae2a-4ddb-420d-9e3a-249c3b484012)

### Training and Validation Performance Analysis
The training and validation performance over 30 epochs is visualized in the graphs above. Key observations:
- **Accuracy:** Both training and validation accuracy improve steadily during the early epochs and stabilize around 85%-90%. The close alignment between training and validation accuracy suggests that the model generalizes well to unseen data.
- **Loss:** The training and validation loss decrease consistently, indicating successful optimization. Although validation loss shows slight fluctuations, it remains close to the training loss, implying minimal overfitting.

## Installation and Usage

### Requirements:
- Python 3.8 or later
- TensorFlow 2.x
- Matplotlib
- NumPy

### Steps to Run the Project:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors-classification.git
   cd rock-paper-scissors-classification
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download and extract the dataset:
   ```bash
   wget --no-check-certificate \
     https://github.com/dicodingacademy/assets/releases/download/release/rockpaperscissors.zip \
     -O /tmp/rockpaperscissors.zip
   unzip /tmp/rockpaperscissors.zip -d ./data
   ```
4. Run the notebook
   

## Key Code Snippets

### Model Creation
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(256, activation='relu'),
    Dense(3, activation='softmax')
])
```

### Data Augmentation
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size = (150,150),
    batch_size = 32,
    class_mode = 'categorical')

validation_generator = validation_datagen.flow_from_directory(
    val_dir,
    target_size = (150,150),
    batch_size = 16,
    class_mode = 'categorical')
```

## References
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Dicoding Rock-Paper-Scissors Dataset](https://www.dicoding.com/)

---
Feel free to contribute to this project by creating issues or submitting pull requests!

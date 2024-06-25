import tkinter as tk
from tkinter import messagebox
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL

# Load Dataset
df = pd.read_csv("/1-python/Dataset.txt", header=None)
x = df.iloc[:, :-1].values  # Features
y = df.iloc[:, -1].values   # Class labels

# Define class labels
class_labels = {
    "Benign": 438,
    "Reveton": 948,
    "Cerber": 897,
    "teslacrypt": 914,
    "Locky": 944,
    "Yakes": 925
}

# Train RandomForestClassifier
x_train_rf, x_test_rf, y_train_rf, y_test_rf = train_test_split(x, y, test_size=0.2, random_state=42)
rf_classifier = RandomForestClassifier()
rf_classifier.fit(x_train_rf, y_train_rf)

# Train KNeighborsClassifier
x_train_knn, x_test_knn, y_train_knn, y_test_knn = train_test_split(x, y, test_size=0.2, random_state=42)
knn_classifier = KNeighborsClassifier()
knn_classifier.fit(x_train_knn, y_train_knn)

# Function to classify using RandomForestClassifier
def classify_rf(pattern):
    pattern_array = np.array([int(i) for i in pattern.split(",")])
    prediction = rf_classifier.predict([pattern_array])
    show_result("RandomForestClassifier", prediction[0])

# Function to classify using KNeighborsClassifier
def classify_knn(pattern):
    pattern_array = np.array([int(i) for i in pattern.split(",")])
    prediction = knn_classifier.predict([pattern_array])
    show_result("KNeighborsClassifier", prediction[0])

# Function to display classification result
def show_result(classifier_name, prediction):
    if prediction == "Benign":
        messagebox.showinfo(f"Ransomware is Gentle - '{classifier_name}'", f"Ransomware is gentle - '{classifier_name}'")
    else:
        messagebox.showinfo(f"Ransomware is Malicious - '{classifier_name}'", f"Ransomware is Malicious - '{prediction}'")

# Function to create GUI
def create_gui():
    root = tk.Tk()
    root.title("Classifier Selection")

    # Heading
    heading_label = tk.Label(root, text="Ransomware Transaction Classification System", font=("Helvetica", 16, "bold"))
    heading_label.pack(pady=10)
    
    try:
        # Load and display image
        image = Image.open("ransom.jpg")  # Replace "image.jpg" with the path to your image file
        image = image.resize((300, 200), Image.ANTIALIAS)  # Resize the image as needed
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(root, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        print("Error loading image:", e)
    # Input Box
    print("Enter Pattern for Tseting : ")
    pattern_entry = tk.Entry(root, width=50)
    pattern_entry.pack(pady=10)

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack()

    # Button for RandomForestClassifier
    rf_button = tk.Button(button_frame, text="RandomForestClassifier", command=lambda: classify_rf(pattern_entry.get()), bg="blue", fg="black")
    rf_button.pack(side=tk.LEFT, padx=5)

    # Button for KNeighborsClassifier
    knn_button = tk.Button(button_frame, text="KNeighborsClassifier", command=lambda: classify_knn(pattern_entry.get()), bg="blue", fg="black")
    knn_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()

# Run the GUI
create_gui()

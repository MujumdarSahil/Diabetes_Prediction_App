import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os

# Ensure the parent directory is in sys.path for imports to work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prediction_logic import predict_diabetes  # Fixed the import

# Create the main window
root = tk.Tk()
root.title("Diabetes Prediction")

# Set window size
root.geometry("800x600")

# Load background image
background_image_path = os.path.join(os.path.dirname(__file__), "../assets/Bacground.jpg")
bg_image = Image.open(background_image_path)
bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)  # Updated for Pillow 10+
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# Create and place input fields
tk.Label(root, text="Pregnancies").place(x=50, y=50)
entry_pregnancies = tk.Entry(root)
entry_pregnancies.place(x=200, y=50)

tk.Label(root, text="Glucose").place(x=50, y=100)
entry_glucose = tk.Entry(root)
entry_glucose.place(x=200, y=100)

tk.Label(root, text="Blood Pressure").place(x=50, y=150)
entry_blood_pressure = tk.Entry(root)
entry_blood_pressure.place(x=200, y=150)

tk.Label(root, text="Skin Thickness").place(x=50, y=200)
entry_skin_thickness = tk.Entry(root)
entry_skin_thickness.place(x=200, y=200)

tk.Label(root, text="Insulin").place(x=50, y=250)
entry_insulin = tk.Entry(root)
entry_insulin.place(x=200, y=250)

tk.Label(root, text="BMI").place(x=50, y=300)
entry_bmi = tk.Entry(root)
entry_bmi.place(x=200, y=300)

tk.Label(root, text="Diabetes Pedigree Function").place(x=50, y=350)
entry_diabetes_pedigree = tk.Entry(root)
entry_diabetes_pedigree.place(x=200, y=350)

tk.Label(root, text="Age").place(x=50, y=400)
entry_age = tk.Entry(root)
entry_age.place(x=200, y=400)

# Function to get input and predict
def on_predict():
    try:
        pregnancies = int(entry_pregnancies.get())
        glucose = float(entry_glucose.get())
        blood_pressure = float(entry_blood_pressure.get())
        skin_thickness = float(entry_skin_thickness.get())
        insulin = float(entry_insulin.get())
        bmi = float(entry_bmi.get())
        diabetes_pedigree = float(entry_diabetes_pedigree.get())
        age = int(entry_age.get())

        # Make prediction
        prediction = predict_diabetes([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age])

        # Show result
        if prediction == 1:
            messagebox.showinfo("Prediction Result", "The patient is likely to have diabetes.")
        else:
            messagebox.showinfo("Prediction Result", "The patient is unlikely to have diabetes.")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")

# Create Predict button
predict_button = tk.Button(root, text="Predict", command=on_predict)
predict_button.place(x=300, y=450)

# Start the Tkinter main loop
root.mainloop()

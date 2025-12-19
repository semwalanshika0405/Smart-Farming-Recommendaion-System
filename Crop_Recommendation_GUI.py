import tkinter as tk 
from tkinter import ttk, messagebox


def recommend_crop():
        try:
                soil = soil_type.get()
                temp = float(temperature.get())
                rainfall = float(rain.get())

                if soil == "Loamy" and 20 <= temp <= 30 and rainfall >= 100:
                        crop = "🌾 Rice"
                elif soil == "Black" and 25 <= temp <= 35 and rainfall >= 50:
                        crop = "🌿 Cotton"
                elif soil == "Sandy" and 20 <= temp <= 30 and rainfall >= 60:
                        crop = "🥜 Groundnut"
                elif soil == "Clay" and 15 <= temp <= 25 and rainfall >= 70:
                        crop = "🌾 Wheat"
                else:
                        crop = "🌽 Maize"

                result_label.config(text=f"✅ Recommended Crop: {crop}")

        except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numeric values")



root = tk.Tk() 
root.title("🌾 Smart Farming Crop Recommendation System 🌱") 
root.geometry("450x420") 
root.configure(bg="#e8f5e9")



heading = tk.Label( root, text="🌱 Smart Farming Recommendation System 🌾", font=("Arial", 16, "bold"), bg="#e8f5e9" ) 
heading.pack(pady=15)


soil_type = tk.StringVar()

tk.Label(root, text="🪴 Soil Type:", bg="#e8f5e9").pack() 
soil_menu = ttk.Combobox(root, textvariable=soil_type, state="readonly") 
soil_menu['values'] = ("Loamy", "Black", "Sandy", "Clay") 
soil_menu.pack(pady=5)


tk.Label(root, text="🌡️ Temperature (°C):", bg="#e8f5e9").pack() 
temperature = tk.Entry(root) 
temperature.pack(pady=5)


tk.Label(root, text="🌧️ Rainfall (mm):", bg="#e8f5e9").pack() 
rain = tk.Entry(root) 
rain.pack(pady=5)


recommend_btn = tk.Button( root, text="🌾 Recommend Crop 🌱", command=recommend_crop, bg="#4caf50", fg="white", font=("Arial", 11, "bold") ) 
recommend_btn.pack(pady=20)


result_label = tk.Label( root, text="", font=("Arial", 12, "bold"), bg="#e8f5e9" ) 
result_label.pack(pady=10)


tk.Label( root, text="🤖 Smart Farming ", bg="#e8f5e9" ).pack(side="bottom", pady=10)


root.mainloop()

# Predicting Mechanical Properties of Steels using Deep Learning Model
This project uses a deep learning regression model to predict key mechanical properties of steels — namely Yield Strength, Ultimate Tensile Strength (UTS), and Elongation — based on their composition and processing parameters.
## 📁 Dataset

- The dataset is synthetic and consists of steel compositions with:
  - Carbon (C%)
  - Chromium (Cr%)
  - Nickel (Ni%)
  - Manganese (Mn%)
  - Heat Treatment Temperature (°C)
  - Cooling Rate (°C/s)
  - Strain Rate (s⁻¹)
- Target outputs:
  - Yield Strength (MPa)
  - UTS (MPa)
  - Elongation (%)

📄 File: `synthetic_dataset.xlsx`

> 📌 Note: Make sure the Excel file is placed in the same directory as the notebook/script.

## 🛠️ Tools & Libraries

- Python 3.x
- pandas
- numpy
- TensorFlow / Keras
- scikit-learn
- matplotlib

## 🧠 Model Architecture

- Input Layer: 7 features
- Hidden Layers: [64, 128, 64] neurons with ReLU activation
- Output Layer: 3 neurons with linear activation
- Loss: Mean Squared Error (MSE)
- Optimizer: Adam

## 📈 Training

- Data normalized using `StandardScaler`
- Validation split: 20%
- Epochs: 50
- Batch size: 16

During training, both loss and MAE (Mean Absolute Error) are monitored.

![Screenshot 2025-07-05 224225](https://github.com/user-attachments/assets/20dd8633-d025-4bd5-8ea1-f87c9f46f47f)

## 📊 Visualization

The training process is visualized using matplotlib:
- **Loss & MAE curves**
- **Predicted vs Actual plots** on the validation set
- ![result](https://github.com/user-attachments/assets/5496a86e-d769-41f4-a0d7-730e6a9a982d)


## 🔍 Prediction Example

```python
X_new = np.array([[0.1, 0.3, 0.5, 0.9, 1050, 0.6, 0.02]])
```
![Screenshot 2025-07-05 224512](https://github.com/user-attachments/assets/b0e1daa5-0ddb-4d9c-b304-5e56fcccb6ce)

## Result

![Screenshot 2025-07-05 224212](https://github.com/user-attachments/assets/5463936f-5d1f-4bfd-a2dd-a547e9480265)

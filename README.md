# Predicting-Mechanical-Property-using-Deep-Learning
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

## 📊 Visualization

The training process is visualized using matplotlib:
- **Loss & MAE curves**
- **Predicted vs Actual plots** on the validation set


> You can generate these plots by running the script. Save them in a folder named `results/` for easy GitHub preview.

## 🔍 Prediction Example

```python
X_new = np.array([[0.1, 0.3, 0.5, 0.9, 1050, 0.6, 0.02]])

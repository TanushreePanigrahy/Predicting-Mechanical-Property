import numpy as np
import pandas as pd 
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense 
from tensorflow.keras.models import Sequential 
from sklearn.preprocessing import StandardScaler 

data = pd.read_excel('synthetic_dataset.xlsx', header=0)
data.info()

column_names = data.iloc[0].tolist()
data = data[1:].reset_index(drop=True)
data.columns = column_names
print(data.columns)

X = data[['Carbon (C%)', 'Chromium (Cr%)', 'Nickel (Ni%)', 'Manganese (Mn%)', 'Heat Treatment Temp (°C)','Cooling Rate (°C/s)', 'Strain Rate (s⁻¹)']]
y = data [['Yield Strength (MPa)','UTS (MPa)','Elongation (%)']]

scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

model = Sequential([
    Dense(64, activation='relu', input_shape=(X_scaled.shape[1],)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(y.shape[1], activation='linear')
])

model.compile(optimizer='Adam', loss='mse', metrics=['mae'])
history = model.fit(X_scaled, y_scaled, epochs=50, batch_size=16, validation_split=0.2, verbose=1)

X_new = np.array([[0.1, 0.3, 0.5, 0.9, 1050, 0.6, 0.02]])
X_new_scaled = scaler_X.transform(X_new)
y_pred_scaled = model.predict(X_new_scaled)
y_pred = scaler_y.inverse_transform(y_pred_scaled)

print('Predicted values: ')
print(f'Yeild strength (MPa): {y_pred[0][0]:.4f}')
print(f'UTS (MPa): {y_pred[0][1]:.4f}')
print(f'Elongation (%): {y_pred[0][2]:.4f}')
#Loss
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(history.history['loss'], label='Train loss')
plt.plot(history.history['val_loss'], label='Validation loss')
plt.title('Model Loss over epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.grid(True)
#MAE
plt.subplot(1,2,2)
plt.plot(history.history['mae'], label='Train MAE')
plt.plot(history.history['val_mae'], label='Val MAE')
plt.title('Model MAE over Epochs')
plt.xlabel('Epoch')
plt.ylabel('MAE')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
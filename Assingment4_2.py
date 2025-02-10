import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('weight-height(1) (3).csv')

# Inspect the data
plt.scatter(df['Height'], df['Weight'], alpha=0.5)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Scatter Plot of Height vs. Weight')
plt.show()

# Choose a model (Linear Regression)
X = df[['Height']]
y = df['Weight']

# Perform regression
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Plot the regression results
plt.scatter(X, y, alpha=0.5, label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Linear Regression of Height vs. Weight')
plt.legend()
plt.show()

# Compute RMSE and R2 value
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

print(f'RMSE: {rmse}')
print(f'R^2: {r2}')
import numpy as np
from scipy.integrate import quad

# Define a time-varying power function.
def power_func(t):
    return 120 * np.cos((np.pi / 12) * t)

print("Antiderivative expression:", "[120 * (12/pi) * sin((pi/12) * t)]")

# Integrate from t = 0 to t = 6.
# quad() returns (integral result, estimated error).
result, error = quad(power_func, 0, 6)

print(f"Integrated power over the interval: {result:.2f}")
print(f"Estimated numerical error: {error}")

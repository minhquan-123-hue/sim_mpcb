"""Bai 3: Lap phuong trinh vi phan cho be khuay."""

V = 500       # L
q_in = 8      # L/s
q_out = 8     # L/s
C_in = 2      # g/L
k = 0.02      # s^-1 

# dC/dt = (q_in*C_in - q_out*C - k*V*C) / V
source = q_in * C_in / V
loss = q_out / V + k

print(f"dC/dt = {source:g} - {loss:g} * C(t)")

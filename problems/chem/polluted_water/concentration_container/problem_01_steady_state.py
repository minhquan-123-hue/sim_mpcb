"""Bai 1: Be tron khong co phan ung, trang thai dung."""

V = 200       # L
q_in = 10     # L/min
q_out = 10    # L/min
C_in = 4      # g/L

m_in = q_in * C_in
C_out = m_in / q_out
tau = V / q_in

print(f"Muoi di vao: {m_in:g} g/min")
print(f"Nong do dong ra: {C_out:g} g/L")
print(f"Thoi gian luu trung binh: {tau:g} min")

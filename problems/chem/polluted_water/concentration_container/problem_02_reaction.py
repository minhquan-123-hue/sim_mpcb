"""Bai 2: Be phan ung o trang thai dung."""

V = 1000       # L
q_in = 20      # L/min
q_out = 20     # L/min
C_in = 0.5     # g/L
m_consumed = 6 # g/min

m_in = q_in * C_in
m_out = m_in - m_consumed
C_out = m_out / q_out

print(f"Chat o nhiem di vao: {m_in:g} g/min")
print(f"Chat o nhiem di ra: {m_out:g} g/min")
print(f"Nong do dong ra: {C_out:g} g/L")

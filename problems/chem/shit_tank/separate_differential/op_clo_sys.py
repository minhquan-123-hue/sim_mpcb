"""mot be chua do chat thai vao vao dong be xem phan ung va chay chat thai ra"""

from math import log
# axioms: Ct = Co.e^-kt , q/V + k , 0 = m_in - (m_cons + m_out)

V = 500#L
q = 50#L/h
k = 0.05#gio^-1
Co = 100#mg/L

# tinh hang so tong
K = q/V + k
print("toc do thay doi mol cua thai: ",K,"o don vi")

# tinh thoi gian tu 100mg/L -> 10mg/L
Ct = 10#mg/L

t = log(Ct / Co) / -k
print("thoi gian giam tu 100mg/l -> 10mg/l la: ",t,"ngay")
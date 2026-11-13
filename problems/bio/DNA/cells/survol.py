"""diện tích bề mặt và thể tích ảnh hưởng đến việc trao đổi chất , và sinh sản của tế bào (nhân sơ vs nhân thực)"""

# Ex1: ta tính kích thước cơ bản dựa trên bán kính từ đó sẽ thấy tỷ lệ
# giảm dần thể tích tăng mạnh hơn , diện tích bề mặt
# Surface Area / Volume

# surface area = 4*PI*r^2 (hình cầu)
# volume = 4/3*PI*r^3 (hình cầu)

rA = 1#micro met
rB = 10#micro met
rC = 100#icrom met

PI = 3.14#approximately 

rA_SV_rate = (4*PI*rA**2) / ((4/3)*PI*rA**3)
rB_SV_rate = (4*PI*rB**2) / ((4/3)*PI*rB**3)
rC_SV_rate = (4*PI*rB**2) / ((4/3)*PI*rC**3)

print(rA_SV_rate)
print(rB_SV_rate)
print(rC_SV_rate)

# tỷ lệ ngày càng nhỏ dần
# tức thể tích lớn hơn rất nhiều so với bề mặt 
# và việc bề mặt nhỏ mà thể tích lớn
# vận chuyển chất sẽ khó hơn rất nhiều




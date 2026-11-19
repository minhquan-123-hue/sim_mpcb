"""sử dụng tổ hợp và xác suất để xét được đột biến câm và đột biến thường xảy ra như thế nào khi replication error"""

# combinatrics: có tổng bao nhiêu khả năng
# probability: cái này xảy ra bao nhiêu lần trong tổng số lần và đổi ra phần
# trăm là bao nhiêu

#acid amin code
#Phenylalanine = UUX, UUU
#Leucine = UUA , UUG

# nếu ở vị trí số 3 của UUU đột biến
# chuyển thành A , G ,X
# vậy ta có UUA , UUG , UUX
# trong đó UUG,UUA là bị đổi thành acidamin khác (Leucine)
# và nếu bị đổi thành UUA thì vẫn có thể giải mã
# là 1 Phenylalanine (đột biến câm)

UUA = 1
UUG = 1
UUX = 1
tong_so_kha_nang = UUA + UUG + UUX
prob_to_leucine = (UUA + UUG)/tong_so_kha_nang
prob_to_pheny = (UUX)/tong_so_kha_nang

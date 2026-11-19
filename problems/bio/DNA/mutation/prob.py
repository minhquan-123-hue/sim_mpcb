"""tính xác suất để rơi vào trường hợp đột biến câm"""

#phần toán học xác suất có nhiều công thức bao trùm rộng
#tức rút ra sau nhiều lần thực hiện thực tế
#ta có thể đi sâu sau nếu cần thiết
#trong thời điểm hiện tại : số lần mong muốn xảy ra | số lần xảy ra / 
#tổng số khả năng => xác suất xảy ra

#datas
#Glycine == GGA-GGU-GGX-GGG
# với mỗi vị trí ta có 4 cách để trộn bằng neucleotide
# nhưng nếu với 1 bộ có sẵn thì mỗi một vị trí chỉ còn 3
# neucleotides để thay (tức bị đột biến)
pos1 = 4 - 1
pos2 = 4 - 1
pos3 = 4 - 1

total_outcome = pos1 * pos2 * pos3
print(total_outcome)

#nếu mà đột biến xảy ra ngẫu nhiên 1 trên 3 vị trí
#xác suất mà rơi vào vị trí số 3 sẽ là
#về công thức tạm thời chưa đi sâu nhưng phần này khá thú vị
#mình sẽ đào sâu sau
silmu_prob = 1/3
print(silmu_prob)


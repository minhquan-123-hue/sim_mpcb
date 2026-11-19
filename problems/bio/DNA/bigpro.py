""" 
1. quãng đường di chuyển của dinh dưỡng
2. dna: bản thiết kế sinh hoàn chỉnh từ gạch và bậc và sợi
3. toán tổ hợp
"""

"PRO1"
# với vi khuẩn nhân sơ có kích bán kính 1 nano mét
# và tế bào nhân thực có bán kính 10 nano mét
# dùng S/V tỷ lệ để xác độ hiệu quả trong "vận chuyển"
# nutrients
bacteria = 3. / 1.
print(bacteria)

cell = 3. / 10.
print(cell)

"PRO2"
# lập hệ phương trình không số
# tính từng A T G X
# ta có axiom: 2A + 2G = N
# mà A/G = 2/3 => 3A = 2G
# 2A + 3A = N
# 3A = 2G
# A = N/5
# G = 3N/10

"PRO3"
# Tại sao khi có 3 vị trí mỗi vị trí có 4 cách
# tổ hợp lại là 4^3 
# ta có thể biểu diễn như sau:
# pos1:A-T-G-X , pos2:A-T-G-X, pos3:A-T-G-X
# chứng minh bằng tay viết từng tổng hợp ra
# ta thấy là nó ra 64 tổ hợp
# khoa học là như vậy dùng tay chứng minh
# sau đó lặp đi lặp lại thì suy ra quy tắc
# tổng số cách tại 1 ví trí ** tổng số vị trí = tổng số khả năng
# Ex: mk iphone: có 6 vị trí , và một vị trí có kết dùng 0-9 (10 cách) => 10^6 , nếu để mk khó một chút chẳng ai có thể giải ra nổi kể cả siêu máy tính nói phét vậy cho vui nhưng đây là phần giải thích kết nối phần toán học

#justify for writing code and text , vì mình viết văn bản mà nó vẫn tính toán được , đôi khi mình không phải biết trong var là con số gì , con nếu làm việc với số liên tục sẽ không thấy mối quan hệ , tức là nhét số vào variable để có thể suy nghĩ ẩn đi nhiều chi tiết hơn
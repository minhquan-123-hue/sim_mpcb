"""đây là phần bài cuối cùng được giải ra để giúp đất hồi phục không 
còn quá nhiều ion H^+ dẫn đến việc ion Al^3+ hòa tan nhiều trong 
dung dịch nữa"""

# ta có
Soil = 1#ton
CEC = 15#charge + / 100g
CaCO3 = 100#g/mol

# ta sẽ đổi đơn vị ton -> g
Soil *= 1000 * 1000

# tính tổng số lượng điện tích
# 100 g có 15 charge vậy 1000000 g có bao nhiêu => lấy 1000000 / 100
total_ion_charge_positive = CEC * Soil / 100

# chất CaCO3 sẽ giải phóng ra rất nhiều Ca^2+
# mà ta biết là Ca^2+ sẽ có 2 điện tích
# giờ ta có thể tìm số mmol và số mol cần trao đổi
Ca_2_positive = (total_ion_charge_positive / 2) / 1000

# giờ ta có tìm được khối lượng Canxi carbonate đưa vào đất
# vì 1 mol CaCO3 tạo 1 mol Ca^2+ => ta có thể lấy mol của Ca^2+
# và thực hiện nhân nó với khối lượng 1 mol của CaCO3
CaCO3 = Ca_2_positive * 100
print(CaCO3)

# tự kết luận + tham khảo từ gpt: đúng về mặt toán học trong này , nhưng có # thể chưa chuẩn trong thực tế ,  nhưng model cần hiểu ở đây là:
# CaCO3 -> Ca^2+ + CO3^2- ?
# và sau đso CO3^2- sẽ phản ứng tiếp tạo ra OH^-
# và OH^- sẽ phản ứng với Al^3+
# từ chuỗi phản ứng này ta có thể thấy được rằng số lượng H^+ giảm là độc tố
# Al^3+ cũng giảm theo và kết tinh thành chất rắn ít tan Al(OH)3

"""sử dụng nhân tổ hợp để biết xem bộ 2 hay bộ 3 (sinh vật nhân tạo với 6 neucleotides) có thể mã hóa được hết 150 loại acidamins"""

# datas
acidamins = 150#types 
neucleotides = 6#types: A U G C (D K)

# bộ 2 có được phép lặp, pos 1: 6 , pos 2: 6
two_enc = neucleotides * neucleotides

# bộ 3 có được phép lặp, pos 1: 6 , pos 2: 6 , pos 3: 6
thr_enc = neucleotides * neucleotides * neucleotides

print(two_enc,"bộ codons theo bộ 2")
print(thr_enc,"bộ codons theo bộ 3")

#vì bộ 150 acidamins cần ít nhất 150 bộ codon để mã hóa và 1 bộ codon kết thúc
# số lượng codons của bộ 3 mới đủ thỏa mãn
# và có thêm một phần chú ý là cơ chế "thoái hóa di truyền"
# nếu codons có bị gặp xóa nhầm , thêm nhầm , lặp lại cũng sẽ tạo ra đúng amino acids cần tạo không gây đột biến


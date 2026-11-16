"""từ chiều dài của sợi DNA ta sẽ tính có bao nhiêu viên gạch thông tin (neucleotides)"""

# lưu ý viên gạch neucleotide có phần không chỉ là A T G X
# phần yêu cầu:
# + đổi length về Neucletides tổng sử dụng: N/2 * 3.4A 
# + thiết lập 2 hệ phương trình tuyến tính cho A và G
# + đo A T G X

# Ta có:
L=5100#Angstrom = 0.1nm
A = 1
G = 2*A
T = A
C = G

N = L / 3.4 * 2
print("tổng số gạch thông tin: ",N)

# N = A + T + G + C
# N = 2A + 2G
# G = 2A
# N = 6A
A = N / 6
print(A)
T = A
print(T)
G = 2*A
print(G)
C = G
print(C)


"""trong dung dich qua trinh ket tinh va phan ly(hoa tan) dien ra dong thoi , ta phai su dung phuong phap de loai bo kim loai ion trong dung dich nen phai lam no ket tinh"""


# intution model not correctly in mathmetic
# Cu(OH)2
ion_Cu = 10
ion_OH = 0 #mol luc dau

# Ksp = (ion_Cu)*(ion_OH) tich so tan
# Qsp = (ion_Cu)*(ion_OH) tich so ket

# tuc la toc do Cu(OH)2 <=> Cu^2+ + OH^- se lien tuc ket tinh va hoa tan dong thoi [mol * mol]
Ksp = 10 * 20 

# do NaOH vao dung dich de duoc 5OH^- 
ion_OH += 5
Qsp = ion_Cu * ion_OH

if Qsp < Ksp:
    print("so luong ion_OH thap nen lien tuc bi hoa tan sau khi ket tinh")

# do them NaOH vao dung de duoc them 20OH^-
ion_OH += 15
Qsp = ion_Cu * ion_OH

if Qsp == Ksp:
    print("so luong ion_OH bang voi ion_Cu nen ket tinh va hoa tan bang nhau")

# do them NaOH vao de ta co 21OH^-
ion_OH += 1
Qsp = ion_Cu * ion_OH

if Qsp > Ksp:
    print("so luong ion_OH lon hon ion_Cu nen gio ket tinh se duoc thuc hien")

# vi 1 Cu^2+ = 2OH^- => ta se ket tinh duoc 1 anh Cu^2+ xuong duoi day
ion_Cu = 10 - 1

# sau do thi 9 anh Cu^2+ va 19 em OH^- lien tuc ket hop va hoa tan
# again this is intution model not correctly in math
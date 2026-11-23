""" mỗi một lần hít thở là một chuỗi tiêu hóa glucose xảy ra"""

# câu 1: tính mol Glucose
# câu 2: tính mol Oxy , và lít của Oxy
# câu 3: số lần thở để tiêu hóa hết 1 bánh quy

# datas
# Phương trình cân bằng: C6H12O6 + 6O2 -> 6CO2 + 6H20 + 32ATP
glucose_of_banh_quy = 27#g
mpm_glucose = 180#g
vpm_o2 = 22.4#lít
volume_per_breathing = 0.5#lít/breathing

# câu 1: done
banh_quy_mol = 1/ (mpm_glucose / 27)

# câu 2: done 
# nhìn vào phương trình số mol của o2
# gấp số mol của glu 6 lần
o2_mol = banh_quy_mol * 6
o2_volume = o2_mol * vpm_o2

# câu 3: done 
so_lan_tho_de_tieu_hoa_het_banh_quy = o2_volume / volume_per_breathing




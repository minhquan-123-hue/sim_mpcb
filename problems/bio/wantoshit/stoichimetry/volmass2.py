"""tính thể tích và khối lượng dựa vào phương trình cân bằng
Glu + Oxy => Carbon + Oxy + ATP"""

# 1. tính mol Glucose
# 2. tính mol của ATP, mol của CO2 dựa vào hệ số tỷ lượng
# 3. tính volume của CO2 

# datas
# C6H12O6 + 6O2 -> 6CO2 + 6H20 + 32ATP
glucose_mass = 45#g
mpm_glucose = 180#g
vpm_co2 = 24.79#lít

# câu 1: done 
mol_of_glucose = mpm_glucose / glucose_mass

# câu 2: done 
# từ phương trình ta có:
# + mol co2 gấp 6 lần mol glucose
# + mol atp gấp 32 lần mol glucose
mol_of_co2 = mol_of_glucose * 6
mol_of_atp = mol_of_glucose * 32

# câu 3: done
co2_volume = mol_of_co2 * vpm_co2


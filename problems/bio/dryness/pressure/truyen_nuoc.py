"""
đi khám bị truyền nhầm dung dịch có nồng độ muối cao hơn
nồn độ muối trong cơ thể
"""

# 1.đổi đơn vị Celcuis -> Kelvin
# 2. tính áp suất thẩm thấu của tế bào trong cơ thể ?
# 3. tính áp suất thẩm thấu của dung dịch , và đo chênh lệch áp suất để 
# biết nước sẽ di chuyển về đâu

# datas
# sử dụng van't hoff equation : Pressure = Cm.R.T
# trong đó R là hằng số khí lí tưởng (chưa cần biết rõ)
# chỉ cần sử dụng
# Kelvin = ? độ C + 273

C_solute_of_cell = 0.30#mol/L
C_solute_of_solution = 0.60#mol/L
cell_temp = 37# độ C
solution_temp = cell_temp
hang_so_khi_li_tuong = 0.082#L.atm/mol.K

# câu 1
Cell_temp_in_kelvin = cell_temp + 273
Solution_temp_in_kelvin = solution_temp + 273

# câu 2
Osmoisis_pressure_of_cell = C_solute_of_cell * hang_so_khi_li_tuong * Cell_temp_in_kelvin
print("áp suất thẩm thấu của tế bào: ",Osmoisis_pressure_of_cell)

# câu 3
Osmoisis_pressure_of_solution = C_solute_of_solution * hang_so_khi_li_tuong * Solution_temp_in_kelvin
print("áp suất thẩm thấu của dung dịch: ",Osmoisis_pressure_of_solution)

delta_pressure = Osmoisis_pressure_of_solution - Osmoisis_pressure_of_cell
print("chênh lệch áp suất thẩm thấu: " ,delta_pressure)

if Osmoisis_pressure_of_cell > Osmoisis_pressure_of_solution:
    print("Áp suất thẩm thấu trong tế bào lớn hơn dung dịch: nước đi vào tế bào.")
elif Osmoisis_pressure_of_cell < Osmoisis_pressure_of_solution:
    print("Áp suất thẩm thấu trong tế bào nhỏ hơn dung dịch: nước đi ra khỏi tế bào.")
else:
    print("Áp suất thẩm thấu trong tế bào bằng dung dịch: không có sự di chuyển thuần của nước.")

    

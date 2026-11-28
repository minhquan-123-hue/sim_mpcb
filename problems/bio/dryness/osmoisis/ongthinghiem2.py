"""
tiếp tục cho mô tế bào vào trong ống
thí nghiệm có nồng độ chất tan cao
hơn nồng độ chất tan của mô
"""

# câu 1: tính khối lượng nước thoát ra khỏi mô ?
# câu 2: tạo tỷ lệ nước mất / dd ban đầu (gồm nước + chất tan) * 100%
# câu 3: tạo tỷ lệ nước mất / nước ban đầu( chỉ gồm nước ) * 100%

# datas:
mass_of_solution = 50.0#g
solute_percent_rate_before = 2.0#%
solute_percent_rate_after = 5.0#%
hundred_percent = 100.0

# câu 1: 
# tính khối lượng của chất tan
mass_of_solute = (solute_percent_rate_before / hundred_percent) * mass_of_solution
print("khối lượng của chất tan trong mô: ",mass_of_solute,"g")

# tính khối lượng dung dịch còn lại sau khi bị hút nước ra
mass_of_solution_after = mass_of_solute / (solute_percent_rate_after /  hundred_percent)
print("dung dịch còn lại là: ", mass_of_solution_after,"g")

# tính khối lượng nước bị mất đi 
mass_of_water_loss = mass_of_solution - mass_of_solution_after
print("số lượng nước bị mất đi: ",mass_of_water_loss,"g")

# câu 2:
waterloss_solution_rate = (mass_of_water_loss / mass_of_solution) * hundred_percent
print("tỷ lệ nước mất trên dung dịch: ", waterloss_solution_rate,"%")

# câu 3:
waterloss_initwater_rate = (mass_of_water_loss / (mass_of_solution - mass_of_solute)) * hundred_percent
print("tỷ lệ nước mất trên nước ban đầu: ",waterloss_initwater_rate,"%")


# hai tỷ lệ khác nhau vì một cái so sánh nước mất với dung dịch gồm cả chất tan
# còn cái còn lại chỉ là nước mất và nước ban đầu không tính với chất tan.
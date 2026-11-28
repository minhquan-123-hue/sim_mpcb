"""
Put the fucking cell into ông nghiệm
ktra hướng đi của lượng nước khi mà 
chất tan của ống nghiệm lớn hơn
chất tan của tế bào đưa vào
"""

# câu 1: khối lượng chất tan trong dung dịch ban đầu ?
# câu 2: khối lượng nước đã mất đi ?
# câu 3: khối lượng nước còn lại ?

# datas
mass_of_solution = 25.0#g
solute_percent_rate_before = 1.6#%
solute_percent_rate_after = 4.0#%

# câu 1: answer
mass_of_solute = solute_percent_rate_before / 100.0 * mass_of_solution
print("khối lượng chất tan ban đầu: ", mass_of_solute)

# câu 3: answer
mass_of_solution_after = (mass_of_solute / (solute_percent_rate_after / 100.0)) - mass_of_solute
print("khối lượng dung dịch về sau: " , mass_of_solution_after)

# câu 2: answer
mass_of_solution_loss = mass_of_solution - mass_of_solution_after
print("khối lượng dung dịch bị mất đi là: ", mass_of_solution_loss)






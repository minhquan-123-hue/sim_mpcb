"""năng lượng vào - năng lượng ra - năng lượng hao phí = 0"""

# tính E tp , E có ích
# tính hiệu suất 
# tính E tỏa ra 

# datas
glucose = 2.5#mol
atp = 32#mol/glucose
energy_atp_release = 7.3#kcal/mol
energy_glucose_release = 686#kcal/mol

total_energy = glucose * energy_glucose_release
print("total energy =",total_energy)

out_energy = atp * glucose * energy_atp_release
print("out energy =",out_energy)

# con số hiệu suất sẽ không thay đổi
# dù tăng hay giảm số mol của glucose
hieu_suat = out_energy / total_energy
hieu_suat *= 100
print(f"hieu suat {hieu_suat:.2f}%")

# năng lượng này biến thành nhiệt
# và giữ ấm cho cơ thể nên không lãng phí
loss_energy = total_energy - out_energy
print("loss energy =",loss_energy)


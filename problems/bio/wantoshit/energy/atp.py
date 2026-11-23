"""
từ hiệu suất tính số lượng 'gói năng lượng'
"""

# tính E có ích 
# số lượng atp

#datas
energy_release_per_glucose = 686#kcal/mol
hieu_suat_convert_energy_storeinatp = 25.55#%

energy_huu_ich = (energy_release_per_glucose * hieu_suat_convert_energy_storeinatp) / 100
print(f"năng lượng hữu ích: {energy_huu_ich}kcal")

# ta biết 1mol atp = 7.3 kcal
atp_quantity = energy_huu_ich / 7.3
print(f"số lượng atp: {atp_quantity}")
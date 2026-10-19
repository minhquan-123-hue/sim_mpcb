def energy(beta):
    return -0.2*(beta)**2 + 16*beta + 80

beta_1 = 39
beta_efficiency = 40
beta_2 = 41

energy_from_beta_1 = energy(beta_1)
energy_from_beta_efficiency = energy(beta_efficiency)
energy_from_beta_2 = energy(beta_2)

print(f"e1 = {energy_from_beta_1}")
print(f"e_e = {energy_from_beta_efficiency}")
print(f"e_2 = {energy_from_beta_2}")

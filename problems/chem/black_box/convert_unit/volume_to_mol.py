"""branch: conversion => chuyen doi tu the tich ve 
khoi luong sau tinh so luong hat(mol)"""

from problems.chem.black_box.convert_unit.kmol import kg_to_g,cal_tt_mol, mol_to_kmol

# de bai yeu
# doi tu volume => mass
# tu mass lai doi ve kmol 

# constants , datas
H_volume = 100#L
H_own_mass = 0.07#Kg/L
H_mpm = 1#g/mol

def volume_to_mass(volume, own_mass):
    return volume * own_mass

def main():
    H_tt_mkg = volume_to_mass(H_volume, H_own_mass)
    H_tt_mg = kg_to_g(H_tt_mkg)#g
    print(f"chuyen du lieu ve gam => {H_tt_mg:.0f}")
    
    H_tt_mol = cal_tt_mol(H_tt_mg, H_mpm)#mol
    print(f"tinh ra tong so mol:  {H_tt_mol:.2f}")
    H_tt_kmol = mol_to_kmol(H_tt_mol)#kmol
    
    print(f"H total mass: ~{H_tt_mkg:.0f}kg")
    print(f"H total kmol: {H_tt_kmol:.2f}")
 
if __name__ == "__main__":
    main()
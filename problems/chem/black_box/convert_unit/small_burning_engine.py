"""dot chay toan bo nhien lieu"""

from kmol import cal_tt_mol, kg_to_g, mol_to_kmol
#datas , constants
# atoms weight
Carbon = 12#g/mol
Hydro = 1#g/mol
Oxi = 16#g/mol

CH4 = 32#kg == total_mass

#cong thuc tinh total_mol = total_mass / mass_per_mol
#phai doi don vi total_mass tu kg ve g sau do moi tinh duoc
#mass_per_mol cho phan tu CH4
def main():
    mpm_CH4 = Carbon * 1 + Hydro * 4
    print(f"mpm_CH4: {mpm_CH4}g/mol")
    
    ttmass_CH4_g = kg_to_g(CH4)
    print(f"chuyen khoi luong CH4 ve gram: {ttmass_CH4_g}g")
    
    ttmol_CH4 = cal_tt_mol(ttmass_CH4_g,mpm_CH4)
    print(f"tong so mol: {ttmol_CH4}mol")
    
    ttkmol_CH4 = mol_to_kmol(ttmol_CH4)
    print(f"tong so kmol: {ttkmol_CH4}kmol")
    
    
    
if __name__ == "__main__":
    main()
    

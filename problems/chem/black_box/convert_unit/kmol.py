"""quy doi don vi giua mol va kmol, so luong hat 
, khoi luong , khoi luong tren 1 mol , 1 kmol"""

def mol_to_kmol(kmol):
    return kmol / 1000

def kg_to_g(kg):
    return kg * 1000

def cal_tt_mol(tt_mass, mass_per_mol):
    # mass_per_mol = nguyen tu khoi / 1
    return tt_mass / mass_per_mol

def main():
    # constant (atomics weight)
    H = 1
    O = 8
    N = 14
    
    # mocules weight == mass_per_mol
    mpm_O2 = O * 2
    mpm_H2 = H * 2
    mpm_N2 = N * 2
    
    # datas
    total_mass_O2 = 64#kg
    total_mass_H2 = 6#kg
    total_mass_N2 = 14#kg
    
    # kg_to_g == total_mass
    tt_m_O2 = kg_to_g(total_mass_O2)
    tt_m_H2 = kg_to_g(total_mass_H2)
    tt_m_N2 = kg_to_g(total_mass_N2)
    
    
    #tinh mol cua tung phan tu
    tt_mol_O2 = cal_tt_mol(tt_m_O2, mpm_O2)
    tt_mol_H2 = cal_tt_mol(tt_m_H2, mpm_H2)
    tt_mol_N2 = cal_tt_mol(tt_m_N2, mpm_N2)
    
    print(f"mol O2: {tt_mol_O2}")
    print(f"mol H2: {tt_mol_H2}")
    print(f"mol N2: {tt_mol_N2}")
    print()
    print(f"kmol 02 {mol_to_kmol(tt_mol_O2)}")
    print(f"kmol H2 {mol_to_kmol(tt_mol_H2)}")
    print(f"kmol N2 {mol_to_kmol(tt_mol_N2)}")


if __name__ == "__main__":
    main()

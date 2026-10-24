"""Imagine two hydrogen atoms and one oxygen atom form a water molecule. """

# khi ma no co hat nhan nguyen tu giong nhau
# no co the co the ket hop lai bang cac trao doi qua lai
# cac hat electron va no bien thanh atom moi van giu
# cac nguyen to ban dau
def atom_link(atom_same_ele):
    atom_same_ele *= 2
    return atom_same_ele

def mocules_form(atom_ele_1, atom_ele_2):
    new_mocules = atom_ele_1 * atom_ele_2
    return new_mocules


def main():
    Hydrogen = 1
    print(f"Hydrogen before link: {Hydrogen}Hydrogen")
    
    Hydrogen = atom_link(Hydrogen)
    print(f"Hydrogen after link: {Hydrogen}Hydrogen")
    
    # nguyen to oxy co hat nhan khac voi hydrogen
    # khi chung hop voi nhau ta se goi la hop chat
    Oxy = 1
    H20 = mocules_form(Hydrogen,Oxy)
    print(f"2Hydrogen fuck 1Oxy, now we have: H{H20}0")
    

main()
    
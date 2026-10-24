"""mo phong chat thieu khi phan ung"""

def cal_lim_react(mol_H2_real , mol_O2_real):
    
    H2_in_process = 2
    O2_in_process = 1
    H20_out_process = 2
    
    H2_rate = mol_H2_real / H2_in_process
    O2_rate = mol_O2_real / O2_in_process
    
    if H2_rate == O2_rate:
        return "khong con chat han che, phan ung het"
    elif H2_rate > O2_rate:
        return "O2 la chat han che"
    else:
        return "H2 la chat han che"
    

def main():
    H2 = 3
    O2 = 1.5
    
    
    message = cal_lim_react(H2, O2)
    print(message)    

main()
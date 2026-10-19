# tong dien tro he thong trong 
# va cong suat toa nhiet 

def resistance_sum(number_of_cells ,resitance_per_cell):
    N = number_of_cells # o ben trong cell pin co dien tro
    R_int = resitance_per_cell
    
    return N * R_int

def power_emit(current, resistance_sum): #nang luong hao phi bien thanh nhiet
    I = current
    R_sum = resistance_sum
    
    return I**2 * R_sum

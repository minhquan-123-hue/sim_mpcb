"""gioi thieu ve "dien tro tong" & "nang luong hao phi do dong dien lon"""

# bom nuoc tu gieng len dung nang luong dien

def Head_sum(Height , Height_loss): #Height_loss represent for friction
    return Height + Height_loss

def M_dot(volume_flow_rate_per_hour, water_density):
    vfrps = volume_flow_rate_per_hour / 3600
    mass_flow_rate_per_second = water_density * vfrps
    return mass_flow_rate_per_second

def Power_out(m_dot , gravity, total_height):
    return (m_dot * gravity) * total_height # P = A / t , and A = F * D , F = mass * graivity , D = Head_sum

def Power_in(power_out , long_n):
    return power_out / long_n

def Current(power_in,voltage):
    return power_in / voltage

def Power_loss(resistance_sum,current):
    return current**2 * resistance_sum


def main():
    height = 20#m
    height_loss = 3#m
    total_height = Head_sum(height,height_loss)
        
    rho = 1000#kg/m^3
    vfrph = 10#m^3/h
    mfrps = M_dot(vfrph,rho)
    print(f"m_dot: {mfrps:.2f}kg/s")
    
    gravity = 9.8#m/s^2
    power_thuc_nhan = Power_out(mfrps,gravity,total_height)
    print(f"cong_suat_thuc_nhan: {power_thuc_nhan:.2f}watt(J/s)")
    
    long_n = 50/100
    power_dua_vao = Power_in(power_thuc_nhan,long_n)
    print(f"cong_suat_dua_vao: {power_dua_vao:.2f}watt(J/s)")
    
    voltage = 24#V
    current = Current(power_dua_vao,voltage)
    print(f"dong_dien: {current:.2f}Ampere(J/s)")

    R_sum = 0.8#Ohm
    power_mat_tren_duong_di = Power_loss(R_sum,current)
    print(f"cong_suat_mat_tren_duong_di: {power_mat_tren_duong_di:.2f}watt(J/s)")
    

main()
    
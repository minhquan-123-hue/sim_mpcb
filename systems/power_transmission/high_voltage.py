def may_tang_ap(dien_ap_nguon):
    return dien_ap_nguon * 10

def may_ha_ap(dien_ap_da_tang):
    return dien_ap_da_tang / 10

def dong_dien(dien_ap,cong_suat):
    return cong_suat / dien_ap

def cong_suat_hao_phi(dong_dien,dien_tro):
    return dong_dien**2 * dien_tro

def cong_suat_thuc_nhan(cong_suat_hao_phi , cong_suat_dau_vao):
    output = cong_suat_dau_vao - cong_suat_hao_phi
    loss_percent_rate = (cong_suat_hao_phi / cong_suat_dau_vao) * 100
    
    return output,loss_percent_rate

def main():
    
    #new data
    input_power = 5000#Watt - tong so hang qua tram
    resistance = 1.2#Ohm - hang roi vai khi gap o ga
    voltage_frontend = 220#Voltage - so hang tren xe cong
    
    #tu power_source di qua may tang ap
    new_voltage = may_tang_ap(voltage_frontend)
    print(f"dong ap dau vao di qua may tang ap: {new_voltage:.0f}V(J/C)")
    
    #dong dien - tong so xe cong trong 1 second giam xuong 
    #vi moi xe bay co the tro nhieu hang hon
    current = dong_dien(new_voltage,input_power)
    print(f"dong dien moi: {current:.2f}A(C/s)")
    
    #cong suat hao phi - hang roi vai tren duong o ga
    power_loss = cong_suat_hao_phi(current,resistance)
    print(f"cong suat lang phi thanh nhiet: {power_loss:.2f}Watt(J/s)")
    
    #cong suat thuc nhan - so hang o tram sau khi bi mat tren duong
    output_power, loss_percent_rate = cong_suat_thuc_nhan(power_loss,input_power)
    print(f"nang luong thuc nhan: {output_power:.2f}Watt(J/s)")
    print(f"ty le lang phi thanh nhiet: {loss_percent_rate:.2f}%")
    
if __name__ == "__main__":
    main()

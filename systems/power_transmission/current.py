#constant
power = 5000 #W - tổng số hàng qua trạm mỗi giây (J/s)
voltage_end = 220 #Voltage (J/C) số thùng hàng
distance = 500 * 2 # độ dài của dây *2 ddeeer tạo thành mạch kín
resistance = 1.2 #Ohm của toàn bộ đoạn dây 1000m 

def Current(voltage, power):
    return power / voltage

def Power_loss(current, resistance):
    return (current**2) * resistance

def main():
    current = Current(voltage_end, power)
    
    power_loss = Power_loss(current, resistance)
    print(f"năng lượng hao phí - hàng rơi mất: {power_loss:.2f}")
    #phần hao phí bằng bao nhiêu phần trăm của tổng năng lượng
    power_loss_percent = (power_loss / power) * 100
    
    print(f"dòng điện - tổng số xe container: ~{current:.0f}")
    print(f"năng lượng hao phí phần trăm - hàng rơi mất: {power_loss_percent:.2f}%")
    
main()
"""Q generate = Q transfer"""
# hoc cach de can bang nhiet sao cho thiet co 
# the khong qua nong va bi hong 

# trong formula thi cac symbol da triet tieu lan nhau
# ma Power_loss = Q_transfer ==> they are same unit 
def Q_generated(current, resistance_sum):
    return current**2 * resistance_sum

def Balance_heat(h,A,delta_temp):
    Q_transfer = h*A*delta_temp
    
    return Q_transfer

def main():
    
    #so cong suat bi dot thanh nhiet nang
    #cong suat cang lon thi nhiet do cang lon
    I = 50#Ampere
    R = 0.5#ohm
    
    q_gen = Q_generated(I,R)
    print(f"so cong suat sinh bien sinh nhiet: {q_gen:.2f}")
    
    #h.A la do hieu qua cua air,fluid lam
    #giam nhiet do cua vat tren mot don vi dien tich
    #W/m^2K * m^2 => triet tieu dien tich 
    #hi can bo ra nang luong de giam nhiet do
    h = 50#W/Km^2
    A = 1#m^2
    safe_temp = 70#celcuis
    env_temp = 35
    delta_temp = safe_temp - env_temp
    
    q_transfer = Balance_heat(h,A,delta_temp)
    print(f"so cong suat tan nhiet: {q_transfer:.2f}")
    
    if q_gen == q_transfer:
        print(f"ping se giu nguyen ko tang them") 
    elif q_gen < q_transfer:
        print(f"pin se ha nhiet xuong")
    else:
        print(f"pin se tang nhiet len")

main()
    


    


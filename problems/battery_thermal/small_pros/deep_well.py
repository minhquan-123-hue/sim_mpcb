# bom nuoc tu gieng len dung nang luong dien

def Head_sum(Height , Height_loss): #Height_loss represent for friction
    return Height + Height_loss

def M_dot(volume_flow_rate_per_hour):
    rho = 1000 #kg/m^3 a constant
    vfrps = volume_flow_rate_per_hour / 3600
    mass_flow_rate_per_second = rho * vfrps
    return mass_flow_rate_per_second

def 

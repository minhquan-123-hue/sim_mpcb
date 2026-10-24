# write program to give input generate output
"""constant"""
pipe_height = 15  # m
friction_head = 2.5  # m, assumed loss due to friction
volume_flow_rate = 3.6  # m^3/hour
rho = 1000  # kg/m^3
gravity = 9.8  # m/s^2
pump_efficiency = 0.6  #thay với dự liệu thật 

def M_dot(Q_hour):
    Q_second = Q_hour / 3600
    mass_flow_rate = Q_second * rho
    return mass_flow_rate, Q_second

def Pressure(rho, height, gravity):
    return rho * height * gravity

def Power_efficiency(mass_flow_rate, gravity, height):
    return mass_flow_rate * gravity * height

def Power_efficiency_2(Q_second, pressure):
    return Q_second * pressure

def main():
    mass_flow_rate, Q_second = M_dot(volume_flow_rate)

    # Add the friction loss to the terrain height.
    total_height = pipe_height + friction_head

    pressure = Pressure(rho, total_height, gravity)
    hydraulic_power = Power_efficiency(mass_flow_rate, gravity, total_height)
    hydraulic_power_2 = Power_efficiency_2(Q_second, pressure)

    # Input power must be greater than hydraulic power when efficiency < 100%.
    input_power = hydraulic_power / pump_efficiency

    print(f"Mass flow rate: {mass_flow_rate:.3f} kg/s")
    print(f"Flow rate: {Q_second:.6f} m^3/s")
    print(f"Total head: {total_height:.2f} m")
    print(f"Pressure: {pressure:.2f} Pa")
    print(f"Hydraulic power: {hydraulic_power:.2f} W")
    print(f"Cross-check hydraulic power: {hydraulic_power_2:.2f} W")
    print(f"Pump efficiency: {pump_efficiency:.0%}")
    print(f"Final input power: {input_power:.2f} W")

if __name__ == "__main__":
    main()

"""Nồng độ chất tan trong dịch tế bào và các cốc dung dịch (M)."""

C_M1 = 0.3
C_M2 = {
    1: 0.15,
    2: 0.30,
    3: 0.60,
    4: 0.05,
}


def compare_concentrations():
    for beaker, external_concentration in C_M2.items():
        if external_concentration < C_M1:
            relation = "nhỏ hơn"
            water_direction = "đi vào tế bào"
        elif external_concentration == C_M1:
            relation = "bằng"
            water_direction = "không có sự di chuyển thuần"
        else:
            relation = "lớn hơn"
            water_direction = "đi ra khỏi tế bào"

        print(
            f"Cốc {beaker}: C_M2 = {external_concentration:.2f} M "
            f"{relation} C_M1 = {C_M1:.2f} M; nước {water_direction}."
        )


if __name__ == "__main__":
    compare_concentrations()
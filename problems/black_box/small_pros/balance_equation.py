"""
Can bang phuong trinh hoa hoc bang cach thu cac he so.

Vi du:
    H2 + O2 -> H2O

Chi ho tro cong thuc don gian nhu H2O, Fe2O3.
Chua ho tro dau ngoac nhu Ca(OH)2.
"""

import re
from itertools import product


def dem_nguyen_tu(cong_thuc):
    """Tra ve so nguyen tu cua moi nguyen to trong mot chat."""
    tokens = re.findall(r"([A-Z][a-z]?)(\d*)", cong_thuc)

    # Bao dam da doc het cong thuc, khong bo sot ky tu.
    if not tokens or "".join(a + n for a, n in tokens) != cong_thuc:
        raise ValueError(f"Cong thuc khong ho tro: {cong_thuc}")

    atoms = {}
    for element, number in tokens:
        if element not in atoms:
            atoms[element] = 0
        atoms[element] += int(number) if number else 1

    return atoms


def can_bang(he_so, so_nguyen_tu, so_chat_trai):
    """Kiem tra so nguyen tu moi nguyen to co bang nhau hai ben khong."""
    cac_nguyen_to = set()
    for atoms in so_nguyen_tu:
        cac_nguyen_to.update(atoms)

    for element in cac_nguyen_to:
        trai = sum(
            he_so[i] * so_nguyen_tu[i].get(element, 0)
            for i in range(so_chat_trai)
        )
        phai = sum(
            he_so[i] * so_nguyen_tu[i].get(element, 0)
            for i in range(so_chat_trai, len(he_so))
        )

        if trai != phai:
            return False

    return True


def can_bang_phuong_trinh(phuong_trinh):
    trai_text, phai_text = phuong_trinh.split("->")
    trai = [chat.strip() for chat in trai_text.split("+")]
    phai = [chat.strip() for chat in phai_text.split("+")]

    cac_chat = trai + phai
    so_nguyen_tu = [dem_nguyen_tu(chat) for chat in cac_chat]

    # Thu cac bo he so: (1, 1, 1), (1, 1, 2), ...
    # Giu lai bo he so hop le co tong nho nhat.
    he_so_tot_nhat = None

    for he_so in product(range(1, 9), repeat=len(cac_chat)):
        if he_so_tot_nhat is not None:
            if sum(he_so) >= sum(he_so_tot_nhat):
                continue

        if can_bang(he_so, so_nguyen_tu, len(trai)):
            he_so_tot_nhat = he_so

    if he_so_tot_nhat is None:
        raise ValueError("Khong tim thay he so. Hay kiem tra phuong trinh.")

    trai_kq = []
    for i, chat in enumerate(trai):
        if he_so_tot_nhat[i] == 1:
            trai_kq.append(chat)
        else:
            trai_kq.append(str(he_so_tot_nhat[i]) + chat)

    phai_kq = []
    for i, chat in enumerate(phai):
        he_so = he_so_tot_nhat[len(trai) + i]
        if he_so == 1:
            phai_kq.append(chat)
        else:
            phai_kq.append(str(he_so) + chat)

    return " + ".join(trai_kq) + " -> " + " + ".join(phai_kq)


phuong_trinh = input("Nhap phuong trinh, vi du H2 + O2 -> H2O: ")

try:
    print("Phuong trinh da can bang:", can_bang_phuong_trinh(phuong_trinh))
except ValueError as loi:
    print("Loi:", loi)

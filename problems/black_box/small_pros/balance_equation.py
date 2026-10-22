"""
Can bang phuong trinh hoa hoc bang cach thu cac he so nguyen duong.

Vi du:
    H2 + O2 -> H2O
    Fe + O2 -> Fe2O3

Ban hoc tap nay ho tro cong thuc don gian (H2O, Fe2O3).
Chua ho tro dau ngoac nhu Ca(OH)2.
"""

import re
from itertools import product
from math import gcd
from functools import reduce


def parse_formula(formula):
    """Dem so nguyen tu cua moi nguyen to trong mot cong thuc."""
    tokens = re.findall(r"([A-Z][a-z]?)(\d*)", formula)

    # Neu regex khong doc het cong thuc, bao loi thay vi am tham bo qua ky tu.
    if not tokens or "".join(element + number for element, number in tokens) != formula:
        raise ValueError(f"Cong thuc chua duoc ho tro: {formula}")

    atoms = {}
    for element, number in tokens:
        count = int(number) if number else 1
        atoms[element] = atoms.get(element, 0) + count
    return atoms


def parse_equation(equation):
    """Tach phuong trinh thanh cac chat o ve trai va ve phai."""
    if "->" not in equation:
        raise ValueError("Hay dung dau -> de ngan cach hai ve, vi du: H2 + O2 -> H2O")

    left_text, right_text = equation.split("->", 1)
    left = [part.strip() for part in left_text.split("+")]
    right = [part.strip() for part in right_text.split("+")]

    if not all(left) or not all(right):
        raise ValueError("Thieu chat o mot trong hai ve cua phuong trinh.")

    formulas = left + right
    atom_counts = [parse_formula(formula) for formula in formulas]
    return left, right, atom_counts


def balanced(coefficients, atom_counts, number_of_reactants):
    """Kiem tra moi nguyen to co so nguyen tu bang nhau o hai ve khong."""
    elements = set()
    for atoms in atom_counts:
        elements.update(atoms)

    for element in elements:
        left_total = sum(
            coefficients[i] * atom_counts[i].get(element, 0)
            for i in range(number_of_reactants)
        )
        right_total = sum(
            coefficients[i] * atom_counts[i].get(element, 0)
            for i in range(number_of_reactants, len(coefficients))
        )
        if left_total != right_total:
            return False
    return True


def balance_equation(equation, max_coefficient=12):
    """
    Tim bo he so nguyen duong co tong nho nhat.
    Day la cach thu he so de hoc, khong phai thuat toan toi uu cho phuong trinh lon.
    """
    left, right, atom_counts = parse_equation(equation)
    number_of_reactants = len(left)
    number_of_compounds = len(atom_counts)

    best = None
    best_sum = None

    # Thu cac he so 1, 2, ..., max_coefficient.
    # Chon bo he so can bang co tong nho nhat.
    for coefficients in product(range(1, max_coefficient + 1), repeat=number_of_compounds):
        if best_sum is not None and sum(coefficients) >= best_sum:
            continue

        # Bo he so toi gian khong duoc co uoc chung lon hon 1.
        if reduce(gcd, coefficients) != 1:
            continue

        if balanced(coefficients, atom_counts, number_of_reactants):
            best = coefficients
            best_sum = sum(coefficients)

    if best is None:
        raise ValueError(
            "Chua tim thay he so. Hay thu tang max_coefficient "
            "hoac kiem tra lai phuong trinh."
        )

    left_result = " + ".join(
        f"{best[i]} {left[i]}" if best[i] != 1 else left[i]
        for i in range(len(left))
    )
    right_result = " + ".join(
        f"{best[number_of_reactants + i]} {right[i]}"
        if best[number_of_reactants + i] != 1
        else right[i]
        for i in range(len(right))
    )

    return f"{left_result} -> {right_result}", best, atom_counts, number_of_reactants


def main():
    equation = input("Nhap phuong trinh (vi du: H2 + O2 -> H2O): ")

    try:
        result, coefficients, atom_counts, number_of_reactants = balance_equation(equation)
    except ValueError as error:
        print("Loi:", error)
        return

    print("\nPhuong trinh da can bang:")
    print(result)

    print("\nHe so theo thu tu cac chat:", coefficients)
    print("\nKiem tra so nguyen tu:")
    elements = sorted({element for atoms in atom_counts for element in atoms})
    for element in elements:
        left_total = sum(
            coefficients[i] * atom_counts[i].get(element, 0)
            for i in range(number_of_reactants)
        )
        right_total = sum(
            coefficients[i] * atom_counts[i].get(element, 0)
            for i in range(number_of_reactants, len(coefficients))
        )
        print(f"{element}: ve trai = {left_total}, ve phai = {right_total}")


if __name__ == "__main__":
    main()

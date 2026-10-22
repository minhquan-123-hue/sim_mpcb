"""
Mo phong dinh luat bao toan khoi luong trong phan ung:
    2 H2 + O2 -> 2 H2O

Muc tieu hoc:
- Moi nguyen tu la mot object Atom co khoi luong va loai nguyen to.
- Lien ket la cac tham chieu (references) den object Atom khac.
- Phan ung chi thay doi cac lien ket; khong tao hay huy object Atom.
- Vi vay, tong khoi luong nguyen tu trong mo hinh giu nguyen.

Luu y: day la mo hinh hoc tap don gian, khong phai bo mo phong hoa hoc
day du. Khoi luong nguyen tu duoc coi la co dinh; thay doi khoi luong do
nang luong lien ket la rat nho va duoc bo qua trong hoa hoc thong thuong.
"""

from dataclasses import dataclass, field


@dataclass(eq=False)
class Atom:
    """Mot nguyen tu. eq=False giup moi object co danh tinh rieng."""

    atom_id: str
    element_type: str
    mass: float  # don vi khoi luong nguyen tu (u), gia tri gan dung
    bonds: set["Atom"] = field(default_factory=set)

    def __repr__(self) -> str:
        return f"{self.atom_id}({self.element_type})"


def connect(atom_a: Atom, atom_b: Atom) -> None:
    """Tao lien ket hai chieu giua hai object Atom da ton tai."""
    atom_a.bonds.add(atom_b)
    atom_b.bonds.add(atom_a)


def disconnect_all(atoms: list[Atom]) -> None:
    """Xoa cac lien ket, khong xoa bat ky object Atom nao."""
    for atom in atoms:
        atom.bonds.clear()


def sum_total_mass(atoms: list[Atom]) -> float:
    """Cong khoi luong cua tat ca nguyen tu trong he."""
    return sum(atom.mass for atom in atoms)


def count_elements(atoms: list[Atom]) -> dict[str, int]:
    """Dem so nguyen tu theo tung loai nguyen to."""
    counts: dict[str, int] = {}
    for atom in atoms:
        counts[atom.element_type] = counts.get(atom.element_type, 0) + 1
    return counts


def show_bonds(atoms: list[Atom], title: str) -> None:
    """In cac cap lien ket, moi cap chi in mot lan."""
    print(f"\n{title}")
    shown_pairs: set[tuple[str, str]] = set()

    for atom in atoms:
        for neighbor in atom.bonds:
            pair = tuple(sorted((atom.atom_id, neighbor.atom_id)))
            if pair not in shown_pairs:
                shown_pairs.add(pair)
                print(f"  {atom} -- {neighbor}")

    if not shown_pairs:
        print("  (khong co lien ket)")


def rearrange_bonds(reactants_list: list[Atom]) -> None:
    """
    Mo phong 2 H2 + O2 -> 2 H2O.

    Ham nay chi thay doi cac lien ket giua cac Atom co san.
    Khong tao Atom moi va khong huy Atom nao.
    """
    hydrogen = [a for a in reactants_list if a.element_type == "H"]
    oxygen = [a for a in reactants_list if a.element_type == "O"]

    if len(hydrogen) != 4 or len(oxygen) != 2:
        raise ValueError(
            "Phan ung demo can dung 4 nguyen tu H va 2 nguyen tu O."
        )

    # Pha bo lien ket cu H-H va O-O. Cac object nguyen tu van con nguyen.
    disconnect_all(reactants_list)

    # Tao lien ket moi: moi O ket noi voi 2 H de tao thanh H2O.
    connect(oxygen[0], hydrogen[0])
    connect(oxygen[0], hydrogen[1])
    connect(oxygen[1], hydrogen[2])
    connect(oxygen[1], hydrogen[3])


def main() -> None:
    # Khoi tao 6 object Atom tu dau. Cac object nay se duoc dung truoc
    # va sau phan ung, khong co Atom nao duoc tao them trong reaction.
    h1 = Atom("H1", "H", 1.008)
    h2 = Atom("H2", "H", 1.008)
    h3 = Atom("H3", "H", 1.008)
    h4 = Atom("H4", "H", 1.008)
    o1 = Atom("O1", "O", 15.999)
    o2 = Atom("O2", "O", 15.999)

    # Danh sach nay chinh la toan bo cac nguyen tu trong he.
    atoms = [h1, h2, h3, h4, o1, o2]

    # Tao cac phan tu reactants: 2 phan tu H2 va 1 phan tu O2.
    connect(h1, h2)
    connect(h3, h4)
    connect(o1, o2)

    # Luu danh tinh object de chung minh khong co Atom nao bi thay the.
    original_object_ids = {id(atom) for atom in atoms}
    mass_before = sum_total_mass(atoms)
    counts_before = count_elements(atoms)

    print("PHAN UNG: 2 H2 + O2 -> 2 H2O")
    show_bonds(atoms, "TRUOC PHAN UNG (cac lien ket cu):")
    print(f"So nguyen tu truoc: {counts_before}")
    print(f"Tong khoi luong truoc: {mass_before:.3f} u")

    # Buoc chinh: chi sap xep lai cac lien ket.
    rearrange_bonds(atoms)

    mass_after = sum_total_mass(atoms)
    counts_after = count_elements(atoms)
    final_object_ids = {id(atom) for atom in atoms}

    show_bonds(atoms, "SAU PHAN UNG (cac lien ket moi):")
    print(f"So nguyen tu sau: {counts_after}")
    print(f"Tong khoi luong sau: {mass_after:.3f} u")

    print("\nKIEM TRA BAO TOAN:")
    print(f"Khoi luong co bang nhau? {mass_before == mass_after}")
    print(f"So nguyen tu moi nguyen to co giu nguyen? {counts_before == counts_after}")
    print(f"Bo object Atom co giu nguyen? {original_object_ids == final_object_ids}")
    print(f"So object Atom truoc/sau: {len(original_object_ids)}/{len(final_object_ids)}")

    print("\nY NGHIA:")
    print("- Cac object Atom van la H1, H2, H3, H4, O1, O2.")
    print("- Chi cac lien ket giua chung thay doi.")
    print("- Tong khoi luong trong mo hinh giu nguyen.")


if __name__ == "__main__":
    main()

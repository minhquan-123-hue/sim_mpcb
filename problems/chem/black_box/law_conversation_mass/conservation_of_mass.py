# Mo phong: 2 H2 + O2 -> 2 H2O

# Moi dong la mot nguyen tu: ten, loai, khoi luong
atoms = [
    {"name": "H1", "type": "H", "mass": 1.008},
    {"name": "H2", "type": "H", "mass": 1.008},
    {"name": "H3", "type": "H", "mass": 1.008},
    {"name": "H4", "type": "H", "mass": 1.008},
    {"name": "O1", "type": "O", "mass": 15.999},
    {"name": "O2", "type": "O", "mass": 15.999},
]

# Moi cap la mot lien ket giua hai nguyen tu
bonds = [("H1", "H2"), ("H3", "H4"), ("O1", "O2")]


def total_mass():
    total = 0
    for atom in atoms:
        total = total + atom["mass"]
    return total


print("Truoc phan ung:")
print("So nguyen tu:", len(atoms))
print("Tong khoi luong:", total_mass())
print("Lien ket:", bonds)

# Phan ung: chi thay danh sach lien ket.
# Khong them hay xoa nguyen tu nao.
bonds = [
    ("O1", "H1"), ("O1", "H2"),
    ("O2", "H3"), ("O2", "H4")
]

print("\nSau phan ung:")
print("So nguyen tu:", len(atoms))
print("Tong khoi luong:", total_mass())
print("Lien ket:", bonds)

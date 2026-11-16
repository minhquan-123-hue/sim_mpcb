"""từ số lượng hydrogen bonds tính số lượng neucleotides của A,T,G,C và tổng neucleotides"""

#datas
Hydrogen = 3900
# H = 2A + 3G
# A/G = 1/2 => 2A = 1G
# H = 2A + 6A

Ademine = Hydrogen / 8
Themine = Ademine
Guamine = 2*Ademine
Cytosine = Guamine

Neucleotides = Ademine + Themine + Guamine + Cytosine 
print("tổng số gạch thông tin:",Neucleotides)
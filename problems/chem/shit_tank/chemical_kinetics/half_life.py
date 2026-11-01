"""Tinh chu ky ban ra va thoi gian suy giam nong do cho dong hoc bac 1."""

from math import log

k = 0.05 #ngay^-1
Co = 80 #mg/L
Ct = 10 #mg/L

# tinh chu ky ban ra
# neu khong dung cong thuc nay se phai tinh ra so mol da bi phan huy
# sau lay so mol con lai de thuc hien tinh tiep so mol bi phan huy
# 80*0.05 + (80-4)*0.05 + (80-4-3.8)*0.05 + (80-4-3.8-3.61)*0.05 + (80-4-3.8-3.61-3.43)*0.05 + (80-4-3.8-3.61-3.43-3.25)*0.05 + (80-4-3.8-3.61-3.43-3.25-3.08)*0.05 + (80-4-3.8-3.61-3.43-3.25-3.08-2.91)*0.05 + (80-4-3.8-3.61-3.43-3.25-3.08-2.91-2.75)*0.05 + (80-4-3.8-3.61-3.43-3.25-3.08-2.91-2.75 - 2,59)*0,05 
# va sau do moi ra duoc so ngay bang cach dem chay
t_half = log(2) / k
print("Chu ky ban ra cua dong hoc bac 1 la: ", t_half, "ngay")

# tinh thoi gian suy giam nong do
t = 1
# Ct = Co * (log(2) ** (-k * t))
# log(Ct / Co) = -k * t
t = log(Ct / Co) / (-k)
print("Thoi gian suy giam nong do tu", Co, "mg/L den", Ct, "mg/L la: ", t, "ngay")

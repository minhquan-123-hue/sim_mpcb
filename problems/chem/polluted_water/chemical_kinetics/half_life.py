"""Tinh chu ky ban ra va thoi gian suy giam nong do cho dong hoc bac 1."""

from math import log

k = 0.05  # ngay^-1
initial_concentration = 80  # mg/L
target_concentration = 10  # mg/L

half_life = log(2) / k
time_to_target = log(initial_concentration / target_concentration) / k

print(f"Chu ky ban ra: {half_life:.2f} ngay")
print(
    f"Thoi gian de nong do giam tu {initial_concentration:g} xuong "
    f"{target_concentration:g} mg/L: {time_to_target:.2f} ngay"
)

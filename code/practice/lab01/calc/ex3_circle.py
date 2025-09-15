'''
=== Nội dung bài ===
Nhập vào bán kính r của hình tròn. Tính và in ra chu vi và diện tích của hình tròn đó.
'''

import numpy as np

print("Radius and area of circle")
r = float(input("Moi ban nhap ban kinh: "))
c = 2 * np.pi * r
s = (r ** 2) * np.pi

print(f"Chu vi hinh tron co ban kinh la {r}: {c:.2f}")
print(f"Dien tich hinh tron co ban kinh la {r}: {s:.2f}")
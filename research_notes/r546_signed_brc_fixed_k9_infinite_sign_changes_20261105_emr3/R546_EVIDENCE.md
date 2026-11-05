# R546 精确执行证据（2026-11-05，作者侧）

## 可复现命令

python R546_VERIFY.py
python R546_INDEPENDENT.py

执行器：Python 3 / fractions.Fraction / math.isqrt / math.comb；独立矩阵程序另外使用 SymPy 的 Berkowitz 精确行列式。Rouché 证明中的所有判断均使用精确整数或有理数，数值根只用于初期选择随后固定的有理圆心。

## 已执行输出摘录

R546_RATIONAL_ROUCHE_PASS degree 17 Catalan 4862 p2 5985
disk_count 17 disjoint_pairs 136 radius 1/1000
max_Rouche_ratio_lt_1/40 True
dominant_y_lower = 8.11111898
other_y_upper = 4.24004831
dominant_X_gt 47880 other_X_lt 101745/4
first_1025: positive 516, negative 509, zero 0, adjacent_sign_changes 295
first_changes = [5,8,12,15,19,22,26,29,33,36,40,43,46,50,53,57,60,64,67,71,74,78,81,85]

R546_INDEPENDENT_RAW_PASS k 9 H/B 18 raw_matrices 12
Original matrix sign sample m=1:+,2:+,3:+,4:+,5:-,6:-,8:+,10:+,12:-,16:+,20:-,24:+.

完整检验参数和断言在两份源码中，下一读者可重新执行。验证覆盖精确根盘17个、盘间136对、原始系数18项、原始矩阵12项、回归序列前1025阶。全阶定理由 Rouché 和部分分式振荡论证给出，并非有限序列外推。

## 控制与数学审阅

冻结输入 R462: 18783e01e3646c72b7aab3b16d3f565e83e6446f；上一次不可变作者前沿 R545: c3ba2406d9dfc990cb58e962ad812608bf35d7b0。结果为作者侧证明及精确证书；正式独立 Driver 审阅、原生任务 CLAIM 和 Result 需各自取得实际授权及回执。
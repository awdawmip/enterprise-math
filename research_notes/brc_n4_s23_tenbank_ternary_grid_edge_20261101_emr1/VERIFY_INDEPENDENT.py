"""Independent NumPy integer/vectorized check of the 11-coin ternary S23 grid."""
import numpy as np

M20 = np.array([
    [10, 10, 0, 0, 0, 0], [9, 11, 0, 0, 0, 0],
    [0, 0, 20, 0, 0, 0], [0, 0, 0, 10, 10, 0],
    [0, 0, 0, 2, 18, 0], [0, 0, 0, 0, 0, 20],
], dtype=np.int32)
BOXES = [
    "34 24 34 24", "34 23 34 34", "34 34 34 23",
    "24 24 12 12", "12 12 24 34", "12 13 23 24",
    "23 34 12 13", "24 34 12 14", "13 12 13 13",
    "12 12 14 12",
]
GROUP = np.array([0, 0, 1, 2, 2, 3])
A_SLOT = np.array([0, 0, 0, 1, 1, 1])
B_SLOT = np.array([0, 0, 1, 0, 0, 2])
Q160 = np.zeros((10, 6, 4), dtype=np.int32)
for label, boxline in enumerate(BOXES):
    pair = [tuple(int(c) - 1 for c in piece) for piece in boxline.split()]
    for i in range(6):
        for time in pair[GROUP[i]]:
            Q160[label, i, time] = 80

histogram = {}
for start in range(0, 3**11, 4096):
    numbers = np.arange(start, min(start + 4096, 3**11), dtype=np.int32)
    digits = np.stack([(numbers // (3**j)) % 3 for j in range(11)], axis=1)
    a = digits[:, A_SLOT]
    b = digits[:, 2 + B_SLOT]
    c = digits[:, 5:11]
    f8 = np.stack([
        4*a, 2*(2-a)*b, (2-a)*(2-b)*c,
        (2-a)*(2-b)*(2-c)
    ], axis=2)
    p160 = np.einsum('ij,njt->nit', M20, f8, optimize=True)
    losses = np.abs(p160[:, None] - Q160[None]).sum(axis=-1).max(axis=-1)
    best = losses.min(axis=-1)
    values, counts = np.unique(best, return_counts=True)
    for value, count in zip(values, counts):
        histogram[int(value)] = histogram.get(int(value), 0) + int(count)

assert sum(histogram.values()) == 177147
assert max(histogram) == 160
assert histogram[160] == 169441
assert sum(n for v, n in histogram.items() if v < 160) == 7706
print('PASS_INDEPENDENT_NUMPY_INTEGER_TERNARY_GRID')
print('policies=177147 max_TV=160/320=1/2 equal_half=169441 below_half=7706')


"""Independent exact-set implementation of the S23 3-box obstruction."""
from itertools import combinations, product

H = (2, 3, 4)
G = (3, 4)
S = {(1, 1, 1, 1)}
S.update((1, 1, x, y) for x, y in product(H, repeat=2))
S.update((x, y, 1, 1) for x, y in product(H, repeat=2))
S.update((2, x, 2, y) for x, y in product(H, repeat=2))
S.update((x, u, y, v) for x, u, y, v in product(G, H, G, H))
assert len(S) == 64

# Independently index via sorted set of actual tuples, not JS string order.
points = tuple(sorted(S))
boxes = []
for omitted in product(range(1, 5), repeat=4):
    incidence = sum(
        1 << idx for idx, signature in enumerate(points)
        if all(signature[j] != omitted[j] for j in range(4))
    )
    boxes.append((omitted, incidence))
assert len(boxes) == 256

full = (1 << 64) - 1
checked = 0
max_cover = 0
for (a, mask_a), (b, mask_b), (c, mask_c) in combinations(boxes, 3):
    covered = mask_a | mask_b | mask_c
    count = covered.bit_count()
    if count > max_cover:
        max_cover = count
    assert covered != full, (a, b, c)
    checked += 1
assert checked == 2763520
assert max_cover == 63
print('INDEPENDENT_PASS_S23_THREE_CHOICE_SET_COVER')
print(f'points={len(points)};boxes={len(boxes)};triples={checked};max_covered={max_cover}')

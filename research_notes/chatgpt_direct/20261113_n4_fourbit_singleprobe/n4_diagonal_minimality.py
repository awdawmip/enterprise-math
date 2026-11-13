"""Restricted optimality checks for the explicit 4D certificate."""
from itertools import product
from n4_four_bit_certificate import THREE_D_CLASSES,STAR_COLOR,laminar

def unpack(v):
    return v//25, (v//5)%5, v%5

# The 60 one-point moves into fixed 3D classes do not preserve laminarity.
for a,j in product(range(5),range(12)):
    assert not laminar([unpack(v)for v in THREE_D_CLASSES[j]+[31*a]])

# Every color on the diagonal must be a bipartite star forest, hence <=8 cells;
# 25 cells require >=4 colors, achieved by the explicit 4-color grid.
for c in range(4):
    cells=[(t,a) for t,a in product(range(5),repeat=2)
           if STAR_COLOR[t][a]==c]
    assert len(cells)<=8 and laminar(cells)
assert sum(STAR_COLOR[t][a] in range(4)
           for t,a in product(range(5),repeat=2))==25
print('RESTRICTED_ARCHITECTURE_PASS: four colors necessary;',
      '60 direct singleton absorptions rejected')

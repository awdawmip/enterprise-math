from itertools import product
from collections import Counter
from fractions import Fraction as Q
from math import isqrt
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
from os import environ
from hashlib import sha1
source_root = Path(environ["EM_SOURCE_ROOT"]).resolve()
p = source_root / "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"
buf=p.read_bytes()
assert sha1(b'blob '+str(len(buf)).encode()+b'\x00'+buf).hexdigest()=='300a96e3dc24bf6fff73743037a0347a8bc83176'
spec=spec_from_file_location('signed_brc',p); mod=module_from_spec(spec); spec.loader.exec_module(mod)
assert mod.shortest_path_multiplicity((6,6,0,0,0,0))==924
cols=[(0,0,3,6,6,6),(1,3,4,4,4,5),(1,4,4,4,4,4),(3,3,3,4,4,4)]
weights=[Q(1,12),Q(1,2),Q(1,4),Q(1,6)]
words=['XXYY','XYXY','XYYX','YXXY','YXYX','YYXX']
tbl=[Q(0)]*6
for c,weight in zip(cols,weights):
    assert sum(c)==21
    # Slots (X index, 0) and (Y column size, 1) order all selected sources.
    # X source numbered 1,...,6 occurs before a Y source of column size c iff x<=c.
    counter=Counter()
    for x1,x2,y1,y2 in product(range(6),repeat=4):
        events=[(x1+1,0,'X'),(x2+1,0,'X'),(c[y1],1,'Y'),(c[y2],1,'Y')]
        counter[''.join(x[-1] for x in sorted(events))]+=1
    row=[counter[w] for w in words]
    print(c,row)
    tbl=[s+weight*Q(v,6**4) for s,v in zip(tbl,row)]
assert tbl==[Q(7,24),Q(7,72),Q(7,24),Q(7,72),Q(7,72),Q(1,8)]
full=[Q(6,7)*v+Q(int(j==5),7) for j,v in enumerate(tbl)]
assert full==[Q(1,4),Q(1,12),Q(1,4),Q(1,12),Q(1,12),Q(1,4)]
# Each bound is in units of 1/D.
D=10**80
def root(k): return isqrt(k*D**2),isqrt(k*D**2)+1
s2lo,s2hi=root(2);s6lo,s6hi=root(6)
hlo=isqrt((4*D-s6hi-s2hi)*D//8);hhi=isqrt((4*D-s6lo-s2lo)*D//8)+1
lo=Q(12*hlo-s2hi,7*D);hi=Q(12*hhi-s2lo,7*D)
place=10**18
print('W 1e-18 enclosure',lo*place//1, -((-hi*place)//1))

from pathlib import Path
from itertools import combinations
from hashlib import sha256
H=Path(__file__).resolve().parent
Q0={0,1,2,3,4,51,64,71,74}; D={1,2,64}; O=sorted(set(range(84))-Q0)
assert D<=Q0 and len(O)==75
p=H/'distance3_remove1264_180.bin'
with p.open('wb') as f:
    for A in combinations(O,3):
        q=sorted((Q0-D)|set(A))
        f.write(bytes(q)+bytes(18))
assert p.stat().st_size==67525*27
print(f'PREFIX180_FREEZE rows=67525 bytes={p.stat().st_size} sha256={sha256(p.read_bytes()).hexdigest()}')

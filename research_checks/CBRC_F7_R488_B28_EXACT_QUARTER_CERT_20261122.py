#!/usr/bin/env python3
"""F7 B25 exact quarter-grid certificate; exhaustive original-input integer check."""
from pathlib import Path
from collections import Counter
import hashlib, base64, itertools, zlib

B = 28
DATA = "F7_R488_B28_Exact_Quarter_Witness_20261122.b85"
SHA256 = "fa01c131e431a7ff708dbffc9974c44dcb8e2f126349bcbe8ba6ee5bc7a1fd6d"

def indexed_keys():
    R = list(range(-2*B, 2*B+1))
    T = {r: range(2*r-min(B,r+B), 2*r-max(-B,r-B)+1) for r in R}
    ix = {}
    for i, r in enumerate(R):
        for u in R[i+1:]:
            for v in itertools.chain(T[r], T[u]):
                for rr in (r,u):
                    x, y = 2*rr-v, rr-v
                    key = (abs(x),y)
                    if y and key not in ((2,1),(1,-1)) and key not in ix:
                        ix[key] = len(ix)
    return ix

def main():
    encoded = (Path(__file__).resolve().parent.parent / 'research_artifacts' / DATA).read_text(encoding="utf8").strip()
    values = zlib.decompress(base64.b85decode(encoded))
    assert hashlib.sha256(values).hexdigest() == SHA256
    ix = indexed_keys()
    assert len(ix) == len(values) == 16294
    assert Counter(values) == {2:10390, 3:4709, 4:1195}
    def Q(x,y):
        if y == 0:
            return 0 if x == 0 else 4
        key = (abs(x),y)
        if key in ((2,1),(1,-1)):
            return 2
        return values[ix[key]] if key in ix else 2

    assert Q(0,0)==0 and Q(2,1)==2 and Q(-1,-1)==2
    counts = Counter()
    for a,b,c,d in itertools.product(range(-B,B+1), repeat=4):
        k = a-2*b-c+2*d
        d4 = Q(a+k,b+k)+Q(c-k,d-k)-Q(a,b)-Q(c,d)
        assert abs(d4) <= 2, (a,b,c,d,k,d4)
        counts[d4] += 1
    assert dict(counts) == {-2:226326, -1:2236954, 0:5104257, 1:2657374, 2:331090}
    assert sum(counts.values()) == 57**4 == 10556001
    print("CERTIFIED exact finite-box e_B=1/2 for B<=28")
    print("inputs",sum(counts.values()),"indexed q coords",len(values))
    print("tight",counts[-2]+counts[2],"histogram",dict(sorted(counts.items())))
    print("data_sha256",SHA256)
if __name__ == "__main__":
    main()

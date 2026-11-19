"""Independent vectorized exact k=10 boundary census and priority partition.
Frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run from the directory containing all prior sorted uint64 binary inputs.
"""
from pathlib import Path
import hashlib
import json
import numpy as np

Q0, QMAX, NQ, K, N = 262145, 524287, 131072, 10, 1 << 32
A = np.arange(Q0, QMAX + 1, 2, dtype=np.int64)
assert len(A) == NQ
ids = []
raw_t = [0] * 22
nraw = 0
num_00 = 0
for j in range(19):
    y = np.bitwise_xor(K * A, np.int64(1 << j))
    for i in range(19):
        if i > 0 and j > 0:
            continue
        d = y - (1 << i)
        assert np.all((d > 0) & (d < N))
        for t in range(1, 22):
            b = d // t
            good = ((d % t) == 0) & (b >= Q0) & (b <= QMAX) & ((b & 1) == 1)
            n = int(np.count_nonzero(good))
            if n:
                raw_t[t] += n
                nraw += n
                if i == j == 0:
                    num_00 += n
                r = (np.flatnonzero(good).astype(np.uint64) * NQ + ((b[good] - Q0) // 2).astype(np.uint64))
                ids.append(r)
pairs = np.unique(np.concatenate(ids))
assert len(pairs) > 0
pairs.astype('<u8').tofile('D10_numpy.bin')
assert Path('D10_numpy.bin').read_bytes() == Path('D10.bin').read_bytes()
prior = []
prior_files = ['PREFIX928_R6_SORTED_PAIR_IDS.bin', 'W2.bin','W3.bin','D4_sorted_cpp.bin', 'W5.bin', 'D6.bin', 'W7.bin','D8.bin','W9.bin']
for f in prior_files:
    v = np.fromfile(f, dtype='<u8')
    assert np.all(v[1:] > v[:-1]), f
    prior.append(v)
a = Q0 + 2 * (pairs // NQ).astype(np.int64)
b = Q0 + 2 * (pairs % NQ).astype(np.int64)
b_domain = np.arange(Q0,QMAX + 1,2,dtype=np.int64)
r = np.ones(NQ,dtype=np.int64)
s_class=np.zeros(NQ,dtype=bool)
late_class=np.zeros(NQ,dtype=bool)
for n in range(1,53):
    r = (2 * r) % b_domain
    hit = (r==1) | (r==(b_domain-1))
    if n <= 31:
        s_class |= hit
    else:
        late_class |= hit
assert s_class.sum() == 24
late_only = late_class & ~s_class
assert late_only.sum() == 91
late_vals = set(b_domain[late_only].tolist())
late_vals.update([262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287])
assert len(late_vals) == 104
L = np.array(sorted(late_vals),dtype=np.int64)
T = Q0+2*((77081 * np.arange(1024,dtype=np.int64)+12345) % NQ)

def membership(z, arr):
    j = np.searchsorted(arr,z)
    return (j < arr.size) & (arr[np.minimum(j,arr.size-1)]==z)

BZS = ((b < 33 * ((N+a-1)//a)) |
       (a < 33 * ((N+b-1)//b)) |
       s_class[(b-Q0)//2] |
       ((a // np.gcd(a,b))*b < N))
V = (np.isin(a,L) | np.isin(b,L) |
     ((a>=500001) & np.isin(b,T)) | ((b>=500001) & np.isin(a,T)))
old_hits = [membership(pairs,z) for z in prior]
conds = [BZS,old_hits[0],V,*old_hits[1:]]
labels = ['BZS','U','V','W2','W3','D4','W5','D6','W7','D8','W9']
remaining = np.ones(len(pairs),dtype=bool)
counts={}
for lbl,cond in zip(labels,conds):
    hit = remaining & cond
    counts[lbl] = int(np.count_nonzero(hit))
    remaining &= ~hit
counts['NEW'] = int(np.count_nonzero(remaining))
new_ids=pairs[remaining]
new_ids.astype('<u8').tofile('NEW10_numpy.bin')
assert Path('NEW10_numpy.bin').read_bytes() == Path('NEW10.bin').read_bytes()
assert sum(counts.values()) == pairs.size
result = {
 'raw':nraw,'raw_t':[raw_t[t] for t in range(1,22)],'raw_i0j0':num_00,
 'unique':int(pairs.size),'priority_disjoint':counts,
 'prior_union':7552031686,'new_union':7552031686+counts['NEW'],
 'remaining':NQ*NQ-7552031686-counts['NEW'],
 'sha256_D10':hashlib.sha256(Path('D10_numpy.bin').read_bytes()).hexdigest(),
 'sha256_NEW10':hashlib.sha256(Path('NEW10_numpy.bin').read_bytes()).hexdigest(),
 'first_new_pair':[int(Q0+2*(new_ids[0]//NQ)), int(Q0+2*(new_ids[0]%NQ))]
}
print(json.dumps(result,ensure_ascii=False,indent=2))
Path('k10_numpy_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

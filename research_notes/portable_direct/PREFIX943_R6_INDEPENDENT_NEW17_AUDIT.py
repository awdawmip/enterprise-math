"""PREFIX-943 independent exhaustive NEW17 old-certificate nonoverlap audit.
Input: NEW17.bin plus 13 SHA-pinned predecessor sorted uint64 little-endian arrays.
Run in directory containing prefix941_inputs/. No formal X6 claim is made.
"""
from pathlib import Path
import numpy as np

L,U,Q=262145,524287,131072
N=1<<32
root=Path(__file__).resolve().parent/'prefix941_inputs'
old=['PREFIX928_R6_SORTED_PAIR_IDS.bin','W2.bin','W3.bin','D4_sorted_cpp.bin',
     'W5.bin','D6.bin','W7.bin','D8.bin','W9.bin','D10.bin',
     'W11.bin','W13.bin','W15.bin']
new=np.memmap(root/'NEW17.bin',dtype='<u8',mode='r')
assert np.all(new[:-1]<new[1:]),'duplicate or unsorted NEW17'
a=L+2*(new//Q).astype(np.int64)
b=L+2*(new%Q).astype(np.int64)
assert np.all((a>=L)&(a<=U)&(b>=L)&(b<=U))
assert np.all((a&1)==1) and np.all((b&1)==1)
moduli=np.arange(L,U+1,2,dtype=np.int64)
r=np.ones(Q,dtype=np.int64)
E=np.zeros(Q,dtype=bool);D=np.zeros(Q,dtype=bool)
for depth in range(1,53):
    r=(2*r)%moduli
    hit=(r==1)|(r==moduli-1)
    if depth<=31:E |= hit
    else:D |= hit&(~E)
assert E.sum()==24
D &= ~E
assert D.sum()==91
Lrows=set(moduli[D].tolist())
Lrows.update([262145,321651,440667,440669,524273,524275,524277,
              524279,524281,524283,524285,440665,524287])
assert len(Lrows)==104
isL=np.zeros(Q,dtype=bool)
isL[(np.array(sorted(Lrows))-L)//2]=True
isT=np.zeros(Q,dtype=bool)
for n in range(1024):isT[(77081*n+12345)%Q]=True
old_bzs=(b<33*((N+a-1)//a))|(a<33*((N+b-1)//b))|E[(b-L)//2]|((a//np.gcd(a,b))*b<N)
old_v=isL[(a-L)//2]|isL[(b-L)//2]|((a>=500001)&isT[(b-L)//2])|((b>=500001)&isT[(a-L)//2])
assert not np.any(old_bzs),f'BZS overlap {old_bzs.sum()}'
assert not np.any(old_v),f'V overlap {old_v.sum()}'
print('NEW17 BZS=0, V=0')
for name in old:
    arr=np.memmap(root/name,dtype='<u8',mode='r')
    shared=np.intersect1d(new,arr,assume_unique=True)
    assert not len(shared),(name,len(shared))
    print(name,'overlap=0','old_count=',len(arr))
print('NEW17 fully old-disjoint',len(new))

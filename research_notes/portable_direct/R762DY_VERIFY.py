#!/usr/bin/env python3
"""R762DY exact 3-adic full-three-coordinate BRC kernel verifier.

Python 3, NumPy 2.3.5 (or compatible int64 NumPy). Every arithmetic
operation is integer; all moduli <= 243 so int64 additions are exact.
"""
from collections import Counter
from hashlib import sha256
import json
import numpy as np

SHIFTS=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))

def cyclic_power(q,n,mod):
    arr=np.zeros((q,q,q),dtype=np.int64)
    arr[0,0,0]=1
    for _ in range(n):
        arr=sum((np.roll(arr,shift=delta,axis=(0,1,2))
                 for delta in SHIFTS))%mod
    return arr

def kernel(s):
    q=3**s
    original=cyclic_power(q,q,3*q)
    assert np.count_nonzero(original%3)==0
    return original//3

def main():
    kernels={s:kernel(s) for s in range(1,5)}
    for s in (2,3,4):
        assert np.array_equal(kernels[s][::3,::3,::3]%(3**(s-1)),kernels[s-1])
    a=kernels[4]
    hist=dict(sorted((str(k),int(v)) for k,v in Counter(a.ravel().tolist()).items()))
    expected={
        '0':352564,'2':1,'3':108,'6':60,'9':1352,
        '12':24,'15':72,'18':2010,'24':12,'27':85716,
        '30':24,'32':6,'33':24,'36':1380,'39':96,
        '45':1080,'51':30,'54':83388,'56':12,
        '63':1692,'72':1728,'74':8,'75':24,'78':30}
    assert hist==dict(sorted(expected.items()))
    valuation_classes=[
        int(np.count_nonzero(a%3!=0)),
        int(np.count_nonzero((a%3==0)&(a%9!=0))),
        int(np.count_nonzero((a%9==0)&(a%27!=0))),
        int(np.count_nonzero((a%27==0)&(a%81!=0))),
        int(np.count_nonzero(a==0))
    ]
    assert valuation_classes==[27,504,9242,169104,352564]
    assert sum(valuation_classes)==81**3
    # The 27 first-level units lie exactly in the order-3^3 subgroup.
    assert np.count_nonzero(a[::27,::27,::27]%3)!=0
    assert np.count_nonzero(a[::27,::27,::27]%3)==27
    digest=sha256(np.asarray(a,dtype="<i8",order="C").tobytes()).hexdigest()
    assert digest=="585aec88800aeca4aa3c55efb78c4187e292510731fa6d0cb03853f2a194c417"
    result={
        "theorem":"R762DY",
        "source":"P=1+X+Z+XY+YZ+XYZ in Z[C_q^3]",
        "author_result":"PASS",
        "numerical_model":"exact int64 cyclic six-shift recurrence modulo 3^(s+1), s<=4",
        "numpy_version":np.__version__,
        "s_levels":[1,2,3,4],
        "s4_positions":int(a.size),
        "s4_mod81_residue_histogram":hist,
        "s4_quotient_v3_classes_0_1_2_3_ge4":valuation_classes,
        "nested_full_array_congruences":[
            "K4 embedded order27 subgroup mod27 equals K3",
            "K3 embedded order9 subgroup mod9 equals K2",
            "K2 embedded order3 subgroup mod3 equals K1"
        ],
        "sha256_K4_int64_le_C_order":digest,
        "review_status":"NOT_REVIEWED",
        "next":"all-horizon full three-coordinate gcd content; licensed signed native updates"
    }
    print(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2))
    return result

if __name__=="__main__": main()

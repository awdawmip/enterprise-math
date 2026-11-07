#!/usr/bin/env python3
"""PREFIX-573 exact modular Hankel certificate for the frozen native X6 BRC model.
Requires unchanged published PREFIX565 and PREFIX566 certificates in same folder.
"""
import json
from collections import Counter
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN, ROOTS, ZERO_ROOT, klass, EXPECTED
from PREFIX566_gate_quotient_certificate import marginal_gate_rows, weighted_quotient
P=1000003
PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"

def determinant(A):
    A=[row[:] for row in A]
    n=len(A); d=1
    for k in range(n):
        i=next((i for i in range(k,n) if A[i][k]),None)
        if i is None:return 0
        if i!=k:
            A[i],A[k]=A[k],A[i];d=-d
        q=A[k][k]
        d=d*q%P
        inv=pow(q,-1,P)
        for i in range(k+1,n):
            h=A[i][k]*inv%P
            if h:
                for j in range(k+1,n):
                    A[i][j]=(A[i][j]-h*A[k][j])%P
                A[i][k]=0
    return d

def sequence(rows,x,y,z):
    v=[1]*len(rows);values=[v]
    weighted=[[(j,m*pow(x,a,P)*pow(y,b,P)*pow(z,g,P)%P)
               for (j,a,b,g),m in row.items()] for row in rows]
    for _ in range(70):
        v=[sum(w*v[j] for j,w in row)%P for row in weighted]
        values.append(v)
    return values

def minors(values,n,start):
    return [determinant([[values[start+2*(r+c)][i] for c in range(n)]
            for r in range(n)]) for i in range(37)]

def main():
    assert SCIENCE_PIN==PIN and len(ROOTS)==9
    native=marginal_gate_rows(ZERO_ROOT)
    assert len(native)==96 and all(marginal_gate_rows(r)==native for r in ROOTS)
    ids,Q,growth=weighted_quotient(native)
    assert (len(Q),growth)==(37,[1,4,13,21,33,37])
    for i,row in enumerate(native):
        push=Counter()
        for (j,a,b,g),v in row.items():push[(ids[j],a,b,g)]+=v
        assert push==Q[ids[i]]
    five=[]
    for i in range(37):
        old={klass(j) for j in range(96) if ids[j]==i}
        assert len(old)==1
        five.append(next(iter(old)))
    for i,row in enumerate(Q):
        projected=Counter()
        for (j,a,b,g),v in row.items():projected[(five[j],a,b)]+=v
        assert projected==EXPECTED[five[i]]
    full=sequence(Q,2,3,5)
    odd14=minors(full,14,1);even14=minors(full,14,2)
    assert all(odd14) and all(even14)
    c14=(-1320903770112*6**5*5-3962711310336*6**5)%P
    assert c14==478364
    summed=sequence(Q,2,3,1)
    odd5=minors(summed,5,1);even5=minors(summed,5,2)
    assert all(odd5) and all(even5)
    equalaxis=sequence(Q,2,2,7)
    return {"status":"ALL_CHECKS_PASS","pin":PIN,"modulus":P,
      "generic_specialization":{"x":2,"y":3,"z":5,
        "odd_14x14_nonzero":sum(bool(v) for v in odd14),
        "even_shift_14x14_nonzero":sum(bool(v) for v in even14),
        "q14_constant_modulus":c14,
        "odd_determinants_mod_p":odd14,
        "even_shift_determinants_mod_p":even14},
      "gate_summed_specialization":{"x":2,"y":3,"z":1,
        "five_state_projection_verified":True,
        "odd_5x5_nonzero":sum(bool(v) for v in odd5),
        "even_shift_5x5_nonzero":sum(bool(v) for v in even5),
        "odd_determinants_mod_p":odd5,
        "even_shift_determinants_mod_p":even5},
      "equal_axes_control":{"x":2,"y":2,"z":7,
        "odd_14x14_nonzero":sum(bool(v) for v in minors(equalaxis,14,1))}}

if __name__=="__main__":
    print(json.dumps(main(),ensure_ascii=False,indent=2))

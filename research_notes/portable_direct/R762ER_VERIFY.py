#!/usr/bin/env python3
"""R762ER finite certificate. Pure standard-library, exact six-branch BRC convolution.

Run: python3 R762ER_VERIFY.py
No external network or input file required. The all-horizon theorem follows from
R762EQ and the separately documented induction, not from these finite tests.
"""
import hashlib
import json
from array import array

BRANCHES = ((0,0,0), (1,0,0), (0,0,1), (1,1,0), (0,1,1), (1,1,1))

def predecessors(q):
    maps = [array('i') for _ in BRANCHES]
    for x in range(q):
        for y in range(q):
            for z in range(q):
                for m, (dx,dy,dz) in zip(maps, BRANCHES):
                    m.append(((((x-dx)%q)*q+((y-dy)%q))*q+((z-dz)%q)))
    return maps

def f(q,n):
    return max(0, n//(q//3)-2)

def run(q, N, E):
    modulus = 3**E
    maps=predecessors(q)
    v=array('q',[0])*(q**3)
    v[0]=1
    shadows=[]; supports=[]; mass_checks=0; sharp_checks=0
    for n in range(N+1):
        k=f(q,n)
        assert k+1 <= E
        scale=3**k
        assert all(x%scale==0 for x in v), ('divisibility',q,n)
        s=bytes((int(x)//scale)%3 for x in v)
        assert any(s), ('sharpness',q,n)
        sharp_checks+=1
        assert sum(v)%modulus==pow(6,n,modulus),('mass',q,n)
        mass_checks+=1
        shadows.append(s)
        supports.append(sum(bool(x) for x in s))
        if n<N:
            w=array('q',[0])*len(v)
            for i in range(len(v)):
                w[i]=sum(v[p[i]] for p in maps)%modulus
            v=w
    return shadows,supports,{'q':q,'N':N,'exponent_E':E,
        'modulus_decimal':str(modulus),'sharpness_checks':sharp_checks,
        'mass_checks':mass_checks}

def pmod3(v,q):
    p=predecessors(q)
    return bytes(sum(v[m[i]] for m in p)%3 for i in range(len(v)))

def embed9_to27(b):
    out=bytearray(27**3)
    for x in range(9):
        for y in range(9):
            for z in range(9):
                out[((x*3*27+y*3)*27+z*3)]=b[(x*9+y)*9+z]
    return bytes(out)

def rank3(rows):
    a=[bytearray(r) for r in rows]
    piv=[]; R=len(a); C=len(a[0]); row=0
    for col in range(C):
        pivot=next((k for k in range(row,R) if a[k][col]),None)
        if pivot is None:continue
        a[pivot],a[row]=a[row],a[pivot]
        if a[row][col]==2:
            a[row][:]=bytes((2*v)%3 for v in a[row])
        for rr in range(row+1,R):
            factor=a[rr][col]
            if factor:
                a[rr][:]=bytes((a[rr][cc]-factor*a[row][cc])%3 for cc in range(C))
        piv.append(col);row+=1
        if row==R:break
    return row,piv

def main():
    small,_,smeta=run(9,65,20)
    large,large_support,lmeta=run(27,300,34)
    checks=0
    for n in range(195):
        m,r=divmod(n,3)
        b=embed9_to27(small[m])
        for _ in range(r): b=pmod3(b,27)
        assert b==large[n],('lift',n)
        checks+=1
    period_checks=0
    for n in range(27,247):
        assert large[n]==large[n+54],('period',n)
        period_checks+=1
    rank9,pivots9=rank3(small[9:27])
    assert rank9==17
    output={
        'schema':'R762ER_Q27_FROBENIUS_LIFT_FINITE_CERTIFICATE_V1',
        'scope':'positive six-named-branch terminal group algebra; finite tests only',
        'science':{'base_q9':'R762EQ author all-horizon theorem at PR 2731',
                   'universal_q_ge9':'separate Frobenius-lift induction, dependent on q9'},
        'q9':{**smeta,'rank_base_18':rank9,'pivot_columns':pivots9,
              'base_18_sha256':hashlib.sha256(b''.join(small[9:27])).hexdigest()},
        'q27':{**lmeta,
               'start_of_period':27,'period':54,'period_equality_checks':period_checks,
               'lift_shadow_equality_checks':checks,
               'period_base_rank_from_theorem':51,
               'base_54_sha256':hashlib.sha256(b''.join(large[27:81])).hexdigest(),
               'base_54_supports':large_support[27:81],
               'content_exponent_at_300':f(27,300)},
        'review':'NOT_REVIEWED','formal_checker':'NOT_PERFORMED',
        'native_signed_events':'NOT_TESTED',
    }
    print(json.dumps(output,ensure_ascii=False,indent=2))

if __name__=='__main__':main()

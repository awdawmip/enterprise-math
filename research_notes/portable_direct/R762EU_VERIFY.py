#!/usr/bin/env python3
"""R762EU independent exact standard-library verification: digitwise q=3^a BRC normalized shadows.
Frozen terminal model: P=1+X+Z+XY+YZ+XYZ, full 3-coordinate positive named-branch observer.
No continuous functions; computations in integers and F_3.
"""
from array import array
from hashlib import sha256
import json

BRANCHES=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
PERIOD=18
START=8
BASE_SIZE=9**3
BASE_COUNT=START+PERIOD

def f(q,n):
    return max(0, n//(q//3)-2)

def idx(x,y,z,q):
    return (x*q+y)*q+z

def pows_direct(q, horizon, E):
    """Independent original six-branch shift: full vector, exactly mod 3**E."""
    dim=q**3
    mod=3**E
    predecessors=[]
    for dx,dy,dz in BRANCHES:
        predecessors.append(array('I',(idx((x-dx)%q,(y-dy)%q,(z-dz)%q,q)
                            for x in range(q) for y in range(q) for z in range(q))))
    v=[0]*dim; v[0]=1
    shadows=[]
    for n in range(horizon+1):
        scale=3**f(q,n)
        assert (f(q,n)+1)<=E
        assert all(z%scale==0 for z in v), (q,n,'divisibility')
        shadow=bytes((z//scale)%3 for z in v)
        assert any(shadow),(q,n,'nonzero')
        assert sum(v)%mod==pow(6,n,mod),(q,n,'mass')
        shadows.append(shadow)
        if n==horizon: break
        w=[0]*dim
        for j in range(dim):
            w[j]=sum(v[perm[j]] for perm in predecessors)%mod
        v=w
    return shadows

def local_kernel():
    # C_e(dx,dy,dz) = [X^dx Y^dy Z^dz] P^e (mod 3), e in {0,1,2}
    out=[]
    d={(0,0,0):1}
    for e in range(3):
        out.append(bytes(d.get((x,y,z),0)%3 for x in range(3) for y in range(3) for z in range(3)))
        dnext={}
        for (x,y,z),c in d.items():
            for dx,dy,dz in BRANCHES:
                pos=(x+dx,y+dy,z+dz)
                dnext[pos]=dnext.get(pos,0)+c
        d=dnext
    assert [sum(x>0 for x in s) for s in out]==[1,6,18]
    return out

C=local_kernel()
BASE=pows_direct(9,25,7)

def shadow_entry(q,n,x,y,z):
    """Random access in the exact normalized terminal shadow, no q^3 array materialization."""
    assert q>=9 and q%9==0
    h=q//9
    m,r=divmod(n,h)
    b=m if m<START else START+(m-START)%PERIOD
    u=(x//h,y//h,z//h)
    v=(x%h,y%h,z%h)
    result=BASE[b][idx(*u,9)]
    while h>1:
        e=r%3
        a,b0,c=(v[0]%3,v[1]%3,v[2]%3)
        result=(result*C[e][idx(a,b0,c,3)])%3
        v=(v[0]//3,v[1]//3,v[2]//3)
        r//=3
        h//=3
    assert r==0 and v==(0,0,0)
    return result

def lifted_vector(q,n):
    return bytes(shadow_entry(q,n,x,y,z)
                 for x in range(q) for y in range(q) for z in range(q))

def test():
    assert len(BASE)==26 and len(C)==3
    assert BASE[8]==pows_direct(9,26,7)[26]
    assert BASE[7]!=pows_direct(9,25,7)[25]
    for n in range(26):
        assert lifted_vector(9,n)==BASE[n]
    q=27
    full=pows_direct(q,82,11)
    for n in range(83):
        predicted=lifted_vector(q,n)
        assert predicted==full[n], ('mismatch', q,n)
    assert lifted_vector(27,24)==lifted_vector(27,78)
    assert lifted_vector(27,23)!=lifted_vector(27,77)
    for q in (27,81,243):
        h=q//9
        samples=[0,1,h-1,h,h*7-1,h*8-1,h*8,h*9,q+5,2*q+17,10**12+271828]
        points=[(0,0,0),(q-1,q-1,q-1),(h*4,0,h*3),
                (h-1,h-2 if h>1 else 0,0),(q//2,q//3,q//4)]
        for n in samples:
            for x,y,z in points:
                value=shadow_entry(q,n,x,y,z)
                assert value in (0,1,2)
                if n>=8*h:
                    assert value==shadow_entry(q,n+2*q,x,y,z)
    evidence={
        'schema':'R762EU_DIGITWISE_RANDOM_ACCESS_CERTIFICATE_V1',
        'frozen_model':'P=1+X+Z+XY+YZ+XYZ, six named positive 3-coordinate BRC terminal observer',
        'base_q9_states':26,
        'base_q9_bytes':len(BASE)*BASE_SIZE,
        'local_kernel_bytes':sum(map(len,C)),
        'total_table_bytes':len(BASE)*BASE_SIZE+sum(map(len,C)),
        'kernel_support_sizes':[sum(v!=0 for v in k) for k in C],
        'base_26_sha256':sha256(b''.join(BASE)).hexdigest(),
        'kernel_sha256':sha256(b''.join(C)).hexdigest(),
        'q9_full_vector_checks':26,
        'q27_full_vector_checks':83,
        'full_vector_coordinates_checked':26*729+83*19683,
        'q27_direct_modulus':'3^11',
        'q27_horizon':[0,82],
        'period_boundary_27':{'equal_24_78':True,'unequal_23_77':True},
        'random_point_ranges':[27,81,243],
        'random_point_checks':'5 points x 11 timestamps per q, with extended period checks where n>=8*h',
        'large_timestamp_test':'10**12+271828',
        'arithmetic':'integer original branch convolution mod 3^E; base-3 digit table mod 3; no floating point',
        'depends_on':['R762ER Frobenius coefficientwise lift','R762ET sharp eventual q9 period 18 starting at 8'],
        'independent_review':'NOT_REVIEWED',
        'result':'PASS'
    }
    print(json.dumps(evidence,ensure_ascii=False,indent=2))

if __name__=='__main__': test()

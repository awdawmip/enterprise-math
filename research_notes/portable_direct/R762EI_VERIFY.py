#!/usr/bin/env python3
"""R762EI deterministic exact Z/9 minor certificate for four BRC zero generators.
Requires numpy; all arithmetic is integer modulo 9 or modulo 3, never floating point.
"""
from __future__ import annotations
import hashlib
import json
import sys
import numpy as np

MODEL = 'P=1+X+Z+XY+YZ+XYZ; K_J=T(U_J)D(V_J); q=3^a'

def selected_points(q: int, count: int) -> list[int]:
    total=q**3
    if count>total:raise ValueError('count exceeds group order')
    seen=set();result=[];counter=0
    while len(result)<count:
        msg=f'R762EI:selection:v1:q={q}:index={counter}'.encode('ascii')
        idx=int.from_bytes(hashlib.sha256(msg).digest(),'big')%total
        counter+=1
        if idx not in seen:
            seen.add(idx);result.append(idx)
    return result

def row_matrix(q:int,indices:list[int])->np.ndarray:
    """Exact 8q columns: K_{j,t,b}=3*1_{ell=t,m=b}-1_{ell=t}, b=0,1."""
    A=np.zeros((len(indices),8*q),dtype=np.uint8)
    for i,p in enumerate(indices):
        x,yz=divmod(p,q*q);y,z=divmod(yz,q)
        ell=(x,y,z,(x-y+z)%q)
        stripe=((y+z)%3,(x-z)%3,(x+y)%3,(y+z)%3)
        for j in range(4):
            t=int(ell[j]);v=int(stripe[j]);first=j*2*q+2*t
            A[i,first]=2 if v==0 else 8
            A[i,first+1]=2 if v==1 else 8
    return A

def unit_eliminate_mod9(A:np.ndarray)->tuple[int,np.ndarray]:
    """Exact row/column unit-pivot operations over Z/9; matrix dtype uint8."""
    rows,cols=A.shape
    inv=np.array([0,1,5,0,7,2,0,4,8],dtype=np.uint8)
    k=0
    while k<min(rows,cols):
        sub=A[k:,k:]
        found=(sub%3!=0)
        first=int(np.argmax(found))
        if not bool(found.flat[first]):break
        di,dj=divmod(first,cols-k);i,j=k+di,k+dj
        if i!=k:A[[k,i],k:]=A[[i,k],k:]
        if j!=k:A[:,[k,j]]=A[:,[j,k]]
        p=int(A[k,k]);assert p%3!=0
        A[k,k:]=(A[k,k:]*inv[p])%9
        fac=A[k+1:,k].copy()
        if np.any(fac):
            # maximum unsigned intermediate is 80, so no uint8 wrap.
            A[k+1:,k+1:]=(A[k+1:,k+1:]+72-fac[:,None]*A[k,k+1:])%9
        A[k+1:,k]=0
        k+=1
    assert not np.any(A[k:,k:]%3)
    return k,A

def field_rank_mod3(A:np.ndarray)->int:
    rows,cols=A.shape;k=0
    while k<min(rows,cols):
        sub=A[k:,k:];found=(sub!=0);first=int(np.argmax(found))
        if not bool(found.flat[first]):break
        di,dj=divmod(first,cols-k);i,j=k+di,k+dj
        if i!=k:A[[k,i],k:]=A[[i,k],k:]
        if j!=k:A[:,[k,j]]=A[:,[j,k]]
        p=int(A[k,k]);assert p in (1,2)
        if p==2:A[k,k:]=(A[k,k:]*2)%3
        fac=A[k+1:,k].copy()
        if np.any(fac):
            A[k+1:,k+1:]=(A[k+1:,k+1:]+24-fac[:,None]*A[k,k+1:])%3
        A[k+1:,k]=0
        k+=1
    assert not np.any(A[k:,:]%3)
    return k

def case(q:int,rows:int)->dict:
    assert q>=3
    u=q
    while u%3==0:u//=3
    assert u==1
    indices=selected_points(q,rows)
    matrix=row_matrix(q,indices)
    r0,U=unit_eliminate_mod9(matrix)
    tail=U[r0:,r0:]
    assert np.all(tail%3==0)
    r1=field_rank_mod3((tail//3).copy())
    assert r0==4*q-4,(q,'unit rank',r0)
    assert r1==4*q-8,(q,'three rank',r1)
    assert r0+r1==8*q-12,(q,'rational-rank bound',r0+r1)
    idx_str=','.join(map(str,indices)).encode('ascii')
    return {'q':q,'sampled_rows':rows,'full_rows':q**3,'columns':8*q,
            'mod9_unit_pivots':r0,'mod9_exact_three_pivots':r1,
            'sum_pivots':r0+r1,'global_kernel_rank_from_R762ED':8*q-12,
            'smith_valuation_ge_2_count':0,
            'conclusion':f'K/I ~= (Z/3Z)^{4*q-8}',
            'row_sample_sha256':hashlib.sha256(idx_str).hexdigest(),
            'sample_rule':'SHA256("R762EI:selection:v1:q=<q>:index=<counter>") -> int mod q^3, first distinct rows'}

def symbolic_q3_certificate()->dict:
    """Tests 12-polynomial basis and five-point carry separation over F3."""
    pts=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
    B=np.zeros((27,12),dtype=np.uint8)
    F=np.zeros((27,24),dtype=np.uint8)
    kappa=np.zeros(27,dtype=np.uint8)
    coeff={(0,0,1):-1,(0,2,2):1,(1,0,2):1,(1,2,1):1,(1,2,2):1}
    lam=np.array([coeff.get(p,0)%3 for p in pts],dtype=np.uint8)
    for i,(x,y,z) in enumerate(pts):
        U=x*(y+z);V=y*(x-z)
        A=x*x*(y+z);C=z*z*(x+y);D=y*y*(x-z)
        B[i,:]=np.array([1,x,y,z,x*x,y*y,z*z,U,V,A,D,C],dtype=np.int16)%3
        ell=(x,y,z,(x-y+z)%3)
        stripe=((y+z)%3,(x-z)%3,(x+y)%3,(y+z)%3)
        for j in range(4):
            e=ell[j];m=stripe[j]
            F[i,j*6:j*6+6]=[1,e,e*e,m,m*e,m*e*e]
        kappa[i]=((x-y+z)//3)%3
    F%=3
    assert field_rank_mod3(B.copy())==12
    assert field_rank_mod3(F.copy())==12
    assert field_rank_mod3(np.column_stack((B,F)))==12
    assert np.all((lam.astype(np.uint16)@F.astype(np.uint16))%3==0)
    assert np.all((lam.astype(np.uint16)@B.astype(np.uint16))%3==0)
    pairing=int((lam.astype(np.uint16)@kappa.astype(np.uint16))%3)
    assert pairing==1
    return {'q3_polynomial_basis_rank':12,'q3_family_rank':12,
            'five_point_carry_annihilator':[(list(p),int(v)) for p,v in coeff.items()],
            'annihilator_pairs_with_family_columns':[0]*24,
            'annihilator_pairs_with_carry':pairing}

def main():
    sizes={3:27,9:220,27:400,81:1600,243:3000}
    qs=[int(q) for q in sys.argv[1:]] or [81,243]
    result={'schema':'R762EI_INTEGRAL_NULL_QUOTIENT_Q81_Q243_V1',
            'arithmetic':'exact uint8 Z/9 and F3 row/column elimination; all intermediates bounded <256',
            'premise':'earlier author-proved R762ED kernel rank 8q-12 and R762EF full rational span, not independently reviewed',
            'model':MODEL,'verification':'PASS',
            'symbolic_q3_certificate':symbolic_q3_certificate(),
            'cases':[case(q,sizes[q]) for q in qs]}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()

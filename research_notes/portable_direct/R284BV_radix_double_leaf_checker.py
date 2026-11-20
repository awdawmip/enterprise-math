#!/usr/bin/env python3
"""Exact 4x4 star-Port radix separation certificate. Python standard library only."""
from itertools import product, permutations
from collections import Counter
import json
from pathlib import Path

def signature(C,t,s):
    a,b1,b2,b3=C[0]
    u1,A11,x,y=C[1]
    u2,w,A22,z=C[2]
    u3,g,h,r=C[3]
    T=t-A11; S=s-A22
    U=T*S-x*w
    V=-r*U-z*(T*h+x*g)-y*(w*h+S*g)
    p1=S*u1+x*u2
    p2=T*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+S*u3)
    q2=-r*p2+T*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=U*u3+p1*g+p2*h
    J=-a*U-b1*p1-b2*p2
    K=-a*V-b1*q1-b2*q2-b3*q3
    return (U,V,p1,p2,q1,q2,q3,J),K

def eval_sig(sig,K,d0,d3,z1,z2,z3):
    U,V,p1,p2,q1,q2,q3,J=sig
    return d0*(U*d3+V)-z1*(p1*d3+q1)-z2*(p2*d3+q2)-z3*q3+J*d3+K

def det_perm(A):
    out=0
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        v=1
        for i in range(4):v*=A[i][p[i]]
        out+=(-1 if inv%2 else 1)*v
    return out

def det_star(C,t,s,d0,d3,z1,z2,z3):
    M=[[-v for v in row] for row in C]
    for i,di in enumerate((d0,t,s,d3)):M[i][i]+=di
    for i,z in enumerate((z1,z2,z3),1):M[0][i]-=z
    return det_perm(M)

def balanced_digits(value,base,count):
    out=[]
    for _ in range(count):
        digit=value%base
        if digit>base//2:digit-=base
        value=(value-digit)//base
        out.append(digit)
    assert value==0
    return out

def recover_from_noisy_integer(y,H,B,Q):
    # Recover P=round(y/Q). All test inputs are exact integers.
    P=(2*y+Q)//(2*Q) if y>=0 else -((2*(-y)+Q)//(2*Q))
    ds=balanced_digits(P,Q,9)
    assert ds[1]==0
    J,V,U,q1,p1,q2,p2,q3=(ds[0],ds[2],ds[3],-ds[4],-ds[5],-ds[6],-ds[7],-ds[8])
    ud=balanced_digits(U,B,4);p1d=balanced_digits(p1,B,4)
    p2d=balanced_digits(p2,B,4);q3d=balanced_digits(q3,B,4)
    vd=balanced_digits(V,B,4);jd=balanced_digits(J,B,4)
    A11=-ud[1];A22=-ud[2]
    u1=p1d[1];u2=p2d[2];u3=q3d[3]
    assert u1>0 and u2>0 and u3>0
    x,rem=divmod(p1d[0]+A22*u1,u2);assert rem==0
    w,rem=divmod(p2d[0]+A11*u2,u1);assert rem==0
    resd=balanced_digits(q3-U*u3,B,4)
    g,rem=divmod(resd[1],u1);assert rem==0
    h,rem=divmod(resd[2],u2);assert rem==0
    r=-vd[3]
    resd=balanced_digits(V+r*U,B,4)
    z,rem=divmod(-resd[2],h);assert rem==0
    yy,rem=divmod(-resd[1],g);assert rem==0
    a=-jd[3]
    resd=balanced_digits(J+a*U,B,4)
    b1,rem=divmod(-resd[1],u1);assert rem==0
    b2,rem=divmod(-resd[2],u2);assert rem==0
    K_base=-a*V-b1*q1-b2*q2
    n=P*Q+K_base-y
    b3=(2*n+q3)//(2*q3)
    C=(a,b1,b2,b3,u1,A11,x,yy,u2,w,A22,z,u3,g,h,r)
    assert all(1<=v<=H for v in C)
    assert signature([C[i:i+4] for i in (0,4,8,12)],B*B,B)[0]==(U,V,p1,p2,q1,q2,q3,J)
    return C

def run(H=2):
    B=48*H**4+1;t=B*B;s=B
    A=24*(t+s+H+1)**4
    rho_int=(t*s-(H-1)*(t+s)-1)//2
    Q=4*(A+rho_int+1)
    seen={};sizes=Counter();count=0;pair_count=0
    minimum=None;maximum=None;wmin=None;wmax=None
    crosschecks=0;decoder_checks=0
    for entries in product(range(1,H+1),repeat=16):
        C=[entries[0:4],entries[4:8],entries[8:12],entries[12:16]]
        key,K=signature(C,t,s)
        reduced=entries[:3]+entries[4:]
        hit=seen.get(key)
        if hit is None:seen[key]=(reduced,[(entries[3],K)])
        else:
            assert hit[0]==reduced
            hit[1].append((entries[3],K))
        if count%max(1,H**16//128)==0:
            for ctrl in ((0,0,0,0,0),(7,-5,3,0,9),(-11,13,17,-2,1)):
                assert eval_sig(key,K,*ctrl)==det_star(C,t,s,*ctrl)
                crosschecks+=1
        if H==2:
            ctrl=(Q**3,Q,Q**5,Q**7,Q**9)
            f=eval_sig(key,K,*ctrl)
            for eps in (-rho_int,0,rho_int):
                assert recover_from_noisy_integer(f+eps,H,B,Q)==entries
                decoder_checks+=1
        count+=1
    for reduced,members in seen.values():
        sizes[len(members)]+=1
        assert len(members)==H
        members.sort()
        for (x,k1),(y,k2) in zip(members,members[1:]):
            assert y-x==1
            gap=abs(k2-k1)
            pair_count+=1
            if minimum is None or gap<minimum:
                minimum=gap;wmin=list(reduced[:3])+[x]+list(reduced[3:])
            if maximum is None or gap>maximum:
                maximum=gap;wmax=list(reduced[:3])+[x]+list(reduced[3:])
    assert minimum==t*s-(H-1)*(t+s)
    assert maximum==H*(t+H-1)*(s+H-1)
    return {'schema':'EM_R284BV_RADIX_DOUBLE_FROZEN_PORT_CERT_V1',
      'H':H,'B':B,'t':t,'s':s,'candidate_count':count,
      'nonconstant_signature_classes':len(seen),'size_histogram':dict(sizes),
      'adjacent_constant_pairs':pair_count,'min_adjacent_constant_gap':minimum,
      'max_adjacent_constant_gap':maximum,'predicted_min':t*s-(H-1)*(t+s),
      'predicted_max':H*(t+H-1)*(s+H-1),
      'min_witness_row_major':wmin,'max_witness_row_major':wmax,
      'independent_determinant_crosschecks':crosschecks,
      'radix_Q':str(Q),'radix_Q_bit_length':Q.bit_length(),
      'max_correctable_integer_noise':rho_int,
      'deterministic_decoder_checks':decoder_checks,
      'control_exponents':{'d0':3,'d3':1,'z1':5,'z2':7,'z3':9},
      'prime_condition':'choose any prime p > 4*(A+max_correctable_integer_noise+1)*Q**9 with A=24*(t+s+H+1)**4; its residues never wrap the noisily observed integer F.',
      'scope':'Complete 4x4 H=2 candidate census; general-H proof is algebraic and independent of this census',
      'review':'NOT_REVIEWED'}

if __name__=='__main__':
    data=run(2)
    dest=Path(__file__).with_name('R284BV_radix_double_leaf_verification.json')
    dest.write_text(json.dumps(data,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps(data,indent=2,sort_keys=True))

#!/usr/bin/env python3
"""R261 exact author-side BRC affine-fibre moment verifier.

All scientific state steps use the explicit R260 six-axis affine BRC subcarrier
and retain positive integer source multiplicities. Original enterprise_math
package is not imported. SymPy checks exact rational generating-function
algebra for the finite BRC moment recurrences; no physical time is involved.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from itertools import product
from math import isqrt
import json
import sympy as sp

EDGE={0:{0:(2,-1,-1),1:(2,1,-1)},
      1:{0:(0,-1,-1),1:(0,1,-1)},
      2:{0:(1,1,1),1:(2,1,-1)}}
DFA={0:{0:1,1:0},1:{0:2,1:0},2:{0:2,1:2}}
STATES=((0,1),(2,0),(2,1),(1,0))
INDEX={state:i for i,state in enumerate(STATES)}

def mats():
    T=sp.zeros(4); S=sp.zeros(4); B=sp.zeros(4); C=sp.zeros(4)
    for i,(q,last) in enumerate(STATES):
        for a,(q1,eta,b) in EDGE[q].items():
            if last==a==0:continue
            j=INDEX[(q1,a)]
            T[j,i]+=1; S[j,i]+=eta; B[j,i]+=b; C[j,i]+=eta*b
    return T,S,B,C

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def moment_vectors(max_L,T,S,B,C):
    n=sp.Matrix([1,0,0,0]); u=sp.zeros(4,1); v=sp.zeros(4,1)
    out=[]
    for L in range(max_L+1):
        out.append((int(n[0]+n[2]),int(u[0]+u[2]),int(v[0]+v[2])))
        n,u,v=T*n, S*u+B*n, T*v+2*C*u+T*n
    return out

def primitive_word(w):
    q=0;r=0;eps=1;k=0
    for ch in w:
        a=int(ch)
        q1,eta,b=EDGE[q][a]
        q,r,eps,k=q1,DFA[r][a],eps*eta,eta*k+b
    return q,r,(eps,k)

def exact_fib_effect_counts(max_L):
    counts={(0,1,1,0):1}
    out=[]
    for L in range(max_L+1):
        group=Counter()
        for (q,last,eps,k),v in counts.items():
            if last==1:group[(eps,k)]+=v
        out.append(group)
        if L==max_L:break
        nxt=defaultdict(int)
        for (q,last,eps,k),v in counts.items():
            for a,(q1,eta,b) in EDGE[q].items():
                if last==a==0:continue
                nxt[(q1,a,eps*eta,eta*k+b)]+=v
        counts=nxt
    return out

def integer_ceil_sqrt_ratio(num,den):
    assert num>=0 and den>0
    t=(num+den-1)//den
    q=isqrt(t)
    return q if q*q>=t else q+1

def main():
    T,S,B,C=mats()
    x=sp.Symbol('lambda')
    assert sp.factor(T.charpoly().as_expr())==(x*x+1)*(x*x-x-1)
    assert sp.factor(S.charpoly().as_expr())==(x-1)**2*(x*x+x+1)
    assert (S**3-sp.eye(4))**2==sp.zeros(4)
    z=sp.Symbol('z'); I=sp.eye(4); eA=sp.Matrix([1,0,0,0]); h=sp.Matrix([[1,0,1,0]])
    nz=(I-z*T).inv()*eA
    uz=(I-z*S).inv()*(z*B*nz)
    vz=(I-z*T).inv()*(z*(2*C*uz+T*nz))
    n_gen=1/(1-z-z*z)
    u_gen=z*(z*z-2*z-1)/((1-z)*(1-z**3)*(1-z-z*z))
    v_gen=z*(1+6*z+2*z*z-z**3)/((1-z**3)*(1-z-z*z)**2)
    assert sp.cancel((h*nz)[0]-n_gen)==0
    assert sp.cancel((h*uz)[0]-u_gen)==0
    assert sp.cancel((h*vz)[0]-v_gen)==0
    rho=(sp.sqrt(5)-1)/2
    sigma=sp.simplify((1+6*rho+2*rho**2-rho**3)/((1-rho**3)*(1+2*rho)))
    assert sp.simplify(sigma-(sp.Rational(3,2)+7*sp.sqrt(5)/10))==0
    mean=sp.simplify(rho*(rho**2-2*rho-1)/((1-rho)*(1-rho**3)))
    assert sp.simplify(mean-(-sp.Rational(9,4)-3*sp.sqrt(5)/4))==0
    moments=moment_vectors(256,T,S,B,C)
    effects=exact_fib_effect_counts(256)
    samples={}
    for L,(n,u,v) in enumerate(moments):
        group=effects[L]
        assert n==fib(L+1)==sum(group.values())
        assert u==sum(k*w for (eps,k),w in group.items())
        assert v==sum(k*k*w for (eps,k),w in group.items())
        assert all(k%2==L%2 for eps,k in group)
        assert v<=4*L*n if L>=1 else v==0
        if L>0:
            R=integer_ceil_sqrt_ratio(2*v,n)
            close=sum(w for (eps,k),w in group.items() if -R<=k<=R)
            assert 2*close>=n
            assert sum(1 for (eps,k) in group if -R<=k<=R)<=2*(R+1)
            lower=(n+4*(R+1)-1)//(4*(R+1))
            assert max(group.values())>=lower
            if L in (1,2,3,8,20,50,117,128,200,256):
                samples[str(L)]={'N':str(n),'sum_k':str(u),'sum_k2':str(v),
                  'R':R,'moment_pigeonhole_lower':str(lower),
                  'max_fibre':str(max(group.values())),'effect_atom_count':len(group)}
    bases=('1110101','1011010','0000000')
    assert [primitive_word(w)[1] for w in bases]==[0,1,2]
    assert len({(primitive_word(w)[0],primitive_word(w)[2]) for w in bases})==1
    sync='1101'
    for q in range(3):
        eps,k=1,0;qq=q
        for ch in sync:
            qq,eta,b=EDGE[qq][int(ch)];eps,k=eta*eps,eta*k+b
        assert qq==0 and (eps,k)==(1,-2)
    full=Counter({(0,0,1,0):1}); comparisons=0; minima={}
    for m in range(129):
        if m>=12:
            rows=defaultdict(lambda:[0,0,0])
            for (q,r,eps,k),v in full.items():rows[(q,eps,k)][r]+=v
            M=max(min(row) for row in rows.values())
            L=m-11
            n,u,v=moments[L]
            R=integer_ceil_sqrt_ratio(2*v,n)
            lb=(n+4*(R+1)-1)//(4*(R+1))
            assert M>=lb
            if m in (12,13,19,31,61,128):
                minima[str(m)]={'M_m':str(M),'single_block_lower':str(lb)}
            comparisons+=1
        if m<=10:
            raw=Counter((q,r,ep,k) for bits in product('01',repeat=m)
                        for q,r,(ep,k) in [primitive_word(''.join(bits))])
            assert raw==full
        if m<128:
            nxt=Counter()
            for (q,r,eps,k),v in full.items():
                for a in (0,1):
                    q1,eta,b=EDGE[q][a]
                    nxt[(q1,DFA[r][a],eps*eta,eta*k+b)]+=v
            full=nxt
    out={
      'schema':'EM_R261_BRC_FIBONACCI_MOMENT_WIDTH_EXACT_V1',
      'date':'2026-10-24',
      'mode':'AUTHOR_SIDE_EXACT_INTEGER_AND_SYMBOLIC_VERIFIED_NOT_NATIVE_ADMITTED',
      'source_ref':'awdawmip/enterprise-math@4f7169291a872467496de179666f456e67869749',
      'source_pins':{'brc_transport_blob':'be1debe367263931bd5e93fd750be3ed54624fe1',
         'brc_control_port_blob':'44def6b8ac787e798d3cc2c6be16f873f91b9db8',
         'r260_author_proof_commit':'43dc61f43a73cf6b0ec535c01efedd5067400fc2'},
      'moment_gf':{'N':'1/(1-z-z^2)',
        'U':'z(z^2-2z-1)/((1-z)(1-z^3)(1-z-z^2))',
        'V':'z(1+6z+2z^2-z^3)/((1-z^3)(1-z-z^2)^2)'},
      'limiting_mean':'-(9+3sqrt(5))/4',
      'limiting_variance_per_length':'3/2+7sqrt(5)/10',
      'exact_construction':'M_(L+11)>=ceil(F_(L+1)/(4*(ceil(sqrt(2V_L/F_(L+1)))+1))) for L>=1',
      'asymptotic':'M_m = Omega(phi^m / sqrt(m)); M_m <= F_m; matching upper polynomial order not established',
      'verification':{'symbolic_gf_identities':3,'signed_matrix_charpolys':2,
        'nilpotent_Jordan_block_check':1,'integer_moment_vs_histogram_lengths':len(moments),
        'full_source_words_independent_lengths':'0..10',
        'full_positive_3mode_histogram_vs_lower_lengths':comparisons,
        'global_empirical_V_le_4L_N_lengths':'1..256 (not proof of all-length bound)'},
      'samples':samples,'M_samples':minima,
      'native_original_package_imported':False,
      'formal_task_owner_verified':False,
      'not_p000_or_r193_native_proof':True
    }
    print(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False))

if __name__=='__main__':main()

#!/usr/bin/env python3
"""EC17 author-side exact verification of the auxiliary BRC reflection kernel.

All computations are exact Python integers, no floating-point assumptions.
This checks finite evidence and polynomial certificates, not canonical admission.
"""
import argparse
import json
from collections import defaultdict
from math import comb

EDGE = {
    0: {0: (2, -1, -1), 1: (2, +1, -1)},
    1: {0: (0, -1, -1), 1: (0, +1, -1)},
    2: {0: (1, +1, +1), 1: (2, +1, -1)},
}
STATES = ((0,0,-1),(0,0,1),(1,1,-1),(1,1,1),
          (2,0,-1),(2,0,1),(2,1,-1),(2,1,1))


def step(q, r, e, bit):
    next_q, eta, b = EDGE[q][bit]
    next_e = e * eta
    next_r = 0 if bit == 1 else (1 if r == 0 else 2)
    grade = int(next_e * b == -1)
    assert next_e * b == e * (1 - 2*bit)
    return (next_q, next_r, next_e), grade


def fine_dp(limit):
    current = {(0,0,1,0): 1}
    rows = [{0: 1}]
    for n in range(1, limit+1):
        nxt = defaultdict(int)
        for (q,r,e,k),mass in current.items():
            for bit in (0, 1):
                (qq,rr,ee),g = step(q,r,e,bit)
                if rr != 2:
                    nxt[(qq,rr,ee,k+g)] += mass
        current = nxt
        row = defaultdict(int)
        for (_,_,_,k),mass in current.items():
            row[k] += mass
        rows.append(dict(row))
    return rows


def enumerate_raw(limit):
    rows = []
    for n in range(limit+1):
        row = defaultdict(int)
        for word in range(1 << n):
            q,r,e,k = 0,0,1,0
            for i in range(n):
                (q,r,e),g = step(q,r,e,(word >> i)&1)
                k += g
                if r == 2: break
            else:
                row[k] += 1
        rows.append(dict(row))
    return rows


def kernel_rows(limit):
    # Delta(x,u)*E(x,u) = 1-u*x^2. Rows are E[n][k].
    rows = []
    for n in range(limit+1):
        row = [0]*(n+1)
        for k in range(n+1):
            value = int(n==0 and k==0)-int(n==2 and k==1)
            if n>=1:
                if k<n: value += rows[n-1][k]
                if k: value += rows[n-1][k-1]
            if n>=4 and 2<=k<=n-2:
                value -= 2*rows[n-4][k-2]
            if n>=6 and 3<=k<=n-3:
                value += rows[n-6][k-3]
            row[k] = value
        rows.append(row)
    return rows


def get(rows, n, k):
    if n<0 or k<0 or n>=len(rows) or k>=len(rows[n]): return 0
    return rows[n][k]


def add(a,b,scale=1):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=scale*v
    while len(out)>1 and out[-1]==0:out.pop()
    return out


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]+=c*d
    while len(out)>1 and out[-1]==0:out.pop()
    return out


def shift(a,n): return [0]*n+a


def polynomial_certificates(maxk=12):
    # [u^k]1/Delta = B_k(x)/(1-x)^(k+1).
    B=[]
    P={}
    for k in range(maxk+1):
        if k==0: B.append([1])
        else:
            cur=shift(B[k-1],1)
            if k>=2:cur=add(cur,mul(shift(B[k-2],4),[1,-1]),-2)
            if k>=3:cur=add(cur,mul(shift(B[k-3],6),[1,-2,1]))
            B.append(cur)
        assert len(B[k])-1<=3*k and sum(B[k])==1
        if k==0:continue
        p=shift(B[k-1],3)
        if k>=2:p=add(p,mul(shift(B[k-2],3),[1,-1,1,-1]),-1)
        if k>=3:p=add(p,mul(shift(B[k-3],5),[1,-2,1]))
        assert len(p)-1<=3*k and sum(p)==1
        P[k]=p
    return P


def polynomial_value(p,k,n):
    return sum(coef*comb(n-degree+k-1,k-1)
               for degree,coef in enumerate(p)
               if coef and n-degree+k-1>=k-1)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--depth', type=int, default=256)
    parser.add_argument('--report', default='R4_EC17_AUTHOR_EXACT_REPORT.json')
    args=parser.parse_args()
    N=args.depth
    assert N>=40
    raw=enumerate_raw(12)
    direct=fine_dp(N)
    E=kernel_rows(N)
    polys=polynomial_certificates(12)
    for n in range(13):
        assert all(raw[n].get(k,0)==direct[n].get(k,0) for k in range(n+1))
    bad=[]
    flat=[]
    for n in range(N+1):
        assert E[n]==E[n][::-1]
        assert all(v>=0 for v in E[n])
        for k in range(n+1):
            clean=get(E,n,k)-get(E,n-3,k-1)
            assert clean==direct[n].get(k,0),(n,k,clean,direct[n].get(k,0))
            if n>=3:
                defect=get(E,n-3,k-1)-get(E,n-3,k-2)
                assert defect==direct[n].get(n-k,0)-direct[n].get(k,0),(n,k)
        for k in range(1,(n-1)//2+1):
            val=direct[n].get(n-k,0)-direct[n].get(k,0)
            if val<0:bad.append((n,k,val))
            if val==0:flat.append((n,k))
    for k,p in polys.items():
        for n in range(2*k+1,N+1):
            defect=direct[n].get(n-k,0)-direct[n].get(k,0)
            assert polynomial_value(p,k,n)==defect,(n,k)
    for n in range(9,N+1):
        assert polynomial_value(polys[4],4,n)==(n-13)*(n-9)*(n-8)//6
    for n in range(11,N+1):
        assert polynomial_value(polys[5],5,n)==(n-15)*(n-10)*(n*n-25*n+148)//24
    assert bad==[(7,3,-1),(8,3,-1),(10,4,-1),(11,4,-2),(12,4,-2)]
    assert flat==[(5,2),(9,3),(9,4),(13,4),(15,5)]
    report={
        'schema':'EM_R4_EC17_AUTHOR_EXACT_V1',
        'model':'auxiliary positive ordered binary affine BRC, clean-source grade observer',
        'global_pin':'7120aa3053ac490626bfc808810021701308a0c3',
        'em_source_pin':'865b82764a5f85d946cd674a0c2ca8f9d9f1d51e',
        'prior':'EC16 exact generating function and source model',
        'theorems':['E=(1-u*x^2)/Delta is palindromic by (x,u)->(u*x,1/u)',
                    'D[n,k]=E[n-3,k-1]-E[n-3,k-2]',
                    'for each k>=1 D[n,k] equals explicitly computable degree-(k-1) polynomial in n whenever n>=2*k+1',
                    'exact k=4 and k=5 formulas and signs'],
        'raw_binary_words_checked':sum(1<<i for i in range(13)),
        'dynamic_clean_dp_depth':N,
        'recurrence_E_depth':N,
        'P_polynomials_verified_k':12,
        'noncentral_half_shell_negatives_through_depth':bad,
        'noncentral_half_shell_zeros_through_depth':flat,
        'finite_no_further_exceptions_claimed':False,
        'unimodality_n_ge_10_through_depth':all(all(E[m][j]>=E[m][j-1]
                 for j in range(1,m//2+1)) for m in range(10,N+1)),
        'native_x6':'NOT_RUN',
        'native_claim':'NOT_AUTHORIZED',
        'driver_review':'NOT_PERFORMED',
        'result':'PASS'
    }
    with open(args.report,'w',encoding='utf-8') as f:
        json.dump(report,f,ensure_ascii=False,indent=2)
    print('PASS exact checks: raw words',report['raw_binary_words_checked'],
          'depth',N,'polynomials k<=12; negative half-shell',bad,'zeros',flat)


if __name__=='__main__':main()

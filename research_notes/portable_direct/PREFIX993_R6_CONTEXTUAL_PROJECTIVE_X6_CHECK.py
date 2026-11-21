"""PREFIX-993: full exact native X6 positive-axis/BRC port-feedback checker.
Uses Python Fraction/Counter. No classical numerical fallback.
Run: python PREFIX993_R6_CONTEXTUAL_PROJECTIVE_X6_CHECK.py
"""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

N=6
X=((1,2,1,3,2,4),(2,1,3,1,4,2))
K=(0,0,1,1,0,1)
R=(1,2,1,2,3,3)
T=F(1,5000)
O=(0,)*N
W=tuple(tuple(F(R[h]*X[K[h]][j],5000) for j in range(N)) for h in range(N))
WD=tuple(tuple(W[h][j]+(T if h==j else 0) for j in range(N)) for h in range(N))
WS=tuple(tuple(W[h][j]+(R[h]*T if j==0 else 0) for j in range(N)) for h in range(N))

def partition(a):
    out=[]
    for h in range(N):
        for cell in out:
            k=cell[0]
            if all(a[h][i]*a[k][j]==a[h][j]*a[k][i]
                   for i in range(N) for j in range(N)):
                cell.append(h);break
        else:out.append([h])
    return out

def step(z,j): return z[:j]+(z[j]+1,)+z[j+1:]

def direct(w,h,n):
    d=Counter({(O,h,F(1)):1})
    for _ in range(n):
        nxt=Counter()
        for (z,last,weight),mult in d.items():
            for j in range(N):
                nxt[(step(z,j),j,weight*w[last][j])]+=mult
        d=nxt
    return d

def project(h,n,k,r,f):
    if not n:return Counter({(O,h,F(1)):1})
    d=Counter({(O,k[h],F(1)):1})
    for _ in range(n-1):
        nxt=Counter()
        for (z,c,weight),mult in d.items():
            for j in range(N):
                nxt[(step(z,j),k[j],weight*r[j]*f[c][j])]+=mult
        d=nxt
    out=Counter()
    for (z,c,weight),mult in d.items():
        for j in range(N):
            out[(step(z,j),j,weight*r[h]*f[c][j])]+=mult
    return out

def summary(d):
    return {'path_count':sum(d.values()),
            'mass':str(sum((w*cnt for (_z,_j,w),cnt in d.items()),F())),
            'distinct_endpoint_port_weights':len(d)}

def main():
    assert partition(W)==[[0,1,4],[2,3,5]]
    assert partition(WS)==[[0,1,4],[2,3,5]]
    assert partition(WD)==[[h] for h in range(N)]
    assert max(map(sum,WS))==F(21,2500)
    assert max(map(sum,WD))==F(1,125)
    minors=[]
    for h,k in combinations(range(N),2):
        d=WD[h][h]*WD[k][k]-WD[h][k]*WD[k][h]
        assert d
        minors.append({'rows':[h,k],'cols':[h,k],'value':str(d)})
    cross=WD[0][0]*WD[1][1]-WD[0][1]*WD[1][0]
    assert cross==F(6,5000*5000)
    basef=tuple(tuple(F(x,5000) for x in row) for row in X)
    safef=tuple(tuple(F(x+(j==0),5000) for j,x in enumerate(row)) for row in X)
    sums={}
    for h in range(N):
        for n in range(8):
            d=direct(W,h,n)
            assert d==project(h,n,K,R,basef)
            e=direct(WD,h,n)
            assert e==project(h,n,tuple(range(N)),(1,)*N,WD)
            assert sum(d.values())==sum(e.values())==N**n
            if n<=5:assert direct(WS,h,n)==project(h,n,K,R,safef)
            for z,_j,_weight in d:
                depth=min(z)
                rel=tuple(x-depth for x in z)
                assert depth*6+sum(rel)==n
                assert tuple(x+depth for x in rel)==z
        if h in (0,1,2):
            sums[str(h)]={'base':summary(direct(W,h,7)),
                          'diag_context':summary(direct(WD,h,7))}
    # Old fixed templates cease to be correct after context, already in one step.
    old_wrong=project(1,1,K,R,(tuple(WD[0]),tuple(WD[2])))
    assert old_wrong!=direct(WD,1,1)
    D=(1,)*6
    assert tuple(x-min(D) for x in D)==O
    cert={'schema':'PREFIX993_R6_CONTEXTUAL_PROJECTIVE_X6_V1',
          'status':'AUTHOR_ANALYTIC_PROOF_EXACT_FRACTION_CHECKED_NOT_REVIEWED',
          'model':'native X6 positive-axis Cell skeleton + BRC-T30/T31 exact Schur kernel',
          'P000_frozen_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
          'original_classes':partition(W),
          'safe_context_classes':partition(WS),
          'diagonal_context_classes':partition(WD),
          'context_t':str(T),
          'max_row_sum_original':str(max(map(sum,W))),
          'max_row_sum_safe':str(max(map(sum,WS))),
          'max_row_sum_diag':str(max(map(sum,WD))),
          'nonzero_pairwise_minors':minors,
          'cross_minor_0_1_axes_0_1':str(cross),
          'full_histogram_checked_lengths':[0,7],
          'safe_histogram_checked_lengths':[0,5],
          'checked_initial_history_ports':list(range(N)),
          'length7':sums,
          'native_relative_witness':{'zero':[0]*6,'full_D':[1]*6,'same_can6':True,'L_E_squared_D':6},
          'scope':'author-computed exact rational verification; no independent Review; no full native Link/occupancy or physical time proof'}
    target=Path(__file__).with_name('PREFIX993_R6_EXACT_RESULTS.json')
    target.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('PASS: base classes=2, safe classes=2, diagonal context classes=6; 15 nonzero minors')
    print('PASS: all six histories length 0..7 exact X6 endpoint/port/weight histograms')
    print(json.dumps(sums,ensure_ascii=False))

if __name__=='__main__': main()

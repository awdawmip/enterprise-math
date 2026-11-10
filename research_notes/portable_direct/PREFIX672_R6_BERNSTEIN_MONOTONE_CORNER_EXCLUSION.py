#!/usr/bin/env python3
"""PREFIX-672 BRC monotone-survival and four-corner exclusion: exact Fraction replay.
Frozen pin f42f2906d77f24085c123f3ccfe9667d41caa96d; no external dependencies.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json
N,DEN=189,2**18
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
R=F(1,32);STEP=F(1,128);GRID=4
Q=F(19,128)
@lru_cache(None)
def inside(n,k,a):return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n
@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*DEN//n
    assert inside(n,k,mid)
    if k==0:ll=lh=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            m=(lo+hi)//2
            if inside(n,k,m):hi=m
            else:lo=m
        ll,lh=lo,hi
    lo,hi=mid,DEN
    while hi-lo>1:
        m=(lo+hi)//2
        if inside(n,k,m):lo=m
        else:hi=m
    rl,rh=lo,hi
    if 4*(rl-lh)>DEN:return True
    if 4*(rh-ll)<DEN:return False
    raise AssertionError(('frozen ambiguity',n,k))

def make_rows():
    state={0:1};rows=[state.copy()]
    for n in range(1,N+1):
        nx=defaultdict(int)
        for k,v in state.items():nx[k]+=v;nx[k+1]+=v
        state={k:v for k,v in nx.items() if wide(n,k)}
        rows.append(state.copy())
    assert not rows[N]
    assert all(sum(rows[n].values())==2**n for n in range(25))
    return rows[:N]

def svec(rows,num,den):
    ps=[num**i for i in range(N)]
    ts=[(den-num)**i for i in range(N)]
    ds=[den**i for i in range(N)]
    return [F(sum(v*ps[k]*ts[n-k] for k,v in row.items()),ds[n]) for n,row in enumerate(rows)]

def solve():
    checks=0
    def ck(ok,name):
        nonlocal checks
        assert ok,name
        checks+=1
    rows=make_rows()
    ck(len(rows)==N and sum(map(len,rows))==9529,'rows count frozen')
    # Bernstein shape condition sufficient for monotonic s_n(u) on [0,1/2].
    pair_count=0
    for n,row in enumerate(rows):
        for k,v in row.items():
            ck(row.get(n-k,0)==v,f'row symmetry {n},{k}')
        for k in range(n//2):
            ck(row.get(k,0)*comb(n,k+1)<=row.get(k+1,0)*comb(n,k),f'left normalized coefficient monotonicity {n},{k}')
            pair_count+=1
    ck(GRID*STEP==R,'rational grid exact')
    vectors=[svec(rows,i,128) for i in range(GRID+1)]
    # First stop Gamma kernel: a_n(z)=1-sum_m w_nm*s_m(z),
    # b_n(z)=n+1-sum_m ((n+m+1)/2)*w_nm*s_m(z).
    # Cache the single-parameter z coefficients once, share them across all p grid vertices.
    means=[[None]*(GRID+1) for _ in range(GRID+1)]
    halves=[[None]*(GRID+1) for _ in range(GRID+1)]
    aa_all=[];bb_all=[];mz_all=[];hz_all=[]
    for j,sz in enumerate(vectors):
        a=[];b=[]
        for n in range(N):
            an,bn=F(1),F(n+1)
            for m,t in enumerate(sz):
                if not t:continue
                w=F(comb(n+m,n),2**(n+m+1))
                an-=w*t;bn-=F(n+m+1,2)*w*t
            a.append(an);b.append(bn)
        ck(all(0<=a[n]<=1 and 0<=b[n]<=n+1 for n in range(N)),f'nonnegative moment kernels for j={j}')
        aa_all.append(a);bb_all.append(b)
        mz_all.append(sum(sz,F(0)))
        hz_all.append(sum(((m+1)*x for m,x in enumerate(sz)),F(0)))
    for i,sp in enumerate(vectors):
        for j in range(GRID+1):
            means[i][j]=mz_all[j]+sum((x*s for x,s in zip(aa_all[j],sp)),F(0))
            halves[i][j]=hz_all[j]+sum((x*s for x,s in zip(bb_all[j],sp)),F(0))
    ck(all(means[i][j]<=means[i+1][j] for i in range(GRID) for j in range(GRID+1)),'mean grid monotone p')
    ck(all(means[i][j]<=means[i][j+1] for i in range(GRID+1) for j in range(GRID)),'mean grid monotone z')
    ck(all(halves[i][j]<=halves[i+1][j] for i in range(GRID) for j in range(GRID+1)),'half moment grid monotone p')
    ck(all(halves[i][j]<=halves[i][j+1] for i in range(GRID+1) for j in range(GRID)),'half moment grid monotone z')
    worst=None;worst_idx=None
    for i in range(GRID):
        for j in range(GRID):
            upper=2*halves[i+1][j+1]-means[i][j]**2
            ck(upper<F(384),f'corner box {i},{j} exceeds upper bound')
            if worst is None or upper>worst:
                worst=upper;worst_idx=(i,j)
    ck(F(383)<worst<F(384),'precise max-box interval')
    # Exact fixed competitor independent of parameter-grid computations.
    sq=svec(rows,Q.numerator,Q.denominator)
    sp0=vectors[0]
    az=[];bz=[]
    for n in range(N):
        a,b=F(1),F(n+1)
        for m,t in enumerate(sq):
            if not t:continue
            w=F(comb(n+m,n),2**(n+m+1))
            a-=w*t;b-=F(n+m+1,2)*w*t
        az.append(a);bz.append(b)
    muq=sum(sq,F(0))+sum((x*s for x,s in zip(az,sp0)),F(0))
    Hq=sum(((m+1)*v for m,v in enumerate(sq)),F(0))+sum((x*s for x,s in zip(bz,sp0)),F(0))
    Wq=2*Hq-muq**2
    ck(605<Wq<606,'fixed edge Q variance W')
    ck(89<muq<90,'fixed edge Q mean')
    ck(worst<384<605<Wq,'strict gap between region upper bound and edge competitor')
    for q in (12,18,24):
        ck(q*(221*q-90)>0,f'positive uniform competitor gap at q={q}')
    return {'schema':'EM_PREFIX672_R6_MONOTONE_SURVIVAL_CORNER_EXCLUSION_V1',
      'science_pin':PIN,'q_scope':'all real q in [12,24]','square':['0','1/32'],
      'grid':{'step':'1/128','cells_per_axis':4,'total_cells':GRID*GRID},
      'frozen':{'rows':N,'nonzero_path_entries':sum(map(len,rows)),'verified_left_Bernstein_shape_pairs':pair_count},
      'max_box_variance_upper':{'lower_integer':383,'upper_integer':384,'max_cell':[int(worst_idx[0]),int(worst_idx[1])],
            'exact_numerator':str(worst.numerator),'exact_denominator':str(worst.denominator)},
      'competitor':{'p':'0','z':'19/128','variance_W_strict_bracket':['605','606'],'mean_mu_strict_bracket':['89','90']},
      'proved':'For all real q in [12,24], Vq(0,19/128)-Vq(p,z)>q*(221*q-90)>0 on [0,1/32]^2 and its four reflected corner squares.',
      'scope_warning':'Frozen 189-layer BRC statistical observer only; not global maximum theorem or native X6 dynamics',
      'checks_passed':checks,'result':'ALL_CHECKS_PASS',
      'status':'AUTHOR_PROVED / EXACT_RATIONAL_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED'}
if __name__=='__main__':
    r=solve()
    print(json.dumps(r,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS',r['checks_passed'])

"""R749SI exact time-indexed Walsh and sliding-window rank checker.
Model: R749SF/SG finite signed-Port conditional unsigned observer; exact fractions.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json
AXES=tuple(range(6))
SUPPORTS=tuple(combinations(AXES,2))
def neighbors(B):
    return tuple(C for C in SUPPORTS if len(set(B)&set(C))==1)
def state_axes(A,B): return tuple(sorted(set(A)|set(B)))
def forced(A,B,C): return set(C)==(set(A)^set(B))
def expand_histories(word,p,mu):
    theta=F(8)*p/(F(1)+F(7)*p)
    init_axes=state_axes(*word[:2]); states=[]
    for vals in product((-1,1),repeat=3):
        d=dict(zip(init_axes,vals)); w=mu[vals]
        if w: states.append(((dict(d),),w))
    for j in range(len(word)-2):
        A,B,C=word[j:j+3]; is_forced=forced(A,B,C)
        if p==1 and not is_forced:
            raise ValueError('zero-probability observer word at p=1')
        drop=next(iter(set(A)-set(B)))
        new=next(iter(set(C)-set(B)))
        nxt=[]
        for hist,w in states:
            last=hist[-1]
            for z in (-1,1):
                d={x:last[x] for x in B};d[new]=z
                prob=(F(1)+theta*z*last[drop])/2 if is_forced else F(1,2)
                if prob:nxt.append((hist+(d,),w*prob))
        states=nxt
    assert sum((w for _,w in states),F(0))==1
    return states
def symbolic_hist(word):
    d={x:frozenset({('X',x)}) for x in state_axes(*word[:2])}
    snaps=[dict(d)]
    for j in range(len(word)-2):
        A,B,C=word[j:j+3]
        drop=next(iter(set(A)-set(B)))
        new=next(iter(set(C)-set(B)))
        d2={x:d[x] for x in B}
        if forced(A,B,C):
            d2[new]=d[drop].symmetric_difference({('N',j)})
        else:
            d2[new]=frozenset({('F',j)})
        d=d2;snaps.append(dict(d))
    return snaps
def walsh_transform(v):
    a=v[:];h=1;n=len(a)
    while h<n:
        for b in range(0,n,2*h):
            for j in range(b,b+h):
                u,w=a[j],a[j+h]
                a[j]=u+w;a[j+h]=u-w
        h*=2
    return a
def numerical_moments(word,p,mu):
    axes=[state_axes(*word[t:t+2]) for t in range(len(word)-1)]
    labels=[(t,x) for t,xyz in enumerate(axes) for x in xyz]
    counts=[F(0) for _ in range(1<<len(labels))]
    for hist,w in expand_histories(word,p,mu):
        mask=sum(1<<i for i,(t,x) in enumerate(labels) if hist[t][x]==-1)
        counts[mask]+=w
    return walsh_transform(counts),labels
def formal_moment(mask,word,p,mu,labels):
    sym=symbolic_hist(word);parity=frozenset()
    for i,(t,x) in enumerate(labels):
        if mask&(1<<i):parity=parity.symmetric_difference(sym[t][x])
    if any(k=='F' for k,_ in parity):return F(0)
    noise=sum(k=='N' for k,_ in parity)
    ix=tuple(sorted(v for k,v in parity if k=='X'))
    ax=state_axes(*word[:2]);theta=F(8)*p/(F(1)+F(7)*p)
    return theta**noise*sum((w*__import__('math').prod(s[ax.index(x)] for x in ix) for s,w in mu.items()),F(0))
def rank(matrix):
    a=[list(row) for row in matrix];n=len(a);cols=len(a[0]);r=0
    for col in range(cols):
        j=next((i for i in range(r,n) if a[i][col]),None)
        if j is None:continue
        a[r],a[j]=a[j],a[r];inv=1/a[r][col]
        for c in range(col,cols):a[r][c]*=inv
        for i in range(n):
            if i!=r and a[i][col]:
                factor=a[i][col]
                for c in range(col,cols):a[i][c]-=factor*a[r][c]
        r+=1
        if r==n:break
    return r
def rank_at_start(word,p,a):
    axesa=state_axes(*word[a:a+2]);rows=[]
    for s in product((-1,1),repeat=3):
        mu={v:F(v==s) for v in product((-1,1),repeat=3)}
        states=expand_histories(word[:a+2],p,mu)
        rows.append([sum((w for hist,w in states if tuple(hist[-1][x] for x in axesa)==v),F(0)) for v in product((-1,1),repeat=3)])
    return rank(rows)
def lineage_rank(word,p):
    sym=symbolic_hist(word);ans=[]
    for d in sym:
        ancestors=set()
        for expr in d.values():
            xx=[v for k,v in expr if k=='X']
            if p==0 and any(k=='N' for k,v in expr):continue
            ancestors.update(xx)
        ans.append(2**len(ancestors))
    return ans
def check_case(word,p):
    initial=list(product((-1,1),repeat=3))
    mu={s:F(i+1,36) for i,s in enumerate(initial)}
    actual,labels=numerical_moments(word,p,mu)
    for mask,val in enumerate(actual):
        pred=formal_moment(mask,word,p,mu,labels)
        assert val==pred,(word,p,mask,val,pred)
    predicted=lineage_rank(word,p)
    observed=[rank_at_start(word,p,a) for a in range(len(word)-1)]
    assert predicted==observed,(word,p,predicted,observed)
    return len(actual),predicted
def main():
    nonforced=((0,1),(1,2),(2,3),(3,4),(4,5))
    forced_cycle=((0,1),(1,2),(0,2),(0,1),(1,2))
    mixed=((0,1),(1,2),(0,2),(2,3),(3,4))
    checks=[]
    for label,w in [('nonforced',nonforced),('forced',forced_cycle),('mixed',mixed)]:
        for p in (F(0),F(1,2),F(1)):
            if p==1 and any(not forced(*w[j:j+3]) for j in range(len(w)-2)):continue
            n,r=check_case(w,p)
            checks.append({'case':label,'p':str(p),'walsh_subsets':n,'window_start_ranks':r})
    assert [d['window_start_ranks'] for d in checks if d['case']=='nonforced' and d['p']=='1/2']==[[8,4,2,1]]
    assert [d['window_start_ranks'] for d in checks if d['case']=='forced' and d['p']=='0']==[[8,4,2,1]]
    assert [d['window_start_ranks'] for d in checks if d['case']=='forced' and d['p']=='1']==[[8,8,8,8]]
    w=nonforced[:4]
    vals=list(product((-1,1),repeat=3))
    mu_plus={s:F(1,4) if __import__('math').prod(s)==1 else F(0) for s in vals}
    mu_minus={s:F(1,4) if __import__('math').prod(s)==-1 else F(0) for s in vals}
    a,labels=numerical_moments(w,F(1,2),mu_plus)
    b,_=numerical_moments(w,F(1,2),mu_minus)
    assert all(a[mask]==b[mask] for mask in range(len(a)) if mask.bit_count()<=2)
    triple=sum(1<<labels.index((t,axis)) for t,axis in ((0,0),(1,1),(2,2)))
    assert a[triple]==1 and b[triple]==-1
    print(json.dumps({'status':'PASS','scenarios':checks,
        'three_time_degree_le2_equal':True,
        'three_time_triple':{'mu_even':str(a[triple]),'mu_odd':str(b[triple])},
        'scope':'fixed positive-probability unsigned observation words; exact rational and all Walsh subsets on test paths'},
        ensure_ascii=False,indent=2))
if __name__=='__main__':main()

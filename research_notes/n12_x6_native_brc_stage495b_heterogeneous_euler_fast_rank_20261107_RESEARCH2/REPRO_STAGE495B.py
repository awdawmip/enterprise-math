"""Stage495-B exact integer population and rank/unrank, signed native X6 directions.
This is a positive multiplicity-one value-word Euler/BRC branch model, not native dynamics.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import product
from math import factorial
import json, time

D=tuple('ABCDEFGHIJKL') # aliases for +E1..+E6,-E1..-E6

def inventory(word):
    m=Counter(zip(word,word[1:])); return m

def support(m,s,t):
    return sorted({s,t}|{a for (a,b),c in m.items() if c}|{b for (a,b),c in m.items() if c})

def outgoing(m):
    r=Counter()
    for (a,b),c in m.items():
        if c:r[a]+=c
    return r

def bareiss(A):
    n=len(A)
    if not n:return 1
    a=[list(map(int,row)) for row in A]; sign=1; prev=1
    for k in range(n-1):
        if not a[k][k]:
            piv=next((i for i in range(k+1,n) if a[i][k]),None)
            if piv is None:return 0
            a[k],a[piv]=a[piv],a[k]; sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q=a[i][j]*p-a[i][k]*a[k][j]
                assert q%prev==0
                a[i][j]=q//prev
            a[i][k]=0
        prev=p
    return sign*a[-1][-1]

def reduced_lap(m,verts,t):
    V=[v for v in verts if v!=t]
    L=[]
    for v in V:
        L.append([sum(c for (a,b),c in m.items() if c and a==v and b!=v) if v==w else -m.get((v,w),0) for w in V])
    return V,L

def count(m,s,t):
    if any(c<0 for c in m.values()):return 0
    n=sum(m.values())
    if n==0:return int(s==t)
    verts=support(m,s,t); out=outgoing(m); inc=Counter()
    for (a,b),c in m.items():
        if c:inc[b]+=c
    if any(out[v]-inc[v]!=(int(v==s)-int(v==t)) for v in verts):return 0
    if any(v!=t and out[v]==0 for v in verts):return 0
    _,L=reduced_lap(m,verts,t); tau=bareiss(L)
    if tau<=0:return 0
    num=tau*factorial(out[t])
    for v in verts:
        if v!=t:num*=factorial(out[v]-1)
    den=1
    for c in m.values():den*=factorial(c)
    assert num%den==0
    return num//den

def solve(A,b):
    n=len(A)
    aug=[[Fraction(x) for x in A[i]]+[Fraction(b[i])] for i in range(n)]
    for k in range(n):
        p=next((i for i in range(k,n) if aug[i][k]),None)
        if p is None:raise ValueError('singular')
        aug[k],aug[p]=aug[p],aug[k]
        q=aug[k][k];aug[k]=[x/q for x in aug[k]]
        for i in range(n):
            if i!=k:
                q=aug[i][k]
                if q:aug[i]=[v-q*w for v,w in zip(aug[i],aug[k])]
    return [row[-1] for row in aug]

def decrement(m,a,b):
    assert m.get((a,b),0)>0
    p=m.copy();p[(a,b)]-=1
    if not p[(a,b)]:del p[(a,b)]
    return p

def blocks(m,s,t):
    """One reduced-Laplacian solve for all support-preserving successors."""
    n=count(m,s,t)
    if not n:return {}
    V=support(m,s,t);out=outgoing(m)
    vs,L=reduced_lap(m,V,t);tau=bareiss(L)
    if s!=t:
        idx={v:i for i,v in enumerate(vs)}
        y=solve(L,[int(v==s) for v in vs])
        ys=y[idx[s]]
    else:
        idx={v:i for i,v in enumerate(vs)}; y=[];ys=Fraction(0)
    answer={}
    for b in sorted({b for (a,b),q in m.items() if a==s and q}):
        p=decrement(m,s,b)
        if support(p,b,t)!=V:
            val=count(p,b,t)
        else:
            tau2=Fraction(tau)
            if s!=t and s!=b:
                yb=y[idx[b]] if b!=t else Fraction(0)
                tau2=tau*(1-ys+yb)
            # For s=t, root Laplacian row is absent; for s=b, loops cancel.
            assert tau2.denominator==1
            den=out[s] if s==t else out[s]-1
            assert den>0
            q=Fraction(n*m[(s,b)]*int(tau2),den*tau)
            assert q.denominator==1
            val=int(q)
        if val:answer[b]=val
    assert sum(answer.values())==n,(s,t,n,answer)
    return answer

def unrank(m,s,t,k):
    m=m.copy(); N=count(m,s,t);assert 0<=k<N
    word=[s];q=0
    while m:
        bks=blocks(m,s,t);q+=1
        for b,amount in bks.items():
            if k<amount:break
            k-=amount
        else:raise AssertionError('rank overflow')
        m=decrement(m,s,b);s=b;word.append(s)
    assert s==t and k==0
    return ''.join(word),q

def rank(m,s,t,word):
    assert word[0]==s and word[-1]==t and inventory(word)==m
    m=m.copy();ans=0
    for b in word[1:]:
        bks=blocks(m,s,t)
        assert b in bks
        ans+=sum(v for x,v in bks.items() if x<b)
        m=decrement(m,s,b);s=b
    return ans

def brute():
    groups=defaultdict(list)
    for length in range(1,8):
        for w in product(D[:3],repeat=length):
            word=''.join(w);key=(tuple(sorted(inventory(word).items())),word[0],word[-1]);groups[key].append(word)
    total=0
    for (pairs,s,t),words in groups.items():
        m=Counter(dict(pairs));words.sort(); N=count(m,s,t)
        assert N==len(words)
        assert sum(blocks(m,s,t).values())==N if m else N==1
        for j,w in enumerate(words):
            got,_=unrank(m,s,t,j)
            assert got==w and rank(m,s,t,w)==j
            total+=1
    return len(groups),total

def full_example():
    # Baseline every ordered native direction pair once (144 edges),
    # plus heterogeneous loop/cycle repetitions (preserve Euler balance).
    m=Counter({(a,b):1 for a in D for b in D})
    for j,a in enumerate(D):m[(a,a)]+=j%5
    for j in range(12):
        a=D[j];b=D[(j+1)%12]
        m[(a,b)]+=j%3+1;m[(b,a)]+=j%3+1
    return m

def main():
    t0=time.perf_counter();ng,nw=brute(); t1=time.perf_counter()
    M=full_example();N=count(M,D[0],D[0]);bits=N.bit_length()
    kset=sorted({0,1,N//3,N//2,N-2,N-1})
    checks=[];count_queries=0
    for k in kset:
        w,q=unrank(M,D[0],D[0],k)
        assert inventory(w)==M
        assert rank(M,D[0],D[0],w)==k
        count_queries+=q
        checks.append({'rank_fraction':('last' if k==N-1 else 'first' if k==0 else str(k.bit_length())+'bit'), 'word_len':len(w),'blocks':q})
    t2=time.perf_counter()
    # Support-preserving block oracle vs independently recomputed full determinants.
    witness,_=unrank(M,D[0],D[0],N//2)
    cur=D[0];m=M.copy();manual=0;support_drop=0
    for b in witness[1:]:
        bp=blocks(m,cur,D[0]);ref={v:count(decrement(m,cur,v),v,D[0]) for v in bp}
        assert bp==ref
        p=decrement(m,cur,b)
        if support(p,b,D[0])!=support(m,cur,D[0]):support_drop+=1
        manual+=1;m=p;cur=b
    assert sum(M.values())+1==checks[0]['word_len']
    print(json.dumps({'stage':'495-B','model':'12 signed native X6 letters; positive unit BRC branch weight', 'brute_groups':ng,'brute_words':nw,'all_raw_multiplicities_preserved':True,'active_edge_types':len(M),'total_edges':sum(M.values()),'population_digits':len(str(N)),'population_bits':bits,'sample_rank_roundtrips':len(kset),'roundtrips':checks,'crosschecked_successor_layers':manual,'support_shrink_layers':support_drop,'unrank_rank_block_steps':count_queries,'brute_seconds':round(t1-t0,4),'full_seconds':round(t2-t1,4),'assertions':'PASSED'},sort_keys=True))
if __name__=='__main__':main()

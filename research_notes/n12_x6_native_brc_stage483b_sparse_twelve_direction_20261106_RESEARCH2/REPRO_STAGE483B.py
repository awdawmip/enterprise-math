"""Stage483-B: sparse directed Euler/positive BRC for all twelve signed X6 directions.
Scoped to ordered primitive path-word model, exact integer counting, no physics/phase attribution.
Frozen science: Global bf84bd7c61a2444b59b1da96be57df0e9ae47e53;
EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
"""
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import product,combinations
from math import factorial
import json

# First six positive +E1,...,+E6, last six negative -E1,...,-E6.
D='ABCDEFGHIJKL'; # G -> -E1, ..., L -> -E6.
VECTOR={c:tuple((1 if j==i%6 else 0) * (1 if i<6 else -1) for j in range(6))
        for i,c in enumerate(D)}
A='A'

def canonical(x):
    return tuple(sorted((a,b,int(v)) for (a,b),v in x.items() if v))

def entries(e):return {(a,b):n for a,b,n in e}

def E(word):return canonical(Counter(zip(word,word[1:])))

def sub(e,f):
    d=entries(e)
    for a,b,n in f:d[a,b]=d.get((a,b),0)-n
    if any(n<0 for n in d.values()):return None
    return canonical(d)

def add(e,f):
    d=Counter(entries(e));d.update(entries(f));return canonical(d)

def det_bareiss(matrix):
    """Fraction-free integral determinant, with exact pivoting and no external dependencies."""
    n=len(matrix)
    if not n:return 1
    a=[list(row) for row in matrix];sgn=1;den=1
    for k in range(n-1):
        if not a[k][k]:
            r=next((i for i in range(k+1,n) if a[i][k]),None)
            if r is None:return 0
            a[k],a[r]=a[r],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*pivot-a[i][k]*a[k][j]
                assert z%den==0
                a[i][j]=z//den
            a[i][k]=0
        den=pivot
    return sgn*a[-1][-1]

@lru_cache(None)
def N(ell,s,t,e):
    """Number of distinct vertex words of length ell, endpoints s,t, directed edge multiset e."""
    if ell<1 or sum(n for a,b,n in e)!=ell-1:return 0
    if ell==1:return int(s==t and not e)
    if not e:return 0
    od=Counter();id_=Counter()
    for a,b,n in e:
        if n<0:return 0
        od[a]+=n;id_[b]+=n
    active=sorted(set(od)|set(id_)|{s,t})
    if any(od[v]-id_[v]!=int(v==s)-int(v==t) for v in active):return 0
    other=[v for v in active if v!=t]
    if any(od[v]==0 for v in other):return 0
    ed=entries(e)
    lap=[[od[v] - ed.get((v,v),0) if v==w else -ed.get((v,w),0)
          for w in other] for v in other]
    tau=det_bareiss(lap)
    if tau<=0:return 0
    numerator=tau*factorial(od[t]);denominator=1
    for v in other:numerator*=factorial(od[v]-1)
    for _,_,n in e:denominator*=factorial(n)
    assert numerator%denominator==0
    return numerator//denominator

@lru_cache(None)
def suffix_dp(R,u,r):
    """Exact Boolean suffix support and positive word multiplicity, without suffix enumeration."""
    assert 0<=r<=u and sum(n for _,_,n in R)==u+1
    keys=tuple((a,b) for a,b,n in R);initial=tuple(n for a,b,n in R)
    incoming=defaultdict(list)
    for j,(x,y) in enumerate(keys):incoming[y].append((x,j))
    states={(A,initial):1};trans=0;max_states=1
    for _ in range(r):
        nxt=defaultdict(int)
        for (tip,rem),weight in states.items():
            for x,j in incoming[tip]:
                if rem[j]:
                    v=list(rem);v[j]-=1
                    nxt[(x,tuple(v))]+=weight;trans+=1
        states=dict(nxt);max_states=max(max_states,len(states))
    support=mass=0
    for (tip,rem),ways in states.items():
        residue=tuple((x,y,n) for (x,y),n in zip(keys,rem) if n)
        n=N(u-r+2,A,tip,residue)
        support+=ways*bool(n);mass+=ways*n
    assert mass==N(u+2,A,A,R)
    return support,mass,{'states_at_r':len(states),'max_states':max_states,'transitions':trans,'active_edges':len(R)}

def prefix_suffix_support(R,u,r,prefix):
    """# supported length-r suffixes with a given *left* prefix, computed backwards."""
    assert len(prefix)<=r
    keys=tuple((a,b) for a,b,n in R);initial=tuple(n for a,b,n in R)
    incoming=defaultdict(list);idx={edge:i for i,edge in enumerate(keys)}
    for j,(x,y) in enumerate(keys):incoming[y].append((x,j))
    states={(A,initial):1}
    for _ in range(r-len(prefix)):
        nxt=defaultdict(int)
        for (tip,rem),w in states.items():
            for x,j in incoming[tip]:
                if rem[j]:
                    v=list(rem);v[j]-=1;nxt[(x,tuple(v))]+=w
        states=dict(nxt)
    answer=0
    for (tip,rem),ways in states.items():
        v=list(rem);cur=tip
        for x in reversed(prefix):
            j=idx.get((x,cur))
            if j is None or not v[j]:break
            v[j]-=1;cur=x
        else:
            residue=tuple((x,y,n) for (x,y),n in zip(keys,v) if n)
            answer+=ways*bool(N(u-r+2,A,cur,residue))
    return answer

def rank_suffix(R,u,r,z):
    if len(z)!=r or prefix_suffix_support(R,u,r,z)!=1:raise ValueError('unsupported suffix')
    pos=0;pre=''
    for ch in z:
        for x in D:
            if x==ch:break
            pos+=prefix_suffix_support(R,u,r,pre+x)
        pre+=ch
    return pos

def unrank_suffix(R,u,r,n):
    support=suffix_dp(R,u,r)[0]
    if not 0<=n<support:raise ValueError('outside support')
    z=''
    for _ in range(r):
        for x in D:
            count=prefix_suffix_support(R,u,r,z+x)
            if n>=count:n-=count
            else:z+=x;break
        else:raise AssertionError('missing branch')
    return z

def theta(k,w,h):return E(A*(2*k+2)+w+A+h+A)

def base(k,w):return E(A*(2*k+2)+w+A)

def bounded_counts(edges,budget,i=0,prefix=()):
    if i==len(edges):
        if budget==0:yield prefix
        return
    for z in range(min(edges[i][2],budget)+1):
        yield from bounded_counts(edges,budget-z,i+1,prefix+(z,))

@lru_cache(None)
def types(k,u,r,T):
    """Exact W directed-types; no W-word enumeration, support of T only."""
    starter=E(A*(2*k+2));rem=sub(T,starter)
    if rem is None:return ()
    edgekeys=[(a,b) for a,b,_ in rem]
    letters=sorted(set([A]+[a for a,b,_ in rem]+[b for a,b,_ in rem]))
    out=[]
    for counts in bounded_counts(rem,k-1):
        ew=tuple((a,b,n) for (a,b),n in zip(edgekeys,counts) if n)
        for s in letters:
            for t in letters:
                wcnt=N(k,s,t,ew)
                if not wcnt:continue
                B=add(starter,((A,s,1),))
                B=add(B,ew)
                B=add(B,((t,A,1),))
                R=sub(T,B)
                if R is None:continue
                q,p,det=suffix_dp(R,u,r)
                if q:out.append((s,t,ew,R,wcnt,q,p))
    return tuple(out)

def fiber(k,u,r,T):
    rows=types(k,u,r,T)
    return {'classes':sum(n*q for s,t,e,R,n,q,p in rows),
            'population':sum(n*p for s,t,e,R,n,q,p in rows),
            'w_types':len(rows),
            'distinct_R':len({R for s,t,e,R,n,q,p in rows}),
            'type_weighted_transitions':sum(suffix_dp(R,u,r)[2]['transitions'] for s,t,e,R,n,q,p in rows),
            'unique_R_transitions':sum(suffix_dp(R,u,r)[2]['transitions'] for R in {R for s,t,e,R,n,q,p in rows})}

def w_prefix_support(k,u,r,T,prefix):
    if len(prefix)>k:return 0
    prefedges=E(prefix);out=0
    for s,t,ew,R,wcnt,q,p in types(k,u,r,T):
        if prefix:
            if s!=prefix[0]:continue
            rem=sub(ew,prefedges)
            if rem is None:continue
            wc=N(k-len(prefix)+1,prefix[-1],t,rem)
        else:wc=wcnt
        out+=wc*q
    return out

def rank_key(k,u,r,T,w,z):
    if len(w)!=k:raise ValueError('wrong W')
    R=sub(T,base(k,w))
    if R is None:raise ValueError('invalid fiber')
    ans=0;pre=''
    for ch in w:
        for x in D:
            if x==ch:break
            ans+=w_prefix_support(k,u,r,T,pre+x)
        pre+=ch
    return ans+rank_suffix(R,u,r,z)

def unrank_key(k,u,r,T,idx):
    if not 0<=idx<w_prefix_support(k,u,r,T,''):raise ValueError('outside fiber')
    w=''
    for _ in range(k):
        for ch in D:
            cnt=w_prefix_support(k,u,r,T,w+ch)
            if idx>=cnt:idx-=cnt
            else:w+=ch;break
        else:raise AssertionError('missing W branch')
    R=sub(T,base(k,w))
    return w,unrank_suffix(R,u,r,idx)

def brute_fibers(k,u,letters):
    bins=defaultdict(list)
    for w in map(''.join,product(letters,repeat=k)):
        for h in map(''.join,product(letters,repeat=u)):
            bins[theta(k,w,h)].append((w,h))
    return bins

def displacement(word):
    return tuple(sum(VECTOR[x][i] for x in word) for i in range(6))

def observation(p,q):
    return (len(p),len(q),displacement(p),displacement(q),E(p),E(q),sum(x==y for x,y in zip(p,q)))

def future_equivalent(k,h,P,Q1,Q2):
    """Full identical-operation future-tree check with all 12 APPEND directions."""
    # Bound individual P pops/appends by k; Q pops by h, appends by 1.
    todo=[(P,Q1,Q2,0,0,0,0)];visited=set();n=0
    while todo:
        p,q1,q2,pp,pa,qp,qa=todo.pop()
        state=(p,q1,q2,pp,pa,qp,qa)
        if state in visited:continue
        visited.add(state);n+=1
        if observation(p,q1)!=observation(p,q2):return False,n
        if pp<k and len(p)>1:todo.append((p[:-1],q1,q2,pp+1,pa,qp,qa))
        if qp<h and len(q1)>1:todo.append((p,q1[:-1],q2[:-1],pp,pa,qp+1,qa))
        if pa<k:
            for a in D:todo.append((p+a,q1,q2,pp,pa+1,qp,qa))
        if qa<1:
            for a in D:todo.append((p,q1+a,q2+a,pp,pa,qp,qa+1))
    return True,n

def run():
    # Unit tests for fraction-free determinant, including row pivot.
    assert det_bareiss([[0,1],[1,0]])==-1
    assert det_bareiss([[2,-1,0],[-1,2,-1],[0,-1,2]])==4
    # Exhaustive Euler word counting on small alphabet including negative signed directions.
    euler_types=set();euler_words_tested=0
    for n in range(1,6):
        buckets=Counter()
        for tup in product('ABG',repeat=n):
            word=''.join(tup);buckets[(word[0],word[-1],E(word))]+=1;euler_words_tested+=1
        for (s,t,e),cnt in buckets.items():
            assert N(n,s,t,e)==cnt
        euler_types.update(buckets)
    # All twelve primitive directions exercised in basic exact counting, including reverse signed steps.
    for x in D:
        assert N(3,A,A,E(A+x+A))==1
        assert displacement(x)[(D.index(x)%6)]==(1 if D.index(x)<6 else -1)
    # Exhaust small complete-observation fibers; use three-letter signed support including G=-E1.
    fibercases=raw=class_occ=keys_ranked=0
    cases=[(1,1,'ABG'),(1,2,'ABG'),(1,3,'ABG'),(2,1,'ABG'),(2,2,'ABG'),(2,3,'ABG'),(2,2,'ABCG'),(3,1,'ABG')]
    cases += [(1,2,'A'+x) for x in D[1:]]
    for k,u,letters in cases:
        grouped=brute_fibers(k,u,letters)
        for T,items in grouped.items():
            # Fixed T implies fixed signed displacement, as Q always ends with A.
            assert len({displacement(A*(2*k+2)+w+A+H+A) for w,H in items})==1
            for r in range(u+1):
                actual=Counter((w,H[-r:] if r else '') for w,H in items)
                got=fiber(k,u,r,T)
                assert got['classes']==len(actual),(k,u,r,T,got,actual)
                assert got['population']==len(items)
                fibercases+=1;raw+=len(items);class_occ+=len(actual)
                if len(actual)<=18 and k<=2:
                    for j,key in enumerate(sorted(actual)):
                        assert rank_key(k,u,r,T,*key)==j
                        assert unrank_key(k,u,r,T,j)==key
                        keys_ranked+=1
    # Non-degenerate, larger sparse support: 12-direction alphabet, three active letters and signed reversals.
    k,u=16,13
    W=('ABGA' * 4)[:k];H=('AGBA' * 4)[:u]
    assert 'G' in W+H and 'B' in W+H
    large_T=theta(k,W,H);res=[]
    for r in (0,1,3,6,9,13):
        f=fiber(k,u,r,large_T)
        assert f['classes']>0 and f['population']>=f['classes']
        assert f['population']==N(u+2,A,A,sub(large_T,base(k,W))) or f['population']>=N(u+2,A,A,sub(large_T,base(k,W)))
        res.append({'r':r,**f})
    assert len({x['population'] for x in res})==1
    # Independent direct-simulation future equivalence for a nontrivial same-key pair.
    k,u,h=1,4,1
    grouped=brute_fibers(k,u,'ABG')
    pair=None
    for T,items in grouped.items():
        found={}
        for w,H in items:
            key=(w,H[-h:])
            if key in found and found[key]!=H:pair=(w,found[key],H,T);break
            found[key]=H
        if pair:break
    assert pair is not None
    same_w,same_h1,same_h2,same_theta=pair
    P=A*(2*k+2);Q1=P+same_w+A+same_h1+A;Q2=P+same_w+A+same_h2+A
    eq,visits=future_equivalent(k,h,P,Q1,Q2)
    assert eq
    # Distinct suffix pairs with identical initial observation are distinguished by Q POP.
    other=None
    for T,items in grouped.items():
        for (w1,H1),(w2,H2) in combinations(items,2):
            if w1==w2 and H1[-2:]!=H2[-2:]:
                other=(w1,H1,H2);break
        if other:break
    assert other is not None
    ow,oh1,oh2=other
    qe1=P+ow+A+oh1+A;qe2=P+ow+A+oh2+A
    neq,negative_visits=future_equivalent(k,2,P,qe1,qe2)
    assert not neq
    # A changed W is visible through P's allowed APPEND, with identical initial observation.
    changed_w=None
    for T0,items in grouped.items():
        for (w1,h1),(w2,h2) in combinations(items,2):
            if w1!=w2:
                changed_w=(w1,h1,w2,h2);break
        if changed_w:break
    assert changed_w is not None
    w1,h1,w2,h2=changed_w
    different_w_eq,different_w_visits=future_equivalent(k,1,P,P+w1+A+h1+A,P+w2+A+h2+A)
    assert not different_w_eq
    return {'status':'ALL_ASSERTIONS_PASSED','model':'native_X6_12_signed_directions_positive_integer_BRC',
            'signed_alphabet':{c:('+' if i<6 else '-')+f'E{i%6+1}' for i,c in enumerate(D)},
            'euler_exact':{'word_cases':euler_words_tested,'types':len(euler_types)},
            'finite_fibers':{'fiber_budget_cases':fibercases,'history_occurrences':raw,'class_occurrences':class_occ,'full_key_rank_checks':keys_ranked},
            'large_sparse':{'k':16,'u':13,'theta':list(large_T),'edge_support':len(large_T),'active_letters':len({x for a,b,n in large_T for x in (a,b)}),
                            'scenarios':res,'full_word_search_space':'12^29'},
            'future_tree':{'same_key_pair':{'W':same_w,'H1':same_h1,'H2':same_h2,'visited_states':visits},
                           'different_key_pair':{'W':ow,'H1':oh1,'H2':oh2,'visited_before_distinction':negative_visits},
                           'different_W_pair':{'W1':w1,'H1':h1,'W2':w2,'H2':h2,'visited_before_distinction':different_w_visits}},
            'N_cache':N.cache_info()._asdict(),'types_cache':types.cache_info()._asdict()}

if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))

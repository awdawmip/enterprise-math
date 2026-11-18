"""Rational inertia certificates for prime-replacement graphs. Python 3.9+."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt, lcm
import json


def factorizations(X):
    fs=[()]*(X+1)
    primes=[]
    for n in range(2,X+1):
        p=next((p for p in primes if n%p==0),n)
        if p==n:
            primes.append(p)
        fs[n]=(p,)+fs[n//p]
    return fs,primes


def signed_inertia(M):
    """Positive, zero, negative counts by symmetric fraction-free elimination."""
    a=[row[:] for row in M]
    n=len(a)
    previous=1
    pos=neg=0
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][i]),None)
        if pivot is None:
            # On the trailing subspace replace a basis vector e_i by e_i+e_j.
            edge=next(((i,j) for i in range(k,n) for j in range(i+1,n) if a[i][j]),None)
            if edge is None:
                return (pos,n-k,neg)
            i,j=edge
            a[i][i]=2*a[i][j]
            for h in range(k,n):
                if h!=i:
                    a[h][i]=a[i][h]=a[i][h]+a[j][h]
            pivot=i
        if pivot!=k:
            a[pivot],a[k]=a[k],a[pivot]
            for row in a:
                row[pivot],row[k]=row[k],row[pivot]
        q=a[k][k]
        if q*previous>0:
            pos+=1
        else:
            neg+=1
        for i in range(k+1,n):
            ci=a[i][k]
            for j in range(i,n):
                v=q*a[i][j]-ci*a[k][j]
                t,r=divmod(v,previous)
                assert r==0
                a[i][j]=a[j][i]=t
        previous=q
    return (pos,0,neg)


def fraction_free_rank(rows):
    if not rows:
        return 0
    a=[row[:] for row in rows]
    r=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        for i in range(r+1,len(a)):
            if not a[i][col]:
                continue
            f,g=a[r][col],a[i][col]
            common=gcd(f,g)
            f//=common
            g//=common
            a[i]=[f*b-g*c for b,c in zip(a[i],a[r])]
            content=0
            for v in a[i]:
                content=gcd(content,v)
            if content>1:
                a[i]=[v//content for v in a[i]]
        r+=1
        if r==len(a):
            break
    return r


class Graph:
    def __init__(self,X,k):
        fs,primes=factorizations(X)
        self.verts=[n for n in range(2,X+1) if len(fs[n])==k]
        self.V=len(self.verts)
        self.w=[len(set(fs[n])) for n in self.verts]
        gs=sorted({n//p for n in self.verts for p in fs[n]})
        index={g:j for j,g in enumerate(gs)}
        self.C=len(gs)
        self.inc=[[index[n//p] for p in sorted(set(fs[n]))] for n in self.verts]
        degrees=Counter(i for indices in self.inc for i in indices)
        self.sizes=[degrees[i] for i in range(self.C)]
        assert self.sizes==[sum(p<=X//g for p in primes) for g in gs]
        self.cliques=gs
        self.maxdeg=max(sum(self.sizes[j]-1 for j in indices) for indices in self.inc)
        self.numedges=sum(d*(d-1)//2 for d in self.sizes)
        pnum={p:j for j,p in enumerate(primes,1)}
        self.squarefree=[i for i in range(self.V) if self.w[i]==k]
        self.ballot=[self.verts[i] for i in self.squarefree if all(
            pnum[p]>=2*j for j,p in enumerate(fs[self.verts[i]],1))]
        cols=[[int(g in self.inc[i]) for i in self.squarefree] for g in range(self.C)]
        self.inc_null=len(self.squarefree)-fraction_free_rank(cols)
        assert self.inc_null==len(self.ballot)
        self.base=Counter()
        for w,indices in zip(self.w,self.inc):
            for i in indices:
                for j in indices:
                    if i<=j:
                        self.base[w,i,j]+=1

    def direct_matrix(self):
        # Independent adjacency test on quotients of the two integers, without consulting cliques.
        v=self.verts
        limit=max(v)
        fs,_=factorizations(limit)
        A=[[0]*len(v) for _ in v]
        for i,u in enumerate(v):
            for j in range(i+1,len(v)):
                z=v[j]
                g=gcd(u,z)
                flag=int(len(fs[u//g])==len(fs[z//g])==1)
                assert flag==len(set(self.inc[i])&set(self.inc[j]))
                A[i][j]=A[j][i]=flag
        assert sum(map(sum,A))==2*self.numedges
        return A

    def threshold(self,t):
        # Congruence by a strictly positive integer scalar, not by a rounded determinant.
        a,b=t.numerator,t.denominator
        ws=set(self.w)
        denom={w:a+b*w for w in ws}
        assert all(x>0 for x in denom.values())
        scale=lcm(*denom.values())
        factor={w:b*(scale//denom[w]) for w in ws}
        H=[[0]*self.C for _ in range(self.C)]
        for (w,i,j),v in self.base.items():
            H[i][j]+=factor[w]*v
            if i!=j:
                H[j][i]+=factor[w]*v
        for i in range(self.C):
            H[i][i]-=scale
        return signed_inertia(H)[:2]


def ration(v):
    return str(Fraction(v))


def intervals(g,howmany,grid=4096):
    cache=lru_cache(None)(g.threshold)
    positives=cache(Fraction(0))[0]
    rows=[]
    ranking=sorted((w-1,coin) for coin,w in zip(g.cliques,g.sizes))[::-1]
    distinct=sorted(set(d for d,_ in ranking))
    for j in range(1,min(howmany,positives)+1):
        left,right=0,(g.maxdeg+1)*grid
        while right-left>1:
            middle=(left+right)//2
            u,v=cache(Fraction(middle,grid))
            if u<j<=u+v:
                left=right=middle
                break
            if u>=j:
                left=middle
            else:
                right=middle
        lo,hi=Fraction(left,grid),Fraction(right,grid)
        nlo,zlo=cache(lo)
        nhi,zhi=cache(hi)
        if nlo<j<=nlo+zlo:
            hi=lo
            nhi,zhi=nlo,zlo
        elif nhi<j<=nhi+zhi:
            lo=hi
            nlo,zlo=nhi,zhi
        assert (lo==hi and nlo<j<=nlo+zlo) or (nlo>=j>nhi+zhi)
        # Voronoi cells of the distinct clique values. Each possible nearest value
        # is retained on a midpoint/tie. All examples except explicit ties are decisive.
        nearest=[]
        for idx,v in enumerate(distinct):
            if idx>0 and 2*hi<distinct[idx-1]+v:
                continue
            if idx+1<len(distinct) and 2*lo>distinct[idx+1]+v:
                continue
            nearest.append(v)
        rk=ranking[j-1][0] if j<=len(ranking) else None
        rows.append(dict(j=j,low=ration(lo),high=ration(hi),
                         at_low_above_equal=[nlo,zlo],at_high_above_equal=[nhi,zhi],
                         same_rank_clique=rk,possible_nearest_clique_values=nearest,
                         same_rank_among_possible_nearest=(rk in nearest)))
    for row in rows:
        anchor=row['same_rank_clique']
        own_lo,own_hi=Fraction(row['low']),Fraction(row['high'])
        own_min=max(own_lo-anchor,anchor-own_hi,0)
        row['strictly_closer_eigenvalue_ranks_to_this_anchor']=[
            candidate['j'] for candidate in rows if
            max(abs(Fraction(candidate['low'])-anchor),abs(Fraction(candidate['high'])-anchor))<own_min]
    return positives,rows,cache.cache_info().currsize


def sample(X,k,count=4,direct=False):
    g=Graph(X,k)
    positive,rows,thresholds=intervals(g,count)
    verified=[]
    if direct:
        A=g.direct_matrix()
        shifts=[Fraction(-k),Fraction(-k)-1,Fraction(0),Fraction(1,3),Fraction(2),Fraction(11,2)]
        shifts.extend(Fraction(row['low']) for row in rows)
        shifts.extend(Fraction(row['high']) for row in rows)
        for t in sorted(set(shifts)):
            m=[[t.denominator*x-int(i==j)*t.numerator for j,x in enumerate(row)]
               for i,row in enumerate(A)]
            inertia=signed_inertia(m)
            if t==-k:
                assert inertia[2]==0 and inertia[1]==g.inc_null
            if t<-k:
                assert inertia[0]==g.V
            if t>=0:
                assert inertia[:2]==g.threshold(t)
            verified.append([ration(t),list(inertia)])
    return dict(X=X,k=k,vertices=g.V,cliques=g.C,edges=g.numedges,
                clique_details_g_and_d_minus_one=[[c,v-1] for c,v in zip(g.cliques,g.sizes)],
                positive_eigenvalues=positive,distinct_reduced_thresholds=thresholds,top=rows,
                bottom_minus_k_multiplicity=g.inc_null,
                ballot_vertices_at_minus_k=g.ballot,direct_inertia_at_selected_thresholds=verified)


def incremental_endpoint(k,bound):
    """Independent rank of one new squarefree deletion column per admitted integer."""
    fs,primes=factorizations(bound)
    indices={p:i for i,p in enumerate(primes,1)}
    basis={}
    num=nullity=0
    changes=[]
    for n,ps in enumerate(fs):
        if len(ps)!=k or len(set(ps))!=k:
            continue
        num+=1
        v={n//p:Fraction(1) for p in ps}
        while v:
            pivot=max(v)
            if pivot not in basis:
                top=v[pivot]
                basis[pivot]={r:c/top for r,c in v.items()}
                break
            f=v[pivot]
            for r,y in basis[pivot].items():
                new=v.get(r,0)-f*y
                if new:
                    v[r]=new
                else:
                    v.pop(r,None)
        dependent=not v
        ballot=all(indices[p]>=2*j for j,p in enumerate(ps,1))
        assert dependent==ballot
        if dependent:
            nullity+=1
            if len(changes)<6:
                changes.append(n)
    return dict(k=k,all_X_through=bound,squarefree_columns=num,final_nullity=nullity,
                first_six_increases=changes)

def prime_core_constants():
    """Outward rational bounds for the first two fixed prime-core offsets."""
    cutoff = 12_000_000
    scale = 10**24

    def ceil_ratio(a,b):
        return -((-a)//b)

    def bracket_frac(v):
        return (v.numerator*scale//v.denominator,ceil_ratio(v.numerator*scale,v.denominator))

    def decimals(bounds,places=13):
        unit = 10**places
        def fmt(x):
            return ('-' if x<0 else '')+str(abs(x)//unit)+'.'+str(abs(x)%unit).zfill(places)
        lo,hi=bounds
        return [fmt(lo*unit//scale),fmt(ceil_ratio(hi*unit,scale))]

    # gamma = H_n - log n - 1/(2n) + sum of the positive trapezoid errors of 1/x.
    # Each error on [j,j+1] is at most max(f'')/12 = 1/(6 j^3).
    exponent=16
    n=2**exponent
    h_lo=sum(scale//j for j in range(1,n+1))
    h_hi=sum(ceil_ratio(scale,j) for j in range(1,n+1))
    terms=32
    ln2=sum(Fraction(2,(2*j+1)*3**(2*j+1)) for j in range(terms))
    ln2_tail=Fraction(9,8)*Fraction(2,(2*terms+1)*3**(2*terms+1))
    gamma_lo=h_lo+bracket_frac(-exponent*(ln2+ln2_tail)-Fraction(1,2*n))[0]
    gamma_hi=h_hi+bracket_frac(-exponent*ln2-Fraction(1,2*n)
                                +Fraction(1,6*n**3)+Fraction(1,12*n*n))[1]

    odd=bytearray([1])*((cutoff+1)//2)
    odd[0]=0
    for p in range(3,isqrt(cutoff)+1,2):
        if odd[p//2]:
            first=p*p//2
            odd[first::p]=bytes((len(odd)-1-first)//p+1)
    cores=(2,3)
    mix={p:[0,0] for p in cores}
    primes_seen=0
    series_terms=0
    log_lo=log_hi=0
    def accumulate(q):
        nonlocal primes_seen,series_terms,log_lo,log_hi
        primes_seen+=1
        # L(q)=-log(1-1/q)-1/q, positive from m=2 onwards.
        m,q_power=2,q*q
        while True:
            den=m*q_power
            u,rem=divmod(scale,den)
            if u==0:
                log_hi+=2  # Remaining geometric majorant < 2/scale.
                break
            series_terms+=1
            log_lo+=u
            log_hi+=u+(rem!=0)
            m+=1
            q_power*=q
        for p in cores:
            if q==p:
                continue
            numerator=(p+q)**2 if q<p else 4*p*p
            denominator=q*(q-p)
            mix[p][0]+=numerator*scale//denominator
            mix[p][1]+=ceil_ratio(numerator*scale,denominator)
    accumulate(2)
    for i,flag in enumerate(odd):
        if flag:
            accumulate(2*i+1)
    bp=(gamma_lo-log_hi,gamma_hi-log_lo)
    tail_b=Fraction(1,2*cutoff)
    core_results={}
    for p in cores:
        # The only prime smaller than either of these cores is 2 for p=3.
        correction=-4-3*sum((Fraction(p,q)-1) for q in cores if q<p)
        mix_tail=4*p*sum(Fraction(1,r) for r in range(cutoff-p+1,cutoff+1))
        low=4*p*bp[0]+mix[p][0]+bracket_frac(correction-4*p*tail_b)[0]
        high=4*p*bp[1]+mix[p][1]+bracket_frac(correction+mix_tail)[1]
        core_results[p]=dict(mix_partial=decimals(mix[p]),mix_tail_upper=str(mix_tail),
                             infinite_constant_bracket=decimals((low,high),7))
    return dict(prime_cutoff=cutoff,number_of_primes=primes_seen,fixed_point_scale=str(scale),
                gamma_harmonic_cutoff=n,ln2_atanh_terms=terms,gamma_bracket=decimals((gamma_lo,gamma_hi)),
                log_series_terms_summed=series_terms,B1_partial=decimals(bp),B1_tail_upper=str(tail_b),
                B1_bracket=decimals((bp[0]-bracket_frac(tail_b)[1],bp[1])),
                prime_core_constants=core_results)


def main():
    # Exercise the mixed-sign hyperbolic two-by-two pivot, and singular edge cases.
    assert signed_inertia([[0,1],[1,0]])==(1,0,1)
    assert signed_inertia([[1,2],[2,4]])==(1,1,0)
    assert signed_inertia([[-1,1,0],[1,-1,1],[0,1,-1]])==(1,0,2)
    cases=[(18,1,2,True),(20,2,5,True),(21,2,5,True),(45,2,5,True),
           (90,2,5,False),(180,2,5,False),(45,3,4,True),(90,3,5,True),
           (180,3,5,False),(272,3,5,False),(273,3,5,False),(360,3,5,False)]
    data=[sample(*case) for case in cases]
    assert any(not row['same_rank_among_possible_nearest'] for g in data for row in g['top'])
    incremental=[incremental_endpoint(k,bound) for k,bound in [(1,120),(2,180),(3,500),(4,5300)]]
    assert [a['first_six_increases'][0] for a in incremental]==[3,21,273,5187]
    print(json.dumps({'dyadic_denominator':4096,'case_count':len(data),'samples':data,
                      'incremental_squarefree_deletion_checks':incremental,
                      'fixed_prime_core_constants':prime_core_constants()},
                     indent=2))
if __name__=='__main__':
    main()

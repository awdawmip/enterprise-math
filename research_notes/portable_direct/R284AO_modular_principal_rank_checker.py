"""R284AO deterministic multi-prime exterior-span principal rank checker.

Works on full-column-rank integer factors X,Y for C = X Y^T.
The algorithm and finite tests use exact integer arithmetic only.
"""
from math import comb, factorial, prod
from itertools import combinations
import random, json, hashlib


def primes():
    found=[]
    n=2
    while True:
        if all(n % p for p in found if p*p<=n):
            found.append(n)
            yield n
        n+=1


def primes_for_bound(B):
    out=[]; product=1
    for p in primes():
        out.append(p); product*=p
        if product>B:
            return out,product


def wedge_append(coeff,row,j,oldcols,newcols):
    oldidx={t:i for i,t in enumerate(oldcols)}
    out=[]
    for J in newcols:
        z=0
        for pos,a in enumerate(J):
            t=J[:pos]+J[pos+1:]
            z+=(-1 if (j-1-pos)%2 else 1)*coeff[oldidx[t]]*row[a]
        out.append(z)
    return tuple(out)


class ModSpan:
    def __init__(self,p):
        self.p=p
        self.pivots={}
    def remainder(self,vec):
        p=self.p
        v=[int(z)%p for z in vec]
        for i,row in sorted(self.pivots.items()):
            z=v[i]
            if z:
                v=[(a-z*b)%p for a,b in zip(v,row)]
        return v
    def possible_rank(self,vec):
        return len(self.pivots)+any(self.remainder(vec))
    def add(self,vec):
        v=self.remainder(vec)
        i=next((i for i,z in enumerate(v) if z),None)
        if i is None:return False
        p=self.p
        f=pow(v[i],-1,p)
        self.pivots[i]=tuple((z*f)%p for z in v)
        return True


class Grade:
    def __init__(self,j,k,M):
        self.j=j
        self.dim=comb(k,j)**2
        H=factorial(j)**2*M**(2*j)
        self.bound=factorial(self.dim)*H**self.dim
        self.primes,self.prime_product=primes_for_bound(self.bound)
        self.spans=[ModSpan(p) for p in self.primes]
        self.basis=[]
        self.tested=0
    def add(self,S,a,b):
        z=tuple(x*y for x in a for y in b)
        self.tested+=1
        d=len(self.basis)
        independent=any(s.possible_rank(z)>d for s in self.spans)
        if independent:
            self.basis.append((tuple(S),tuple(a),tuple(b)))
            for s in self.spans:s.add(z)
        return independent
    def verify_basis(self):
        d=len(self.basis)
        return max(len(s.pivots) for s in self.spans)==d


def determinant(M):
    # Exact Leibniz formula for small finite independent test instances.
    n=len(M)
    if not n:return 1
    total=0
    from itertools import permutations
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        total+=sign*prod(M[i][p[i]] for i in range(n))
    return total


def solve(X,Y):
    m=len(X);k=len(X[0]) if m else 0
    assert len(Y)==m and all(len(x)==k for x in X+Y)
    assert all(isinstance(a,int) for row in X+Y for a in row)
    M=max(1,*(abs(a) for row in X+Y for a in row))
    grades=[Grade(j,k,M) for j in range(k+1)]
    grades[0].add((),(1,),(1,))
    cols={j:list(combinations(range(k),j)) for j in range(k+1)}
    for i in range(m):
        for j in range(min(k,i+1),0,-1):
            for S,a,b in tuple(grades[j-1].basis):
                ta=wedge_append(a,X[i],j,cols[j-1],cols[j])
                tb=wedge_append(b,Y[i],j,cols[j-1],cols[j])
                grades[j].add(S+(i,),ta,tb)
    d=0;witness=None;value=None
    for j in range(1,k+1):
        for S,a,b in grades[j].basis:
            tr=sum(u*v for u,v in zip(a,b))
            if tr:
                d=j;witness=S;value=tr
                break
    assert all(g.verify_basis() for g in grades)
    assert all(sum(u*v for u,v in zip(a,b))==0
               for g in grades[d+1:] for _,a,b in g.basis)
    return {'m':m,'k':k,'d':d,'witness':[i+1 for i in witness] if witness else [],
            'witness_det':value,'basis_dims':[len(g.basis) for g in grades],
            'candidate_counts':[g.tested for g in grades],
            'prime_counts':[len(g.primes) for g in grades],
            'max_prime':max((g.primes[-1] for g in grades),default=None),
            'max_bound_bits':max((g.bound.bit_length() for g in grades),default=0),
            'all_prime_products_exceed_bounds':all(g.prime_product>g.bound for g in grades)}


def exhaustive(X,Y):
    m=len(X);k=len(X[0]);C=[[sum(X[i][t]*Y[j][t] for t in range(k)) for j in range(m)] for i in range(m)]
    d=0
    for j in range(1,min(m,k)+1):
        for S in combinations(range(m),j):
            if determinant([[C[a][b] for b in S] for a in S]):d=j
    return d


def main():
    rng=random.Random(284015)
    sizes=[]; totals=0; results=[]
    for m in range(2,7):
        for k in range(1,min(m,3)+1):
            for _ in range(3):
                X=[[rng.randint(-3,4) for _ in range(k)] for __ in range(m)]
                Y=[[rng.randint(-3,4) for _ in range(k)] for __ in range(m)]
                report=solve(X,Y)
                assert report['d']==exhaustive(X,Y),(X,Y,report)
                if report['witness']:
                    C=[[sum(X[i][t]*Y[j][t] for t in range(k)) for j in range(m)] for i in range(m)]
                    S=[a-1 for a in report['witness']]
                    assert determinant([[C[a][b] for b in S] for a in S])==report['witness_det']
                totals+=1;sizes.append((m,k));results.append(report)
    for X,Y,expect in [([[1],[0]],[[0],[1]],0),
                         ([[1],[0]],[[1],[0]],1),
                         ([[1,0],[0,1],[1,1]],[[0,1],[1,0],[1,1]],2)]:
        report=solve(X,Y)
        assert report['d']==expect==exhaustive(X,Y)
        results.append(report)
    ans={'status':'PASS','unit':'R284AO','arithmetic':'exact integers, finite primes and modular echelon',
         'random_seed':284015,'small_exhaustive_cases':totals,'targeted_cases':3,
         'max_candidates':max(sum(r['candidate_counts']) for r in results),
         'max_primes_per_grade':max(max(r['prime_counts']) for r in results),
         'max_hadamard_bound_bits':max(r['max_bound_bits'] for r in results),
         'sample_nilpotent':results[-3],
         'sample_highest_dimension':next(r for r in reversed(results) if r['m']==6 and r['k']==3),
         'claim':'Deterministic exact principal degree via multi-prime state spans',
         'review':'NOT_REVIEWED'}
    with open('/mnt/data/R284AO_modular_principal_rank_verification.json','w') as f:json.dump(ans,f,indent=2)
    print(json.dumps(ans,indent=2))


if __name__=='__main__':main()

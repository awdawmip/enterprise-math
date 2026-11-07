"""Stage494-B: exact BRC branch counts and lex ranks for directed Euler words.
All arrows are typed ordered X6 direction pairs, no geometric propagation.
Use only exact integer arithmetic and full ordered path observer.
"""
from collections import Counter
from itertools import product
from math import factorial
from random import Random
from time import perf_counter


def det_bareiss(a):
    a = [r[:] for r in a]
    n = len(a)
    if not n: return 1
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1,n) if a[j][k]), None)
            if j is None: return 0
            a[k], a[j] = a[j]
            sign = -sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num % prev == 0
                a[i][j]=num//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]


def completion_count(m, start, end):
    """Number of value-words using each directed edge multiplicity exactly."""
    d=len(m)
    out=[sum(row) for row in m]
    inc=[sum(m[i][j] for i in range(d)) for j in range(d)]
    edges=sum(out)
    if not edges: return int(start == end)
    for v in range(d):
        expected=int(v == start)-int(v == end)
        if out[v]-inc[v] != expected:
            return 0
    vertices=[v for v in range(d) if out[v] or inc[v] or v in (start,end)]
    if any(v != end and out[v] == 0 for v in vertices): return 0
    lap=[]
    for v in vertices:
        lap.append([((out[v]-m[v][v]) if v == w else -m[v][w]) for w in vertices])
    root=vertices.index(end)
    minor=[[lap[i][j] for j in range(len(vertices)) if j != root] for i in range(len(vertices)) if i != root]
    trees=det_bareiss(minor)
    if trees == 0: return 0
    assert trees > 0
    num=trees
    for v in vertices:
        num *= factorial(out[v]-1+int(v == end))
    den=1
    for row in m:
        for multiplicity in row:
            den*=factorial(multiplicity)
    assert num%den==0
    return num//den


def enumerate_words(m, start, end):
    """Bruteforce for small certificates only."""
    m=[row[:] for row in m]
    def go(v, r, path):
        if not r:
            if v==end: yield tuple(path)
            return
        for w in range(len(m)):
            if m[v][w]:
                m[v][w]-=1
                yield from go(w,r-1,path+[w])
                m[v][w]+=1
    return list(go(start, sum(map(sum,m)), [start]))


def unrank(m, start, end, rank):
    n=completion_count(m,start,end)
    if rank<0 or rank>=n: raise ValueError('rank outside population')
    m=[row[:] for row in m]
    cur=start
    word=[cur]
    while any(any(row) for row in m):
        for w in range(len(m)):
            if not m[cur][w]: continue
            m[cur][w]-=1
            c=completion_count(m,w,end)
            if rank < c:
                word.append(w);cur=w;break
            rank-=c;m[cur][w]+=1
        else: raise AssertionError('unrank failed')
    assert cur==end and rank==0
    return tuple(word)


def rank_word(m,start,end,word):
    if word[0] != start or word[-1] != end: raise ValueError('wrong endpoints')
    m=[row[:] for row in m]
    r=0
    for cur,nxt in zip(word,word[1:]):
        for w in range(nxt):
            if m[cur][w]:
                m[cur][w]-=1
                r+=completion_count(m,w,end)
                m[cur][w]+=1
        if not m[cur][nxt]: raise ValueError('edge missing')
        m[cur][nxt]-=1
    if any(any(row) for row in m): raise ValueError('unused edges')
    return r


def run():
    t0=perf_counter(); finite_cases=0; finite_paths=0
    # Mixed multiplicities / open trails as well as Euler circuits.
    for d in (2,3):
        for bits in product(range(2),repeat=d*d):
            m=[list(bits[i*d:(i+1)*d]) for i in range(d)]
            if sum(bits)>8: continue
            for start in range(d):
                for end in range(d):
                    brute=enumerate_words(m,start,end)
                    count=completion_count(m,start,end)
                    assert count==len(brute),(d,bits,start,end,count,len(brute))
                    assert brute==sorted(brute)
                    for r,word in enumerate(brute):
                        assert unrank(m,start,end,r)==word
                        assert rank_word(m,start,end,word)==r
                    finite_cases+=1;finite_paths+=len(brute)
    # Test positive parallel arc multiplicity with closed/open paths.
    multiplicity_cases=0
    for d in (2,):
        for digits in product(range(3),repeat=d*d):
            if sum(digits)>7: continue
            m=[list(digits[i*d:(i+1)*d]) for i in range(d)]
            for start in range(d):
                for end in range(d):
                    brute=enumerate_words(m,start,end)
                    assert len(brute)==completion_count(m,start,end)
                    for r,word in enumerate(brute):
                        assert rank_word(m,start,end,word)==r
                    multiplicity_cases+=1
    print(f'FINITE_EXACT cases={finite_cases} total_paths={finite_paths} parallel_cases={multiplicity_cases}')
    # Local sequential SET(center b -> z), DELETE(right neighbor c) versus the naive sum.
    D='ABCDEFGHIJKL'
    def edges(w): return Counter(zip(w,w[1:]))
    def minus(x,y): return Counter({e:x[e]-y[e] for e in set(x)|set(y) if x[e]!=y[e]})
    nonzero=0
    for b,c,d,z in product(D,repeat=4):
        a='A'
        before=a+b+c+d
        set_only=a+z+c+d
        del_only=a+b+d
        joint=a+z+d
        exact=minus(edges(joint),edges(before))
        delta_set=minus(edges(set_only),edges(before))
        delta_del=minus(edges(del_only),edges(before))
        independent=delta_set.copy();independent.update(delta_del)
        residual=minus(exact,independent)
        formula=Counter()
        for edge,coeff in [((b,c),1),((z,d),1),((z,c),-1),((b,d),-1)]:
            formula[edge]+=coeff
        assert residual==minus(formula,Counter())
        if residual: nonzero+=1
        # Deleting the just-edited center cancels the edit at terminal readout.
        assert a+z+c+d != '' and (a+z+c+d)[:1]+(a+z+c+d)[2:]==a+c+d
    print(f'SET_DELETE_INTERACTION 12^4=20736 exact_cases nonzero={nonzero}')
    d=12
    m=[[1]*d for _ in range(d)]
    expected=(d**(d-2))*factorial(d)*factorial(d-1)**(d-1)
    n=completion_count(m,0,0)
    assert n==expected
    print(f'DENSE_X6 directions={d} directed_edge_types={d*d} edges={d*d} population={n} decimal_digits={len(str(n))}')
    probes=[0,1,2,n//2,n-3,n-2,n-1]
    probes+= [Random(494).randrange(n),Random(495).randrange(n)]
    for r in probes:
        w=unrank(m,0,0,r)
        assert len(w)==145 and rank_word(m,0,0,w)==r
        assert Counter(zip(w,w[1:]))==Counter({(i,j):1 for i in range(d) for j in range(d)})
    print(f'DENSE_RANK roundtrips={len(probes)} each_word_length=145 bitlen={n.bit_length()}')
    print(f'WALL_TIME_SEC {perf_counter()-t0:.3f}')
    print('ALL_ASSERTIONS_PASSED')
if __name__=='__main__':run()

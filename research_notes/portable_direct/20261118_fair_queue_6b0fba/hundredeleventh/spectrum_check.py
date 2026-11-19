"""Verify prime-replacement graph spectra from the integer value window."""
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import exp, gcd, isqrt, log, sqrt

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import LinearOperator, eigsh


def factor_table(x):
    spf = list(range(x + 1))
    for p in range(2, int(sqrt(x)) + 1):
        if spf[p] == p:
            for v in range(p*p, x + 1, p):
                if spf[v] == v:
                    spf[v] = p
    factors = [()] * (x+1)
    primes = []
    for v in range(2, x+1):
        factors[v] = (spf[v],) + factors[v//spf[v]]
        if v == spf[v]:
            primes.append(v)
    return factors, primes


def inspect(x, k, display, exact=False):
    factors, primes = factor_table(x)
    numbers = [v for v in range(2, x+1) if len(factors[v]) == k]
    kernels = sorted({n//p for n in numbers for p in factors[n]})
    rank = {g:i for i,g in enumerate(kernels)}
    row, col = [], []
    for i,n in enumerate(numbers):
        for p in sorted(set(factors[n])):
            row.append(i)
            col.append(rank[n//p])
    incidence = csr_matrix((np.ones(len(col), dtype=int), (row, col)),
                           shape=(len(numbers),len(kernels)))
    multiplicity = np.asarray(incidence.sum(axis=1)).ravel()
    size = np.asarray(incidence.sum(axis=0)).ravel()
    assert [int(v) for v in size] == [int(np.searchsorted(primes,x//g,side='right')) for g in kernels]
    def adjacency(v):
        return incidence @ (incidence.T @ v) - multiplicity*v
    degree = adjacency(np.ones(len(numbers),dtype=int))
    exact_edge_twice = sum(int(m)*(int(m)-1) for m in size)
    assert int(degree.sum()) == exact_edge_twice
    exact_spectrum = None
    if exact:
        import sympy as sy
        dense = incidence.toarray()
        direct = np.zeros((len(numbers),len(numbers)),dtype=int)
        for i,j in combinations(range(len(numbers)),2):
            if len(factors[gcd(numbers[i],numbers[j])]) == k-1:
                direct[i,j] = direct[j,i] = 1
        assert np.array_equal(direct,dense@dense.T-np.diag(multiplicity))
        # Sylvester's determinant identity from the two sides, in exact rationals.
        exact_spectrum = np.linalg.eigvalsh(direct.astype(float))
        dag = sy.Matrix(direct)
        rr = sy.Matrix(dense)
        for point in [1,3,13]:
            diag = sy.diag(*[int(point+m) for m in multiplicity])
            assert ((point*sy.eye(len(numbers))-dag).det() ==
                    diag.det()*(sy.eye(len(kernels))-rr.T*diag.inv()*rr).det())
    operator = LinearOperator((len(numbers),len(numbers)),matvec=adjacency,dtype=float)
    ncomp = min(len(numbers)-1, display+2)
    vals, vecs = eigsh(operator, k=ncomp, which='LA', tol=1e-13,
                        v0=np.arange(1,len(numbers)+1,dtype=float))
    vals, vecs = vals[::-1], vecs[:,::-1]
    modes = []
    for j in range(min(display,len(kernels))):
        g = kernels[j]
        indicator = incidence[:,j].toarray().ravel()
        neighbors = adjacency(indicator)
        assert np.all(neighbors[indicator==1] == size[j]-1)
        outside = neighbors[indicator==0]
        assert np.all((0<=outside)&(outside<=2))
        residual_energy_numerator = int(outside@outside)
        # Classify every outside vertex with a neighbor via a unique r | g
        # and the two prime factors left after removing g/r.
        head = defaultdict(Counter)
        for n,count,inside in zip(numbers,neighbors,indicator):
            if inside or not count:
                continue
            match = [r for r in set(factors[g]) if n%(g//r)==0]
            assert len(match)==1
            r = match[0]
            pair = factors[n//(g//r)]
            assert len(pair)==2 and r not in pair
            assert count==len([p for p in set(pair) if p<=x//g])
            head[r][int(count)] += 1
        assert residual_energy_numerator == sum(v[1]+4*v[2] for v in head.values())
        residue = np.linalg.norm(adjacency(vecs[:,j])-vals[j]*vecs[:,j])
        assert residue < 1e-7
        oriented = vecs[:,j] * (1 if indicator@vecs[:,j] > 0 else -1)
        cross = {}
        for h in kernels[:display]:
            if h == g:
                continue
            ratio = g/h
            common = gcd(h,g)
            near = len(factors[h//common]) == len(factors[g//common]) == 1
            limit = (1+min(1,ratio))/(sqrt(ratio)*(1-ratio)) if near else 0
            other = incidence[:,rank[h]].toarray().ravel()
            strength = size[j]*float(other@oriented)/sqrt(size[rank[h]])
            cross[str(h)]=[round(strength,6),round(limit,6)]
        modes.append(dict(cross_readout_and_limit=cross,kernel=g,clique=int(size[j]),eigenvalue=round(float(vals[j]),7),
                          overlap_squared=round(float((indicator@vecs[:,j])**2/size[j]),8),
                          scaled_shift=round(float((vals[j]+1-size[j])*size[j]/log(log(x))),6),
                          limiting_scaled_shift=4*sum(set(factors[g])),
                          squared_residual_numerator=residual_energy_numerator,
                          outside_counts={str(r):[v[1],v[2]] for r,v in sorted(head.items())}))
    test_moments = {}
    for kind, precision, target in [('trace',0,2*k), ('boundary',1/log(x),1+(2*k-1)/exp(1)),
                                    ('intermediate',1/sqrt(log(x)),0.5**(k-1))]:
        prime_count = len(primes)
        mass = np.sum(size*(size/prime_count)**precision)/len(numbers)
        row = dict(positive_clique_proxy=round(float(mass),7), combined_limit=round(target,7))
        if exact_spectrum is not None:
            positive = np.maximum(exact_spectrum,0)
            row['positive_matrix_moment']=round(float(np.sum(positive*(positive/prime_count)**precision)/len(numbers)),7)
            row['full_matrix_moment']=round(float(np.sum(abs(exact_spectrum)*(abs(exact_spectrum)/prime_count)**precision)/len(numbers)),7)
        test_moments[kind]=row
    return dict(moment_examples=test_moments,X=x,k=k,vertices=len(numbers),number_of_kernels=len(kernels),edges=exact_edge_twice//2,
                modes=modes,all_pairs_and_exact_determinants_checked=exact)


def main():
    records=[inspect(36,2,2,True),inspect(60,3,2,True)]
    for x,k,count in [(1000,2,3),(20000,2,3),(100000,2,3),(10000,3,4),(60000,3,4),(24000,4,3)]:
        records.append(inspect(x,k,count))
    # Pure integer interval for the absolutely convergent constant in the angle loss.
    cutoff, unit = 200000, 10**11
    sieve = bytearray([1]) * (cutoff+1)
    sieve[:2] = bytes(2)
    for t in range(2, isqrt(cutoff)+1):
        if sieve[t]:
            sieve[t*t::t] = bytes((cutoff-t*t)//t+1)
    angles = {}
    for prime in (2,3,5):
        lower = upper = 0
        for q, on in enumerate(sieve):
            if not on or q == prime:
                continue
            a = (prime+q)**2 if q < prime else 4*prime*prime
            b = (prime-q)**2
            lower += a*unit//b
            upper += (a*unit+b-1)//b
        upper += (4*prime*prime*unit+cutoff-prime-1)//(cutoff-prime)
        angles[str(prime)] = [lower,upper,unit]
    return dict(records=records, angle_constant_rational_intervals=angles,
                convention="simple undirected graph, distinct integer vertices, gcd loses exactly one prime factor",
                large_window_eigenvalues="sparse symmetric eigensolver, displayed values rounded; edge and residual counts exact")


if __name__ == '__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))

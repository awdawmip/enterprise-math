"""Integer checks of joint vertical continuations in the R004 column model.

Run python3 merge_check.py to regenerate merge_checked.json (standard library).
"""
from collections import Counter
from fractions import Fraction
from functools import cache
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from math import comb, gcd, perm
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


@cache
def gaussian(p, n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return gaussian(p, n-1, k-1) + p**k * gaussian(p, n-1, k)


def profile(group_type, j):
    return sum(max(0, a-j) for a in group_type)


def type_from_profile(values):
    return tuple(j for j in range(1, len(values)-1)
                 for _ in range(values[j-1]-2*values[j]+values[j+1]))


def logarithm(n, p):
    h = 0
    while n > 1:
        assert n % p == 0
        n //= p
        h += 1
    return h


def trim(coeff):
    while len(coeff) > 1 and not coeff[-1]:
        coeff.pop()
    return tuple(coeff)


def generating_factor(p, rank):
    coeff = [1]
    for j in range(rank):
        coeff = [v-p**j*u for v, u in zip(coeff+[0], [0]+coeff)]
    return coeff


@cache
def subgroup_zeta(p, typ):
    """Count subgroups by index using the classical finite p-group type formula."""
    heights = [sum(a >= j for a in typ) for j in range(1, max(typ, default=0)+1)]
    coefficients = [0]*(sum(typ)+1)
    for widths in product(*(range(a+1) for a in heights)):
        if any(a < b for a, b in zip(widths, widths[1:])):
            continue
        count = 1
        for j, (a, b) in enumerate(zip(heights, widths)):
            following = widths[j+1] if j+1 < len(widths) else 0
            count *= p**(following*(a-b))*gaussian(p, a-following, b-following)
        coefficients[sum(typ)-sum(widths)] += count
    return coefficients


def compressed(p, G, A, B):
    """Use only the three Smith types via filtered-subspace counts."""
    K = max(G, default=0)
    delta = [profile(A,j)-profile(B,j) for j in range(K+2)]
    k = len(G)-delta[0]
    multiplicities = [a-b for a,b in zip(delta,delta[1:])]
    coeff = [0]*(sum(G)+1)
    for amounts in product(*(range(a+1) for a in multiplicities)):
        depths = [sum(amounts[j:]) for j in range(K+2)]
        u = depths[0]
        factor = (-1)**u * p**(k*u + u*(u-1)//2)
        for j, (n, h) in enumerate(zip(multiplicities, amounts)):
            factor *= gaussian(p,n,h)*p**(h*(delta[j+1]-depths[j+1]))
        quotient = type_from_profile([profile(A,j)-depths[j] for j in range(K+2)])
        for j, value in enumerate(subgroup_zeta(p,quotient)):
            coeff[j+u] += factor*value
    result = [0]*(len(coeff)+k)
    for i, a in enumerate(coeff):
        for j, b in enumerate(generating_factor(p,k)):
            result[i+j] += a*b
    return trim(result)


def evaluate(coeff,p,t):
    return sum(Fraction(a,p**(i*t)) for i,a in enumerate(coeff))


def without_replacement(coeff,p,n,t,used=0):
    stirling = [1]
    for i in range(t):
        stirling = [a-(i+used)*b for a,b in zip([0]+stirling,stirling+[0])]
    distinct = sum(s * n**j * evaluate(coeff,p,j) for j,s in enumerate(stirling))
    return distinct / perm(n-used,t)


class FiniteGroup:
    def __init__(self,p,typ):
        self.p = p
        self.typ = typ
        self.moduli = tuple(p**e for e in typ)
        self.points = list(product(*(range(m) for m in self.moduli)))
        self.indices = {v:i for i,v in enumerate(self.points)}
        self.sum = [[self.indices[tuple((x+y)%m for x,y,m in zip(a,b,self.moduli))]
                    for b in self.points] for a in self.points]
        self.zero = frozenset({0})
        self.cycles = [self.cyclic(x) for x in range(len(self.points))]
        self.socle = frozenset(i for i,v in enumerate(self.points)
                              if all(p*x%m==0 for x,m in zip(v,self.moduli)))
        self.groups = [self.zero]
        seen = {self.zero}
        for h in self.groups:
            for x in range(len(self.points)):
                if x in h:
                    continue
                large = self.plus(h,self.cycles[x])
                if large not in seen:
                    seen.add(large)
                    self.groups.append(large)

    def cyclic(self,x):
        result = {0}
        y = x
        while y not in result:
            result.add(y)
            y = self.sum[y][x]
        return frozenset(result)

    def plus(self,h,j):
        return frozenset(self.sum[x][y] for x in h for y in j)

    def quotient(self,h):
        values = []
        for j in range(max(self.typ,default=0)+2):
            images = {self.indices[tuple(self.p**j*x%m for x,m in zip(v,self.moduli))]
                      for v in self.points}
            values.append(logarithm(len(self.plus(images,h))//len(h),self.p))
        return type_from_profile(values)

    def direct_coeff(self,I):
        coeff = [0]*(sum(self.typ)+1)
        for H in self.groups:
            if I<=H:
                idx = logarithm(len(self.points)//len(H),self.p)
                rank = logarithm(len(H & self.socle),self.p)
                for j,a in enumerate(generating_factor(self.p, rank)):
                    coeff[idx+j] += a
        return trim(coeff)


def group_checks():
    records = []
    for p,G in [(2,(1,1,1)),(2,(1,2)),(2,(2,2)),(2,(1,2,3)),(3,(1,2)),(5,(1,1))]:
        group = FiniteGroup(p,G)
        laws = set()
        subset_checks = 0
        distinct_subsets = []
        if len(group.points)<=8:
            for t in range(len(group.points)+1):
                generated = []
                for chosen in combinations(range(len(group.points)),t):
                    h0 = group.zero
                    for x in chosen:
                        h0=group.plus(h0,group.cycles[x])
                    generated.append(h0)
                distinct_subsets.append(generated)
        for I in group.groups:
            A = group.quotient(I)
            B = group.quotient(group.plus(I,group.socle))
            law = group.direct_coeff(I)
            assert law == compressed(p,G,A,B)
            laws.add(law)
            for t, generated in enumerate(distinct_subsets):
                assert without_replacement(law,p,len(group.points),t)==Fraction(
                    sum(I<=h0 for h0 in generated),len(generated))
                subset_checks+=len(generated)
            if len(I)==1:
                assert law==(1,)
                continue
            h = min(min((logarithm(gcd(x,m),p)
                         for x,m in zip(group.points[y],group.moduli) if x),default=max(G))
                    for y in I)
            m = h+1
            lead = (p**sum(min(m,a) for a in G)-p**sum(min(m,a) for a in A))//(p**m-p**(m-1))
            assert next(j for j in range(1,len(law)) if law[j])==m
            assert law[m]==-lead
            n = len(group.points)
            cap = n//p**m
            for t,generated in enumerate(distinct_subsets):
                fails = sum(not I<=h0 for h0 in generated)
                if cap//p<t<=cap:
                    assert fails==lead*comb(cap,t)
                if t>cap:
                    assert fails==0
            k = logarithm(len(I & group.socle),p)
            assert evaluate(law,p,k)>0 and evaluate(law,p,k-1)==0
        records.append(dict(prime=p,ambient=G,all_subgroups=len(group.groups),distinct_time_laws=len(laws), without_replacement_subset_checks=subset_checks))
    return records


def prefix_check():
    g = FiniteGroup(2,(2,1))
    n = len(g.points)
    cache_laws = {}
    cases = 0
    for s in range(3):
        for prefix in combinations(range(n),s):
            H = g.zero
            for y in prefix:
                H = g.plus(H,g.cycles[y])
            pullback = frozenset(x for x in range(n) if g.sum[x][x] in H)
            left = sorted(set(range(n))-set(prefix))
            for t in range(len(left)+1):
                hist = Counter()
                for suffix in combinations(left,t):
                    J = H
                    for y in suffix:
                        J = g.plus(J,g.cycles[y])
                    hist[J] += 1
                for I in g.groups:
                    if (I,H) not in cache_laws:
                        cache_laws[I,H] = compressed(2,g.quotient(H),
                            g.quotient(g.plus(I,H)),g.quotient(g.plus(I,pullback)))
                    observed = Fraction(sum(count for J,count in hist.items() if I<=J),comb(n-s,t))
                    assert observed==without_replacement(cache_laws[I,H],2,n,t,used=s)
                    cases += 1
    return dict(p=2,ambient=[2,1],prefix_sizes=[0,1,2],
                distinct_specific_prefixes=37, exact_conditional_cdf_comparisons=cases)


def actual_columns():
    """Check actual A_H,(A_H;B_H) Smith increments over the original free rings."""
    filename = HERE.parent/'seventyfourth'/'probes_check.py'
    spec = spec_from_file_location('r004_raw',filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = []
    for p,ring_h,typ,atoms,times in [
        (2,2,(1,2),[(1,0)],[0,1,2,3]),
        (2,4,(1,2),[(0,2)],[0,1,2,3]),
        (3,2,(1,2),[(0,3)],[0,1,2]),
        (5,3,(1,1),[(1,0)],[0,1,2]),
        (2,3,(3,2,1),[(2,0,0),(0,0,1)],[0,1,2]),
        (2,3,(3,2,1),[(0,1,0),(4,0,0)],[0,1,2]),
    ]:
        mod = p**ring_h
        r,d = len(atoms),len(typ)
        zero_source = (0,)*r
        zero_target = (0,)*d
        generator = [tuple(int(k==j) for k in range(r)) for j in range(r)]
        background = [zero_source+tuple(p**a%mod if k==j else 0 for k in range(d))
                      for j,a in enumerate(typ) if a<ring_h]
        one = [u+zero_target for u in generator]+background
        extra = [u+z for u,z in zip(generator,atoms)]
        # Both histories and their join have full, identical control projection.
        def delta(cols):
            matrix = list(zip(*cols))
            return module.log_span(matrix,p,ring_h)-module.log_span(matrix[:r],p,ring_h)
        group = FiniteGroup(p,typ)
        I = group.zero
        for a in atoms:
            I=group.plus(I,group.cycles[group.indices[tuple(a)]])
        expected = compressed(p,typ,group.quotient(I),group.quotient(group.plus(I,group.socle)))
        res=[]
        for t in times:
            total=len(group.points)**t
            good=0
            good_distinct=0
            for word in product(group.points,repeat=t):
                post=[zero_source+x for x in word]
                merged=delta(one+post)==delta(one+extra+post)
                good+=merged
                good_distinct+=merged and len(set(word))==t
            assert Fraction(good,total)==evaluate(expected,p,t)
            total_distinct=perm(len(group.points),t)
            assert Fraction(good_distinct,total_distinct)==without_replacement(expected,p,len(group.points),t)
            res.append(dict(t=t,merged=good,total=total,merged_distinct=good_distinct,total_distinct=total_distinct))
        rows.append(dict(p=p,ring_exponent=ring_h,ambient=typ,difference_generators=atoms,cdf_polynomial=expected,raw_histories=res))
    return rows


def main():
    report=dict(model='Shared ordered vertical-column words, uniformly counted. No source prior assumed.',
                script_requirements='Python standard library; original wave 74 probes_check.py, log_span.',
                all_subgroup_cross_checks=group_checks(), named_distinct_prefixes=prefix_check(),
                original_delta_checks=actual_columns())
    output = HERE/'merge_checked.json'
    output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')


if __name__=='__main__':
    main()

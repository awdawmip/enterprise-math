"""Integer return counts, normal contractions, and the two-state congruence filter."""
from collections import Counter
from fractions import Fraction as Q
from functools import cache
from hashlib import sha256
from itertools import product
from math import comb, exp, pi
import json


@cache
def equal_counts(size, plus, minus):
    if (plus-minus)%size:
        return 0
    if size==1:
        return 1
    k = (plus-minus)//size
    # Assign the time labels visiting the first axis, then fill the other axes.
    return sum(comb(plus,j+k)*comb(minus,j)*equal_counts(size-1,plus-j-k,minus-j)
               for j in range(max(0,-k),min(minus,plus-k)+1))


@cache
def ways(dim, plus, minus):
    if dim==5:
        return equal_counts(6,plus,minus)
    if (plus-minus)%3:
        return 0
    return sum(comb(plus,i)*comb(minus,j)*equal_counts(3,i,j)
               *equal_counts(3,plus-i,minus-j)
               for i in range(plus+1) for j in range((i-plus+minus)%3,minus+1,3))


def direct_words():
    cases = 0
    for n in range(7):
        for p in range(n+1):
            hits = Counter()
            for axes in product(range(6), repeat=n):
                x = [0]*6
                for j,i in enumerate(axes):
                    x[i] += 1 if j<p else -1
                if len(set(x))==1:
                    hits[5] += 1
                if len(set(x[::2]))==1 and len(set(x[1::2]))==1:
                    hits[4] += 1
            for dim in (4,5):
                assert hits[dim] == ways(dim,p,n-p)
                cases += 1
    return cases


def cumulants(group_size):
    gram = [[6*(i==j)-(6//group_size)*(i//group_size==j//group_size)
             for j in range(6)] for i in range(6)]

    @cache
    def wick(powers):
        if not any(powers):
            return 1
        remaining = list(powers)
        i = next(i for i,k in enumerate(remaining) if k)
        remaining[i] -= 1
        total = 0
        for j in range(6):
            if remaining[j] and gram[i][j]:
                factor = remaining[j]*gram[i][j]
                remaining[j] -= 1
                total += factor*wick(tuple(remaining))
                remaining[j] += 1
        return total

    @cache
    def moment(*degrees):
        total = 0
        for axes in product(range(6), repeat=len(degrees)):
            powers = [0]*6
            for i,k in zip(axes,degrees):
                powers[i] += k
            total += wick(tuple(powers))
        return Q(total,6**len(degrees))

    m = moment
    k4, k33 = m(4)-3*m(2,2), m(3,3)
    k6 = m(6)-15*m(4,2)-10*m(3,3)+30*m(2,2,2)
    k44, k35 = m(4,4)-6*m(4,2,2)+9*m(2,2,2,2), m(3,5)-10*m(3,3,2)
    k433, k3333 = m(4,3,3)-3*m(2,2,3,3), m(3,3,3,3)
    first = [k4/24, -k33/72]
    second = [-k6/720+k44/1152, k35/720-k433/1728, k3333/31104]
    return first,second


def probabilities(n, rho):
    # Exact dynamic recurrence on sign total and final sign, with a common denominator.
    stay = (1+rho)/2
    v,den = stay.numerator,stay.denominator
    rows = {(1,1):1,(-1,-1):1}
    for _ in range(1,n):
        new = Counter()
        for (s,last),w in rows.items():
            new[s+last,last] += v*w
            new[s-last,-last] += (den-v)*w
        rows = new
    masses = Counter()
    for (s,_),w in rows.items():
        masses[s] += w
    z = 2*den**(n-1)
    prob = Q(sum(w for s,w in masses.items() if s%3==0),z)
    u,w = Q(1),Q(-1,2)
    for _ in range(1,n):
        u,w = w, -(1+rho)*w/2-rho*u
    assert prob==(1+2*w)/3
    return prob,masses,z


def run():
    direct = direct_words()
    # In a single three-axis group the unsigned triangular walk polynomial
    # is (1+x+xy)(1+x^-1+(xy)^-1)-3. Use its constant term separately.
    trinomial_collision = [sum(comb(j,i)**2 * comb(2*i,i) for i in range(j+1))
                           for j in range(129)]
    group_returns = [sum(comb(m,j)*(-3)**(m-j)*trinomial_collision[j]
                         for j in range(m+1)) for m in range(129)]
    stored = []
    for n in range(1,129):
        hits = sum(comb(n,p)*ways(4,p,n-p) for p in range(n+1))
        independent = sum(comb(n,i)*group_returns[i]*group_returns[n-i] for i in range(n+1))
        assert hits == independent
        stored.append(str(Q(hits,12**n)))
    old_steps = (1,2,3,4,6,8,12,16,24,32,48,64,96,128)
    digest = sha256(('\n'.join(stored[n-1] for n in old_steps)+'\n').encode()).hexdigest()
    assert digest=='5b0835054cce814727fedd4a10879eeef753616c29ca17f66c8a2ca8967ee1d9'
    rows = []
    polys = {d:cumulants(g) for d,g in ((4,3),(5,6))}
    assert polys[5] == ([Q(-5,4),Q(-5,3)],[Q(105,32),Q(-95,12),Q(80,9)])
    assert polys[4] == ([Q(-1),Q(-2,3)],[Q(4,3),Q(-4,3),Q(11,9)])
    for n in (24,60,120,180):
        for s in (0,6,n//2,n):
            p = (n+s)//2
            for d,vol in ((4,36),(5,216)):
                val = Q(ways(d,p,n-p),6**n)
                t = Q(s,n)**2
                f,g = polys[d]
                prediction = 1+(f[0]+t*f[1])/n+(g[0]+t*g[1]+t*t*g[2])/n**2
                relative = float(val)*(2*pi*n)**(d/2)/vol
                rows.append([n,s,d,str(val),format(relative,'.12g'),
                             format(n**3*(relative-float(prediction)),'.8g')])
    markov = []
    for rho in (Q(-1),Q(-1,2),Q(0),Q(1,2),Q(3,4),Q(1)):
        for n in (23,24,60):
            filt,dist,den = probabilities(n,rho)
            p_return = [Q(sum(w*ways(d,(n+s)//2,(n-s)//2) for s,w in dist.items()),
                          den*6**n) for d in (4,5)]
            markov.append([n,str(rho),str(filt),*map(str,p_return)])
    endpoints = []
    for n in (59,60,61,120,121):
        for lam in (1,3):
            for mode in ('persistent','alternating'):
                rho = 1-Q(2*lam,n)
                if mode=='alternating':
                    rho = -rho
                    approx = (1+0.5*exp(-1.5*lam)+1.5*(-1)**n*exp(-0.5*lam))/3
                else:
                    approx = (1+exp(-lam)*(2 if n%3==0 else -1))/3
                filt,_,_ = probabilities(n,rho)
                endpoints.append([n,lam,mode,format(float(filt),'.12g'),format(approx,'.12g')])
    return {'axis_word_comparisons':direct,'independent_return_counts':128,'published_checkpoints':old_steps,'published_probability_digest':digest,
            'old_n128_H4_probability':stored[-1],
            'edgeworth_polynomials_in_squared_sign_bias':
            {d:[[str(z) for z in row] for row in pair] for d,pair in polys.items()},
            'conditional_rows_n_s_dim_exact_scaled_n3_error':rows,
            'markov_n_rho_mod3_H4_H5':markov,'endpoint_congruence_exact_vs_limit':endpoints}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))

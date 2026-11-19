"""Independent integer coefficient and original cosine checks for prefix bins."""
from fractions import Fraction as F
from math import ceil, comb, cos, factorial, floor, isqrt, log, pi
from hashlib import sha256
from array import array
from mpmath import iv
from collections import Counter, defaultdict
import json


def factors(n):
    out=[]
    p=2
    while p*p<=n:
        while n%p==0:
            out.append(p)
            n//=p
        p+=1
    if n>1:
        out.append(n)
    return out


def run(T,y,q):
    grid=[F(1)]
    g=F(q+1,q)
    while grid[-1]<=T:
        grid.append(grid[-1]*g)
    H=len(grid)-2
    fact={n:factors(n) for n in range(1,T+1)}
    P=[n for n,f in fact.items() if n>y and len(f)==1]
    bins={p:next(i for i,x in enumerate(grid) if x>=p) for p in P}
    K=max(len([p for p in v if p>y]) for v in fact.values())
    S=[]
    for gx in grid[:-1]:
        X=T/gx
        S.append(sum(cos(pi*float(n/X)/2) for n,fs in fact.items()
                     if n<=X and len(set(fs))==len(fs)))
    keys_by_bin=defaultdict(list)
    for p in P:
        keys_by_bin[bins[p]].append(p)
    # Coordinate key is (rounded log size, degree in binomial variable).
    state=Counter({(0,0):1})
    for h,ps in keys_by_bin.items():
        # Coefficients of (1+X^h)^(-len(ps)).
        new=Counter()
        for (d,j),v in state.items():
            for k in range((H-d)//h+1):
                new[d+k*h,j]+=v*(-1)**k*comb(len(ps)+k-1,k)
        state=Counter({key:v for key,v in new.items() if v})
    batch_reads={}
    fingerprints={}
    def fingerprint(rows):
        return tuple(sorted((h,j,v) for (h,j),v in rows.items() if v))
    def collect(state):
        return [sum(S[d]*v for (d,i),v in state.items() if i==j) for j in range(K+1)]
    batch_reads[0]=collect(state)
    fingerprints[0]=fingerprint(state)
    nseen=0
    for h,ps in keys_by_bin.items():
        shifts=[]
        for k in range(K+1):
            tmp=Counter()
            for (d,j),v in state.items():
                if d+k*h<=H:
                    for a in range(k+1):
                        tmp[d+k*h,j+a]+=v*comb(k,a)
            shifts.append(tmp)
        cols=[collect(s) for s in shifts]
        for a in range(1,len(ps)+1):
            coefficient_oracle=Counter()
            for k,shift in enumerate(shifts):
                if k<=a:
                    for key,value in shift.items():
                        coefficient_oracle[key]+=comb(a,k)*value
            fingerprints[nseen+a]=fingerprint(coefficient_oracle)
            batch_reads[nseen+a]=[sum(comb(a,k)*co[j] for k,co in enumerate(cols)
                                      if k<=a) for j in range(K+1)]
        nseen+=len(ps)
        new=Counter()
        for k,s in enumerate(shifts):
            if k<=len(ps):
                for key,v in s.items():
                    new[key]+=comb(len(ps),k)*v
        state=Counter({key:v for key,v in new.items() if v})
    by_prime={p:i for i,p in enumerate(P,1)}
    errors=[0.0]*(K+1)
    parity_error=0.0
    bound=pi/4*(T+1)*K*log(1+1/q)
    for pref,values in batch_reads.items():
        actual=[0.]*(K+1)
        oracle=Counter()
        for d,f in fact.items():
            if all(p>y for p in f):
                a=sum(by_prime[p]<=pref for p in set(f))
                degree=sum(bins[p] for p in f)
                if degree<=H:
                    oracle[degree,a]+=(-1)**(len(f)-a)
            rough=[p for p in f if p>y]
            if len(f)==len(set(f)) and all(by_prime[p]<=pref for p in rough):
                for j in range(len(rough)+1):
                    actual[j]+=comb(len(rough),j)*cos(pi*d/(2*T))
        assert fingerprints[pref]==fingerprint(oracle)
        assert all(abs(a-b)<1e-7 for a,b in zip(collect(oracle),values))
        for j in range(K+1):
            errors[j]=max(errors[j],abs(values[j]-actual[j]))
        parity_error=max(parity_error,abs(sum((-2)**j*(values[j]-actual[j]) for j in range(K+1))))
    assert max(errors)<=2**K*bound and parity_error<=3**K*bound
    return dict(T=T,y=y,q=q,K=K,grid_last=H,prime_bins=len(keys_by_bin),checked_prefixes=len(batch_reads),
                max_abs_moment_errors=[round(z,7) for z in errors],parity_error=round(parity_error,7),
                analytic_bounds=[round(2**K*bound,6),round(3**K*bound,6)])



iv.dps=32

def sieve(n):
    flag=bytearray(b'\x01')*(n+1)
    flag[0:2]=bytes(2)
    for p in range(2,isqrt(n)+1):
        if flag[p]: flag[p*p::p]=bytes((n-p*p)//p+1)
    return flag

def enclosure(x):
    return [(floor(float(x.a)*10**8)-1)/10**8,(ceil(float(x.b)*10**8)+1)/10**8]

def bracket():
    N=8000
    prime=sieve(N)
    zv=iv.mpf(0); zdd=iv.mpf(0)
    for p in range(2,N+1):
        if prime[p]:
            lp=iv.log(p)
            zv+=lp/(p*p-1)
            zdd+=lp**2*p*p/(p*p-1)**2
    # All integer terms beyond N can be integrated, as log(x)^j/x² decreases.
    lN=iv.log(N)
    zv+=iv.mpf([0,1])*2*(lN+1)/N
    zdd+=iv.mpf([0,1])*2*(lN*lN+2*lN+2)/N
    gamma=sum((1/iv.mpf(i) for i in range(1,N+1)),iv.mpf(0))-lN + iv.mpf([-1,0])/N
    g1=sum((iv.log(i)/i for i in range(1,N+1)),iv.mpf(0))-lN**2/2+iv.mpf([-1,0])*lN/N
    # Normalized moments int w(t)(log t)^k dt / (2/pi); alternating cosine expansion.
    moments=[]
    for k in [1,2]:
        def term(j):
            return (iv.pi/2)**(2*j+1)*(-1)**(j+k)*factorial(k)/(factorial(2*j)*(2*j+1)**(k+1))
        tot=sum((term(j) for j in range(11)),iv.mpf(0))
        moments.append(tot+term(11)*iv.mpf([0,1]))
    K=gamma+2*zv+moments[0]
    M=gamma**2/2+g1+2*zdd-(moments[1]-moments[0]**2)/2
    assert K.a>0 and M.a>0
    return dict(K=enclosure(K),M=enclosure(M),lambda_star=enclosure(K/iv.exp(iv.mpf('0.5'))),
                mu_star=enclosure(M/iv.exp(iv.mpf('0.5'))))


def atan_bounds(z,terms=6):
    s=sum((-1)**j*z**(2*j+1)/(2*j+1) for j in range(terms))
    t=s+(-1)**terms*z**(2*terms+1)/(2*terms+1)
    return min(s,t),max(s,t)
half=F(3141592653589793,2*10**15)
atan_sum=[sum(2*k*atan_bounds(F(a,b))[j] for a,b,k in [(1,21,16),(1,239,3),(3,1042,4)]) for j in (0,1)]
assert max(abs(q-half) for q in atan_sum)<F(1,10**14)
def signed_intervals(T,p):
    sf=bytearray([1])*(T+1)
    P=array('I',[0])*(T+1)
    for t in range(2,T+1):
        if P[t]:continue
        for n in range(t,T+1,t):P[n]=t
        if t*t<=T: sf[t*t::t*t]=bytes(T//(t*t))
    assert P[p]==p and p-1>isqrt(T)
    m=[[0]*7 for _ in range(2)]
    for n in range(1,T+1):
        if not sf[n]:continue
        s0=1 if P[n]<p else -1
        s1= int(P[n]==p)*2
        z=n*n
        a=s0; b=s1
        for j in range(7):
            m[0][j]+=a
            m[1][j]+=b
            a*=z;b*=z
    w=[(-1)**j*(half/T)**(2*j)/factorial(2*j) for j in range(7)]
    a,b=[sum(q*x for q,x in zip(mass,w)) for mass in m]
    err=T*(F(1,10**14)+F(8,5)**14/factorial(14))
    assert a+err<0<a+b-err
    return [[(1000*(z-err)).__floor__(),(1000*(z+err)).__ceil__()] for z in [a,a+b]]

def sum_powers(n, degree):
    # Telescoping (k+1)^(j+1)-k^(j+1) gives all power sums in integers.
    out=[]
    for j in range(degree+1):
        value=(n+1)**(j+1)-1-sum(comb(j+1,v)*out[v] for v in range(j))
        term,rem=divmod(value,j+1)
        assert not rem
        out.append(term)
    return out


def anchor_prefix(T,y,r):
    a,b=half.numerator,half.denominator
    den=factorial(2*r)*(b*T)**(2*r)
    weights=[(-1)**j*a**(2*j)*(b*T)**(2*r-2*j)*(factorial(2*r)//factorial(2*j))
             for j in range(r+1)]
    fact={n:factors(n) for n in range(1,T+1)}
    primes=[n for n,f in fact.items() if n>y and len(f)==1]
    rank={p:i+1 for i,p in enumerate(primes)}
    U=T//primes[0]
    # Only quotient addresses, not a counter per rough divisor.
    addresses={n for n in range(1,isqrt(T)+1) if n<=U}
    addresses.update(T//n for n in range(1,isqrt(T)+1) if T//n<=U)
    stock={}
    counts=[0]*(r+1)
    for s in range(1,U+1):
        fs=fact[s]
        if len(fs)==len(set(fs)) and all(p<=y for p in fs):
            power=1
            for j in range(r+1):
                counts[j]+=power
                power*=s*s
        if s in addresses:
            stock[s]=counts.copy()
    anchor=0
    for d in range(1,isqrt(T)+1):
        fs=fact[d]
        if len(fs)!=len(set(fs)):
            continue
        sums=sum_powers(T//(d*d),2*r)
        anchor+=(-1)**len(fs)*sum(w*d**(4*j)*sums[2*j] for j,w in enumerate(weights))
    K=max(len([p for p in set(fs) if p>y]) for fs in fact.values())
    increments=[[0]*(K+1) for _ in range(len(primes)+1)]
    visited=[]
    def descend(d,upper,largest,depth):
        if d>1:
            visited.append(d)
            power=1
            mass=0
            for w,M in zip(weights,stock[T//d]):
                mass+=w*M*power
                power*=d*d
            for j in range(depth+1):
                increments[largest][j]+=comb(depth,j)*mass
        for index in range(upper):
            p=primes[index]
            if d*p>T:
                break
            descend(d*p,index,largest or index+1,depth+1)
    descend(1,len(primes),0,0)
    population=[0]*(K+1)
    population[0]=anchor-sum(row[0] for row in increments)
    independent=[[0]*(K+1) for _ in increments]
    for n,fs in fact.items():
        if len(fs)!=len(set(fs)):
            continue
        rough=[p for p in fs if p>y]
        i=rank[rough[-1]] if rough else 0
        value=sum(w*n**(2*j) for j,w in enumerate(weights))
        for j in range(len(rough)+1):
            independent[i][j]+=comb(len(rough),j)*value
    direct=[0]*(K+1)
    dg=sha256()
    for inc,obs in zip(increments,independent):
        population=[x+y for x,y in zip(population,inc)]
        direct=[x+y for x,y in zip(direct,obs)]
        assert population==direct
        dg.update((';'.join(str(x) for x in population)+'\n').encode())
    assert len(set(visited))==len(visited)
    assert population[0]==anchor
    return dict(T=T,y=y,Taylor_half_degree=r,largest_smooth_argument=U,
                quotient_addresses=len(stock),nontrivial_divisors=len(visited),
                exact_prefix_vectors=len(increments),scaled_integer_sha256=dg.hexdigest(),
                parity_abs_error_per_T=str(F(1,10**14)+F(8,5)**(2*r+2)/factorial(2*r+2)))

def full_ordered_scan(T):
    scale=1<<32
    pi,radius=2*half,F(2,10**14)
    terms=8
    trunc=F(8,5)**(2*terms+2)/factorial(2*terms+2)
    assert pi/2<F(8,5) and (radius/2+trunc)*scale<1
    # For positive n, integer coefficients evaluated by Horner give exact
    # floor(scale*P_16(pi_approx*n/(2T))). Every error is less than 2 units.
    z=pi/(2*T);a,b=z.numerator,z.denominator; f=factorial(2*terms)
    den=b**(2*terms)*f
    coeff=[scale*(-1)**j*(f//factorial(2*j))*a**(2*j)*b**(2*terms-2*j)
           for j in range(terms+1)]
    primes=bytearray([1])*(T+1);primes[:2]=b'\x00\x00'
    sf=bytearray([1])*(T+1);sf[0]=0
    for p in range(2,isqrt(T)+1):
        if primes[p]:
            primes[p*p::p]=bytes((T-p*p)//p+1)
            sf[p*p::p*p]=bytes(T//(p*p))
    weights=[0]*(T+1)
    for n in range(1,T):
        if sf[n]:
            x=n*n
            v=0
            for c in reversed(coeff):
                v=v*x+c
            weights[n]=v//den
    score=sum(weights); cutoff=None; below=None; near=None; strange=0; nchecked=0
    neg_high=None
    error=2*sum(sf)
    for p in reversed(range(2,T+1)):
        if not primes[p]:continue
        # Before p is removed from the allowed-small primes, this is the score at y=p.
        assert abs(score)>error, (T,p,score,error)
        nchecked+=1
        if near is None or abs(score)<abs(near[1]): near=(p,score)
        if score>0:cutoff=p
        elif neg_high is None: neg_high=p
        if p<=isqrt(T):
            if score>0:strange+=1
            if below is None or score>below[1]: below=(p,score)
        for n in range(p,T+1,p):
            w=weights[n]
            score-=2*w;weights[n]=-w
    return {"T":T,"primes_certified":nchecked,"first_nonnegative_y_ge_2":cutoff,
            "highest_negative_prime":neg_high,"below_sqrt_positive_primes":strange,
            "largest_score_below_sqrt_prime_and_fixed_value":below,
            "nearest_zero_prime_and_fixed_value":near,"error_numerator":error,
            "fixed_point_denominator":scale}


def main():
    anchors=[anchor_prefix(T,3,6) for T in (36,386,1000)]
    grids=[run(T,3,q) for T in (36,386) for q in (8,24,64)]
    crossings={T:dict(first_prime=p,score_brackets_milli=signed_intervals(T,p))
               for T,p in [(10000,317),(100000,1373),(1000000,5647)]}
    scans=[full_ordered_scan(T) for T in crossings]
    assert all(row['first_nonnegative_y_ge_2']==crossings[row['T']]['first_prime'] for row in scans)
    print(json.dumps(dict(all_finite_cutoffs=scans,exact_scale_Taylor=anchors, approximate_log_grid=grids,
                          critical_constants=bracket(), certified_crossings=crossings),indent=2))


if __name__=='__main__':
    main()

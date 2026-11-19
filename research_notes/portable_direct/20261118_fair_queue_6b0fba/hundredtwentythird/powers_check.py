"""Reconstruct the X6 integer cyclic power and all its cyclotomic remainders.

Run python3 powers_check.py from any directory. The two earlier public programs
listed below and Python's standard library suffice.
"""
from collections import Counter, defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from math import gcd
from pathlib import Path
import json

DIR = Path(__file__).resolve().parent


def earlier(directory, filename, module_name):
    spec = spec_from_file_location(module_name, DIR.parent / directory / filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


original = earlier('twentysecond', 'frobenius_check.py', 'x6_original')
observer = earlier('eightyeighth', 'shifts_check.py', 'x6_observer')


def orders(p, n):
    return [original.order(p,d) for d in original.divisors(n)
            for _ in range((sum(gcd(j,d)==1 for j in range(1,d+1)))//original.order(p,d))]


def local_histograms(p,e,c,n):
    ans = Counter({1:1})
    for degree in orders(p,n):
        q = p**degree
        unit_fiber = q if p!=2 else q//2
        fine_units = ((q-1)//gcd(c,q-1)) * q**(p-1)//p
        local = Counter({unit_fiber:fine_units//unit_fiber})
        if e==2 and c==1:
            if p==2:
                local[q]+=1
            else:
                local[1]+=q
        else:
            local[1]+=1
        new = Counter()
        for a,cnt in ans.items():
            for b,num in local.items():
                new[a*b]+=cnt*num
        ans = new
    return ans


def histogram(states,m,expected=None):
    obs = Counter(observer.observed(s,len(s),m) for s in states)
    hist = Counter(obs.values())
    if expected is not None:
        assert hist==expected,(m,hist,expected)
    return {str(k):v for k,v in sorted(hist.items())}


def starting_core(p,e,c,n):
    w=n*p*p
    m=p**e
    r=n*p
    states=set()
    direct=0
    for idx, g in enumerate(product(range(p),repeat=r)):
        if idx%max(1,(p**r)//24)==0:
            f=g+(0,)*(w-r)
            raw=original.power(f,m*c,m,original.naive)
            direct+=1
        # Generate x^{pj} coefficients, in the actual cyclic basis.
        short=original.power(g,(m//p)*c,m)
        s=tuple(short[i//p] if i%p==0 else 0 for i in range(w))
        if idx%max(1,(p**r)//24)==0:
            assert s==raw
            assert original.observed(raw,m)==tuple(
                a for row in observer.observed(s,w,m) for a in row)
        states.add(s)
    expected=local_histograms(p,e,c,n)
    return dict(p=p,e=e,cofactor=c,R=w,local_degrees=orders(p,n),all_reduced_seeds=p**r,
                direct_full_width_schoolbook_checks=direct,distinct_fine_states=len(states),
                cyclotomic_histogram_by_fiber_size=histogram(states,m,expected))


def faithful(N,R,units=False):
    for p,m in observer.factor(N):
        if p!=2 and R%(p*p)==0:
            return False
        if p==2 and R%4==0 and not (R==4 and m>=4 and (units or N!=4)):
            return False
    return True


def is_unit(seed,modulus):
    # A polynomial is a unit iff it is coprime to X^R-1 over each residue field.
    for p,_ in observer.factor(modulus):
        a=tuple([(-1)%p]+[0]*(len(seed)-1)+[1])
        b=[v%p for v in seed]
        while b and not b[-1]:
            b.pop()
        while b:
            a=list(a)
            inv=pow(b[-1],-1,p)
            while len(a)>=len(b):
                k=len(a)-len(b)
                c=a[-1]*inv%p
                for j,h in enumerate(b):
                    a[k+j]=(a[k+j]-c*h)%p
                while a and a[-1]==0:
                    a.pop()
            a,b=b,a
        if len(a)!=1:
            return False
    return True


def full_inputs(N,R):
    all_states=set()
    units=set()
    for f in product(range(N),repeat=R):
        s=original.power(f,N,N)
        all_states.add(s)
        if is_unit(f,N):
            units.add(s)
    a=histogram(all_states,N)
    u=histogram(units,N)
    assert (list(a)==['1'])==faithful(N,R)
    assert (list(u)==['1'])==faithful(N,R,True)
    return dict(N=N,R=R,input_polynomials=N**R,all_fibers=a,unit_fibers=u)


def witness(p,e,c,R,kind):
    m=p**e
    f=[0]*R
    def add(i,v=1):
        f[i%R]=(f[i%R]+v)%m
    expected=[0]*R
    expected[0]=1
    base=[0]*R
    base[0]=1
    if kind=='odd_or_characteristic':
        step=R//(p*p)
        add(0)
        for j in range(p):
            add(j*step)
            expected[p*j*step]=(expected[p*j*step]+p**(e-1)*c)%m
    elif kind=='dyadic_mixed':
        n=R//4
        add(0)
        add(4)
        add(4+n)
        for i in (8,16):
            for j in (0,2*n):
                expected[(i+j)%R]=(expected[(i+j)%R]+2**(e-1))%m
    elif kind=='dyadic_eight':
        step=R//8
        for j in (1,2,3):
            add(j*step)
        for j in range(4):
            expected[2*j*step]=(expected[2*j*step]+2**(e-1))%m
    else:
        assert kind=='zero' and (p,e,c,R)==(2,2,1,4)
        add(0,-1)
        add(1)
        base[0]=0
        expected=[2,0,2,0]
    s=original.power(f,m*c,m)
    assert tuple(expected)==s and s!=tuple(base)
    assert observer.observed(s,R,m)==observer.observed(base,R,m)
    return dict(p=p,e=e,c=c,width=R,case=kind,
                input_sparse=[[i,v] for i,v in enumerate(f) if v],
                output_sparse=[[i,v] for i,v in enumerate(s) if v],
                matching_state='zero' if not base[0] else 'one')


def main():
    cores=[(2,2,1,1),(2,2,3,1),(2,3,1,1),(2,2,1,3),(2,3,3,3),
           (2,5,3,5),(2,3,1,7),(3,2,1,1),(3,2,2,1),(3,3,1,1),
           (3,2,1,2),(3,4,2,2),(5,2,1,1),(5,4,2,1)]
    all_inputs=[(2,4),(2,8),(2,12),(3,4),(3,9),(4,4),(5,4),(6,4),
                (8,4),(9,4),(12,4)]
    examples=[(3,1,2,9,'odd_or_characteristic'),(3,2,1,9,'odd_or_characteristic'),
              (3,7,10,27,'odd_or_characteristic'),(5,4,6,50,'odd_or_characteristic'),
              (2,1,3,12,'odd_or_characteristic'),(2,2,1,4,'zero'),
              (2,2,3,12,'dyadic_mixed'),(2,9,5,20,'dyadic_mixed'),
              (2,2,3,8,'dyadic_eight'),(2,10,9,24,'dyadic_eight')]
    report=dict(scope='Distinct cyclic power states. Classifying p is used for verification, not supplied to a factor finder.',
                local_fiber_histograms=[starting_core(*a) for a in cores],
                all_original_polynomial_inputs=[full_inputs(*a) for a in all_inputs],
                exact_collision_witnesses=[witness(*a) for a in examples])
    (DIR/'powers_checked.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    main()

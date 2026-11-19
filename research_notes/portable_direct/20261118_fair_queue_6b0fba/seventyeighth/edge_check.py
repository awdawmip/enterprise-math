"""Actual count-centred carry on selected shells and an exact-frequency model."""
import argparse
import cmath
import json
import math
from collections import defaultdict
from decimal import Decimal as D, localcontext
from fractions import Fraction
from pathlib import Path


def mangoldt_addresses(limit):
    sieve = bytearray([1])*(limit+1)
    sieve[:2] = bytes(2)
    for p in range(2,math.isqrt(limit)+1):
        if sieve[p]:
            for j in range(p*p,limit+1,p):
                sieve[j]=0
    return sorted((q,p) for p in range(2,limit+1) if sieve[p]
                  for q in powers(p,limit))


def powers(p,limit):
    q=p
    while q<=limit:
        yield q
        q*=p


def step_coefficients(n,addresses):
    ones=sum(2*n//m-2*(n//m) for m in range(1,n+1))
    direct=defaultdict(int)
    factorial=defaultdict(int)
    for q,p in addresses:
        if q>2*n:
            break
        bit=2*n//q-2*(n//q)
        if q<=n:
            direct[p]+=n*bit-ones
        factorial[p]+=n*bit-n+(n-ones)*(q<=n)
    assert {p:c for p,c in direct.items() if c}=={p:c for p,c in factorial.items() if c}
    return direct


def original_checks():
    addresses=mangoldt_addresses(4096)
    out=[]
    with localcontext() as ctx:
        ctx.prec=48
        logprime={p:D(p).ln() for _,p in addresses}
        def display(x):
            return format(x,'.16f')
        for N in (16,64,256,1024):
            values=[]
            for n in range(N,2*N):
                coeff=step_coefficients(n,addresses)
                J=sum(c*logprime[p] for p,c in coeff.items())/D(n)
                values.append((D(n),J))
            W=sum((j/n)**2 for n,j in values)
            H=sum(j*j/(n*n*n.sqrt()) for n,j in values)
            raw=W/D(N).sqrt()
            assert H<raw<D(2).sqrt()*H
            # Integral of e^u on each [log n,log(n+1)] matches its exact step width 1.
            check=sum((j/n)**2*(n/D(N)).sqrt()/n.sqrt() for n,j in values)
            assert abs(check-raw)<D('1e-45')
            signed=sum(j/(n*n.sqrt().sqrt()**3) for n,j in values)
            out.append(dict(N=N, W=display(W), test_theta='3/4', critical_weighted=display(H),
                            normalized_original=display(raw), raw_over_critical=display(raw/H),
                            signed_partial_sum_frequency_zero=display(signed)))
    return out


L=math.log(2)
A=2-2*L


def window(lam):
    return L if lam==0 else (cmath.exp(lam*L)-1)/lam


def edge_model():
    theta=Fraction(3,4)
    d=float(2*theta-1)
    # The frequencies are in turns per dyadic window. They are artificial.
    specs=[(theta,Fraction(1),1),(theta,Fraction(2),2),(theta,Fraction(3,2),1),
           (Fraction(1,2),Fraction(5,4),3)]
    rows=[]
    for beta,turns,multiplicity in specs:
        for sign in (1,-1):
            f=sign*turns
            rho=float(beta)+1j*float(f)*2*math.pi/L
            c=multiplicity*(cmath.exp(rho*L)-A)/rho
            rows.append((beta,f,c))
    edge=[row for row in rows if row[0]==theta]

    def energy(k,items,tilt):
        value=0j
        for beta,f,c in items:
            for gamma,g,b in items:
                alpha=float(beta+gamma-2*theta)
                freq=float(f-g)
                phase=cmath.exp(2j*math.pi*float((f-g)*k%1))
                factor=phase*2**(alpha*k)*c*b.conjugate()
                value+=factor*window(alpha+tilt+2j*math.pi*freq/L)
        assert abs(value.imag)<1e-12
        return value.real

    def mean(tilt):
        return sum(c*b.conjugate()*window(tilt+2j*math.pi*float(f-g)/L)
                   for _,f,c in edge for _,g,b in edge if (f-g).denominator==1).real

    flat=L*sum(abs(c)**2 for _,f,c in edge)
    raw=mean(d)
    assert abs(mean(0)-flat)<1e-13 and flat<raw<2**d*flat
    diagonal=window(d).real*sum(abs(c)**2 for _,f,c in edge)
    assert abs(raw-diagonal)>1e-6
    for tilt,want in ((0,flat),(d,raw)):
        assert abs(sum(energy(k,edge,tilt) for k in range(4))/4-want)<1e-13
    comparisons=[]
    for k in (0,8,24,96):
        # Independent direct quadrature of the original finite exponential field.
        steps=1024
        def square(u):
            val=sum(c*cmath.exp((float(beta-theta)+2j*math.pi*float(f)/L)*u)
                    for beta,f,c in rows)
            return abs(val)**2*math.exp(d*(u-k*L))
        dt=L/steps
        integ=(square(k*L)+square((k+1)*L)+
               sum((4 if j%2 else 2)*square(k*L+j*dt) for j in range(1,steps)))*dt/3
        full=energy(k,rows,d)
        assert abs(integ-full)<1e-10
        comparisons.append(dict(k=k,raw=round(full,13),edge=round(energy(k,edge,d),13),
                                difference=round(full-energy(k,edge,d),13)))
    return dict(synthetic_edge_real_part='3/4',positive_frequencies=[str(f) for _,f,_ in specs],
                multiplicities=[m for _,_,m in specs],weighted_mean=round(flat,13),
                raw_mean=round(raw,13),raw_diagonal_alone=round(diagonal,13),
                raw_shells=comparisons)


def filter_example():
    """Exact Gaussian rational moments before a final translation by 1/16."""
    r = Fraction(257,256)
    a = (r/(1+r), 1/(1+r))
    b = (r*r/(1+r*r), 1/(1+r*r))
    mass = [Fraction(0)]*4
    for i,ai in enumerate(a):
        for k,bk in enumerate(b):
            mass[i+2*k] += ai*bk
    # With real part 16 log(r), phase advances -1 or i per time step.
    # The second moment is evaluated separately in Q and i Q.
    at_minus_r = sum(x*(-r)**j for j,x in enumerate(mass))
    at_i_r_real = sum(mass[j]*r**j*(-1)**(j//2) for j in (0,2))
    at_i_r_imag = sum(mass[j]*r**j*(-1)**(j//2) for j in (1,3))
    assert sum(mass)==1 and at_minus_r==at_i_r_real==at_i_r_imag==0
    # Same ordinate, real-part difference 1/8: use (1+8 derivative).
    target_factor=1-8*Fraction(0)
    same_height_factor=1-8*Fraction(1,8)
    assert target_factor==1 and same_height_factor==0
    return dict(support='(j+1)/16, 0 <= j <= 3; translation multiplies each moment by a nonzero factor',
                exponential_radius=str(r),
                four_atom_masses=[str(x) for x in mass], target_moment='1',
                at_minus_radius='0', at_i_times_radius='0+0i',
                same_ordinate_difference='1/8', differential_multiplier_at_it='0')


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--out',type=Path)
    out=args.parse_args().out
    record=dict(actual_levels=original_checks(),synthetic_resonance=edge_model(),
                finite_filter=filter_example())
    blob=json.dumps(record,indent=2,sort_keys=True)+'\n'
    if out:
        out.write_text(blob)
    else:
        print(blob,end='')

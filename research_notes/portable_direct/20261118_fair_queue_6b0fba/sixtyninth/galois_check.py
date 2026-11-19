"""Degree-780 AP cofactor, its normalizing numerator and the real interval.
Dependencies: numpy and python-flint 0.9.0. Reuses two audited wave-21 modules.
"""
import json
import sys
from math import comb, factorial, gcd, lcm, prod
from hashlib import sha256
from pathlib import Path
import numpy as np
from flint import acb, acb_mat, arb, ctx, fmpq, fmpq_mat, fmpz, nmod_mat, nmod_poly as poly

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"twentyfirst"))
import christoffel_check as c
from physical_flow_check import cofactor, lower_power, split_half


def residue_polynomial(m,p):
    n=m-1;d=n*(2*m-3);w=[(-1)**i*comb(n,i)%p for i in range(m)]
    inv=np.array([0]+[pow(i,-1,p) for i in range(1,p)],dtype=np.int64)
    layer=np.array([[[w[i]*w[j]*w[s]*int(inv[i+1+m*j+m*m*s])%p for j in range(m)]for i in range(m)]for s in range(m)],dtype=np.int64)
    a0,ad=c.endpoints_mod(m,p)
    xs=list(range(1,d+1))+[d+1,p-1]
    ys=[a0]
    for start in range(0,len(xs),100):
        x=np.array(xs[start:start+100],dtype=np.int64);h=np.zeros((len(x),m,m),dtype=np.int64)
        for l in reversed(layer):h=(h*x[:,None,None]+l)%p
        lap=np.zeros((len(x),2*m-1,2*m-1),dtype=np.int64)
        lap[:,range(m),range(m)]=h.sum(axis=2)%p;lap[:,range(m,2*m-1),range(m,2*m-1)]=h.sum(axis=1)[:,:-1]%p
        lap[:,:m,m:]=(-h[:,:,:-1])%p;lap[:,m:,:m]=(-h[:,:,:-1].transpose(0,2,1))%p
        ds=c.determinant_batch(lap,inv,p).tolist()
        ys.extend((z*pow(int(i),-n,p))%p for z,i in zip(ds,x))
    dif=np.array(ys[:d+1],dtype=np.int64); coeff=[];fac=1
    for j in range(d+1):
        if j:fac=fac*j%p
        coeff.append(int(dif[0])*int(inv[fac])%p)
        dif=np.diff(dif)%p
    x=poly([0,1],p);q=poly([coeff[-1]],p)
    for i in reversed(range(d)): q=q*(x-i)+coeff[i]
    assert int(q[d])==ad and int(q(p-1))==ys[-1] and int(q(d+1))==ys[-2]
    return q

def margins(p):
 n=20;q=[(-1)**i*comb(n,i)%p for i in range(n+1)]
 es=[];ds=[]
 for i in range(21):
  es.append(poly([sum(q[j]*pow(1+i+21*j+441*s,-1,p) for j in range(21))*q[s]%p for s in range(21)],p))
  ds.append(poly([sum(q[j]*pow(1+j+21*i+441*s,-1,p) for j in range(21))*q[s]%p for s in range(21)],p))
 alpha=sum((q[j]*es[j] for j in range(21)),poly([],p))
 assert alpha==sum((q[j]*ds[j] for j in range(21)),poly([],p))
 return alpha,es,ds

def real_interval(m):
    n, b = m-1, m*m
    degree = n*(2*m-3)
    # An odd transform length avoids the pole introduced by dividing by (1+z)^n.
    length = min(3**a*5**j*7**k for a in range(8) for j in range(5) for k in range(4)
                 if 3**a*5**j*7**k > degree)
    weights = [(-1)**i*comb(n,i) for i in range(m)]
    spectra = []
    exact_at_one = []
    for i in range(m):
        row, fixed = [], []
        for j in range(m):
            ell = 1+i+m*j
            # Coefficients of the homogenized edge in ordinary powers of z.
            value = arb(weights[i]*weights[j])/ell
            poly = [acb(value)]
            for h in range(1,n+1):
                value = value*((n-h+1)*b)/(ell+b*h)
                poly.append(acb(value))
            row.append(acb.dft(poly + [acb(0)]*(length-len(poly))))
            fixed.append(fmpq(weights[i]*weights[j]*factorial(n)*b**n,
                               prod(ell+b*s for s in range(n+1))))
        spectra.append(row)
        exact_at_one.append(fixed)

    values = [None]*length
    for k in range(length//2+1):
        z = (acb(-2*k)/length).exp_pi_i()
        edges = [[spec[k] for spec in row] for row in spectra]
        value = cofactor(edges,acb_mat) / ((z*(1+z))**n)
        values[k] = value
        if k:
            values[-k] = value.conjugate()
    coefficients = acb.dft(values,inverse=True)
    assert all(x.imag.contains(0) for x in coefficients)
    assert all(x.contains(0) for x in coefficients[degree+1:])
    beta = [x.real/comb(degree,j) for j,x in enumerate(coefficients[:degree+1])]
    q0 = fmpq(n**n * m**(n*(n+3)+m) * factorial(n)**(2*m) *
              prod(comb(n,j)**2 for j in range(m)) * (3*b+1), 2*factorial(2*b))
    q1 = cofactor(exact_at_one,fmpq_mat)
    assert q1 > 0 and beta[0].overlaps(arb(q0)) and beta[-1].overlaps(arb(q1))


    normalized=[v/arb(q0) for v in beta]
    assert all(u>0 or u<0 for u in normalized)
    neg=[j for j,v in enumerate(normalized) if v<0]
    left,right=split_half(normalized)
    assert all(v>0 or v<0 for v in left+right)
    left_neg=[j for j,v in enumerate(left) if v<0]
    ql,qr=split_half(left)
    pieces=[ql,qr,right]
    bounds=[lower_power(row) for row in pieces]
    assert neg==list(range(259,283)) and left_neg==[545,546] and bounds==[13,23,20]
    first=int((normalized[neg[0]]*10**12).floor().unique_fmpz())
    assert arb(fmpq(first,10**12))<normalized[neg[0]]<arb(fmpq(first+1,10**12))
    return dict(m=m,degree=degree,precision=ctx.prec,transform_length=length,
                original_negative=neg,left_half_negative=left_neg,original_positive=len(beta)-len(neg),
                first_negative_ratio_interval_times_10_12=[first,first+1],
                positive_pieces=[dict(interval_at_quarters=ab,power_bound=bnd)
                    for ab,bnd in zip(([0,1],[1,2],[2,4]),bounds)],
                exact_rational_endpoint_positive=bool(q1>0))


def schur_identity(p,q):
    """Verify the entire reduction via >780 nonroot-of-marginal evaluations."""
    m=21
    n=m-1
    weights=[(-1)**i*comb(n,i)%p for i in range(m)]
    layers=np.array([[[weights[i]*weights[j]*weights[k]*pow(1+i+m*j+m*m*k,-1,p)%p
                       for j in range(m)] for i in range(m)] for k in range(m)],dtype=np.int64).reshape(m,-1)
    assert gcd(19,p-1)==1
    roots=[1+(7+19*i)%(p-1) for i in range(920)]
    powers=np.array([[pow(int(a),k,p) for k in range(m)] for a in roots],dtype=np.int64)
    edges=(powers@layers%p).reshape(len(roots),m,m)
    inv=np.array([0]+[pow(i,-1,p) for i in range(1,p)],dtype=np.int64)
    seen=0
    for a,W in zip(roots,edges):
        E=W.sum(axis=0)%p
        if (E==0).any():
            continue
        D=W.sum(axis=1)%p
        sub=np.diag(D[:n])-((W[:n]*inv[E])%p)@W[:n].T
        det=int(nmod_mat((sub%p).tolist(),p).det())*prod(int(x) for x in E)%p
        assert det==pow(int(a),n,p)*int(q(int(a)))%p
        seen+=1
    assert seen>780
    return seen


def cycles(f):
    assert f.gcd(f.derivative()).degree()==0
    scale,factors=f.factor()
    reconstructed=poly([int(scale)],f.modulus())
    for irreducible,k in factors:
        assert k==1
        reconstructed*=irreducible
    assert reconstructed==f
    return sorted(a.degree() for a,k in factors)


def degrees(parts):
    possible={0}
    for value in parts:
        possible|={a+value for a in possible}
    return possible


def digest(f):
    return sha256(','.join(str(int(c)) for c in f.coeffs()).encode()).hexdigest()


def normalized_kernel(p,polynomial,expected):
    w=[(-1)**i*comb(20,i) for i in range(21)]
    for root,mult in sorted((int(r),int(e)) for r,e in polynomial.roots()):
        assert mult==1
        t=root
        layers=[z*pow(t,k,p)%p for k,z in enumerate(w)]
        H=[[sum(layers[k]*pow(1+i+21*j+441*k,-1,p) for k in range(21))%p
            for j in range(21)] for i in range(21)]
        e=[sum(x*b for x,b in zip(row,w))%p for row in H]
        d=[sum(H[i][j]*w[i] for i in range(21))%p for j in range(21)]
        if 0 in e+d:
            continue
        A=nmod_mat([[H[i][j]*w[j]*pow(e[i],-1,p)%p for j in range(21)] for i in range(21)],p)
        B=nmod_mat([[H[i][j]*w[i]*pow(d[j],-1,p)%p for i in range(21)] for j in range(21)],p)
        I=nmod_mat([[int(i==j) for i in range(21)] for j in range(21)],p)
        delta=I-B*A
        nullities=[21-(delta**j).rank() for j in (1,2,3)]
        assert nullities==expected
        return dict(prime=p,residue=t,nullities=nullities)
    raise AssertionError('no simple residue with invertible margins')


def main():
    m=21
    large_types={9277:[2,15,45,718],9323:[5,8,29,30,43,76,589],
                 9391:[1,1,1,13,56,67,120,521]}
    small_types={9277:[1,3,16],9293:[1,19],9391:[2,5,13]}
    large_data={}
    small_data={}
    kernels={}
    possible=set(range(781))
    small_possible=set(range(21))
    for p in sorted(set(large_types)|set(small_types)):
        assert fmpz(p).is_prime() and p>m**3
        if p in large_types:
            f=residue_polynomial(m,p)
            lengths=cycles(f)
            assert lengths==large_types[p] and f.degree()==780
            if p==9391:
                kernels['q']=normalized_kernel(p,f,[2,2,2])
            possible&=degrees(lengths)
            large_data[p]=dict(degrees=lengths,proper_degrees_left=len(possible)-2,
                               poly_sha256=digest(f),independent_schur_points=schur_identity(p,f))
        if p in small_types:
            a,left,right=margins(p)
            lengths=cycles(a)
            assert lengths==small_types[p] and a.degree()==20
            if p==9277:
                kernels['alpha']=normalized_kernel(p,a,[1,2,2])
            small_possible&=degrees(lengths)
            assert all(v.degree()==20 and a.gcd(v).degree()==0 for v in left+right)
            small_data[p]=dict(degrees=lengths,poly_sha256=digest(a),coprime_degree_20_margins=42)
    assert possible=={0,780} and small_possible=={0,20}
    assert fmpz(521).is_prime() and all(s%521 for s in large_types[9391] if s!=521)
    assert fmpz(13).is_prime() and gcd(lcm(2,5),13)==1
    parity=lambda n,parts:(n-len(parts))%2
    assert parity(780,large_types[9323])==1
    assert parity(780,large_types[9391])==0 and parity(20,small_types[9391])==1
    ctx.prec=2048
    print(json.dumps(dict(q21=large_data,alpha21=small_data,characteristic_zero_kernel_witness=kernels,real=real_interval(m)),
                     indent=2))


if __name__=='__main__':
    main()

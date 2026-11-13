"""Two-block model checks and rational recovery of p-adic Taylor centers and slopes."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from itertools import permutations
from math import gcd, prod
from pathlib import Path
import json
import sys


def order(x):
    if x == 0:
        return float("inf")
    x = Q(x)
    return (x.numerator & -x.numerator).bit_length() - (x.denominator & -x.denominator).bit_length()


def residue(x, bits):
    """Return x modulo 2**bits for a 2-adically integral rational x."""
    assert x.denominator % 2
    mod = 1 << bits
    return (x.numerator * pow(x.denominator, -1, mod)) % mod


def recover(x, bits, bound):
    """Recover a small-height rational from dyadic data; check the output congruence."""
    shift = min(order(x), 0)
    y = x * (1 << -shift)
    mod = 1 << bits
    assert mod > 2 * bound**2
    val = residue(y, bits)
    r, s, v, t = mod, val, 0, 1
    while abs(s) > bound:
        q, rem = divmod(r, s)
        r, s, v, t = s, rem, t, v - q*t
    if not t or abs(t) > bound or gcd(t, mod) != 1 or gcd(s,t) != 1:
        raise ArithmeticError("out of reconstruction range")
    ans = Q(s,t)
    assert residue(ans,bits) == val
    return ans / (1 << -shift)


def coefficient(k,n,s):
    return Q(k-1+s,28*(k-1+4*s))*Q(prod(range(n+k+1,n+4*k+1)),prod(range(s+k,s+4*k)))


def parameters(k,n,s):
    a = coefficient(k,n,s)
    inv_rho = Q((4**(n-s))*prod(range(k+s,k+n+1)),prod(k+4*i for i in range(s,n+1)))
    return a, a*inv_rho


def model(c,gaps):
    v = c-gaps[0]
    w = v-gaps[1]
    assert w-2 == gaps[2] and w >= 4
    a,t = parameters(5,c,v)
    b,s = parameters(3,v,w)
    W = Q((w+2)*(w+3)*(w+4),840)
    h = Q(prod(4*i+4 for i in range(3,w+1)),prod(4*i+1 for i in range(3,w+1)))
    U, X, deriv = [], [], []
    for j,u in [(Q(1,2),Q(6)), (Q(5),Q(3,32))]:
        L = 1+j*W
        tail = L/(1+h*W/u)
        U.append((1+b/L)/a)
        X.append(((tail+b)/(tail+s)+t)/(a-t))
        deriv.append(((1+U[-1])/a, -U[-1]/L, b*W/(a*u*L)))
    return U,X,[deriv[0][i]/deriv[1][i] for i in range(3)],(t,s,h)


def native_controls(prior):
    sys.path.insert(0,str(prior.resolve()))
    from mixed_kernel import responses
    count = 0
    for c in range(4,15):
        for v in range(4,c+1):
            for w in range(4,v+1):
                gaps=(c-v,v-w,w-2)
                _,X,_,_=model(c,gaps)
                rows,_=responses(2,c,gaps)
                Z=[(7*rows[0][j]+rows[1][j])/(7*rows[0][j]+rows[2][j]) for j in (3,4,5)]
                assert X == [1/(Z[2]-1),1/(Z[0]-1)]
                assert sorted((Z[2],Z[0])) == [min(Z),max(Z)]
                count+=1
    return count


def monotone_integer(f, value, low, high):
    while low < high:
        mid = (low+high)//2
        if f(mid) < value:
            low = mid+1
        else:
            high = mid
    assert f(low) == value
    return low


def decode(c, xs, bits, bound):
    # Pair each unlabelled endpoint with its reconstructed center, then order centers.
    (Ud,Xd),(UD,XD)=sorted(((recover(x,bits,bound),x) for x in xs),reverse=True)
    V=Ud/UD
    slope=recover((Xd-Ud)/(XD-UD),bits,bound)
    if 1 < slope < V:
        assert slope == (1+Ud)/(1+UD)
        val=order((Xd-Ud)/(1+Ud))
        n=c+5
        def first_gap_order(m):
            s=n-m-1
            return 2*m+n-n.bit_count()-s+s.bit_count()
        v=c-monotone_integer(first_gap_order,val,0,c-2)
        A=1/coefficient(5,c,v)
        T=(Ud-A)/(UD-A)
        shortest=1
    elif slope > V:
        shortest,T=2,slope/V
    else:
        assert slope < 1
        shortest,T=3,64*slope
    W=(T-1)/(5-T/2)
    w=monotone_integer(lambda k:(k+2)*(k+3)*(k+4),840*W,2,c)
    if shortest != 1:
        d,D=1+W/2,1+5*W
        A=(D*UD-d*Ud)/(D-d)
        v=monotone_integer(lambda k:1/coefficient(5,c,k),A,2,c)
    return shortest,(c-v,v-w,w-2)


def jet_controls():
    cert=[]
    for sizes in [(180,390,640),(275,600,993),(300,700,1290)]:
        for gaps in permutations(sizes):
            c=sum(gaps)+2
            U,X,S,p=model(c,gaps)
            i=gaps.index(min(gaps))
            assert U[0] > U[1] and 0 < S[2] < 1 < S[0] < U[0]/U[1] < S[1]
            bits=min(order(X[j]-U[j]) for j in (0,1))
            margin=min(order(q) for k,q in enumerate(p) if k != i)-order(p[i])
            assert min(bits,margin)>500
            which,word=decode(c,sorted(X),500,1<<245)
            assert (which,word)==(i+1,gaps)
            recovered=[recover(x,500,1<<245) for x in sorted(X)]
            assert sorted(recovered) == sorted(U)
            slope=(X[0]-U[0])/(X[1]-U[1])
            slope_bits=order(slope-S[i])
            assert slope_bits>=500
            assert recover(slope,500,1<<245)==S[i]
            if i==0:
                vp=order((X[0]-U[0])/(1+U[0]))
                v=c-gaps[0]
                assert vp==2*gaps[0]+sum(order(5+j) for j in range(v,c+1))
            else:
                T=S[i]/(U[0]/U[1]) if i==1 else S[i]*64
                W=(T-1)/(5-T/2)
                w=gaps[2]+2
                assert 840*W==(w+2)*(w+3)*(w+4)
                d,D=1+W/2,1+5*W
                A=(D*U[1]-d*U[0])/(D-d)
                assert 1/A==parameters(5,c,c-gaps[0])[0]
            cert.append(dict(gaps=gaps,stock=c,shortest=i+1,center_agreement_bits=bits,
                             slope_agreement_bits=slope_bits,next_parameter_margin_bits=margin))
    return cert


if __name__ == '__main__':
    here=Path(__file__).resolve().parents[2]
    p=ArgumentParser(description=__doc__)
    p.add_argument('--prior',type=Path,default=here/'C67'/'joint')
    args=p.parse_args()
    print(json.dumps(dict(native_three_state_words=native_controls(args.prior),
                          blind_decoded_words=18, dyadic_reconstruction_precision=500,controls=jet_controls()),indent=2))

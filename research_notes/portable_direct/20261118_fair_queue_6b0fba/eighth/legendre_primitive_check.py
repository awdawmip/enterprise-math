"""Check the classical polynomial primitive and its CM divided-value corollary."""
from fractions import Fraction as F
from math import isqrt


def plus(*args):
    size = max(map(len, args))
    return [sum((x[i] for x in args if i < len(x)), F(0)) for i in range(size)]


def scale(s, f):
    return [s*x for x in f]


def mult(f, g):
    result = [F(0)]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):
            result[i+j] += a*b
    return result


def derivative(f):
    return [i*f[i] for i in range(1,len(f))] or [F(0)]


def trim(f):
    return tuple(f[:next((i+1 for i in reversed(range(len(f))) if f[i]),0)])


def check_polynomials(top):
    polynomials = [[F(1)], [F(0),F(1)]]
    for k in range(1,top):
        polynomials.append(scale(F(1,k+1),plus([F(0)]+scale(2*k+1,polynomials[k]),
                                                    scale(-k,polynomials[k-1]))))
    for n,f in enumerate(polynomials):
        parts=[scale(F(2*j+1,(n-j)*(n+j+1)),polynomials[j]) for j in range(n%2,n,2)]
        aux=plus(*parts) if parts else [F(0)]
        square=mult(f,f)
        expected=[F(0)]+[F(2*n+1,i+1)*a for i,a in enumerate(square)]
        wronskian=plus(mult(derivative(f),aux),scale(-1,mult(f,derivative(aux))))
        rhs=plus([F(0)]+square,mult([F(2),F(0),F(-2)],wronskian))
        assert trim(expected)==trim(rhs),n


def compare_lifts(p):
    """Compute p^2 digit by Bonnet, predict it using only residues modulo p."""
    assert p%24 in (13,19) and all(p%j for j in range(2,isqrt(p)+1))
    n=(p-1)//3
    # V_j=P_j(t)/t^(j mod 2), computed without adjoining t.
    def cycle(modulus):
        prev,now=1,1
        yield prev
        yield now
        half=pow(2,-1,modulus)
        for j in range(1,n):
            factor=half if j%2 else 1
            prev,now=now,((2*j+1)*factor*now-j*prev)*pow(j+1,-1,modulus)%modulus
            yield now

    values=iter(cycle(p))
    weighted=0
    previous=0
    for j,v in enumerate(values):
        if j%2==0 and j<n:
            weighted=(weighted+v*(pow(3*j+1,-1,p)+pow(3*j+2,-1,p)))%p
        if j==n-1:
            previous=v
        if j==n:
            assert v==0
    prediction=(-2*weighted-pow(2*previous,-1,p))%p
    raw=0
    for raw in cycle(p*p):
        pass
    assert raw%p==0
    assert raw//p==prediction
    return (p,n,previous,weighted,prediction)


if __name__=='__main__':
    check_polynomials(24)
    print('Exact rational polynomial coefficients agree for 0 <= n <= 24.')
    for p in (21157,21139):
        print('p, n, V_(n-1), harmonic sum, P_n(t)/p:', *compare_lifts(p))


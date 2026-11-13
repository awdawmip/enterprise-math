"""Rational point Jacobians for the combined real and 2-adic limiting observables."""
import json
import sympy as sp


def quantities(landings):
    r = len(landings)
    x = [1, *landings]
    real = 0
    real_deriv = 1
    center = 0
    center_deriv = 1
    for i in range(r,0,-1):
        power = 3*(2*(r-i+1)+1)
        rate = 4*(x[i]/x[i-1])**power
        scale = sp.Rational(7,16)*rate**5
        alpha = rate/scale
        real_deriv *= scale*(1-rate)/(1+scale*real)**2
        real = (rate+scale*real)/(1+scale*real)
        center_deriv *= -alpha/(1+alpha*center)**2
        center = 1/(1+alpha*center)
    return [real, real_deriv*x[-1]**-3, center, center_deriv*x[-1]**-12][:r]


# First-order dual arithmetic over a prime field; raises on a zero divisor.
P=10**9+7


def add(u,v):
    return tuple((a+b)%P for a,b in zip(u,v))


def mul(u,v):
    return (u[0]*v[0]%P, *((u[0]*b+a*v[0])%P for a,b in zip(u[1:],v[1:])))


def power(u,n):
    if n < 0:
        inv=pow(u[0],-1,P)
        return power((inv,*((-inv**2*a)%P for a in u[1:])), -n)
    result=(1,*(0 for _ in u[1:]))
    x=u
    while n:
        if n & 1:
            result=mul(result,x)
        n//=2
        x=mul(x,x)
    return result


def dual_run(r):
    def constant(x):
        return (x%P,*(0 for _ in range(r)))
    xs=[constant(1)]
    for i in range(1,r+1):
        xs.append(((13-i)*pow(13+i,-1,P)%P,*(int(i==j) for j in range(1,r+1))))
    one, minus, h=constant(1),constant(-1),constant(7*pow(16,-1,P))
    real,center=constant(0),constant(0)
    dr,dc=one,one
    for i in range(r,0,-1):
        d=3*(2*(r-i+1)+1)
        rate=mul(constant(4),power(mul(xs[i],power(xs[i-1],-1)),d))
        scale=mul(h,power(rate,5))
        a=mul(rate,power(scale,-1))
        den=add(one,mul(scale,real))
        dr=mul(mul(dr,scale),mul(add(one,mul(minus,rate)),power(den,-2)))
        real=mul(add(rate,mul(scale,real)),power(den,-1))
        den=add(one,mul(a,center))
        dc=mul(mul(dc,mul(minus,a)),power(den,-2))
        center=power(den,-1)
    obs=[real,mul(dr,power(xs[-1],-3)),center,mul(dc,power(xs[-1],-12))][:r]
    return [list(o[1:]) for o in obs]


def main():
    data=[]
    for r in (3,4):
        x=sp.symbols('x:'+str(r))
        values={v:sp.Rational(12-i,14+i) for i,v in enumerate(x)}
        def reduce(q):
            n,d=q.xreplace(values).as_numer_denom()
            return int(n)*pow(int(d),-1,P)%P
        jac=[[reduce(f.diff(v)) for v in x] for f in quantities(x)]
        assert dual_run(r)==jac
        det=int(sp.Matrix(jac).det())%P
        assert det
        data.append(dict(visible_blocks=r,root_coordinates=[str(values[v]) for v in x],
                         jacobian_mod_prime=jac,determinant_mod_prime=det))
    print(json.dumps(dict(prime=P,agrees_two_independent_derivatives=True,controls=data),indent=2))


if __name__=='__main__':
    main()

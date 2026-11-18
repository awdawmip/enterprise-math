"""Exact checks of the modular formulas and the discriminant -64 example. Needs SymPy."""
import json
import sympy as s

x, e, z, w = s.symbols("x e z w")


def j(x):
    return 256*(1-x+x*x)**3/(x*x*(1-x)**2)


def jdouble(x):
    return 16*(16-16*x+x*x)**3/(x**4*(1-x))


def selector(x,e):
    return ((e**2+(4*x-2)*e+7*x*x-7*x+1)/(3*(1-x)**2),
            (1-3*x-e)/(1-x))


def zero(expr):
    assert s.factor(expr)==0


def universal():
    a,b=selector(x,e)
    t=1/(1-x)
    t2=5-2*b-t
    x2=(1+2*x+2*e)/(2+x+2*e)
    e2=-(2+2*x+3*e)/(2+x+2*e)
    zero(t*t+(2*b-5)*t+b*b-2*b+4-3*a)
    zero(1/(1-x2)-t2)
    zero(t2-t-(1+x+2*e)/(1-x))
    zero(e2+1+(x+e)/(2+x+2*e))
    for actual,wanted in zip(selector(x2,e2),(a,b)):
        zero(actual-wanted)
    A4=1-x+x*x
    A6=(1+x)*(1-2*x)*(2-x)/2
    zero((A4**3-A6**2)/1728-x*x*(1-x)**2/256)
    zero(j(((1-w)/(1+w))**2)-jdouble(1-w*w))
    return 8


def quadratic_demo():
    h=s.sqrt(2)
    X=17-12*h
    E=9-6*h
    a,b=selector(X,E)
    assert s.simplify(j(X))==66**3
    return dict(x=str(X),e=str(E),alpha=str(s.radsimp(a).expand()),
                b=str(s.radsimp(b).expand()), j=int(j(X).simplify()))


def quartic_demo():
    P=s.Poly(w**4+32*w*w-32,w,domain=s.QQ)
    assert P.is_irreducible and P.count_roots(-s.oo,s.oo)==2
    def red(expr):
        num,den=map(lambda v:s.Poly(v,w,domain=s.QQ),s.fraction(s.cancel(expr)))
        return (num*s.invert(den,P)%P).as_expr()
    def primitive(expr):
        resultant=s.resultant(P.as_expr(),z-expr,w)
        return s.Poly(resultant,z).clear_denoms()[1].primitive()[1]
    X=red(((1-w)/(1+w))**2)
    E=red(3/(1+w)**2)
    # Check the quadratic input for the duplication from 2i to 4i.
    h=red((w*w+16)/12)
    assert red(h*h-2)==0 and red(1-w*w-(17-12*h))==0
    assert red(2*(9-6*h)+2-(17-12*h)-3)==0
    a,b=map(red,selector(X,E))
    data={}
    for name,value in (("x",X),("e",E),("alpha",a),("b",b),("j8i",red(jdouble(X)))):
        poly=primitive(value)
        assert poly.degree()==4 and poly.is_irreducible
        matrix=s.Matrix([[s.Poly(red(value**i),w).nth(j) for i in range(4)]
                         for j in range(4)])
        determinant=matrix.det()
        assert determinant!=0
        data[name]=dict(polynomial=str(poly.as_expr()),generator_det=str(determinant))
    return dict(w_polynomial=str(P.as_expr()), real_roots=2,values=data)


if __name__=="__main__":
    print(json.dumps(dict(symbolic_checks=universal(),square_CM=quadratic_demo(),
                          quartic_CM=quartic_demo()),indent=2))

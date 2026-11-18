"""Exact CP19, odd-row, CM orbit, and theta-series checks. Requires SymPy."""
import sympy as S

x, s, e, w, t = S.symbols("x s e w t", nonzero=True)
d = 1 - x
delta = d * w
theta_s = -(s**2 + 2*(2*x-1)*s + 1 - x + x*x)/(6*d)
theta_w = w*(s+2*x-1)/(3*d)
theta_t = 1/delta


def theta(f):
    return x*f.diff(x) + theta_s*f.diff(s) + theta_w*f.diff(w) + theta_t*f.diff(t)


def zero(f):
    assert S.factor(f) == 0


def algebra():
    w0 = w**2
    u = theta(w0)/w0
    L = w**3/d
    b = -3/(delta*t) - theta(L)/L
    a = 3/(delta*t)**2-u*b-theta(theta(w0))/w0
    bc = (1-3*x-e)/d
    ac = (e**2+(4*x-2)*e+7*x*x-7*x+1)/(3*d**2)
    for coeff, wanted in [(a, ac), (b, bc)]:
        zero(coeff - wanted.subs(e, s+3/(w*t)))

    def operator(f):
        return a*f+b*theta(f)+theta(theta(f))

    zero(operator(w0*t))
    zero(operator(w0*t**3/6))
    zero(operator(w0)-3*w0/(delta*t)**2)
    zero(-theta(w0*t)/(w0*t) -
         (-2*(e+2*x-1)/(3*d)+1/(delta*t)).subs(e, s+3/(w*t)))

    r = S.sqrt(3)
    for sign in [1, -1]:
        cm_x = (2-sign*r)/4
        cm_e = (1-2*cm_x)/2
        aa = S.simplify(ac.subs({x: cm_x, e: cm_e}))
        bb = S.radsimp(bc.subs({x: cm_x, e: cm_e})).expand()
        zero(16*cm_x**2-16*cm_x+1)
        zero(aa)
        zero(bb-(-10+sign*6*r))
        zero(bb**2+20*bb-8)
        print("x =", cm_x, "ray =", (aa, bb, 1))
    T = S.symbols("T")
    assert S.Poly(T*T+20*T-8, T, domain=S.QQ).is_irreducible


def theta_series(n=24):
    # q = exp(pi i tau), so E_k(tau) uses q^2; E_k((tau+1)/2) uses -q.
    def plus(a, b):
        return [aa+bb for aa, bb in zip(a, b)]

    def scale(a, c):
        return [aa*c for aa in a]

    def mult(a, b):
        return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(n+1)]

    def fourth(a):
        square = mult(a, a)
        return mult(square, square)

    def eisen(k, half=False):
        result = [1]+[0]*n
        for j in range(1, (n if half else n//2)+1):
            sigma = sum(k0**(k-1) for k0 in range(1, j+1) if j % k0 == 0)
            result[j if half else 2*j] = {2:-24, 4:240}[k] * sigma * ((-1)**j if half else 1)
        return result

    th3, th4 = [1]+[0]*n, [1]+[0]*n
    for j in range(1, int(n**0.5)+1):
        th3[j*j], th4[j*j] = 2, 2*(-1)**j
    W, Y = fourth(th3), fourth(th4)
    X = plus(W, scale(Y,-1))  # X = lambda*W = theta_2^4
    assert plus(eisen(2, True), scale(eisen(2), -2)) == plus(scale(X, 2), scale(W,-1))
    assert eisen(4, True) == plus(mult(W, W), plus(scale(mult(X, W),-16), scale(mult(X, X),16)))
    print("both half-argument identities through q^" + str(n))


if __name__ == "__main__":
    algebra()
    theta_series()

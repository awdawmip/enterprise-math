# R284IK — Exact critical exception asymptotic by nondegenerate endpoint transfer
2026-11-26. Author proof, NOT_REVIEWED. Directed continuation of R284IJ @75426bd0581d1826bfde31ac82cb5a632f53cc51:research_notes/portable_direct/R284IJ_THIRD_ORDER_CRITICAL_PROFILE_SHARP_EXCEPTION_SCALE_20261126.md and R284II @c7be4488d3caa0ff3fa0a2febac189f084982516:research_notes/portable_direct/R284II_SECOND_ORDER_CRITICAL_PROFILE_20261126.md. Exact frozen II/IJ statements used; auxiliary binary-tag safe-word total-count observer only. P000 V5, joint-relation preservation and ACTIVE worldview retained; account entry blobs match main@7ed2825fc9b72fdbcaa910e9c4c9d9adf333058c. Own-session metadata recovered with registration request r1-20261124-0256-r284gd-session-v1 SUCCEEDED, same RA-B82240E8488EF5A1DA5186C4 and no runs. Fresh owner inventory r1-20261126-1104-owner-inventory RUNNING at last check; previous snapshot no LEASED. No shared claim, no protected task mutation.

## Main result
Let s=s0 be the unique positive zero of Phi in IH/II, C=C0=-Psi(s)/Phi'(s), Z=Z0 from IJ, W=2Z/s. Put Q_n=((n-C)/s)^2. Then Q_n is equidistributed modulo 1, without assuming irrationality of s^2 or of any unproved constant.
More strongly, s and C cannot both be algebraic: if s is algebraic, C is transcendental.
Consequently, conditional only on the existing II/IJ profile and ID author-level global monotonicity, the actual number N(X) of failures of the II two-term ceil rule for q<=X satisfies
N(X) ~ 2Z sqrt(X), with 16.5341446526 < 2Z < 16.5341446814.
Among complete large-n exception clusters, the proportions of clusters with 18 and 17 failures tend to W-17 and 18-W, respectively. All eventually have 17 or 18 by IJ. The three-term ceil rule ceil(s sqrt(q)+C+Z/sqrt(q)) has o(sqrt(X)) possible exceptions, including any equality ambiguity. Neither result requires a fourth-order explicit error constant or quantitative Diophantine bound.

## 1. Endpoint transfer, exact nondegeneracy
Use II notation x in [0,s], y=s-x, w=exp(-x^2-y^2/2), a=s*x^2-2*x+s*y^2/4-y, b=(2*y-s-(y^2-1)*(s-y))/2. Let M_j=int x^j w dx, m=M_0, e=exp(-s^2/2), f=exp(-s^2). These are auxiliary integral observations of the frozen joint carrier, not native coordinates. All polynomials in x against w reduce exactly to three real observations (m,e,f) at each s:
M_1=(s*m+e-f)/3,
M_j=(s*M_(j-1)+(j-1)*M_(j-2)-s^(j-1)*f)/3 for j>=2.
This follows from w_x=(s-3x)w by integration by parts. Differentiation in s preserves this linear carrier: m'=(-2s*m+e+2f)/3, e'=-s*e, f'=-2s*f. For m', one can use the moving endpoint after completing the square, or m'=f-int(s-x)w dx. These identities establish exact observer reduction for the polynomial moments and derivatives actually used here, not a reduction of all future joint-branch information.

The II integrals I=int xyw, J=int (s+xy*a)w, D=int x(y^2-1)w, D1=int ((xa+1)(y^2-1)+xb)w-s*f/2, X=int x^3*y*w are retained including D1 endpoint. Then
I=(2es+fs+(2s^2-3)m)/9, D=-I'.
At the critical root, r=D/I=-7s/3. Hence
0=9(D+7sI/3)=(6s^2-1)e+(3s^2+1)f+s(6s^2-13)m.
The certified II root interval implies 0.93<s^2<0.94, so the m coefficient is nonzero. Substitute
m=-[(6s^2-1)e+(3s^2+1)f]/[s(6s^2-13)].
Important: evaluate derivatives of I,D BEFORE this substitution (the root identity holds only at s0).

Define N=I Psi(s), P=I Phi'(s) at the root. From II,
N=[(50s^2+48)/27+56sr/9+(16/3)(-r^2/2-19)]I+(16/3)(D1-rJ+2X+s f/2),
P=(112/9)I+(16/3)(D'-rI').
The term s f/2 in N retains the genuine E2 correction; D1 retains its own endpoint. Exact recurrence and elimination give, with z=s^2,
N=2[(40z^3-470z^2+1179z+328)e+(364z^3-1068z^2+1069z-328)f]/[27s(6z-13)],
P=-16[(60z^2+8z+13)e+(78z^2-73z-13)f]/[27s(6z-13)].
Write N=N_e e+N_f f, P=P_e e+P_f f. Then
N_e P_f-N_f P_e = 32(1040z^3+1054z^2-1351z-1296)/[243(6z-13)].
The numerator polynomial is strictly negative on [93/100,94/100]: bound its positive terms at 94/100 and negative z term at 93/100, giving a strictly negative rational upper bound. Denominator 6z-13<0, so determinant is strictly positive. I>0 and Phi'>0 imply P>0.

## 2. Unconditional equidistribution of the critical lattice
At the actual root C=-N/P is a nonconstant fractional-linear transformation of rho=f/e=exp(-s^2/2), with coefficients in Q(s). If s is algebraic, Hermite–Lindemann implies rho transcendental (nonzero algebraic exponent). Were C algebraic, the equation
(N_f+C P_f)rho=-(N_e+C P_e)
would imply rho algebraic unless both coefficients vanished. The latter would contradict the positive determinant. Thus s algebraic implies C transcendental. This is a disjunctive proof; it does not determine whether s itself is transcendental.

Expand Q_n=A n^2+B n+C^2/s^2 with A=1/s^2, B=-2C/s^2. If A irrational, Weyl's polynomial theorem gives equidistribution. If A rational, s algebraic, hence C transcendental, and B irrational. Weyl again applies. No Diophantine conjecture remains for qualitative distribution.

Classical theorem sources checked: Lindemann theorem, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Lindemann_theorem ; Weyl polynomial criterion as recalled in Y. Yifrach, A note on Weyl's equidistribution theorem, Monatshefte fuer Mathematik 206 (2025), 771–780, https://doi.org/10.1007/s00605-025-02057-2 . These are external mathematical inputs, not claims of native physical attribution.

## 3. Exact leading exception coefficient and cluster frequencies
IJ gives for every fixed epsilon>0 sufficiently small and all large n the sandwich of actual failing integer q:
[Q_n-W+epsilon,Q_n] intersect Z is contained in the failures, which are contained in [Q_n-W-epsilon,Q_n] intersect Z. Distinct bands disjoint eventually; all failures underestimate by one. Complete bands for q<=X have count s sqrt(X)+O(1), with at most O(1) integer q in the last incomplete band.
For fixed width L>0, the function G_L(t)=#([t-L,t] intersect Z) is bounded, 1-periodic, and Riemann integrable with integral L on [0,1] (endpoint inclusions only at finitely many phases). Equidistribution therefore gives average G_L(Q_n) -> L. Squeeze at L=W±epsilon then epsilon->0 gives N(X)/sqrt(X)->sW=2Z.
Because IJ already establishes exactly 17 or 18 per complete sufficiently large cluster, average W implies limiting fraction with 18 is W-17 and with 17 is 18-W. No claim of an effective rate is needed.

## 4. Three-term ceil rule: strict improvement of exception order
Let T(q)=s sqrt(q)+C+Z/sqrt(q). By IJ the sign bracket for integer d near crossing is strict outside H/q for some finite H; ID then makes ceil(T(q)) exact whenever dist(T(q),Z)>H/q. If |T(q)-n|<=H/q, then q=Q_n-W+O(1/sqrt(Q_n)): first T(q)=n+O(1/q) implies sqrt(q)~(n-C)/s, then s(sqrt(Q_n)-sqrt(q))=Z/sqrt(q)+O(1/q). Multiply by sqrt(Q_n)+sqrt(q) to obtain Q_n-q=W+O(1/sqrt(q)), with uniform constants for large q. Thus the candidate exception interval per n shrinks to the point Q_n-W, with length O(1/n). For every fixed epsilon in (0,1/2), eventually each interval contains at most one integer and only if dist(Q_n-W,Z)<=epsilon. Equidistribution gives upper density at most 2epsilon in n. Let epsilon->0. Since n<=s sqrt(X)+O(1), the candidate count is o(sqrt(X)), including potential equality cases. We do not infer O(log X) or a finite exception bound: those require quantitative distribution not supplied by qualitative Weyl.

## 5. Executed symbolic and rational check
Python/SymPy exact moment recurrence and Fraction finite ideal-band count; output:
I=(2*e*s+f*s+2*m*s**2-3*m)/9; D+Iprime=0
root=(6*e*s**2-e+3*f*s**2+f+6*m*s**3-13*m*s)/9
N,P and determinant exactly as above.
nonzero determinant certified by rational bounds
ideal band counts n=100..20099: {17:18390,18:1602,unresolved:8}.
The latter is a check of ideal bands (Q_n-W,Q_n], NOT a full true-K exception enumeration. Endpoints are outward rational bounds from IJ. Eight ambiguous intervals are excluded, not treated as errors. Actual asymptotics follow the proof rather than the finite count.

```python
import sympy as S
from fractions import Fraction as F
s,x,m,e,f=S.symbols('s x m e f'); y=s-x
M=[m,(s*m+e-f)/3]
for j in range(2,10):
    M.append(S.expand((s*M[-1]+(j-1)*M[-2]-s**(j-1)*f)/3))
def integ(p):
    return S.expand(sum(c*M[j] for (j,),c in S.Poly(p,x).terms()))
def deriv(p):
    return S.expand(S.diff(p,s)+S.diff(p,m)*(-2*s*m+e+2*f)/3-S.diff(p,e)*s*e-S.diff(p,f)*2*s*f)
a=s*x*x-2*x+s*y*y/4-y
b=(2*y-s-(y*y-1)*(s-y))/2
I=integ(x*y); J=integ(s+x*y*a); D=integ(x*(y*y-1))
D1=integ((x*a+1)*(y*y-1)+x*b)-s*f/2
X=integ(x**3*y)
root=S.expand(D+S.Rational(7,3)*s*I)
print('I=',S.factor(I)); print('root=',S.factor(root))
print('D+Iprime',S.simplify(D+deriv(I)))
assert S.simplify(D+deriv(I))==0
r=-S.Rational(7,3)*s
N=S.expand(((50*s*s+48)/27+56*s*r/9+S.Rational(16,3)*(-r*r/2-19))*I+S.Rational(16,3)*(D1-r*J+2*X+s*f/2))
P=S.expand(S.Rational(112,9)*I+S.Rational(16,3)*(deriv(D)-r*deriv(I)))
ms=S.solve(root,m)[0]; print('m=',S.factor(ms))
N=S.factor(N.subs(m,ms)); P=S.factor(P.subs(m,ms))
print('PsiI=',N); print('PhiPrimeI=',P)
det=S.factor(S.diff(N,e)*S.diff(P,f)-S.diff(N,f)*S.diff(P,e))
print('det=',det)
assert S.simplify(det-32*(1040*s**6+1054*s**4-1351*s**2-1296)/(243*(6*s**2-13)))==0
lo,hi=F(93,100),F(94,100)
assert S.Rational(968081516889,10**12)**2>lo and S.Rational(968081516890,10**12)**2<hi
assert 1040*hi**3+1054*hi**2-1351*lo-1296<0 and 6*hi-13<0
print('nonzero determinant certified')
sl,sh=F('0.968081516889'),F('0.968081516890')
cl,ch=F('2.0640021544'),F('2.0640021551')
wl,wh=F('17.0792896715'),F('17.0792897012')
counts={17:0,18:0,'unresolved':0}
for n in range(100,20100):
    a=(F(n)-ch)**2/sh**2; b=(F(n)-cl)**2/sl**2
    if a//1!=b//1 or (a-wh)//1!=(b-wl)//1 or a.denominator==1 or (a-wh).denominator==1:
        counts['unresolved']+=1; continue
    count=a//1-(a-wh)//1
    assert count in (17,18)
    counts[count]+=1
print('ideal band counts n=100..20099:',counts)
```

## Next
1. Quantitative distribution requires explicit irrationality/Diophantine approximation for at least one nonconstant coefficient (qualitative theorem does not provide it).
2. Derive an explicit uniform O(h^4) bound from IJ to implement the three-term rule with certified sparse fallback; consider fourth coefficient and its signed effect on the shrinking exception bands.
3. Preserve ID independent review pending. This proof closes the qualitative exceptional-count coefficient question, not the broader mother objective.

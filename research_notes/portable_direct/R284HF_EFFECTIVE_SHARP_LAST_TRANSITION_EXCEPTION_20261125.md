# R284HF — Effective sharp last exception and exact low-strip monotonicity

2026-11-25, author proof with exact symbolic computation, NOT_REVIEWED. Auxiliary binary-tag word-count model; no new native physical attribution. Source pins: HE 0e4f8d4318f145100959ca9ec3f41c0e219090d5:research_notes/portable_direct/R284HE_EXPONENTIAL_PORT_STRIP_AND_EVENTUAL_EXACT_ROUNDING_20261125.md; HC 36e96070fd5f44cabe0713c9047fb751232f69bc:research_notes/portable_direct/R284HC_GLOBAL_Q_MONOTONICITY_AND_FINITE_CUTOFF_20261125.md. Preserve their frozen dependencies and original count definitions. P000 V5 and ACTIVE worldview unchanged. Current global main entry snapshot 0a782b7feff54e9e99100d8b36d804348ee87ddc verified; EM main entry reads and observed head 7f2f771820d7671b37232b466191187aef8117ba. Original own registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED; own recovery metadata verified open, no runs, EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Current owner inventory r1-20261125-0501-owner-read RUNNING at last observation before publication; no shared CLAIM or formal mutation.

## Theorems

1. For integer u>=10000 and 0<=q<=floor(u/8), the HE rational strip quotient K0=N/B satisfies |K-K0| <= 960*(19/20)^u*K0. If N!=B, sign(K-1)=sign(N-B). Exact K decreases strictly in q throughout this strip (adjacent endpoints in strip). Also exact K increases strictly in u for adjacent u>=10000 at fixed q in the strip.
2. Let f(u)=(isqrt(324*u+121887)-169)//3. The eventual HE formula has the sharp permanent onset
   U*=2522581650951, q*=9529526.
   For every integer u>U*, K(q,u)>1 exactly when 0<=q<=f(u); all f(u)<q<u give K<1. At u=U*, f(u)=q* but the actual maximal q with K>1 is q*-1; all q>=q* have K<1. Thus the smallest integer onset of permanent validity is 2522581650952. This is a symbolic certificate over an unbounded domain, not a scan up to U*.
3. For u>=10000, HC implies K<1 at q>=u/8 (and q<u). Together with (1), the advantage transition can be decided by binary search of exact rational signs with fallback to exact count only in case N=B. Strict monotonicity in the complementary region q>u/8 remains open; (1) proves uniqueness of the sign transition for these budgets, allowing a possible tie before the permanent onset.

## Explicit residual payment

Use the HE cut after the q-th B (at start if q=0), with remaining A/B inventories a,b, x=t-r in {0,1}, t in {0,1}. All original safe words include the strip words. For u>=10000, q<=u/8, a<=5u/4+1, b>=3u, so a/(a+b)<=1/3. The HE image-kernel inequalities W+2>a+x+1 and 2(W+2)>b+x+1 hold since W=b-a+x+t. The four-binomial expression is exact for the strip. Its fraction T of all inventory words is at least 1-2*(7/16)=1/8 because each ratio R_j (j>=1) is nonnegative and bounded by R_1=a/(b+1)<=7/16, and the last term is nonnegative.

By the original HE corridor, a word excluded by the strengthened lower bound has a violating prefix after a_total>e=A-2q, hence prefix length after the cut >=u. A word excluded by the strengthened upper bound has a<q at violation, hence a reversed suffix length >=A-q>=u. Each violation requires more A than B in the corresponding segment. For length l of a uniform shuffle, the number X of A has E[2^X]<=(1+p)^l, p=a/(a+b)<=1/3, by the sampling-without-replacement factorial expansion. Markov yields Pr(X>l/2)<=(4/(3 sqrt(2)))^l<(19/20)^l. Sum l>=u and both directions: excluded fraction <=40*(19/20)^u. Divide by strip fraction >=1/8 and sum positive cut multiplicities: each original count is its strip count times (1+delta), 0<=delta<=eps=320*(19/20)^u. Thus (1+eps)^(-2)<=K/K0<=(1+eps)^2, giving |K-K0|<=3 eps K0 when eps<=1.

This is an observation-specific BRC residual payment: exact sign and adjacent comparisons descend under the paid quotient, not arbitrary joint-path observations. Retain original HE/HA path residuals for other observables.

## Polynomial certificates

Use H=u+2q+1,D=H+3u,J=3u+q, and HE's T(a,b;x,t)=1-R_(x+1)-R_(t+1)+R_(x+t+2), R_j=product_(i=0)^(j-1)(a-i)/(b+i+1). Set
s=T(H,3u;1,1)+q H/D T(H-1,3u;0,1),
p=H/(3u+1) T(H-1,3u+1;0,0),
r=(D+1)/(3u+1) T(H,3u+1;0,0).
Then K0=p*r*(J+1)^2/(s^2 H)=N/B with integer polynomials as constructed by the code below. B is the square of a polynomial and is positive in the strip by positivity of s. N and B have total degrees 9 and 10, absolute coefficient sums 966628 and 491752. Hence on 0<=q<=u, u>=1, N<=10^6 u^9 and B<=10^6 u^10 in the positive strip.

The derivative numerators G_u=N_u B-N B_u and G_q=N B_q-N_q B, after substituting u=8q+x, have 187 and 189 nonzero monomial coefficients respectively, all strictly positive. Neither specializes identically to zero on either nonnegative axis. Exact polynomial expansion checks this, so K0 strictly increases with real u and decreases with real q throughout the relevant continuous strip u>=10000, 0<=q<=u/8. The rational interpolation is used only for K0.

For integers, a nonzero N-B has absolute value at least 1. Also for any adjacent comparison of K0, the cross numerator is a nonzero integer of absolute value >=1. Multiplying the errors by the denominators, their sum is at most 6 eps 10^12 (u+1)^19 (using the smaller budget u and max <=u+1). This is <1 for u>=10000: the exact integer check at u=10000 is 6*320*10^12*10001^19*19^10000 < 20^10000, and 19*10002^19 <20*10001^19 proves the bound decreases thereafter. Thus signs and strict adjacent comparisons transfer to true K, without computing the huge original counts. No precision extrapolation is used.

## Sharp last-exception proof

Define F=N-B, E=324u+121887-(3q+169)^2, and U_e(q)=((3q+169)^2-121887+e)/324. E modulo 324 depends only on q mod 54; its possible least nonnegative residues are 54 distinct values, smallest 2, second smallest 11, largest 323. Residue 2 occurs only for q=38 mod 54. Consequently E never vanishes, positive E is either 2 or >=11, and negative E<=-1.

For each of these exact substitutions the following polynomials have 17 strictly positive coefficients in x:
 F(U_11(9000000+x),9000000+x);
 -F(U_-1(9000000+x),9000000+x);
 F(U_2(9529580+x),9529580+x).
All three boundary curves are within the real strip for q>=their displayed shifts: U_e(q)>=8q and >=10000 (immediate from the quadratic formula). The derivative sign in u therefore extends their signs to integer inputs with E>=11, E<=-1, and E>=2 respectively on the indicated q domains, as long as the input is in the strip.

Set q*=9529526, the largest q<9529580 in class 38 mod 54, and U*=U_2(q*)=2522581650951. At (U*,q*) exact polynomial sign F<0, despite E=2. At (U*,q*-1) F>0. At (U*+1,q*) F>0 and (U*+1,q*+1) F<0. The certificate below checks these four integer signs, and the strict residual payment transfers them to original K. The K0-1 values at the first two points are approximately +2.09875066065909167e-7 and -8.55395335111883841e-21 (display only). The last exception is an extremely small nonzero residual, whose sign is certified exactly.

For any u>U*, f=f(u)>=q*. Both f and f+1 are in the strip, since 6 sqrt(u+13543/36)<u/8 for u>=U* (square both positive sides). E(u,f)>0 and E(u,f+1)<0 because E cannot vanish. At f, if E>=11 use the first boundary certificate. If E=2, then f=38 mod 54, and f=q* would force u=U*, impossible. Therefore f>=q*+54=9529580 and the third certificate applies. At f+1 use the second certificate. Thus exact K(f,u)>1>K(f+1,u). Strict monotonicity extends the signs to all q in the strip. For q>u/8, HC's envelope K<144u/(q+5)^2<1 because sqrt(u)>=100>96. At U*, the two tested adjacent positions q*-1 and q* instead straddle the crossing, and the same monotonicity/envelope argument applies. This proves minimal permanent onset, not merely a sufficient upper bound.

## Executed exact reproduction (Python 3 / SymPy)

The following calculation was executed locally; all assertions passed. Polynomial coefficient counts: 187,189,17,17,17. Integer boundary signs +,-,+,-. No floating-point comparisons are used in proofs.

```python
import sympy as s
from math import isqrt
u,q,x,e=s.symbols('u q x e');H=u+2*q+1;D=H+3*u;J=3*u+q
def T(a,b,x,t):
    def R(k): return s.prod((a-j)/(b+j+1) for j in range(k))
    return 1-R(x+1)-R(t+1)+R(x+t+2)
S=T(H,3*u,1,1)+q*H/D*T(H-1,3*u,0,1)
P=H/(3*u+1)*T(H-1,3*u+1,0,0)
Q=(D+1)/(3*u+1)*T(H,3*u+1,0,0)
N,B=map(s.expand,s.fraction(s.factor(P*Q*(J+1)**2/(S*S*H))))
F=N-B
assert s.Poly(N,u,q).total_degree()==9 and s.Poly(B,u,q).total_degree()==10
assert sum(map(abs,s.Poly(N,u,q).coeffs()))==966628
assert sum(map(abs,s.Poly(B,u,q).coeffs()))==491752
for G,n in [(s.diff(N,u)*B-N*s.diff(B,u),187),(N*s.diff(B,q)-s.diff(N,q)*B,189)]:
    p=s.Poly(G.subs(u,8*q+x),x,q)
    assert len(p.terms())==n and all(c>0 for c in p.coeffs())
    assert p.eval(q,0).as_expr()!=0 and p.eval(x,0).as_expr()!=0
    print('derivative positive coefficients',n)
res=[(121887-(3*j+169)**2)%324 for j in range(54)]
assert len(set(res))==54 and min(res)==2 and sorted(res)[1]==11 and max(res)==323
assert res.index(2)==38 and res.index(323)==49
def U(q,e): return ((3*q+169)**2-121887+e)/324
p=s.Poly(F.subs(u,U(q,e)),q,e)
for E,sign,shift in [(11,1,9000000),(-1,-1,9000000),(2,1,9529580)]:
    c=s.Poly(sign*p.as_expr().subs({q:x+shift,e:E}),x).coeffs()
    assert len(c)==17 and all(v>0 for v in c)
    print('boundary positive coefficients',E,shift,len(c))
assert 6*320*10**12*10001**19*19**10000 < 20**10000
assert 19*10002**19 < 20*10001**19
qstar=9529526;Ustar=((3*qstar+169)**2-121887+2)//324
assert qstar%54==38 and qstar+54==9529580 and Ustar==2522581650951
assert (isqrt(324*Ustar+121887)-169)//3==qstar
for v,k,sign in [(Ustar,qstar-1,1),(Ustar,qstar,-1),(Ustar+1,qstar,1),(Ustar+1,qstar+1,-1)]:
    nv=N.subs({u:v,q:k});bv=B.subs({u:v,q:k});assert bv>0 and s.sign(nv-bv)==sign
    print(v,k,324*v+121887-(3*k+169)**2,s.N((nv-bv)/bv,18))
print('all certificates passed')
```

Actual output:
```
derivative positive coefficients 187
derivative positive coefficients 189
boundary positive coefficients 11 9000000 17
boundary positive coefficients -1 9000000 17
boundary positive coefficients 2 9529580 17
2522581650951 9529525 171532475 2.09875066065909167e-7
2522581650951 9529526 2 -8.55395335111883841e-21
2522581650952 9529526 326 3.96423513737553214e-13
2522581650952 9529527 -171532165 -2.09874603571428673e-7
all certificates passed
```

## Continuation

The eventual formula onset question is closed at author-proof scope, contingent on the stated HE/HC count/corridor identities; independent review remains pending. Do not rescan all budgets to 2.5e12. Next: classify the remaining finite pre-onset exceptions by the 54 residue classes, using polynomial sign intervals and a more accurate finite rounding rule; investigate whether F=0 has any integer solutions in the strip. Full-domain strict monotonicity outside the strip remains independent. No formal Result, shared Task claim, review or P000 change.

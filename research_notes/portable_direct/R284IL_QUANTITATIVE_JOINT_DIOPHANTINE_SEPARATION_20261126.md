# R284IL — Quantitative joint Diophantine separation and logarithmic critical-exception bound
2026-11-26. Author proof, NOT_REVIEWED. Independent continuation of own direct-research front; no shared Task claim or protected task-state change. Same auxiliary binary-tag safe-word total-count observer as IJ/IK, not a native physical attribution. P000 V5, joint relation and ACTIVE worldview retained. Current account entry blobs checked against main@40537c15383347592413adba2e77c19043682851. Own registration r1-20261124-0256-r284gd-session-v1 returned SUCCEEDED, session not closed, no runs; owner inventory r1-20261126-1203-owner-inventory RUNNING at last observation before publication. No live claim inferred.

Frozen inputs:
- IK: edf8d2a631c536cc4f7e9f4c94ed3fa77306c3bd:research_notes/portable_direct/R284IK_CRITICAL_EXCEPTION_EQUIDISTRIBUTION_20261126.md
- IJ: 75426bd0581d1826bfde31ac82cb5a632f53cc51:research_notes/portable_direct/R284IJ_THIRD_ORDER_CRITICAL_PROFILE_SHARP_EXCEPTION_SCALE_20261126.md
- ID monotonicity remains an author-level dependency through IJ/IK, not independent acceptance.

## Main result
Write s=s0, C=C0, Z=Z0, W=2Z/s and Q_n=A n^2+B n+C^2/s^2 with A=1/s^2, B=-2C/s^2. There exists a fixed K>0 such that for every positive integer T,
max(||TA||,||TB||) >= exp(-K T log(T+2)).
Here ||.|| denotes distance to the nearest integer. This is simultaneous separation, without a hypothesis about the irrationality of either particular coefficient.

For the interval discrepancy D_M of {Q_n}, n=1,...,M, we prove
D_M = O((log log M / log M)^(1/3)).
Combining the actual IJ sign band with this estimate gives, as X tends to infinity,
N_3(X) = O(sqrt(X) (log log X / log X)^(1/3)),
N(X) = 2Z sqrt(X) + O(sqrt(X) (log log X / log X)^(1/3)).
N is the number of failures of the II two-term ceil rule, N_3 counts actual failures (and is bounded by the same count of possible sign-ambiguous positions) of the IJ three-term ceil rule. Minimum-budget interpretation uses ID. The constants in these asymptotic estimates are not numerically optimized; no explicit finite validity threshold for true-K rounding is claimed.

## 1. An elementary exponential rational separation lemma
Fix 0.4<=t=a/b<=0.6 with positive integers a,b, and any rational v/d with positive denominator d. There is an absolute K1>0 such that
|exp(t)-v/d| >= exp(-K1 (b+log(d+2)) log(b+log(d+2)+2)).
Proof: for integer j>=1 put f(x)=x^j(a-bx)^j/j! and J=int_0^t exp(x) f(x) dx. Define F=sum_{i=0}^{2j} (-1)^i f^(i); F+F'=f. Therefore J=U exp(t)-V where U=F(t), V=F(0). All endpoint derivatives are integers: for i<j they vanish; for i=j+k, k=0,...,j, the coefficient of x^(j+k) in j!f about 0 equals binom(j,k)a^(j-k)(-b)^k; about t the coefficient of (x-t)^(j+k) equals (-1)^j binom(j,k)a^(j-k)b^k. Multiplication by (j+k)!/j! preserves integrality.
Choose j=ceil(4b+log_2(4d)+2). Since t<=1, x(a-bx)<=b/4 and j!>=(j/e)^j, 0<J<=e (e b/(4j))^j < 1/(2d). On [t/4,3t/4], x(a-bx)=b x(t-x)>=b/100; interval length >=1/5. Thus J >= (b/100)^j/(5 j!). Also |U| <= (j+1) 2^j b^j (2j)^j by the endpoint derivative formula and a<=b. In particular log(max(1,|U|))=O(j log(b+j+2)), and J>=exp(-O(j log(j+2))). U is nonzero since otherwise J is a nonzero integer of size <1.
If Uv/d-V differs from zero, its absolute value is at least 1/d, so |U| |exp(t)-v/d| >=1/(2d). If it equals zero, |U| |exp(t)-v/d|=J. Combining proves the lemma, with constants uniform over the declared rational t interval. This supplies a quantitative substitute for the qualitative Hermite–Lindemann branch in IK, using an integral with its endpoint difference retained, not assuming any algebraic nature of s.

## 2. Joint separation via the exact endpoint coordinate
Set z=s^2. From IK's exact eliminated N/P formula,
C=(n_e+n_f rho)/(8(p_e+p_f rho)), rho=exp(-z/2),
n_e=40z^3-470z^2+1179z+328,
n_f=364z^3-1068z^2+1069z-328,
p_e=60z^2+8z+13,
p_f=78z^2-73z-13.
The determinant n_e p_f-n_f p_e=-3z(6z-13)(1040z^3+1054z^2-1351z-1296) is nonzero by the certified IK interval .93<z<.94. Hence
exp(z/2)=R(z,C)=(8C p_f-n_f)/(n_e-8C p_e)
with denominator nonzero at the actual (z,C). Indeed n_e-8C p_e=rho(8C p_f-n_f); simultaneous vanishing would contradict the determinant. Choose a fixed small compact neighborhood on which the denominator is separated from zero, z/2 is in [0.4,0.6], and R is Lipschitz. The neighborhood exists by continuity and can in principle be certified from rational enclosures.

For integers T>=1 choose nearest integers p,l to TA,TB; let eta=max(|TA-p|,|TB-l|). If eta/T is small enough, p>0, p and |l| are O(T), and
z'=T/p, C'=-l/(2p), |z'-z|+|C'-C|=O(eta/T).
Then R(z',C') is a rational whose height is O(T^3): multiplication of numerator and denominator by p^3 yields integer homogeneous cubics in T,p,l. The exponent t'=z'/2 has denominator <=2p=O(T). The mean value theorem and Lipschitz R give
|exp(t')-R(z',C')| <= K2 eta/T.
The lemma gives the opposite lower bound exp(-K3 T log(T+2)), since log of the denominator of R is O(log(T+2)). Absorb factors to obtain eta>=exp(-K T log(T+2)). If eta/T is outside the small neighborhood criterion the bound holds after enlarging K. For the finitely many remaining T, eta>0 follows by IK (or by the same exponential lemma if eta=0); enlarge K again. This proves the asserted simultaneous lower bound, retaining BOTH A and B. A lower bound on either individual coefficient has not been established.

## 3. Quantitative discrepancy: frequency-dependent resonance budget
Use e(x)=exp(2pi i x) for ordinary external Fourier estimates on the auxiliary integer sequence. The constant term of Q_n only rotates its sums. For integer M sufficiently large take L=c log(M)/log log(M) with small fixed c>0 such that K (2L)log(2L+2)<= (log M)/8. Let H0=floor(L^(1/3)). For 1<=h<=H0 put H=floor(L/h), alpha=hA, beta=hB, and S_h=sum_{n=1}^M e(alpha n^2+beta n). Then H>=1, H<=M, and we show |S_h|/M=O(sqrt(h/L)) uniformly.

If every 1<=k<=H has ||2k alpha||>=M^(-1/2), each shift correlation is a geometric sum of size O(M^(1/2)); van der Corput differencing gives |S_h|^2/M^2=O(1/H+M^(-1/2)).
Otherwise take one k with ||2k alpha||<M^(-1/2), r=2k, p nearest integer to r alpha, delta=alpha-p/r. Then r<=2H, hr<=2L and |delta|<M^(-1/2)/r. Split n into residues a mod r. The rational quadratic p n^2/r is constant modulo 1 on each residue, so the remaining phase for n=a+rj is delta(a+rj)^2+beta(a+rj).
- If |delta|>=M^(-3/2), its second derivative in j has size 2|delta|r^2. The standard second derivative estimate, summed over residues, gives |S_h|/M=O(r sqrt(|delta|)+1/(M sqrt(|delta|)))=O((1+sqrt(r)) M^(-1/4)). (Each progression has length O(M/r); endpoint O(1) terms can be absorbed in this bound.)
- If |delta|<M^(-3/2), joint separation for T=hr implies max(||r alpha||,||r beta||)>=M^(-1/8). The first term is <=r M^(-3/2), so ||r beta||>=M^(-1/8). The derivative in j is r beta+2delta r(a+rj); its drift on n in [1,M] has size at most 2r M^(-1/2)=o(M^(-1/8)). It is monotone and lies within a single unit interval at distance >=M^(-1/8)/2 from integers. The first derivative (Kusmin–Landau) estimate gives O(M^(1/8)) per residue, hence |S_h|/M=O(r M^(-7/8)).
All polynomially decaying terms are uniformly smaller than sqrt(h/L) because r<=2L. Erdős–Turán for interval discrepancy now yields
D_M <= O(1/H0 + sum_{h<=H0} |S_h|/(h M))
     = O(L^(-1/3) + L^(-1/2) sum_{h<=H0} h^(-1/2))
     = O(L^(-1/3)).
The dependence H=floor(L/h), rather than a common shift budget, removes a superfluous logarithmic loss. These external classical estimates are applied to this arithmetic observer only, not a native geometry assertion. Standard estimates checked against “On van der Corput's k-th derivative test for exponential sums”, Indagationes Mathematicae 27 (2016), 559–589, https://doi.org/10.1016/j.indag.2015.11.009 ; Erdős–Turán background: https://arxiv.org/abs/0903.1834 (Martin–Sitar).

## 4. True-K exception accounting
IJ gives strict sign outside H1/q about T(q)=s sqrt(q)+C+Z/sqrt(q), for a finite H1. With q~Q_n and |T(q)-n|<=H1/q, multiplying by sqrt(q) and using the exact difference of square roots first gives q=Q_n-W+O(1/n). Conversely the II failure sandwich has lower endpoint Q_n-W+O(1/n) and exact upper endpoint Q_n: in the bounded-width band, sqrt(q)(n-(s sqrt(q)+C))=(s/2)(Q_n-q)+O(1/q), and the sign tolerance after multiplication is H1/sqrt(q)=O(1/n). This sharpens the fixed-epsilon IJ/IK sandwich. Thus actual II failure counts agree with counts of integers in (Q_n-W,Q_n] except possibly at integers within O(1/n) of Q_n-W; any equality at that endpoint is included in the ambiguous set. The intervals for distinct large n are disjoint, and each has O(1) integers. The final incomplete band and fixed initial segment change counts by O(1).
For M large, on each dyadic block M/2<n<=M, a candidate shrinking band contains at most one integer eventually and only if dist(Q_n-W,Z_integers)<=K4/M. The interval discrepancy for the two prefixes bounds the count by O(1+M D_M+(M/2)D_floor(M/2)); sum over dyadic blocks (or first discard n<=sqrt(M), then use comparable log M for larger blocks). This is O(M (log log M/log M)^(1/3)). It bounds both three-term candidate exceptions and differences between true two-term failure counts and ideal band counts.
The exact ideal count for (Q_n-W,Q_n] is floor(W)+1_{frac(Q_n)<frac(W)}. Its sum is MW+O(M D_M), with endpoint conventions as above. For q<=X, M=s sqrt(X)+O(1) complete bands, so the two asserted quantitative exception bounds follow. This is an unconditional rate relative to the fixed IJ and ID proof dependencies, with no extra Diophantine conjecture.

## 5. Author checks actually executed
Local Python/SymPy exact symbolic check of determinant and homogeneous cubics, plus 40 exact endpoint-integrality and antiderivative checks (a,b)=(1,2),(2,5),(3,7),(4,9),(5,11), j=1..8. Output:
det: -3*z*(6*z - 13)*(1040*z**3 + 1054*z**2 - 1351*z - 1296)
homogeneous numerator: -364*T**3 - 312*T**2*l + 1068*T**2*p + 292*T*l*p - 1069*T*p**2 + 52*l*p**2 + 328*p**3
homogeneous denominator: 40*T**3 + 240*T**2*l - 470*T**2*p + 32*T*l*p + 1179*T*p**2 + 52*l*p**2 + 328*p**3
integral certificate exact cases: 40
Reproduction:
```python
import sympy as S
z,p,T,l=S.symbols('z p T l')
ne=40*z**3-470*z**2+1179*z+328
nf=364*z**3-1068*z**2+1069*z-328
pe=60*z**2+8*z+13
pf=78*z**2-73*z-13
print('det:',S.factor(ne*pf-nf*pe))
for v in [-4*l/p*pf-nf, ne+4*l/p*pe]:
    print('homogeneous:',S.expand(p**3*v.subs(z,T/p)))
x=S.symbols('x'); cases=0
for a,b in [(1,2),(2,5),(3,7),(4,9),(5,11)]:
 for j in range(1,9):
    f=x**j*(a-b*x)**j/S.factorial(j)
    F=S.expand(sum((-1)**k*S.diff(f,x,k) for k in range(2*j+1)))
    assert S.expand(F+S.diff(F,x)-f)==0
    assert F.subs(x,0).is_Integer and F.subs(x,S.Rational(a,b)).is_Integer
    cases+=1
print('integral certificate exact cases:',cases)
```
These finite checks support the algebra; the unbounded estimates use the written proof, not an extrapolation. No true-K point was recomputed this turn.

## Next
Improve the simultaneous bound, e.g. exploit the rational-curve endpoint constraints in sharper Padé or linear-form estimates, or seek a polynomial lower bound on joint resonance. A power discrepancy saving and O(log X)/O(X^epsilon) rounding exception bounds remain open. Independently extract explicit uniform IJ remainder and test the resulting sparse fallback certificate; no repeat of ID's completed enumeration unless a specific review defect appears. ID independent review remains pending.

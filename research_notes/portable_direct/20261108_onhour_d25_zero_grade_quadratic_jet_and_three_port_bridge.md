# D25 — Original 216/2304 grade-zero quadratic p-adic jet and full three-grade carry

Date: 2026-11-08 (Asia/Hong_Kong).
Scope: author-side exact mathematics, UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Frozen Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3.
Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923.

## Original objects and carrier

For prime p>3 and 0<=n<p,
\[
w_n=(6n+1)\frac{(2n)!(3n)!}{(n!)^5 216^n},\qquad
v_n=(8n+1)\frac{(4n)!}{(n!)^4 2304^n}.
\]
The valuation grade is assigned to the coefficient BEFORE its optional linear weight. BRC reuse: COMPOSE_APPLIED with a signed tuple (model,index,grade,weight,base binomial,first harmonic,second harmonic), retained until the specified mod-p^3 sum observer. This is not a positive-branch mass interface.

Their hypergeometric parameter lists are a_W=(1/2,1/3,2/3), base b_W=2 and weight g_W(n)=6n+1; a_V=(1/4,1/2,3/4), base b_V=9 and g_V(n)=8n+1:
\[
w_n=g_W(n)2^{-n}\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3},\quad
v_n=g_V(n)9^{-n}\frac{(1/4)_n(1/2)_n(3/4)_n}{(n!)^3}.
\]
In particular, the V base is **9**, not 36.

## Theorem 1: exact second-order binomial/harmonic evaluator of the original zero-grade port

For every a=A/d in the appropriate parameter list choose unique r_a in {0,...,p-1} and lambda_a in Z_(p) by
\[
A+d r_a\equiv0\pmod p,\qquad
\lambda_a=(A+d r_a)/(dp),\qquad
a=-r_a+p\lambda_a.
\]
Define N_W=floor((p-1)/3) and N_V=floor((p-1)/4). For either X=W,V, N_X=min_a r_a and 0<=n<=N_X entails n<=r_a for all a. Put
\[
h_a(n)=\sum_{j=0}^{n-1}(r_a-j)^{-1},\qquad
h_a^{(2)}(n)=\sum_{j=0}^{n-1}(r_a-j)^{-2},
\]
\[
D_X(n)=\sum_{a\in a_X}\lambda_a h_a(n),\quad
E_X(n)=\sum_{a\in a_X}\lambda_a^2 h_a^{(2)}(n),\quad
b_{X,n}=g_X(n)(-1)^n b_X^{-n}\prod_{a\in a_X}{r_a\choose n}.
\]
Define three port sums:
\[
\mathcal A_X=\sum_{n=0}^{N_X}b_{X,n},\quad
\mathcal J_X=\sum_{n=0}^{N_X}b_{X,n}D_X(n),\quad
\mathcal K_X=\frac12\sum_{n=0}^{N_X}b_{X,n}(D_X(n)^2-E_X(n)).
\]
Then the actual original grade-zero sum X_0 satisfies for **every prime p>3**
\[
\boxed{X_0\equiv\mathcal A_X-p\mathcal J_X+p^2\mathcal K_X\pmod{p^3}.}\tag{1}
\]
It suffices to evaluate A modulo p^3, J modulo p^2, K modulo p. All displayed inverses are p-units.

Proof: For n<=r_a,
\[
(a)_n=(-r_a)_n\prod_{j=0}^{n-1}(1-p\lambda_a/(r_a-j)).
\]
The product over the three parameters and j, modulo p^3, is
\[
1-pD_X(n)+\tfrac{p^2}{2}(D_X(n)^2-E_X(n)).
\]
The three integer Pochhammer factors satisfy
\[
\prod_a(-r_a)_n=(-1)^n(n!)^3\prod_a{r_a\choose n}.
\]
Insert this expression termwise, then sum. The least r for parameters (1/3,2/3) equals floor((p-1)/3); for (1/4,3/4), floor((p-1)/4), establishing the exact grade-zero interval. QED.

If W_0-V_0 is divisible by p, (1) also gives its **second** carry digit:
\[
\boxed{c_0=(W_0-V_0)/p\equiv
(\Delta\mathcal A)/p-\Delta\mathcal J+p\Delta\mathcal K\pmod{p^2}.}\tag{2}
\]
Here Delta denotes W minus V, and Delta A must be represented mod p^3 before taking its integral quotient. The quadratic term is necessary to evaluate c0 mod p^2.

## Theorem 2: source-preserving three-grade bridge

Consume the earlier exact first-grade Wilson/harmonic formula from
research_notes/portable_direct/20261108_onhour_d25_wv_grade_one_wilson_harmonic_two_carry.md:
\[
X_1/p\equiv B_X+p(H_X-\omega_p B_X)\pmod{p^2},
\quad \omega_p=((p-1)!+1)/p\pmod p.
\]
Here B_X is the previous signed p-local base sum and H_X its previous weighted local harmonic correction. Let tau_X=X_2/p^2 mod p be the actual third-grade source port. Then, **unconditionally for all primes p>3**,
\[
\boxed{
W_p-V_p\equiv
\Delta\mathcal A+p(\Delta B-\Delta\mathcal J)+
p^2(\Delta\mathcal K+\Delta H-\omega_p\Delta B+
\tau_W-\tau_V)\pmod{p^3}.}\tag{3}
\]
Proof: The grades of the original coefficients for n<p are respectively floor(2n/p)+floor(3n/p) and floor(4n/p). All grades >=3 vanish mod p^3. Apply (1), the earlier first-grade formula, and the actual third-grade sources; the identity follows by labeled addition. QED.

Previously proved/source-derived inputs:
- Guo–Zudilin double-truncation gives the **aggregate** tau_V=0 for p>3 (see 20261108_onhour_d25_2304_grade2_tail_universal_zero.md; Adv. Math. 346 (2019), arXiv:1803.01830).
- The independent original-W signed tail kernel gives
\[
\tau_W\equiv\frac19\left(\frac6p\right)
\sum_{r=0}^{\lfloor(p+4)/6\rfloor-1}
(6r+4)\frac{(1)_r(5/6)_r(7/6)_r}
{(3/2)_r^3 2^r}\pmod p.
\tag{4}
\]
Therefore (3)-(4) are an explicit finite integer-binomial/harmonic/3F2 reduction of the remaining W216/2304 three-digit correspondence; they do not establish its unproved universal vanishing.

If Delta A=0 mod p, define
\[
d=(\Delta\mathcal A)/p+\Delta B-\Delta\mathcal J\pmod{p^2}.
\]
The full correspondence is equivalent to the **ordered** modular tests
\[
\boxed{d\equiv0\pmod p,\quad
d/p+\Delta\mathcal K+\Delta H-\omega_p\Delta B+\tau_W
\equiv0\pmod p.}\tag{5}
\]
Only divide d after the first test. Since the published V result is V_p=p(-3/p) mod p^3, proving (5) uniformly proves the corresponding W conjecture in that domain; in the frozen p=13,19 mod24 classes (-3/p)=+1.

## Executed certificates

Companion independent checker: research_notes/portable_direct/d25_zero_grade_second_jet_check_20261108.py. Standard Python exact modular integers, run on **all 301 primes 5<=p<=2000**. For both original models, each grade-zero term was compared modulo p^3 to an independently formed original factorial coefficient; 602 complete zero-grade evaluations and their termwise checks passed. The existing first-grade Wilson/harmonic term and independent signed hypergeometric tail reproduce zero W/V difference on all 301 primes (a finite observation). At p=5,11,13,19,37,373 a further original **all-grades binomial** path independently verified the total and grade-two source.

Numerical witnesses; Delta A modulo p^3; Delta J/Delta B modulo p^2; Delta K/Delta H/tau modulo p:

| p | Delta A | Delta J | Delta K | Delta B | Delta H | omega | tau_W | d/p | correction mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 845 | 17 | 12 | 108 | 5 | 0 | 10 | 12 | 1 |
| 19 | 4864 | 66 | 7 | 323 | 14 | 2 | 9 | 27 | 11 |
| 373 | 17893183 | 88258 | 359 | 36930 | 56 | 224 | 266 | -9 | 9 |

For p=13, d=845/13+108-17=156=12*13, and 12+1=0 mod13. For p=19, d=27*19 and 27+11=0 mod19. For p=373, d=17893183/373+36930-88258=-3357=-9*373; its four second correction terms are 359,56,-224*36930,266, summing to 9 mod373. Thus -9+9=0.

The independently computed original p373 zero-grade terms are W0=28094360 and V0=45069217 mod p^3. Their A/J/K summaries are W=(15521276,136007,82) and V=(49523210,47749,96), reduced mod (p^3,p^2,p). The original p373 complete totals remain W373=V373=373 mod p^3.

The all-prime identities (1) and (3) are proved by finite polynomial algebra; the all-prime vanishing of (5) remains an open scientific step.

## Durable frontier and source separation

Next exact mathematics: seek a terminating binomial / Fricke–Cartier proof or an exact falsifier of (5), first testing structural relations among Delta A, Delta J, the second-harmonic Delta K, the Wilson correction and tau. A Wilson-free simplification has a live discriminating witness at p=373: omega=224 and Delta B=36930=3 mod373, so the Wilson term is nonzero modulo p.

Frozen mother objective: Delta_p-R_p=0 mod p and W_p=p mod p^3 for p=13,19 mod24. D24 RR-AC9B3BA5BD277CE043F5 remains frozen/accepted and is not rerun.

Original native p373 same-class H0/B0 divided-power [X]U mod139129, actual module rank, semilinear Frobenius direction/eta, signed Green/Hesse kappa, Delta-R and independent reproduction are **PENDING_OWNER / NOT_EXECUTED** at issue #1559. This standard-Python binomial work is not that benchmark.

2026-11-08 ~07:02 UTC original request onhour11-20261106-1400-exact-research-lane-continuation read WAITING_RESOURCE / EVENT_COLLECTION_IO / formal_task_created=false. Site diagnostics: CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Native session/claim/run NOT_VERIFIED; Source checkpoint NOT_WRITTEN. Old staging is separate. Retain the original request and next reconcile condition; no maintenance-lane identity.

# D25: even-degree Legendre port and exact p² Gauss valuation split

2026-11-01. AUTHOR-SIDE / PROVED WITH PUBLISHED THEOREM / EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED. Task SECOND-DIGIT-LIFT. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Reuse previous odd-degree port in project commit 42da097851a02b96f8ff2018f5c28096eec13866; mathematical novelty here is the previously missing p=1,3 mod8 branch and its p² obstruction, notably p=19 mod24.

## Exact carrier and observer

For a prime p>3 and 0<=k<p, use p-integral rational quantities

\[
c_k=\frac{(1/8)_k(3/8)_k}{(k!)^2},\quad F_p(z)=\sum_{k=0}^{p-1}c_kz^k,\quad \beta_k=c_k9^{-k},
\]
\[
G_p=F_p(1/9),\quad H_p=[(1+16z\partial_z)F_p(z)]_{z=1/9},
\]
\[
B_p=\sum_{k=0}^{p-1}(8k+1)\frac{\binom{4k}{2k}\binom{2k}{k}^2}{2304^k}.
\]
The signed Clausen overflow is
\[
T_{\beta,p}=\sum_{0\le i,j<p,\ i+j\ge p}(8(i+j)+1)\beta_i\beta_j.
\]
The classical Clausen power-series identity, together with (1+8zD)F(z)^2=F(z)(1+16zD)F(z), gives the exact rational equation
\[
\boxed{B_p=G_pH_p-T_{\beta,p}.}
\]
Its coefficients below p agree with the complete hypergeometric expansion; all higher i+j form precisely the displayed signed overflow. No boundary was dropped.

## Theorem 1: uniform finite Legendre port, both parity branches

Let n=(p-1)/4 if p=1 mod4 and n=(p-3)/4 if p=3 mod4. Then for p=1,3 mod8, n is even and
\[
\boxed{F_p(z)\equiv P_n(\sqrt{1-z})\pmod p\quad\text{in }\mathbf F_p[z].}
\]
The right side is an ordinary polynomial of degree n/2, constant term 1. For p=5,7 mod8, n is odd and the already published companion theorem is
\[
F_p(z)\equiv(1-z)^{(p+1)/2}\frac{P_n(\sqrt{1-z})}{\sqrt{1-z}}\pmod p.
\]
Together these cover every prime p>3 and restore the original p=19 mod24 branch.

Proof of the even case: the coefficients satisfy (k+1)^2 c_{k+1}=(k+1/8)(k+3/8)c_k. The corresponding operator is
\[
L=z(1-z)D^2+(1-\tfrac32 z)D-\tfrac3{64}.
\]
For y=P_n(sqrt(1-z)), the Legendre equation yields
\[
[z(1-z)D^2+(1-\tfrac32 z)D]y=-n(n+1)y/4.
\]
Because n=-1/4 or -3/4 modulo p, n(n+1)/4=-3/64 modulo p, so Ly=0 modulo p. Both polynomials have constant coefficient 1 and degree <p. The coefficient recurrence has invertible denominator (k+1)^2 for k+1<p, proving all coefficients agree. This proof is universal in its stated residue classes; the 2026-10-31 source gives the odd-degree/Frobenius-twist proof.

## Theorem 2: source-wise overflow vanishes to p² for every even n

For each p=1 mod8 the indices r1=(p-1)/8 and r3=(3p-3)/8, both below p/2, satisfy 8r1+1=p and 8r3+3=3p. For p=3 mod8 the indices r3=(p-3)/8 and r1=(3p-1)/8 similarly satisfy 8r3+3=p and 8r1+1=3p. Thus each Pochhammer product for k>p/2 includes two p factors; all denominators for k<p are p-units. In particular
\[
v_p(\beta_k)\ge2\quad\text{if } k\ge(p+1)/2,\quad p=1,3\pmod8.
\]
Each pair i+j>=p necessarily has at least one index >=(p+1)/2. This proves term by term, including signs and multiplicities,
\[
\boxed{T_{\beta,p}\equiv0\pmod{p^2}\qquad(p=1,3\pmod8).}
\]

## Theorem 3: the selected p²-zero strategy is impossible for the p=19 mod24 target

Guo–Zudilin, A q-microscope for supercongruences, Advances in Mathematics 346 (2019), 329–358, DOI 10.1016/j.aim.2019.02.008, arXiv:1803.01830, prove for every p>3
\[
B_p\equiv p\chi_{-3}(p)\pmod{p^3}.
\]
Combining that published theorem with the exact signed equation and Theorem 2 gives
\[
\boxed{G_pH_p\equiv p\chi_{-3}(p)\pmod{p^2},\quad p=1,3\pmod8.}
\]
Since chi is +/-1, v_p(GH)=1: exactly one factor has valuation 1 and the other is a p-adic unit. Neither G nor H can vanish modulo p². This is a universal theorem (with the published Guo–Zudilin result as an explicit input), not an experimental conjecture.

Every p=19 mod24 has p=3 mod8 and chi=+1; therefore G_pH_p=p modp². The earlier character-selected p²-vanishing conjecture was explicitly restricted to p=5,7 mod8 and cannot be extended to the p=19 mod24 part of D25. In contrast the original p=13 mod24 target has p=5 mod8, where the earlier p²-vanishing conjecture remains an open candidate. **The two original target classes need different p-adic proof routes.** The p=19 class must retain a nonzero first lift and its signed boundary rather than seek an annihilated Gauss product.

## Exact p=19 witness and typed first-lift defect

Here n=4 and
\[
P_4(\sqrt{1-z})=1-5z+\tfrac{35}{8}z^2\equiv1+14z+2z^2\pmod{19}.
\]
At z0=1/9 its exact rational value is 323/648 =19*17/648; after division by 19 its residue is 18 mod19. Full original finite beta coefficients give
\[
G_{19}=171=9\cdot19,\quad H_{19}=131,\quad B_{19}=19,\quad T_{\beta,19}=0\pmod{19^2}.
\]
Thus the exact beta-specific coefficientwise defect
\[
D_{\beta,19}(z)=\frac{F_{19}(z)-P_4(\sqrt{1-z})}{19}
\]
is 19-integral and has D_beta(1/9)=10 mod19. Its observer combines the Legendre first lift 18 with defect 10 to give G_19/19=9 mod19, genuinely nonzero. H_19=17 mod19 is a unit. Further exact finite examples: G_43=860=20*43, G_67=938=14*67, G_139=9591=69*139 modulo their respective p². These examples do not claim a class-wide identification of which factor vanishes modp.

## Actually executed exact certificate and frontier

The standard-library Python program d25_even_legendre_port_20261101.py completed exact modular checks for every one of the 93 primes 5<=p<=499: the characteristic-p Legendre polynomial coefficients in all four residue classes; independent B hypergeometric recurrence and signed Clausen overflow computed from suffix moments modulo p²; the p² consequence of the published B theorem; source-wise beta tail and exact-order-one factor test for all 44 even-n primes; and a p=19 defect witness. The other 49 odd-n primes constitute a scoped regression of the previously proved formula. The all-prime theorems are established by the arguments above, not by the finite checks.

Parent D25 goal remains A_p=p modp³ for p=13,19 mod24, with stronger A_p-2B_p+p*chi_{-3}(p)=0 modp⁴ an unproved conjecture. Next exact mathematical action: for the p=19 mod24 branch prove CM/finite-field character selection of the **mod-p** Legendre zero and determine the nonzero p-linear Gauss coefficient and the p³ boundary/216 affine difference. For p=13 mod24, continue the distinct beta-defect/carry p² cancellation. The existing native issue #1559 for fixed p373 original H0/B0 divided-power, genuine semilinear Frobenius/rank, signed Green/Hesse/kappa and independent replication remains NOT_EXECUTED/PENDING_OWNER; scalar beta computation is not native acceptance.

Control provenance: ordinary Research logical ID chatgpt-research-onhour-enterprise-math-20260923; never the maintenance conversation. Original recovery request research-onhour-20261031-0202-recovery-r15 in awdawmip/kimi-query-bridge#6632 had no winning CLAIM/run; original dispatch research-onhour-20261031-0205-dispatch-r15 in #6633 ended FAILED/UPSTREAM_CODE_REVIEW_REQUIRED, not retried. Native Research-Activity REGISTER_PENDING, SOURCE_CHECKPOINT_PENDING, no role-bound Result/review. This neutral author-side mathematical preservation does not create any native session, CLAIM, Source promotion or independent review. P000/ACTIVE worldview and frozen scientific Source pin unchanged.
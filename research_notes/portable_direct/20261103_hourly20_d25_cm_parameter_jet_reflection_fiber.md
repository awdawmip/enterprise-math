# D25 — CM parameter two-jet and a reflection-fiber separation certificate

Date: 2026-11-03 (+08). Role: TASK_RESEARCH, logical Research lane \`chatgpt-research-hourly-enterprise-math-20260923\`; distinct maintenance lane \`chatgpt-hourly-enterprise-math-20260921\`. This is **author-side mathematics, HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, frozen scientific input pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.

## Source frontier and question

Consume, without recrediting, (i) accepted D24 finite CM0 for primes p ≡13,19 (mod24), (ii) the original finite Clausen/Gauss identities and Gauss single-root author proof, and (iii) sibling reciprocal-index three-atom theorem at \`20261103_hourly20_d25_reflection_three_port_universal_measure.md\`. The concurrent onhour sibling \`20261103_onhour_d25_original216_coupled_finite_hensel_ode.md\` treats a different terminating Hensel parameter jet; its original weighted coefficient sources are preserved. This note studies **variation of the original 216 argument** and the information retained by reflected products.

For prime p=6r+1 with p ≡13 or 19 (mod24), work over Z_(p). Put

\[
b_k=\binom{2k}k^2\binom{3k}k216^{-k},\quad
F_p(t)=\sum_{k=0}^{p-1}b_kt^k,\quad
W_p(t)=\sum_{k=0}^{p-1}(6k+1)b_kt^k=(1+6\theta_t)F_p(t),
\quad \theta_t=t\,d/dt.
\]

For p-integral index weight w(k), set
\[
C_p(w;t)=\sum_{k=0}^{p-1}w(k)(b_kt^k)(b_{p-1-k}t^{p-1-k}).
\]
Retain the exact index, reflection pairing, valuation, argument lift, and signed weights as typed source fields.

Let \(\ell_r(z)=\sum_{k=0}^{r}\binom rk\binom{2r}kz^k={}_2F_1(-r,-2r;1;z)\).
The existing CM0 input gives \(\ell_r(1/2)=0\) mod p. Define \(j=(\theta_z\ell_r)(1/2)\) mod p.

## Theorem A — exact first and second argument jets at CM0

Define the p-integral finite sums
\[
D_p=(\theta_t W_p)(1)=\sum k(6k+1)b_k,\qquad
T_p=((\theta_t^2-\theta_t)W_p)(1)=\sum k(k-1)(6k+1)b_k.
\]
Then for every prime p in the stated classes,
\[
\boxed{D_p\equiv12j^2,\qquad T_p\equiv8j^2\pmod p,\qquad j\not\equiv0\pmod p.}
\]

**Proof.** The exact Clausen hypergeometric identity
\[
{}_3F_2(1/2,1/3,2/3;1,1;z)
={}_2F_1(1/6,1/3;1;z)^2
\]
gives a coefficientwise congruence in F_p[t]:
\[
F_p(t)\equiv\ell_r(t/2)^2\pmod p.
\]
Indeed the finite Gauss series mod p stops at k=r since 1/6 ≡-r and 1/3≡-2r; the finite 3F2 stops at k=2r since 1/3≡-2r; all relevant denominators k! for k<p are p-units and 2r<p. This is a polynomial identity, not an infinite truncated series assumption.

Write G(t)=\ell_r(t/2), so G(1)=0; j=(theta G)(1). Applying the Gauss equation
\[
[\theta_z^2-z(\theta_z-r)(\theta_z-2r)]\ell_r=0
\]
at z=1/2 gives \(h=(\theta^2G)(1)\equiv-3rj\equiv j/2\pmod p\).
The product derivatives at the CM zero are
\[
\theta(G^2)=0,\qquad\theta^2(G^2)=2j^2,\qquad
\theta^3(G^2)=6jh=3j^2.
\]
Therefore
\[
D_p=[\theta+6\theta^2]F_p(1)\equiv12j^2,
\]
\[
T_p=[6\theta^3-5\theta^2-\theta]F_p(1)
\equiv18j^2-10j^2=8j^2\pmod p.
\]
To show \(j\ne0\), if both \(\ell_r(1/2)\) and its first derivative vanished, the regular Gauss differential equation at z=1/2, whose leading coefficient is nonzero, forces consecutive Taylor coefficients through degree r to vanish (division by integers 1,...,r<p is permitted). This contradicts \(\ell_r(0)=1\) and deg \(\ell_r=r<p\). QED.

## Theorem B — reflection fiber and minimum deformation-sensitive port

For every p-integral weight w(k) and every p-adic unit t,
\[
\boxed{C_p(w;t)\equiv C_p(w;1)\pmod{p^3}.}
\]
For any \(\lambda\in\mathbb Z_{(p)}\), the original weighted readout satisfies
\[
\boxed{W_p(1+p\lambda)-W_p(1)
\equiv p\lambda D_p+4p^2\lambda^2j^2\pmod{p^3}}
\]
and hence
\[
\boxed{W_p(1+p\lambda)-W_p(1)
\equiv12p\lambda j^2\pmod{p^2}.}
\]
When \(\lambda\) is a p-unit, the latter difference has exact p-adic valuation one.

**Proof.** Each reflected pair has product \(b_kb_{p-1-k}t^{p-1}\). The earlier reciprocal-index valuation theorem gives \(v_p(b_kb_{p-1-k})\ge2\) for every k. Fermat's theorem yields \(t^{p-1}\equiv1\pmod p\), so every paired term is invariant modulo p^3 (independently of w). Taylor-expand \(t^k=(1+p\lambda)^k\) through quadratic order, sum with the original factor (6k+1), and use Theorem A to reduce T_p/2 to \(4j^2\) modulo p. The last claim follows from the nonzero j proved above. QED.

**Exact observer-safety certificate.** Fix the reflected-source observation family \(\{C_p(w;t)\pmod{p^3}: w\text{ p-integral and independent of the lift }t\}\), supplemented by t mod p, but not by the lifted parameter t mod p². The two source states \(t=1\) and \(t=1+p\) have identical values for every such observer, yet \(W_p(t)\pmod{p^2}\) differs by \(12pj^2\ne0\). Therefore **no readout factoring solely through that declared reflected-observer family plus t mod p can reconstruct \(W_p(t)\pmod{p^2}\) uniformly over both states**. This is an exact fiber-nonconstancy/descent obstruction for the stated observer and future-operation horizon. It does not constrain additional source-sensitive CM/WZ operators or the special fixed t=1 target.

The missing information can be provided by the typed parameter-lift \(\lambda\) and the oriented Gauss derivative \(j\); for a p^3 readout, the full \(D_p\bmod p^2\) and quadratic jet are required. The earlier three-port reflected compression remains valid at its certified precision; this finding identifies a concrete BRC information-loss boundary under subsequent argument deformation.

## Exact arithmetic witness and executed coverage

At p=13 (r=2), \(\ell_2(z)=1+8z+6z^2\), \(\ell_2(1/2)=0\) mod13 and \(j=7\).
The actual integer recurrence yields
\[
W_{13}(1)=13,\quad D_{13}\equiv68\pmod{169},\quad T_{13}\equiv2\pmod{13}.
\]
Thus \(W_{13}(14)=1066\pmod{2197}\), whereas \(W_{13}(1)=13\pmod{2197}\). The difference is 1053 mod2197, and is 39 mod169. Both states have the same all-weight reflection readout mod2197. The individual sample observers are
\(C_{13}(1)=1690,\;C_{13}(6k+1)=1014\pmod{2197}\).

At p=373, \(j=294\), \(D_{373}=84217\pmod{373^2}\), \(T_{373}=319\pmod{373}\), \(W_{373}(1)=373\), and \(W_{373}(374)=27656831\pmod{373^3}\).

The attached standard JavaScript BigInt checker was **actually executed** for all 77 primes 13<=p<=2000 in the two target residue classes. For each it independently generated b_k with the original exact rational recurrence in Z/p³, reconstructed ell_r and j, and checked CM0, nonzero j, both jets, earlier reflection weighted scalars, reflected invariance and Taylor through p^3; all PASS. The all-prime mathematics is the above derivation, not the finite test count.

## Continuation

Mother objective: prove \(\Delta_p-R_p\equiv0\pmod p\) (equivalently original \(W_p(1)\equiv p\bmod p^3\)) for both target classes, or produce an in-hypothesis counterexample. This remains OPEN.

**Next precise action:** compose the source-sensitive argument jet \((j,D_p\bmod p^2,\lambda)\) with the sibling original 216 terminating three-strip \((F_0,F_1,F_2)\) differential system, and seek a finite WZ/contiguous identity evaluating the *fixed* t=1 weighted functional. Discriminating check: the proposed bridge must retain the upper H2 4F3 strip, signed weight and p13/p19/p373 divided second carry, and must distinguish t=1 from t=1+p. The direct reflected-three-atom scalar alone is insufficient for that declared deformation horizon. The separate native p373 H0/B0 operator experiment remains with support #1559.

**Source/process provenance:** author-side GitHub evidence only; current Gateway 0.6.11 was read, exact native continuation call returned \`CONTROL_QUOTA\`, source sync reported \`UPSTREAM_CODE_REVIEW_REQUIRED\`, \`research_authority_granted=false\` and \`executor_binding_configured=false\`. There is no native session/claim/run/source-checkpoint/Result/review established by this note. Preserve old service session \`MCP-06f7ad61a8d841d9ba1ba1ef4d088d94\`, requests/issues #6637/#6638 and unpublished staging without replay; owner transition remains under support #1558. Frozen scientific pin, P000, applicable ACTIVE worldview and distinct Research/Maintenance identities unchanged.

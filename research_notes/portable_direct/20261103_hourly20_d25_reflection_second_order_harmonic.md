# D25: second-order harmonic refinement of original 216–2304 reflected-unit transfer

Date: 2026-11-03 (+08). Researcher logical conversation: chatgpt-research-hourly-enterprise-math-20260923 (separate from maintenance chatgpt-hourly-enterprise-math-20260921). Author-side portable mathematical result: HAND_PROVED / FINITE_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; original scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

Previous source: enterprise-math@50c6e6bc55cd3e5778cfb400ee09b0c40e71138e, where the three-value mod-p reflected-unit law was proved. P000 and ACTIVE Heartbeat native X6 are preserved. The argument below is ordinary auxiliary p-adic rational arithmetic, not a native-X6 result.

## New theorem (all primes p >= 5)

For 1 <= k < p, set

\[
b_k=\frac{(2k)!(3k)!}{(k!)^5 216^k},\qquad
c_k=\frac{(4k)!}{(k!)^4 2304^k},\qquad
h_k=\frac{c_k}{b_k}=\frac{(4k)!k!}{(2k)!(3k)!}\left(\frac3{32}\right)^k.
\]

Put q_a=floor(ak/p), r_a=ak-p q_a (1<=r_a<p) for a=1,2,3,4, and d=q_4-q_2-q_3. Define

\[
\tau_p(k)=\frac{(-1)^d}{16}\cdot\frac{3\binom 2{q_3}}{\binom 3{q_4}}\in\mathbb Z_p^\times.
\]

For harmonic numbers H_n=sum_{j=1}^n 1/j in F_p, H_0=0, and integer Fermat quotients Q_p(a)=(a^{p-1}-1)/p mod p, let

\[
E_p(k)=Q_p(3)-5Q_p(2)+4H_{r_4-1}+H_{k-1}-2H_{r_2-1}-3H_{r_3-1}\quad(\bmod p).
\]

**For all primes p>=5 and all k=1,...,p-1:**

\[
\boxed{h_kh_{p-k}\equiv\tau_p(k)[1+pE_p(k)]\pmod{p^2}.}
\]

Also E_p(p-k)=E_p(k) mod p, and tau_p(p-k)=tau_p(k) in Z_p. This is a strict precision lift of the prior three-class law: tau_p(k) reduces to 3/16, -1/16 or 1/8 mod p according to the previously proved exact bands. Every denominator is a p-unit. The involution is k -> p-k, not k -> p-1-k.

## Proof

For n=qp+r with q<=3, 1<=r<p, define U_p(n)=product of 1<=j<=n with p not dividing j. Since n<4p<=p² (p>=5),

\[
n!=p^q q!U_p(n),\quad
U_p(qp+r)\equiv(-1)^q r![1+qp(H_r-W_p)]\pmod{p^2},
\]

where W_p=((p-1)!+1)/p is the Wilson quotient. Indeed, each complete unit block has product (p-1)! mod p² because H_(p-1)=0 mod p. The residual block contributes 1+qpH_r.

For each a=1,2,3,4, put q'_a=a-1-q_a and r'_a=p-r_a. The exact p-valuation of (ak)![a(p-k)]! is a-1. Using r!(p-r)!=(-1)^r r[1+p(H_(r-1)-W_p)] mod p², H_(p-r)=H_(r-1) mod p and H_r=H_(r-1)+1/r, its p-unit is

\[
F_a:=p^{-(a-1)}(ak)![a(p-k)]!
 \equiv(-1)^{a-1+r_a}r_a q_a!q'_a!
 \left[1+p\left(aH_{r_a-1}+\frac{q_a}{r_a}-aW_p\right)\right]\pmod{p^2}.
\]

The reflected ratio has the exact form h_kh_(p-k)=(3/32)^p F_4F_1/(F_2F_3); all p powers cancel. The Wilson quotient disappears because 4+1=2+3. The quotient of the four small factorial factors equals

\[
\frac{q_4!q'_4!}{q_2!q'_2!q_3!q'_3!}
=\frac{3\binom2{q_3}}{\binom3{q_4}},
\]

and its sign is (-1)^(r_4+k-r_2-r_3)=(-1)^d, as r_4+k-r_2-r_3=-pd.

The leading residue ratio has expansion

\[
\frac{r_4k}{r_2r_3}
\equiv \frac23\left[1+p\left(\frac{q_2}{2k}+\frac{q_3}{3k}-\frac{q_4}{4k}\right)\right]\pmod{p^2}.
\]

These three q-corrections cancel the q_4/r_4-q_2/r_2-q_3/r_3 terms from F_4F_1/(F_2F_3), because r_a=ak mod p. Finally (3/32)^p=(3/32)[1+p(Q_p(3)-5Q_p(2))] mod p² and (3/32)*(2/3)=1/16. This yields precisely tau_p(k)[1+p E_p(k)].

For reflection symmetry, under k -> p-k, r_a -> p-r_a and H_(p-r_a-1)=H_(r_a-1)+1/r_a mod p. Thus

\[
E_p(p-k)-E_p(k)
=4/r_4+1/k-2/r_2-3/r_3=0\pmod p.
\]

The tau symmetry follows directly by q_a -> a-1-q_a and binomial symmetry. QED.

## Explicit BRC information-fidelity witness

At p=13, k=1 and k=2 both belong to the same outer reflected class d=0 and have the same tau_13=53 mod 169. But E_13(1)=9 and E_13(2)=8 mod 13, so

\[
h_1h_{12}=1,\qquad h_2h_{11}=157\pmod{169}.
\]

Both are 1 mod 13. Therefore the previous mod-p three-class label alone loses information needed by the mod-p² reflected observer; a class label plus E_p(k) recovers this specified higher-precision observation. The preserved data include ordered kernel sources, k/p-k pairing, valuation stratum, unit class, Fermat quotient and harmonic correction.

## Reproducible verification and continuation

The companion JavaScript file d25_two_kernel_reflection_second_order_checker_20261103.js was actually executed in V8 with exact BigInt arithmetic. It independently computes the original factorial p-unit ratio and the harmonic formula, also tests reflection symmetry, for **all 76 primes 5<=p<=400 and all 13,806 nonzero indices**; PASS, including 13,19,373. This is exact finite regression distinct from the all-prime algebraic proof. Native H0/B0 p373 was not executed.

Current mother goal stays OPEN: Delta_p-R_p=0 mod p, with the frozen signed W216(p-1)=p mod p³ target for p mod 24 in {13,19}. The sibling result enterprise-math@90bc3567d93d82323e9becf477d20a3e81df6e50 has already discharged the 2304 Q4 high-tail zero using the published Guo-Zudilin full/half congruence. Do not repeat that proof or the earlier 301-prime scalar check.

**Next scientific action:** construct a p-dependent two-index k <-> p-k signed 216-to-2304 finite transform using the new mod-p² class-plus-harmonic transfer, preserving 6k+1 versus 8k+1 weights, inclusive p-1 endpoint and the known -2p³ terminal correction mod p⁴. Test exact residuals at 13,19,373 and seek a terminating WZ/parameter certificate or precise obstruction; alternatively discharge the remaining 216 low-half + Q3 signed high-tail cancellation from the sibling reduction.

At 2026-11-03T07:23:51Z the live gateway 0.6.11 reported UPSTREAM_CODE_REVIEW_REQUIRED; research_authority_granted=false, executor_binding_configured=false, active quota 5/5. Historical read-only recovery issue #6637 succeeded; continuation issue #6638 failed. No new native session, claim, open, Source checkpoint, Result or admission was created. Old session/staging remain untouched. Control support #1558 and native benchmark #1559 retain their existing owners and scope.

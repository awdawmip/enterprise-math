# D25 original 216: one-sided primal–dual Laurent reduction modulo p^3

Date: 2026-11-03; independent author-side TASK_RESEARCH work for logical lane `chatgpt-research-onhour-enterprise-math-20260923`, separate from maintenance. Status **AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Immutable scientific input: Enterprise Math `c47e13e4aba0e006366f989d6334d443f6333ae3`; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Current behavioral rules are separate. No native Source claim/run/checkpoint, acceptance, or H0/B0 experiment.

## Theorem 1: original middle ↔ high reflected reciprocal pair

Let p=6r+1>=7 be prime, let
$
b_k=\frac{(2k)!(3k)!}{(k!)^5 216^k}
=\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k},
\qquad W_{p-1}=\sum_{k=0}^{p-1}(6k+1)b_k.
$
For every integer j with 2r+1<=j<=3r, write `x_j=b_j/p` and `y_j=b_{p-j}/p^2`. Both are p-adic units, and **for every such p and j**:
$
\boxed{x_j y_j\equiv\frac{1}{36j^3}\pmod p.} \tag{1}
$
In particular, `y_j=(36j^3 x_j)^(-1) (mod p)`, with all factors invertible.

**Self-contained proof.** Legendre's factorial valuation gives v_p(b_j)=1 and v_p(b_{p-j})=2 on exactly these oriented bands. For 0<=q<=3, 0<=s<p, the p-free factorial block is `(pq+s)!/p^q = (-1)^q q! s! (mod p)`. Here the block quotients for 2j,3j,2(p-j),3(p-j) are 0,1,1,1. Hence, after dividing the product by p^3, its numerator is the product of
`(2j)!, -(3j-p)!, -(p-2j)!, -(2p-3j)!` modulo p. The complementary factorial identity `n!(p-n)!=(-1)^n n (mod p)` for 1<=n<p gives
`(2j)!(p-2j)!=2j` and
`(3j-p)!(2p-3j)!=(-1)^(j-1)3j` modulo p.
The three negative factorial-block signs leave numerator `(-1)^j 6j^2`. The denominator `[j!(p-j)!]^5=(-1)^j j^5` and `216^p=216` modulo p yield `b_j b_(p-j)/p^3=1/(36j^3)`. This proves (1), without dividing by a nonunit or inferring a summed cancellation.

## Theorem 2: one-sided complete p^3 formula (no high coefficients)

For every prime p=6r+1>=7, in Z_(p):
$
\boxed{
W_{p-1}\equiv
\sum_{k=0}^{2r}(6k+1)b_k+
\sum_{j=2r+1}^{3r}\left[
p(6j+1)x_j+
p^2\frac{1-6j}{36j^3x_j}
\right]\pmod{p^3}.} \tag{2}
$
The inverse in the second term needs only `x_j (mod p)`, while the first term uses the genuine p-adic lift `x_j (mod p^2)`. Thus the high 216 band is recovered from exactly the same original middle-band source, without an independent high-band factorial evaluation.

**Proof.** Partition 0<=k<=p-1 into 0..2r, 2r+1..3r, 3r+1..4r and 4r+1..6r. The last band has v_p(b_k)>=3. Pair the high index k=p-j (3r+1..4r) with the middle j (2r+1..3r). Since `6(p-j)+1=1-6j (mod p)` and b_(p-j) has valuation two, (1) gives `(6(p-j)+1)b_(p-j)=p^2(1-6j)/(36j^3x_j) (mod p^3)`. The middle term is exactly p(6j+1)x_j. Sum each directed pair. QED.

For p mod24 in {13,19}, consume the accepted first-digit result; the frozen D25 scalar lift `Delta_p=R_p (mod p)` is already source-equivalent to `W_(p-1)=p (mod p^3)` via the finite signed Clausen bridge. Consequently the **remaining open mother congruence** is equivalent to setting the right-hand side of (2) equal to p modulo p^3. Equation (2) is proved; that final equality remains to be proved universally.

## Theorem 3: two-carrier SL2 transport and retained observer

Set `X_j=x_j mod p`, `Z_j=j^3 y_j mod p`. Then `X_j Z_j=1/36 (mod p)`. For 2r+1<=j<3r put
$
\rho_j=\frac{(2j+1)(3j+1)(3j+2)}{36(j+1)^3}\in\mathbb F_p^\times.
$
The original exact consecutive-coefficient ratio yields
$
\boxed{
\binom{X_{j+1}}{Z_{j+1}}=
\begin{pmatrix}\rho_j&0\\0&\rho_j^{-1}\end{pmatrix}
\binom{X_j}{Z_j},\qquad
\det=1,\quad X_jZ_j=1/36.} \tag{3}
$
The original signed second-digit high observer is
$
\boxed{
T_{\mathrm{high}}(p)=
\sum_{j=2r+1}^{3r}\frac{(1-6j)Z_j}{j^3}
\equiv\frac{W_{p-1}-W_{3r}}{p^2}\pmod p.} \tag{4}
$
This is a finite algebraic 2-component dual transport/readout in F_p; it is not a native X6 spatial cell, Frobenius, or substitute for the frozen source provenance. The original indices, coefficients, valuation bands, orientation, sign, and p-adic lifts are retained (BRC COMPOSE_APPLIED). The transfer remains on its stated open interior; its singular exiting boundary requires the already sourced p-adic edge-lift, not a fictional invertible step.

## Actual exact checks, distinct from proof

A JavaScript BigInt modular checker was executed for every one of the **77 target primes p<=2000, p mod24 in {13,19}**, checking **11,487 oriented middle↔high pairs**, the original recurrence modulo p^3, (1), both entries and determinant/invariant of (3), the per-pair Laurent equality (2), and the full W sum; all passed. Each of these finite primes also gave W_(p-1)=p mod p^3. An independent original *integer binomial coefficient* computation reproduced the full and half sums and high carry at p=13,19,37,373. Selected witnesses:

| p | (W_(3r)-p)/p^2 mod p | high dual observer T_high mod p | W_(p-1) mod p^3 |
|---:|---:|---:|---:|
| 13 | 3 | 10 | 13 |
| 19 | 10 | 9 | 19 |
| 37 | 17 | 20 | 37 |
| 373 | 107 | 266 | 373 |

For p=373, `W_(3r)=14887176`, `p^2 T_high=37008314`, `p^3=51895117`; their sum is `p^3+373`. At j=125 (beginning) `(X,Z)=(320,26)`, and at j=186 (end) `(X,Z)=(2,57)`; both products are 114 = 36^(-1) mod373. The two carried observers are 107 and 266; they cancel mod373.

## Minimal unfinished scientific unit and durable author-side continuation

Build a source-preserving *one-sided* terminating WZ/adjoint certificate for the right-hand side of (2) minus p, retaining the first/middle p-adic lifts, the determinant-one dual transfer, and the directed edge at j=3r. Begin with p=13,19,373 including both sign/cutoff checks; then seek an identity over all target primes. This is an alternative to repeating the completed Q3/Green/2304-tail proofs and does not assert that a rational low-degree telescope already exists.

Do not redo accepted D24 UR, published frozen R/Green binding, proven 2304 tail vanishing, Clausen zero strip, or other lane's p-k product theorem and H2 boundary. The new contribution is their **full original D25 one-sided Laurent elimination and determinant-one same-band carrier**.

Native p373 H0/B0 divided-power original [X]U modulo 139129, module rank, actual semilinear Frobenius and independent verification remain NOT EXECUTED, tracked by support #1559. Original research/maintenance lane identities remain separated. Historical native dispatch `research-onhour-20261031-0205-dispatch-r15` outer COMPLETE / inner FAILED UPSTREAM_CODE_REVIEW_REQUIRED; no duplicate. Latest em_status 0.6.11 has `research_authority_granted=false`, `executor_binding_configured=false`, Source `UPSTREAM_CODE_REVIEW_REQUIRED`, active control quota 5/5. Exact continuation: CONTROL_QUOTA; own checkpoint read: ACCESS_DENIED. No service-issued Researcher session, native CLAIM, open/run, Result/review/official checkpoint or admission in this work. Supports #1558 (execution authority) and #1559 (native benchmark). Preserve `REGISTER_PENDING` and author-side origin. No scheduler/notification change.

**Author-side continuation packet:** `mother=Delta_p-R_p=0 (modp) p=13,19 mod24`; `scientific_pin=c47e13e4aba0e006366f989d6334d443f6333ae3`; `completed_here=(1),(2),(3),(4)`; `unresolved=one-sided primal-dual full carry; native p373 experiment`; `next=derive WZ/adjoint coupling low/middle p² lift and Z, check 13/19/373`; `research_conversation=chatgpt-research-onhour-enterprise-math-20260923`; `native_session=null`; `claim=null`; `run=null`; `original_request=research-onhour-20261031-0205-dispatch-r15 FAILED`; `author_admission=UNREVIEWED_NOT_ADMITTED`.

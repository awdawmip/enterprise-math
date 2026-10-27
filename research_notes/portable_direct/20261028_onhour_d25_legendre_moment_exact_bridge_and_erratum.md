# D25 / SECOND-DIGIT-LIFT — exact Legendre moment bridge and normalization repair

2026-10-28 Asia/Hong_Kong. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`, not the separate maintenance lane. Mother `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin **`c47e13e4aba0e006366f989d6334d443f6333ae3`** is unchanged.

**Status:** AUTHOR-SIDE / ALL-PRIME EXACT POLYNOMIAL AND MOMENT IDENTITIES PROVED / 11 ACTUALLY EXECUTED FINITE CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / ORIGINAL NATIVE H0-B0 BENCHMARK NOT EXECUTED. This is an external scalar observer, not a native-X6 theorem.

## 1. Consume precisely the existing second-digit frontier

Let `p=6m+1>3` be prime and `n=2m=(p-1)/3`. Work in `F_p` and retain signed source weights, original factorial denominators and cutoff:

\[
t_k=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},\quad
f_k=(6k+1)t_k,\quad
A_m(z)=\sum_{j=0}^{m}\binom mj\binom{2m}j(z/2)^j,
\]
\[
F_m(z)=\sum_{k=0}^{n}f_kz^k=(1+6z\partial_z)A_m(z)^2,\qquad
q_m(z)=\frac{F_m(1)-F_m(z)}{1-z}.
\]

The coefficient equality `A_m(z)^2=Σ_{k=0}^{n}t_kz^k` was proved in the preceding Clausen author note; it is consumed here without recrediting. So `deg(q_m)≤n-1`, with `[z^s]q_m=Σ_{k>s}f_k` retaining the original signed rank and cutoff. The previously proved R2 reduction identifies

\[
\mathcal T_p=\sum_{k=0}^{n}f_k\sum_{s=0}^{k-1}u_s
=\sum_{s=0}^{n-1}[z^s]q_m\,u_s,\qquad
u_s=\frac{8^s}{(2s+1)\binom{2s}s}.
\]

Only `mathcal T_p mod p` is the present observer. The full `p²/p³` factorial, Green/Hesse, `κ`, native Frobenius and source ports are **not** compressed by this result.

## 2. New exact finite-field Legendre transport (all p=1 mod 6)

Let `P_n(x)` be the classical even Legendre polynomial of degree `n=2m`, reduced coefficientwise modulo `p`. Then

\[
\boxed{ A_m\bigl(2(1-x^2)\bigr)=P_{2m}(x)\quad\text{in }\mathbb F_p[x]. }\tag{L1}
\]

**Proof.** In `F_p`, `-2m ≡ m+1/2` since `6m+1=0`. The finite hypergeometric polynomial `A_m(2X)=\,{}_2F_1(-m,-2m;1;X)` therefore agrees with `{}_2F_1(-m,m+1/2;1;X)`. The classical *polynomial* identity

\[
{}_2F_1(-m,m+\tfrac12;1;1-x^2)=P_{2m}(x)
\]

follows directly by substituting `X=1-x²` into the hypergeometric differential equation and verifying the Legendre equation, parity, polynomial degree, and value 1 at `x=1`. It holds over `Q`; all coefficient denominators needed to reduce this finite identity are `p`-units. This proves (L1), with no appeal to the unproved Cauchy congruence. QED.

Write `Y(x)=P_{2m}(x)^2` and `D(x)=2x²-1`. Since `P_{2m}` is even, `Y'(x)/x` is a polynomial. The signed derivative is *essential*:

\[
F_m(2(1-x^2))=Y(x)-\frac{3(1-x^2)}xY'(x).
\]

Consequently the following is a **polynomial**, not merely a rational function:

\[
\boxed{
Q_p(x):=q_m(2(1-x^2))
=\frac{F_m(1)-Y(x)+3(1-x^2)Y'(x)/x}{D(x)}
\in\mathbb F_p[x^2],\quad \deg Q_p\le4m-2.
}\tag{L2}
\]

The numerator is divisible by `D` because it is the substituted polynomial difference `F_m(1)-F_m(z)`, exactly divisible by `1-z`. No division by `D` at its roots is performed in the computation.

## 3. New exact Legendre integral/coefficient observer

For each `0≤s≤n-1`, all the denominators `2r+1` with `r≤s` are `p`-units, since `2n-1=4m-1<p`. The finite rational beta integral gives

\[
\int_0^1(1-x^2)^s\,dx=\frac{4^s(s!)^2}{(2s+1)!},
\qquad
u_s=2^s\int_0^1(1-x^2)^s\,dx
=\frac{8^s(s!)^2}{(2s+1)!}.
\]

The integral is simply a finite coefficient functional reduced modulo `p`, not a real-analytic integration assertion about `F_p`. Linearity and (L2) yield the **all-prime exact bridge**

\[
\boxed{
\mathcal T_p
=\int_0^1 Q_p(x)\,dx
=\sum_{r=0}^{2m-1}\frac{[x^{2r}]Q_p(x)}{2r+1}
\pmod p .
}\tag{L3}
\]

Equivalently it is the `P_0` coefficient in the finite even-Legendre expansion of `Q_p`, since the integral of every even `P_{2j}`, `j≥1`, is zero. Thus the original nested factorial `(k,s)` observer is transported *exactly at this declared mod-p observer horizon* to a classical degree-`4m-2` polynomial and its zeroth Legendre component. Original labels/rank, signs and cutoff remain recoverable through (L1–L3).

**Normalization erratum to earlier author note:** `research_notes/portable_direct/20261028_onhour_d25_clausen_coboundary_portable.md` printed `L(z^s)=u_s=4^s(s!)²/(2s+1)!`; that equality is off by `2^s`. The correct numerator is **`8^s`**, as explicitly defined in its first paragraph, implemented by its actual checker, and required by its displayed recurrence `(2s+3)u_{s+1}=4(s+1)u_s`. At `s=1`, the true moment is `4/3`, not `2/3`. This note corrects the written identity without silently altering the prior immutable contribution.

## 4. More focused exact next obstacle

In the finite field the Legendre differential equation takes the *same eigenvalue for all target primes*:

\[
(1-x^2)P_{2m}''(x)-2xP_{2m}'(x)
-\frac29P_{2m}(x)=0\pmod p,
\qquad 2m(2m+1)\equiv-\frac29\pmod p.
\tag{L4}
\]

This is the correct bounded Sturm–Liouville / finite orthogonality interface for further proof search. From the *previously proved* R2 theorem, in the two frozen target classes `p≡13,19 (mod 24)`, the Cauchy `S_{p-1}≡p (mod p²)` conjecture is equivalent to the **still-open** assertion

\[
\boxed{\int_0^1 Q_p(x)\,dx=6\pmod p.}\tag{OPEN}
\]

(L1–L4) prove the reformulation, **not the constant 6**. A next real mathematics unit is to use (L4), Legendre orthogonality and the exact `D(x)`-divisibility source to prove or refute (OPEN) separately in the 13- and 19-classes. For measured `\chi_2=-1` samples, `P_{2m}` is additionally divisible by `2x²-1`; the checker verifies this for its samples, but this file does **not** infer it for every prime from finite data or solely from the sign of `\chi_2`.

## 5. Actually executed exact tests and limitations

`d25_legendre_moment_bridge_guard_20261028.py` was executed locally using Python standard-library integer arithmetic. Eleven distinct primes `7,13,19,31,37,43,61,67,73,211,373` passed: every coefficient of (L1), every coefficient of the signed quotient (L2), every required factorial/rational beta moment, equality of original nested `mathcal T` with (L3), and the **separate finite conjectural numerical prediction**. The last prediction is only checked in those 11 cases, not proved generally. At `p=373`: `m=62`, `deg P=124`, `F_m(1)=0`, `A_m(1)=0`, `P_{124}(0)=38`, `mathcal T=6`, and polynomial division by `2x²-1` has zero remainder. Test output ends `PASS_AUTHOR_SIDE_D25_LEGENDRE_MOMENT_EXACT_11_PRIMES`.

## 6. BRC, current native benchmark, and continuation

BRC decision **COMPOSE_APPLIED** from the already declared weighted source/finite-moment carrier: full population `(p,k,s,original t_k, signed f_k, beta moment u_s, cutoff, source)`; scoped observer `mathcal T mod p`; exact transport `z↦2(1-x²)` and Legendre coefficient extraction. This licenses one scalar readout only and does not certify redundancy of the original joint factorial/Green/Hesse/CM/X6 data for other operators. The native Heartbeat World remains an affine discrete X6 Cell space plus separately typed time; this external finite-field model does not claim native spatial or temporal transport. Frozen P000 and ACTIVE worldview unaffected.

Read-only Source continuation original request `joint-20261027-d25-continuation-r2` returned `SUCCEEDED` but `execution_authorized=false`, historical Source pin and predecessor frontier only. Own bridge recovery #6575 is `SUCCEEDED` for a local ACTIVE pointer without current Source authority; old dispatch #6576 terminal `FAILED/TimeoutExpired`. The static Site currently has `research_authority_granted=false`, no write relay, backend sync `CODE_REVIEW_REQUIRED`, and authenticated-subject quota `5/5`; no new CLAIM/open/Result was attempted. Three older preserved staging materials remain separate.

**Hard experimental frontier unchanged:** [original native intake #1559](https://github.com/awdawmip/enterprise-math/issues/1559) still requires an actual authorized original-class H0/B0 divided-power p=373 benchmark: `[X]U mod 139129`, module rank, semilinear Frobenius direction and normalization `eta`, signed/odd Green–Hesse observer, original `kappa`, and `Delta_p−R_p`, with independently reproducible source-pinned raw output. None of the Legendre computations constitute that native experiment. The responsible path is the canonical authorized native Task researcher or specifically designated implementation maintainer; until accepted by one, support is PENDING_OWNER.

**Research frontier:** D25/LIFT/JT2 OPEN. Do not redo D24 UR/CM0, the earlier K-boundary/R2/Clausen proof, or finite bulk scans. Resume legitimate own Source continuation/claim only after real same-subject authorization; retain original request IDs and staging provenance. Publish this author-side proof as such and have a genuinely independent Driver review before formal admission. The present checkpoint does not release or inherit anyone else's run.

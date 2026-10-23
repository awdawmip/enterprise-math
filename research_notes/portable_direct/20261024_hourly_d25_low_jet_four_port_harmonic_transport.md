# D25/LIFT — Exact LOW first-jet four-port carrier and harmonic transport; fixed-pole nonclosure

2026-10-24 | TASK_RESEARCH | **new portable, author-proved rational identities** | **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Task Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** is unchanged. Author provenance: ordinary Research lane **chatgpt-research-hourly-enterprise-math-20260923**, not CONTROL_PLANE_MAINTENANCE chatgpt-hourly-enterprise-math-20260921. Current portable evidence is not a Source execution or native experiment. Current GitHub control head and this older scientific pin are different objects. Global-Knowledge canonical read: main@1a5c1a6d2833f3441c46eba5c5d01427b3e299ca, P000 startup projection checked against canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (ACTIVE_LOCKED).

## Inherited precise question

The independently authored [LOW-JET/HIGH sectors reduction](20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md) defines, for every integer m>=0,
\[
b_{m,n}=(-1)^n2^{-n}\binom mn,\qquad
k_n=\frac{(1-3n)(6n+3)}{(3n+1)(3n+2)},\qquad 0\le n\le m,
\]
\[
\epsilon_j=\frac3{6j+1}-\frac1{3j+2}-\frac2{3j+1},\quad
e_n=\sum_{j=0}^{n-1}\epsilon_j,\quad
d_n=\frac2{1-3n}+\frac2{6n+3}-\frac1{3n+2}-\frac2{3n+1},\quad D_n=e_n+d_n,
\]
\[
A_m=\sum_{n=0}^m b_{m,n}k_n,\qquad
J_m^{\rm lo}=\sum_{n=0}^m b_{m,n}k_nD_n.
\]
The exact previously proved two-port recurrence for A_m is [LOW binomial two-port contiguity](20261024_hourly_d25_low_binomial_two_port_contiguity.md); that result and the first-jet definition are consumed, **not claimed as discoveries here**. Remaining original second-digit requirement is D_m^{finite}=0 mod p with p=6m+1 prime, and it retains BOTH high sectors, n=2m seam, n=4m terminal, Fermat quotient, and Source-specific CM/divided-power comparison.

## Theorem 1: cancellation of the apparent extra LOW-jet poles

Define finite rational Cauchy moments, for m>=0, a in {1,2}, r in {1,2}, and rational x,
\[
Q_m^{(r)}(a;x):=\sum_{n=0}^{m}\frac{b_{m,n}x^n}{(3n+a)^r}.
\]
Then the following equality is an identity of rational functions in n (not merely a congruence):
\[
\boxed{k_nd_n=
\frac{2}{3n+1}+\frac{6}{3n+2}
-\frac{4}{(3n+1)^2}-\frac{3}{(3n+2)^2}.}\tag{1}
\]
In particular, the apparent poles at 1-3n and 6n+3 in d_n cancel **before** summing; no extra negative/half-integer port is needed. Therefore the whole rational part of the original LOW first jet is exactly
\[
\boxed{R_m:=\sum_{n=0}^m b_{m,n}k_nd_n
=2Q_m^{(1)}(1;1)+6Q_m^{(1)}(2;1)
-4Q_m^{(2)}(1;1)-3Q_m^{(2)}(2;1).}\tag{2}
\]
Proof: substitute the displayed exact k_n,d_n, put over (3n+1)^2(3n+2)^2, and cancel the common factors. All denominators are nonzero for nonnegative integer n. Sum (1) against b_{m,n}. No step invokes reduction mod p.

## Theorem 2: exact four-port contiguity and ONE polynomial harmonic transport

Both moment orders have elementary integral representations (termwise finite polynomial integration):
\[
Q_m^{(1)}(a;x)=\int_0^1 t^{a-1}(1-xt^3/2)^m\,dt,\quad
Q_m^{(2)}(a;x)=\int_0^1 t^{a-1}(-\log t)(1-xt^3/2)^m\,dt.
\]
For m>=1 these obey exact triangular recurrences
\[
\boxed{(3m+a)Q_m^{(1)}(a;x)=3mQ_{m-1}^{(1)}(a;x)+(1-x/2)^m,}\tag{3}
\]
\[
\boxed{(3m+a)Q_m^{(2)}(a;x)=3mQ_{m-1}^{(2)}(a;x)+Q_m^{(1)}(a;x),}\tag{4}
\]
with Q_0^{(1)}(a;x)=1/a, Q_0^{(2)}(a;x)=1/a^2.

Let the original finite binomial LOW polynomial be
\[
P_m(x):=\sum_{n=0}^m b_{m,n}k_nx^n
=-2(1-x/2)^m+2Q_m^{(1)}(1;x)+3Q_m^{(1)}(2;x).\tag{5}
\]
Define a linear functional on **polynomials** (so the apparent t=1 singularities are removable):
\[
\mathscr H_\epsilon[P]=
3\int_0^1\frac{P(1)-P(t^6)}{1-t^6}\,dt
-\int_0^1\frac{(t+2)(P(1)-P(t^3))}{1-t^3}\,dt.\tag{6}
\]
Then, for every m>=0, the exact original first jet has the NEW compact certificate
\[
\boxed{J_m^{\rm lo}=R_m+\mathscr H_\epsilon[P_m].}\tag{7}
\]
The integrals in (6) are **finite rational evaluations**; use polynomial identities (1-t^{6n})/(1-t^6)=sum_{j=0}^{n-1}t^{6j} and (1-t^{3n})/(1-t^3)=sum_{j=0}^{n-1}t^{3j}, then integrate monomials. In fact
\[
\mathscr H_\epsilon[x^n]
=\sum_{j=0}^{n-1}\left(\frac3{6j+1}-\frac1{3j+2}-\frac2{3j+1}\right)=e_n.
\]
By linearity \mathscr H_\epsilon[P_m]=sum b_{m,n}k_ne_n. Equation (1) supplies the remaining rational part, proving (7).

For (3), integrate the total derivative of t^a(1-xt^3/2)^m; its boundary is (1-x/2)^m. Differentiating the exact rational identity (3) with respect to a, using Q_m^{(2)}=-partial_a Q_m^{(1)}, gives (4). This supplies a finite, terminating algorithm requiring just two labeled first ports, their two first a-derivative ports, and one explicit polynomial harmonic operator; there is **no double harmonic sum or hidden infinite tail**. This is a typed BRC observer-preserving decomposition of the LOW scalar, not a native-X6 operation or an unrestricted quotient of branch histories.

## Theorem 3: provable obstruction to a naive fixed-pole lift of the rank-two LOW recurrence

The original two simple-pole moments alone, or **any finite fixed family of rational Cauchy poles with m-independent coefficients**, cannot reproduce the entire J_m^{lo} sequence. Precisely, no finite identity valid for all m>=0 of the form
\[
J_m^{\rm lo}=c\,2^{-m}+\sum_{i=1}^s c_i Q_m^{(r_i)}(a_i;1),
\quad c,c_i,a_i\in\mathbb Q,\ r_i\in\mathbb N_{>=1},
\]
with all denominators 3n+a_i nonzero at n>=0 and data independent of m, is possible.

Proof: the triangular binomial transform h_n -> sum_{n<=m}(-1)^n2^{-n}binom(m,n)h_n has nonzero diagonal and is injective on sequences. Such an identity would force, at every n,
\[
k_nD_n=c+\sum_i c_i/(3n+a_i)^{r_i},
\]
a fixed rational function of n. But \epsilon_j=-1/(2j)+O(j^{-2}) as j->infinity, hence e_n=-(1/2)\log n+O(1); also k_n=-2+O(1/n) and d_n=O(1/n). Therefore
\[
\boxed{k_nD_n=\log n+O(1)\quad(n\to\infty),}
\]
contradicting rational-function asymptotics. The harmonic channel in (6) is structurally necessary for this **specific class of fixed finite-pole representations**. This does not exclude m-dependent coefficient recurrences, enlarged differential/difference modules, or another legitimate WZ certificate for the full LIFT.

## Exact p-local reuse and evidence

For every prime p=6m+1 and the ORIGINAL LOW cutoff n<=m, the integers 3n+1,3n+2 and 6j+1 (j<n) are strictly between 0 and p. Thus (1)–(7) may be read in Z_(p) without inverting p or losing a seam. Combining (7) with the independently proved full forcing equivalence gives a joint normal form **only modulo p**:
\[
\boxed{
\mathcal D_m^{finite}\equiv
\frac{A_m-G_m+B_m}{p}+R_m+\mathscr H_\epsilon[P_m]
+B_mZ_m^{hi}+\frac{B_m}{9}\bigl(28-6H_{2m}-12q_p(6)\bigr)\pmod p,}\tag{8}
\]
where B_m=(2m-1)!(2m)!/(4m)!, G_m=(-1)^m((2m)!)^3/((3m)!)^2, q_p(6)=(6^{p-1}-1)/p, and Z_m^{hi} is the existing **two-seam-sensitive** high-sector carrier. Equation (8) does not assert that the boxed scalar vanishes; it isolates a new exact LOW harmonic operator compatible with the existing high Cauchy/Beta carrier. Original terminal and seam data are untouched.

**Executed author-side exact checks.** Independently reconstructed the original b_{m,n}, k_n, e_n, d_n with Python standard-library rational fractions; independently reconstructed Q_m^{(r)} by finite sums. Equality (1) passed for n=0..29, (2)/(7) for m=0..23, (3)/(4) for m=1..14 at a=1,2 and x=1,1/2,3/4; (5) for m=0..17 at those x. Every rational equality passed. Witnesses (m : J_m^{lo}, R_m, \mathscr H[P_m]):
0: (1/4,1/4,0);
1: (-19/100,-83/200,9/40);
2: (-150443/313600,-267563/313600,183/490).
These finite self-checks do not prove the general claims: proofs are the explicit rational partial fraction, finite polynomial, total-derivative, and invertible-transform arguments above. The harmonic operator was evaluated through monomial finite sums; **no numerical quadrature, native CM/divided-power benchmark, Lean/formal checker, independent proof review, Source run or checkpoint** occurred.

**BRC application:** labeled signed original n-branches; precise four rational a-ports (a=1,2; derivative order 1,2), and a separately sourced harmonic residual functional. Recurrences (3)/(4) preserve the exact m-transition and boundary (1-x/2)^m; (6) preserves the harmonic residual that a rank-two quotient loses. The observer is the LOW first-jet scalar; neither (7) nor (8) is a native space/time identity.

**Highest native frontier:** existing Source-persisted D25 checkpoint remains separate and unchanged. Source continuation most recently read for this lane requires source-specific CM companion/representative normalization and subsequent legal successor session + CLAIM/open; no such data are supplied by this portable note. Current recovery confirms historical active service session but no winning claim, no authorized run, no pending local mutation, and no unpublished active upload. No new canonical checkpoint, Result or task acceptance is claimed.

**Next exact research unit:** insert (6) and the inherited seam-regularized HIGH Beta polynomial kernel into (8), apply the two independent m/n finite differences, and construct or refute a terminating identity for the complete mod-p scalar. In parallel the true Source-bound hard blocker remains: determine the primitive class, map direction/semilinearity, relation to the ordinary omega+6 nabla_lambda omega, exact leading normalization and same-class CM/divided-power bridge before formal LIFT reopening. Do not mistake an algebraic LOW certificate for this missing Source input.

Support ticket: https://github.com/awdawmip/enterprise-math/issues/1558. Source activity/admission still pending; no task-owner role, result acceptance, automation setting or notification change follows from this GitHub evidence preservation.

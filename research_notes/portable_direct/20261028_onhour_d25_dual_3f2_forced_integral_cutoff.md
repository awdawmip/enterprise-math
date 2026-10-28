# D25/LIFT — dual truncated 3F2 kernel at z=2 and its forced p-adic cutoff

Date: 2026-10-28, 20:06 Asia/Hong_Kong. Ordinary onhour research lane: chatgpt-research-onhour-enterprise-math-20260923.
Classification: AUTHOR-SIDE / EXACT RATIONAL HYPERGEOMETRIC IDENTITY / PRIME-VALUATION BOUNDARY THEOREM / 80 EXECUTED PRIME TESTS / UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_EXECUTED.

## Scope, frozen provenance, and the new unit

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
P000 is unchanged. Original native H0/B0 odd Green/Hesse, direction, kappa, and Delta-R remain outside this scalar derivation.

Consume without recredit the exact original-216 endpoint and middle/high pairing (EM commits d8dee3c159b5c991272d50e29165b357ae8718cf, a4a706832aec5351ab7cfd36b76daef4b1ac7e28) and the new one-seed transport (EM commit 83233b9637e72b677998e2befa5f12b9770461a4). This unit gives an **exact rational hypergeometric transformation of the seed kernel**, with a mathematically forced stopping index. It directly turns the remaining character/CM evaluation problem into a finite dual 3F2 differential-moment problem.

Let p=6m+1>3 be prime. From the one-seed note, the high-tail coefficient is u_0^{-1}S_m modulo p, where

\[
S_m=\sum_{r=0}^{m-1}\frac{9(66r^2-25r+3)}
{4(1-3r)^3(3r+2)^3}
\,2^r\frac{(5/3)_r^3}{(7/6)_r(4/3)_r\,r!}.
\tag{A}
\]

## Exact rational hypergeometric transformation

**Theorem 1.** For every integer r>=0, independently of any prime, the rational r-th summand in (A) is identically

\[
\boxed{
\frac9{32}(66r^2-25r+3)\;
\frac{(-1/3)_r^3}{(7/6)_r(4/3)_r\,r!}\,2^r .
}
\tag{B}
\]

**Proof.** The elementary rising-factorial shift formula gives

\[
(5/3)_r=\frac{3r+2}{2}(2/3)_r,\qquad
\frac{(-1/3)_r}{(2/3)_r}=\frac1{1-3r}.
\]

Consequently,

\[
\frac{(5/3)_r^3}{(1-3r)^3(3r+2)^3}
=\frac18(-1/3)_r^3.
\]

Multiplication by 9/4 times the quadratic weight gives (B). This equality is in Q, before reduction modulo p. QED.

Define a truncated polynomial, not the nonterminating analytic function,

\[
F_m(z)=\sum_{r=0}^{m-1}
\frac{(-1/3)_r^3}{(7/6)_r(4/3)_r\,r!}z^r,
\quad \theta=z\frac{d}{dz}.
\]

**Corollary 1.** In Z_(p),

\[
\boxed{
S_m=\frac9{32}
\left[(66\theta^2-25\theta+3)F_m(z)\right]_{z=2}
\pmod p.
}
\tag{C}
\]

Thus the high contribution to the *original* 216 interior observer is exactly

\[
\boxed{
\sum_{n=3m+1}^{4m}a_n\equiv
\frac{9p^2}{32u_0}
\left[(66\theta^2-25\theta+3)F_m(z)\right]_{z=2}
\pmod{p^3}.
}
\tag{D}
\]

For p=13,19 mod24, the outstanding original LIFT evaluation is the equality

\[
\sum_{n=0}^{3m}a_n+
\frac{9p^2}{32u_0}
[(66\theta^2-25\theta+3)F_m]_{z=2}
\stackrel{?}{\equiv}p+4\pmod{p^3}.
\tag{E}
\]

Equation (E) retains the original weights and cutoff and is an equivalent unfinished target, not an all-prime proof.

## Theorem 2: the cutoff m-1 is forced by a denominator valuation

Let

\[
h_r=2^r\frac{(-1/3)_r^3}{(7/6)_r(4/3)_r\,r!}.
\]

Its rational recurrence is

\[
\boxed{
\frac{h_{r+1}}{h_r}
=\frac{4(3r-1)^3}
{3(6r+7)(3r+4)(r+1)}.
}
\tag{F}
\]

For every prime p=6m+1>3, **all** h_r for 0<=r<=m-1 are p-adic units, but

\[
\boxed{v_p(h_m)=-1.}
\tag{G}
\]

Indeed for 0<=r<m-1, every numerator and denominator factor in (F) is a p-unit. At r=m-1,

\[
6r+7=p,\quad 3r-1=3m-4=(p-9)/2,
\]

and both 3r+4=3m+1 and r+1=m remain p-units. Hence the next term has valuation -1. The quadratic weight in (B) at r=m is also a unit:

\[
66m^2-25m+3\equiv9\pmod p.
\]

Therefore the weighted dual 3F2 summand at the first *excluded* index r=m also has valuation exactly -1. **The p-adically integral initial segment ends precisely at m-1; extending the truncation without an explicitly defined regularization would change the research object.**

This is an observer/source-boundary theorem: it identifies the singular index introduced by the dual representation and preserves the truncation as real p-adic data, rather than treating F_m as an unqualified infinite hypergeometric function.

## Executed evidence

Standard-library Python executable:
research_notes/portable_direct/d25_dual_3f2_boundary_guard_20261028.py.

The script checked 15 exact rational cases r=0,...,14; 80 primes p<1000, p=1 mod6, and 6098 indexed terms for identity (B), recurrence (F) and the singular next-index (G). Actual result:

~~~text
PASS_D25_DUAL_3F2_NATURAL_CUTOFF 80 primes; 6098 indexed terms; 15 exact Q cases
p373 (p,m,S_m): (373, 62, 230)
~~~

Composition with the one-seed source u_0=320 mod373 gives 230/320=59 mod373 and high contribution 59*373^2=8208611 mod373^3, independently matching the original 216 high tail from the predecessor note. These tests validate instances; (B), (F) and (G) have direct exact proofs.

## BRC and exact continuation

BRC COMPOSE_APPLIED for the signed indexed high contribution and the finite scalar observer W/J mod p^3: one-seed recurrence and the hypergeometric variable retain deterministic index, sign, multiplicity and p-adic boundary. The apparent infinite 3F2 completion is **not observer-equivalent** to the finite p-integral segment, because its first excluded term has valuation -1. No positive-weight or absolute-value projection was used, and no claim of native-operator reconstruction is made.

Next mathematical action: evaluate the *truncated* dual 3F2 differential moment at z=2 by a sourced character/CM identity or a p-adic hypergeometric transformation whose singular r=m boundary term is explicitly controlled; compare with the low/middle term modulo p^3 in (E). A generic analytic 3F2 continuation would lose the finite cutoff. Target test p=373, with both residue classes 13 and 19 mod24. Existing native experimental support issue #1559 remains the exact H0/B0 benchmark intake with PENDING_OWNER at last read.

As of the 2026-10-28 Site read, no Source Researcher/write-relay authority was granted; exact continuation read returned CONTROL_QUOTA. Existing old recovery/dispatch bridge receipts #6575/#6576 were read only. No formal CLAIM, run, Result, native experiment, Research-Activity or Driver acceptance is asserted. Author-side GitHub durability and pending formal registration are separate from Source admission.
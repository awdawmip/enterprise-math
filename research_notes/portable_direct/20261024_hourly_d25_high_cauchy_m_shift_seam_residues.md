# D25/LIFT — Exact m-contiguity of the seam-excluded high Cauchy carrier; both exceptional pole residues

2026-10-24 | **new author-side algebraic unit**, `UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT`. No independent review, native benchmark, Source CLAIM, authorized run, Result or freeze is asserted.

Parent: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable *scientific* Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**. Author-provenance logical lane: `chatgpt-research-hourly-enterprise-math-20260923`, distinct from maintenance and the onhour Research lane. This result **consumes** the independently authored [high-seam single-Beta/Cauchy bridge](20261024_onhour_d25_high_seam_single_beta_cauchy_bridge.md) and its [rank-two reflection and four-boundary recurrence](20261024_onhour_d25_high_mirror_rank_two_finite_certificate.md); it does not re-claim either. Current control head checked separately at `cacf206c5c3a5cfaa2311858d921b0bdb880fda7`, global knowledge main at `779a23bbf80a705993a4be5ca3cabfa9bdb3a2fe`, P000 ACTIVE_LOCKED. Support/recovery: [Enterprise Math #1558](https://github.com/awdawmip/enterprise-math/issues/1558).

## Problem and retained carrier

For each integer `m >= 1` let `I_m={1,...,m-1} union {m+1,...,3m-1}`, `w_{m,r}=1` below the omitted `r=m` seam and `w_{m,r}=1/3` above it. Define the **rational**, not native-X6, finite Cauchy transform

\[
F_m(z)=\sum_{r\in I_m}\frac{w_{m,r}}{2^r(r+z)},\qquad
M^{(6)}_m=\frac{F_m(1/6)}6=\sum_{r\in I_m}\frac{w_{m,r}}{2^r(6r+1)},\quad
M^{(2)}_m=\frac{F_m(1/2)}2=\sum_{r\in I_m}\frac{w_{m,r}}{2^r(2r+1)}.
\]

The inherited rank-two reflection formula uses exactly `M^{(6)}_m,M^{(2)}_m`; the original second-digit obstruction `D_m^finite = 0 mod p` and the separate Source-specific CM normalization remain **unproved**. We ask for an exact *m-direction* contiguous law that retains the two removed high-seam indices. Here `m -> m+1` is an algebraic comparison at the **same rational argument z**, not an assertion that the prime attached to the new m equals the old one.

## Theorem 1: exact five-boundary m-contiguity (all m)

For every `m>=1` and every rational `z` avoiding displayed poles, define

\[
U_m(z)=\frac{2^{-m}}{m+z}
-\frac{2^{-(m+1)}}{3(m+1+z)}
+\frac13\sum_{j=0}^2\frac{2^{-(3m+j)}}{3m+j+z}.
\]

Then the **exact identity in Q** is

\[
\boxed{F_{m+1}(z)-F_m(z)=U_m(z).}\tag{M}
\]

In particular, all the terms are genuine boundary contributions; the old `r=m` seam enters as `+2^{-m}/(m+z)`, the old excluded upper terminal `r=3m` enters as `+2^{-3m}/[3(3m+z)]`, and the remaining three new/removed boundary terms are visible. There is no hidden infinite remainder.

**Proof.** The existing two-block polynomial is
\[
W_m(x)=\sum_{r=1}^{m-1}x^r+\frac13\sum_{r=m+1}^{3m-1}x^r,\qquad
F_m(z)=\int_0^1t^{z-1}W_m(t/2)\,dt
\]
for `Re(z)>-1`, with rational continuation of the finite sum wherever its denominators are nonzero. Subtracting the two *finite polynomials* gives
\[
W_{m+1}(x)-W_m(x)=x^m-\frac13x^{m+1}
+\frac13(x^{3m}+x^{3m+1}+x^{3m+2}).
\]
Termwise integration, valid initially on the common convergence domain and then as a finite rational identity, gives (M). The boundary labels are preserved exactly; no modular limit is involved. QED.

Let `Q_m(n)` denote the previously proved four-boundary law
\[
Q_m(n)=\frac1{2(n+1)}-\frac{2^{-m}}{n+m}
+\frac{2^{-(m+1)}}{3(n+m+1)}
-\frac{2^{-3m}}{3(n+3m)},\quad
F_m(n)-\tfrac12F_m(n+1)=Q_m(n).
\]
The two independently defined finite difference directions are **exactly compatible**:
\[
\boxed{Q_{m+1}(n)-Q_m(n)=U_m(n)-\tfrac12U_m(n+1).}\tag{FLAT}
\]
This follows by applying `1-(1/2)E_n` to (M), or directly expanding the five monomials. Thus the previously separate `n`-boundary and new `m`-boundary relations form a closed two-direction rational difference certificate. This is an exact *input* for finite WZ/contiguous search, not a WZ proof of the entire LIFT.

## Theorem 2: two distinct p-local simple poles, and their exact regularized successors

Now let `p=6m+1` be prime (`m>=1`). The original `M^{(6)}_m,M^{(2)}_m` lie in `Z_(p)` because the `r=m` and `r=3m` singular indices are **absent**. Their adjacent-`m` differences have the following **exact rational** decompositions:

\[
\boxed{
M^{(6)}_{m+1}-M^{(6)}_m
=\frac{2^{-m}}p+V^{(6)}_m,}
\tag{P6}
\]
\[
V^{(6)}_m=
-\frac{2^{-(m+1)}}{3(p+6)}
+\frac{2^{-3m}}{3(3p-2)}
+\frac{2^{-(3m+1)}}{3(3p+4)}
+\frac{2^{-(3m+2)}}{3(3p+10)}.
\]

\[
\boxed{
M^{(2)}_{m+1}-M^{(2)}_m
=\frac{2^{-3m}}{3p}+V^{(2)}_m,}
\tag{P2}
\]
\[
V^{(2)}_m=
\frac{3\,2^{-m}}{p+2}
-\frac{2^{-(m+1)}}{p+8}
+\frac{2^{-(3m+1)}}{3(p+2)}
+\frac{2^{-(3m+2)}}{3(p+4)}.
\]

**Proof.** Specialize (M) to `z=1/6` and divide by 6, and independently to `z=1/2` and divide by 2. Use only `p=6m+1` for exact re-expression. The first pole is precisely the newly included `r=m` term of `M^{(6)}_{m+1}`; the second is the newly included `r=3m` term of `M^{(2)}_{m+1}`. All denominators of `V^{(6)},V^{(2)}` are p-units for every target prime `p>=7` (their nonzero reductions are among 2,4,6,8,10 and 3-unit multiples), so
\[
\boxed{v_p(M^{(6)}_{m+1}-M^{(6)}_m)
=v_p(M^{(2)}_{m+1}-M^{(2)}_m)=-1.}\tag{VAL}
\]
The two principal parts cannot be silently discarded or averaged away; each is a nonzero p-unit divided by p. QED.

The **regularized** adjacent carriers
\[
\widehat M^{(6)}_{m+1\mid m}:=M^{(6)}_{m+1}-\frac{2^{-m}}p,\qquad
\widehat M^{(2)}_{m+1\mid m}:=M^{(2)}_{m+1}-\frac{2^{-3m}}{3p}
\]
are p-integral, and their differences from the old moments are the explicit four-term `V` above, with mod-p residues
\[
\boxed{
V^{(6)}_m\equiv -\frac{2^{-m}}{36}-\frac{7\,2^{-3m}}{60},\qquad
V^{(2)}_m\equiv\frac{23\,2^{-m}}{16}+\frac{5\,2^{-3m}}{48}\pmod p.
}\tag{RES}
\]
All inverses in (RES) are of p-units; `p` was subtracted **in Q before any reduction**, never inverted modulo p.

**Consequence for the actual research plan.** A naive m-induction on either high rank-one Cauchy moment creates a genuine valuation -1 obstruction at the old source prime; this is a **proved failure of that unregularized method**, not a failure of the LIFT conjecture. Any inductive/contiguous combination with the original LOW jet must retain both the `r=m` and `r=3m` principal parts and use `V` (or an exactly equivalent seam-sensitive coordinate). Conversely, for integer `0<=n<=m`, (M) and (FLAT) have p-unit denominators; thus the low-index finite-difference route is algebraically regular and may safely use the new five-boundary law *at its own stated observer*. No cross-prime induction or native equality follows.

## Theorem 3: unique p-local cancellation direction of the two seam poles

Theorem 2 can be sharpened to an exact obstruction to, and a repair for, arbitrary scalar compression. Fix `p=6m+1` prime and write `\Delta_m M^{(a)}=M^{(a)}_{m+1}-M^{(a)}_m`. For **every p-integral rational coefficient c** (which may depend on m), the following equivalence holds:
\[
\boxed{
\Delta_m M^{(6)}-c\,\Delta_m M^{(2)}\in\mathbb Z_{(p)}
\quad\Longleftrightarrow\quad
c\equiv3\cdot 2^{2m}\pmod p.
}\tag{UNIQUE}
\]
Indeed Theorem 2 gives the exact principal part
\[
\Delta_m M^{(6)}-c\,\Delta_m M^{(2)}
=\frac{2^{-m}-c\,2^{-3m}/3}{p}
+V_m^{(6)}-cV_m^{(2)}.
\]
The last two terms are p-integral; the principal part is integral **if and only if** its numerator is divisible by p. Since `3\cdot 2^{3m}` is a p-unit, this is precisely the stated congruence. This proves necessity as well as sufficiency: the incoming two-pole vector has rank one over the residue field, and its annihilator is exactly one line. This is a p-adic/branch-carrier statement, *not* an assertion that the two moments are individually equal or may be deleted.

Choosing the exact distinguished coefficient `c_m=3\cdot2^{2m}` gives a globally rational, p-integral pair-difference:
\[
\boxed{
\mathcal J_m=
\left(M^{(6)}_{m+1}-M^{(6)}_m\right)
-3\cdot2^{2m}\left(M^{(2)}_{m+1}-M^{(2)}_m\right)
=V_m^{(6)}-3\cdot2^{2m}V_m^{(2)}.
}\tag{PAIR}
\]
Its second-digit-relevant first residue is the explicit finite expression
\[
\boxed{\mathcal J_m\equiv
-\frac{49}{144}2^{-m}
-\frac7{60}2^{-3m}
-\frac{69}{16}2^m\pmod p.}\tag{PAIR-RES}
\]
Proof: substitute both previously proved `(RES)` expressions into (PAIR), combine the two `2^{-m}` fractions `-1/36-5/16=-49/144`, and retain the untouched `2^m` and `2^{-3m}` sectors. This formula keeps the original seam labels and is a certified **repair coordinate for the m-step**. It cannot by itself evaluate the full `D_m^{finite}` or show that its LOW/high and Fermat-quotient pieces vanish.

Additional exact author self-check: direct rational `V^{(6)}-3\cdot2^{2m}V^{(2)}` versus the two original finite moment differences agrees for `m=1..17`. For target primes in that range, the mod-p residues from the two independently calculated sides and (PAIR-RES) agree; witnesses `p: J mod p` are `7:1, 13:12, 19:16, 31:1, 37:34`. The proof is the two-term valuation argument above, not this finite verification.

## Checked mathematical evidence and admission boundaries

Independent author `fractions.Fraction` calculations reconstructed `F_m(z)` from the original finite, seam-labeled sums rather than from (M), and checked:
- (M), the inherited n-boundary law, and (FLAT) exactly for every `m=1..17` and `z in {0,1/6,1/2} union {0,...,m+1}`;
- (P6), (P2) exactly for every `m=1..17`;
- (RES) by modular rational arithmetic for each prime `p=6m+1` in that range; explicit principal-part residues `p(M^{(6)}_{m+1}-M^{(6)}_m),p(M^{(2)}_{m+1}-M^{(2)}_m) mod p`: `p=7: (4,5)`, `13:(10,4)`, `19:(12,6)`, `31:(1,21)`.
All self-checks passed. The general theorems rest on the displayed finite polynomial and rational identities, not finite extrapolation. No native scientific experiment, independent proof review, execution authorization or Source durable checkpoint was performed here.

**BRC typed composition applied:** source carrier retains each signed high `r` branch, multiplicity `w_r`, rational weight `2^{-r}`, the two omitted seam labels and the future `z`-observer. The `m`-shift is an operation that changes the allowed ports: `r=m,3m` emerge as explicit residual channels. (P6)/(P2) is a mathematically exact failure witness against a lossy total-only quotient, while the regularized two-port lift preserves the p-local scalar observer. No positive-mass cancellation, native-X6 transfer or invented BRC computation is claimed.

**Highest preserved frontier:** inherited Source-persisted D25 checkpoint and frozen scientific pin only; portable proofs from the other research lane and our present note remain `UNREVIEWED / NOT_ADMITTED`. **Still open:** prove `D_m^{finite}\equiv0\pmod p` for all target-class primes by a valid terminating contiguous/WZ identity with full LOW jet, first-digit quotient, Fermat term and both rank-two corrections, *or* exhibit a genuine obstruction; independently supply original Source-specific CM divided-power comparison/representative normalization and execute the required native validation. **Next exact action:** use (M)+(FLAT)+(P6)/(P2) to form a seam-regularized joint LOW/high finite-difference certificate, compare its complete endpoints against the fixed `D_m^{finite}` without changing its original task/observer. Current bridge recovery verified active historical session but no winning CLAIM or authorized run; exact continuation remains subject to its own original request receipt; neutral staging archives are not research checkpoints. Keep the schedule/notification and Source pin unchanged.

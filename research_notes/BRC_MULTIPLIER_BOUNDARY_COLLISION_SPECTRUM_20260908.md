# BRC Multiplier Boundary Collision Spectrum — Exact Oracle Reduction

Status: `RESEARCH FRONTIER / EXACT DERIVATIONS + FINITE DIAGNOSTIC / FACTORING-EQUIVALENT ORACLE / NO FACTORIZATION SPEEDUP CLAIM`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Parent family: `T0_BRC / multiplier factor bridge`
Current source context at derivation: `main@0242e5ccbc6b134241f083e6204de2bd47393e78`
Relevant prior notes:

- `research_notes/BRC_MULTIPLIER_FACTOR_BRIDGE_20260906.md`
- `research_notes/BRC_MULTIPLIER_PRIORITY_JUMP_20260906.md`
- `research_notes/BRC_OPPORTUNISTIC_SHORTCUT_PORTFOLIO_20260907.md`

## 0. Scope and BRC typing

Let

`N=pq`,

with distinct odd coprime factors `1<p<q`. For an odd multiplier split `k=ab`, define the hidden factor-split boundary

`L_(a,b)=(ap+bq-2)/2`.

The object studied here is **not** a positive branch weight. The adequate BRC carrier is labeled boundary support/provenance, and the translation-invariant observer is its pairwise-difference/autocorrelation spectrum. Collapsing immediately to Boolean existence, branch count, or a coarse basin total can erase the signal.

Accordingly this note does not invoke Weighted-BRC mass identities. It applies the BRC observer/provenance discipline to an arithmetic boundary-support carrier.

The central question is computational, not merely extensional:

> Can any nontrivial translation-invariant functional of the hidden boundary family be computed from `N` through an N-visible BRC process without first recovering a factor or an equivalent hidden boundary?

## 1. Odd multiplier lattice and exact difference law

For a scan horizon `K`, let

`D_K={(a,b): a,b positive odd integers, ab<=K}`.

For two points `(a,b),(c,d)` in `D_K`, write

`a-c=2r`, `b-d=2s`.

Then exactly

`L_(a,b)-L_(c,d)=r p+s q`.

Thus every translation-invariant boundary gap is an integer linear form in `(p,q)`, while the multiplicity with which a coefficient vector `(r,s)` occurs is determined solely by the known geometry of `D_K`.

For opposite-sign coefficients this is the rational-approximation regime

`|r p-s q|`, 

so small near-collisions are the same Diophantine balancing phenomenon underlying multiplier-Fermat / Lehman-style searches. The BRC-specific opportunity, if any, must therefore come from obtaining a spectrum/autocorrelation observable without individually materializing those hidden factor-split boundaries.

## 2. Exact collision onset theorem for the odd multiplier lattice

Suppose two distinct points collide exactly:

`L_(a,b)=L_(c,d)`.

Then

`(a-c)p+(b-d)q=0`.

Because `gcd(p,q)=1`, there is an integer `t` such that

`a-c=tq`, `b-d=-tp`.

All coordinates in `D_K` are odd, hence both differences are even. Since `p,q` are odd, `t` must be even. For a nontrivial collision `|t|>=2`, so

`|a-c|>=2q`, `|b-d|>=2p`.

Consequently any exact collision requires

`K>=2q+1`.

This bound is sharp. At `K=2q+1`, the two admissible points

`(2q+1,1)` and `(1,2p+1)`

satisfy

`(2q+1)p+q = p+(2p+1)q = 2pq+p+q`.

Therefore:

`FIRST_NONTRIVIAL_EXACT_COLLISION_HORIZON = 2q+1`.

For balanced RSA-scale semiprimes this is factor-scale, not a small-multiplier phenomenon. In particular, an exact-collision count at `K<=1000` cannot be the desired RSA shortcut unless one factor is itself tiny.

## 3. Three-boundary affine-simplex theorem: `m in {1,3}` already suffices as an oracle

Take only the baseline split `(1,1)` and the two splits of multiplier `3`:

`(3,1)`, `(1,3)`.

Put

`A=L_(1,1)=(p+q-2)/2`.

Then exactly

`L_(3,1)=A+p`,

`L_(1,3)=A+q`.

Hence the three hidden boundaries are simply the translated set

`{A, A+p, A+q}`.

Their unlabeled pairwise-distance multiset is

`{p, q, q-p}`.

Since `0<p<q`, the diameter is exactly `q`. Therefore **an oracle that returns only the unlabeled pairwise-distance multiset of these three boundaries factors `N` immediately**; no boundary labels are required.

Two scalar consequences are also sufficient:

1. Absolute-distance mass

   `T_3=p+q+(q-p)=2q`,

   so `q=T_3/2`.

2. Squared-distance energy

   `E_3=p^2+q^2+(q-p)^2`

   `=2(p+q)^2-6N`.

   Thus, with `S=p+q`,

   `S^2=E_3/2+3N`.

   Exact `S` then yields the ordinary quadratic factor recovery.

This sharply reduces the previous `K<=1000` collision-spectrum proposal: if BRC can compute a genuine hidden-boundary distance moment from `N`, multiplier `3` already contains enough information.

## 4. Five-boundary unlabeled multiplicity certificate: `m in {1,3,5}`

Add the two multiplier-5 splits. After subtracting the common translation `A`, the five hidden positions are

`{0,p,q,2p,2q}`.

The ten positive pairwise distances are the multiset

`{p,p,q,q,2p,2q,q-p,2(q-p),|2p-q|,2q-p}`.

For distinct odd coprime `p<q`, the values `p` and `q` each occur exactly twice. Every other displayed value is positive, differs from `p` and `q`, and the six singleton values are pairwise distinct. This follows by pairwise equality case analysis: any forbidden equality reduces either to `p=q`, an even-ratio relation such as `q=2p`, or a small rational relation such as `2q=3p`, `3q=4p`, etc.; oddness and `gcd(p,q)=1` exclude all of them for `p,q>1`.

Therefore the unlabeled distance spectrum of just five boundaries identifies `{p,q}` as the **two and only two multiplicity-2 spectral lines**.

Its total squared-distance energy is

`E_5=sum_(i<j)(L_i-L_j)^2`

`=16(p^2+q^2)-18N`

`=16(p+q)^2-50N`.

So a single exact scalar `E_5` would again suffice:

`S^2=(E_5+50N)/16`.

The five-point formulation is not needed information-theoretically; its value is robustness of an unlabeled multiplicity fingerprint.

## 5. Autocorrelation formulation

For a chosen finite split family `B`, define the hidden boundary counting measure

`A_B(t)=#{beta in B : L_beta=t}`.

Define its ordered autocorrelation

`R_B(h)=sum_t A_B(t) A_B(t+h)`.

This is the natural BRC collision-spectrum observer for this route:

- branch provenance is retained long enough to place mass at a boundary coordinate;
- translation is quotiented out only after it is proved irrelevant;
- individual labels may then be discarded if the declared future operation is only the difference spectrum;
- moments such as `sum_h h^2 R_B(h)` remain sufficient for factor recovery in the three-point family.

The critical unresolved operator is therefore not `find S` directly and not `count exact collisions`. It is:

`N -> implicit hidden-boundary autocorrelation or one sufficient moment`.

## 6. Factorization-equivalent-oracle boundary

This route now has a clean no-free-information checkpoint.

Factors trivially generate all `L_(a,b)` and their spectrum. Conversely:

- the `m={1,3}` distance multiset gives `q` as its diameter;
- its absolute-distance mass gives `q`;
- its squared-distance energy gives `S`;
- the `m={1,3,5}` unlabeled multiplicity spectrum gives `{p,q}` directly.

Therefore merely *defining* or *materializing* the collision spectrum is not an N-only factoring algorithm. It is a factorization-equivalent oracle target.

A candidate BRC shortcut counts as new progress only if its evaluation uses N-visible operations and does not first obtain a successful difference-of-squares boundary, a factor, `S`, `g=q-p`, or an algebraically equivalent quantity.

## 7. Relation to current project negative results

The current multiplier factor-bridge program already found:

- coarse basin support/Pell endpoint phase is not a useful multiplier selector on the tested population;
- cheap `N/J/R` shadow classification did not retain stable held-out routing gain;
- exact gap sorting helps only when the states are already materialized;
- factor information remained concentrated in point-level completion-gap structure.

Accordingly the collision-spectrum continuation must not simply repackage those discarded coarse selectors. It requires a genuinely new exact or measurably stronger N-visible operator that acts on an **implicit factor-split boundary family**.

## 8. Finite multi-horizon fingerprint diagnostic

A finite diagnostic was also run on the odd hyperbolic domains `D_K` for

`K in {25,49,81,121,169,225,361,529,729,1000}`.

For realized coefficient vectors with `|r|,|s|<=20`, the growth signature of the purely geometric line multiplicity

`m_K(r,s)=#{boundary pairs in D_K with half-difference vector (r,s), up to sign}`

separated all tested vectors up to the unavoidable coordinate swap `(r,s)<->(s,r)` caused by the symmetry of `D_K`. In the tested set, every nontrivial signature collision class was exactly such a swap; `(1,-1)` was unique.

This is finite evidence, not a theorem for all coefficient vectors. Its significance is secondary: if only an unlabeled *partial* spectrum can be exposed, changing `K` may provide a known geometric fingerprint for decoding a spectral line's coefficient vector without recovering individual source boundaries.

## 9. Revised experiment program

### Experiment C1 — minimal implicit observer challenge

Do not begin with `K=1000`. Restrict to the three hidden boundaries from `m=1,3` and attempt to compute, using only N-visible BRC operations, at least one of:

- diameter of the hidden support;
- total absolute pairwise-distance mass `T_3`;
- squared-distance energy `E_3`;
- autocorrelation support `R_B(h)`.

### Experiment C2 — hard kill condition

If the proposed observer can only be evaluated after a factor/success boundary is already known, or its derivation inserts `S`, `g`, `p`, or `q` as hidden inputs, classify it as

`FACTORING_EQUIVALENT_ORACLE / NOT N_ONLY_PROGRESS`.

### Experiment C3 — current-state regression guard

If the proposal uses only current N-visible root/remainder/phase summaries `(J_m,R_m,...)`, it must be checked against the existing negative basin/shadow results and must supply either a new exact identity or a reproducible held-out gain. A relabeling of the old shadow features is not a new route.

### Experiment C4 — success closure

If an exact N-only evaluator for `E_3` is found, recover

`S=isqrt(E_3/2+3N)`

and verify `S^2=E_3/2+3N`, then recover the factors from

`X^2-SX+N=0`.

No larger collision scan is necessary.

## 10. Current verdict

The promising insight from the multiplier lattice survives, but in a narrower form:

`LARGE_K_EXACT_COLLISION_SEARCH -> REJECT AS PRIMARY ROUTE`.

`NEAR_COLLISION_MINIMUM -> CLASSICAL DIOPHANTINE BALANCING UNLESS NEW OBSERVER EXISTS`.

`SMALL_K_HIDDEN_DISTANCE_SPECTRUM -> FACTORIZATION_EQUIVALENT ORACLE`.

`NEXT TRUE BOTTLENECK -> N_ONLY IMPLICIT AUTOCORRELATION / MOMENT OPERATOR`.

No factorization complexity improvement is claimed. No Foundation or theorem-ledger promotion is made by this research-note persistence.
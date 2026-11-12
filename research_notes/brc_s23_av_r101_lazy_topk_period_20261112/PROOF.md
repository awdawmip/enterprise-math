# R101 — Exact lazy top-k transport across source edits, with a period-expansion lower bound

Date: 2026-11-12. Status: author-side mathematical proof and exact finite implementation audit; independent review pending.

Predecessor: R100 at `bfec57d7e7c72c64a2e3b2c07a7a5c39e9291683`; frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Scope: the auxiliary finite rational circular-source model of R99–R100. P000 and native X6 are unchanged. The requested Source task `RS-S23-AV` currently has no immutable publication (read request `r101-research1-20261112-1959-task` returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`). This is independently saved author-side research without a shared CLAIM.

## Setting

Fix observer signature `sigma=(j,x,a,b)`, with `j,a,b in Z`, `x in Q`. A complete source identity is `u=(t,branch)` with integer fields ordered lexicographically. At real parameter `theta`, set `s_t={x+(t-j)theta}`, `A={a theta}`, `B={b theta}`; braces are fractional part in `[0,1)`. Source `u` is eligible precisely when `s_t` is on the directed half-open circular arc `[A,B)`; when `A=B` the arc is empty. Membership depends on `t`, while ranking retains the complete branch identity.

For any finite identity set `E`, `Top_r(E,theta)` is the ordered list of the first `r` distinct eligible identities, padded conceptually with `NONE`. `Top_1` recovers R100's winner. Let an edited version be `F=(E\\D) union Anew`, with `D subseteq E`, `|D|=d` and `Anew` a finite insertion set (identities may be newly reinserted after deletion, but no identity is counted twice).

## R101.1 — Exact batched top-k transport

For all finite `E,D,Anew`, every `k>=1`, and **every real theta**,

```
Top_k(F,theta) =
  Top_k( (Top_(k+d)(E,theta) minus D)
          union {u in Anew : M_time(u)(theta)} ).
```

Here `Top_k` of a set means the first `k` distinct identities in descending lexicographic order, with `NONE` padding if necessary.

**Proof.** Let `v` be an eligible old identity omitted from `Top_(k+d)(E,theta)`. At least `k+d` distinct eligible old identities rank strictly above `v`. Removing at most `d` old identities leaves at least `k` such identities. Additional eligible identities can only move `v` further down the ranking. Consequently `v` cannot enter the first `k` ranks of the edited version. All other retained candidates, and every newly eligible identity, occur explicitly on the right-hand side. Equality follows, including tied timestamps distinguished by branch. This proof is pointwise in `theta`, so no period-alignment or finite parameter sampling hypothesis is required. QED.

**Sharpness.** For any integers `k,d>=1`, take `E={(0,b):0<=b<k+d}`, `D={(0,b):k<=b<k+d}`, `Anew=empty`, `sigma=(0,1/4,0,1)`, and `theta=1/2`. The arc is `[0,1/2)` and all identities are eligible at phase `1/4`. Deleting the `d` highest-ranked identities makes the `(k+d)`-th original identity the `k`-th surviving identity. Thus a stored prefix of length smaller than `k+d` cannot universally provide this update without further old-source information. QED.

**Algorithmic consequence.** An exact lazy persistent edit node needs its parent top-`k+d` query, deletion list, and newly inserted source membership predicates. Its local extra work at a specified exact parameter is at most `k+d+|Anew|` candidate inspections and sorting the resulting at most `k+d+|Anew|` identities (standard comparison upper bound `O(n log(n+1))`). It does **not** require enumerating a newly enlarged global period. Old-source calculation cost, exact rational bit cost, edit depth, cache storage, and interval/output enumeration remain separate and are not hidden by this local bound.

## R101.2 — Exact finite-interval certificate for the lazy update

Fix a closed bounded rational interval `I=[L,U]`. For each source time `t` in `E union Anew`, define six affine integer-slope expressions

```
a*theta, b*theta, (t-j)*theta+x,
(t-j-a)*theta+x, (t-j-b)*theta+x, (a-b)*theta.
```

For each nonzero slope, include in `C_I` every rational `theta in I` where the corresponding expression is an integer; also include `L,U`. On every connected open gap between consecutive cuts, each source membership predicate is constant, and hence the exact transported top-k list is constant. Thus evaluating the R101.1 formula on **every cut point** and **one rational midpoint of each gap** yields a complete exact top-k profile on `I`; source identity changes or mismatches against a reference profile have exact rational witnesses.

**Proof.** Fractional-part discontinuities can only occur when one of the phases `a theta`, `b theta`, `x+(t-j)theta` crosses an integer. On a continuous fractional-part cell, order comparisons can change only where two phases coincide modulo one; these are the remaining three integer equations above. No such event lies inside a gap of `C_I`, so every arc-membership predicate, its rank ordering, and the transported top-k list stay constant on the gap. Closed cut points are evaluated individually to respect the half-open arc and isolated equality cases. Each nonzero integer slope `c` generates finitely many cuts in a bounded interval, making the certificate complete. QED.

This certificate can be used for explicit profile construction, targeted interval questions, and exact difference witnesses. Its size depends on actual phase intersections in `I`.

## R101.3 — Explicit-profile period-expansion lower bound

For every integer `N>=2`, choose `sigma=(j=0,x=1/4,a=0,b=N)`, old `E={(N,0)}`, and newly inserted lower-ranked source `u=(1,0)`. The R99 safe gcd changes from `g_E=N` to `g_F=1`. On `[0,1]` write `q={N theta}`. The old source is eligible **exactly when** `q in [3/4,1)`: the circular arc is `[0,q)`, and `s_N={q+1/4}`, which lies below `q` exactly after wrap-around at `q=3/4`. At `q=0` the arc is empty.

Since `(N,0)` outranks the inserted `(1,0)`, the edited winner equals `(N,0)` on all `N` disjoint windows

```
[m/N+3/(4N), (m+1)/N),  m=0,...,N-1,
```

and is different from `(N,0)` on the separating gaps. Therefore every *explicit, nonperiodic piecewise-constant winner profile* on the full new certified period `[0,1]` has at least `N` components carrying the old winner and at least `2N` winner-identity transitions. Materialization requires `Omega(N)` output components, although `N` has only `Theta(log N)` input bits. This is an output representation lower bound, not a lower bound on compressed symbolic or lazy point-query representations. QED.

R101.1 avoids eager replication: the source version is represented as an exact reference to the parent plus one inserted source predicate, regardless of `N`. Materialization is still available when the workload benefits from it, and R100's exact period formulas remain sound.

## Verification, reproduction and boundaries

The accompanying `check_r101.py` uses only Python's `fractions.Fraction` for mathematical assertions, without floating point. Seed `10120261112`. It compares directly re-evaluated complete eligible identities with the cached-update rule on 260 randomly generated edit histories, for `k=1..4`, at each six-family exact interval cut, each rational gap midpoint and eight additional rational points. It checks the sharpness example for all 16 `(k,d)` combinations with `k,d in {1,...,4}`, and the expanding-period construction for `N in {7,31,127,509}` at exact inside/outside rational witnesses.

The saved local reproduction returned `R101_PASS 260 360504 16 509`. Full counters and the exact domain are in `verification_r101.json`. The pointwise and interval claims above have direct mathematical proofs; the finite tests audit the implementation and edge cases. In particular, there is no claim of measured CPU speedup or a universal sublinear explicit-profile construction.

## Next frontier R102

Develop a *compressed certificate DAG* that supports exact interval classification and witness extraction on many historical versions without expanding the full safe period. Characterize edit-depth-dependent query costs, when to checkpoint/materialize a top-k prefix, and the lower bounds imposed by an explicit full-profile request. Combine this with R93 OUT certificates keyed to the full observation signature and source time, maintaining their original coverage proof and version-independent validity.

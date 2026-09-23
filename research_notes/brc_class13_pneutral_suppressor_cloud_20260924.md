# BRC class-13 p-neutral suppressor cloud

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note continues the exact `UNIFORM_EARLIEST_VISIBILITY` record problem while the formal D24 successor lifecycle remains blocked. It consumes the proved branch-defect cocycle, the uniform-union record automaton, the base-13 cancellation witness, and the Driver's clean base-13 cloud / class-19 obstruction checkpoints. It does not allocate a new formal Researcher owner, does not alter D24/UR theorem status, and does not promote auxiliary evidence.

## 1. Exact defect carrier

For a finite exponent vector `m=(m_j)`, retain the generic weight

`W_inf(m)=sum_j m_j(2j+1)`

and the exact target-prime defect

`Delta_r(m)=W_inf(m)-W_r(m)`.

For a target prime `r ==13 or 19 (mod24)`,

`Delta_r(m) = sum_j m_j [E_r(j)+v_r(j)-C_r(j)(v_r(j)+c_r)] + sum_j v_r(m_j!).`

Here

- `E_r(j)=1` iff `h_r=(r-1)/2` divides `j`;
- class `19 mod24` has no coefficient-cancellation channel, so `C_r=0`;
- for class `13 mod24`, put `ord_r(4)=2s_r`; then coefficient cancellation is exactly `j=s_r u` with `u` odd, and `c_r=v_r(1+4^{s_r})>=1`.

Endpoint, denominator, cancellation and factorial provenance remain separate.

## 2. The class-19 cleanliness invariant of a class-13 cancellation step

Fix target primes

`13 < q < p`, with `q == p == 13 (mod24)`.

A negative `q`-defect is possible only by occupying a `q` coefficient-cancellation port. Every such port has the form

`j=s_q u`, `u` odd.

Define `q` to be **19-clean below p** when, for every target prime `r<p` with `r ==19 (mod24)`,

`r does not divide s_q` and `h_r does not divide s_q`.

Because `s_q < q < p`, any positive class-19 event intrinsic to `s_q` already comes from an `r<q`; the wording “below p” is retained because that is the observer being protected.

### Theorem 2.1 — exact obstruction

If `q` is not 19-clean, then there is no finite exponent cloud `S` satisfying simultaneously

- `Delta_q(S)<0`, and
- `Delta_r(S)<=0` for every target `r<p`, `r ==19 (mod24)`.

### Proof

If `Delta_q(S)<0`, at least one occupied port must contribute through the only negative channel available on branch `q`: coefficient cancellation. Hence some occupied `j=s_q u` has `u` odd.

If `q` is not 19-clean, choose a class-19 target `r<p` with either `r|s_q` or `h_r|s_q`.

- If `r|s_q`, then `r|j`, so branch `r` receives positive denominator credit.
- If `h_r|s_q`, then `h_r|j`, so branch `r` receives positive endpoint credit.

Class `19 mod24` has no coefficient-cancellation channel; its denominator, endpoint and factorial terms are all nonnegative. Therefore `Delta_r(S)>0`, contradicting the required class-19 nonpositivity.

So a dirty `q` cannot be made negative without waking a class-19 record.

## 3. A clean q-specific suppressor, with exact p-neutral compensation

Assume now that `q` is 19-clean. Choose any prime `ell>p` and set

`j_q=s_q ell`.

Because `ell` is odd and exceeds every earlier target prime,

`Delta_q(e_{j_q})=-c_q`.

For every class-19 target `r<p`, `gcd(ell,r h_r)=1`, so the 19-clean conditions imply

`Delta_r(e_{j_q})=0`.

On branch `p`, there is no p-denominator or p-endpoint event. The only possible event is p-coefficient cancellation. It occurs exactly when

`s_p | s_q` and `s_q/s_p` is odd.

Thus

`Delta_p(e_{j_q}) = 0`

unless the q-cancellation progression is nested inside the p-cancellation progression, in which case

`Delta_p(e_{j_q})=-c_p`.

The nested case has an exact provenance-preserving compensation. Let

`u_p=p^{c_p}`.

Then

`Delta_p(e_{u_p})=c_p`,

while every target branch `r<p` sees `e_{u_p}` neutrally: no smaller target prime divides `p^{c_p}`, no `h_r>1` divides this pure p-power, and no class-13 cancellation step `s_r>1` divides it.

Define

`S_{p,q}=e_{j_q}`

in the nonnested case and

`S_{p,q}=e_{j_q}+e_{p^{c_p}}`

in the nested case.

### Theorem 3.1 — exact p-neutral / class-19-neutral suppressor

For `13<q<p`, both `13 mod24`, such an `S_{p,q}` exists with

`Delta_p(S_{p,q})=0`,
`Delta_q(S_{p,q})<0`,
`Delta_r(S_{p,q})=0` for every `r<p`, `r ==19 (mod24)`

**if and only if q is 19-clean**.

Necessity is Theorem 2.1. Sufficiency is the construction above.

This is stronger than merely finding a q-cancellation port. It proves exactly when q can be pushed downward without spending any target-p defect and without creating any class-19 competing record.

## 4. Triangularity on the remaining class-13 branches

For the canonical suppressor port `j_q=s_q ell` with `ell>p`, a larger earlier class-13 branch `r` satisfying

`q<r<p`

cannot receive a positive endpoint or denominator event:

- `r` cannot divide `s_q ell`;
- `h_r>s_q`, and `ell>h_r`, so `h_r` cannot divide `s_q ell`.

It may see a coefficient-cancellation event, but that contributes nonpositively.

Hence q-suppression can create positive spill only on **smaller** class-13 branches. Ordered from larger q downward, the canonical suppressors are therefore lower-triangular with a strictly negative diagonal. Base branch 13 is handled last by the already-proved clean base-13 cloud.

This yields a finite constructive elimination procedure whenever every positive class-13 branch encountered in the downward sweep is 19-clean. It is stated here as a sufficient construction, not as a global necessity theorem, because alternative cancellation multipliers can add extra class-13 cancellation structure.

## 5. Exact finite classification of the nine class-13-only primitive-endpoint cases below 5000

The Driver checkpoint classified the 82 higher class-13 target primes below 5000 by their non-base primitive-endpoint blockers. Independently reproducing that census gives exactly nine cases with at least one smaller class-13 blocker and no smaller class-19 blocker:

- `p=733`, blockers `{61}`;
- `p=1021`, blockers `{61}`;
- `p=1741`, blockers `{61,349}`;
- `p=1861`, blockers `{61,373}`;
- `p=2029`, blockers `{157}`;
- `p=2221`, blockers `{37,61}`;
- `p=2749`, blockers `{229}`;
- `p=3181`, blockers `{61}`;
- `p=3541`, blockers `{61,709}`.

Their relevant cancellation half-orders are

- `s_37=9`,
- `s_61=15`,
- `s_157=13`,
- `s_229=19`,
- `s_349=87`,
- `s_373=93`,
- `s_709=177`.

Two cases are now ruled out for every p-neutral, class-19-nonpositive repair:

1. `q=37` is 19-dirty because `h_19=9 | s_37=9`. Therefore any cloud with negative 37-defect necessarily gives positive branch-19 defect. This blocks `p=2221`.
2. `q=229` is 19-dirty because `19 | s_229=19`. Therefore any cloud with negative 229-defect necessarily gives positive branch-19 defect. This blocks `p=2749`.

In both cases the original class-19 defect at the primitive p-endpoint is zero. Since the target p defect is one and the repair is p-neutral, waking any class-19 branch to defect at least one produces a tie and prevents strict uniform novelty.

The remaining seven cases admit explicit finite certificates. Writing the full carrier as `e_h` plus the listed support ports, every earlier target branch has defect `<=0` and branch p has defect exactly `1`:

- `p=733`, `h=366`: add `e_11085` (`11085=15*739`).
- `p=1021`, `h=510`: add `e_15465` (`15465=15*1031`).
- `p=1741`, `h=870`: add `e_151989` (`87*1747`) and `e_26295` (`15*1753`).
- `p=1861`, `h=930`: add `e_173631` (`93*1867`) and `e_28065` (`15*1871`).
- `p=2029`, `h=1014`: add `e_26507` (`13*2039`) and four clean base-13 suppressors `e_6159,e_6189,e_6207,e_6243`.
- `p=3181`, `h=1590`: add `e_47805` (`15*3187`).
- `p=3541`, `h=1770`: add `e_627819` (`177*3547`), the exact p-compensation `e_3541`, and `e_53355` (`15*3557`).

The `p=3541,q=709` certificate is the first finite census example here where the q-cancellation progression is nested inside the p-cancellation progression:

`s_709=177=3*59=3s_3541`.

Thus `e_627819` lowers both q and p by one, and the own p-power port `e_3541` restores exactly the target unit without affecting any earlier branch.

The `p=2029,q=157` certificate shows a different residual: `s_157=13` gives positive base-13 denominator spill. The four clean base-13 ports pay the pre-existing base-13 depth plus that one new unit while leaving all other earlier targets unchanged.

Therefore, within this bounded primitive-endpoint census and under the exact p-neutral/class-19-nonpositive repair regime, the former nine unresolved class-13-only cases split into

`7 constructively rescued + 2 structurally obstructed`.

This is a finite classification, not an infinitude or density statement.

## 6. Independent falsification/regression

Checker:

`research_checks/check_brc_class13_pneutral_suppressor_cloud_20260924.py`.

Checker publication commit:

`94cb469e4c7f94599fd5749069874cc21e0b2ad1`.

The checker independently reconstructs target primes, multiplicative orders, coefficient valuations and the exact branch-defect cocycle. Results before publication:

- target primes `<5000`: `166`;
- higher class-13 targets: `82`;
- 19-clean higher class-13 q: `38`;
- 19-dirty higher class-13 q: `44`;
- clean `(q,p)` constructive pairs checked: `1672`;
- q-specific p-neutral construction failures: `0`;
- class-19-neutrality failures: `0`;
- reproduced class-13-only primitive-endpoint cases: exactly the nine listed above;
- explicit rescued certificates: `7/7` passed against every earlier target branch;
- obstruction cases: exactly `p=2221` via `q=37 -> r=19`, and `p=2749` via `q=229 -> r=19`;
- total failures: `0`.

Finite computation is falsification/regression only. The proof is Theorems 2.1 and 3.1 plus the exact branch-defect cocycle.

## 7. BRC meaning

The source-coefficient cancellation port is not “negative mass” in isolation. It is a provenance-bearing branch operation that can suppress one class-13 record, remain neutral on the target branch after an explicit compensation coordinate, and still be forbidden by a class-19 observer that has no cancellation channel.

The smallest sufficient carrier for this repair problem therefore includes:

- target p defect;
- blocker q cancellation step `s_q` and depth `c_q`;
- class-19 endpoint/denominator incidence on `s_q`;
- the nested p-cancellation flag;
- the compensation port when nested;
- the current uniform record source.

Collapsing those coordinates to a single signed defect would erase the obstruction proved in Theorem 2.1.

## 8. Do not repeat / next

Do not revisit class-19-positive primitive blockers with p-neutral cancellation clouds; the Driver obstruction already rules them out.

Do not retry `q=37` or `q=229` as class-19-neutral suppressors; Theorem 2.1 now proves those attempts cannot succeed.

If the formal D24 successor lifecycle remains blocked, the next nonredundant auxiliary question is to lift the lower-triangular class-13 suppression construction from this bounded nine-case census to an exact finite closure algorithm on the class-13 suppressor graph, retaining the q-specific signed cross-defect matrix rather than only Boolean incidence.

If the control service exposes the canonical lossless staging-disposition/session-rollover operation, stop auxiliary work immediately and return to the Source-native D24 continuation path.

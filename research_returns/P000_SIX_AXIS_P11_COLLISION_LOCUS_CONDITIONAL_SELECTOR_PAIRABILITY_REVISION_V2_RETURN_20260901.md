# P000 six-axis P11 pairability-filtered collision locus revision V2 — Research Return

Status: `SUCCESS / EXACT_PAIRABILITY_FILTERED_COLLISION_LOCUS_WITH_ONE_BIT_ONLY_ON_ADMISSIBLE_DOUBLETONS / DERIVED-ONLY / DRIVER_REVIEW_PENDING`

- Task: `RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR`
- Publication: `TP2-E899F20BC1B62973D07C` (Generation 2; supersedes `TP2-3DEA87F0F4ED366BEE03`)
- Researcher: `EM-P000P11C2-6F42A1`
- Claim: `chatgpt-p000p11c2-20260901-1043-6f42a1`
- Execution record: `ER-3253C0D0495870F1C434`
- Result: `RR-16ADB5F4DE72A332B509`
- Parent accepted Result: `RR-B96585874709743F94BC`
- Retained Generation-1 Result: `RR-C3E71A9D4B6052F88E21`
- Driver revision authority: `DR-C5539B165E52AAAA3C6A`
- Taskbook: `research_tasks/P000_SIX_AXIS_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR_PAIRABILITY_REVISION_V2_20260831.md` / `sha1:15f8b2a063f900bcd0ff317d0c216e5d0d97bf7f`

Hard target:
`P000_P11_PAIRABILITY_FILTERED_ADMISSIBLE_COLLISION_LOCUS_AND_CONDITIONAL_SELECTOR_EXACTLY_CLASSIFIED_OR_FROZEN_RESOLVENT_ROUTE_OBSTRUCTED`.

Terminal disposition:
`EXACT_PAIRABILITY_FILTERED_COLLISION_LOCUS_WITH_ONE_BIT_ONLY_ON_ADMISSIBLE_DOUBLETONS`.

## 1. Corrected theorem

Let the already-known integer marginals be sorted as

`H=(h0,h1,h2)`, `T=(t0,t1,t2)`,

and for `sigma in S3` define

`K_sigma = multiset{(h_i,t_sigma(i)) : i=0,1,2}`,

`P11(sigma)=sum_i h_i t_sigma(i)`,

with `P21` and `P12` defined as in Generation 1.

For one local pair define the frozen admissibility predicate

`Pair(h,t) <=> Delta(h,t)=h^2-4t is a nonnegative square d^2 and d ≡ h (mod 2)`.

For an alignment define

`Adm(sigma) <=> AND_i Pair(h_i,t_sigma(i))`.

Finally define the actual admissible fibre

`F_adm(H,T,p) = { K_sigma : P11(sigma)=p and Adm(sigma) }`

after the already-frozen `K/Gamma` deduplication.

Generation 1 remains correct at the **combinatorial** level.  On fully distinct marginals, with positive gaps

`A=h1-h0`, `B=h2-h1`, `C=t1-t0`, `D=t2-t1`,

the only algebraic equal-`P11` pairs are

- `C1: AC=BD`, pair `132/213`;
- `C2: AD=BC`, pair `231/312`.

Repeated-`H` or repeated-`T` strata remain combinatorially injective.

The corrected admissible theorem is therefore exact and very simple:

### C1 level

When `AC=BD`, put

`a132 = Adm(132)`,
`a213 = Adm(213)`.

Then

`|F_adm(H,T,P11(132))| = a132 + a213`.

Equivalently, a genuine two-admissible-orbit `C1` fibre exists iff all six local predicates hold:

`Pair(h0,t0)`,
`Pair(h1,t2)`,
`Pair(h2,t1)`,
`Pair(h0,t1)`,
`Pair(h1,t0)`,
`Pair(h2,t2)`.

### C2 level

When `AD=BC`, put

`a231 = Adm(231)`,
`a312 = Adm(312)`.

Then

`|F_adm(H,T,P11(231))| = a231 + a312`.

Equivalently, a genuine two-admissible-orbit `C2` fibre exists iff all six local predicates hold:

`Pair(h0,t1)`,
`Pair(h1,t2)`,
`Pair(h2,t0)`,
`Pair(h0,t2)`,
`Pair(h1,t0)`,
`Pair(h2,t1)`.

This is necessary and sufficient because the retained Generation-1 collision theorem proves that no third combinatorial packet has the same `P11`.  Pairability only deletes candidate packets; it cannot create new ones.

Hence every algebraic collision level is classified exactly as

- `ZERO_ADMISSIBLE` if both packet predicates fail;
- `ONE_ADMISSIBLE` if exactly one succeeds;
- `TWO_ADMISSIBLE` if both succeed.

A valid task input is, by definition, realized by at least one integer-pairable packet, so only the latter two occur for the observed `P11`.

Globally,

`|F_adm(H,T,p)| <= |F_comb(H,T,p)| <= 2`.

If either marginal has a repeated value, the Generation-1 affine injectivity proof already gives `|F_comb|<=1`, therefore every valid repeated-marginal admissible fibre has size exactly one.

## 2. Why this is the exact correction rather than a new grammar

No new invariant is needed.  The defect in Generation 1 is purely the order of operations:

1. enumerate the at-most-two algebraic packets at fixed `H,T,P11`;
2. **filter each whole packet through `Adm`**;
3. only then measure residual information.

The admissibility test is already part of the frozen six-coordinate arithmetic interface.  Therefore the revision does not add a higher mixed moment, native orientation, signed carrier, factorization, dimension reduction, or Full-Cell semantics.

## 3. Gram/Vandermonde resolvents survive unchanged

The Generation-1 symmetric quadratics remain valid algebraic candidate resolvents.

For `X=P21`, with `V_H`, `G_H=V_H V_H^T`, `Delta_H=det(G_H)` and `m_X=[S_T,p,X]^T`,

`Q21(X) = m_X^T adj(G_H) m_X - Delta_H * sum_j t_j^2`.

Dually, for `Y=P12`,

`Q12(Y) = m_Y^T adj(G_T) m_Y - Delta_T * sum_i h_i^2`.

On a combinatorial `C1` or `C2` double level, the two algebraic packets still produce exactly the two roots of each quadratic.

The correction is downstream of the quadratic:

- `ZERO_ADMISSIBLE`: both reconstructed packets fail the frozen pairability gate; there is no valid observed state at that level.
- `ONE_ADMISSIBLE`: both algebraic roots remain roots, but exactly one reconstructed packet satisfies all three local pairability predicates.  The other root is an **algebraic ghost**, not a second admissible state.
- `TWO_ADMISSIBLE`: both roots reconstruct admissible packets and are exactly the two states of `F_adm`.

Thus the quadratic is a **candidate resolvent**, not an admissibility oracle.  Filtering its reconstructed packets is mathematically necessary.

The retained branch-order law also survives exactly where it is meaningful:

- on a genuine `C1` doubleton, numeric `P21` and `P12` root ordering selects the same packet;
- on a genuine `C2` doubleton, the two root orderings select opposite packets.

No such binary relation is needed on a singleton.

## 4. Mandatory Driver falsifier is now a positive regression

Take

`H=(-2,0,2)`, `T=(-1,0,1)`.

Then `A=B=2`, `C=D=1`, so both algebraic collision equations hold.

### C1: `P11=2`

The algebraic pair is `132/213`.

- `132 = {(-2,-1),(0,1),(2,0)}` is nonadmissible:
  `Delta(-2,-1)=8` is not a square and `Delta(0,1)=-4`.
- `213 = {(-2,0),(0,-1),(2,1)}` is admissible, with root pairs
  `{-2,0}`, `{-1,1}`, `{1,1}`.

Therefore `|F_adm|=1` and the selector cost is `0` bits.

The algebraic `P21` roots are `-4,4`; the algebraic `P12` roots are `-2,2`.  The roots corresponding to `132` remain legitimate roots of the eliminants but reconstruct the packet that fails pairability.

### C2: `P11=-2`

The algebraic pair is `231/312`.

- `231 = {(-2,0),(0,1),(2,-1)}` is nonadmissible.
- `312 = {(-2,1),(0,-1),(2,0)}` is admissible, with root pairs
  `{-1,-1}`, `{-1,1}`, `{0,2}`.

Again `|F_adm|=1` and the selector cost is `0` bits.

This exactly repairs the Driver counterexample without changing the retained algebra.

## 5. New audit: simultaneous C1+C2 does not imply equal selector cost on the two levels

Generation 1 correctly proved that simultaneous `C1+C2` forces `A=B` and `C=D` and produces two disjoint algebraic double levels.  Pairability adds a new distinction: the two levels need not have the same admissible cardinality.

Exact witness:

`H=(1,4,7)`, `T=(-60,-30,0)`.

Here `A=B=3`, `C=D=30`, so both collision equations hold.

### C1 level: `P11=-270`

`132` is nonadmissible because `(1,-60)` has discriminant `241`, not a square.

`213` is admissible:

- `(1,-30) -> roots {-5,6}`;
- `(4,-60) -> roots {-6,10}`;
- `(7,0) -> roots {0,7}`.

Hence the C1 level is a singleton and costs `0` bits.

### C2 level: `P11=-450`

Both packets are admissible.

`231`:

- `(1,-30) -> {-5,6}`;
- `(4,0) -> {0,4}`;
- `(7,-60) -> {-5,12}`.

`312`:

- `(1,0) -> {0,1}`;
- `(4,-60) -> {-6,10}`;
- `(7,-30) -> {-3,10}`.

Hence the C2 level is a genuine doubleton and costs `1` bit.

Its two `P21` values are `-2970,-2430` and its two `P12` values are `26100,20700`, exhibiting the retained C2 opposite-root-order relation.  On the C1 level the algebraic values are `P21=-1530,-990` and `P12=9900,15300`, but only the second packet is admissible.

**Consequence:** selector cost is a function of the actual level
`(H,T,P11)`, not a single flag attached to `(H,T)` or to membership in `C1 union C2`.

## 6. Exact selector and information law

Given a valid packet `(H,T,p)`:

1. enumerate the distinct `K/Gamma` alignments with `P11=p`;
2. apply `Adm` to every candidate packet;
3. the surviving set is `F_adm(H,T,p)` and has size `1` or `2`;
4. if it has size `1`, return that packet with no side bit;
5. if it has size `2`, order the two `Q21` roots increasingly and use one branch bit to select the corresponding reconstructed packet.

No separate collision flag is required because the receiver already has `H,T,p` and can reproduce both the algebraic candidate set and the pairability filtering.

The exact fixed-instance residue is

`I_selector(H,T,p) = log2 |F_adm(H,T,p)|`.

Thus:

- admissible singleton: `0` bits, including one-branch algebraic collisions;
- admissible doubleton: `1` bit;
- zero-admissible algebraic level: no valid task state.

Worst-case extra alignment information remains exactly one bit, but **not** on every algebraic collision level.

## 7. Retained genuine doubleton witnesses and minimality

Driver review explicitly retained the Generation-1 exact root-box result: in the frozen local-root metric

`R_B = {(a+b,ab): a<=b, |a|,|b|<=B}`,

the first genuine pairable two-branch witness occurs at `B=6` for both classes, with no witness for `B<=5`.

The frozen minimal witnesses remain:

### C1

`H=(-1,1,4)`, `T=(-30,-12,0)`, `P11=-18`.

Both `132` and `213` are admissible.

`P21=(-222,-42)`, `P12=(-324,756)`; root order is SAME.

### C2

`H=(-4,-1,1)`, `T=(-30,-12,0)`, `P11=18`.

Both `231` and `312` are admissible.

`P21=(-222,-42)`, while assignment-order `P12=(324,-756)`; root order is OPPOSITE.

For every integer `m>=1`, scaling local roots by `m` sends `H -> mH`, `T -> m^2 T`, preserves pairability, preserves C1/C2, and preserves doubleton status.  The new checker rechecks the endpoint witnesses and twelve scaling factors per class.  The expensive `B<=6` minimality census itself is retained by immutable dependency rather than re-authored.

## 8. Deterministic exact control

The Generation-2 checker directly computes `F_adm` rather than inferring it from combinatorial collision classes.

Frozen run:

`PASS P000_P11_PAIRABILITY_FILTERED_V2 direct_cases=48400 valid_fibres=2923 direct_doubletons=2 max_adm_fibre=2 repeated_valid_max=1 algebraic_C1_0=286 algebraic_C1_1=8 algebraic_C1_2=1 algebraic_C2_0=350 algebraic_C2_1=11 algebraic_C2_2=1 resolvent_collision_checks=657 witness_checks=2 scale_checks=24 driver_falsifier=C1:1|C2:1 mixed_levels=C1:1|C2:2 retained_rootbox_min=B6 selector_bits=log2_admissible_fibre`

The finite control uses the fixed value set

`{-30,-12,-4,-2,-1,0,1,2,4,7}`

for both sorted marginals, enumerates all `220^2=48,400` multiset pairs, computes every distinct alignment, filters each packet by exact `isqrt` square/parity pairability, and only then groups by `P11`.

This finite control is regression evidence, not the proof of the global bound.  The global bound follows symbolically because `F_adm` is a subset of the already-proved combinatorial fibre and the latter has size at most two.

## 9. Reconciliation of Generation-1 claims

| Generation-1 claim | Generation-2 disposition |
|---|---|
| C1 `AC=BD` and C2 `AD=BC` are the only distinct-stratum equal-P11 classes | **RETAINED**, combinatorial only |
| repeated marginal strata are injective | **RETAINED**, hence admissible valid fibres are singleton |
| simultaneous C1+C2 gives two disjoint doubled levels, no triple | **RETAINED algebraically** |
| Gram/Vandermonde quadratics give the two candidate second-moment roots | **RETAINED as candidate resolvents** |
| same/opp P21/P12 branch relation | **RETAINED on TWO_ADMISSIBLE fibres** |
| B=6 first genuine pairable witness for each class | **RETAINED by Driver-reviewed exact evidence** |
| `1 bit on collision locus` | **CORRECTED** |
| corrected information law | `log2 |F_adm(H,T,P11)|`, 0 on singleton and 1 exactly on admissible doubleton |

## 10. Attribution and firewall

The assignment-collision geometry, Vandermonde/Gram elimination, symmetric/multisymmetric invariant perspective, perfect-square discriminant test, and finite permutation enumeration are classical/elementary ingredients.  This Return makes no historical novelty claim.

Everything remains a derived six-coordinate arithmetic facade.  In particular this Result does **not**:

- select a native orientation or Pfaffian negative slot;
- promote any signed carrier to P000 ontology;
- infer dimension reduction or factorization;
- enter Full-Cell dynamics;
- enlarge the mixed-moment grammar;
- grant Working Truth, Foundation authority, or canonical promotion.

## 11. Driver handoff

Requested review disposition:

`ACCEPT at EXACT_PAIRABILITY_FILTERED_COLLISION_LOCUS_WITH_ONE_BIT_ONLY_ON_ADMISSIBLE_DOUBLETONS strength`.

If accepted, the exact practical statement is:

> The algebraic C1/C2 equations enumerate at most two candidate packets, but the side-information residue is measured only after packetwise integer pairability.  The candidate quadratic resolvent survives unchanged; pairability removes algebraic ghost roots at singleton levels.  One bit is required exactly on genuine admissible doubletons and nowhere else.

No downstream task decision is made from the Researcher lane.

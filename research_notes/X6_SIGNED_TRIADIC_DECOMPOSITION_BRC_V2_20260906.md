# X6 triadic decomposition V2: signed macro-force lift, exact generating functions and BRC multiplicity

Status: `FREE_RESEARCH / EXACT COMBINATORIAL DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- P000 primitive stable balance = triadic closure;
- V1 atomic scatter on all 20 distinct-axis selections and all 8 sign patterns;
- previous equal-unit degree-sequence decomposition criterion.
Checker: `experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py`.

## 1. Macro forces are populations of primitive signed quanta

P000 makes the primitive object a `PRIMITIVE_FORCE_QUANTUM`, and stable configurations with more than three quanta are nonprimitive composites requiring triadic decomposition.

For axis `i` record signed quantum counts

`d_i^+ , d_i^- in N_0`,

and aggregated unsigned-axis demand

`D_i=d_i^+ + d_i^-`.

Let

`N=sum_i D_i`.

A primitive signed triad uses exactly three **distinct underlying native axes**, with one arbitrary sign choice on each. The existing atomic scatter theorem realizes all

`C(6,3)*2^3 = 20*8 = 160`

such signed atomic types.

Thus the macro problem is to partition the signed quantum population into members of this 160-type atomic family.

## 2. Existence theorem for a macro triadic decomposition

Suppose `N=3m`. Then a decomposition into `m` primitive triads exists iff

`max_i D_i <= m`.

Equivalently:

`sum_i D_i=3m` and `D_i<=m` for every axis.

### Necessity

There are `m` triad events and one triad can use a fixed underlying axis at most once, so axis `i` can appear at most `m` times.

### Sufficiency by induction

Assume `m>0`. Let

`P={i:D_i=m}`.

Because `sum D_i=3m`, at most three axes lie in `P`. At least three axes have positive demand. Choose a three-axis set `S` containing every member of `P` and fill the remaining slots with positive-demand axes.

Remove one quantum from every axis in `S`. The residual degree vector has total `3(m-1)`. Every former maximum `m` was selected and drops to `m-1`; every unselected axis was already at most `m-1`. Hence the residual maximum is at most `m-1`.

Induction constructs the remaining `m-1` triads.

The signs introduce no new existence obstruction because every signed pattern on a chosen distinct-axis triple is an admitted atomic type. Once the underlying axis incidences are constructed, assign the required plus/minus occurrences to each axis's incidence slots.

This closes the equal-unit macro stability existence problem for the current atomic model.

## 3. Ordered underlying decomposition count

Let

`e_3(x_1,...,x_6)=sum_{|S|=3} product_{i in S}x_i`.

For an aggregated degree vector `D` with total `3m`, the number of **ordered/labeled triad-event type sequences** is

`N_ord(D)=[x_1^{D_1}...x_6^{D_6}] e_3(x)^m`.

This is exactly an N-BRC multiplicity when event order/type provenance is retained but individual quanta on one signed direction are indistinguishable.

For example:

`D=(1,1,1,1,1,1)`, `m=2` gives

`N_ord=20`.

The corresponding unordered underlying decompositions are the 10 complementary partitions of six axes into two triples.

For

`D=(2,2,2,2,2,2)`, `m=4`,

exact counts are

`N_ord=1860`,

`N_unord=85`.

So decomposition provenance grows quickly even before path/rotation histories inside each atomic event are added.

## 4. Signed atomic generating polynomial

Introduce variables `x_i^+,x_i^-` and define

`T(x)=sum_{|S|=3} product_{i in S}(x_i^+ + x_i^-)`.

Equivalently,

`T=e_3(x_1^+ + x_1^-, ..., x_6^+ + x_6^-)`.

It contains exactly the 160 signed atomic triad monomials.

The ordered signed decomposition count is

`N_ord^±(d)=[x^d] T(x)^m`.

Because the underlying axis degree `D_i` is fixed, the coefficient factorizes exactly:

`N_ord^±(d)=N_ord(D) * product_i C(D_i,d_i^+)`.

Proof: first choose the ordered underlying triad incidence sequence; axis `i` then has `D_i` distinct event slots, and exactly `d_i^+` of them must receive the plus sign.

The checker verifies the formula exhaustively over the complete one-event and two-event signed populations generated from all 160 atomic types.

## 5. If primitive quanta are individually labeled

Suppose every primitive quantum occurrence is distinguishable in Path-formal provenance.

For a fixed ordered underlying incidence sequence, axis `i` has `D_i` event slots. Choosing which are plus and assigning labeled plus/minus occurrences gives

`C(D_i,d_i^+) d_i^+! d_i^-! = D_i!`.

Therefore the complete labeled-quantum multiplicity above the ordered underlying type population is

`N_labeled(d)=N_ord(D) * product_i D_i!`.

Notably this labeled multiplicity depends on the aggregated axis counts `D_i`, not on how those labels split between plus and minus after the signed counts themselves are fixed.

This is a higher-provenance BRC layer, not the same observer as the signed type count.

## 6. Unordered decomposition generating function

If triad events are treated as an unordered multiset rather than a time-ordered event sequence, use one variable `y` for event count and one monomial `x^tau` for every admitted signed atomic type `tau`.

Then

`Z_unord(y,x)=product_{tau in T_160} (1-y x^tau)^(-1)`.

The coefficient

`[y^m x^d] Z_unord`

is the exact unordered signed decomposition multiplicity.

At the unsigned level replace the 160 signed types by the 20 underlying three-axis subsets.

Ordered and unordered multiplicities answer different time/provenance questions and must not be silently interchanged.

## 7. BRC hierarchy for macro stability

The current macro-force carrier naturally has several levels:

1. **Boolean stability support** — does at least one triadic decomposition exist?
2. **unordered triad-type BRC** — how many simultaneous decomposition multisets exist?
3. **ordered triad-event N-BRC** — how many event-type sequences exist?
4. **signed type BRC** — retain plus/minus incidence assignment;
5. **labeled-quantum Path-formal layer** — retain individual primitive quantum provenance;
6. **atomic Cell-path layer** — for every triad event, retain/derive its correlated `III` microtrace under the atomic closure law.

The existence theorem allows collapse from richer levels to Boolean stability under a future language asking only existence, but not under observers that inspect decomposition route, event order or force provenance.

## 8. Factorized per-axis weights cannot select a decomposition route

Suppose a positive weight factorizes completely over signed primitive directions:

`w(tau)=product_{(i,s) in tau} q_{i,s}`.

For any complete decomposition with the same signed count vector `d`, the product of all atomic weights is

`product_{i,s} q_{i,s}^{d_i^s}`, 

independent of which triad decomposition was used.

Therefore factorized signed-axis weights multiply every decomposition branch by the same common factor and **cannot distinguish or select triadic decomposition provenance**.

To favor one decomposition over another, a weighting law must contain at least one genuinely interaction-sensitive term, e.g. triad-type weight `w_{S,s}`, neighboring-event coupling, history dependence or another non-factorized relation.

This is an exact BRC observer/law-selection no-go.

## 9. General weighted ordered partition function

For exact positive-rational triad-type weights `w_tau`, define

`T_w(x)=sum_{tau in T_160} w_tau x^tau`.

Then

`Z_m(d;w)=[x^d] T_w(x)^m`

is the exact ordered Weighted-BRC mass of signed triadic decompositions.

This reuses the existing Weighted-BRC semantics; it does not create a new general-purpose tool family.

If weights factor per signed axis, `Z_m` reduces to the unweighted count times the common factor from section 8.

## 10. Relation to time and dependency traces

`N_ord` counts fully serialized triad events. If some triad events are certified independent under the current dependency-time rule, serializations related only by swaps of independent events may be quotiented to one dependency trace.

Thus:

`ordered triad BRC -> dependency-trace BRC -> unordered simultaneous decomposition`

are different possible observers. The final arrow is not generally safe when noncommuting neighboring interactions or timing queries remain.

The generating functions above keep these distinctions explicit rather than treating one count as universal.

## 11. Current macro-force frontier

Closed for equal primitive quanta in the current all-20 atomic triad model:

- exact signed macro input type `d_i^±`;
- decomposition existence iff `sum D_i=3m` and `max D_i<=m`;
- exact ordered underlying coefficient formula;
- exact signed ordered factorization;
- labeled-quantum multiplicity;
- exact unordered signed generating function;
- factorized-axis-weight route-selection no-go;
- weighted triad-type partition function.

Still open:

1. genuinely unequal **primitive** quantum magnitudes if P000 later admits more than one primitive magnitude unit rather than repeated unit quanta;
2. multi-Cell triadic networks with shared resources and nontrivial dependency constraints;
3. non-factorized physical interaction weights;
4. coupling of decomposition BRC to energy/duration calibration or PDE readouts.

No Foundation promotion or external novelty claim is made.

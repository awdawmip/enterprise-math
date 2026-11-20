# X6 r415 — Sharp bounded-prefix calibration and stabilizer-automaton repair budgets

Date: 2026-11-20 (Asia/Shanghai).
Status: **author-side exact mathematical result**, not Native Result acceptance, independent Driver Review, or an established physical X6 rotation.
New mathematical contribution: Driver EM-DVR-DEBB5E. Original X6 contributors EM-EMF6D046-5A2844, EM-X6-DFD1FD and EM-X6CM-EDBD55 retain their attribution.
Continues the separately sourced r411–r414 static-frame results, in particular r414@85d0d6e93dded6bc96e05fa0ce41bea164cf51a8. P000 and the Heartbeat X6 time/Cell and joint-observer preservation contracts remain the native boundary.

## Theorem A: exact finite-horizon information repair for the signed six-axis alphabet

Let `H = (C2)^6 ⋊ A6` act simultaneously, letter by letter, on the signed alphabet `Σ={±e1,…,±e6}`. Choose a **fixed** signed-letter suffix `s` mentioning exactly `k` distinct unsigned axes, and observe the global orbit `O_s(u)=[us]_H`, restricted to prefixes `u` of **exactly** `n` primitive signed letters. Put `m=6-k`, `r=min(n,m)`, and

`a(t)=t!/2` for `t≥2`, while `a(0)=a(1)=1`.

Then the maximum number of distinct prefixes in one observer fiber is precisely

`M(k,n) = 2^r a(m)/a(m-r)`.

Consequently the smallest **uniform fixed-width auxiliary tag**, in addition to the entire orbit datum and the known fixed suffix, that makes the observation injective on all length-`n` prefixes has length

`b(k,n) = ceil(log2 M(k,n))` bits.

The same maximum holds for prefixes of length **at most** `n` (provided an empty word is included). In particular, the unbounded-horizon r414 result is attained as soon as `n≥6-k`; before that, fewer bits may suffice.

### Proof

The stabilizer `K_s=Stab_H(s)` consists of arbitrary sign flips on the `m` axes absent from `s`, together with even permutations of those unused axes. Thus `|K_s|=2^m a(m)`. The orbit observation fiber for any fixed-length prefix `u` is exactly `K_s·u` (r414); the global orbit representative fixes the common suffix and hence belongs to `K_s`.

Let `r_u` count the **distinct unused axes** occurring in `u`. A group element fixing `u` must fix those axes and their signs, as well as all suffix axes. The remaining `m-r_u` unused axes admit `2^(m-r_u) a(m-r_u)` sign/permutation transformations. Orbit–stabilizer gives

`|K_s·u| = 2^r_u a(m)/a(m-r_u)`.

The orbit size cannot decrease as new distinct unused axes appear, since pointwise stabilizers can only shrink. The maximum `r_u=min(n,m)` is attained by listing that many different positive unused-axis letters and, when needed, repeating any existing alphabet letter. Therefore the displayed `M(k,n)` is sharp. Distinct elements of one fiber demand distinct tags; conversely shortlex ranking inside each finite fiber attains `ceil(log2 M)`. The maximum for lengths at most `n` is attained by a length-`n` word. QED.

### Exact bit table

Columns are the prefix horizon `n`. For `n≥6` all rows have reached the r414 unbounded value.

| distinct suffix axes k | n=0 | n=1 | n=2 | n=3 | n=4 | n=5 | n≥6 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 4 | 7 | 10 | 13 | 14 | 15 |
| 1 | 0 | 4 | 7 | 9 | 10 | 11 | 11 |
| 2 | 0 | 3 | 6 | 7 | 8 | 8 | 8 |
| 3 | 0 | 3 | 4 | 5 | 5 | 5 | 5 |
| 4 | 0 | 1 | 2 | 2 | 2 | 2 | 2 |
| 5 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

For a three-axis suffix, **one further signed primitive letter** needs at most and sometimes exactly 3 repair bits; **two** need 4; **three or more** need 5. The r414 five-bit lower bound was an unbounded-prefix worst-case statement and is now sharpened for bounded horizons.

## Theorem B: exact repair-budget computation for a regular H-equivariant legal event language

Let a finite group `H` act letterwise on a finite event set `E`, with an injective fixed-length H-equivariant encoding into primitive letters. Let `L⊆E*` be recognized by a DFA `(Q,E,δ,q0,F)` and globally H-invariant. Fix a legal suffix `s∈E*`. Put `K=Stab_H(s)`, `U_s={u:us∈L}`; a suffix stabilizer of the encoded word agrees with the event stabilizer by injectivity/equivariance.

An exact (possibly unbounded-horizon) minimum repair-bit computation uses a **finite subgroup-state automaton**:

1. Begin at `(q0,K)`.
2. Reading event `e`, update `(q,J) -> (δ(q,e), J ∩ Stab_K(e))`, where `Stab_K(e)={g∈K:g e=e}`.
3. Accept those reachable states `(q,J)` for which `δ*(q,s)∈F`.
4. If any accepting state exists, set `J_min` to the smallest cardinality among their subgroup components. Then

`M_s = |K| / |J_min|`, and `b_min = ceil(log2 M_s)`.

If `U_s` is empty, the encoding problem is vacuous and `b_min=0`. To restrict to prefixes of length at most `n`, retain a length counter up to `n` in the search; for exactly `n`, accept only at depth `n`.

**Proof.** By induction on the read word, the second automaton coordinate is precisely `Stab_K(u)`: a group element fixes an ordered word if and only if it fixes each event label in it. The first coordinate is `δ*(q0,u)`; suffix acceptance is exactly `us∈L`. The H-invariance of `L` implies `U_s` is K-invariant. Hence each legal fiber is the entire K-orbit of its prefix, with size `|K|/|Stab_K(u)|`. A finite graph search enumerates precisely reachable `(q,J)` pairs, so minimizing subgroup order maximizes the fiber and gives the sharp number of tag bits via r414's elementary fiber-coloring argument. A cycle does not create additional subgroup states once the finite pair repeats. QED.

The finite state space is bounded by `|Q|·|Sub(K)|`, with each transition costing the subgroup intersection representation used. This is an exact decidability bound, **not** a claim of polynomial complexity in the bit-length of an arbitrary input group or DFA.

### Triadic-candidate consequence and limitations

For the candidate alphabet of 960 ordered signed triples on distinct axes, a suffix `s=(e1,e2,e3)` fixes three axes, so `|K|=24`. Under the free **candidate** event language `E*`, a single legal event `(e4,e5,e6)` already has trivial K-stabilizer; hence **one event** can require the full five bits, even though one single primitive signed *letter* with the same suffix requires only three. Under the repeat-only H-equivariant candidate language of r413, zero bits suffice. Event count and primitive-letter count are therefore distinct horizons.

These statements are about the candidate static group and explicitly declared languages. The native P000 `TRIADIC_CLOSURE_E` incidence, actual Cell/Port/branch and time succession, and preservation under future physical operations remain open inputs; no dynamic legality, physical rotation or total Cell-state compression is inferred from a static orbit. The supplemental tag cost excludes base-orbit serialization, reconstruction, legality-oracle and time/branch provenance costs.

## Reproducible arithmetic / finite-check scope

For each `k,n∈{0,…,6}`, independently enumerated all 360 even permutations of the six axes and the compatible unused-axis sign flips, computed the complete orbit of a prefix with `min(n,6-k)` distinct unused axes, and compared the exact orbit cardinality to `2^r a(m)/a(m-r)`: **49/49 cases matched**. The table is formed by integer `ceil(log2 M)`. This checks those explicitly stated finite cases; the general theorem is proved above by orbit–stabilizer, not by extrapolation.

Provenance: r411@5e3d07b0; r412@7d98fdd1; r413@e86c1ef0; r414@85d0d6e9, plus P000 and observer-preservation definitions. Current note is independently reproducible author-side work of EM-DVR-DEBB5E, not an independent review of its own r411–r414. No preexisting X6 researcher identity, live CLAIM, formal Native Result, Activity record, mother Objective or Task status is modified by this GitHub publication.

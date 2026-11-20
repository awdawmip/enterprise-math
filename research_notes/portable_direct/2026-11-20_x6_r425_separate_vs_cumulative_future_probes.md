# X6 r425 — Separate one-step probes are not equivalent to a cumulative future path

Date: 2026-11-20. **Author-side finite-group theorem** extending the source-published r423 and r424. This is not independent Native Review, Native Result acceptance, or a claim about full triadic Cell/Port/branch/time dynamics.

## Exact question and provenance

Source antecedents:
- r423: `enterprise-math@9af7cca8ab1c62471c6da1c446a7843956cb562a:research_notes/portable_direct/2026-11-20_x6_r423_repeated_axis_paths_hidden_parity.md`.
- r424: `enterprise-math@c83635cd2e7c57dd2e664fc5df940bc041f30d40:research_notes/portable_direct/2026-11-20_x6_r424_one_step_future_parity_probe.md`.
- Native spatial coordinate adjacency (not the complete triadic event law): `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`.

This result belongs to the existing RESEARCH_DRIVER mathematical continuation line `EM-DVR-DEBB5E`; it preserves separate preceding X6 authors and does not claim a new official Task/Result.

Question: suppose an observer separately tries several common fixed-labelled next-axis commands, resetting to the same historical prefix for each experiment. Does collecting *all* those one-step observations reveal as much as following one common future path containing the same commands? **In general, no.**

## Domain and notation

Retain precisely r423's `B6 = (C2)^6 ⋊ S6` letterwise action on the signed six-axis alphabet. Its five candidate groups are `B6`, `G_S=ker q`, `G_+=ker(pq)`, `G_A=ker p`, `D=ker p∩ker q`, where `p=sgn(permutation)` and `q=product(signs)`.

Let `c∈N_0^6`, `W_c` be the set of all ordered **positive** axis words with occurrence vector `c`, and `s` a fixed positive calibration suffix using distinct axis set `S`. Write
`m_t = |{i∉S: c_i=t}|` for `t≥1`,
`r = |{i∉S: c_i=0}|`, and `P=∏_{t≥1}m_t!`.

Choose a set `T⊆{1,…,6}` of distinct fixed-labelled positive future commands. Put
- `a_t = |{j∈T\S: c_j=t}|` for `t≥1`;
- `Z = {j∈T\S: c_j=0}`, `z=|Z|`;
- `P_T = ∏_{t≥1}(m_t-a_t)!`.

All observations below have the **same restricted domain** `u∈W_c`. In particular, the time-evolved word is not silently reclassified into a different unrestricted occurrence-vector family.

The baseline observation is `O_0(u)=[us]_G`. Define two materially distinct experiments:

1. **Reset/separate**: `O_T^{sep}(u)=(O_0(u),([u e_j s]_G)_{j∈T})`. Every probe starts again from the same `u`; each orbit comparison is allowed its own witnessing group element.
2. **Cumulative**: for any fixed ordering `(j_1,…,j_z')` of all elements of `T`, `O_T^{cum}(u)=([us]_G,[u e_{j_1}⋯e_{j_{z'}} s]_G)`. One group element must explain the entire common future word. The fiber formula does not depend on the order of its distinct future labels.

For a positive integer `P'`, let `E(P')=P'/2` if `P'>1`, and `E(1)=1`. For each candidate group use the parity-reservoir threshold
`h(B6)=h(G_S)=0`, `h(G_+)=1`, `h(G_A)=h(D)=2`.
Define `H(P',R;G)=P'` if `R≥h(G)`, and `E(P')` otherwise.

## Theorem: exact joint versus cumulative fibers

For **every** `c,S,T,G` above, every nonempty fiber of the reset/separate observation has the common exact size

```
F_sep(G;c,S,T) = H(P_T, r - min(1,z); G).
```

Every nonempty fiber of the cumulative observation has the common exact size

```
F_cum(G;c,S,T) = H(P_T, r-z; G).
```

In particular,
`F_cum ≤ F_sep ≤ F_G(c,S)`. Each factor
`F_G(c,S)/F_sep` and `F_G(c,S)/F_cum` is a positive integer. The exact minimal **extra fixed-length tag** in bits, given the baseline orbit observation, to predict the separate or cumulative experiment respectively is
`ceil(log2[F_G(c,S)/F_sep])` or
`ceil(log2[F_G(c,S)/F_cum])`.

The two experiments differ in information precisely when `P_T>1` and the group's parity threshold is met after deleting at most one invisible-axis reservoir but not after deleting all `z` reservoirs:

```
r - min(1,z) ≥ h(G) > r-z.
```

This can occur only for the two parity-sensitive groups `G_+` and `G_A/D`, and requires at least two distinct originally unseen future labels. It never occurs for `B6` or `G_S`.

### Proof

Suppose `u,v∈W_c`. As each positive label occurring in `u` must map to a positive label in the same positive count block, the equality `g(u)=v` uniquely determines an effective permutation `σ` on the **used** labels of `u`. This effective permutation is the same for every attempted probe, although its extensions to unused labels and signs may differ between probes.

Every positive calibrated label in `S` is fixed. For a probe `j` with `c_j>0`, the equation `[u e_j s]_G=[v e_j s]_G` additionally forces `σ(j)=j`. Over all separately tested `j∈T`, the free effective permutations therefore form the product of symmetric groups on the `m_t-a_t` remaining uncalibrated positive-count labels. Its order is `P_T`.

For `B6,G_S`, any such effective permutation extends to the required group with positive signs. For `G_+`, an odd effective permutation can be balanced by reversing the sign on one label invisible in that *individual* comparison, requiring at least one such label. For `G_A,D`, it can be balanced by transposing two invisible labels, requiring at least two. A given individual probe `j∈Z` removes exactly one invisible label, whereas a probe on a used or previously calibrated label removes none. The odd-permutation extension must exist for **each separate comparison**, so the sharp common feasibility condition uses `r-min(1,z)`. If odd permutations are unavailable, exactly the index-two alternating part remains whenever `P_T>1`; when `P_T=1` the action is trivial. Hence `F_sep) as stated.

For a cumulative word, every orbit witness `g` must fix every future label `j∈T` simultaneously. Now all `z` originally invisible future labels are removed from the parity reservoir of that **one** group element. The same extension argument therefore uses `r-z` and gives `F_cum`.

All these effective actions on the fixed-`c` labelled word family are free on the used-label permutation: if an effective permutation fixes the ordered word `u`, it fixes every used label. Thus their orbit sizes are the stated uniform cardinalities, and counting equal subfibers proves the information-tag formulas. The strict-inequality condition follows directly from the threshold cases. QED.

## Explicit exact witnesses

**Determinant-positive candidate `G_+`.** Take `c=(1,1,1,1,0,0)`, `S=∅`, `T={5,6}`. There are 24 positive words, all within one baseline orbit: `F_G(c,S)=24`. Separate probes `e5` and `e6` each leave one invisible sign flip available and collectively **do not split** that orbit: `F_sep=24`. The cumulative two-step word `e5e6` removes both sign reservoirs, giving `F_cum=12` and exposing one bit of permutation parity. In particular `u=e1e2e3e4`, `v=e2e1e3e4` are equivalent under each separate probe (the negative sign can be carried by the *other* invisible axis), but not under their cumulative future word.

**Even-permutation candidate `G_A` or `D`.** Take `c=(1,1,1,0,0,0)`, `S=∅`, `T={4,5}`. The initial fiber has 6 words, each separate probe leaves two unseen axes available to balance odd permutation parity, and `F_sep=6`. A cumulative `e4e5` future leaves only axis 6 unseen, hence `F_cum=3`. For `u=e1e2e3`, `v=e2e1e3`, the odd transposition `(12)` extends separately using `(56)` after `e4` and using `(46)` after `e5`; no parity-balancing transposition remains after both.

**Exact finite crosschecks.** A direct enumeration over all `6!·2^6=46,080` signed permutations and positive word orbit fibers independently checked the displayed `G_+`, `G_A` and `D` witnesses (initial / separate / cumulative respectively: `24/24/12`, `6/6/3`, `6/6/3`). The proof covers all `c,S,T,G`; the enumerations are finite corroboration, not a claim of exhaustive verification of every input vector.

## Scientific meaning and remaining native bridge

The same *set* of labelled future commands has different discriminatory power depending on whether the observation resets between commands or follows one cumulative trajectory. For any future-lifting or observer-safe-quotient claim, the legal command composition, the observation schedule, and whether one common reference-frame transformation must witness the whole future are load-bearing assumptions. An abstract orbit quotient is not automatically a congruence for a fixed-labelled legal future path.

The coordinate words above use positive native-unit adjacency `T_i^+(z)=z+e_i` from the frozen X6 spatial Cell torsor. Actual primitive triadic stability, Port incidence, branch identity, time and active/passive rotation remain separately typed and unproved by this group theorem. The original X6 owner, source authors, P000, and existing Task/Result/Activity boundaries are unchanged.

Status: one author-side proved mathematical subunit; zero Native Result admission, zero formal Task closure, zero mother-objective closure. Native independent review and formal Source/Activity linkage remain pending.

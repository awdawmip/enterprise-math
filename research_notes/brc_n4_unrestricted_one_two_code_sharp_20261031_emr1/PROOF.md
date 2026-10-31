# BRC N=4: exact unrestricted one- and two-symbol minimax for complete lawful terminal observations

**2026-10-31 / AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Direct continuation of the three-code proof in PR #1757 at immutable `c9559807c0b41b4ba8f2d83e12b947f50765b80c`.

## Exact model and game

The original strictly positive 16-leaf P/Q experiment has source S∈{AU,AV,BU,BV}, third-stage J∈{0,1}, and fair independent fourth-stage K∈{0,1}. Per-K raw P weights are AU=(9,11), AV=(5,5), BU=(3,27), BV=(30,30); Q weights are AU=(10,10), AV=(20,20), BU=(15,15), BV=(15,15). Every leaf is positive; each law sums to 240. Conditioned on eight prepared inputs (S,B) with B∈{P,Q}, the six distinct third-stage conditional rows, ordered AU_Q,AU_P,AV,BU_Q,BU_P,BV, and columns AU0,AU1,AV,BU0,BU1,BV, are

```
M = 1/20 * [
 [10,10, 0, 0, 0, 0], [ 9,11, 0, 0, 0, 0],
 [ 0, 0,20, 0, 0, 0], [ 0, 0, 0,10,10, 0],
 [ 0, 0, 0, 2,18, 0], [ 0, 0, 0, 0, 0,20] ].
```

The AV_P/AV_Q (and BV_P/BV_Q) conditional futures coincide, but all **eight prepared inputs** remain in the scoring maximum. The public output is the complete O=(T,Decision,Z_BU), with BU-only sensor Z=J xor Bernoulli(ε), Z=⊥ outside BU, for arbitrary real 0≤ε≤1/2. A common row-stochastic encoder E sends each preparation to ≤k symbols **before** H is chosen; a decoder D_H may use H, be randomized and synthesize a fresh outcome. Let F range over all lawful S23 (or S2) causal stopping/decision policies, and define

`R_k(F;ε)=inf_E sup_{H in F} inf_{D_H} max_{x=(S,B)} TV(L_H(O|x),(E D_H)(O|x)).`

Reconstruction concerns distributions, not the actual realized path.

## New sharp theorem

For **all** real ε∈[0,1/2] and arbitrary stochastic code sharing,

```
R1(all S23; ε) = R1(all S2; ε) = 3/4,
R2(all S23; ε) = R2(all S2; ε) = 1/2.
```

With earlier **unreviewed author-side** sharp results R3=1/2 (commit c9559807), R4=1/5 (d11461c2), R5=1/40 (f8e934df), Rk=0 for k≥6 (8b4aaf08), this completes the k≥1 finite rate–distortion staircase for this **declared model**: 3/4, 1/2, 1/2, 1/5, 1/40, 0. In particular, the third symbol does not reduce the all-lawful-public-observer minimax below the two-symbol value.

## One lawful four-provenance separating policy H*

Continue at T1. At T2 **stop only AV**, terminal Decision=Q; continue AU, BU and BV with probability one. This satisfies the S2 condition that AU and BU use identical T2 action kernels. At T3 stop all continuations, choose Decision=P at AU and BU, Decision=Q at BV, and emit the declared BU-only Z when S=BU. These deterministic T3 decisions are constant on equal contemporaneous likelihood-ratio nodes: AU0=9/10, AU1=11/10, BU0=1/5, BU1=9/5, BV0=BV1=2, so H* is also lawful S23. No unseen K is queried.

A single complete public outcome identifies **which of four provenance groups** was present:
```
AV: (2,Q,⊥)
AU: (3,P,⊥)
BU: (3,P,0) or (3,P,1)
BV: (3,Q,⊥)
```
These group support sets are pairwise disjoint for all ε (including sensor endpoints). There is no assumed free public S label; the distinction is conveyed entirely by a permitted stop time, a terminal decision and BU sensor presence.

### Packing lemma (analytic lower bound, arbitrary random E)

For G inputs with mutually disjoint output supports U_i under **one** lawful policy, any shared stochastic k-code E and decoder D have decoded success p_i=(ED)_i(U_i). Since U_i are disjoint,
```
sum_i p_i = sum_j sum_i E_ij D_j(U_i)
          <= sum_j (max_i E_ij) sum_i D_j(U_i) <= k.
```
Thus some p_i≤k/G, and since the true outcome satisfies P_i(U_i)=1,
`max_i TV(P_i,(ED)_i)≥1-k/G`. The lemma holds for every random encoder/decoder and its limiting infimum. Apply it to the four preparations AU_Q, AV_Q, BU_Q, BV_Q under H*: G=4 yields R1≥3/4 and R2≥1/2. Since H* belongs to both languages, both lower bounds are uniform in real ε. For k=3 the single-policy lemma only yields 1/4, which is consistent with the **stronger** previous all-policy R3=1/2 result.

### Achieving kernels (analytic upper bound for **all** adaptive H)

A one-code encoder sends every preparation to the sole symbol and outputs the six-class reconstructed future
```
D1 = (5,5,10,2,8,10)/40.
```
A two-code **deterministic** encoder assigns C_L to AU and AV, and C_R to BU and BV, independently of B. Decode by
```
D2_L = (10,10,20,0,0,0)/40,
D2_R = (0,0,0,4,16,20)/40.
```
All rows are probability distributions. On the provenance support of **each** true row M_i, D1 is a coordinatewise submeasure of mass 1/4; D2_{E(i)} is a coordinatewise submeasure of mass 1/2 (in particular BU_P=(2,18)/20 dominates its reconstruction (4,16)/40, and BU_Q=(10,10)/20 also dominates it). All remaining decoded mass lies outside that input's provenance block. Consequently
```
TV(M_i,D1)=3/4;   TV(M_i,D2_{E(i)})=1/2
```
for each of the eight preparations, including duplicate AV/BV rows. Conditional fair K, BU sensor with parameter ε, all allowed stopping/decisions and H's internal randomization are **common stochastic postprocessings of the complete labeled future**. Total-variation data processing therefore gives ≤3/4 and ≤1/2 for every S2/S23 H, uniformly in ε; H* attains both. The lower and upper bounds close.

## Executed exact verification and claim scope

`VERIFY.py` was executed with Python's standard-library Fraction arithmetic. It independently reconstructs positive 16-leaf weights and P/Q normalization 240/240, validates the six prepared rows, one- and two-code block domination, 64 lawful T3 class-subset policies × six rows × four ε values and H* × six rows × four ε values (**1560 exact terminal distributions and two associated TV comparisons per case**). It checks H*'s pairwise disjoint provenance supports. The executable prints `PASS_BRC_N4_R1_R2_EXACT_FULL_TERMINAL_20261031`; see `RUN_EVIDENCE.txt`. All-real-ε, arbitrary stochastic encoder and all-lawful-adaptive-policy quantifiers are discharged by the displayed analytic inequalities, **not** by sampled finite cases.

This is a positive-rational BRC **finite observation/deficiency theorem**; it does not provide a native P000 X6 physical transition, independent time calibration or actual Heartbeat law. It preserves provenance and joint observer semantics, uses no signed-amplitude cancellation, and does not revise P000 or establish independent mathematical acceptance.
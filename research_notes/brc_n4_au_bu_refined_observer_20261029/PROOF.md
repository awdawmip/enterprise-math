# BRC N=4 — AU/BU dual-lineage terminal-observer refinement (2026-10-29)

**AUTHOR_SIDE_PORTABLE / UNREVIEWED / NOT_ADMITTED / NONBLIND.** No native research CLAIM, Driver DA, immutable review or theorem admission is asserted here. This result concerns the **stipulated external positive 16-leaf P/Q model** and behavioral S2/S23 policies from `research_notes/brc_n4_bu_full_causal_reduction_audit_20261029_r1t11/PROOF.md`. It does not prove a P000 native-X6 transfer, three-dimensional slice theorem or physical time-dynamics theorem. Source read: Enterprise Math `5c3a63b7794b7dd8ae209435a020ea8e5d554a1e`.

## Statement and precise observer

Let `Z_AU` (respectively `Z_BU`) equal one iff an AU (BU) path reaches time 3 or 4, and zero on any earlier stop. Refine the complete terminal observer to `O'=(T,Decision,Z_BU,Z_AU)`. Keep the target `F_(a,b)`, `0<=a,b<=1`, and the conditional behavioral S2/S23 policy classes from the cited input. S2 requires identical conditional time-two action kernels at AU and BU, which have the same contemporaneous likelihood ratio; S23 additionally identifies actions of time-three/four nodes with equal contemporaneous ratios.

**Exact reduction theorem:** For every real `0<=a,b<=1`, the minimax over all S2 policies of `max(TV_P(O'_F,O'_G),TV_Q(O'_F,O'_G))` equals the minimax over S23 policies. Both equal the attained five-atom objective below. The old four-atom **numeric** minimax value is not asserted to be invariant under this observer refinement.

Define a deterministic map `K'` on observed tuples: for `T=1,2`, retain T, set decision Q and both tags zero; for `T=3,4`, set T to 3, retain both tags and set decision Q iff `Z_BU=1`, otherwise P. The target `F` is `K'`-fixed under both P and Q.

For any lawful S2 strategy G, build `G^{K'}` by retaining G's time-one/time-two conditional **continuation** kernels, deciding Q at all early stops, and terminating every time-three arrival. Decide Q on BU descendants and P elsewhere. The BU time-three ratio set `{1/5,9/5}` is disjoint from non-BU ratios `{9/10,11/10,1/4,2}`, so the time-three decision obeys S23. At time two the AU/BU common conditional continuation kernel is unchanged and their early-stop decision is uniformly Q. Every time-three/four path has the same two lineage tags when it first arrives at time three, so a direct pathwise coupling yields, **for each L in {P,Q}**, the full-distribution identity

`Law_L(O'_(G^{K'})) = K'_# Law_L(O'_G).`

The target is fixed by `K'` and total variation contracts under a deterministic pushforward. Consequently this S2-to-S23 construction never increases either law's loss. Since S23 is contained in S2, the two minimax values are equal.

## Five lawful parameters, five observable atoms

Let `A,B,c in [0,1]`, `0<=U<=A`, `0<=V<=B`. Here A/B are time-one continuation probabilities; c is the common AU/BU time-two continuation; U=A*u and V=B*v are AV/BV time-two continuation masses. Every such tuple defines an actual S23 policy by choosing u=U/A for A>0 (u=0 for A=0), and analogously for v. Compactness ensures the resulting minimum is attained.

List the five atoms in order as
`(1,Q,0,0), (2,Q,0,0), (3,P,0,1), (3,P,0,0), (3,Q,1,0)`.
Direct summation of the original 16 leaves gives

```text
Q_F = (1-(a+b)/2,    a/3+b/2,     a/6,          0,                0)
Q_G = (1-(A+B)/2,    (A+B)/2-Ac/6-Bc/4-U/3-V/4,
                       Ac/6,     U/3+V/4,       Bc/4)
P_F = (1-(a+3b)/4,   a/12+3b/4,   a/6,          0,                0)
P_G = (1-(A+3B)/4,   (A+3B)/4-Ac/6-Bc/4-U/12-V/2,
                       Ac/6,     U/12+V/2,     Bc/4)
```

Put `s=(A-a+B-b)/2`, `t=(A-a+3(B-b))/4`, `H=Bc/4`, `w=a/6-Ac/6`. The signed target-minus-competitor vectors are exactly

```text
DeltaQ' = (s, H-s-w+U/3+V/4,   w, -U/3-V/4,  -H)
DeltaP' = (t, H-t-w+U/12+V/2, w, -U/12-V/2, -H)
```

Thus `d'_2(a,b)=d'_23(a,b)=min_(A,B,c,U,V feasible) max(||DeltaQ'||_1,||DeltaP'||_1)/2`. Dropping AU lineage combines atoms 3 and 4 and recovers the prior four-atom vectors. Consequently `d'_2(a,b)>=d_2(a,b)`; whether equality holds is a **separate open optimization question**.

## Exact discrimination witness

The lawful tuple `a=A=1/2, b=B=0, c=0, U=1/4, V=0` gives, for **the same fixed policy**, the original four-atom TV pair `(Q,P)=(0,1/16)` and the refined five-atom pair `(Q,P)=(1/12,1/12)`. The AU-tag refinement prevents cancellation between target AU time-three mass and competitor AV time-three mass. This proves strict information loss for that fixed-policy coarsening, **not** a strict gap between two minimax capacities.

## Validation, provenance, next discriminating question

`VERIFY.py` symbolically checks both five-atom signed vectors, P/Q normalization and the four-atom collapse identities, then exactly verifies the strict witness with rational arithmetic. `VERIFY_EVIDENCE.txt` records the executed output. Finite checks verify algebra; the all-policy equality uses the pathwise construction and TV data processing.

The previous 16-leaf reduction remains author-side, not independently admitted. Preserve its complete behavioral policy semantics and observables; the refinement result cannot promote either source to Working Truth or Foundation. Next find an exact parameter pair `(a,b)` with `d'_2(a,b)>d_2(a,b)`, or prove equality on a stated region. This is a proof obligation, not a new published formal Task.

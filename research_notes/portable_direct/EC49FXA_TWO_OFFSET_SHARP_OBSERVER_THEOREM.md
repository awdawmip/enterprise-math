# EC49FXA — Sharp observer for the two adjacent relative phases D={0,1}

Date: 2026-11-22 (Asia/Shanghai). Frozen scientific input: **BRC16943**, unchanged. Direct predecessor: [EC49FWZ](https://github.com/awdawmip/enterprise-math/blob/201000cb4e8132e90e1f993ba1e7297d3878f500/research_notes/portable_direct/EC49FWZ_ANTIPODAL_TRANSVERSAL_OBSERVER_THEOREM.md). Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**.

## Precise model

Use the inherited 110-periodic two-sided CRT/Farey auxiliary observer. The frozen P10 mask U ranges over 50 supports, the mod-11 factor V is full or lacks exactly one residue, and the reference and full indexed reflection-defect spectra of L(t)=w(t-s_L) and R(t)=w(-t-s_R) are available. The allowed relative offset is **D={0,1}** in Z/110. One installed physical site t measures **two separate Boolean bits**. A fixed set S must have sampled Hamming distance at least r for all compatible nonempty two-word spectral fibers. This concerns relative-phase uncertainty and does not assert the whole signed/causal native X6 state is reconstructible.

As in EC49FWZ, the only residual ambiguity inside such a fiber is a simultaneous half-turn. A frozen single-pair half-turn disagreement witness (U=299, mask represented as an integer bitset) realizes every residue block i mod5 and every one-hole column j mod11 under the allowed phases. The exact sampled distance is

```
F_S(d,i,j) =
  sum(t in S) (
    1[t mod 5=i and t mod11 != j]
    + 1[(d-t) mod5=i and (d-t) mod11 != j]
  ),
 d in {0,1}, i in Z/5, j in Z/11.
```

For a multi-pair disagreement, contributions add over disjoint i-blocks; thus `F_S(d,i,j)>=r` for these 110 elementary constraints is necessary and sufficient for the stated fixed worst-case requirement.

## Exact theorem

For every integer **1<=r<=40**,

[
\boxed{N_{\mathrm{fixed}}(\{0,1\};r)=
\left\lceil\frac52\bigl(r+\lceil r/10\rceil\bigr)\right\rceil .}
]

For **r>=41** no site set suffices. In particular:

| sampled distance r | 1 | 2 | 3 | 10 | 11 | 20 | 21 | 30 | 31 | 40 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| exact site optimum | 5 | 8 | 10 | 28 | 33 | 55 | 60 | 83 | 88 | 110 |

The physically important cases are 5 activations for noiseless recovery (r=1), 8 for one known channel-bit erasure (r=2), and 10 for one unknown channel-bit error (r=3). Compared with an arbitrary full antipodal transversal (EC49FWZ: 10,10,15), uncertainty between these **two** offsets costs no extra activation over the single-offset lower bound.

## Proof of lower bound (human-checkable)

Write m_i=|{t in S:t mod5=i}| and M=|S|. Fix any allowed d and block i, put k=(d-i) mod5. Let c_{i,j} count selected physical sites in block i, column j mod11, so c_{i,j} belongs to {0,1,2} and sum_j c_{i,j}=m_i. Then

[
F_S(d,i,j)=m_i+m_k-c_{i,j}-c_{k,(d-j)\bmod11}.
]

On summing the two deletion terms over all 11 choices of j one obtains exactly n=m_i+m_k. Consequently some j has deletion >=ceil(n/11), so the requirement F>=r forces

[
n-\lceil n/11\rceil\ge r.
]

For integers 1<=r<=40 the least feasible n is
[
h(r)=r+\lceil r/10\rceil.
]
(This follows by splitting r into ten-element blocks, or by checking h-ceil(h/11)>=r and (h-1)-ceil((h-1)/11)<r.) Hence **m_i+m_{d-i}>=h(r)** for all five i. Summing over i for one d yields 2M>=5h, giving M>=ceil(5h/2).

This lower bound is valid for any nonempty set of relative offsets; it does not assume symmetry or a special site configuration.

## Attainment and exact finite certificate

The accompanying [checker](EC49FXA_TWO_OFFSET_VERIFY.js) contains **40 explicit 110-bit hexadecimal masks**, one for every r=1,...,40. Bit t of the r-th mask is 1 precisely if site t is installed. Each mask has exactly ceil(5h(r)/2) bits. A pure BigInt/Boolean verifier independently calculates the complete 2*5*11 elementary distances, confirming F>=r for every possible d,i,j. This is **4,400 exact inequalities** across all 40 masks, not an optimization solver's floating-point gap estimate. The checker also validates the lower bound's integer threshold h. It emits [the reference JSON](EC49FXA_TWO_OFFSET_OUTPUT.json); both may be run or reviewed without scipy or any external package.

For r>=41, the inherited frozen one-pair/one-hole witness has exactly 20 distinguishing physical positions on each channel, so even reading all 110 sites yields total channel-bit distance 40.

The proof uses exact finite CRT formulas and the inherited frozen P10 realization theorem; only the finite upper-certificate verification is delegated to the attached simple exhaustive checker. It is a reproducible computer-assisted exact theorem, pending independent mathematical review.

## What changed, what remains

EC49FWZ closed the **55-offset transversal** model. This theorem closes the much smaller, nontransversal, **two adjacent offsets** `D={0,1}` for all admissible distances. The fixed lower bound happens to remain attained despite the additional offset; that fact is certified, rather than inferred from the full-transversal result.

Next: determine sharp thresholds for `D={0,1,...,k-1}` with 3<=k<=55, initially k=3, and classify when the two-offset optimum first fails. The static theorem retains signed Farey anchor, phase, branch, CRT source and native X6 relation provenance as separate required types for any later dynamical promotion. No formal Task CLAIM, accepted Result, or independent Review is asserted here.

**Source custody:** own continued independent portable research in the EC49 line. `RS-EC49AS` task-directory read at Source `15ff44ef9aea62985582b8ef8bca4a82813e6a2e` returned `SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY` (2026-11-22T15:30:32.840Z). This only covers that pinned directory, not active owner projection. Historical Researcher `EM-DIRECT-525D43`, Activity `RA-E1C533B86B927384C5B0ADED` preserved; no session capability or formal CLAIM inferred from public IDs.

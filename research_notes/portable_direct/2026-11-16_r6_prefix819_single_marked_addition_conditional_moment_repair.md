# PREFIX-819 — One marked addition, exact conditional BRC moment repair and a nonnegative counterexample

Date: 2026-11-16 (Asia/Shanghai). Independent portable TASK_RESEARCH auxiliary mathematics. Frozen scientific P000 pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Predecessors: PREFIX-817–818. Research lineage: `EM-DIRECT-AB379B / MCP-ddad8ec8dced4918a59a479555c21490`. No formal shared-task CLAIM. Scope: exact weighted formal-toggle counts, not native X6 events or elapsed physical time.

## Problem

PREFIX-818 gives a triangular `T(q)=(q+1)(q+2)/2`-coordinate elementary-symmetric integer carrier for **pure removal**, independent of the number m of named branches. Determine whether permitting **one named addition branch** loses that compressed observer information, and find a finite exact repair.

States are subsets S⊆[m] with |S|<=q; all named branches i have removal weight β_i∈Z_{≥0}. Choose one distinguished branch j with addition weight a∈Z_{≥0} whenever j∉S and |S|<q. All other additions have weight 0. Paths multiply transition weights and alternatives add. The observer retains, at every future formal toggle horizon, the exact terminal-count histogram by |S|.

## Theorem 819.1: exact marked/unmarked conditional moment carrier

Represent S as `(z,U)`, where z=1 if j∈S and z=0 otherwise, with U⊆[m]\{j} and |U|=k<=q−z. For arbitrary integer initial named mass μ, define

`M_{z,k,h}=Σ_{|U|=k} μ_{U∪(z?{j}:∅)} e_h(β_i:i∈U)`, `0<=h<=k<=q−z`.

The integer coordinates have dimension
`T(q)+T(q−1)=(q+1)^2`,
where T(−1)=0. Their **exact one-toggle update**, with missing/out-of-range coordinates interpreted as 0, is

`M'_{0,k,h}=(h+1)M_{0,k+1,h+1}+β_j M_{1,k,h}`,
`M'_{1,k,h}=(h+1)M_{1,k+1,h+1}+a M_{0,k,h}`.

The output after each update is
`Y_l=M_{0,l,0}+M_{1,l−1,0}` for l=0,...,q.
The recurrence works for **every** m,q, removal weights β_i, distinguished addition weight a, initial integer mass, and unlimited formal-toggle horizon. It uses nonnegative coordinates/updates for nonnegative data.

*Proof.* Unmarked branch removals preserve z and by the PREFIX-818 elementary-symmetric identity give (h+1)M_{z,k+1,h+1} on each z-class. Removal of the distinguished j transfers z=1 to z=0 without changing U, multiplying by β_j; it contributes β_j M_{1,k,h}. Addition of j transfers z=0 to z=1, when k<q, without changing U and contributes a M_{0,k,h}. These are the only permitted moves and yield exactly the two equations. The readout counts U together with z; the two contributions at total size l are (z,k)=(0,l),(1,l−1). Induction establishes the result for all horizons. QED.

This is a sufficient **integer future-count carrier**, of dimension independent of m for fixed q. It is not claimed to be minimal for every weight choice. A full arbitrary named initial mass costs at least its input-reading cost to transform; the recurrence uses O(q²) integer additions/multiplications per update, with size-dependent bit lengths.

## Proposition 819.2: a single addition makes the original unconditioned moments insufficient

Take m=3, capacity q=2, removal β=(1,2,3), and permit addition **only** of branch 1, with weight a=1. Consider two nonnegative integer initial mass distributions:
`μ=δ_{ {1} }+δ_{ {3} }`, and `ν=2δ_{ {2} }`.

Both have the **same full PREFIX-818 unconditioned moment carrier**: the only nonzero moments are `M_{1,0}=2` and `M_{1,1}=4`. Their initial terminal-count histograms coincide at (0,2,0). After one allowed toggle the histograms differ:

`Y^(1)(μ)=(4,0,1)`, `Y^(1)(ν)=(4,0,2)`.

For both, the weighted total to empty is 4. The additional count-two mass from adding named branch 1 is 1 from μ (the {3} state) and 2 from ν (the two {2} states). Thus the original T(2)=6 moment vector is not a future-sufficient observer under this enlarged move language. The conditional j-presence refinement distinguishes the two distributions and repairs exactly this loss. QED.

The construction directly tests the information-preservation requirement: one new future operation reveals a previously hidden named-source correlation, while a bounded-size exact integer carrier remains available.

## Independent exact verification

Standalone standard Node.js BigInt checker: `research_notes/portable_direct/PREFIX819_R6_MARKED_ADDITION_MOMENT_CHECK.js`. Results JSON: `research_notes/portable_direct/PREFIX819_R6_MARKED_ADDITION_MOMENT_RESULTS.json`.

For m=1..7, q=0..min(m,4), three exact β patterns, distinguished index first or last, and a=1,2,3, independently compare generic named-state weighted path enumeration to the conditional-moment recurrence for every named basis state and horizons h=0..q+3. Coverage: 504 parameter cases, 8,775 named initial states, 61,902 exact full-histogram comparisons. The nonnegative μ/ν witness is checked directly. All asserted equalities and the strict witness difference passed. General validity rests on the constructive proof.

## Next

Determine the minimal rational observability rank for the one-marked-addition model at q>=2 and characterize the gap to the (q+1)^2 sufficient carrier. Extend to s addition-enabled named branches, testing the natural 2^s conditional-type moments against a sharper minimal repair. Retain the original X6 native event admission and causal time problem as separate from these auxiliary exact formal-toggle counts.

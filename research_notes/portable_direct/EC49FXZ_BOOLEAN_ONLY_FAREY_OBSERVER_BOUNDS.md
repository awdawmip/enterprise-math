# EC49FXZ — Boolean-only observation without a free indexed spectrum

Date: 2026-11-23. Author provenance: EM-DIRECT-48E619 / TASK_RESEARCH. Frozen scientific pin: `BRC16943`. Parent: EC49FXY `75bb1374183bb339f70fabecb99c72b7ccadb9f8`; genuine-anchor surjectivity from EC49FXU `5e33d4576bb0c1ef09e9169f8e17df469b8b7692`.

Status: **AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**. This is the scalar auxiliary Farey–CRT `C11` observation model, not a native X6 transfer. No P000 or ACTIVE premise is changed.

## Question and observation contract

EC49FXY gives exactly `r` additional Boolean readings once the complete 110-entry indexed reflection-defect spectrum has been supplied as side information, but did not price obtaining that spectrum. Study the opposite, physically defined model: the observer starts without the spectrum or the anchor and may query **one binary value of the original frozen C11 normalized trace per unit cost**. After each answer the next CRT site may depend on previous answers. All 600 genuine normalized product states are a priori possible, and exact identification of the normalized 110-bit trace is required. The observer does not need to identify the unobservable original anchor among equal normalized traces.

Define `P10(h,n)` by the frozen 44-residue slope table `(0,0):{3}, (0,1):{0,3,4,5}, (1,0):{2,3,4,5}, (1,1):{2,3}`, with `P10=0` for `h=n=0 mod 5`. This is exactly the predicate in EC49FXY, not a new science input. Every normalized trace has the form
```
W_{U,z}(t,j) = 1[t-th bit of U is 1] * 1[z != j],
t in Z/10, j in Z/11,
U one of the original 50 nonzero ten-bit support masks,
z in {-1,0,...,10}; z=-1 denotes the full eleven-factor.
```
The parent EC49FXU proves that every one of these `50*12=600` states is realized by a genuine reduced Farey anchor; the included stronger independent crosscheck reconstructs this by searching `1<=a,c<=79` and evaluating 66,000 original C11 witness entries.

Let `Q` be the minimum, over deterministic adaptive binary-site decision trees identifying all 600 normalized words, of the maximum number of binary C11 queries on any input.

## Theorem: exact proved interval

**14 <= Q <= 16.** The lower bound is analytic. The upper bound is a completely specified finite constructive decision tree with 600 distinct leaves, built from the frozen masks.

**Lower bound.** Fix any permissible nonempty U and consider the state with full mod-11 factor `W_{U,-1}`. For each `j=0,...,10`, compare to `W_{U,j}`, which deletes only column `j`. A physical Boolean query distinguishes this pair only if it queries column `j` at a row with `U(t)=1`. These eleven required distinguishing-coordinate sets are pairwise disjoint in the `j` coordinate. The full-factor state's decision-tree path must contain at least one query from each set, hence at least eleven queries. This holds for each of the 50 permissible U.

**Strengthened disjoint-support lower bound (14).** The frozen 50-mask atlas contains the four masks
`U=833`, `U_1=857`, `U_2=867`, `U_3=965`. Their supports satisfy `U subset U_k` for `k=1,2,3`, with pairwise disjoint extra-row sets
```
supp(U1) minus supp(U) = {3,4},
supp(U2) minus supp(U) = {1,5},
supp(U3) minus supp(U) = {2,7}.
```
Along the transcript of the full-factor state `W_{833,-1}`, eleven positive readings in **distinct columns** are still mandatory to reject all eleven deletion variants `W_{833,j}`. To reject each full-factor supermask `W_{U_k,-1}`, the transcript additionally must contain a **negative** reading on one of the extra rows in the corresponding set, because these two full-factor traces differ only on those rows. The three extra-row sets are disjoint, so these need three different query sites. They are on rows with `U(t)=0`, disjoint from the eleven obligatory positive readings. Hence every valid decision tree uses at least `11+3=14` site queries along `W_{833,-1}`, establishing `Q>=14`. Membership of these four masks is audited by direct frozen-slope enumeration in the companion program.

**Constructive upper bound.** Start with the exact 600 candidates `(U,z)`. For each non-singleton candidate set `S`, inspect all 110 sites `(t,j)` and choose one that minimizes `max(#zeros,#ones)`, breaking ties by the smaller `t`, then smaller `j`. Query that site and recurse on the two nonempty response classes. When only one candidate remains, output that candidate. This is an actual observation procedure; its precomputed candidate atlas and query tree are free offline computation, while each executed Boolean query is charged one unit. Each split strictly decreases the candidate set. The companion Node.js program reconstructs the frozen 50 masks, runs this exact algorithm, checks every single 600-state path and proves no path exceeds 16.

The calculated certificate is: 599 internal nodes, 600 leaves, first query `(8,0)` with branches 303/297, maximum depth **16**, average depth **10.95** over the uniform 600-state set, and leaf-depth histogram `{7:50,8:61,9:137,10:56,11:50,12:50,13:50,14:57,15:83,16:6}`. The histogram is not a probability assumption for the worst-case theorem.

A second source-level program in the author's local verification rebuilt 600 genuine witnesses in the same `1<=a,c<=79` square, checked 66,000 original integer C11 values, 550 full-versus-deleted disjoint-column differences, and all 600 adaptive decision paths. It found the same tree depth, counts and histogram. Its output is archived with this work and the independently executable compact tree verifier.

## Meaning, limitation and next question

This establishes an **end-to-end physical Boolean-query budget** without charging an arbitrary zero cost for the indexed spectrum, and improves the naive 110-bit full scan to a 16-bit adaptive guarantee. The lower bound 14 is stronger than the information-theoretic `ceil(log2 600)=10`; in addition to eleven column-wise one-hole alternatives, the full-factor state `U=833` has three disjoint extra-row obligations against strictly larger support masks.

The **exact optimum Q remains open within [14,16]**. In particular, the deterministic balanced-split rule is a constructive bound, not a claim of globally optimal decision-tree design. Additional actual measurement modalities for obtaining the indexed spectrum require their own explicit per-operation cost and interface before end-to-end comparison. Query feedback is assumed noiseless, `r=1` identification, with a fixed publicly known normalized atlas. No branch, height, affine-origin or full native X6 reconstruction is claimed.

Next: use bounded-depth decision-tree search, symmetry on the 50 ten-bit masks and 11 column factors, or a new lower-bound adversary to close `Q`. Also study noisy or erased Boolean queries with explicit repeated-sampling cost and retain the anchor/provenance residual for any subsequent native bridge. No independent Project Review, formal CLAIM/Result or theorem promotion is represented by this draft.
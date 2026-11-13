# PREFIX-591-R2 — Integral dual BRC lattice, exact one-stream lift and arithmetic accounting

Date: 2026-11-08. Status: AUTHOR-SIDE PROOF + EXECUTED EXACT CERTIFICATES / UNREVIEWED.
Scientific input remains frozen at `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessors: PREFIX-588 common invariant cone, PREFIX-589 dual labelled carrier, PREFIX-590 universal two-positive-channel lift (PR #1797). All 96 native ports, 576 labelled transitions, six original axes and marked gate branches are retained. This is an exact finite-state BRC model result; no physical attribution is proposed.

## Theorem 591.1 — Exact integral image lattice and index

Write the 96 ports as 24 source-preserving groups `G` of four, with fixed block `W_G=J_4-I_4`. Set
```
H := 3 W^{-1} = W-2I = direct_sum_G (J_4-3I_4).
L := H Z^96.
```
Then
```
L = {v in Z^96 : v_i ≡ v_j (mod 3) for every i,j in the same four-port group G};
[Z^96:L] = 3^72.
```
In particular, H and W have integer entries, `WH=HW=3I`. Proof: for a four-vector `r`, put `s=sum r_i`. Its image is `v_i=s-3r_i`, so all four residues agree modulo 3. Conversely, if the residues agree, `sum_i v_i ≡ v_i (mod 3)` (four congruent entries), and `r_i=(sum_j v_j-v_i)/3` is an integer preimage. The block determinant of `J_4-3I_4` is `1*(-3)^3=-27`, yielding the exact index `27^{24}=3^{72}`.

## Theorem 591.2 — All-length lattice invariance for native weighted BRC

Let `A_k` and `T_k=W^{-1} A_k W` denote the seven *original-labelled* native and dual coefficient matrices (`k=1,...,6,gate`). PREFIX-588/589 proves their exact integer 0/1 entries and 576 total marked native branches. Then coefficientwise
```
T_k H = H A_k .
```
Hence for any sequence of integer-weight native operators `A^{(t)}` obtained from these seven matrices (including time-dependent axis weights and gate weight),
```
T^{(t)} L ⊆ L,
v_0 = H r in L,
v_n = T^{(n)} ... T^{(1)} v_0 = H A^{(n)} ... A^{(1)} r,
A^{(n)} ... A^{(1)} r = (W v_n)/3 in Z^96
```
for any integer native initial column `r`. In the original nonnegative-weight regime, the dual core T remains a nonnegative **operator**; the single stored lattice state `v_n` may be signed. Proof: `T H=(W^{-1}AW)(3W^{-1})=3W^{-1}A=HA`, by telescoping, coefficientwise. The congruence condition supplies an exact mod-3 admissibility test at every step. A failed test detects some implementation corruptions; passing the test alone does not establish equality to the intended native path.

For any integer left observer `l`, the exact scalar is `l^T W v_n/3`. The divisibility is a theorem, not a numerical tolerance. Coordinates retain source/branch/gate information via the original native A and its labelled dual T. Conversion is invertible over Q; the congruences characterize the actual integer image.

## Theorem 591.3 — Cost variants and unavoidable cancellation witness

The earlier always-nonnegative representation uses `p_0=Wr>=0`, `q_0=2r>=0`, computes `T^n p_0` and `T^n q_0`, and recovers their difference via `W/3`. The new *integer signed lattice* route computes only `v_0=p_0-q_0=Hr` through one dual propagation. In a dense 96-state sparse-edge sweep at generic positive weights, the reference upper counts per step are: original = 576 labelled edge terms; one signed dual = 576; two independent positive streams = 1152. `H` and `W` cost O(96) each by 24 block sums. Integer coefficients remove repeated division by three inside propagation; the final recovery division is exact. No unconditional speedup claim follows from equal edge counts, and bit lengths, active support, input/output conversion and query batching remain part of workload-specific accounting.

A structural cancellation witness shows why the distinction matters. Let `e_i,e_j` be distinct original singleton ports in the same four-port group, `n=0`. Then `e_i^T e_j=0`, whereas the two positive-stream contributions are both `2/3`: `(W e_i)^T(W e_j)/3=2/3` and `(W e_i)^T(2e_j)/3=2/3`. Their final subtraction is exact zero. Therefore finite-precision cancellation is genuine already at zero horizon for these observer endpoints.

## Exact executable evidence and scoped benchmarks

The companion Python certificate imports the unchanged PREFIX-589 original 48-phase/96-port BRC transition constructor. It checks all `7*96=672` complete integer matrix-column intertwining equalities, the block inverse and congruences; four explicit endpoint families and every horizon `0,...,12` under four nonuniform time-dependent integer weight sets; independent original, signed dual and two-positive native-to-dual evolutions; and the exact cancellation witness. All integer assertions passed.

A second, more detailed local certificate counts *nonzero labelled sparse-edge summands* at depths 1–12, without substituting time/cost claims. Total counts (original, signed-dual, dual-two-positive) were:
- singleton port 0: `2658,2400,5412`;
- uniform 96-port input: `6912,6912,13824`;
- one entire four-port block: `3000,2760,5520`;
- selected seven sparse native ports: `5658,5268,11880`.

These are a declared reference algorithm's exact active-term counts (sum over 12 steps), not machine timings; they show the potential benefit depends on source support. The detailed script also measures growing integer bit lengths. Exact nonnegative dual stream evaluation, native observables and recovery were compared with the original for every tested step. All assertions passed.

The mathematical theorems are algebraic; finite test counts verify this specific full-native implementation and workload samples. Full native repository import/independent Driver proof review remain unperformed. Current native session-start returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE / operation_sent=false`; formal Owner/CLAIM/Native Result are unconfirmed. This author-side artifact is not a canonical theorem admission.

## Next discriminating unit: PREFIX-592

Characterize which batches of native endpoint queries admit a *single nonnegative* dual stream (`Hr>=0`, equivalently `3r_i≤sum_{G}r_j` in each block), and compare native, one-signed, single-nonnegative, and two-positive routes including exact bit lengths, sparsity, input/output transform costs and reuse. Check the hypothesis that nonnegative feasible inputs may avoid signed cancellation without creating a general speedup. Retain original branch provenance and gate labels.

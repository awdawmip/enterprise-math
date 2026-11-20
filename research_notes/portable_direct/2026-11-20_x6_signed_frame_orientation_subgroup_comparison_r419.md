# X6 r419 — 两种 23,040 阶有符号轴参考架群的校准差异

Date: 2026-11-20. Status: **author-side exact group-theoretic comparison and independently recomputed finite enumeration within the same Driver research context; no Native Result or independent Native Review**.

Contributor: the existing RESEARCH_DRIVER logical session EM-DVR-DEBB5E. This note does not claim new ownership of r411–r418 or the native X6 foundation. Preserve original X6 contributions EM-EMF6D046-5A2844, EM-X6-DFD1FD, EM-X6CM-EDBD55. It compares, rather than revises, the *explicitly assumed* abstract frame group of r411–r418.

Source frontier: r411@5e3d07b05799754cb1b4327e97bb30aaf12f0652, r415@88e41b7b8ed36cab0551ae6345d2da7576b41d39, r418@86faf6b796b0fb5b8703bea2c016a77195611597. Native P000 and Heartbeat X6 time sources remain fixed; the physical admissible rotation group is **not** inferred from the following ordinary signed-permutation representations.

## Precise alternative models

Let B_6=(C_2)^6 ⋊ S_6 act faithfully on the 12 signed labels ±e_1,...,±e_6 by permutations of six unsigned axes together with independent sign changes. For (ε,π)∈B_6, in the ordinary signed-permutation 6×6 representation define det(ε,π)=sgn(π)∏_{i=1}^6 ε_i.

- **G_A=(C_2)^6 ⋊ A_6**, used explicitly in r411–r418. It has order 23,040. Even permutations are required, but sign changes are unrestricted. In the ordinary matrix representation, it includes determinant -1 maps.
- **G_+=(ker det)≤B_6**, the orientation-preserving subgroup of ordinary signed-permutation matrices. It *also* has order 23,040. Odd permutations are allowed when paired with odd sign parity. These are different subgroups, although they have equal order.

The comparison is purely algebraic. P000 defines native six-axis relations and rotation semantics; it does not declare that ordinary Euclidean determinant is the native physical orientation predicate. No change to P000, native Cell/Port or time dynamics is proposed.

Fix the **ordered, positive, pointwise fixed** suffix s=e_1...e_k, 0≤k≤6; write m=6-k. The action on a word is simultaneous letterwise action by one group element. Let K_A=Stab_{G_A}(s), K_+=Stab_{G_+}(s). The remaining primitive signed-letter alphabet is the usual full ±e_i set; all prefix words are freely available for this theorem.

## Theorem: stabilizers, minimum universal primitive probes and exact repair bits

For m≥2,

|K_A|=2^m·(m!/2)=2^{m-1}m!,      |K_+|=2^{m-1}m!.

For m=1, |K_A|=2 whereas |K_+|=1; for m=0, both equal 1.

Writing d_G(s) for the shortest fixed word w of primitive signed letters whose pointwise stabilizer inside K_G is trivial (the r418 universal-probe criterion), and b_G(s)=ceil(log2|K_G|) for unrestricted full-word literal/future repair, the exact values are:

| k fixed axes | m remaining | |K_A| | |K_+| | b_A | b_+ | d_A | d_+ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 23040 | 23040 | 15 | 15 | 6 | 5 |
| 1 | 5 | 1920 | 1920 | 11 | 11 | 5 | 4 |
| 2 | 4 | 192 | 192 | 8 | 8 | 4 | 3 |
| 3 | 3 | 24 | 24 | 5 | 5 | 3 | 2 |
| 4 | 2 | 4 | 4 | 2 | 2 | 2 | 1 |
| 5 | 1 | 2 | 1 | 1 | 0 | 1 | 0 |
| 6 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |

**Proof.** A group element fixing e_1,...,e_k has π(i)=i and ε_i=+1 on these axes. For G_A, the remaining π must be even, giving 2^m|A_m| elements; use |A_m|=m!/2 for m≥2 and 1 for m≤1. For G_+, the remaining permutation is arbitrary, while the product of remaining signs is forced by its permutation parity. For m≥1 this leaves 2^{m-1}m! elements; m=0 leaves the identity.

For K_A, any unused axis j admits the independent sign flip e_j↦-e_j with all other letters fixed, so fewer than m distinct remaining signed letters cannot form a base. Choosing all m positive labels does form a base: d_A=m. For K_+, if at least two remaining axes have not appeared in the fixed probe, an even permutation swapping these two axes paired with one sign flip (or another nonidentity determinant-positive signed permutation supported on them) fixes every probed letter; thus d_+≥m-1 for m≥2. Fixing m-1 distinct remaining positive axes forces the last axis permutation and its sign by the determinant equation, so d_+=m-1. For m≤1 the stabilizer is already trivial. The r418 full-free-language orbit-fiber argument yields b_G=ceil(log2 |K_G|), since the action is faithful on the primitive alphabet. QED.

## Finite-length prefix refinement and the three-axis case

Let M_G(k,n) be the maximum initial orbit fiber size for an unrestricted primitive signed-letter prefix of length n, with the fixed k-axis suffix. Put r=min(n,m). For G_+ and m≥1,

M_+(k,n) =
  2^r m!/(m-r)!        when 0≤r≤m-1,
  2^{m-1}m!            when r=m.

For m=0 it equals 1. This follows by fixing r distinct remaining positive letters; repetitions cannot shrink the stabilizer further, and the stabilizer of a remaining a-axis group has order 2^{a-1}a! if a≥1, otherwise 1. G_A retains exactly the r415 formula under its original G_A assumption.

For k=3, both groups have 24-element suffix stabilizers but a different stabilizer chain:

- G_A: fixing (+e_4), then (+e_5), then (+e_6) gives |K|: 24→4→2→1. The maximum fiber sizes for n=1,2,≥3 are 6,12,24, so the minimum repair bits are 3,4,5.
- G_+: fixing (+e_4), then (+e_5) gives |K|: 24→4→1. The maximum fiber sizes for n=1,≥2 are 6,24, so the minimum repair bits are 3,5.

Thus r411's six-primitive-letter calibration and r418's three-letter diagnostic are exact **for G_A**. Under the distinct G_+ model they become five and two, respectively; at a three-axis suffix the worst-case storage remains five bits, while its two-letter-prefix storage increases by one bit.

If the event alphabet is **freely composable ordered triads of three distinct signed axes**, the single candidate event (+e_4,+e_5,+e_6) fixes K_A and K_+ trivially in the k=3 case, giving one *candidate triad event* as a universal static probe in either model. It is not asserted to be a native legal three-force event.

## Exact finite cross-check and transfer boundary

Independent enumeration of all 6! permutations and 2^6 sign configurations gives |G_A|=|G_+|=23,040. For each k=0,...,6, enumeration of pointwise stabilizers gives exactly the seven rows above. For k=3, the G_A chain is 24/4/2/1 and G_+ is 24/4/1. This is a finite exact check (integer and permutation parity only) that corroborates, not replaces, the group-theoretic proof.

**Discriminating native question:** establish the actual X6 admissible transformation/rotation group from exact P000, Cell/Port/branch/time event and observer contracts, rather than selecting G_A or G_+ by resemblance to conventional 6D rotations. Once that group and its event action are pinned, calculate its true suffix stabilizer and legal-future observer fibers using the existing r416/r417 mechanisms. The equal group orders above give no basis for identifying their physical meanings.

Status boundaries: existing r411–r418 results retain their statements and assumptions; no Native Result acceptance, new task CLAIM, independent mathematical reviewer, Activity association, mother-objective completion or schedule change follows from this author-side comparison.

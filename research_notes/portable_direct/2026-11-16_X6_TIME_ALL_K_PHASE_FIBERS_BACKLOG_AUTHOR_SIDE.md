# X6 native-time conditional C12 product: exact all-k phase fibers and sharp aliasing

Date: 2026-11-16. Author-side independent mathematics by EM-EMF6D046-5A2844 (RA-6B0C6701D225841FFCCECF3E). Topic: RS-X6-NATIVE-TIME-DYNAMICS / TP2-91D4A7C2F63805BE21A3. Scientific status: conditional exact mathematical proposition, not formal Task Result or independent Driver review. The typed continuation prepare request backlog-driver-20261116-0640-x6time-typed-prepare-v1 failed `PREREQUISITE_NOT_SUCCEEDED`; **no CLAIM or RUN/open is asserted**. This GitHub note preserves unclaimed author-side mathematical research without changing native task ownership.

## Conditional mathematical domain

Fix integers m>=1 and k>=0. Assume m labeled, local, deterministic directed V1R decorated-state cycles, each of **exact period 12**, and assume every finite interleaving of their individual update counts is enabled by an explicitly independent product protocol through the horizon k. This product is a mathematical conditional model, not a certification of native multi-Cell Cell/Link/Port/triadic resource permissions.

A globally serialized k-prefix is encoded by a progress vector n=(n_1,...,n_m), n_i>=0, sum_i n_i=k. The full local C12 phase readout, together with the known global event count, is a=(n_i mod 12)_i. Distinguish the source progress cut n from the observer state a.

## All-k theorem

The exact number of labeled progress cuts is

`H_m(k) = binom(k+m-1,m-1).`

Let P(x)=1+x+...+x^11. The exact number of **distinct local phase tuples** reachable at global count k is

`F_m(k) = [x^k] P(x)^m/(1-x^12) = [x^k] (1-x^12)^(m-1)/(1-x)^m`

`= sum_(j=0)^(m-1) (-1)^j binom(m-1,j) binom(k-12j+m-1,m-1),`

with out-of-range binomial coefficients interpreted as zero.

For a phase vector a with S=sum a_i, it is reachable iff S<=k and k-S is a multiple of 12. If Q=(k-S)/12, the **exact cut-to-phase fiber cardinality** is

`|fiber(a)| = binom(Q+m-1,m-1).`

The maximum over all attainable a is

`max_a |fiber(a)| = binom(floor(k/12)+m-1,m-1).`

For m>=2, the first collision of distinct progress cuts with identical full phase tuple and global time count occurs at k=12: the m vectors n=12e_i share zero phase. For k<12 the phase readout is injective. Thereafter the number of distinct reachable phase vectors saturates sharply:

`F_m(k)=12^(m-1)` for every k>=11(m-1),

and `F_m(11(m-1)-1)=12^(m-1)-1`. For m=1, H_m=F_m=1.

## Exact proof

Stars and bars counts all nonnegative n_i with sum k, giving H. Write uniquely n_i=a_i+12q_i, with 0<=a_i<=11 and q_i>=0. Fixing a forces sum q_i=Q; the positive compositions give the exact fiber binomial. A residue tuple contributes once to F whenever k-S=12Q>=0, producing generating function P(x)^m/(1-x^12). Substitute P(x)=(1-x^12)/(1-x) and expand to get the alternating binomial.

Maximize Q by minimizing S among attainable tuples, namely S=k mod 12, achieved by (k mod 12,0,...,0). When k<12, every n_i<12, hence uniqueness; at k=12 all 12e_i collide.

There are 12^(m-1) residue vectors of a given total mod 12 (choose m-1 coordinates and solve uniquely for the last). Each has S<=11m. For k>=11(m-1), a congruent but unreachable tuple would require S>=k+12>11m, impossible. At k=11(m-1)-1, the all-11 tuple has S=k+12 and is uniquely the unreachable congruent tuple. This proves exact saturation and sharpness.

## Correction to R2's displayed binomial index

The earlier author-side R2 note at [immutable R2 commit](https://github.com/awdawmip/enterprise-math/blob/f115d6abf67f4dd41fe8a4d89367a0b1d1caa55f/research_notes/portable_direct/2026-11-12_x6_time_cut_lattice_and_C12_winding_residual_r2.md) writes `binomial(m+11,11)-(m-1)` for k=12 phase tuples. Its correct stars-and-bars count is

`binomial(m+11,m-1)-(m-1) = binomial(m+11,12)-(m-1).`

For m=2, R2's displayed expression gives 77, whereas the correct value is 12 (13 distinct ideals minus one collision); for m=3, the correct value is 89. The earlier proof's reasoning and its m=2 worked example agree with the corrected expression. This note records the error without altering the original author's research file or performing independent Driver acceptance.

## Reproducible integer checks

Companion verifier: `research_notes/portable_direct/x6_time_all_k_phase_fiber_verify_20261116.py`, executable with Python standard library only. Exact checked output: `X6_TIME_ALL_K_PHASE_FIBER_EXACT_PASS phase_checks=255 fiber_checks=147`. It enumerates all 12^m phase tuples for m=1..5 and k=0..50 and separately enumerates finite progress cuts to validate every fiber for selected horizons. The unrestricted theorem follows from the proof, not the finite tests.

## Research frontier

Earlier independent cut and one-link conditional theorems are already saved: [R2](https://github.com/awdawmip/enterprise-math/blob/f115d6abf67f4dd41fe8a4d89367a0b1d1caa55f/research_notes/portable_direct/2026-11-12_x6_time_cut_lattice_and_C12_winding_residual_r2.md), [R2b](https://github.com/awdawmip/enterprise-math/blob/c8a44eeb585f83be41a161f1492caae07f8066f6/research_notes/portable_direct/2026-11-12_x6_time_one_causal_crosslink_cut_polynomial_r2.md). Do not redo them. The decisive next native question is an actual source/target-admitted two-Cell triadic event with explicit resource guards and causal order, to compare its legal k-cut set against these independent/one-crosslink formulas. A phase observer and uncalibrated event count are not physical duration. Keep P000 and frozen task inputs unchanged.
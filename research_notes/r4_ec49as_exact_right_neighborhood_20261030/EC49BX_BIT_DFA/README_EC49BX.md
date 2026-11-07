# EC49BX — Native signed-X6 BRC: exact numeral bits and finite-state observer certificate

**Date:** 2026-10-31. **Evidence status:** `AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_BRC_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`. An author-side mathematical result, not a formal Task Result, independent review, or change to P000.

## Source pins and scope

- GLOBAL_KNOWLEDGE_V1 current canonical main: `e5b88cd1418df81a633a50542f6b02320475bb3e`; source entry, operating manual, ACTIVE worldview, Enterprise Math project router, math and BRC policies were read at the same pin.
- Enterprise Math current canonical main: `684a68342bf1321ba4ad33ea02b3e25f20d789e7`; native P000 V5, HEARTBEAT_WORLD X6, joint-observer-preservation, residual-fidelity and portable-research protocols read.
- Prior author-side frontier: EC49BW, this draft PR #1730 at `02058a5a9b561ecbe4c1f65602a425eced89b943`.
- Executed unchanged native source `signed_brc.py` with Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`.
- Model: ordered words of length n in the twelve signed directions of six native X6 spatial axes, endpoint displacement 0 in Z^6; positive rational per-direction weights; arbitrary integer path-bag multiplicities when specified. No physical time evolution, trigonometric propagation, or phase/cancellation claim.

## Theorem 1 — Minimal additive coordinate rank and exact binary bit cost are distinct resources

Let the signed alphabet be Σ={±E_i:1≤i≤6}. Fix positive rational direction weights w_a. Write D=lcm of all their denominators and c_a=D w_a∈Z_{>0}. For each ordered length-n path p define C(p)=product of its c_a values and χ_w(p)=C(p)/D^n. For a nonnegative integer path bag (m_p), with M=Σ_p m_p≥1, the BRC aggregate is

`S_n=Σ_p m_p χ_w(p) = N_n/D^n,quad N_n=Σ_p m_p C(p)`.

Let c_max=max_a c_a. Then `M≤N_n≤M c_max^n`. Thus, for fixed instrument, the explicit reduced rational numerator and denominator each require at most O(n+log₂ M) bits; the denominator divides D^n. If each ordered path appears at most U times, `M≤U·12^n`, hence the total explicit bit cost is O(n+log₂ U). All of this is exact integer/rational arithmetic.

If arbitrary multiplicity M is permitted, no uniform bit bound exists even at fixed n=0: M copies of the empty path have BRC readout M. For unit multiplicity and all unit weights, the **native unfiltered return count** C_{2m}=endpoint_multiplicity(2m,0) nevertheless has Θ(n) explicit binary bits. Indeed, each of the 6^m axis sequences specifies a distinct return word of m consecutive loops (+E_i,-E_i); and the total number of candidate ordered words is 12^{2m}. Hence `6^m≤C_{2m}≤12^{2m}`, and `bitlen(C_{2m})=Θ(m)=Θ(n)`.

**Proof.** C(p) is an n-fold product of integers between 1 and c_max; summing M terms proves the first inequality. Cancelling a positive rational fraction cannot enlarge either its numerator or denominator. There are at most 12^n words. The loop injection gives the return-count lower bound and the full alphabet count gives its upper bound. Binary logarithms complete the proof.

**Representation boundary:** This concerns expanded exact binary numerals, not arbitrary symbolic codes. For example 2^r has an O(log r)-bit exponent description while its expanded binary numeral has r+1 bits. An additive observer with just one scalar coordinate therefore does not have a uniform number-of-bits bound.

## Theorem 2 — Exact integer return coefficient recurrence, preserving native ordering

With q_i=c_{+i}c_{-i}, define T_j(m) as the sum of integer **common-denominator numerators** over all closed ordered length-2m paths restricted to axes 1,...,j. Set T_0(0)=1 and T_0(m>0)=0. Then, for 1≤j≤6,

`T_j(m) = Σ_{k=0}^m binom(2m,2k) binom(2k,k) q_j^k T_{j-1}(m-k)`.

The exact project-native bridge is

`endpoint_weight(2m,(0,0,0,0,0,0),w⁺,w⁻)=T_6(m)/D^{2m}`.

If w is the all-unit instrument, `T_6(m)=endpoint_multiplicity(2m,0)`.

**Proof.** A native closed word with the j-th axis used 2k times must have k positive and k negative occurrences of that axis. Choose its 2k ordered positions in binom(2m,2k) ways, and choose which k signs are positive in binom(2k,k) ways. Their weight is q_j^k. All remaining ordered positions form exactly one closed word on axes 1,...,j−1. This is a bijection preserving all interleavings, branch multiplicity, and signed spatial closure. Summation over k yields the recurrence. The published unchanged native endpoint_weight implementation sums the same signed-axis positive/negative occurrence configurations, giving the stated identity.

For six fixed axes the recurrence uses O(6m²) integer summands, once integer binomial coefficients are available. Each intermediate positive numerator has O(n) bits for fixed weights. This is an **arithmetic-operation** claim; bit-operation runtime and aggregate memory costs require separate analysis.

## Theorem 3 — A finite certificate for variable-length, fixed-automaton BRC observers

Fix a deterministic complete automaton A=(Q,δ,q₀) on the signed-X6 alphabet, one finite signed-axis permutation subgroup H≤S₆, and one fixed positive rational instrument. For path p define the source-side joint state

`Φ(p)=(δ*(q₀,hp))_{h∈H} ∈ Q^H`.

Allow every Boolean combination of tests on these component states **before** taking any orbit-weight readout χ_w(hp). Let A_n be the number of joint-state fibers attained by ordered native closed words of length n. The exact minimum dimension R_fixed(n) of a Q-linear additive statistic sufficient for all those weighted atom observations obeys

`A_n ≤ R_fixed(n) ≤ |H|·A_n ≤ |H|·|Q|^{|H|}`.

If the instrument transforms covariantly with the axes, `χ_{h·w}(hp)=χ_w(p)`, while the source-side selectors are unchanged, then `R_covariant(n)=A_n≤|Q|^{|H|}`.

**Proof.** The joint-state map partitions all paths into at most |Q|^{|H|} fibers. The observation matrix has separate, disjoint-support column blocks for these fibers. Strictly positive weights give at least one nonzero row per realized block. Each fixed-instrument block has at most |H| weight-orbit rows; its rational rank is between 1 and |H|. In the covariant instrument all transformed weight rows on a fixed source fiber coincide termwise, so its rank is exactly one. Ranks of disjoint-support blocks add. If O is the complete linear observation matrix and T is any additive Q-linear sufficient state, O=BT implies rank(T)≥rank(O); selecting a row-space basis attains equality.

This yields a **computable, sufficient, uniform-in-n bound** for fixed finite automata. It makes no universal decision claim for an unrestricted program generating new query languages/automata at each n (the EC49BW halting-reduction boundary).

## Sharp native example — exact rank saturation 8 versus 4

Take H={id,(E₁ E₂)}, w⁺=(2,3,3,2,1,1), and w⁻=(1,1,1,1,1,1). A three-state deterministic pattern detector recognizes A=(+E₁,+E₂); its swapped counterpart recognizes B=(+E₂,+E₁). Retain all four Boolean atom labels β(p)=(contains A,contains B) ∈ {00,01,10,11}. These full-atom selectors precede the two fixed-instrument weight-orbit readouts.

Every length n has at most four atoms, hence rank ≤8 fixed and ≤4 covariant. For n=6 all four atoms are realized, and **each** has two legitimate closed words with independent weight columns. The entire rank certificate is:

| β | Native signed path p; weight pair (χ_w(p),χ_w(swap·p)) | Native signed path p′; weight pair | Exact determinant |
|---|---|---|---|
| 00 | `1 1 1 -1 -1 -1`; (8,27) | `1 1 -1 -1 2 -2`; (12,18) | −180 |
| 01 | `1 -1 -1 2 1 -2`; (12,18) | `-1 2 1 -2 2 -2`; (18,12) | −180 |
| 10 | `1 1 2 -1 -1 -2`; (12,18) | `1 2 -1 2 -2 -2`; (18,12) | −180 |
| 11 | `1 2 1 -1 -1 -2`; (12,18) | `-1 2 1 2 -2 -2`; (18,12) | −180 |

Integers ±i in this table denote the *signed native step ±E_i*. For any t≥0 append t copies of (+E₃,−E₃) to each length-6 witness. The endpoint remains zero, no A or B is created or removed, and the two weight channels each multiply by 3^t. All determinants become −180·9^t, remaining nonzero. Thus for **all even n≥6**, exactly `R_fixed(n)=8` and `R_covariant(n)=4`.

This proves constant minimum **coordinate dimension** for a fixed source-filter system while Theorem 1 proves Θ(n) exact numeral bits for a different permitted one-coordinate native aggregate. These resources are not interchangeable.

## Exact executed evidence

The accompanying binary evidence archive `EC49BX_execution_evidence.tar.xz` contains the **actually executed** `VERIFY_EC49BX.py`, original exact `EXACT_REPORT_EC49BX.json`, `HANDOFF_EC49BX.md`, and two identical execution outputs. Its SHA256 is `b092307c76de38aed56f54e1649ca26f053e001b2288fa2f72d194944943b383`. The verifier imports the unchanged native signed_brc source at Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`; obtain it from the separately preserved EC49BW full-sources archive or from its pinned project source.

Direct complete native closed-word enumerations were performed at lengths 2,4,6, respectively 12,396,19920 words; the computed (fixed,covariant) ranks were (2,1),(4,3),(8,4). Every witness and its determinant were checked. Ten exact integer-recurrence values at m=0,...,9 (length 0,...,18) agreed with native endpoint_weight and endpoint_multiplicity. The recurrence alone was evaluated at n=24,40,80,120,200; the n=200 native unit-return count has 695 binary bits and the non-unit weighted common-denominator integer numerator has 789 bits. The witness-extension equality was directly checked for t=1,2,3 and proved symbolically for all t. Two independent executions yielded identical JSON and stdout.

Reproduce with `tar -xJf EC49BX_execution_evidence.tar.xz`, place the **pinned** `signed_brc.py` in a `source/` subdirectory alongside the verifier, then run `python VERIFY_EC49BX.py`. All comparisons use integers/Fraction, not floating point. No physical dynamics or phase/cancellation model was executed.

## Real authority, handoff and next mathematical unit

The native service (0.6.11) returned `research_authority_granted=false` and the owner/tasks query returned `CONTROL_QUOTA` on 2026-10-31. Current formal owner was not verified; this source-preservation commit does not establish native activity registration, CLAIM, Result, Driver review or mathematical admission.

**EC49BY:** Obtain a typed bit-operation complexity bound for DFA-filtered endpoint BRC dynamic programming in terms of path length, automaton size, fixed H, and output bit size. Contrast all-path native BRC aggregates with arbitrary supplied unit-multiplicity bags, including sparse representations and observer-composition preservation. Preserve the exact source pins, scope and current author-only status.

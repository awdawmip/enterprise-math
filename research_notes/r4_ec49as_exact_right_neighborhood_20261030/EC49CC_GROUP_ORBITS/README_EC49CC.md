# EC49CC — Exact symmetry-orbit reduction for signed-X6 BRC spectral computation

**Classification:** Author-side analytic proof + executed exact finite audit; PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. No Source-native CLAIM/Result/review or physical heartbeat propagation is asserted.

**Frozen source snapshot (2026-10-31):** GLOBAL_KNOWLEDGE_V1 main 30c9c016803244ac83e814c3253dbd2c9c0d554a; Enterprise Math main a9f5eb650bbee893c6128746ade4c0c90a1a4603; predecessor PR #1730 head b52ef077ee19fedd17a801cdafa0276b6e5c1d7a (EC49CB). Native BRC implementation: Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176. P000, ACTIVE worldview, and original native source remain unchanged.

## Input, declared observations and future-operation limit

The carrier is the original six native spatial axes, with twelve signed primitive letters Σ={+E_i,-E_i:1≤i≤6}, six signed displacement coordinates, ordered path provenance and path multiplicity. The model is static path combinatorics; no extra spatial axis or untyped physical-time conclusion is introduced.

For each positive +E_i, channel 0 uses the weight vector W=(2,3,3,2,1,1), channel 1 uses W'=(3,2,3,2,1,1). Negative letters have weight one in both channels, and channel 2 counts words. A nine-state deterministic automaton detects adjacent ordered substrings A=(+E_1,+E_2) and B=(+E_2,+E_1). The four terminal atoms, in order 00,01,10,11, record the Boolean occurrence bits (A,B). The exact required output has twelve coordinates: each atom's two positive weighted BRC totals and its unweighted count, restricted to zero native displacement. It does not support undeclared future append/filter operations without further proof.

Let p be prime and ω an element of multiplicative order L in F_p, with L dividing p−1. For e in (Z/LZ)^6, define the *unprojected* full-output integrand:

    F_n(e)[a,c] =
      Σ_{u ∈ Σ^n : detector(u)=a}
         weight_c(u) · ω^{<e, displacement(u)>}  (mod p).

The six-dimensional root average L^{-6}Σ_e F_n(e) filters words of displacement divisible by L. At even n and odd L with 2L>n, no nonzero reachable six-dimensional displacement can be an L-multiple: displacement parity is even and the least nonzero even-parity integer L-multiple has L1-norm 2L. Hence the average gives exactly the native zero-displacement BRC sum. As in EC49CA/CB, with positive integer weights the unfiltered native total B_n bounds each terminal coordinate (the two weighted totals agree by axis relabeling; count is bounded by them here because all W_i≥1). If p>B_n, the finite-field residue is the unique exact nonnegative integer output. These hypotheses guarantee no alias and no modular ambiguity separately.

## Theorem 1 — non-scalar equivariance

Let s=(1 2) and t=(5 6) act on the six signed axis letters and on all six root-grid exponents. Let T act on the twelve terminal output coordinates by exchanging both detector bits (01↔10) and the two weighted channels (0↔1); the count channel is unchanged.

For **all** word lengths n and all root tuples e,

    F_n(s·e) = T F_n(e);
    F_n(t·e) = F_n(e).

**Proof:** For each ordered word u, relabel every letter bijectively as s·u. The six-dimensional displacement and root monomial transform covariantly. The two monitored ordered patterns are exchanged; the channel-0 positive weights become channel-1 positive weights; negative weights and the count channel remain unchanged. Reindexing the sum produces the first equality in all twelve coordinates. Under t, both monitored patterns are unchanged and axes 5 and 6 have identical weights in every channel, giving the second equality. The bijections preserve word order, signs and multiplicity; no path quotient or scalar-amplitude cancellation is used. QED.

Within the explicitly limited class of **axis permutations that merely permute the declared pattern labels and weight-channel functions**, K=<s,t> is the largest symmetry subgroup: preservation of {A,B} forces {1,2} invariant; among remaining axes the two-channel positive-weight pairs are (3,3) on axis 3, (2,2) on axis 4, and (1,1) on both axes 5 and 6. Thus only 5↔6 is additionally possible. This is **not** a claim of maximality among arbitrary linear representations or accidental symmetries after the terminal sum.

## Theorem 2 — exact K-orbit formula and sharp representative count

Take one representative e of each K-orbit by ordering e_1≤e_2 and e_5≤e_6. Define δ12=1 if e_1<e_2, otherwise 0; δ56=1 if e_5<e_6, otherwise 0. The contribution of the distinct grid points in that orbit is precisely

    (1+δ56) ( F_n(e) + δ12 T F_n(e) ).

This is a sum over the actual two commuting involution orbits, not multiplication by a presumed free action. When e_1=e_2, the fixed-point relation F_n(e)=T F_n(e) is checked directly and follows from Theorem 1. Consequently the complete twelve-coordinate root average is obtained from one transfer evaluation per K-orbit.

Burnside's orbit formula gives the exact number of evaluations:

    N_K(L) = (L^6+2L^5+L^4)/4 = L^4(L+1)^2/4.

For the smaller subgroup H=<s> one has N_H(L)=(L^6+L^5)/2. The reduction in number of root-grid evaluations is exact for all L. The result does **not** establish an equivalent wall-clock speedup, nor beat sparse integer BRC DP in the tested regime. The Cauchy–Frobenius orbit-counting theorem and finite-field root filters are existing mathematical techniques; the new author-side certificate is this typed BRC-DFA equivariance and exact K action.

## Counterexample — why fixed-channel scalar orbit folding fails

In F_11 let L=5, ω=3 (order five), and compare x=(3,1,1,1,1,1) with s·x=(1,3,1,1,1,1). For the unfiltered one-step channel-0 transfer P_W(x)=Σ_i(W_i x_i+x_i^{-1}), its values are respectively 3 and 5 modulo 11. At two steps P_W(x)^2=9 but P_W(s·x)^2=3 modulo 11. Doubling one scalar representative instead of transporting channel+atom labels is false. This is a **pointwise finite-field obstruction**, not a complete CRT reconstruction modulo 11. It demonstrates exactly why the output transformation T is necessary.

## Actually executed certificate and numerical scope

VERIFY_EC49CC.py executes a nine-state finite-field transfer at K-orbit representatives with exact stabilizer multiplicities. An independently structured integer displacement DP with return-cone pruning computes the same twelve outputs and calls the unchanged native BRC endpoint_weight/endpoint_multiplicity functions for the unfiltered totals. H-orbit evaluation is cross-checked for n=4 and n=8, and the entire uncompressed character grid is checked at n=4.

| even path n | odd L | prime p | full grid L^6 | H orbits | K orbits | native weighted BRC | closed words | integer DP peak states |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 3 | 1000000000177 | 729 | 486 | **324** | 1560 | 396 | 94 |
| 8 | 5 | 1000000000211 | 15625 | 9375 | **5625** | 18921000 | 1281420 | 1874 |
| 10 | 7 | 1000000000189 | 117649 | 67228 | **38416** | 2737312704 | 96807312 | 5932 |

At length n=10 the exact atom vectors (channel 0, channel 1, word count), ordered 00/01/10/11, are:

    (2301388704,2301388704,85795032)
    (205661520,205661520,5275080)
    (205661520,205661520,5275080)
    (24600960,24600960,462120)

The K orbit reduction eliminates 64% of character evaluations at L=5 and about 67.35% at L=7. In one local run, K spectral evaluation versus direct integer DP took approximately 1.25s versus 0.036s at n=8, and 11.43s versus 0.217s at n=10. These are machine-local measurements, not asymptotic benchmarks; the sparse integer DP remains much faster on these inputs.

All-n proofs are the word relabeling and finite group action above. Finite checks cover exactly n=4,8,10 and stated variants; no Lean/formal proof assistant verification, independent reviewer replication or physical model calibration is claimed.

### Reproduction and source binding

Execute on the existing PR branch using Python 3.11+ standard library:

    python research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49CC_GROUP_ORBITS/VERIFY_EC49CC.py

The checker imports unchanged sibling EC49CA_CRT/native_signed_brc.py at Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176. It emits EXACT_REPORT_EC49CC.json and aborts if an atom vector, return total, primality/no-alias/modulus bound, fixed-point orbit identity or orbit count disagrees. The executed source file and exact output report are preserved beside this README.

## Permissions and next EC49CD unit

At the 2026-10-31 01:32 UTC service snapshot, research_authority_granted=false, executor_binding_configured=false, registered_session_count=0 and active subject quota 5/5. An attempted native owner-list read returned CONTROL_QUOTA, so the **current Source owner is UNKNOWN**, not assumed free or transferred. This PR is an author-side portable draft, not canonical main or an admission event.

**EC49CD:** build an exact **signed-displacement sparse-DP orbit quotient** using the same K action and complete 12-coordinate observer fiber; rigorously handle stabilizers, word multiplicity and backward-return pruning. Compare orbit state counts and integer bit operation resources at n=10,12 against the original integer DP. Show a counterexample if scalar-state grouping loses channel/atom data. Preserve native P000 and source pins; do not self-review under another identity.

External context: classical Burnside/Cauchy–Frobenius orbit enumeration and finite-field root-of-unity filters; not a claim of external novelty for these standard tools.

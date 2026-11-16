# PREFIX-829 — Ideal delayed-observer source counts and a sharp PTE reduction

**Status:** AUTHOR_PROVED / EXACT_BIGINT_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Scientific input:** pinned awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d, via PREFIX-827/828. **Model:** the exact finite named positive-count BRC operator Q=R+A, not native physical X6 time. Current P000 and joint observer safety are retained. This is an independent portable research unit and creates no shared Task CLAIM.

## 1. Exact first-separation characterization

For an integer n≥1, let p≥1 be the number of initially present independent named unmarked sources, with positive integer removal weights A=(α_1,…,α_p) or B=(β_1,…,β_p), identical capacity q=p, distinguished mark initially absent, and common nonnegative distinguished insertion/removal weights a,b. Every Q step removes one currently present unmarked source with its weight, removes a present mark with weight b, or inserts an absent mark with weight a when below capacity. Y_l(t;A) denotes the sum of weights of all length-t named trajectories ending with occupancy l. Work with the full histogram Y(t), not a scalar total.

Write e_k(A) for the elementary symmetric polynomial in the p source weights, with e_0=1 and e_k=0 for k>p. Fix equal cardinality and common a,b.

**Theorem 829.1 (first-discrepancy criterion).** The two complete occupancy histograms are identical at every t=0,…,n−1 and differ at t=n if and only if

e_k(A)=e_k(B) for k=0,…,n−1, while e_n(A)≠e_n(B).

When these conditions hold, the first difference at t=n is entirely in occupancy bin p−n, with exact signed *difference of two positive counts*

ΔY_(p−n)(n)=n! [e_n(A)−e_n(B)].

The statement requires p≥n; its sign is an inter-configuration difference and is not a signed branch amplitude.

**Proof.** By PREFIX-827 Theorem 827.1, Y(t) depends only on e_0,…,e_t, which gives the forward implication of moment agreement to equal full histograms. Conversely, for every 0≤k≤min(p,n−1), the saturated absent-mark state has exact triangular readout Y_(p−k)(k)=k! e_k: an occupancy drop of k in k steps can only comprise k different unmarked-source removals. Thus equal histograms imply equality of e_k for all k<n that exist. If p<n, equality of all e_0,…,e_p gives identical multisets (from the monic polynomial ∏(X−α_i)), hence identical future histograms, so first separation requires p≥n. At time n, the only branch reaching occupancy p−n uses all n steps for distinct unmarked removals, yielding n!e_n. Every other bin's difference depends only on e_0,…,e_(n−1) at this time: a branch with d=n unmarked removals has no step left for a marked operation. The criterion follows. □

By Newton identities, for fixed source count p, equality of the first n−1 elementary polynomials is equivalent to equality of the first n−1 ordinary power sums, and a differing e_n is equivalent to a differing nth power sum. Thus the positive-source minimal-cardinality problem is precisely an integer Prouhet–Tarry–Escott (PTE) first-separation problem. In particular **p_min(n)≥n**; equality p_min(n)=n is exactly the existence of an ideal PTE pair of size n with positive entries.

## 2. Explicit cardinality-optimal certificates

Each row gives two positive-integer weight multisets, with q=p=n and common a=2,b=3. For all rows, their full Q-only occupancy histograms are equal at t<n; at t=n their *only* difference is the bin 0 value shown (A minus B).

| n | A | B | e_n(A)−e_n(B) | ΔY_0(n) |
|---:|---|---|---:|---:|
| 1 | 1 | 2 | −1 | −1 |
| 2 | 1,4 | 2,3 | −2 | −4 |
| 3 | 1,5,6 | 2,3,7 | −12 | −72 |
| 4 | 1,7,8,14 | 2,4,11,13 | −360 | −8,640 |
| 5 | 1,18,19,44,48 | 4,8,33,34,51 | −1,108,800 | −133,056,000 |
| 6 | 1,6,7,17,18,23 | 2,3,11,13,21,22 | −100,800 | −72,576,000 |
| 12 | 1,12,25,66,91,130,174,213,238,279,292,303 | 4,6,31,58,105,117,187,199,246,273,298,300 | −67,440,294,559,676,054,016,000 | −32,304,008,998,556,125,355,350,425,600,000 |

**Consequently p_min(n)=n for n=1,2,3,4,5,6,12.** This replaces PREFIX-828's exponential-size construction with the actual information-theoretic minimum at these exact horizons.

The n=5 pair admits an especially compact integer certificate: choose signed offsets x=(−25,−8,−7,18,22), for which Σx_i=Σx_i³=0. The two positive families 26+x_i and 26−x_i have matching first four power sums by the finite binomial theorem, but differing fifth sums. This also proves the elementary-coefficient equalities without a numerical search claim.

The n=6 row translates a known ideal size-six PTE witness into positive weights by adding 1. The n=12 row translates an ideal symmetric size-twelve PTE witness by adding 152. Their power-sum equalities and first nonzero e_n were *independently checked with exact integers* for this BRC translation. Literature provenance:
- Eric W. Weisstein, "Prouhet–Tarry–Escott Problem", MathWorld, https://mathworld.wolfram.com/Prouhet-Tarry-EscottProblem.html .
- "Prouhet–Tarry–Escott problem", ideal-solution examples (size 6 and symmetric size 12), https://en.wikipedia.org/wiki/Prouhet%E2%80%93Tarry%E2%80%93Escott_problem .
- D. Coppersmith, M. Mossinghoff, D. Scheinerman, J. VanderKam, *Ideal solutions in the Prouhet–Tarry–Escott problem* (2023), https://arxiv.org/abs/2304.11254 .

These are existing number-theory witnesses newly applied and exactly validated for this narrow BRC observer; no claim of newly discovering the classical ideal PTE examples is made.

## 3. Source-efficient delay lifting

**Theorem 829.2 (one-step delay lift).** Let A,B each have p positive weights with e_0,…,e_(n−1) equal and Δe_n≠0, and select any positive integer h. Form multisets

A' = A ⊔ (B+h),   B' = B ⊔ (A+h),

where +h translates each weight and ⊔ is disjoint *named-source* concatenation (multiplicity retained). Then A', B' have 2p sources each, their first n elementary polynomials agree, and

e_(n+1)(A')−e_(n+1)(B') = n h [ e_n(A)−e_n(B) ] ≠0.

For capacity q'=2p with absent mark, the first full Q-histogram difference is at time n+1, bin 2p−(n+1), with ΔY=(n+1)! n h Δe_n.

**Proof.** Let F_A(z)=Σ_{α∈A}z^α and F_B similarly, interpreted as finite integer polynomials. Equality of their first n−1 power sums means F_A−F_B has a zero of multiplicity n at z=1, and the nth derivative difference there is nonzero. The lift satisfies

F_(A')(z)−F_(B')(z)=(1−z^h)(F_A(z)−F_B(z)),

so its zero order at 1 increases from n to n+1. Its first unequal power sum is Δs_(n+1)'=−(n+1)h Δs_n. Newton's identities give Δs_n=(−1)^(n−1)n Δe_n and Δe_(n+1)'=(−1)^n Δs_(n+1)'/(n+1)=n h Δe_n. Apply Theorem 829.1. □

Taking the explicit base at n=4,5,6,12 and lifting repeatedly gives the rigorously constructive upper bounds

p_min(n)≤4·2^(n−4) (n≥4);
p_min(n)≤5·2^(n−5) (n≥5);
p_min(n)≤6·2^(n−6) (n≥6);
p_min(n)≤12·2^(n−12) (n≥12).

Select the strongest available bound. For example at delay 13, **24** positive named sources suffice (12-base + one lift), compared with **4096** in the original parity-partition construction. The lower bound remains 13, so 24 is an upper bound, not a minimality claim. Choosing h larger than the current weight range keeps translated sets positive and nonoverlapping across the two layers.

## 4. Exact independent verification

The accompanying standard JavaScript BigInt checker computes e_k by a descending integer recurrence and **independently enumerates every named subset/mark transition** for each example, without invoking the closed-form observation formula. It checks each complete occupancy histogram at t=0,…,n, that every t<n is equal, that the first discrepancy occurs in the unique specified bin, and that its exact value is n!Δe_n. This includes 12-source, 4096-subset support; it is a finite exact check of the listed examples, not the proof of Theorems 829.1/829.2. It also checks explicit one-step lifts from n=4,5,6,12 by integer elementary coefficients and the closed difference identity, not by exponential-state enumerations.

Validation result JSON: PREFIX829_R6_IDEAL_PTE_DELAY_RESULTS.json.
Reproduction: node PREFIX829_R6_IDEAL_PTE_DELAY_CHECK.js.
All integers in these checks use BigInt; no floating-point rounding, numerical spectral estimates or native BRC–Shor physical trajectory substitution.

## 5. Frontier and contribution scope

The new theorem identifies **the exact combinatorial obstruction** to minimum p=n for each delay: an ideal integer PTE solution in positive weights. Further work: build and check explicit optimal source certificates for n=7…11 and source-count/maximum-weight Pareto bounds; determine whether richer observers with single-source addressing detect the constructed differences earlier. Independently preserve PREFIX-825's open minimal nonnegative carrier problem for Q-only q≥5,b>0.

The research is on the declared Q-only positive-count BRC auxiliary layer. It does not claim all-source provenance, signed/phase information, X6 Cell/Link/Port physical permission, nor a heartbeat time calibration. Its temporal index counts discrete Q applications. The frozen scientific input pin remains unchanged. No shared-task Result/Review/CLAIM or native acceptance is requested by this paper.

# R762HV — exact Port-parity census and spectral mixing law

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Date: 2026-11-21. Independent portable research, no claim of current native RUN/PROGRESS or Result acceptance.

## Source, scope and question

Continues R762HU@0e5a7b56c7a3c00907b6cdd0c844c6f85e4de02c and R762HT. Frozen task-science pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389; task RS-X6-TRIADIC-CLOSURE-DYNAMICS. P000 and ACTIVE worldview remain unchanged.

Here X={0,...,5}; Ports are the 15 unordered pairs p⊂X, |p|=2. A legal directed Port transition p→q requires |p∩q|=1 and carries the three-axis composite support h(p,q)=1_(p∪q)∈{0,1}^6. Each Port has 8 successors. The support is a *composite model readout*, not a primitive three-force TRIADIC_CLOSURE_E result. Fix one rooted Port p, and let E_m(p) count **unsigned**, ordered, rooted closed m-transition Port histories whose six axis-occurrence totals are all even. Let P_m(p) count all rooted closed m-transition Port histories. Every event retains its order; repeated event types contribute independent choices.

The remaining open Port/sign question is whether an all-even realizable support histogram can have C(n)=0, where C(n) counts zero-six-vector signings. The present result counts the precisely parity-eligible Port histories and establishes their asymptotic density; it does not presuppose signing.

## HV1 — exact six-bit BRC character projection

For x=(x_0,...,x_5)∈{−1,+1}^6, let M_x be the 15×15 real symmetric integer matrix indexed by Ports:

M_x[p,q] = (∏_{i∈p∪q}x_i)  if |p∩q|=1, and 0 otherwise.

Then for every integer m≥0,

E_m(p) = (1/64) ∑_{x∈{±1}^6} (M_x^m)[p,p].                  (HV1)

Proof: expand the matrix power as a sum over each ordered rooted closed Port path. The path with total occurrence vector H contributes ∏_i x_i^{H_i}. Summing independently over each x_i yields 64 if all H_i are even, and 0 otherwise. Every retained path has positive weight one. This is an exact parity projection of nonnegative path sources: character signs are an algebraic *filter*, not negative BRC mass or physical cancellation.

Since ∑_i H_i=3m, E_m(p)=0 for odd m.

## HV2 — the exact Port-even mixing density is 1/32

For each even m≥0,

P_m(p)=(8^m+14·2^m)/15.                                    (HV2a)

Write ρ=1+√33 (<7). Then

| E_m(p) − P_m(p)/32 | ≤ (31/32) ρ^m.                         (HV2b)

Consequently, along even m→∞,

E_m(p)/P_m(p)→1/32,   E_m(p)/8^m→1/480.                   (HV2c)

Both limits hold for every root Port. A useful explicit consequence is

E_m(p) = (8^m+14·2^m)/480 + O(ρ^m)  (m even).              (HV2d)

Proof of HV2a: Let B be the 15×6 unsigned Port-axis incidence matrix, B[p,i]=1 if i∈p. For the untwisted adjacency A=M_(+1,...,+1), we have A=BB^T−2I_15 and B^TB=4I_6+J_6. Thus A has eigenvalues 8 (once), 2 (five times), and −2 (nine times). The symmetric group on six axes acts transitively on Port roots, so (A^m)[p,p]=tr(A^m)/15. For even m this is HV2a.

Proof of HV2b: For the all-minus character, M_(-1,...,-1)=−A, so it contributes another A^m at even m. Every other character has between 1 and 5 minus entries. Axis permutations preserve its matrix spectrum, so only minus-count k=1,2,3 needs separate analysis; k↔6−k negates the matrix.

The exact characteristic polynomials for k=1,2,3 (variable λ) are

k=1: (λ+2)^5 (λ²−2λ−32) (λ²−2λ−2)^4.
k=2: λ³ (λ+2)^2 (λ+4) (λ²−2λ−4)^3 (λ³−2λ²−28λ+32).
k=3: λ^5 (λ²−28) (λ²−2λ−6)^2 (λ²+2λ−6)^2.

These are also independently checked using exact integer Newton traces in the accompanying standard-library Python program. For k=1 the maximum absolute eigenvalue is 1+√33. For k=3 every root has modulus <6. For k=2 the cubic's three roots lie respectively in (−6,−4), (1,2) and (5,6), by direct sign changes; its remaining factors have roots of modulus <6. Hence all 62 mixed-character symmetric matrices have operator norm ≤ρ. For a unit basis vector e_p, |e_p^T M_x^m e_p|≤ρ^m. Removing the two pure characters from HV1 gives

E_m(p)= (2/64)P_m(p) + (1/64)∑_(mixed x) (M_x^m)[p,p],

so HV2b follows. Divide by P_m(p)≥8^m/15 or by 8^m to obtain HV2c. All calculations are exact on this finite matrix family. QED.

## HV3 — exact finite census, independent computational crosscheck

The accompanying Python 3 standard-library checker implements a positive integer BRC dynamic program over (Port, 6-bit parity), with 960 states, for every length m≤26. It independently evaluates the 64-character Fourier sum for m≤12 and computes the k=0,...,6 characteristic polynomials by Newton identities using unbounded integers. All checks PASS.

| m | E_m(root 01) parity-even closed Port histories | P_m(root 01) all closed Port histories |
|---:|---:|---:|
| 2 | 8 | 8 |
| 4 | 168 | 288 |
| 6 | 4,960 | 17,536 |
| 8 | 177,536 | 1,118,720 |
| 10 | 7,289,184 | 71,583,744 |
| 12 | 333,869,824 | 4,581,302,272 |
| 14 | 16,704,767,360 | 293,203,116,032 |
| 16 | 895,432,338,432 | 18,764,998,508,544 |
| 18 | 50,536,314,156,544 | 1,200,959,900,876,800 |
| 20 | 2,960,499,535,228,928 | 76,861,433,641,435,136 |
| 22 | 178,075,797,825,189,888 | 4,919,131,752,993,128,448 |
| 24 | 10,911,885,695,401,934,848 | 314,824,432,191,325,339,648 |
| 26 | 677,370,234,552,288,468,992 | 20,148,763,660,243,882,213,376 |

The first four parity totals match earlier R762HP/HR rooted Port counts (2,4,6,8). The 10/12-event parity totals also match R762HM. Those are reused comparison points; the 14..26 totals and HV1/HV2 spectral theorem are this unit's new outputs.

Exact finite verification coverage: all 15·64 local states reachable in the parity DP, rooted at Port 01, through length 26; complete independent Fourier comparison through length 12; all 7 character classes for polynomial identity. The all-length theorem rests on the explicit matrices and algebraic proof, not finite extrapolation. Code is unsigned-path arithmetic and all counts are arbitrary-precision Python integers.

## Research value and continuation

The exponent parity requirement becomes asymptotically only 1/32 of *closed* Port histories, because parity totals satisfy one global relation (three incidences per event). For a candidate support histogram n, use the positive Port BRC coefficient N_p(n) and independent sign count C(n) of R762HT, with J_p(n)=N_p(n)C(n). This new character projection certifies the aggregate parity-eligible search-space size, but is not by itself a test of whether C(n)>0.

Next discriminating unit: search support histograms in the 14+ event parity-eligible rooted Port population, classifying N_p(n)>0 and C(n)=0 without collapsing Port connectivity into support overlap. Retain the actual Port Eulerian realization, ordered steps, sign-source counts and frozen-science provenance for each witness. Separately, original P000 TRIADIC_CLOSURE_E Cell/Link/Port/time/rotation lifting remains open.

Provenance: derived independently from the exact R762HU candidate formalism, current P000 / ACTIVE worldview and frozen task pin; published as portable scientific evidence only. No altered P000, no Task claim, no native PROGRESS/Review asserted.
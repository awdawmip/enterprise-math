# R5 finite extension: exact O(N) period for m=5,...,17 and m=20

Date 2026-11-22. Frozen R5 input enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Parent verified m=1,...,4 at enterprise-math@0a9a5cb9d79e4200521ef50cfe90ee9ca82225e1. This is author-side **exact integer computational proof** with reproducible source; status NOT_REVIEWED.

## Theorem and finite coverage

For every integer m in {1,...,17,20}, under the same true-five-event scalar partition model with prices 214,...,314 and the five original event supports,

M_m(O_m(N))=229746052653717600.

m=1,...,4 use previously stored independent exact computations; m=5,...,17 and m=20 are new exact runs in this unit. The missing m=18,19 and m≥21 are **not asserted** here. In particular, the separate new all-threshold order-43 theorem proves that m≡0,37,...,42 (mod 43) has a strictly smaller period than this maximum; thus universal equality for all m is false.

## Factorization lemma: replace 31 global intersections by 7 exact core intersections

The groups U={214,...,221}, V={223,...,290}, W={296,...,312} are pairwise disjoint. The first three events E0,E1,E2 live in U and have true overlaps. E3 lives in V, E4 in W. All other prices are unrestricted.

Define A_m(q) as the **local numerator** of the event union E0∪E1∪E2 on U, retaining the seven nonempty core inclusion-exclusion subsets and their simultaneous capacity constraints. Let B_m(q) and C_m(q) be the single-event local numerators for E3 on V and E4 on W, respectively. Then the complete global numerator satisfies the exact polynomial identity

R_m(q)=1-(1-A_m(q))(1-B_m(q))(1-C_m(q)).

Proof: the complement of the union E0∪...∪E4 is the simultaneous conjunction of the three block successes. Independence here is **combinatorial factorization across disjoint price sets**, not independence of the overlapping E0,E1,E2 constraints. Multiplying the three block successes by their disjoint unrestricted generating functions, then by D(q), yields the formula.

For each nonempty I⊆{0,1,2}, the core intersection uses state c=(c_i)_{i∈I}, each 0≤c_i≤m-1. On price p with event membership J_p={i∈I:p∈S_i}, a multiplicity r updates c_i→c_i+r for i∈J_p and leaves other counters unchanged, with r bounded by all affected capacities. This DP enumerates the exact finite local intersection polynomial without losing price/event provenance.

For B_m and C_m, use complete homogeneous coefficients h_r of their weighted prices: h_0=1 and, on adding price p, h_r←h_r+q^p h_{r-1}. The truncated single-event sum is Σ_{r=0}^{m-1}h_r. Product factors form the corresponding local numerator.

## Exact pole proof and certificate

Compute in Z[q]/(q^d-1) both the value and Euler derivative D_q=q∂/∂q for the above numerator, using typed jet multiplication (f,Df)(g,Dg)=(fg,(Df)g+f(Dg)). Reduce each complete cyclic vector modulo Φ_d(q). For each of the 14 witness orders

7,9,11,13,17,19,23,25,27,29,31,32,37,43,

the first nonzero zero/first-jet vector leaves a pole of order ≥3 at the primitive d-th roots. The lcm of the 14 orders is L=229746052653717600. Independently, the 101-price denominator has no order outside the previously enumerated 39 candidates with pole order ≥3; their lcm is L. Therefore the measured 14 nonzero witness conditions certify the **exact** minimum period for each checked m.

At m=4 the same factorized implementation reproduces all 14 signed first-coordinate/jet witnesses already committed in the parent certificate (not merely the lcm), including d=7 (-1519 at coordinate 2), d=9 (-7776), d=27 (+6021), d=31 (+744), d=43 (+1). This crosschecks the new factorization against the historical independent whole-event computation.

For m=5 the new witness vectors have first decisive coordinates and pole orders recorded in FINITE_CERTIFICATE.json. For each m=6,...,17 and m=20, the integer run returned all 14 surviving orders and the exact lcm L. The calculations used Python 3 arbitrary-precision integers and SymPy 1.14.0 solely for exact cyclotomic reduction; no floating point or numerical root tests.

## Reproduction and boundaries

From this directory run python VERIFY_FINITE.py 4 for m=5, python VERIFY_FINITE.py 3 to crosscheck m=4, or python VERIFY_FINITE.py 19 for m=20. The argument to the script is CAP=m-1, and each invocation asserts all 14 poles survive and the lcm equals L, printing ALL CHECKS PASS.

The finite ranges have exact exhaustive algebraic state enumeration for each listed m; they do not form an infinite all-threshold theorem. The separate RESEARCH.md in this directory supplies the infinite theorem for the primitive-43 factor. Both results operate in the frozen scalar partition model without changes to P000 or native heartbeat dynamics.

Next: optimize core capacity computation or derive a rational threshold generating function for the **other** witness roots, so that m=18,19 and then complete residue classifications can be handled without repeated large-capacity enumeration. Retain mathematical review as NOT_REVIEWED and protect active task ownership.

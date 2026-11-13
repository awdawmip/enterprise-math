# R728 — S3 character-resolved positive BRC renewal and primitive nine-step lift

Date: 2026-11-12 (Asia/Shanghai). Author-side scientific continuation of R725–R727. Task context: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142, frozen P000 Source scientific pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Later derived V17 slot transport and R725's network classes have independent provenance. Predecessors: R725@a9ba60cab51fc98e4b39f73e5d0eda7f49c51bb3; R726@5ef47c8c33d09925c1d69119509cb6e0fbf904a1; R727@6ee088071f48a3f7e935918005f29b9ab6341519. Author proof and exact local integer tests are completed; independent review, actual native V29 implementation and formal Source Result are pending.

## I. Declared carrier and source-preserving observer

Inside P000's six-axis ambient X6 world, take the **derived five-axis** active triad carrier 01234 (it is not a separate native five-dimensional world). Vertices are the ten unordered 3-subsets, and the available sixty directed arcs connect vertices sharing two labels. The two R725 sharp 15-arc canonical representatives use lexicographic enumeration of those sixty arcs:

* Type A (R725 classes 1 and 2 under reversal): mask 211733226574.
* Type B (R725 classes 3 and 4 under reversal): mask 5363347296468.

A rooted positive source-distinct cyclic nonbacktracking (CNB) history is a directed sequence of m arcs based at 012 such that consecutive endpoints match and immediate reversal is forbidden, including at the cyclic seam. Slot transport begins at ordered frame 012, replacing the departing axis by the entering one in the same slot. A closed history ends with an ordered permutation h of 012. Let N_m(h) count these histories **with positive multiplicity and distinct ordered source histories**.

For a directed arc e=(u,v) define g_e as the position permutation that takes the sorted frame of u to the result of replacing its departed label by the entering label, expressed relative to the sorted frame of v. For an arbitrary ordered frame with slot permutation sigma at u, the update is g_e sigma. Therefore the full 90-state arc/frame lift retains every named-slot history.

## II. R728-A: exact all-length S3 character rational generating functions

Write I_m=N_m(012), P_m=N_m(021)+N_m(102)+N_m(210), and C_m=N_m(120)+N_m(201). Define integer formal series, with m starting at 1:

T(x)=Σ_m (I_m+P_m+C_m)x^m,   S(x)=Σ_m (I_m-P_m+C_m)x^m,
U(x)=Σ_m (2I_m-C_m)x^m.

T, S and U correspond to the trivial, sign and 2-dimensional standard characters of S3. The following expressions are **exact rational formal power series for all integer lengths m≥1**.

### A carrier

~~~text
T_A=(3x^3+7x^4+8x^5+4x^6)/(1-3x^3-7x^4-8x^5-4x^6)
S_A=(-x^3-x^4+2x^5)/(1+x^3+x^4-2x^5)
U_A=(2x^3-2x^5-2x^6+2x^7+6x^8+2x^9-6x^10-4x^11)
    /(1-2x^3+2x^5+2x^6-x^7-3x^8-x^9+3x^10+2x^11)
~~~

### B carrier

~~~text
T_B=(3x^3+7x^4+8x^5+5x^6+x^7)/(1-3x^3-7x^4-8x^5-5x^6-x^7)
S_B=(-x^3-x^4+2x^5+x^6-x^7)/(1+x^3+x^4-2x^5-x^6+x^7)
U_B=(2x^3-2x^5-3x^6+2x^7+6x^8+4x^9-4x^10-8x^11-4x^12+2x^13+2x^14)
    /(1-2x^3+2x^5+3x^6-x^7-3x^8-2x^9+2x^10+4x^11+2x^12-x^13-x^14)
~~~

Character inversion yields all three class counts for **each m**:

I=(T+S+2U)/6,   P=(T-S)/2,   C=(T+S-U)/3.

This is an exact observer-targeted compression of the full positive path history. R727's total-only count T loses an exact parity contrast S and identity/three-cycle contrast U. Individual named permutations still require the finer full 90-state transfer.

### Proof and exact certificate

Enumerate the 15 selected directed arcs E. Form the 15×15 nonbacktracking matrix B whose entry B[e,f] is one precisely if head(e)=tail(f) and tail(e)≠head(f); otherwise zero. P_R is the diagonal indicator of the arcs leaving root 012. R727 supplies T_m=tr(P_R B^m).

For the sign character use B_sgn[e,f]=B[e,f]sgn(g_f). For the standard character rho on the integer basis (e_0-e_2,e_1-e_2) of the sum-zero permutation module, use the 30×30 block matrix B_std[e,f]=B[e,f]rho(g_f)^transpose. The **transpose is required** because the trace multiplication cyclically reverses the order of step permutations relative to the original ordered-frame update; S3 character traces are conjugacy invariant. Thus for m≥1:

S_m=tr(P_R B_sgn^m),    U_m=tr((P_R⊗I_2) B_std^m).

For any n×n integer matrix M, Newton identities applied to p_k=tr(M^k), k=1,…,n, compute the exact coefficients c_k of det(I-xM). Integer Cayley–Hamilton is checked entrywise on the full n×n matrix. By the adjugate formula det(I-xM)tr(P(I-xM)^(-1)) is a polynomial of degree at most n-1. Its coefficients are determined by the first n exact projected traces, starting at m=0. Subtract the m=0 trace (the root outdegree times representation dimension) to obtain precisely the six rational expressions displayed above. This proves the all-length identities from a **finite complete algebraic certificate**, rather than extrapolating the finite counts.

The linked standard-library checker builds all three integer matrices for both carriers, computes all character determinants and numerators, verifies all Cayley–Hamilton entries and independently compares with source-distinct frame DP at m=3,…,14.

## III. R728-B: primitive exponent nine and six-state asymptotic equipartition

Lift each permitted arc e to six ordered-slot states (e,sigma) with sigma∈S3, and for every B[e,f]=1 insert the positive transition (e,sigma)→(f,g_f sigma). The 90×90 integer transition matrix L has **180 positive entries**. Full exact matrix-power calculation gives:

| network | positive entries L^8 | zero entries L^8 | positive entries L^9 | minimum/maximum L^9 entry | sum of L^9 entries |
|---|---:|---:|---:|---:|---:|
| A | 7992 | 108 | 8100 | 1 / 18 | 58764 |
| B | 8028 | 72 | 8100 | 1 / 18 | 61080 |

Consequently L^9 is strictly positive for both carriers, while L^8 is not; hence **the exact primitive matrix exponent equals 9**.

For each right deck action (e,sigma)→(e,sigma tau), the lift commutes with the action. Perron–Frobenius for a primitive positive-in-a-power matrix implies that its unique positive Perron left/right eigenvectors are invariant under all deck actions, and thus constant across the six states over each directed arc. The Perron eigenvalue equals that of the base B (the fiber-constant invariant subspace). Since L is primitive, its other eigenvalues have strictly smaller modulus.

For each h∈S3 let N_m(h) be positive rooted CNB counts. The operator L, restricted to a fixed root outgoing arc and its six frames, recovers the h-dependence up to an arc-dependent inner conjugation. That fixed relabeling does not change the uniform vector. Therefore each of the six individual final holonomies satisfies, uniformly in h,

N_m(h) / Σ_g N_m(g) = 1/6 + O(eta^m)

for some 0<eta<1 depending on the carrier. Equivalently there are K>0, eta∈(0,1) such that for sufficiently large m, max_h |6N_m(h)/T_m - 1| ≤ K eta^m. This concerns the **uniform distribution over source-distinct positive CNB histories** of a specified length in the derived model. A different observer, path-weighting policy or native-Event executable carrier requires its own conclusion.

Although the two carriers have different total growth constants (R727: lambda_A≈2.059941, lambda_B≈2.069832), both have the same limiting one-sixth proportion.

## IV. Independently checked finite examples

| length m | A: identity / all transpositions / all three-cycles | B: identity / all transpositions / all three-cycles |
|---:|---:|---:|
| 4 | 1 / 4 / 2 | 1 / 4 / 2 |
| 5 | 1 / 3 / 4 | 1 / 3 / 4 |
| 6 | 3 / 6 / 4 | 3 / 6 / 5 |
| 7 | 8 / 20 / 14 | 8 / 21 / 14 |
| 8 | 15 / 50 / 32 | 15 / 50 / 32 |
| 9 | 27 / 84 / 52 | 27 / 88 / 54 |
| 10 | 53 / 154 / 102 | 57 / 164 / 108 |
| 12 | 260 / 772 / 524 | 267 / 798 / 543 |

The separate JSON certificate preserves both exact 15-edge networks, all six named-state populations by length m=3..14, class characters' exact integer polynomials, lifted positivity census and validation scope.

## V. Provenance, reuse and next scientific questions

This result applies BRC to **positive source-distinct branch multiplicities**, preserving the richer information beyond R725 Boolean six-state reachability. The character rational functions are exact under the declared finite observer, all lengths. P000's six axes, native triadic force balance and original science pin are unchanged. V17's 3-subset replacement is later derived lineage, not the frozen P000 physical Link/Port law. No independent mathematical review or real V29 dynamics admission is inferred from author tests.

The next discriminating research units are (1) obtain all **six individually named** rational generating functions from the 90-state deck transfer, compare minimal sufficient future-observer memory and exact mixing rates; (2) for each abstract arc, seek a typed V29 Link/Port inventory, Cell-state, signed direction and event-time witness, or a sharp concrete obstruction, then recompute the all-length character laws on the actually executable subgraph. Keep the original native X6 dimension and triadic source identity explicit.

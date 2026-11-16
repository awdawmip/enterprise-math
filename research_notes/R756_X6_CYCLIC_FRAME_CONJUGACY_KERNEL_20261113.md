# R756 — Exact conjugacy-class BRC kernel for cyclic three-packet frame transport

Status: AUTHOR-PROVED FINITE-GROUP THEOREMS; exact S3 enumeration PASS; native V39 event admission and independent Driver review OPEN.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Lineage: R754 PR #2184 (three-forward-schedule positive BRC kernel); R755 PR #2185 (66 cyclic-invariant triples; 18 exceptional noncommuting triples). P000/ACTIVE worldview unchanged.

## Question and bridge scope

R755 classified which fixed S3-labelled triples have identical final frame for the three forward cyclic serializations. R756 determines the complete output-fiber population, the exact residual coding cost, and an iterative BRC conjugacy kernel that retains rather than erases the residual.

Conditional bridge H: three actual V39 based-loop occurrences must be admitted, composable at compatible base and must have fixed, order-independent increments a,b,c. The algebra below does not assign a packet to a bare V29 PASS and does not assert native TRIADIC_CLOSURE_E admission. The later uniform-label ensemble is a separately specified auxiliary stochastic observer, not a native force law.

Let G be any finite group of cardinality N. For a,b,c in G, write z=abc and W=(abc,bca,cab). Denote the conjugacy class of z by C(z) and its cardinality by k. For the three-support BRC scheduler choose J uniformly from {0,1,2}; the observed endpoint frame is W_J.

For the additional uniform-label ensemble, condition on abc=z, choose a,b independently uniformly in G, and put c=(ab)^(-1)z. This distinguishes random assignments from a fixed labelled triple.

## Theorem 1 (exact independent conjugacy coupling; all finite groups)

Setting t=ab gives the exact identity

    (W0,W1,W2) = (z, a^(-1) z a, t^(-1) z t).

The map (a,b) -> (a,t=ab) is a bijection G^2 -> G^2, so a and t are independent uniform group elements under the uniform-label ensemble. Every conjugate of z has |C_G(z)| preimages. Thus W1,W2, conditioned on z, are independent uniform draws from C(z).

Consequently, among the N^2 ordered triples with product z, the three possible multiplicity patterns of forward endpoint readouts have exact counts:

    (3):       N^2 / k^2;
    (2,1):     3 N^2 (k-1) / k^2;
    (1,1,1):   N^2 (k-1)(k-2) / k^2.

Proof: the k^2 ordered pairs of independent class draws are equally frequent, and one pair is (z,z); exactly 3(k-1) pairs produce two different values; the remainder (k-1)(k-2) produce three different values. Each pair has (N/k)^2 preimages. These formulas are integers because k divides N. Their sum is N^2. QED.

## Theorem 2 (complete S3 BRC source/output fibers)

S3 has conjugacy classes of sizes 1 (identity), 3 (transpositions), 2 (three-cycles). Applying Theorem 1 to all six possible z yields:

| product type | all 3 equal | pattern 2+1 | all 3 distinct | triples |
|---|---:|---:|---:|---:|
| identity (k=1) | 36 | 0 | 0 | 36 |
| transposition (k=3) | 12 | 72 | 24 | 108 |
| three-cycle (k=2) | 18 | 54 | 0 | 72 |
| TOTAL | **66** | **126** | **24** | **216** |

Given the exact labelled triple (a,b,c), the uniform three-order BRC source J has d=1,2,3 distinct endpoint-frame outcomes respectively. When the future observation language consists only of the *final frame* and these labels are retained, the minimal fixed-length additional frame-outcome code is ceil(log2 d), i.e. 0, 1, 2 bits. Two schedules may produce one frame, so save an output-fiber index rather than always saving all three schedules. Other future languages (prefix V29 balances, serial provenance, packet-dependent composition) can require finer source data.

The Shannon endpoint-frame entropy for each fixed triple is: 0 for (3); log2(3)-2/3 for (2,1); log2(3) for (1,1,1). Averaging over all 216 uniformly chosen triples yields the exact value

    E[ H(W_J | a,b,c) ] = (25/36) log2(3) - 7/18
                        = 0.7117795143896918... bits.

This entropy is conditional on the specified ensemble and is not a general physical compression rate.

## Theorem 3 (exact conjugacy Markov kernel; any finite group)

Under the extra uniform-label ensemble and independent uniform J, the final-frame transition law from product z to endpoint y is

    K(z,y) = (1/3) [y=z] + (2/(3k)) [y in C(z)].

Let U average a function uniformly on each conjugacy class. Then K=(I+2U)/3 and U^2=U. For every integer n>=0,

    K^n = U + 3^(-n)(I-U),

    K^n(z,y) = [y in C(z)]/k
               + 3^(-n) ([y=z]-[y in C(z)]/k).

Hence if G has r conjugacy classes and |G|=N, its entire kernel spectrum is eigenvalue 1 with multiplicity r and 1/3 with multiplicity N-r. Proof: decompose functions into class-constant vectors (U=I) and classwise zero-sum vectors (U=0); the formula follows and counts their dimensions. K is symmetric/stochastic, so uniform distribution on G is reversible. QED.

For z belonging to a class of size k,

    P(Z_n=z | Z_0=z) = 1/k + (1-1/k)3^(-n),

    TV(K^n(z,.), uniform(C(z))) = (1-1/k)3^(-n).

Thus within-class source memory decays exactly at rate 3^(-n), while conjugacy class remains an exact invariant of the auxiliary process. In S3 the eigenvalues are 1^[3] and (1/3)^[3]. The largest TV prefactor is 2/3 for transpositions.

An additional exact source statistic: if J,J' are independent uniform cyclic schedule choices on the *same* uniform-labelled triple, then

    P(W_J = W_J') = 1/3 + (2/3)(r/N).

Proof: J=J' has probability 1/3. Given different indices and z, both readouts coincide with probability 1/k using Theorem 1. For uniform z, E_z[1/k]=r/N since each conjugacy class of size k contributes k*(1/k)=1. For S3, r=3,N=6, so this probability is exactly 2/3. QED.

## Verification and native continuation

The accompanying Python standard-library verifier exhausts all 216 S3 triples, the conjugation formulas, 66/126/24 pattern partition and each product-class row. Exact Fraction arithmetic checks all 36 entries of every K^n for n=1..6, row stochasticity, symmetry, and collision probability 2/3. These finite checks complement the general finite-group proofs; no numerical tolerance is used. Actual output is in R756_EXACT_EVIDENCE_20261113.json.

Next investigate an actually admitted V39 based-loop packet triple and Cell/Link/Port incidence on the frozen X6 input; test common-base composition and fixed order-independent labels. If lawful, decide whether the 0/1/2-bit endpoint-frame code remains sufficient for the declared future observer language, and retain V29 prefix or order residual wherever needed. This task's native TRIADIC_CLOSURE_E and V29/V39 coupling remain unresolved.

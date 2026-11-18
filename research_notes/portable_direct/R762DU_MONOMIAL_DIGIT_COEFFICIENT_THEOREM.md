# R762DU — Complete three-area endpoint BRC Lucas digit kernel

Date: 2026-11-18 (Asia/Shanghai). Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Author lineage EM-X6-3050F6, own SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Scientific state: **AUTHOR_PROVED / AUTHOR_CHECKED / NOT_REVIEWED**.

## Frozen input, observer and boundaries

Taskbook: awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md; frozen P000 V5 science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.

Reuse the six named positive BRC increments (0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1). Their exact count polynomial is
\[
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ.
\]
For each a>=1 let Q=3^a, and let C_Q(n;u,v,w) be the nonnegative integer coefficient of X^uY^vZ^w in P^n reduced by X^Q=Y^Q=Z^Q=1, for 0<=u,v,w<Q. This theorem concerns the **integer count modulo 3** in the monomial endpoint basis of the complete three-area observer. Coefficient 2 modulo 3 is not a negative force amplitude. It does not change native six-axis Cell/Link/Port semantics or assert a licensed TRIADIC_CLOSURE_E event.

## Main theorem — pointwise Lucas factorization and exact support

Let K_0,K_1,K_2 be the coefficient maps modulo 3 of 1,P,P^2 in the ordinary (noncyclic) polynomial ring, viewed on digit triples (r,s,t) in {0,1,2}^3.

| input digit | residue 1 | residue 2 | nonzero |
|---:|---:|---:|---:|
| 0 | 1 | 0 | 1 |
| 1 | 6 | 0 | 6 |
| 2 | 6 | 12 | 18 |

For n>=Q all endpoint residues C_Q(n;u,v,w) are zero modulo 3. For 0<=n<Q, write the a base-3 digits of n,u,v,w as n_j,u_j,v_j,w_j. Then the pointwise identity holds for every endpoint:
\[
\boxed{ C_Q(n;u,v,w)\pmod3
=\prod_{j=0}^{a-1}K_{n_j}(u_j,v_j,w_j)\quad\text{in }\mathbf F_3.}
\]

For n<Q, let N_1,N_2 be the counts of ternary digits 1 and 2 in n, and define S_Q(n), S_Q^+(n), S_Q^-(n) to count endpoint coefficients nonzero, equal to 1, or equal to 2 modulo 3. Then
\[
\boxed{S_Q(n)=6^{N_1}18^{N_2},\quad
S_Q^+(n)-S_Q^-(n)=6^{N_1}(-6)^{N_2}.}
\]
In particular, S_Q^± are the half-sum and half-difference. When n>=Q all three counts are 0. Maximum support among n<Q is 18^a, attained at n=Q-1.

Summing across **all** 3^a exponents before the nilpotence threshold:
\[
\boxed{\sum_{n=0}^{Q-1}S_Q(n)=25^a,\quad
\sum_{n=0}^{Q-1}S_Q^+(n)=\frac{25^a+1}{2},\quad
\sum_{n=0}^{Q-1}S_Q^-(n)=\frac{25^a-1}{2}.}
\]
Consequently the proportion of (n, endpoint) pairs with 0<=n<Q and nonzero count modulo 3 is exactly (25/81)^a.

The pointwise digit law evaluates a specified endpoint coefficient mod 3 using a small, constant-sized local table and a ternary digit product of length a. Complexity: O(a) digit operations, O(1) additional machine words, with bit-size accounting for input/output of size O(a). This is not an algorithm for full positive integer multiplicities or the exact BRC denominator.

## Complete algebraic proof

Of the 36 ordered branch pairs in P^2, the six diagonal pairs yield six distinct monomials with coefficient 1. Among fifteen unordered distinct-branch pairs, the three complementary pairs of branch indices (0,5),(1,4),(2,3) all sum to exponent (1,1,1), yielding coefficient 6. The other twelve pairs have distinct exponent sums, none coinciding with diagonal sums, yielding twelve monomials of coefficient 2. Thus 6*1+12*2+6=36 and the stated K_2 table has six residues 1, twelve residues 2 and nine residues 0 (the six-count center and eight unreachable triples). The K_0/K_1 rows follow directly.

In the polynomial ring over F_3, Frobenius gives for n<Q
\[
P(X,Y,Z)^n=\prod_{j=0}^{a-1}P(X^{3^j},Y^{3^j},Z^{3^j})^{n_j}.
\]
Each coordinate exponent contributed by factor j is 3^j times an integer between 0 and n_j<=2. Therefore the resulting three exponents have unique base-three digit decompositions and no cross-factor carries. Each monomial coefficient is the product of the unique digit-coefficients K_{n_j}; no different digit combinations collide. Every exponent coordinate is at most n<Q, so the cyclic reductions at Q do not identify distinct terms. This proves the pointwise statement.

Nonzero residue counts multiply digit by digit, so their one-digit values 1,6,18 produce 6^{N_1}18^{N_2}. The multiplicative sign character (1 maps to +1, 2 maps to -1) gives one-digit differences 1,6,-6 and the stated signed difference. For n=Q, in the cyclic group algebra over F_3,
\[
P^Q=P(X^Q,Y^Q,Z^Q)=P(1,1,1)=6\equiv0\pmod3;
\]
all larger powers vanish. Maximizing the product gives 18^a. Summing counts over all 3^a possible digit strings yields (1+6+18)^a=25^a and signed difference (1+6-6)^a=1, proving the two aggregate sign counts. QED.

## Reproducibility and scope of verification

Companion R762DU_VERIFY.js independently multiplies P in the cyclic group algebra F_3[C_Q^3] with a typed-array recurrence, checking every n from 0 through Q for Q=3,9,27,81. This tests 124 exponent cases, 44,136,684 complete endpoint coefficient-residue visits, and 569,182 pointwise digit-kernel comparisons (exhaustive for Q<=27, deterministic spread samples for Q=81). Integer arithmetic only. All four moduli passed, including the exact nilpotence boundary and aggregate sign counts. See R762DU_EVIDENCE.json for by-modulus counts and representative samples.

This theorem genuinely extends R762DT: that theorem concerns support in the augmentation basis x=X-1,y=Y-1,z=Z-1, whereas this one exactly identifies the observed **monomial endpoint coefficient** residue in all three area coordinates. Both use the positive candidate family; they are distinct, basis-sensitive descriptions. Review: NOT_REVIEWED; no formal Result or Working Truth admission.

## Continuing science

Investigate how to lift the digit kernel modulo 9 and 27 to identify sharp three-adic content witnesses for P^n at n>=Q, ultimately proving/refuting R762DN's full-three-coordinate conjecture v_3(gcd(P^n))=max(0,floor(n/3^{a-1})-2) for a>=2. Preserve all three endpoint area coordinates and signed Port provenance. Independently obtain the native licensed TRIADIC_CLOSURE_E Cell/Link/Port event rule and V17/V29/V39 transport before claiming future-event safe BRC compression.

Predecessors: R762DN@4e9001fe28f8bc19ce93e5a1f87d842a241d7756 and R762DT@2b00cadde50fa5528f4a6e87c0a027ec64767dba. Current behavior: docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, without altering scientific pins.

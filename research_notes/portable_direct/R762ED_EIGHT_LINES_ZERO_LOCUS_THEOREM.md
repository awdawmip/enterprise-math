# R762ED — Exact cyclotomic zero locus of the six-branch three-coordinate BRC model

Date: 2026-11-18 (Asia/Shanghai). Research identity: EM-X6-3050F6; Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Author-side proof and independent exact integer audit; external mathematical review NOT_REVIEWED.

## Frozen science and scope

Frozen P000: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Taskbook: awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md.

The six named, positive BRC branches have full three-coordinate terminal observer polynomial
\[
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ.
\]
All six branch identities, their ordered path provenance and native X6 residuals remain distinct in the original task. The present theorem is about this terminal group-ring observer's spectrum, not the signed native TRIADIC_CLOSURE_E event or its licensed Cell/Link/Port transports.

## Theorem — eight lines classify every zero (all Q=3^a)

For every integer a>=1, put Q=3^a and d=Q/3; fix a primitive Q-th root zeta. Define
\[
\lambda_{ijk}=P(\zeta^i,\zeta^j,\zeta^k), \quad i,j,k\in\mathbb Z/Q.
\]
This vanishes exactly on the union of **eight affine Q-point lines**, parametrized by arbitrary s modulo Q and t in {d,2d}:
\[
\begin{array}{c|c}
A_t&(s,t,t)\\
B_t&(t,s,-t)\\
C_t&(t,t,s)\\
D_t&(s,t-s,t+s)
\end{array}
\qquad(\text{coordinates mod }Q).
\]
Exactly twelve zero points lie on two lines and every other zero belongs to one; none lies on three. Therefore
\[
\boxed{\#\{\lambda_{ijk}=0\}=8Q-12},\qquad
\boxed{\#\{\lambda_{ijk}\ne0\}=Q^3-8Q+12}.
\]
The exact zero-character fraction is 8/Q^2-12/Q^3. At Q=27, this recovers and structurally explains the 204 zeros in the full exact R762EC cyclotomic spectrum.

## Proof

**Lemma 1 (six-term cyclotomic vanishing criterion).** Put
\[
(e_0,e_1,e_2,e_3,e_4,e_5)
=(0,i,k,i+j,j+k,i+j+k)\pmod Q.
\]
Choose representatives in [0,Q-1] and let H(T)=sum_{h=0}^5 T^{e_h} in the integer polynomial ring. Since zeta is a primitive 3^a-th root,
\[
\Phi_Q(T)=1+T^d+T^{2d}, \quad \deg \Phi_Q=2d.
\]
Since deg H<Q, H(zeta)=0 exactly when H=Phi_Q G for a polynomial G with deg G<d. Comparing coefficients yields for all r in {0,...,d-1}:
\[
[T^r]H=[T^{r+d}]H=[T^{r+2d}]H.
\]
These nonnegative integer multiplicities sum to six. Hence their multiset comprises exactly two cyclotomic triples {r,r+d,r+2d}, allowing the same r twice. Conversely any such pair of triples vanishes. All index multiplicities remain accounted for.

**Lemma 2 (ten index pairings).** Partition the six named indices into two triples and orient each partition by putting index 0 in the first triple. There are exactly ten cases. Both triples must be congruent within each group mod d and contain distinct residues mod Q.

Four cases give two Q-point families each:

| First index triple | Exact solutions |
|---|---|
| 012 | B_d or B_{2d} |
| 013 | C_d or C_{2d} |
| 024 | A_d or A_{2d} |
| 034 | D_d or D_{2d} |

For 012, 0,i,k must equal 0,d,2d in some order, so (i,k)=(d,2d) or (2d,d), with j arbitrary. The complementary exponents i+j,j+k,i+j+k automatically form the second cyclotomic triple. For 013, 0,i,i+j are a cyclotomic triple, giving i=j=d or i=j=2d and arbitrary k. For 024, 0,k,j+k similarly give j=k=d or j=k=2d and arbitrary i. For 034, 0,i+j,j+k must be 0,t,-t with t=d or 2d, forcing j=t-i and k=t+i; the complementary exponents i,k,i+j+k form the other triple.

For each of the six remaining index triples 014,015,023,025,035,045, the pair of common-residue constraints in each group implies i=j=k=0 mod d. Writing (i,j,k)=d(I,J,K) with I,J,K in {0,1,2}, direct checking of the 27 digit triples gives precisely:

| First triple | Only allowed (I,J,K) |
|---|---|
| 014 and 023 | 102, 111, 201, 222 |
| 015 and 045 | 110, 122, 211, 220 |
| 025 and 035 | 011, 022, 112, 221 |

All these exceptional solutions are on one of the eight lines already identified. This exhausts the ten index partitions, including repeated monomial values.

**Lemma 3 (overlaps).** Each line has Q points. Solving pairwise line equations gives exactly twelve distinct intersections, listed as d times the following digit triples:
\[
(0,1,1),(0,2,2),(1,0,2),(2,0,1),
(1,1,0),(2,2,0),(1,1,1),(2,2,2),
(1,1,2),(2,2,1),(1,2,2),(2,1,1).
\]
Every listed point is contained in exactly two lines, and all other points in at most one. The union thus has 8Q-12 members. Lemmas 1–3 prove the theorem for all a>=1. QED.

## Exact author-side cross-check

R762ED_VERIFY.py independently computes the cyclotomic coefficient-equality criterion and compares it with the eight-line predicate at every character for Q in {3,9,27,81}, checking all 551,880 triples. This uses only integer arithmetic in the Python standard library. It also exhausts the 27 top-digit possibilities for each exceptional index partition, checks exact multiplicities and emits SHA256 digests of ordered zero-coordinate triples.

| Q | Checked | Zeros | Nonzero characters |
|---:|---:|---:|---:|
| 3 | 27 | 12 | 15 |
| 9 | 729 | 60 | 669 |
| 27 | 19,683 | 204 | 19,479 |
| 81 | 531,441 | 636 | 530,805 |

R762ED_EVIDENCE.json contains executable-check outputs and digest witnesses. This is an author-side symbolic proof with a reproducible exact finite audit; independent review remains NOT_REVIEWED.

## Next scientific frontier

1. Combine the eight-line zero classification with R762EB–EC finite/deep cyclotomic strata to classify higher nonzero v_pi layers for Q=3^a.
2. Search for exact coefficient nondivisibility witnesses to settle the full three-coordinate all-horizon content v_3(gcd(coeff(P^n))) left open by R762DN.
3. Obtain actual signed TRIADIC_CLOSURE_E Cell/Link/Port legality and V17/V29/V39 transport; test future-observer descent before interpreting any terminal distribution compression as native future-safe state compression.

No P000 change, formal Result, review approval, or native event admission is asserted.

## Corollary — exact rational rank of every positive BRC convolution power

Let G=(Z/Q)^3 and let T_P be multiplication by the above P on the Q-vector space Q[G], represented in the Q^3-element group basis by its exact integer convolution matrix. For every integer n>=1,
\[
\boxed{\dim_{\mathbb Q}\ker(T_P^n)=8Q-12,\qquad
\operatorname{rank}_{\mathbb Q}(T_P^n)=Q^3-8Q+12.}
\]
Indeed over the splitting field Q(zeta), discrete character diagonalization has eigenvalues lambda_{ijk}; powering does not change which of these are zero. Scalar extension preserves rank. Consequently ker(T_P^n)=ker(T_P) and im(T_P^n)=im(T_P) as rational subspaces for all positive n. This stable linear image is a property of the terminal positive BRC convolution operator; it does not supply a future-event licence or imply a safe reduction of native signed provenance.

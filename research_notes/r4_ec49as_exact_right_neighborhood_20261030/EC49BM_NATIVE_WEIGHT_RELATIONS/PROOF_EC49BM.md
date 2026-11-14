# EC49BM — Full-S6 weight relations and minimal native-X6 weighted BRC observer

2026-10-30. AUTHOR_ANALYTIC_PROOF / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. This proof uses the original native X6 signed-axis path type, and a **declared per-witness positive-rational product** derived from the actual native aggregate endpoint_weight. It is not a claim about signed/complex amplitude or physical heartbeat time.

Frozen sources: GLOBAL_KNOWLEDGE_V1 main db4d8c81b273b670c9fc6ab09ce258aa9cdca611; Enterprise Math main 483f2688c7accbb66f43f6042e11ea15be96c1d0; native experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176; predecessor PR #1730 head a86606df5dca84196d8757746cd764a8a0e84827. P000 V5 and ACTIVE worldview, X6+typed time, joint-observer preservation and current portable research protocol are retained.

## Exact observation language

Let A={+E_i,-E_i:1<=i<=6}. An ordered word t in A* starts at a typed X6 Cell P, has length n and signed chart-relative displacement d in Z^6. Native paths may contain loops; P is an affine Cell anchor, not a universal ontic origin. For fixed twelve positive rationals w_i+,w_i-, define per-word chi_w(t)=product of w_s over letters s in t. The existing native Python function endpoint_weight(n,d,w+,w-) is SUM of these products over all compatible words: a bridge from native BRC, not an existing per-witness API.

The fixed-frame instrument convention is essential: S6 relabels letters of the path while the twelve-entry table w stays fixed. Inverse sends (s_1,...,s_n) to (-s_n,...,-s_1). Future contexts are any finite *one-hole* word construction using composable concatenation with specified words, inverse and S6, followed by an observer Q_{r,w} returning source/endpoint Cell, n, first min(r,n) letters and chi_w. The observer and future-operation scope are explicitly limited; a simultaneous relabeling of both word and weight table is a separate problem. Define p_r(t),s_r(t) as ordered first/last r labels.

## Theorem A — multiplicative relation lattice

Let P_w be the finite set of primes appearing in the weight numerators or denominators. Define the integer prime-valuation homomorphism V:Z^12 -> Z^{P_w} by V(h)=sum_i h_i+ v(w_i+) + h_i- v(w_i-). Let G=S6 x C2 act by axis permutation and global +/− interchange. Let L=ker_Z V and L_G=intersection over g in G of g^{-1}L.

For words with the same source, n, d, p_r and s_r, equality of all future Q observations is **equivalent** to h(t)-h(u) in L_G, where h is the 12-entry signed-occurrence histogram. Thus the reachable part of Z^12/L_G is the minimal exact *weight-derived* future residual, in addition to the native two-ended registers.

Proof: unique factorization of positive rationals yields chi equality iff the valuation difference belongs to L. Every allowed one-hole context transforms a histogram into g h+c for known c and g in G: concatenation adds histograms, inverse swaps signs and permutations relabel coordinates. Comparing two outputs cancels c, so all future products agree iff V(g(h-h'))=0 for every g. This is necessary by the contexts consisting of g alone and sufficient by induction on contextual constructions. Native source/n/d and boundary comparisons descend; identity observes unequal prefixes, and inverse observes unequal suffixes. Therefore no two inequivalent classes can be merged while preserving the declared observer. QED.

## Theorem B — sharp all-rational dichotomy on every fixed n,d fiber

Put a_i=max(d_i,0), b_i=max(-d_i,0), K=(n-sum_i |d_i|)/2. A fiber is feasible exactly when K is a nonnegative integer. Every compatible histogram has form
h(k)=(a_1+k_1,...,a_6+k_6; b_1+k_1,...,b_6+k_6), k_i>=0, sum_i k_i=K.
Define inverse-pair loop products q_i=w_i+ w_i-.

**Case 1: q_1=...=q_6.** The minimal future observer state is exactly (P,n,d,p_r,s_r), with no weighted occurrence-count residual.

**Case 2: at least two q_i differ.** The exact minimal future observer state is (P,n,d,p_r,s_r,h). Even multiplicatively dependent q_i recover the entire hist under all fixed-table S6 future observations.

Proof: chi_w(t)=B(d)*product_i q_i^{k_i}, where B(d)=product_i (w_i+)^{a_i}(w_i-)^{b_i}. Given two words with equal n,d, write z_i=k_i-k'_i, so sum_i z_i=0. Under sigma in S6, their normalized product ratio is product_i q_{sigma(i)}^{z_i}. In the equal-q case this ratio is q^{sum z_i}=1 under every permutation and inverse, giving Case 1 by Theorem A. Otherwise choose distinct target labels a,b with q_a != q_b. For any original i != j, choose sigma sending i to a and j to b, and tau identical except for swapping those two target labels. If all future outputs agree, divide the two equal-to-one ratios to obtain (q_a/q_b)^{z_i-z_j}=1. A positive rational unequal to one has no nonzero integer power equal to one; hence z_i=z_j for every i,j. Their sum is zero, so z=0 and h=h'. This proves Case 2 and exact minimality. QED.

The quotient can be stated as the **precise lattice identity**: W={z in Z^6:sum z_i=0}, b_i=v(q_i); C={z in W:sum_i z_i b_{sigma(i)}=0 for all sigma in S6}. Then C=W if all q_i equal, and C={0} otherwise. This is a strict observer-scope result, not permission to delete histories for arbitrary later operations.

## Corollaries and reconstruction

When q_a != q_b, choose one reference axis 1 and each j=2,...,6. For every j use two permutations swapping which of axes 1,j maps to target labels a,b. Divide measured products by the known displacement baseline B_sigma(d) and take the ratio. It is exactly (q_a/q_b)^{k_j-k_1}; the exponent is unique. Five exponent differences and sum k_i=K reconstruct all six k_i. Thus at most **ten** exact fixed-table S6 weight readouts recover the full hist for any n,d. This counts observations, not bits, cost or physical experiments.

For n<2r the two boundary windows cover every letter; number of classes equals native N_n(d). For n>=2r, in Case 1 classes equal the number of feasible prefix/suffix pairs:
sum_{p,s in A^r} 1[N_{n-2r}(d-delta(p)-delta(s))>0].
In Case 2 classes equal:
sum_{sum k_i=K} sum_{p,s in A^r} 1[c(p)+c(s) <= h(k) componentwise].
The middle-word count criterion proves these complete formulas. At d=0,n=4,r=1, native N_4(0)=396 words, 21 loop-count profiles, and the two cases yield respectively **144** and **204** future-observer classes. At d=0,n=6,r=1 Case 2 yields 1044 (the EC49BL finite example); Case 1 yields 144.

## Exact minimal counterexample and operation-sensitive witness

Let u=(+E1,+E2,-E2,-E1), v=(+E1,+E3,-E3,-E1). Both are legitimate length-four return paths at the same source Cell with the same first and last steps, but different hist. No shorter witness with r=1 has these properties: at lengths <=3, the known end letters, length and displacement determine the at-most-one interior letter.

For p=(3,5,7,11,13,17), set w_i+=p_i, w_i-=2/p_i. All twelve weights are pairwise distinct and positive rational, while all q_i=2. Both paths have chi=4, and every allowed future context gives identical outputs. This is a strict residual compression despite twelve different non-unit weights.

Conversely, set w_i+=w_i-=2 for axes i=1,...,5 and w_6+=w_6-=3. Now q=(4,4,4,4,4,9). Both u,v initially give chi=16, but after the word-only transposition E3<->E6, chi(u)=16 and chi(v)=36. Thus a single current product may fail to preserve a future-readout distinction.

## Actual executed exact test and boundaries

A pinned native signed_brc.py copy with Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176 was imported. Python Fraction checker executed twice, yielding byte-identical JSON. It enumerated every one of 396 length-four signed X6 return words, all 21 histograms and 720 permutations for each histogram, proved the finite 144/204 counts, checked 105 ratio identities for ten-query reconstruction, both rational witnesses, and verified endpoint_weight aggregate values 1584 (equal q) and 9126 (unequal q). File EXACT_REPORT_EC49BM.json records the exact computation. Full real/unbounded statements above follow algebraically, not by extrapolating the finite run.

The formal native Source authority is separate from these portable author proofs. There is no native session/CLAIM/Result or independent Driver review admission implied by this PR material. Next EC49BN: identify an intermediate relation lattice for a **proper** allowed permutation subgroup or covariant instrument weight transport, and compare single-word and true aggregate endpoint_weight observers.
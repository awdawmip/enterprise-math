# EC49BL — exact weighted-BRC interior witness and the minimal histogram-augmented future observer

Date 2026-10-30. Status: AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_WEIGHTED_BRC_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Frozen sources and exact type

Reuse EC49BK's fixed GLOBAL_KNOWLEDGE_V1 main@104a8e9dabd6198aeb9994305ea4fd4f4eea0d12, Enterprise Math main@7a590c60e49a420b88518fec60818ac3b70a4b7d, P000 V5, ACTIVE world/residual constraints and project portable research protocol. Actual native signed X6 N-BRC and positive-rational Weighted-BRC kernel: experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py, Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176. Previous author-only EC49BK theorem is in adjacent EC49BK_NATIVE_X6 folder at PR #1730.

Let A be the 12 signed-native primitive X6 axis letters ±E_i. A witness is one *ordered* word from an actual Cell with exact length n and six-component signed displacement d. Declared path-algebra operations: Cell-composable concatenation, algebraic inverse I(t)=(-t_n,...,-t_1), and S6 axis-permutation skeleton. Existing native endpoint_weight(n,d,wplus,wminus) is the sum of ordered per-witness weight products at that fixed endpoint/length. For this research *define and type* a stronger **per-witness** positive-rational port chi_w(t)=product over signed letters s in t of the corresponding strictly positive rational weight w_s. The source kernel's multinomial formula proves the bridge:
endpoint_weight(n,d,wplus,wminus) = sum_{|t|=n, delta(t)=d} chi_w(t).
The right-side per-witness port is a declared path-formal extension derived from the source kernel, not an existing native per-witness Python API. Positive rational weights do not represent native signed/complex amplitudes or heartbeat evolution.

## Theorem 1: same EC49BK two-ended residual, different legal BRC witness score

Freeze twelve **distinct prime** weights for signed labels: positive +E1..+E6 weights (2,5,11,17,23,31) and negative -E1..-E6 weights (3,7,13,19,29,37). Take
u=(+1,+2,-2,+3,-3,-1),
v=(+1,+2,-2,+2,-2,-1).
Both length six from the same native Cell; both exact endpoint d=0, same first letter +1 and last letter -1. Thus both have the same full EC49BK S_1=(P,n,d,first,last). They differ in hidden interior signed-axis loop occupancy. Their exact positive-rational witness scores are
chi_w(u)=2*5*7*11*13*3=30030,
chi_w(v)=2*5*7*5*7*3=7350.
Their *aggregate endpoint_weight* readout is identical because it is a function of common n,d, not of the individual selected word. Hence the declared per-witness weighted port does **not factor through S_1**. This is an exact native-signed-X6 type-preserving information-loss counterexample.

## Theorem 2: exact minimal future weighted quotient, under prime-weight hypothesis

Let h(t) be the complete 12-entry signed-label **occurrence histogram** (n_i^+ for i=1..6, then n_i^-). Fix r>=0. Strengthen EC49BK observer to Q_{r,w}(t), returning source and endpoint Cell, exact n, first up-to-r primitive letters, and chi_w(t). Future contexts are all finite typed compositions of signed-word concatenation, algebraic signed inverse and S6 axis permutation, followed by Q_{r,w}. Define T_r(t)=(P,n,d,p_r(t),s_r(t),h(t)), the previous two-ended EC49BK summary augmented by h.

Claim: for these *twelve pairwise distinct primes*, equality of T_r is **equivalent** to indistinguishability by all declared weighted future contexts; T_r is therefore the exact **minimal equivalence relation** for this declared future language.

Proof: Under concatenation, h(tu)=h(t)+h(u); under signed inverse the six + counts exchange with the six - counts; under axis permutation the coordinates relabel. The EC49BK proof supplies exact updates of p_r and s_r under all these operations. Thus the whole T state is compositional, and chi_w(t)=product_s w_s^{h_s(t)} is a function of T. Induction on context establishes sufficiency. Conversely, immediate Q_{r,w} sees p_r and the positive integer chi_w. Unique prime factorization gives **all twelve** histogram entries from that one product. One algebraic-inverse context reveals s_r as the first-r signed inverse. Hence distinct T states are already distinguishable by the identity or single-inverse Q contexts; the quotient cannot be coarsened. QED. The number twelve is not a claim that twelve *machine registers* are necessary: the product integer encodes the histogram for this chosen prime assignment. For weights that are multiplicatively dependent this minimality can fail; no universal claim is made for arbitrary rational weights.

## Theorem 3: general exact signed-BRC weighted class formula

Fix a feasible native signed X6 displacement d and length n. Put a_i=max(d_i,0), b_i=max(-d_i,0), K=(n-||d||_1)/2 in nonnegative integers. Then every compatible hist is uniquely
h(k)=(a_1+k_1,...,a_6+k_6,b_1+k_1,...,b_6+k_6),
where k_i>=0 and sum_i k_i=K. There are exactly C(K+5,5) possible histograms, one per weak composition, and under the distinct-prime weights they give different chi_w values by unique prime factorization. Within each histogram, number of native BRC ordered witnesses equals
n! / product_i ((a_i+k_i)!(b_i+k_i)!).
These factors sum to the native signed endpoint_multiplicity(n,d); multiplying each by product_i (w_i^+)^{a_i+k_i}(w_i^-)^{b_i+k_i} gives exactly the source endpoint_weight(n,d,weights). This proves the typed native correspondence.

If n<2r, the first-r and last-r word registers overlap and determine the complete witness, so weighted observer class count K^w_r(d,n)=N_n(d). If n>=2r, the complete exact class formula is
K^w_r(d,n) = sum_{k_1+...+k_6=K} sum_{p,q in A^r} 1{counts_signed_labels(p concatenated q) <= h(k) coordinatewise}.
Proof: for each chosen histogram k and exact pair (p,q), subtract their signed occurrence counts. A central word consisting of the remaining nonnegative multiset has exactly length n−2r and yields the correct displacement. Hence the pair is feasible iff these count inequalities hold. Conversely every witness selects exactly one such triple. Theorem 2 makes each feasible triple precisely one future-observer equivalence class. At r=0 this is C(K+5,5). QED.

## Corollary: a sharp finite information cost for nonshortest native returns

Take native signed d=0, n=6, r=1, K=3. Exactly C(8,5)=56 occurrence histograms exist, with k-patterns 6 of (3), 30 of (2,1), 20 of (1,1,1). For a fixed histogram with s axes supporting at least one +/− pair and t axes supporting two or more pairs, the allowed first/last ordered signed-letter pairs number H_1(k)=2s(2s−1)+2t (two distinct supported signed labels, or equal label permitted exactly for k_i>=2). Therefore
K^w_1(0,6)=6*4+30*14+20*30=1044.
The EC49BK first/last-only observer has K_1(0,6)=12^2=144, since any signed first/last pair admits a 4-step inverse-pair bridge to displacement zero. The complete source signed N-BRC length-six return fiber contains N_6(0)=19920 ordered native witnesses. Thus
144 < 1044 < 19920,
with exact conditional fixed-width information minimum ceil(log2 1044)=11 bits for this weighted two-ended quotient vs ceil(log2 144)=8 bits for the unweighted one. These are residual-state entropy *counting* bounds conditioned on P,n,d, not finite total state machines or physical energy/space/time claims.

## Executed exact audit / boundaries

The original actual Python stdlib Fraction checker was executed twice, with byte-identical output. Its exact original source is stored losslessly as VERIFY_EC49BL.py.gz.b64; decode via base64+gzip and run it beside byte-pinned native signed_brc.py. EXACT_REPORT_EC49BL.json is the original executed deterministic report (byte identical to output after the second run). It exhaustively enumerates all 19,920 native signed-X6 return witnesses length six via all 56 histogram classes; checks native endpoint_weight(6,0)=859634035540, endpoint_multiplicity(6,0)=19920, histogram classes 56, weighted two-ended classes 1044, unweighted classes144, the explicit 30030/7350 pair, profile identity, all 7,225 short-word histogram-additivity checks and all 61,200 short-word S6 histogram relabeling checks. It pins native Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176 prior to use. The general quantified mathematical claims are the analytic combinatorial proofs above; finite code is not treated as infinite proof.

This is an author-side *portable* mathematical result awaiting independent review/CLAIM/Result if and when native authority permits. No modified P000/ACTIVE worldview; no claim of signed complex phase, heartbeat physical time reversal, triadic forces, or a native physical mechanism. Next EC49BM: characterize the true minimal future-weight observer quotient for general positive-rational weights with multiplicative dependencies, under inverse and S6 (and, separately, distinguish port-local weight from endpoint aggregate).
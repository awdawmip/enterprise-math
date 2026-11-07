# EC49BK — Exact two-ended residual for native signed-X6 path-formal BRC

Date: 2026-10-30. Status: AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_BRC_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Verified frozen input and exact type

GLOBAL_KNOWLEDGE_V1 main@104a8e9dabd6198aeb9994305ea4fd4f4eea0d12; Enterprise Math main@7a590c60e49a420b88518fec60818ac3b70a4b7d. P000 V5, ACTIVE residual-provenance worldview, signed X6 Cell torsor, signed-X6 path-formal/N-BRC, current portable research protocol. Predecessor author-side EC49BJ: existing PR #1730 head 71b21236670da3ab7b3471883997fa86561d0f0f at input freeze. This note does not confer a canonical CLAIM.

Let A={+E_i,-E_i | 1<=i<=6}, a 12-letter primitive signed-X6 alphabet. Let w in A* be an exact *ordered* path witness from a real Cell P, with length n and chart-relative displacement delta(w) in Z^6. P has no intrinsically distinguished coordinate zero. We allow: (i) Cell-composable ordered word concatenation, including inverse pairs and loops, (ii) algebraic signed-word inverse I(w)=(-w_n,...,-w_1), (iii) only the established axis-label permutation skeleton S6, acting consistently on the Cell chart, displacements and labels. These are declared path-formal operations, not an assertion of heartbeat physical time reversal or a full native rotation group.

Fix integer r>=0. The observer R_r returns exact source and endpoint Cell, length and the first min(r,n) ordered signed labels. A *future context* is any finite well-typed expression made by concatenation with other path words, I, and S6 transformations, followed by R_r. It may not inspect arbitrary internal substrings, per-witness weights, phases or other unavailable fields. Define p_r(w) as the first min(r,n) labels and s_r(w) as the last min(r,n) labels, and the summary
S_r(w)=(P,n,delta(w),p_r(w),s_r(w)).
Two summary lengths/endpoint displacements are compared only within their exact typed source and chosen chart.

## Theorem 1 — exact compositional sufficiency and minimality

For any u,v with equal source, length and displacement, all admissible future-context R_r observations on u and v agree **if and only if** p_r(u)=p_r(v) AND s_r(u)=s_r(v).

Proof. For concatenable x,y, both boundary registers satisfy exact identities
p_r(xy)=head_r(p_r(x)p_r(y)),
s_r(xy)=tail_r(s_r(x)s_r(y)).
For the algebraic inverse,
delta(Ix)=-delta(x), source(Ix)=endpoint(x),
p_r(Ix)=I(s_r(x)), s_r(Ix)=I(p_r(x)).
S6 relabels the Cell frame, displacement and registers componentwise. Length and displacement update additively under concatenation, and Cell composability depends only on endpoint/source. Thus every allowed operation descends to a deterministic operation on S_r. Structural induction on any finite context gives sufficiency even if paths contain nonshortest loops. Necessity: identity-context R_r detects a different p_r immediately; one inverse-context R_r detects a different s_r because inverse/reverse/sign is injective. Hence the summary equivalence classes coincide exactly with future observational indistinguishability, so no strictly coarser quotient can preserve this declared family. This is a *relative* minimality theorem, not a universal license to erase native path provenance. QED.

## Theorem 2 — no fixed suffix-only register is sufficient

For any k>=0 let a=+E1, b=+E2 and define u=a b a^k, v=b a a^k. They are distinct **shortest** signed-X6 witnesses from the same Cell to displacement (k+1,1,0,0,0,0), both length k+2. The source native shortest N-BRC multiplicity is k+2. Their last k ordered labels, terminal Cell, length and endpoint multiplicity all agree, but first step a vs b differs. Direct R_1 (or after I^2) separates them. For k>=1, one inverse alone does *not* separate them at its first step, which is the common -a: the direct/two-inverse observation is the correct witness. Thus fixed suffix-only state is inadequate for this declared future readout, while the fixed *two-ended* r-boundaries are sufficient by Theorem 1. Exact source Cell and unbounded n/d remain outside the bounded boundary residual.

## Theorem 3 — exact class-count formula via actual signed-X6 BRC

Let N_M(z) be the *native signed-X6 N-BRC endpoint multiplicity*, as implemented by source-specified signed_brc.endpoint_multiplicity(M,z), extended to M<0 by zero. Feasibility is
N_M(z)>0 iff M>=||z||_1 and M-||z||_1 is even.
The forward direction follows by counting the needed signed axis steps plus opposite pairs; conversely fill shortest signed native steps then insert the required number of (+E1,-E1) pairs. This is a signed combinatorial support statement, not a positive-probability/complex-phase identification.

On the fixed feasible fiber W(P,d,n), the number of distinct S_r-equivalence classes is
K_r(d,n)=N_n(d) if n<2r;
K_r(d,n)=sum_{p,q in A^r} 1[N_{n-2r}(d-delta(p)-delta(q))>0] if n>=2r.
For n<2r, prefix and suffix overlap and determine the entire n-word, giving N_n(d) classes. For n>=2r, every pair of length-r boundary words is either feasible with a central length n-2r bridge with displacement d-delta(p)-delta(q), or infeasible; distinct feasible pairs are distinct observer classes by Theorem 1. This proves the formula for arbitrary signed displacements, loops and all nonnegative r.

For every r>=1, d=0,n=4r, *all* 12^(2r) pairs p,q are feasible. Their combined displacement b has ||b||_1<=2r and parity congruent 2r. A length-2r center of displacement -b exists by taking required signed steps and adding cancelling inverse pairs. Therefore sharp K_r(0,4r)=12^(2r) and minimum fixed-width residual bits on this fixed endpoint/length fiber equal ceil(2r log2 12). For r=1: 144 classes, 8 bits, while source N_4(0)=396. For r=2: 20736 classes, 15 bits, while source N_8(0)=1281420. Because endpoint and exact path length are unbounded types, this is not a finite total machine theorem.

## Theorem 4 — shortest-path bilateral count

For shortest displacement d, let m_i=|d_i|, n=sum m_i; then B_min=n!/prod m_i! (native signed-X6 N-BRC). If n<2r then K_r^min=B_min. If n>=2r,
K_r^min(d)= sum over 0<=a_i,b_i, sum_i a_i=sum_i b_i=r, a_i+b_i<=m_i of (r!/prod_i a_i!)(r!/prod_i b_i!).
Proof: each realizable prefix/suffix consists only of the signed native steps required by d. Its ordered choices with prescribed count-vectors a,b are respectively the multinomial factors; the remaining steps exist exactly when a_i+b_i<=m_i for all i. No double counting occurs because the boundary count-vectors and word orders are uniquely read from a boundary pair. At r=1 and n>=2, with s=# {i:m_i>0}, K_1^min=s(s-1)+# {i:m_i>=2}. For d=(2,-1,1,0,0,0), n=4, B_min=12, K_1^min=7; the EC49BJ one-sided reverse-first class count was 3. QED.

## Exact executed computational evidence and boundaries

The executed Python standard-library verification source is provided losslessly as VERIFY_EC49BK.py.gz.b64, decoded by base64 and gzip, with original source pin native signed_brc.py git blob 300a96e3dc24bf6fff73743037a0347a8bc83176 (at the pinned project main path experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py). The checker actually ran twice and produced byte-identical EXACT_REPORT_EC49BK.json. It checks all 85 signed two-axis words of length at most 3; 4 times 7225 concatenation pairs; inverse identities; 720 S6 permutations across three r values (183600 checks); 13 shortest-path suffix-only witnesses (k=0,...,12); every 12^(2r) boundary pair for r=1,2; native signed BRC return multiplicities; shortest bilateral counts for five exact six-dimensional displacements and r=0..3. This finite audit is evidence of implementation/examples; general quantifiers in the theorems are established by the proofs above, *not* by finite extrapolation.

Verification execution: decompress the Python source in a working directory next to a local copy of the immutable source-specified signed_brc.py (or in the project checkout at the documented native path), run python VERIFY_EC49BK.py and compare EXACT_REPORT_EC49BK.json to the committed report. The script checks the source Git blob before scientific calls and uses actual N-BRC functions. Branch-provenance scope excludes per-path positive-rational weight readout, signed/complex amplitudes, heartbeat time dynamics, triadic balance, arbitrary unseen readouts and physical claims. Source and author identity remain shared with prior research; an independent reviewer has not accepted this result.

Next problem EC49BL: extend the future observer by an actual *per-witness* positive-rational Weighted-BRC score, identify the additional internal signed-occurrence histogram or generating-function residual required to preserve weighted concatenation/inverse/S6. Aggregate endpoint_weight is an *aggregate of all witness words* and must not be substituted for a per-witness port.
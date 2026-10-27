# R1/N14: penultimate LR-call obstruction and N=3 unique coarsest observer quotient

Date: 2026-10-27. AUTHOR MATHEMATICAL PROOF, plus executed exact rational certificate; independent Driver review, Lean checker and X6/P000 native mapping remain pending.

## Frozen input, scope and authority

Account source: GLOBAL_KNOWLEDGE_V1 main b93af5fa5d1f56cff9a63f730c86247619d79b86, with P000 V4, ACTIVE residual-fidelity worldview and TASK_RESEARCH entry. Enterprise Math scientific source: main 65e362f6cbeb4ba06971cc3f166dbbda52a90f26; protocol docs/PORTABLE_RESEARCH_PROTOCOL.md; previous frontier research_notes/r1_n14_brc_observer_only_n2_sharp_20261027_r1/PROOF.md and NEXT_TASK.md. GitHub login awdawmip has push permission. Current native tasks read returned CONTROL_QUOTA, and native session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Registered local author activity RA-R1-20261027-0958-OBSERVER-R11 is not a native CLAIM or independent review.

This is an EXTERNAL finite positive two-probability-law model. The BRC reuse is faithful rational ordered path-flow and retention of future-relevant branch residual; not typed native Heartbeat/BRC-Shor arithmetic, signed-phase cancellation, a 6D Cell theorem or external physical evidence.

Observer is precisely the binary terminal pair (T,D), not the full quotient state. For every original complete-history randomized stopping/decision policy we require existence of ONE compressed policy under both P and Q. The compressed state is a time-typed deterministic labelled right congruence, and its randomized decisions depend only on the current state and a fresh coin; no persistent hidden selector.

## Theorem 1: general penultimate predictive-LR necessity

Let N>=2, and H be all strictly positive histories at time N−1. Assume P(h)=Q(h)=w_h>0 for every h in H. At the last step assume a finite alphabet A with positive conditional probabilities and positive constants r_a independent of h, with Q(a|h)=r_a P(a|h) and both rows normalized. Define

C_h(lambda) = sum_{a in A} P(a|h) max(r_a-lambda, 0),    lambda>0.

If a time-typed recursive quotient z preserves the two laws of (T,D) for EVERY original full-history randomized stopping/decision policy, then

z_{N−1}(h)=z_{N−1}(g)  implies  C_h(lambda)=C_g(lambda) for all lambda>0.

Equivalently, merged penultimate histories must have the same P-conditional probability histogram of the final-step likelihood-ratio value r_a. The theorem is necessary only; it is not a general all-N sufficient observer-only criterion.

### Proof (universal real-parameter separator)

Suppose merged h,g have distinct C values at some lambda>0. Choose a real theta strictly between their values, avoiding the finite set of all C_k(lambda). Let S={k:C_k(lambda)>theta}. A full policy is forced to continue through time N−1, then continues iff k is in S; those stopping at N−1 decide D=0. At time N it decides D=1 iff r_a>lambda.

This policy has P(T=N)=Q(T=N)=m=sum_{k in S}w_k. Its terminal contrast

J_full=Q(T=N,D=1)-lambda P(T=N,D=1)
      =sum_{k in S}w_k C_k(lambda)
      =theta*m+sum_{C_k>theta}w_k(C_k-theta).

A compressed policy matching both terminal laws cannot stop before N−1 because the target has zero earlier stopping probability and every prefix has strictly positive mass. Let c_k be its probability to continue at N−1. Then sum_k w_k c_k=m, with c_h=c_g=c on the merged state. Even granting the compressed policy arbitrary full-history information at its final D decision, its contrast cannot exceed

J_comp <= sum_k w_k c_k C_k(lambda)
        =theta*m+sum_k w_k c_k(C_k-theta).

Name h,g so C_h>theta>C_g. The loss compared to J_full is at least

w_h(C_h-theta)(1-c) + w_g(theta-C_g)c
>= min(w_h(C_h-theta),w_g(theta-C_g)) > 0.

All other histories contribute nonnegative loss. Therefore J_comp<J_full, contradiction. This excludes the entire real randomized compressed strategy class, not a finite grid. QED.

For the equivalence, let R be the finite set of distinct r values and let b_h(r)=sum_{a:r_a=r}P(a|h). Then C_h(lambda)=sum_{r in R} b_h(r)(r-lambda)_+. Each knot lambda=r has a downward-slope jump b_h(r), so the function for all positive lambda determines the entire b_h histogram.

Independent terminal-state necessity: if two terminal histories have distinct Q/P cylinder ratios and share a quotient state, force continuation to N and choose D=1 exactly where Q/P>lambda for a threshold between these ratios. The complete-history contrast attains sum_h [Q(h)-lambda P(h)]_+, while a common quotient-state decision loses strictly on any fiber containing terms of both signs. Hence every universally sufficient quotient refines the terminal likelihood-ratio classes.

## Theorem 2: strictly positive N=3 instance, unique greatest quotient of 10 states

Let observations I,K,J each take values in {0,1,2}. Under both laws the first observation I and the second observation K are uniform, so P(i,k)=Q(i,k)=1/9. Final P(J=j|i,k) depends on i but not k:

| first i | j=0 | j=1 | j=2 |
|---|---:|---:|---:|
| 0 | 1/4 | 1/4 | 1/2 |
| 1 | 1/12 | 3/4 | 1/6 |
| 2 | 1/6 | 1/2 | 1/3 |

Take (r_0,r_1,r_2)=(2,1,1/2) and Q(J=j|i,k)=r_j P(J=j|i,k). Q rows are respectively (1/2,1/4,1/4), (1/6,3/4,1/12), (1/3,1/2,1/6), each normalized and positive. All 40 ordered prefixes have positive probability. The cylinder likelihood ratio is 1 until depth 2, then r_j at depth 3.

With lambda=1, C_(0,k)=1/4, C_(2,k)=1/6, C_(1,k)=1/12. Theorem 1 forces every universally sufficient quotient to separate all time-2 histories with distinct first symbols i, regardless of second symbol k. Therefore |Z_2|>=3. Its deterministic labelled update implies |Z_1|>=3: if first histories i!=i' were merged, appending the same k would produce a forbidden merged time-2 pair. The separate terminal LR argument requires |Z_3|>=3 for r values 2,1,1/2. There is one root state, so total >=1+3+3+3=10.

Two explicit full-policy witnesses quantify the forced splits. With threshold theta=5/24, continue at time 2 exactly for first i=0, then decide D=1 exactly if J=0. This gives m=P(T=3)=Q(T=3)=1/3; P(T=3,D=1)=1/12, Q(T=3,D=1)=1/6, contrast 1/12. With theta=1/8, continue for i in {0,2}, giving m=2/3, P(T=3,D=1)=5/36, Q(T=3,D=1)=5/18, contrast 5/36. All else stops with D=0. For any same-state pair of depth-2 histories with distinct first i, one of these two theta values separates them. Each has P-prefix weight 1/9. The strict pair-loss lower bound is at least 1/216 for matching the witness's stopping mass and two-law terminal contrast. This applies to all real randomization parameters and to all 27 cross-first-type history pairs.

Attaining quotient, with states time tagged:
- z_0=root, 1 state;
- z_1(i)=i, 3 states;
- z_2(i,k)=i, 3 states (discard k);
- z_3(i,k,j)=j, 3 states (discard i,k).

It is a deterministic labelled right congruence. Every fiber has constant Q/P ratio. It is strongly lumpable under both laws: the time-2 terminal kernel for a fixed i is independent of the discarded k, while earlier kernels are uniform/trivial. Thus it is sufficient for all policies, not just two witnesses. Directly, keep all root and time-1 actions; at time 2 average the full stop/continue and D decision masses over surviving k within each i. Both laws have identical prefix masses through time 2, so the averaged common actions preserve both survival/stop flows. As the P final row depends on i only, the resulting arrival mass to final j matches full P; Q mass equals r_j times P in either implementation. At time 3 choose the P-arrival-weighted mean of full D=1 probabilities within each j. Since all paths ending at that j share ratio r_j, the same mean matches Q. Zero-arrival cases are immaterial. A randomized root stopping action, if allowed, is copied identically.

Hence the minimum profile is exactly (1,3,3,3), total 10. More strongly, the necessity argument shows that EVERY observer-sufficient recursive quotient refines this constructed quotient at each depth. It is itself sufficient, so the quotient is the unique greatest/coarsest sufficient right congruence, up to state labels, for THIS model.

This N=3 model is deliberately a delayed lift of the predecessor's N=2 ternary experiment by adding an independent uniform observation K. It gives an N=3 restricted-class uniqueness and quantitative obstruction, NOT a general N>=3 uniqueness theorem or a proof that incomparable minimal quotients never exist.

## Executed verification, source context, limits

VERIFY.py uses Python fractions.Fraction, no floating approximations. It verifies all 1+3+9+27=40 positive prefixes, both-law normalization and prefix conservation, LR-fiber constancy, both-law quotient transition lumpability, both full-policy witness laws and 27 pairwise exact loss bounds. RESULT.json is the actual stdout. The universal all-policy statements are the mathematical proofs above; the program checks this finite model and specified witness family, not every real randomized strategy.

Related general background, not a citation for this exact theorem: Geiger & Temmel, "Lumpings of Markov chains, entropy rate preservation, and higher-order lumpability", arXiv:1212.4375 (2012); Baier, Katoen, Hermanns & Wolf, "Comparative branching-time semantics for Markov chains", Information and Computation 200 (2005). No comprehensive literature novelty review was made.

Open: general N>=3 with nontrivial earlier P/Q history ratios; possible incomparable observer-only quotients; independent Driver review; Lean proof; source-native CLAIM/Result; full P000 native six-axis Cell embedding/readout/transition preservation. See NEXT_TASK.md.

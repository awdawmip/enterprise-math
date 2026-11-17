# R762DB — Adaptive sparse Port probes and exact positive BRC seed budgets

Date: 2026-11-17. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS (publication TP2-8B7E13C5904A2D6F1142). Scientific researcher identity EM-X6-3050F6, original SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Independent review: NOT_REVIEWED.

## Exact frozen scientific provenance

- Taskbook: awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md (Git blob 218bf9ce05fd2dd79f477ac269fc3590f83f482e).
- P000 V5 scientific pin from taskbook: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json; signed six-dimensional native Cell torsor, PERP_E and native 120-degree right-angle definition, three-force minimum stable arity remain intact.
- R762DA: research_notes/portable_direct/R762DA_SPARSE_PORT_SAMPLING_THEOREM.md, immutable PR #2635 commit 7316b407ca28709ad8322bc6a519d55a2a024691. Its fixed nonadaptive sparse schedule theorem is used as an exact predecessor.

This paper concerns a *conditional finite-group, positive named-microbranch N-BRC path carrier*. The group is not a spatial coordinate, the probability is not signed force cancellation, and the candidate time steps are not asserted to be native heartbeats or legal TRIADIC_CLOSURE_E events.

## Observer and branch definitions

Let G be any finite (possibly noncommutative) group with identity e. Let A be a nonempty finite *list of individually named microbranches*, each having one right-multiplication increment a in G; repetitions are distinct named alternatives. Set D=|A|. Initially X_0=e. The BRC count C_n(g) is the number of n-step named branch words whose ordered product is g. In particular C_0(e)=1, C_0(g!=e)=0, sum_g C_n(g)=D^n, and C_{m+n}(z)=sum_y C_m(y)C_n(y^{-1}z).

Fix H>=1. A deterministic adaptive probe protocol takes the previously observed record ((t_1,x_1),...,(t_j,x_j)), and either asks for a strictly later t_{j+1}<=H or terminates. No time choice may depend on a yet-unobserved state or future microbranch. The observed result is the complete *leaf record*, including times and their values. Each complete H-step named branch word yields exactly one leaf record.

An M-equiprobable-seed realization assigns one genuine complete H-step named microbranch word to each of M equally probable initial seeds, with no future random input, and exactly reproduces the leaf-record law. Multiple seeds may map to the same word. It is a one-shot probability representation, not a state-machine or all-future semantic equivalence certificate.

## Theorem A — optimal adaptive leaf information

For each attainable leaf L=((t_1,x_1),...,(t_k,x_k)), put t_0=0, x_0=e and define the *integer* full-horizon BRC word count

\[
 N_L = D^{H-t_k}\prod_{j=1}^{k}C_{t_j-t_{j-1}}(x_{j-1}^{-1}x_j).
\]

For the zero-query leaf use N_L=D^H. Write g_T=gcd_L N_L, with zero-count impossible leaves harmless. Then

\[
 \boxed{M_{\min}(T)=D^H/g_T.}
\]

This holds for every finite G, any named-branch multiplicities, and any finite deterministic adapted query tree.

**Proof.** Given an observed leaf, each time interval has precisely C_{t_j-t_{j-1}}(x_{j-1}^{-1}x_j) named-branch words. For each such interval word, the deterministic query policy makes the same successive query decisions, since those decisions depend only on the listed previous observations. The unobserved suffix after t_k has exactly D^{H-t_k} possible words. Thus N_L counts the full-horizon words mapping to L, and the leaves partition all D^H words. Consequently their exact event probabilities are N_L/D^H and sum to one.

Any M-equiprobable-seed deterministic realization requires M*N_L/D^H to be an integer for every L. The least positive M meeting this condition is D^H/g_T, by prime valuations of the joint reduced denominators. Conversely, allocate N_L/g_T seeds to each attainable leaf L and choose any actual complete H-step microbranch word yielding that leaf for each allocated seed. Every number is an integer, and the total allocation is D^H/g_T. This construction attains the bound. QED.

**Exact method.** Compute C_0,...,C_H by named-branch positive convolution. Traverse the reachable query tree, multiply interval coefficients, multiply by the suffix factor at termination, and take the gcd of leaf counts. The mathematical algorithm avoids full D^H-word enumeration; the attached author checker deliberately enumerates full words to independently test it.

## Theorem B — refinement, time extension and recovery of R762DA

If T' refines T (the T record is a deterministic function of the T' leaf), then

\[
 \boxed{M_{\min}(T)\mid M_{\min}(T')}.
\]

Indeed every coarse leaf count is the sum of the counts of its fine constituent leaves, so the fine common numerator gcd divides the coarse gcd. Extending H while adding no queries multiplies every N_L and D^H by the same power of D and leaves M_min invariant.

For one *fixed* schedule 1<=t_1<...<t_k=s, the map from sampled group states to successive group increments is bijective. The increment variables independently range across G, so the leaf gcd factorizes:

\[
 g_T=D^{H-s}\prod_{j=1}^k g_{t_j-t_{j-1}},\quad
 g_d=\gcd_{z\in G}C_d(z).
\]

Theorem A therefore specializes to the exact R762DA fixed-schedule product-of-gap-gcd formula. In the adaptive case different leaves can use different gap lengths, and the leaf set is not a Cartesian product, so a single product-of-gap-gcd factorization is generally invalid.

## Theorem C — sharp adaptive information jump (conditional C3 Port model)

Take G=C3, one named +1 microbranch, two distinct named -1 microbranches, D=3, and H=6. The positive N-BRC residue-count vectors at residues (0,1,2) include

\[
 C_2=(4,4,1),\quad C_3=(9,6,12),\quad C_5=(90,72,81).
\]

The nonadaptive observer requesting X_1 and X_6 has

\[
 M_{\mathrm{base}}=3^6/(\gcd C_1\cdot\gcd C_5)=729/9=81.
\]

Now the adaptive observer requests X_1; **if X_1=1 it additionally requests X_3**; in every case it finishes by requesting X_6. On the X_1=1 branch the nine distinct (X_3,X_6) leaves have exact full-horizon numerators C_2(u)C_3(v), whose gcd is 1*3=3. On the X_1=2 branch, only X_6 is additionally observed; the three leaf numerators are 2 C_5(v), with gcd 18. Consequently

\[
 g_{\mathrm{adaptive}}=\gcd(3,18)=3,\qquad
 \boxed{M_{\mathrm{adaptive}}=729/3=243}.
\]

Thus a conditional extra sample on only the one-third-probability first-step branch **triples** the exact seed budget, 81 -> 243. This already equals the 243-seed cost of the full fixed union schedule {1,3,6}. The three-way sampling event law is therefore stronger than the baseline two-time law even when the intermediate probe is optional.

The checker also supplies an adaptive second conditional sample example with M_min=729 in the same H=6 candidate. These claims are about an explicitly typed discrete BRC microbranch process; they require no ordinary pi or trigonometric numerical calculation.

## Exact author verification and reproducibility

Run with Python 3 standard library:

    python R762DB_VERIFY.py > R762DB_EVIDENCE.json

The checker separately computes the n-step BRC coefficient histograms and directly enumerates *named* microbranch words, runs the chosen adaptive decision policy on each full path, and compares every leaf count against Theorem A's product formula. It covers C3 p,q=1..3 and noncommutative S3 p,q=1..2, horizons H=4,5,6, and seven fixed/adaptive decision protocols, for 273 configurations. The verified local execution returned PASS with 842,926 enumerated full words and 3,313 exact leaf-count comparisons. It explicitly checks the 81/243 example, twelve adaptive leaf atoms, common numerator gcd 3, and the divisibility of the baseline budget into the refined adaptive budget. All scientific numbers are exact arbitrary-precision integers, not floating point approximations. General Theorems A and B have proofs above; this finite test is complementary.

## Native licence boundary, outcome and next test

The frozen taskbook requires an actual signed TRIADIC_CLOSURE_E Cell/Link/Port incidence and update law, with legal V17/V29/V39 rotation transport and BRC provenance. The source taskbook still lists that dynamics as unresolved. Theorem A is ready to consume an *actual* licensed native adaptive observer once the true event predicate specifies which Port values, time-labelled probes and branch/source/area residuals may be inspected. No native signed-event permission, triadic force balance, or full observer-safe quotient is inferred from the positive carrier alone.

Next discriminating unit: locate or construct and seek admission for the actual signed TRIADIC_CLOSURE_E event predicate; extract one legal state-dependent sequence of Port probes, include the R762CH/CK 15-pair oriented-area and source observables that the legal suffix can read, and apply the adaptive BRC gcd and refinement test to the resulting exact event language. An allowed observer may be weaker or stronger than the demonstration's query tree. Preserve all frozen science pins and existing verified research results.

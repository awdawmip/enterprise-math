# R762GQ — Certified second moment and variance of moving-Port absorption

Research date: 2026-11-20 (Asia/Shanghai). Research scope: frozen Task RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142, taskbook at enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8 and scientific P000 at enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Source lineage: R762GM/GN/GO/GP, especially R762GP PR #2835@49549533d24f883d91c9fc117d27c40d9b608a81. Historical contributor lineage: EM-X6-3050F6; this standalone portable result asserts no current authenticated execution identity or CLAIM. Status: author-side exact proof/check; NOT_REVIEWED.

## Exact question and candidate state

The frozen P000 fixes six signed native X6 axes, separate time, primitive triadic balance arity three, PERP_E pairwise orthogonality at native 120 degrees, and source/provenance retention. The following **constructed moving-Port STAR candidate** is not an admitted TRIADIC_CLOSURE_E event law. It uses all six signed Cell displacement coordinates and an A6 axis-permutation register, while BRC path counts preserve the four named signed event branches.

Let E=(01,02,03,12,13,23), indexed 0..5. For vertex v=0,1,2,3, let S_v be its three incident edge axes, H_v their six-component indicator, and g_v the three-cycle of those axes in the order induced by E. A complete candidate state is (x,p), with x in Z^6 and p an even permutation of six axes. The fixed initial named Port is 01. At a state (x,p) the current Port is the edge E[p(0)], and a signed letter (v,s), s in {-1,+1}, is admitted exactly when v is one of its two endpoints. Updating the state gives

  x' = x + s p H_v,    p' = p g_v^s.

Exactly four signed letters are admitted at each state. Each letter stands for an ordered three-axis native-step composite, not an additional primitive axis. Cell, rotation, named Port and signed event histories remain distinct types. For this single absorption statistic the orientation p alone determines future Port permission. Therefore projecting (x,p) to p is an exact Markov quotient for the stopping time below; it is **not** a lossless quotient for future Cell/complete-return observations.

Define the orientation absorption class A={p : E[p(0)]=23}, and let tau=min{m>=0 : p_m in A}, with p_0=id. From R762GN, A is closed under all permitted candidate events. Equally weighted BRC source words give each of the four admitted signed branches probability 1/4. This measure is an abstract positive source-counting convention, not physical force frequency.

## New theorem — exact computable variance with rigorous error bounds

For the candidate described above, tau is almost surely finite and has all positive integer moments finite. More precisely, its first and second moments and variance satisfy the certified decimal intervals

  12.93946845281426419721 < E[tau] < 12.93946845281426419722,

  263.58902488422540237226 < E[tau^2] < 263.58902488422540237227,

  96.15918104284983428470 < Var(tau) < 96.15918104284983428471.

The second moment and variance intervals are new R762GQ output; the mean agrees with the previously published R762GO mean interval.

The interval bounds are not floating-point fits: the associated verifier proves each inequality by exact integer path counts and rational comparisons at N=600. The resulting rigorously bounded tails are

  0 <= E[tau] - M_600 <= 9.003 × 10^(-27),

  0 <= E[tau^2] - Q_600 <= 1.110 × 10^(-23),

where M_N and Q_N are defined below. These rounded upper endpoints are looser than the exact rational bounds used by the checker.

## Proof

**1. Finite orientation kernel and a sharp eight-event contraction.** Enumerate the 360 even permutations p and define the four successor orientations p g_v^s, with v restricted to endpoints of E[p(0)]. A direct transition check shows the 60 orientations with E[p(0)]=23 are closed. The source-word reachability BFS from id finds 350 orientations; 290 are nonabsorbing and 60 are absorbing.

For a reachable nonabsorbing orientation i define h_0(i)=1; h_0=0 on absorbing orientations; and recursively

  h_(r+1)(i)=sum_(j in legal_successors(i)) h_r(j)

for nonabsorbing i, retaining repeated successor entries if source letters coincide. The exact enumerated maximum of h_8 over the 290 reachable nonabsorbing orientations is 39,652 out of 4^8=65,536, attained at p=(0,2,1,4,3,5). Hence the maximum eight-event survival probability is

  q = 39652/65536 = 9913/16384 < 1.

All later orientations reached from id are in the same 350-element reachable set, so for S_m=Pr(tau>m),

  S_(m+8) <= q S_m

for every m>=0. In particular tau is finite almost surely, and geometric tail domination also proves existence of every finite-order moment.

**2. Exact source recurrence.** Let n_m(i) be the number of length-m named signed source words from id that have avoided A and end at nonabsorbing orientation i. Initialize n_0(id)=1, and propagate each source word by all four admitted signed successors, discarding transitions into A. Then

  S_m = sum_i n_m(i) / 4^m.

The recurrence is entirely integral. It reproduces earlier independent checks: at m=12 exactly 6,534,252 of 4^12 words survive, and at m=16 exactly 1,118,196,052 of 4^16 survive. The supplied program generates S_0 through S_600 inclusive.

**3. Infinite moment identities.** For the positive integer tau, the finite geometric/telescoping identities yield

  E[tau] = sum_(m>=0) S_m,
  E[tau^2] = sum_(m>=0) (2m+1) S_m.

Set M_N=sum_(m=0)^(N-1) S_m and Q_N=sum_(m=0)^(N-1)(2m+1)S_m. With any j>=0 and r=0,...,7, monotonicity and the eight-step contraction give

  S_(N+8j+r) <= S_N q^j.

Summing the blocks gives the exact rational inequalities

  0 <= E[tau]-M_N <= 8 S_N/(1-q) =: a_N,

  0 <= E[tau^2]-Q_N <=
      S_N [ (16N+64)/(1-q) + 128 q/(1-q)^2 ] =: b_N.

Because the mean is nonnegative,

  Q_N - (M_N+a_N)^2 <= Var(tau)
      <= Q_N+b_N - M_N^2.

These statements hold for every positive integer N, with no asymptotic approximation.

**4. Reproducible exact certification at N=600.** The Python standard-library checker constructs E, S_v, g_v, all even permutations and all labeled signed legal arcs directly from the definition, verifies absorption closure, 350/290/60 reachability and the sharp eight-event integer maximum, then evaluates all S_m as Fraction objects. It constructs the rational bounds above and uses Fraction of each displayed decimal endpoint to assert strict containment. Therefore a PASS certifies the three numerical intervals solely within the declared finite candidate model, subject to the ordinary checker correctness obligation. No external floating-point library or randomized sampling is used. QED.

## Scientific interpretation and required next work

The exact expected waiting time and its variance quantify the **loss of return-capable orientation information** induced by a moving named Port. They separate the local 12/16-event constructive return phenomena (R762GM/GP) from long-run source-weighted survival. In this candidate, most source words are absorbed eventually even though some nonzero common-depth return paths exist. Absorption has an exact orientation-only statistic; complete affine return and provenance do not.

Next valuable native discriminator: obtain the frozen task's genuine signed TRIADIC_CLOSURE_E Cell/Port/Link/time permission and determine whether there exists an event-state map preserving the candidate orientation absorption class and its legal successors. A counterexample to that map falsifies **native transfer of this candidate hitting-time law**, not P000. Independently one can study higher moments using the same rigorously bounded survival transform or determine exact non-six-multiple minimal return length L(k).

Verification scope: exact 360-state orientation automaton and integer counts through 600 steps; all-horizon conclusions from the proved q-contraction. No full Cell-return enumeration was repeated here; all Cell/Port/Link force semantics remain at the candidate level. No new native protected Source PROGRESS, RESULT or independent REVIEW is asserted. Proposed artifact status: portable scientific branch pending canonical intake.

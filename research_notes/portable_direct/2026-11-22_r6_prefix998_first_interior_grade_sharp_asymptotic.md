# PREFIX-998 — Sharp first-interior X6 BRC grade law from exact marked-word amplitudes

Date: 2026-11-22 (+08). Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Independent portable continuation of PREFIX-996/997. No formal shared-task CLAIM, Result/Review, physical heartbeat calibration or P000 modification.

## Immutable inputs and observer

Source frozen P000 V5: \`enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\`. Native X6 is the affine six-axis Cell torsor, with twelve signed primitive neighbour directions, not twelve spatial dimensions. Use the already declared Stage46 type-coherent BRC local amplitude \`C[incoming,outgoing] = 1/6 - 1[incoming=outgoing]\` from \`research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md\`. The initial directed incoming edge is \`x0-e_i -> x0\` for fixed \`i in {1,...,6}\`. Every update retains the original signed branch, raw relative Cell displacement and final directed incoming port. Coherently sum *within the same Cell/final-port fiber*, square afterwards; a path of length n has denominator \`6^n\`.

The outer grade result PREFIX-996 (theorem 996.2) is \`M_n ~ (9/(8*pi^(5/2))) n^(-5/2)\` for \`ell=n\`. PREFIX-997 (theorem 997.1) established that the first interior grade \`ell=n-2\` comprises paths with exactly one negative step and verified n<=12 by BRC integer recurrence. The present calculation continues that exact frozen candidate, not an alternative classical propagation.

## Theorem 998.1 — All-length closed coherent amplitude without path enumeration

Write \`n=m+1>=2\`. Delete the unique negative step \`-e_r\` from an n-word, leaving a positive word \`X_1...X_m\`. Let its six-count vector be \`h=(h_1,...,h_6)\`, \`sum h_a=m\`. Its final displacement is \`k=h-e_r\`, which may have one coordinate -1. Define
\`f(a,r)=1-6*1[a=r]\`, \`N(h)=m!/(prod h_a!)\`, and for \`h_j>0\`,
\`N_j(h)=(m-1)!/((h_j-1)! prod_(a!=j) h_a!)\`.

For a final *negative* step \`-e_r\` (incoming neighbour port \`+e_r\`), the integer amplitude numerator at the fiber \`(k,+r)\` is exactly

\`F^-_n(k,+r)=N(h)*(m-6*h_r)/m,    h=k+e_r >=0.\`     (1)

For a final *positive* step \`+e_j\` (incoming neighbour port \`-e_j\`), define \`q=m-1\` and \`b=h-e_j\`; for \`m>=2\`, set

\`t=q-6*b_r, z=q+24*b_r.\`
\`S_(r,j)(h) = N_j(h)/q * [t^2-z+t*(f(i,r)+f(j,r))].\`     (2)

Then the **coherent** numerator is

\`F^+_n(k,-j) = sum_(r: h=k+e_r>=0, h_j>0) S_(r,j)(h).\`     (3)

When \`m=1\`, replace (2) by \`S_(r,j)(h)=f(i,r)f(j,r)\`, with \`h=e_j\`. When \`n=1\` there is only a negative step, whose numerator is \`f(i,r)\` at \`k=-e_r\`.

All the displayed fractions are integers, as each equals a sum of signed integer BRC branch numerators. Thus, for every \`n>=1\`, the exact total Stage46 first-interior grade probability is

\`M_(n,1)=36^(-n) * (sum_(k,j) F^+_n(k,-j)^2 + sum_(k,r) F^-_n(k,+r)^2).\`     (4)

**Proof.** There are \`m+1\` insertion slots for the unique negative step in a positive m-word. If inserted at the final slot, the only possible reversal is between \`X_m\` and \`-r\`; summing \`f(X_m,r)\` over all \`N(h)\` permutations proves (1). For a slot before the last positive letter, its weight is \`f(i,r)f(X_1,r)\` at the initial slot, or \`f(X_s,r)f(X_(s+1),r)\` at slot s, 1<=s<m. Fix \`X_m=j\` and uniformly permute the remaining \`q=m-1\` letters with counts \`b=h-e_j\`. Their mean \`f(X_s,r)\` is \`t/q\`; their sum of squared f-values is \`z\`. Summing over internal consecutive pairs has mean \`(t^2-z)/q\`, while the initial and terminal pair contributions together are \`t(f(i,r)+f(j,r))/q\`. Multiplying by the exact permutation count \`N_j(h)\` gives (2). Distinct erased negative axes r may lead to the same endpoint and terminal positive port, so their signed amplitudes **must** be combined as (3) before squaring. This proves (4) with the native terminal-port observer. QED.

## Theorem 998.2 — Sharp first-interior / outer-grade ratio

For **each** fixed initial incoming axis \`i\` in the six-dimensional native Stage46 candidate,

\`lim_(n->infinity) M_(n,1)/M_n = 35/4.\`     (5)

In particular, reusing the *already proved* PREFIX-996 outer-grade constant,

\`M_(n,1) ~ (315/(32*pi^(5/2))) n^(-5/2).\`     (6)

This is a model-internal asymptotic of exact typed BRC amplitudes, not a physical-time tail or a native force law.

**Proof.** Put \`l=n-2\`. Let \`B_l(k) = l!/(prod k_a!)\` on nonnegative six-count vectors with sum l, and \`Q_l = sum_k (B_l(k)/6^l)^2\`. By PREFIX-996, \`M_n=Q_(n-1)/6\`, and \`Q_(l+1)/Q_l ->1\`.

Consider the collision-biased probability distribution \`w_l(k)= (B_l(k)/6^l)^2/Q_l\`. Write \`Y_a=(k_a-l/6)/sqrt(l)\` with \`sum Y_a=0\`. Stirling's factorial formula uniformly in any central window, together with the standard exponential multinomial tail estimate, shows that under \`w_l\`, Y converges with fourth moments to the five-dimensional Gaussian on the sum-zero subspace having covariance \`(1/12)I\` on that subspace. In particular \`12*sum_a Y_a^2\` tends in moments through order 2 to \`chi-square_5\`. This follows also by squaring the ordinary multinomial local Gaussian law, which halves its covariance; the complement of a growing central window contributes negligibly to fixed polynomial moments. The boundary configurations with a zero/negative coordinate are exponentially small after the polynomially bounded marked-insertion factors in (1)-(3).

For central \`k>=0\`, \`r,j\` fixed, and \`h=k+e_r\`, equation (2) gives
\`N_j(h)/B_l(k) = 1\` if \`r=j\`, or \`k_j/(k_r+1)=1+o(1)\` otherwise. Moreover \`t=-6*sqrt(l)Y_r+O(1)\` and \`z=5*l+O(sqrt(l)(1+|Y_r|))\`. Consequently, uniformly on bounded Y,
\`F^+_n(k,-j)/B_l(k) -> P(Y):=36*sum_r Y_r^2-30,\`
independently of j and i. The formulas and multinomial tail estimates yield uniform square integrability for this polynomially growing ratio; hence the convergence holds for squared weighted sums. All final-negative-port fibers contribute \`o(Q_l)\` after normalization: (1) gives amplitude \`O(B_l(k)(1+|Y|)/sqrt(l))\` centrally; the boundary contribution is exponentially small.

For \`Z~chi-square_5\`, \`P(Y)=3Z-30\`, so
\`E[P(Y)^2] = 9 E[Z^2]-180 E[Z]+900=9*(5*7)-180*5+900=315.\`
There are six final positive ports. Therefore (4) implies
\`M_(n,1) ~ (6*315/36^2)*Q_l = (35/24)*Q_l.\`
Division by \`M_n=Q_(l+1)/6\` proves (5), and combination with the previous exact outer asymptotic proves (6). QED.

The proof uses combinatorial counting of the signed Stage46 BRC output; the Gaussian local limit is an analytical tool for that already-defined integer sequence, not a numerical replacement for BRC dynamics. No new decimal evaluation or classical trigonometric/pi expansion was used as a physical input.

## Exact BRC verification and coverage

Companion reproducible script: \`PREFIX998_R6_ONE_NEGATIVE_ASYMPTOTIC_CHECK.py\`. Certificate: \`PREFIX998_R6_EXACT_RESULTS.json\`. The script implements (1)-(4) using Python built-in integer arithmetic and independently propagates the **same Stage46 twelve signed ports** by the integer kernel numerator \`1-6*1[incoming=outgoing]\`, retaining negative count, signed Cell and final incoming port. Exact fiber-by-fiber equality holds for n=1,...,7; total numerators agree with PREFIX-997 for those n and with its published values for n=8 and 10. The all-n proof is independent of the finite test.

For n = 8,10,12,16,20,24 the exact ratios \`M_(n,1)/M_n\` computed by the closed formula are, respectively:
\`10.421606799494, 10.005479329955, 9.689392367884, 9.355431749081, 9.200184658037, 9.110596760695\`.
The last value is still above its proved limiting value \`35/4=8.75\`; finite convergence is not the proof of (5). All exact numerator and denominator integers are in the JSON certificate. We did not perform a new independent review or a native backend heartbeat experiment.

## Provenance, control, next problem

Inputs: frozen P000 V5 \`f42f2906\`; Stage46 local BRC candidate; PREFIX-996 at \`0bfb06f7e3118bed106b730ec0daf00ab5786adb\`, PREFIX-997 at \`436902ad6606be55f596a228f9419b0573502ff0\`; current active portability and research policies read 2026-11-22. Historical researcher \`EM-DIRECT-FBEA5D\` is provenance, not new execution authority.

Owner-list request \`r6-20261122-0647-current-leased-v1\` returned \`FAILED/SOURCE_TREE_TRUNCATED\` with \`EVENT_ISSUE_GUARD_CHANGED\` during Source materialization. No current full owner census or shared CLAIM was obtained. This is independent portable Source research; no Result/Review or Activity event is asserted by this note.

**Next:** derive a finite exact recurrence for \`M_(n,1)\` avoiding all endpoint/port fiber storage, and calculate a first-order correction to \`35/4\`. Subsequently include native X6 Link/Port occupancy and triadic feedback, with the observation map and signed history preserved. Mother question \`B_fix,odd(32) in {19,20}\` remains open.

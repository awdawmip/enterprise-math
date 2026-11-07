# PREFIX-551 — Terminal-resolved graded BRC observer, exact reconstruction, and information-loss witness

Date: 2026-11-07 Asia/Shanghai. Project: Enterprise Math, independent portable research for RS-X6-NATIVE-ROTATION-DYNAMICS. Frozen science pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; direct prior result PREFIX-550 at \`002b4c8e91d0f78f464ccde9357deeb8d455165b\`. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. No claimed formal task CLAIM/Result/Review.

## A. Model and exact definitions

The frozen four-STAR native X6 candidate has 48 oriented phases, 144 legal directed phase edges, and 96 phase/previous-branch-bit ports. Legal successor actions are three next-position slots times the two possible new branch bits. Signed native phase directions form S={±e_1,…,±e_6}. The first-axis and complete six-axis BRC local increments follow PREFIX-539 / PREFIX-550:

\[
\tau_{a,r}(i,j)=\frac{|\sigma_a(i)|+|\sigma_a(j)|-|\sigma_a(j)-r_a|+|\sigma_a(i)-r_a|}{2}\in\{0,1\}.
\]

The gate variable z counts arrival at the specific native phase (A,+L1,−L3) with consecutive INNER branch bits. The joint readout records all six BRC cancellation counts, gate events, and positive integral path multiplicities. This is a discrete combinatorial counting model, without treating multiplicities as signed physical amplitudes.

PREFIX-549 provides 51 future-counting equivalence classes (a 49-dimensional minimal linear realization is possible). PREFIX-550 gives a universal auxiliary zero-root 51×51 transfer Q_0 in which each legal transition out of class C contributes a factor q_{a(C)} z^g, where a(C)∈{1,…,6} is the class's native source axis, and g∈{0,1} is the gate increment. Auxiliary zero-root is an algebraic transfer parameter; it is not a physical source origin.

## B. Theorem A — exact five-exponent, twelve-terminal-channel transfer

For C in the 51 classes and s∈S, define

\[
B_{C,s}(0)=\mathbf1_{\sigma(C)=s},\qquad
B_{C,s}(d+1)=\sum_D (Q_0)_{C,D}B_{D,s}(d)
\]

for every integer d≥0. Each B is a polynomial over nonnegative integers in q_1,…,q_6,z.

**A1 (homogeneous degree and one-coordinate elimination).** Every nonzero monomial q_1^{p_1}⋯q_6^{p_6}z^h of B_{C,s}(d) satisfies

\[
\boxed{\sum_{a=1}^6 p_a=d}.
\]

Consequently it can be stored *injectively within the fixed length-d stratum* using just (p_1,…,p_5,h) and the terminal label s; the exact missing coordinate is p_6=d−∑_{a≤5}p_a. The recurrence can update these five coordinates directly: when the source class has native axis 6, no retained q-exponent increments; for axes 1–5, increment its corresponding coordinate. In every case add g to h. This reduced-coordinate recurrence recovers the original full polynomial exactly.

*Proof.* At depth zero the nonzero terminal seed is 1 and has total BRC q-degree 0. Every legal Q_0 edge multiplies by precisely one q_{a(C)} (and optionally z), irrespective of endpoint. By induction each path contribution at depth d has six-axis degree d. No cancellation occurs in the positive-integer path-counting semiring. Thus the omitted sixth exponent is uniquely reconstructed and remains nonnegative. Projection and reconstruction commute with the recurrence on each fixed length stratum. ∎

**A2 (all physical root signatures from one transfer).** Let p be a physical initial port with r=σ(p)∈S, quotient class C(p), and q_r=q_{a(r)}. For every d≥0 its exact complete BRC–gate joint generating polynomial is

\[
\boxed{
P_p^{(r)}(d)=B_{C(p),r}(d)+q_r^{-1}\sum_{s\ne r} B_{C(p),s}(d).
}\tag{551.1}
\]

The RHS is a genuine polynomial with nonnegative integer coefficients, and it recovers the **complete** rooted seven-variable histogram, not merely first moments or marginal distributions.

*Proof.* Fix a native path i_0→⋯→i_d, set r=σ(i_0), s=σ(i_d), and use the exact local BRC identity from PREFIX-550. For every axis a, the rooted and auxiliary-zero-root exponents differ by the telescoping boundary term

\[
p_a^{(r)}=p_a^{(0)}-\mathbf1_{a=a(r)}
+\mathbf1_{s=r}\mathbf1_{a=a(r)}.
\]

The gate event exponent is unchanged. When the terminal signature matches r, the rooted and zero-root weights coincide. Otherwise the original root axis loses exactly one q_r factor. For a path of positive length the first source phase has direction r, so its zero-root q_r exponent is at least one, ensuring divisibility. At length zero the only nonzero terminal channel is s=r. Partitioning all action paths by terminal signature and summing their positive integer weights gives (551.1) for all d≥0. ∎

**Implementation interface.** Keep one common 51-class Q_0 kernel, twelve signed-terminal columns indexed by s, and only the five explicit q exponents and the gate exponent. For a given physical start, first reconstruct q_6 from d and then apply the r-dependent boundary correction. The terminal label is finite **relation metadata**, not a seventh spatial dimension. The original initial port/quotient class remains part of the source key.

## C. Theorem B — terminal identity contains necessary information for the specified correction

Consider initial port p=(STAR A, previous +L3, current −L1, previous branch OUTER). Thus r=−e_1. Two legal length-four action strings, with each action (next-position slot,new branch bit), are

- Path I: (0,0),(1,0),(1,0),(1,0); terminal phase (STAR A,+L3,−L1), terminal signed direction −e_1.
- Path II: (0,0),(0,0),(1,0),(0,0); terminal phase (STAR C,+L2,−L5), terminal signed direction −e_5.

Both native action paths have the same zero-root monomial **q_1 q_2 q_3 q_6**, and gate count 0. The rooted physical weights are different: Path I has q_1 q_2 q_3 q_6, while Path II has q_2 q_3 q_6. Hence the unlabelled auxiliary-root histogram does not permit **termwise** rooted reconstruction by (551.1). The twelve endpoint channels preserve the needed distinction, although this example alone does not claim twelve is a universally minimal number of channels.

## D. Executed verification (exact integer arithmetic)

Verified program: \`PREFIX551_terminal_graded_exact_certificate.py\` (Python standard library only), importing the published predecessor \`PREFIX550_shared_gauge_compact_certificate.py\`, Git blob \`a0d057fadf610e89983723f1392d5b798b7c05d5\`. Frozen science input \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.

Execution: \`--cross-depth 8 --internal-depth 6 --benchmark-depth 7 --repeats 3\`. Actual result: **ALL_CHECKS_PASS**.

- 4,284 complete (51 classes ×12 terminal directions × depths 0…6) comparisons of the full q_1,…,q_6,z Q_0 recurrence with five-axis-exponent terminal-channel recurrence.
- 25,128 monomial degree assertions.
- 864 complete rooted physical histograms (96 start ports × depths 0…8) matched coefficientwise against separately assembled native Q_r transfer; 61,907 nonzero coefficient positions compared.
- Both explicit length-four path witnesses checked at the native edge/action level.

The two recurrence implementations share the published native edge law; the published PREFIX-550 source contains additional independent path-endpoint BRC checks. This describes the actual exact verification scope.

## E. Measured full-output cost (exploratory)

Linux/CPython integer polynomial maps; 3 repetitions, median; kernels and quotient precomputed. The timed portion includes dynamic evolution, full readout for **all 96 original start ports at each depth 0…7** (768 joint polynomials, 29,498 nonzero positions), and 49-coordinate reconstruction when used. Python tracemalloc peak is for timed runs, excluding shared precomputation.

| Engine | Median time (s) | Traced peak (bytes) | Max internal polynomial entries |
| --- | ---: | ---: | ---: |
| 12 rooted Q_r 51 positive classes | 1.258624 | 5,644,164 | 8,635 |
| 12 rooted T_r 49 signed coordinates | 1.286641 | 5,403,020 | 8,062 |
| **One Q_0, 12 endpoint channels, 5 retained q exponents** | **0.697078** | **9,021,884** | 24,358 |

All algorithms produced exactly identical complete polynomials. Under these measured conditions the new method runs about 1.81× as fast as the 51-state rooted baseline, with about 60% more tracked peak memory. These are implementation- and horizon-specific empirical performance findings; cold-start initialization and longer-horizon scaling are separate experiments.

## F. Source, evidence, role and next question

Local complete research package contains this theorem expanded in prose, the exact executed Python script, detailed JSON run data, a readable README and SHA256 manifest. Local checked source digest: \`323dfb12b002e8cdeac185f4960fd9a508c809312077b1e547ed72e660c0b2fd\`. Exact JSON output digest: \`ff07e8de0c2ad4a199b7dfa5bd3bd46cddc3230e759755e9b5a054199eb78fd7\`. The full package may also be distributed separately; these hashes are reproducibility references, not independent theorem admission.

Authenticated GitHub account observed: awdawmip (enterprise-math push/admin permission). The native Enterprise Math status gateway returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; no current authenticated Researcher-ID, active Owner, CLAIM, Result or review was established by the present author.

**PREFIX-552 proposed research unit:** design an output-directed endpoint-column strategy or nonnegative channel-sharing compression that lowers peak memory without losing rooted readout; derive shorter future-operation distinguishability witnesses for attempted terminal-channel merges; measure cold-start and deeper-horizon costs. The larger mother goal remains complete relationship-preserving X6/BRC research, not the closure of one implementation optimization.

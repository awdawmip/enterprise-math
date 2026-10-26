# R4-EC35 — Sharp finite-horizon source-label observer compression

**Research status:** author-side exact mathematical proof with local exact-integer/rational checks, not an independently reviewed/admitted theorem and not native Heartbeat dynamics. **Date:** 2026-10-26, Asia/Shanghai.

## Immutable inputs and actual authority

GLOBAL_KNOWLEDGE_V1 single canonical-main snapshot: 8a584051572960ae4823296de3397ffaafbb4b11. Read its bootstrap, manual, Enterprise Math router and task researcher route, P000 and P000_STARTUP, ACTIVE worldview and relevant research/BRC/code/persistence policies. P000 original SHA-1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches its projection and remains ACTIVE_LOCKED. Enterprise Math source snapshot: f52af9bc69937880cca0d3fa5f97cbe9a79e7194. Read docs/PORTABLE_RESEARCH_PROTOCOL.md and docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md; no native heartbeat computation is claimed.

Exact predecessors are EC33 commit 0f84db42704c6e107adb9fd99d5e64cb77589e9d and EC34 commit d90b896f9bdcd61c93d09dd7add5cdbee174b7fa. The unchanged EC33 Python transition source has SHA256 c2c5b183f88e7856c006f6b9ca954d603ac4e2cfd25d65a5558c67c91bc69856 and EC34 rational-rank code has SHA256 6dda5679426771152f3f09fa1327bf7c69dff3c03a9c50214f635532a9bf2862. Authenticated GitHub login awdawmip has push/admin permission, but native owner/task query returned CONTROL_QUOTA; no live Owner or CLAIM is verified or assumed. This is an independent author-side BRC auxiliary computation.

## Typed source carrier and target observer

Fix H>=1. EC33's positive-source carrier has history states q=0,...,H, initial q=0, and one operation A. For q<H, exactly one microscopic red R edge and one blue B edge advance to q+1. At q=H, two **distinct** positive red microscopic alternatives R0 and R1 remain at H, and B is impossible. Ordered path choices multiply; positive alternatives add; all terminal states have readout 1. Set a=H-q, the remaining pre-saturation capacity.

Our observer asks for all exact counts of *observed* source-label words w in {R,B}* up to operation horizon h. R0 and R1 remain different microscopic edges of the carrier, although this specific observer merges their labels into R while preserving multiplicity. No claim about a finer microscopic-source-ID observer, arbitrary future ports, signed/complex phase, physical time, six-dimensional X6 correspondence, or external physics is included. h counts A-steps only.

Let F_a(w) count microscopic source paths from capacity a with observed label word w. Let P_a^n be the probability distribution on length-n observed words after normalizing the total microscopic count.

## Theorem 1: exact state-conditioned word law

For every H>=1, a in {0,...,H}, and word w of length n,

$$
F_a(w)=\begin{cases}
1,&n\le a,\\
2^{n-a},&n>a\text{ and }w_{a+1}\cdots w_n=R^{n-a},\\
0,&\text{otherwise.}
\end{cases}
$$

**Proof.** For the first min(a,n) operations each specified R/B label has exactly one available microscopic edge and the capacity decreases by one. If the word ends by that time, count is 1. After a steps the carrier is saturated; the remainder must be all R, with two independent distinct microscopic red alternatives at each step. The source count is therefore 2^(n-a) on the allowed suffix and zero otherwise. Every state has exactly two outgoing microscopic alternatives in total, so the sum over all words of length n is always 2^n. QED.

## Theorem 2: exact truncated observability rank and minimal lossless classes

Define O_(H,h) as a matrix with one row for each current capacity a=0,...,H and columns indexed by *all* observed label words of length <=h, entry F_a(w). Then

$$
\boxed{\mathrm{rank}_{\mathbb Q}O_{H,h}=m_{H,h}:=\min(H+1,h+1).}
$$

The coarsest exact state-identification relation preserving all declared length-<=h future word-count observations is

$$
\boxed{a\equiv_h b\quad\Longleftrightarrow\quad \min(a,h)=\min(b,h),}
$$

with exactly m_(H,h) classes.

**Proof.** If a>=h, all words of length <=h have count 1 by Theorem 1, so these rows are identical; every a<h may have a distinct row. Thus rank <=m. For a<b with a<h, word B^(a+1) has count 0 from a and count 1 from b, distinguishing the rows and proving the stated exact equivalence. To certify the *linear* lower bound, select m rows a=0,...,m-1 and m columns B^k for k=0,...,m-1. Their entries are precisely 1_{k<=a}, a unit lower triangular matrix with determinant 1. Hence rank >=m. QED.

**Constructive, budget-aware update.** Retain the pair (h,c), where c=min(a,h). At h=0 all states have terminal readout 1 and need no transitions. At h>=1, if c>0 an R or B step has multiplicity one and goes to (h-1,min(c-1,h-1)); if c=0 only R is possible, with multiplicity two, going to (h-1,0). For c=h, all underlying a>=h remain in the same successor class, so the update is well-defined. This is a lossless horizon-decreasing quotient, *not* a single smaller time-homogeneous all-future automaton. When h<H, EC34's all-future Hankel rank H+1 blocks that stronger inference.

## Theorem 3: exact sharp total-variation error and a one-half gap

For any 0<=a<=b<=H and n>=0,

$$
\boxed{\mathrm{TV}(P_a^n,P_b^n)
=1-2^{-\left(\min(n,b)-\min(n,a)\right)}.}
$$

For a fixed maximum depth h,

$$
\boxed{\Delta_h(a,b):=\max_{0\le n\le h}\mathrm{TV}(P_a^n,P_b^n)
=1-2^{-\left(\min(h,b)-\min(h,a)\right)}.}
$$

**Proof.** Theorem 1 gives P_a^n as the uniform distribution on the 2^min(a,n) words whose suffix after position min(a,n) is entirely R. For a<=b, this support is contained in the corresponding support for b. Their common mass sum of pointwise minima is 2^min(a,n) times 2^-min(b,n), giving TV=1-overlap. The exponent is nondecreasing in n and becomes constant by n=b, giving the sharp horizon maximum. QED.

Whenever a<b and a<h, the distinguishing depth n=a+1<=h gives **exactly** TV=1/2. Therefore any pairwise error tolerance epsilon<1/2 permits no merging between two different exact future-observer classes; this discontinuity is sharp, since neighboring capacities have horizon TV exactly 1/2.

## Theorem 4: optimal diameter-controlled approximate grouping

Let H>=1, h>=0, 0<=epsilon<=1. Put m=min(H+1,h+1) and define the integer

$$
d_\epsilon=\max\{j\in\{0,\ldots,m-1\}:1-2^{-j}\le\epsilon\}.
$$

For partitions of the actual carrier states into classes with pairwise future-observer TV diameter <=epsilon (i.e. Delta_h(a,b)<=epsilon for every two members), the exact minimum number of classes is

$$
\boxed{N_{H,h}(\epsilon)=\left\lceil\frac{m}{d_\epsilon+1}\right\rceil.}
$$

**Proof.** The distinct truncated capacities c=min(a,h) run through exactly the consecutive integers 0,...,m-1. By Theorem 3, a class has future-TV diameter <=epsilon iff its maximum and minimum values of c differ by <=d_epsilon. A class therefore contains at most d_epsilon+1 distinct cap values. Covering all m values requires at least ceil(m/(d_epsilon+1)) classes. Consecutive blocks of at most d_epsilon+1 cap values achieve equality; duplicate original states with the same cap join its block. QED.

In particular epsilon<1/2 implies d=0 and N=m (no lossless or small-error extra compression). At epsilon=1/2, d=1, so N=ceil(m/2); at epsilon=1, N=1. This optimality is only for **pairwise diameter-controlled deterministic state grouping for the specified finite-horizon label distributions**. It is not an optimal stochastic approximation theorem, not a global time-homogeneous approximate quotient, and not a bound on propagated native physical error.

**Example:** H=4, h=2 gives exact capacity classes {0}, {1}, {2,3,4} and m=3. The B-word minor for capacities 0,1,2 and words (empty,B,BB) is [[1,0,0],[1,1,0],[1,1,1]], determinant 1. If epsilon=1/2, the optimal pairwise-diameter grouping has two classes; if epsilon<1/2, three classes remain necessary.

## Executed checks, reuse and evidence

The actual local EC35_verify.py reused the **unaltered, SHA256-pinned** EC33 transitions and EC34 rational rank implementation (REUSE_EXECUTED). It checked 304 source-transition cases, 28,880 B-column entries, 304 truncated ranks, 27,594 exact labelled-word counts, 486 complete normalized total masses, 1,485 rational TV comparisons, 2,970 TV horizon inequalities, 164 one-half boundary witnesses, and 64 independent exhaustive small-m partition minima. Parameters: H=1..16, h=0..18, full words through length 8 for H<=9, partition sizes m<=8. All exact integer/rational checks passed. ZIP-extraction cold-start reproduced the full report byte-for-byte. The local complete source, full JSON report, pinned EC33/EC34 programs and cold-start receipt are in EM_R4_EC35_FINITE_HORIZON_20261026.zip (SHA256 409626a74bdc42cb16069c26a4360af729981c3dd4cc717ade4a964a9476e249). Saved code on GitHub does not imply remote execution; no finite test is substituted for these all-parameter proofs.

The program uses BRC positive ordered alternatives, not classical/trigonometric propagation. Existing BRC source IDs and label distinctions are typed explicitly. This does not identify physical residual, phases or the P000-native update.

## Residue and next question

P000 is locked and declares fixed_heartbeat_program=null. The true X6 source-labelled update operator, admissible three-dimensional slice with third-coordinate semantics, time type, source labels and terminal ports remain unspecified/unverified, as does the native-to-BRC map. Native attribution remains NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION.

**R4-EC36:** derive or obtain an actually authorized, fully typed X6 source transition and label/port observation rule, then prove a source-fibre-preserving map or a finite labelled-state closure before using EC32/EC33 finite certificates. Independently, within this auxiliary carrier, determine sharp propagation conditions for genuinely **compositional approximate** observer quotients; the present fixed-horizon TV diameter theorem deliberately does not settle that stronger problem.

# X6-SIG-PREFIX-34 — Partial-source overwrite, two probes, exact right congruence

Status: **UNREVIEWED / AUXILIARY MATHEMATICS / NO FORMAL CLAIM / NO NATIVE MODULE EXECUTION**.
This is a portable research note; neither P000, Heartbeat World dynamics, native rotation, nor independent mathematical admission is asserted.

## Pinned sources and scope

GLOBAL_KNOWLEDGE_V1 canonical main: `330b2c1378bf343fb35d70425573cae9aa2070f2`.
Enterprise Math main: `9eb4f07b2f1fd9f853a860fa156a5bf2a78ce0a2`.
Basis: locally checked prior PREFIX-33 (9-state full product, 7-state safe quotient when P/Q overwrite old tag) plus current P000, ACTIVE residual worldview, portable research protocol, BRC positive-weight contracts and `src/enterprise_math/brc_control_port.py`. Earlier PREFIX-33 remains LOCAL/UNREVIEWED rather than an admitted result.

**Observer:** for every finite selected operation word, observe the full positive rational path weight, complete composed six-coordinate *auxiliary* permutation, and positive integer multiplicity, but not the hidden control state or the last source label directly. Additional operation alternatives combine by adding nonnegative multiplicities; no signed cancellation. The coordinate permutations below are external discrete test actions on six labels; they are **not** asserted to represent native six-axis 120-degree geometry or physical time evolution.

## New exact example: 9 states and 38 positive transitions

Let `X=(12)`, `Y=(23)` act on six integer-coordinate labels and fix 4,5,6. They do not commute. Control states `F(m,l)`, `m∈{1,2,3}`, `l∈{P,Q}`, and `N,S,T`. The cumulative permutation `g` is retained separately, and `m=g(1)`; `l` means the **most recent P/Q source class**, not the last edge ID.

From each F(m,l) there are six deterministic, strictly positive rows:

| Input | positive weight | six-coordinate effect | target |
|---|---|---|---|
| P | 1/5 | X | F(X(m),P) |
| Q | 1/7 | Y | F(Y(m),Q) |
| H | 1/13 | X | F(X(m),l) |
| K | 1/17 | Y | F(Y(m),l) |
| E1 | 1/11 | identity | S iff m=3 and l=Q; otherwise N |
| E2 | 1/19 | identity | S iff m=3 and l=P; otherwise N |

From N, only R (weight 1/2, identity) enters T. From S, only R (weight 1/3, identity) enters T. T has no outgoing rows. This gives 6×6+2=**38** positive edges. P/Q replace old label; H/K **change the guard while preserving old source label**, a partial overwrite. Both probe operations end the F phase.

## Theorem 34.1 — exact four-round separation

Define Hist_s(w) as the exact effect histogram from control state s for word w. For this **deterministic-per-operation invertible-effect** finite BRC, let states be equivalent to depth d if these histograms are equal for all words |w|≤d.

- At depth 0, all nine states have the identical identity observation.
- At depth 1, the classes are [all six F], [N], [S], [T]: **4** classes.
- At depth 2, E1R/E2R distinguish F3P from F3Q, but lower guards still merge: **6** classes.
- At depth 3, K transports F2P/F2Q to F3P/F3Q without resetting l: **8** classes.
- At depth 4, HK transports F1P/F1Q into F3P/F3Q while keeping l: **9** singleton classes.
- A fifth refinement has no change. Thus the minimal deterministic fixed-row, exact-word terminal-observer model has **nine** states. This does not claim global minimality among all arbitrary nondeterministic weighted representations.

Exact shortest witnesses for equal-guard opposite-source pairs:

| Pair | shortest word | first weight | second weight |
|---|---|---|---|
| F3P / F3Q | E1 R | 1/22 | 1/33 |
| F2P / F2Q | K E1 R | 1/374 | 1/561 |
| F1P / F1Q | H K E1 R | 1/4862 | 1/7293 |

Each pair shares exactly the same composed six-coordinate permutation and integer multiplicity on its witness. Witness minimality follows because a non-overwriting H/K prefix needs respectively 0,1,2 steps to bring m to 3, and detecting the changed probe mode requires E1 followed by R. Any P/Q step overwrites and discards the old label before it can be distinguished.

Consequently a proposed **one-pass immediate probe signature** would merge F1P and F1Q, yet `H K E1 R` distinguishes them. The PREFIX-33 shortcut "old source is overwritten before it can matter" fails once a legal continuation can modify the cumulative guard *without* overwriting that source.

## Theorem 34.2 — finite-lookahead right congruence, exact domain of validity

For a finite deterministic partial transition machine with a positive nonzero rational weight and an **invertible** affine effect on each legal letter, define `≡_0` as all states and refine `≡_{d+1}` by the entire per-letter tuple (undefined, or [weight,effect, ≡_d target]). Then **≡_d is exactly equality of all complete effect histograms for words of length at most d**.

Proof: induction on d. The one-letter observation determines presence, exact positive weight, and full effect. For any shared first letter, equality of longer word effects permits cancellation of its nonzero weight and invertible prefix effect, giving equality of every successor future histogram. Conversely identical rows and equivalent targets imply all longer observations equal. Each strict refinement increases class count, so stabilization is finite, in at most |S|-1 strict steps. The stable partition is the exact right congruence. If effects are noninjective, per-row congruence is still a safe sufficient condition but not in general a necessary condition for the coarsest endpoint-observation quotient; do **not** discard this distinction.

For genuinely branching positive BRC, exact effect-valued row descent is sufficient for future-safe compression, but the deterministic/invertible necessity claim must not be silently generalized.

## Additional result: polynomial joint support, exact convergent infinite mass

Allow independent four-way positive alternatives `C=P⊕Q⊕H⊕K`. There are 4^k ordered source paths for `C^k E1 R`. Since weights of P,Q,H,K involve distinct primes 5,7,13,17, a depth-k path's first-stage weight is determined by its four nonnegative letter counts, of which there are `binom(k+3,3)`; the cumulative action lies in the six-element S3, and the final R mode has at most two weights. Thus

`support(C^k E1 R) ≤ 12 binom(k+3,3)`

for exact (weight, six-axis effect) atoms, versus 4^k source paths. This is a general upper bound *for this model*, not an asymptotic theorem for all BRC. At k=8, full reference enumeration finds **65,536** original paths, **508** distinct joint atoms, and largest positive integer multiplicity **1296**.

Let W be the 6×6 positive rational transition matrix for C in state order `F1P,F1Q,F2P,F2Q,F3P,F3Q`, and let r1(s) and r2(s) be the single-probe-plus-R exact mass at state s. Every W row sums to

`s = 1/5+1/7+1/13+1/17 = 3702/7735 < 1.`

Therefore the all-depth positive masses exist *rigorously* as `v_i=(I-W)^{-1}r_i`. Starting in F1P, exact rational Gaussian elimination yields:

- E1: `11957805167982249875/138748133856252806952`.
- E2: `11993960558995387765/239655867569891212008`.

Both solutions are checked by the exact identity `(I-W)v_i=r_i`. The residual beyond depth K is the nonnegative exact expression `e_F1P^T W^(K+1) v_i`, bounded by `max(r_i) s^(K+1)/(1-s)`. These are **mass** results, not physical energy/dissipation statements.

## Executed verification, limitations and next step

A self-contained local Python 3 reference checker with `fractions.Fraction` performs 235,296 independent cumulative-history vs compiled-nine-state checks for all words length 0–5 over the seven inputs and all 6×2 group/tag contexts, plus 7,200 terminal-mode checks. It finds all 36 pairwise shortest distinguishing words and the exact refinement trajectory [4,6,8,9,9]. Independent brute-force path enumeration agrees on all C^k E1R effect histograms for k=0…8; k=8 gives 508 atoms. The same checker verifies both all-depth rational mass values and exact truncation tails. Scope: *auxiliary finite permutation BRC*, not the native ControlPacket runtime (NOT_RUN), not a native Heartbeat World geometric or empirical theorem.

**Next PREFIX-35:** determine whether there is a computable a priori upper bound on minimal source-memory length from a finite guard action, probe location and non-overwriting action graph; distinguish finite guard automata from infinite right-congruence cases, and run the native ControlPacket replay once the real source environment and authorized scope are available.

**Control status:** no native research CLAIM or author-side Source admission is asserted. Project branch storage of this report, if successful, is an unreviewed research frontier only, not canonical main, Result or independent Driver acceptance. Previous runs' inaccessible server owner identity must not be borrowed.

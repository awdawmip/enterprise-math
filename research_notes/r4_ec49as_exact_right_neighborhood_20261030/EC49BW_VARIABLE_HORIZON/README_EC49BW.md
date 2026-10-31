# EC49BW — Variable-horizon signed-X6 BRC: uniform-rank criterion, exact boundary count, and a computability obstruction

2026-10-31. **Evidence class:** AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_X6_FINITE_AUDIT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Frozen inputs and author provenance

- GLOBAL_KNOWLEDGE_V1 canonical main **ddecaf1a2fe9e8ff3840a01f2e53592876e03ccb**, with the current 00_BOOTSTRAP.md, OPERATING_MANUAL.md, project/TASK routers, P000 V4 (canonical blob **770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc**) and ACTIVE worldview.
- Enterprise Math canonical main **215993ba0120825b56004f7cdb149a2332692758**, with AGENTS.md, docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md, docs/PORTABLE_RESEARCH_PROTOCOL.md and research_persistence_policy.json.
- Prior author EC49BV is an **unreviewed draft** at PR #1730 head **e28658dba53ca78d4d1a3609eeb039b5720790e5**. The native Python BRC kernel used for the finite audits is the unchanged EC49BV sibling file signed_brc.py, Git blob **300a96e3dc24bf6fff73743037a0347a8bc83176**.
- Static ordered paths in the six native P000 spatial axes, not physical heartbeat dynamics, three-dimensional slice transfer, complex amplitudes, or twelve spatial dimensions. P000 is not amended.

## 1. Exact observer-rank theorem

Let Sigma={+e_i,-e_i | 1<=i<=6}; for even n let P_n be all ordered n-step words whose signed displacement in Z^6 is zero. Path bags have nonnegative rational multiplicities and their additive observation statistics are extended Q-linearly. Fix a **finite** axis permutation group H<=S_6, strictly positive rational per-step weights w, and a finite family of regular source-side tests at each n. Let beta_n be the **entire Boolean atom**, and expressly allow selecting every attainable atom *before* the group-transformed weighted readout. For each atom b and h in H set

O_(b,h)(p) = 1[beta_n(p)=b] chi_w(h p),  chi_w(p)=product_{a in p} w(a).

The *fixed instrument* keeps w fixed as the path axes are permuted; the *covariant instrument* co-transports w according to (h.w)(h a)=w(a). The source-side atom is kept semantically fixed; filter transport is not silently assumed.

**Theorem A.** If A_n is the number of nonempty realizable source atoms, the exact minimum Q-linear additive state ranks obey

A_n <= R_fixed(n) <= |H| A_n;     R_covariant(n) = A_n.

In particular for one fixed finite group H,

sup_n R_fixed(n) < infinity  iff  sup_n A_n < infinity  iff  sup_n R_covariant(n) < infinity.

**Proof.** Rows with different selectable atoms have disjoint path-column support. Each nonempty atom gives a nonzero matrix block (positive weights), of rank between 1 and |H|. The whole observation matrix is a direct sum of these blocks. Under co-transport all h-rows are identical on that atom, leaving rank exactly 1. Any exact Q-linear factorization O=BT needs dimension at least rank(O); taking a row basis reaches equality. The finite-H rank sandwich yields the uniform equivalence. QED.

The atom-selector assumption is essential: a system observing only separate single tests, with no intersections, need not have block-diagonal rank. This is a minimality statement among **Q-linear additive states**, not arbitrary nonlinear or compressed-bit encodings.

## 2. Exact boundary-label count

Suppose all joint length-r prefix and length-s suffix labels are selectable, with r+s=L<=n, and n even. Write a boundary label as b=u v in Sigma^L (concatenated ordered prefix/suffix) and m=n-L the number of unobserved middle steps. Denote the signed displacement of b by d(b).

**Theorem B.** The label b occurs in at least one closed n-step native X6 word iff ||d(b)||_1 <= m. Consequently the exact number of attainable boundary atoms is

B(n,L) = sum_{b in Sigma^L} 1[||d(b)||_1<=n-L]

       = sum_{d:||d||_1<=n-L} [x^d] (sum_{i=1}^6(x_i+x_i^{-1}))^L.

(The observed r/s split affects the meaning of a label but not the number of realizable labels.) For all even n>=L,

6^{floor(L/2)} <= B(n,L) <= 12^L, and n>=2L implies B(n,L)=12^L.

**Proof.** The middle m steps must cancel d(b). A six-axis signed word with prescribed displacement v exists at length m exactly if ||v||_1<=m and m-||v||_1 is even, since mandatory steps realize v and the remaining steps can be adjacent forward/back pairs. Here ||d(b)||_1 congruent to L mod 2, and m=n-L congruent to L mod 2 (n even), so parity is automatic. The Laurent coefficient identity counts ordered signed boundary words of each displacement. To obtain at least 6^{floor(L/2)} realizable labels, concatenate floor(L/2) independently chosen pairs (+e_i,-e_i) with i in {1,...,6}; if L odd add +e_1 and cancel it with -e_1 in the middle. Fill remaining middle length by canceling pairs. Every such label is distinct and completable. If n>=2L, any L-step boundary has displacement norm <=L<=n-L, so all 12^L labels occur. QED.

**Corollary B1, necessary/sufficient uniform criterion.** Allow at most q additional Boolean regular tests per n for one fixed finite q, selecting all joint atoms of those tests together with boundary labels. Each boundary produces between one and 2^q nonempty refined atoms. Thus

6^{floor(L_n/2)} <= R_covariant(n), R_fixed(n) <= |H| 2^q 12^{L_n}.

For all even closed lengths, ranks are uniformly bounded **iff sup_n (r_n+s_n)<infinity**. If the number of auxiliary tests grows without bound, the bounded-L implication requires a separate uniform bound on attainable atom counts; Theorem A remains the exact criterion.

**Corollary B2, exponential no-go.** Let n=2r, s=0 and observe the entire length-r ordered prefix. Every one of the 12^r signed prefixes is completable by a fixed reverse-opposite r-step word. The covariant minimum state dimension is **exactly 12^r** and the fixed-instrument dimension is at least 12^r for all positive weights and finite H. The fixed-horizon saturation of EC49BU/EC49BV therefore cannot be extended to horizons growing linearly with n without changing the observer language.

## 3. No universal decision algorithm for unrestricted computable variable observers

**Proposition C (elementary halting reduction, not claimed as new priority).** No algorithm decides the uniform-rank boundedness question for arbitrary computable programs that output a finite regular selector family at each even n without a uniform bound on selector number or length.

**Proof.** Given a Turing machine M, on input even n simulate M for the first n steps. If it has not halted by then, return just the universal selector; its positive-weight rank is 1. Otherwise return all 12^{n/2} prefix atom selectors of length n/2, each regular and effectively constructed. If M never halts the ranks stay 1; if M halts the ranks grow without bound along all large even n by Corollary B2. Deciding rank boundedness would decide the complement of halting. QED.

This concerns unrestricted **computable sequences of finite regular families**; it does not rule out a finite certificate for a specified fixed automaton or a restricted parametric subclass.

## 4. Native BRC exact execution

The accompanying VERIFY_EC49BW.py exhaustively enumerates closed words for n=2,4,6 and independently computes boundary feasibility through dynamic programming over signed X6 displacements. It calls the unchanged native signed_brc.endpoint_multiplicity and endpoint_weight with w+=(2,3,3,2,1,1), w-=(1,1,1,1,1,1), and evaluates the row rank for H={id,(1 2)} by exact integer 2-by-2 minors.

(n,r,s) : (covariant rank, fixed rank; closed words; native weighted aggregate)
- (2,1,0): (12, 12; 12; 24).
- (4,1,1): (144, 156; 396; 1560).
- (4,2,0): (144, 156; 396; 1560).
- (6,1,1): (144, 288; 19920; 152640).
- **(6,2,2): (8364, 8760; 19920; 152640).**
- (6,3,0): (1728, 2124; 19920; 152640).

Additional exact boundary DP: B(8,4)=20736; B(8,6)=569100; B(10,5)=248832; B(12,6)=2985984. Two local executions produced byte-identical full JSON. No direct brute enumeration of n=8/10/12 closed words and no Lean formalization are claimed. Exact original author-side script SHA256=3419dd052d077c48042338f1a88229880b40963824b5d11d752f73f256048edb, JSON SHA256=b32f116de28ab54a9aea8d49e46dd2715d6800948e3ac1d90ac30d28b303904c. The sibling native source Git blob was validated before import.

A single signed closed path (+e_1)^r(-e_1)^r has selected native integer weight 2^r under these weights, whose **explicit binary numeral** needs r+1 bits. This is a separate exact-readout cost, not a lower bound on all sparse, factorized or symbolic encodings; a Q-linear rank is not itself a universal bit-memory lower bound.

Theorems A/B are proved at their stated generality; finite calculations verify only their listed input families. Typed BRC: REUSE_EXECUTED endpoint_multiplicity and endpoint_weight; COMPOSE_APPLIED group/filter observation and exact displacement DP. No shared Foundation/tool promotion.

## 5. Authority and smallest successor unit

Authenticated native status (2026-10-31): service 0.6.11, research_authority_granted=false, upstream CODE_REVIEW_REQUIRED and active native job quota 5/5. Actual bounded owner inventory request returned CONTROL_QUOTA. Therefore formal owner is **not independently verified** and there was no CLAIM, native Task Result, Driver review, admission, or P000/worldview modification. This draft is author-side provenance, not canonical accepted mathematics.

**Next EC49BX:** determine sharp exact **binary numeral** resource bounds for restricted nonnegative path bags with bounded coefficients, and distinguish arbitrary multiplicity, unit bags, path-weight growth, and symbolic/sparse representations. Prove a typed coefficient bridge to native endpoint_weight and give an effective finite-certificate subclass for variable filter programs; no universal decider is possible in Proposition C's full generality.

Mathematical background: classical rational formal series and weighted automata (Berstel and Reutenauer, *Noncommutative Rational Series with Applications*, Cambridge UP, 2010), standard Turing halting undecidability. No claim that those classical principles are newly discovered.
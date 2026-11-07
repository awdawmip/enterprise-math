# BRC N=4 — Exact two-query memoryless deficiency and persistent one-bit repair

2026-10-30. **AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Scope and inherited exact model

This is an **external, strictly-positive 16-leaf two-law BRC model** continuing Enterprise Math PR #1738 at immutable commit 0c973337792efd3affe80647e51f9f23f5bf87b7. It is **not** a theorem about native P000 six-dimensional cells, time dynamics, three-dimensional slices, or the native stopping-game minimax.

Original 16 leaves: (s,j,k) with s in {AU,AV,BU,BV} and j,k in {0,1}. Masses are Q(s,j,k)=q_s/4 and P(s,j,k)=q_s*r_(s,j)/4, with q=(1/6,1/3,1/4,1/4), and r_AU=(9/10,11/10), r_AV=(1/4,1/4), r_BU=(1/5,9/5), r_BV=(2,2). All P and Q masses are strictly positive and sum to one.

Under the predecessor's G0 policy the coarse observer O' distinguishes AU, BU, and an AV/BV aggregate. We additionally retain the BU child bit j. On BU, the two laws have exact j-atom masses

P(BU,j=0)=1/40, P(BU,j=1)=9/40;
Q(BU,j=0)=1/8, Q(BU,j=1)=1/8.

Both laws assign total BU mass 1/4. Conditional on BU and j, the **original leaf bit k is fair under P and Q**. No hidden H is added; this is not the predecessor's changed 20-leaf construction.

We declare a **read-only two-query extension**: two probes of the **same realized** BU leaf bit k generate (Y1,Y2)=(k,k), while all non-BU atoms emit (0,0). Whether post-stopping T4 probes are legally implementable in the original S2/S23 stopping filtration is not established and is not presumed here.

## Theorem 1 — sharp simultaneous P/Q error for independent emissions

Let a common decoder preserve (O',j_BU), and at each BU j emit two **conditionally independent** Bernoulli bits with arbitrary probabilities p_j and q_j in [0,1]. The first and second probabilities may differ, so time-homogeneity is NOT assumed. These independent fresh coins carry no persistent shared state or correlated seed between calls. Non-BU emissions are correct and deterministic.

The exact simultaneous two-law minimax reconstruction error of this **restricted decoder class** is

[
R_{mathrm{independent}}
=inf_Dmax{mathrm{TV}(P_{m physical},P_D),mathrm{TV}(Q_{m physical},Q_D)}
=rac{sqrt2-1}{4}approx0.10355339059327376.
]

**Proof for all real p_j,q_j.** Condition on a fixed BU,j. The physical law of (00,01,10,11) is (1/2,0,0,1/2). Independent outputs with parameters p,q have masses A=(1-p)(1-q), (1-p)q, p(1-q), B=pq. Therefore their conditional total variation is the exact overlap complement

[
f(p,q)=1-min(A,	frac12)-min(B,	frac12).
]

Put u=sqrt(A), v=sqrt(B). Cauchy–Schwarz yields

[
u+v=sqrt{(1-p)(1-q)}+sqrt{pq}le1.
]

Define beta=1/sqrt(2) and alpha=1-beta. We maximize g(u,v)=min(u²,1/2)+min(v²,1/2) on u,v>=0 and u+v<=1. If u>=beta, then v<=alpha and g<=1/2+alpha²; the case v>=beta is symmetric. Otherwise u,v<=beta, so g=u²+v². This convex function reaches its maximum over the polygon u,v>=0, u,v<=beta, u+v<=1 at a vertex, with largest value beta²+alpha²=1/2+alpha². In every case

[
glerac12+(1-1/sqrt2)^2=2-sqrt2,
quad	ext{thus}quad f(p,q)gesqrt2-1.
]

Equality holds for p=q=alpha or p=q=beta (both satisfy equality in the Cauchy–Schwarz step). Keeping BU,j in the full observation makes the exact global error under each source L equal to the sum of the j-atom masses L(BU,j) times f(p_j,q_j). Since L(BU)=1/4 under **both** P and Q, each error is at least (sqrt(2)-1)/4, and choosing all p_j=q_j=alpha attains the bound in both laws. This proves the full simultaneous two-law minimax statement. QED.

**Conditional-calibration corollary.** If the decoder additionally must preserve the physically correct fair marginal of *each* query conditional on BU,j, then p_j=q_j=1/2. For each j, f=1/2; hence the full TV error is exactly 1/8 under P and under Q. This differs from the unrestricted independent-emission optimum, which may bias each marginal to improve the joint-TV objective.

## Theorem 2 — one private persistent bit yields exact adaptive read-only simulation

Upon seeing BU,j, instead draw **one** fair private bit K and retain it. Output K for every request to read the original same leaf bit k. The two-output (O',j_BU,Y1,Y2) distribution then coincides exactly with the physical one under both P and Q, so TV=0.

More generally, for any finite horizon and any **P/Q-common read-only** BU probe kernels W_t(y_t|j,k,a_t,public_history), allow an adaptive controller to choose actions from the observed (O',j_BU) and previous public history. Assume no probe changes the already-realized k or reveals an additional hidden upstream variable. Conditioned on BU,j, physical k is fair under both source laws. Couple the physical k and simulated persistent K to the same fair draw. Inductively apply identical action-selection and readout kernels to equal observed histories; their full joint transcript distributions agree in both laws. This is exact even for adaptive action selection, not a finite-horizon numerical approximation.

Thus a persistent fair private bit (or equivalent shared randomness carried between calls) is sufficient for all these BU-local read-only protocols. By Theorem 1, an online architecture whose successive outputs are conditionally independent given only BU,j cannot reproduce even two same-leaf queries: its best error is positive. This is **an online conditional-memory/consistency result**, not a prohibition on a single batch kernel returning a correlated pair, nor pathwise recovery of the actually realized physical k from j.

## Executed evidence, provenance, and obligations

VERIFY.py was actually executed with Python Fraction/SymPy; stdout is preserved in VERIFY_EVIDENCE.txt. The program reconstructs all original 16 positive P/Q leaves and checks normalization, BU-j masses, exact physical/persistent joint-law equality under both sources, fresh fair single-step calibration error 1/8, symbolic radical identities, and product two-query TV identities for 81 rational (p,q) pairs and both laws, plus j-dependent rational checks. The all-real optimum follows from the analytic Cauchy–Schwarz/convex-polygon argument, **not** from the finite grid.

This note does not establish original post-terminal T4 observability or causal implementability, a changed-k intervention, legality of querying stopped paths, native heartbeat evolution, native X6/slice readout, or a new original-game minimax. The predecessor's hidden-H twenty-leaf action counterexample is an **explicitly different source**. An independent reviewer must inspect the inherited atom semantics and the all-real inequality before admission.

**Frozen source:** PR #1738, 0c973337792efd3affe80647e51f9f23f5bf87b7, research_notes/brc_n4_controlled_t4_hidden_history_20261030_r11/{PROOF.md,VERIFY.py,NEXT_TASK.md}. All new files are author-side portable evidence; GitHub storage is not canonical Source CLAIM/Result/Driver review.

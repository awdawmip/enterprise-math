# R5 — Stratified likelihood-ratio collisions: exact singularity and tangential support gap

Date: 2026-10-28 Asia/Shanghai. Scope: exact finite P/Q sequential statistical observer model. Author-level portable research, **AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED**. Source-native CLAIM, Result and independent Driver review remain separate.

## Frozen source and mathematical question

This run pinned GLOBAL_KNOWLEDGE_V1 at main@cd47c1ecd3ba6262dfa1e96bdd3237251cd942fc and Enterprise Math at main@c5fab90f2bbe1cbe8581cef4179aa532cf040388. Read the account bootstrap/manual, ACTIVE worldview and project P000/X6 joint-observer contracts, task researcher entry, portable-research protocol, and the previous unrestricted six-leaf proof at research_notes/brc_r5_two_upstream_rank4_obstruction_20261028_t11/UNRESTRICTED_PROOF.md. The latter supplies the immutable already-verified original six-leaf support gap; it is not presented as new research.

At t=1 the first observed branch is A or B. At t=2 side branches A,L and B,H stop, while A,C and B,C may stop and declare P, stop and declare Q, or continue to t=3. Terminal declarations are arbitrary. Complete-history behavioral policies can act separately on the two C histories; seedless LR behavioral policies use the same action distribution whenever (t,P(history)/Q(history)) is the same. No persistent shared random seed exists.

Exact strictly positive leaf weights are:

| leaf | P | Q |
| --- | ---: | ---: |
| A,C,low | 1/24 | 1/12 |
| A,C,high | 1/8 | 1/12 |
| A,L | 1/12 | 1/3 |
| B,C,low | 1/32 | 1/8 |
| B,C,high | 7/32 | 1/8 |
| B,H | 1/2 | 1/4 |

Each measure totals 1. The t=1 likelihood ratios are R(A)=1/2 and R(B)=3/2. At t=2 the two C histories both have R=1. The objective observer is

\[
O=(e_P,e_Q,T_P,T_Q)=(P(\mathrm{declare\ Q}), Q(\mathrm{declare\ P}), E_P[\tau], E_Q[\tau]).
\]

For the signed direction \(\lambda=(912,456,128,-194)\), let \(V_\mathrm{full}=\max_\pi \lambda\cdot O(\pi)\) over all complete behavioral policies and \(V_\mathrm{LR}\) over all seedless LR behavioral policies. The original model's exact values are 868 and 857, respectively.

## Theorem: nearby distributions can have incompatible exact information partitions

Fix any real \(\epsilon\) with \(0<\epsilon<1/100\). Make the following perturbations to **Q only**, leaving all P leaf masses unchanged:

* **Tangential family T(epsilon)**: increase Q(A,C,low) by epsilon and decrease Q(A,C,high) by epsilon.
* **Transverse family X(epsilon)**: increase Q(A,C,low) by epsilon and decrease Q(A,L) by epsilon.

Both changes preserve strict positivity and normalization; each has Q total-variation distance exactly epsilon from the original distribution. They have sharply different exact observable behavior:

\[
V_\mathrm{full}(T(\epsilon))=868,\qquad
V_\mathrm{LR}(T(\epsilon))=857+456\epsilon,\qquad
\Delta(T(\epsilon))=11-456\epsilon>0.
\]

In contrast, for **every** \(0<\epsilon<1/100\),

\[
\mathcal O_\mathrm{full}(X(\epsilon))
=\mathcal O_\mathrm{LR}(X(\epsilon))
\]

as **actual** reachable subsets of \(\mathbb R^4\), not merely as convex hulls. Thus \(\Delta(X(\epsilon))=0\) for this and every other signed objective. Both input families tend to the same original model as \(\epsilon\to0^+\), whereas the tangential gap tends to 11 and the transverse gap stays 0. Therefore the compression-support gap is discontinuous across a likelihood-ratio signature collision, even among strictly positive leaf masses.

### Proof of the tangential formula

The collision at t=2 persists because the aggregate C masses P(A,C)=Q(A,C)=1/6 and P(B,C)=Q(B,C)=1/4 are unchanged. For our \(\lambda\), a time-3 leaf of masses (p,q) contributes \(384p-126q\) if declared P and \(1296p-582q\) if declared Q. The latter is preferable iff \(p/q>1/2\).

For epsilon>0 the altered A,C,low terminal ratio is \(1/[2(1+12\epsilon)]<1/2\), so declare P there; A,C,high has ratio \((3/2)/(1-12\epsilon)>1/2\), so declare Q. The change in the A,C continuation score is
\[
(-126)\epsilon+(-582)(-\epsilon)=456\epsilon.
\]

The pre-collision optimal t=1 immediate stopping scores are A=163, B=683, and the side-branch t=2 stopping scores are A,L=44, B,H=487. The shared t=2 C action table, after terminal declaration optimization, is:

| C action | A,C continuation contribution | B,C contribution | whole-tree LR optimum |
| --- | ---: | ---: | ---: |
| stop P | 54 | 81 | max(163,44+54)+max(683,487+81) = 846 |
| stop Q | 130 | 195 | max(163,44+130)+max(683,487+195) = 857 |
| continue | 119+456epsilon | 207 | max(163,44+119+456epsilon)+max(683,487+207) = 857+456epsilon |

Since epsilon>0, the last row is maximal. The complete-history policy can independently use C=stop Q after A and C=continue after B. Since \(119+456\epsilon<130\) for epsilon<1/100, complete-history optimum remains \(174+694=868\).

Every information set is visited at most once. The expected objective is multi-affine in independent local action probability vectors, so its maximum on the product of finite action simplexes is attained at deterministic vertices. The Bellman values hence hold for **all real behavioral randomizations**, not just grid samples. This proves the tangential formula.

### Proof of transverse equality and the discontinuity

In X(epsilon) the four t=2 histories have exact likelihood ratios
\[
R(A,L)=\frac1{4(1-3\epsilon)},\quad
R(A,C)=\frac1{1+6\epsilon},\quad
R(B,C)=1,\quad R(B,H)=2.
\]
They are pairwise distinct throughout the stated interval. The four t=3 C leaves have respective ratios
\[
\frac1{2(1+12\epsilon)},\quad \frac32,\quad\frac14,\quad\frac74,
\]
again pairwise distinct, while the two t=1 histories were already distinct. Thus every available complete-history information state has a unique time-likelihood-ratio signature. Given any complete-history behavioral strategy, define its seedless LR action law at each signature to equal the complete-history law at its unique history. This matches all path probabilities and observable distributions exactly. The reverse inclusion is immediate, proving equality of **true** image sets.

Each perturbation transfers mass epsilon between exactly two Q leaves, hence \(\|Q_\epsilon-Q_0\|_1=2\epsilon\) and TV(Q_epsilon,Q_0)=epsilon; P is fixed. The formulas just proved give the distinct limiting gaps. QED.

## Auxiliary fixed-partition Lipschitz bound

For the same finite tree, the **same LR information partition**, and two normalized leaf pairs (P,Q),(P',Q'), define \(V_C\) for either complete-history or LR class C. In the present direction the P per-leaf contribution coefficient lies between 128 and 1296; the Q coefficient lies between -582 and 262. Since each measure's perturbation sums to zero,

\[
|V_C(P',Q')-V_C(P,Q)|
\le584\,\|P'-P\|_1+422\,\|Q'-Q\|_1.
\]

Indeed, for any zero-sum \(\delta_i\) and \(a_i\in[m,M]\), \(|\sum\delta_i a_i|\le(M-m)\|\delta\|_1/2\); then taking suprema over an unchanged policy set preserves the bound. Consequently

\[
|\Delta'-\Delta|
\le1168\,\|P'-P\|_1+844\,\|Q'-Q\|_1.
\]

For T(1/10000), this gives \(\Delta\ge13539/1250\). The exact Bellman value \(\Delta=13693/1250\) is stronger. This bound cannot be exported to X because the LR decision partition changes.

## Reproducibility and evidence

The attached VERIFY.py uses only Python 3 standard-library Fraction and itertools. It checks positivity, normalization, the **exact** signature-partition collision structure at t=1,2,3 and all finite deterministic policies for the original and the two rational epsilon=1/10000 instances. The unrestricted complete-history enumeration has \(3^2 3^2 2^2 2^4=5184\) descriptions; the LR enumeration has 1728 descriptions when the C signature collides and 5184 when it splits.

Exact results:

| model | distinct complete O | distinct LR O | max complete | max LR | gap |
| --- | ---: | ---: | ---: | ---: | ---: |
| original | 196 | 124 | 868 | 857 | 11 |
| T(1/10000) | 196 | 124 | 868 | 1071307/1250 | 13693/1250 |
| X(1/10000) | 196 | 196 | 1084943/1250 | 1084943/1250 | 0 |

The transverse **deterministic** point sets were compared for exact equality. For behavioral policies the preceding explicit signature relabeling proof supplies the all-real result. This verifier's local-execution Git blob is 79deaeef95aa1d17909d8b1dcc8f713aec626f2f; its output Git blob is 53761bbb449f174103231d561617de7a786c0ef8. EXACT_OUTPUT.txt ends with ALL EXACT STRATIFIED COLLISION CHECKS PASSED.

## BRC, X6 and literature boundaries

The project P000 remains native six-axis discrete X6 Cell space plus independently typed time, not a native plane. The finite P/Q histories can be injectively labeled by chart-relative X6 Cell identities with separately recorded decision time; this is a typed **observer-label** bridge, not a claim that these statistical transitions are primitive X6 movement or heartbeat dynamics. Compression (history,t) -> (t,P/Q) erases branch provenance and is certified only for declared observables and downstream decisions. The BRC positive rational branch substrate (definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json at project input revision) supplies the distinction between explicit positive branch masses/histograms and reduced totals. Applied here: retain six labeled P/Q weights and grouped-prefix aggregations before quotient. The signed support vector is a decision functional, **not** a signed BRC branch weight; no native BRC-Shor numerical engine is claimed to have run.

Related external background, not used to establish this new finite proof: Blackwell-Sherman-Stein comparison of statistical experiments, discussed in Buscemi (2010), https://arxiv.org/abs/1004.3794; perfect-recall behavioral vs mixed strategies, discussed in Aryal and Stauber (2014), https://arxiv.org/abs/1408.1022; more recent imperfect-recall game optimization work Zheng, Sim, and Varvitsiotis (2026-02-25), https://arxiv.org/abs/2602.21722. This author proof has not undergone a full prior-art/novelty review.

## Next discriminating task

Search **within fixed LR-collision strata**, not generic unconstrained perturbations. Construct a different strictly positive rational two-upstream collision tree. Use exact Bellman common-action upper envelopes and a rational all-signed-support cone/LP certificate to establish equality of the complete and compressed **convex hulls** first; only then prove some convex-hull point unreachable by all real seedless behavioral parameters. An exact separating signed lambda is an elimination certificate. Preserve P000 observer typing, model positivity, prefixes, authorship and Source task ownership. Owner/CLAIM/native Result/independent Driver judgment remain to be verified through the native project authority.

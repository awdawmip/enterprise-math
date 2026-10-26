# EC48G — Exact two-memory ROC-region preservation for two future labels

**Status:** AUTHOR-SIDE MATHEMATICAL PROOF + TWO INDEPENDENT EXACT CHECKS. Not a native Source Result, independent Driver judgment, Working Truth, Foundation promotion, or native X6/Heartbeat dynamics claim. Date: 2026-10-27.

## 0. Reused source and ontology, with exact scope

GLOBAL_KNOWLEDGE_V1 canonical read pinned for this run: \`awdawmip/chatgpt-global-knowledge@ce56f544d74dc20cecea53a8607e752b2e8c8e9c\`, including \`00_BOOTSTRAP.md\`, \`OPERATING_MANUAL.md\`, \`projects/enterprise-math/00_EM_PROJECT_BOOTSTRAP.md\`, \`P000_REALITY_FOUNDATION.json\` (Git blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\` matched \`P000_STARTUP.json\`), and ACTIVE \`我眼中的世界.md\`. Enterprise Math Source read pinned at \`08b420939c4e5e27bc431cbbf4bcb17a3403e9bc\`, including \`AGENTS.md\`, \`docs/PORTABLE_RESEARCH_PROTOCOL.md\`, the Heartbeat X6 contract, weighted BRC substrate and joint-observer-preservation contract. Reused the verified [EC48E single-tied-history theorem](https://github.com/awdawmip/enterprise-math/blob/629ff0645c1c43285cd9fa0dcdb44403117a23c1/research_notes/r4_ec48e_single_tied_history_20261027/EC48E_SINGLE_HISTORY_TIE_THEOREM.md), the [EC48E one-tied-future-column theorem](https://github.com/awdawmip/enterprise-math/blob/5102f4644ff0bcd989f3b76039e28bbdc254789c/research_notes/r4_ec48e_single_column_20261027/EC48E_SINGLE_COLUMN_TIE_THEOREM.md), and the [EC48F microscopic-kernel-versus-ROC witness](https://github.com/awdawmip/enterprise-math/blob/02d14f547bbdedba764e10abb617d07f5b022b39/research_notes/r4_ec48f_kernel_vs_roc_20261027/EC48F_KERNEL_VS_ROC_THEOREM.md).

These are **auxiliary finite positive-source BRC** observations with history-provenance preserved until an observer-relative quotient is explicitly proved safe. Binary future labels are *not* two native spatial dimensions. P000's six-dimensional native Cell space, three-dimensional restricted slice, and separately typed time are unchanged. No native dynamical transfer is asserted.

## 1. Model and exact theorem

Let \`H\` be an arbitrary nonempty finite set of histories, and \`Y={1,2}\` be exactly two future-visible labels. Let \`p(h,y),q(h,y)>0\` be independently normalized joint laws. After observing \`h\`, an encoder uses only private randomness to select one of \`K\` memory labels with probabilities \`pi_h(m)\`. After observing \`y\`, decoder \`u_m(y) in [0,1]\` declares hypothesis P. No persistent public random seed is allowed:

\[
w(h,y)=\sum_{m=1}^{K}\pi_h(m)u_m(y),\qquad
(\alpha,\beta)=\left(\sum_{h,y}p(h,y)w(h,y),\sum_{h,y}q(h,y)w(h,y)\right).
\]

Let \`S_K\` be the attainable pair region, and \`Z=\sum_{h,y}[0,(p(h,y),q(h,y))]\` the complete-history zonotope. Put \`K_hull=min{K:conv(S_K)=Z}\` and \`K_seed=min{K:S_K=Z}\`. The constant-depth four-observer readout is \`(1-alpha,beta,2,2)\`, not a variable-stopping-depth result.

**Theorem EC48G.1.** For every such finite, strictly positive two-future-label experiment,

\[
\boxed{K_{\mathrm{hull}}\le 2\quad\Longrightarrow\quad K_{\mathrm{seed}}=K_{\mathrm{hull}}.}
\]

Consequently, a counterexample to the general implication \`conv(S_K)=Z => S_K=Z\`, *if one exists with two future labels*, must have \`K_hull>=3\`. Unlike EC48E's sufficient conditions, **this theorem permits arbitrary cross-history and cross-column likelihood-ratio collisions**, provided the global hull capacity is at most two.

## 2. A two-label support-face reconfiguration lemma

Fix any critical likelihood ratio \`r>0\`. Put \`d(h,y)=p(h,y)-r q(h,y)\` and define the two binary words

\[
b_h(y)=\mathbf1[d(h,y)>0],\qquad
a_h(y)=\mathbf1[d(h,y)\ge0].
\]

Write \`B={b_h:h in H}\` and \`A={a_h:h in H}\`. Each row satisfies \`b_h<=a_h\` **coordinatewise**. EC47/EC48A's exact vertex-signature argument gives \`|A|,|B|<=K_hull\`: the all-ties-zero and all-ties-one words are the generic support-signature collections immediately above and below the ratio r.

**Lemma.** If \`Y={1,2}\` and \`|A|<=2, |B|<=2\`, there is a continuous, coordinatewise nondecreasing family \`w_t(h,y)\` (\`0<=t<=1\`), joining \`w_0=b\` and \`w_1=a\`, such that **every family member has a private two-memory encoder/decoder factorization**. All coordinates strict at r stay fixed.

The proof is constructive. View a decoder row as a point of the binary square \`{00,01,10,11}\` or its convex hull.

### Case I: A and B share a word

Choose \`c in A cap B\`. There are at most one other word in each set; call them \`b in B\\{c}\` and \`a in A\\{c}\`, using \`b=c\` or \`a=c\` when the respective difference is empty.

Hold one decoder row fixed at \`c\`, and use the other decoder row \`d\` in **three successive continuous stages**:

1. Hold \`d=b\`. Move all histories of type \`b -> c\` from \`b\` to \`c\` by varying their *private encoder weights* on the two decoder rows. Histories of type \`b -> a\` stay at \`b\`; those of type \`c -> a\` stay at \`c\`; \`c -> c\` remains fixed.
2. Move \`d=(1-s)b+s a\`, \`0<=s<=1\`. Histories \`b -> a\` follow \`d\` deterministically; the other histories remain at their completed or pending row \`c\`.
3. Hold \`d=a\`. Histories of type \`c -> a\` move from \`c\` to \`a\` by private encoder interpolation. Previously completed histories stay at \`c\` or \`a\`.

Every history pair belongs to one of the four types \`c->c\`, \`b->c\`, \`b->a\`, \`c->a\`; when a chosen endpoint coincides with c, any consistent duplicate-type assignment works. On each history's actual transition its lower/upper binary words are comparable. Therefore the constructed path is coordinatewise nondecreasing, stays in the permitted rowwise box \`[b_h,a_h]\`, and never touches strictly signed coordinates. At a stage transition, the induced **kernel** is continuous even if the encoder parametrization changes. At most two decoder states are used throughout.

### Case II: A and B are disjoint

If \`|B|=1\`, say \`B={b}\`, assign one decoder to each \`a in A\` (at most two), move that row from \`b\` to \`a\` via \`d_a(s)=(1-s)b+s a\`, and let each history encode to its own upper-word's decoder. This implements \`w_s=(1-s)b_h+s a_h\`. If \`|A|=1\`, use the symmetric construction, one decoder for each distinct lower word.

The only remaining case is \`|A|=|B|=2\` with \`A cap B=empty\`. Since every lower endpoint \`b_h\` has some coordinatewise greater/equal upper endpoint, \`11\` cannot belong to \`B\` (it would force \`11 in A\`); likewise \`00\` cannot belong to \`A\`. The two sets partition the four square corners; a lower set \`{01,10}\` would force \`A={00,11}\`, impossible because \`00 notin A\`. Hence, up to exchanging the future labels, necessarily

\[
B=\{00,01\},\qquad A=\{10,11\}.
\]

The permitted distinct history transitions are precisely \`00->10\`, \`01->11\`, \`00->11\`. Choose two decoder rows

\[
d_0(s)=(s,0),\qquad d_1(s)=(s,1).
\]

Use \`d_0\` for \`00->10\`, \`d_1\` for \`01->11\`, and private encoding weights \`(1-s,s)\` between these decoders for \`00->11\`. The latter induces \`(s,s)\`; therefore *every tied coordinate increases continuously from zero to one* and all strictly signed coordinates are respected. In the symmetric \`B={00,10}, A={01,11}\` case use \`d_0=(0,s),d_1=(1,s)\`. These exhaustive cases prove the lemma. □

## 3. Entire ROC region, including the one-memory boundary

At each r, \`w_t\` remains optimal for \`alpha-r beta\`: negative-gain entries stay zero, positive-gain entries stay one, and tied entries may change. Let \`Q_r=sum_{d(h,y)=0}q(h,y)>0\`. Since every tied coordinate evolves monotonically and the endpoints are all-zero/all-one, the tied mass

\[
T(t)=\sum_{d(h,y)=0}q(h,y)w_t(h,y)
\]

is continuous and runs through **every** value in \`[0,Q_r]\`. All tied generators share the slope r. Thus the entire exposed support edge \`F_r\` of the complete-history zonotope lies in \`S_2\`. This holds for every breakpoint when \`K_hull=2\`.

All remaining zonotope support vertices correspond to noncritical strict-sign profiles and are realizable with K_hull states; opposite edges follow by decoder complementation \`u->1-u\`. \`S_2\` is star-shaped about \`(0,0)\`, because multiplying every decoder entry by \`c in [0,1]\` multiplies the readout by c. Any point in compact convex Z lies on a radial segment from 0 to its boundary. Hence \`Z subseteq S_2\`, and \`S_2 subseteq Z\` always: \`K_seed=2\` when \`K_hull=2\`.

If \`K_hull=1\`, then at every noncritical r, the strict-sign words must be equal across **all** histories. Consequently, for each fixed future label y, all likelihood ratios \`p(h,y)/q(h,y)\` are identical as h varies; otherwise a generic r between two distinct ratios would distinguish two histories' words. Any full kernel w can therefore be aggregated separately within each y to the Q-weighted mean \`v(y)=sum_h q(h,y)w(h,y)/sum_h q(h,y)\`. The same \`v(y)\` preserves alpha as well as beta, giving a one-memory realization of all Z. Thus \`K_seed=K_hull=1\`. □ Theorem EC48G.1.

## 4. Explicit cross-column multi-history collision witness

Take \`H={1,2,3}\`, \`Y={1,2}\` and positive raw masses

\[
P_\mathrm{raw}=\begin{pmatrix}2&1\\2&4\\2&2\end{pmatrix},
\qquad
Q_\mathrm{raw}=\begin{pmatrix}2&2\\2&2\\2&2\end{pmatrix},
\quad p=P_\mathrm{raw}/13,\;q=Q_\mathrm{raw}/12.
\]

The likelihood ratios are \`6/13,12/13,24/13\`. Across the generic open intervals, the number of distinct strict-sign history words is \`1,2,2,1\`. Thus \`K_hull=2\`. At \`r=12/13\`, the tied cells are \`(1,1),(2,1),(3,1),(3,2)\`: **different histories and both future-label columns tie simultaneously**. The two sides have \`B={00,01}\` and \`A={10,11}\`, the hard disjoint case in the lemma.

For all \`s in [0,1]\`, the two decoders \`u_0=(s,0)\`, \`u_1=(s,1)\`; history 1 encodes to decoder 0, history 2 to decoder 1, and history 3 uses private encoder weights \`(1-s,s)\`. Hence

\[
W_s=\begin{pmatrix}s&0\\s&1\\s&s\end{pmatrix},
\quad
\alpha_s=\frac{4+8s}{13},\qquad
\beta_s=\frac{2+8s}{12},\qquad
\alpha_s-\frac{12}{13}\beta_s=\frac{2}{13}.
\]

The entire support edge with \`beta in [1/6,5/6]\` is thus exactly covered with two memory states. This is a substantive cross-column collision not covered by the single-tied-column theorem.

## 5. Verification, repeatability and open boundary

The proof above is all-finite-alphabet; it is **not** extrapolated from testing. Exact independent Python \`fractions.Fraction\` execution and JavaScript denominator-7 integer execution enumerate **all 66,429 ternary sign templates** with 1..5 histories, two future labels; 6,529 have a tie and at most two one-sided words on each side. Both check 89,685 sampled policy factorizations, 840,030 cell-level bounds, 501,260 forced strict-profile cells and 17,937 monotone path stages, with all tests PASS. In that declared *finite* sign-template domain, the coverage is exhaustive; the continuum path claims follow from the displayed algebraic construction, not only sampled points. The JS checker is stored as \`EC48G_VERIFY.js\` and its JSON statistics as \`EC48G_REPORT.json\`.

No claim is made for \`K_hull>=3\` with two labels or for \`Y>=3\`. No sign/phase cancellation, physical measurement, native BRC heartbeat runtime, X6 dynamics, or independent formal/Driver review was performed. This is an **observer-relative** ROC result: EC48F shows that preserving an entire microscopic decision kernel can require more memory.

BRC classification: \`REUSE_APPLIED\` to EC47/EC48A strict-sign profiles and EC48B/C support-face formalism; \`COMPOSE_APPLIED\` to EC48E/F endpoint reconfiguration; \`EXTEND_EXISTING_TOOL\` for the exact sign-template validator. The new certificate is the three-stage two-decoder construction plus the finite Boolean-square classification.

GitHub actor \`awdawmip\` has project admin/push, but native task/owner query returned \`CONTROL_QUOTA\` and session start \`STATIC_READONLY_SCOPE_DENIED\` (\`operation_sent=false\`). This is a **locally registered author-side** mathematical draft with no verified active Task owner, Source CLAIM, native Result, independent Driver review or Foundation acceptance.

**Next EC48H:** classify the remaining \`K_hull=3, |Y|=2\` support faces. Either prove an at-most-three-decoder face-reconfiguration lemma (which, with the present theorem and trivial \`K_hull=4\` case, would settle all two-label models), or find positive integer P,Q with a fully certified missing face interval using the EC48C exact encoder-quotient graph. For higher Y, seek multi-column collision hypergraphs that defeat any fixed K decoder-bank path. Preserve original microscopic provenance if additional observers require it.


# R762GB — Invariant signed-gate universality and the limit of oriented-triad observations

Date: 2026-11-19. Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`.
Status: **AUTHOR_PROVED / EXACT_FINITE_CHECK_PASS / NOT_REVIEWED**.

## Frozen source and dependencies

P000 triadic-balance definition and signed X6 Cell torsor from immutable task input `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; taskbook `research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md@857280d1012943290d141d1317179c40ec3cbdf8`. Reuses the author-side signed-orbit classification R762GA, Draft PR #2804@677da5651ec753c90d21c032c234963da6ad2a59, and the unsigned candidate BRC kernels R762FV–FY. No present statement is a native `TRIADIC_CLOSURE_E` permission result.

## Domain

Let (X) be a nonempty transitive finite (G)-set of oriented 3-cycles (cyclic rotations of ((i,j,k)) identify the same cycle; inversion does not). Let (Y={(g,s):gin X, s:operatorname{supp}(g)	o{+1,-1}}) be the signed metadata bundle. Let (G) transport the positive-axis labels, cycles and their attached signs as in R762GA. (pi:Y	o X), (pi(g,s)=g), forgets only sign metadata. Positive-rational BRC weights (w_yge0), (sum_{yin Y}w_y=1), are invariant when (w_{gamma y}=w_y) for every (gammain G).

The three **separately typed** cases are:
- Full unframed (S_6), (|X|=40, |Y|=320), four signed orbits with sizes 40,120,120,40.
- Fixed K4 four-STAR frame, (G=S_4), (|X|=8, |Y|=64), four signed orbits 8,24,24,8.
- Fixed K4 frame with one excluded STAR, (G=S_3), (|X|=6, |Y|=48), eight signed orbits, each size 6.

### Theorem 1: invariant signed gates have the same oriented marginal

For **every** invariant normalized nonnegative weight (w) (including normalization of any nonempty union of signed orbits),

[
oxed{sum_{substack{yin Y\ pi(y)=g}}w_y=rac1{|X|}quad	ext{for every }gin X.}
]

**Proof.** The pushforward weight (p(g)=sum_{pi(y)=g}w_y) satisfies
(p(gamma g)=sum_{pi(y)=g}w_{gamma y}=p(g)) by equivariance of (pi) and invariance of (w). Transitivity of (G) on (X) forces (p) to be constant, and normalization forces the displayed value. QED.

This is a statement about **positive BRC branch metadata and a deliberately declared sign-forgetting observer**. It is stronger than the equal-orbit-weight special case: arbitrary relative positive masses among distinct signed orbits give the same oriented marginal.

### Corollary 1: every nonempty Boolean invariant gate is invisible to this observer

An invariant Boolean legality *candidate* (a:Y	o{0,1}) is a union of full signed orbits. There are 15 nonempty gate choices for the full (S_6) case, 15 for fixed (S_4), and 255 for marked (S_3). With uniform BRC weight on permitted signed branches, the exact number of permitted decorations over **each oriented cycle** is, respectively,

[
m_J=sum_{jin J}inom3j,quad
m_J=sum_{jin J}inom3j,quad
m_M=|M|,
]

where (Jsubseteq{0,1,2,3}) and (M) is a nonempty subset of the eight marked-frame orbit labels. In each case (m>0), and every oriented cycle has probability (1/|X|).

In particular, no experiment that reads only the oriented 3-cycle can identify which of these invariant sign gates was used. For marked frames, even eight distinct signed-orbit categories collapse to the same uniform six-branch marginal.

### Corollary 2: inherited candidate reachability and exact mixing

Assume each permitted decorated branch ((g,s)) acts on the **oriented permutation state only** by the same unsigned update (umapsto gu), regardless of (s). Assume fresh independent sampling of a fixed invariant normalized kernel at each step. The law of the entire oriented word ((g_1,ldots,g_h)) and every derived endpoint (g_hcdots g_1u) is **identical** to the pre-existing unsigned uniform-(X) BRC walk, at every depth (hge0).

**Proof.** Theorem 1 gives the per-step oriented law uniformly on (X). Independence makes every oriented word have probability (|X|^{-h}). The endpoint is a deterministic function of the oriented word; pushforward preserves equality of laws. QED.

Consequently, under these declared assumptions, every nonempty invariant sign gate on all 40 oriented cycles inherits the R762FV–FW (A_6) candidate reachability/mixing statements; every such gate on the 8 four-STAR branches inherits R762FX; every such gate on the 6 retained three-STAR branches inherits R762FY. **This is a conditional inheritance, not a new native authorization or a claim that the actual Cell/Link/Port update is sign-blind.**

For *uniform* sampling of a nonempty Boolean gate with exactly (m) allowed decorations over every orientation, each specified oriented word of length (h) has exactly (m^h) distinct signed source-decorated lifts. Therefore the full typed branch-word count is ((|X|m)^h), while the unoriented-sign-forgetting word count is (|X|^h). Under the uniform product distribution the conditional number of sign words given an oriented word is exactly (m^h). These are exact **source/provenance** counts, not a claim that these histories can safely be erased for future native experiments.

### Proposition 2: averaging frame identity preserves the 40-branch marginal

There are exactly 30 (S_6)-transported K4 four-STAR frames, each with eight oriented branches. Every oriented 3-cycle occurs in exactly (30cdot8/40=6) frames. There are 120 transported *marked* frames, each with six retained oriented branches, and every oriented cycle occurs in exactly (120cdot6/40=18) marked frames.

Uniformly averaging frames after applying **any fixed equivariant within-frame signed kernel** gives probability (6/(30cdot8)=1/40), respectively (18/(120cdot6)=1/40), for each oriented 3-cycle. Frame and mark identity must remain as BRC provenance whenever future questions inspect them.

**Proof.** The (S_6) action is transitive on both frame families and on oriented cycles. Every transported frame carries the same within-frame transitive invariant oriented law by Theorem 1. Hence cycle-incidence counts are constant; double counting pairs (frame, oriented branch) gives 6 and 18 and yields the stated probabilities. QED.

## Sharp boundary: signed native updates can distinguish identical marginals

Let a *candidate* signed-coordinate action on (mathbb Z^6) be (U_{g,s}=D_sP_g), where (P_g) permutes the three selected signed-axis coordinates by (g), leaves the others fixed and (D_s) independently multiplies the **output** moved coordinates by the attached sign. Consider (g=(0,1,2)), input (z=e_0), and two decorations (s_+=(+,+,+)) and (s_-=(+,-,+)). They have the **same** oriented branch (g), but (U_{g,s_+}(e_0)=+e_1) and (U_{g,s_-}(e_0)=-e_1). Thus a sign-sensitive Cell observer distinguishes the two immediately.

Theorem 1 alone cannot justify erasing sign, source, carrier frame, Port, Link, history, or incidence from a genuine native state. Such an erasure requires an actual future-observer descent certificate. The candidate (D_sP_g) action is a mathematical counterexample showing the hypothesis boundary, **not a claim that it has been admitted as a P000 physical update**.

## Exact finite checker and evidence

Companion files: `R762GB_VERIFY.py`, `R762GB_EVIDENCE.json`. The integer-only Python checker constructs all 320/64/48 typed states, enumerates all 720/24/6 symmetries and their exact orbit partitions, and exhausts all 15/15/255 nonempty invariant Boolean gates. It checks exact equality of every oriented marginal fibre, all 30/120 transported frame incidences and the explicit signed-coordinate observer-loss counterexample. Output: `PASS`, with no numerical tolerances. General invariant-weight and all-depth statements follow from the preceding proofs, not solely the finite tests.

Review: **NOT_REVIEWED**. GitHub publication does not imply canonical mathematical adoption.

## Next discrimination

Extract from the frozen native Cell/Link/Port records whether the legality gate is really equivariant under the chosen (S_6)/(S_4)/(S_3) action, and whether its effect updates only the unsigned orientation or also signed coordinates/incidence/source. A single permitted sign-sensitive transition is enough to separate orientation-only equivalence from future-native equivalence. Then calculate the genuine typed observation partition and retain all BRC provenance needed by that partition.

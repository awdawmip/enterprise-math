# R5 — Finite-horizon BRC occupation coupling for seedless likelihood-ratio compression

Author-side proof, 2026-10-27; mathematical status: derived, exact finite check, independent review pending. Object: **external** strictly positive two-measure finite observation trees; there is no claimed P000 native X6 propagation/physical calibration.

## Frozen basis, provenance and BRC reuse

Global read snapshot: `awdawmip/chatgpt-global-knowledge@a4cb0f12f564f73b484c63bd589a69189bb67edb`. The mandatory entry documents, original P000 V4, ACTIVE worldview, math/code policies, and project TASK route were read at this same verified immutable GitHub ref. Source research input: prior 14-leaf theorem at `awdawmip/enterprise-math@001527142eb56a89ab1330fd443b8f1edf0c672a:research_notes/brc_n3_weak_strong_lumpability_gap_20261027_r5/PROOF.md`; this result reuses its explicit rational tree and already-proved full/seedless Bellman gap.

Portable project protocol: `docs/PORTABLE_RESEARCH_PROTOCOL.md`. BRC method reuse: `T0_BRC` **REUSE_APPLIED** to positive rational branch masses, retained path/hidden-history labels, exact P/Q mass conservation, and likelihood-ratio occupancy. The registered `T0_BRC_AFFINE_EFFECT_TRANSPORT` executable has a degree-two moment lease that explicitly excludes occupancy and threshold observers; no execution of that subtool is asserted. Python `fractions.Fraction` runs the new exact example audit; the general proof is algebraic. The maximal-coupling identity for total variation is classical; reference: *Stochastic Processes: Markov chains*, §9.2, Theorem 9.2, https://luc-umass.github.io/html/Markov.html.

P000 research semantics: native Heartbeat World has six discrete X6 spatial dimensions and separately typed time. Here `h` is an **auxiliary external** branch history, sampling index `t` is not established as Heartbeat time, and likelihood ratio is not an X6 coordinate. A Cell/path-to-statistical-tree bridge and observer/future-operation preservation are needed before any native-space interpretation.

## Model and exact observer

Fix an observation tree of finite horizon `N`, with strictly positive physical node masses `Q(h),P(h)`, normalized at the root, and `r(h)=P(h)/Q(h)`. Along physical children `h'\succ h`:

\[
\sum_{h'\succ h}Q(h')=Q(h),\qquad
\sum_{h'\succ h}Q(h')r(h')=Q(h)r(h).
\]

A full-history behavioral policy `π` has separate nonnegative `(D_P,D_Q,C)` action probabilities summing to one at each nonterminal history, with compulsory stop/decide at level N. A seedless behavioral policy uses one shared local action distribution per class `g=(t,r)`, using only fresh local randomization and no persistent random seed. The declared observation is

\[
O(\pi)=\big(P_\pi(\mathrm{decide}\ Q),Q_\pi(\mathrm{decide}\ P),
 E_{P,\pi}\tau,E_{Q,\pi}\tau\big).
\]

For any nonterminal physical history h, its next LR kernel on the finite set of next LR values is

\[
K_h(s)=\sum_{h'\succ h:\ r(h')=s}Q(h')/Q(h).
\]

For a coarse class `g=(t,r)`, retain its physical hidden-kernel diameter

\[
\delta_g=\max_{h,h'\in g}\mathrm{TV}(K_h,K_{h'}),\quad
\mathrm{TV}(u,v)=\tfrac12\sum_s|u(s)-v(s)|.
\]

When branch weights are rational, every `δ_g` is an exactly computable rational, requiring no enumeration of real-valued policy probabilities.

## Theorem — exact construction and quantitative error transport

Let π be **any** full-history behavioral policy, including arbitrary real local randomization. Let `m_π(h)` be the Q alive-arrival mass at physical node h, and for each g define

\[
m_\pi(g)=\sum_{h\in g}m_\pi(h),\quad
A^a_\pi(g)=\sum_{h\in g}m_\pi(h)\pi(a\mid h),\ a\in\{D_P,D_Q,C\}.
\]

Construct a seedless LR policy σ at every reached g by

\[
\boxed{\sigma(a\mid g)=A^a_\pi(g)/m_\pi(g).}
\]

Use an arbitrary valid action at zero-π-occupation classes. Write `q^C_π(g)=A^C_π(g)` and

\[
B_{\rm diam}(\pi)=\sum_{t=0}^{N-1}\sum_{g\text{ at }t}q^C_\pi(g)\delta_g,
\quad M=\max_{h}r(h),\quad b=\min\{1,B_{\rm diam}(\pi)\}.
\]

**For all such π, the constructed σ simultaneously obeys**

\[
\boxed{
\begin{aligned}
|e_P(\sigma)-e_P(\pi)|&\le M b,\\
|e_Q(\sigma)-e_Q(\pi)|&\le b,\\
|E_{P,\sigma}\tau-E_{P,\pi}\tau|&\le MN b,\\
|E_{Q,\sigma}\tau-E_{Q,\pi}\tau|&\le N b.
\end{aligned}}
\]

An improved **policy-specific** certificate replaces `B_diam` by

\[
\boxed{B_{\rm pair}(\pi,\sigma)=
\sum_{t,g}q^C_\pi(g)\mathrm{TV}(K_g^\pi,K_g^\sigma)
\le B_{\rm diam}(\pi),}
\]

where `K_g^π` is the continuation-Q-mass-weighted mixture of physical `K_h` among histories at g under π; `K_g^σ` is defined analogously under σ. Use `b=min(1,B_pair)` in the same four bounds.

### Proof

**(1) Validity.** The action Q masses `A^a_π(g)` sum to `m_π(g)`, so σ is a valid local probability distribution. Its state is only (t,r); each random action is fresh and never requires knowing hidden h.

**(2) Marginal Markovization.** At each positive-mass g, aggregate the Q occupation and action masses of π. Their conditional action law is exactly σ by definition. Conditional on continue, the next LR class follows `K_g^π`, the appropriate occupied-history mixture. This produces a finite, inhomogeneous, stopped Markov-class process with exactly the same level-by-level stopping/decision/(t,r) marginals as π. In particular its terminal readout `(τ,r_τ,decision)` has the same law. The actual σ process has the same local action law and transition kernel `K_g^σ`.

**(3) Coupling.** Couple the two class processes at the common root. Whenever alive at the same g, draw **the same** action from σ. For a common continue at g, use a maximal coupling of the two next-LR kernels, with mismatch probability precisely `TV(K_g^π,K_g^σ)`. A common stop gives identical final readouts.

**(4) First-disagreement bound.** The probability of staying equal until t and continuing from g is at most the π-process unconditional continuation Q mass `q^C_π(g)`. The union over first disagreements gives
`Pr_Q[terminal readouts differ] ≤ min(1,B_pair)`.
Both policy-specific conditional kernels are convex mixtures of the same physical `{K_h:h∈g}`; joint convexity/triangle inequality of TV bounds their distance by the maximum pairwise diameter `δ_g`. Hence `B_pair≤B_diam`.

**(5) Four readouts.** For any coupled terminal readouts with disagreement probability at most b, the expectations of every function `f∈[0,R]` differ by at most `Rb`. The four observable functions under Q are `r_τ·1_{decide Q}`, `1_{decide P}`, `r_τ·τ` and `τ`, with respective ranges `[0,M]`, `[0,1]`, `[0,MN]`, `[0,N]`. The P formulas hold exactly because under an identical history-dependent action rule `P(h)=r(h)Q(h)` at each stopped history. The bounds follow. **QED.**

Corollary: if every physical class has `δ_g=0`, σ reproduces all four coordinates exactly for every full π; thus `O_full=O_seedless` (reverse inclusion is automatic). This recovers the earlier *strong lumpability sufficiency*, and gives a quantitative policy-dependent extension for arbitrary finite N. It is a constructive outer-approximation certificate, **not** an exact policy-image Hausdorff distance or a convexity theorem.

## Exact 14-leaf calculation (reused physical model)

The root has `Q(a)=1/3,r(a)=2`, `Q(b)=2/3,r(b)=1/2`. Each of a,b branches to `u,v,w` with Q conditional masses `(1/8,1/8,3/4)`. LRs are `(1,1,7/3)` after a, and `(1,1,1/3)` after b. Each `h∈{au,av,bu,bv}` has terminal LR outcomes `(1/2,1,3/2)` with conditional Q law `K_h=(s_h,1−2s_h,s_h)` and `(s_au,s_av,s_bu,s_bv)=(1/10,2/5,1/5,3/10)`. Each w has a terminal child of unchanged LR. Physical Q/P conservation holds at all 23 histories; there are 14 strictly positive leaves.

At the only nontrivial hidden-kernel collision `g=(2,1)`, `δ_g=2(2/5−1/10)=3/5`. Reuse the full policy π: root continues, a stops/decides P, b continues, bu stops/decides P, bv continues, bw stops/decides Q; at terminal decide Q only when `r<3/4`. Then `q^C_π(g)=Q(bv)=1/12`. The constructed σ continues with probability 1/2 (and otherwise stops/decides P) at g. Under π the continuation kernel parameter is `s=3/10`; under σ it is `s=1/4`.

\[
\boxed{B_{\rm diam}=\tfrac1{20},\quad B_{\rm pair}=\tfrac1{120}.}
\]

\[
O(\pi)=\left(\frac{43}{240},\frac{19}{40},\frac{17}{12},\frac74\right),
\quad
O(\sigma)=\left(\frac{17}{96},\frac{23}{48},\frac{17}{12},\frac74\right).
\]

\[
\boxed{O(\sigma)-O(\pi)=(-1/480,1/240,0,0).}
\]

For `J=e_P+(3/4)e_Q+(11/200)E_Q τ`, `J(π)=379/600` and `J(σ)=3037/4800`; the **construction's** loss is `1/960`. The earlier independently obtained *best* seedless support gap is `1/2400`. These are different optimizations.

## Checks, status and next question

The locally executed full Python Fraction verifier reconstructs all 23 physical nodes, checks every Q/P conservation equality and the above rational identities, and audits both bounds over **512 deterministic stop/continue patterns** plus **128 seeded reproducible arbitrary rational local behavioral policies**. Full proof covers all real probabilities by coupling, not by extrapolating the finite checks. `VERIFY.py` and `EXACT_OUTPUT.txt` are retained as source and executed evidence. No certified software/formal proof assistant result or independent Driver review was obtained.

**Next unit**: test the stronger N=3 mother question `conv(O_seedless)=O_full` but `O_seedless≠O_full` in a one-collision three-terminal-LR positive-rational family. Start with exact rational convex-hull inclusion over all deterministic full-history four-vectors; only candidates that pass should receive an all-real image-membership certificate.

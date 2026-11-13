# R762O — Sharp adversarial-channel robustness for signed X6 triadic BRC observers

Date: 2026-11-14 (Asia/Shanghai). Status: author-side exact conditional theorem with reproducible finite verification; NOT an accepted native-physics result.

Parent task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Publication: `TP2-8B7E13C5904A2D6F1142`. Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (not modified). Predecessor: R762N, Draft PR #2310, research commit `d73517ebad637d29e8fb541492ee0c09e4c95a4c`. Applies P000's six native spatial axes, 12 signed directions and non-Euclidean `PERP_E`; does not introduce an extra spatial axis or equate a candidate sign-cube to real `TRIADIC_CLOSURE_E` admission.

## Model and explicit observer

Let \(V=Q_3=\{0,1\}^3\), and let \(E\) be its 12 edges (two vertices differ in one of the three named source-sign bits). A candidate signed-triad incidence law is an arbitrary Boolean function \(a:V\to\{0,1\}\); there are 256. Select a labelled subset \(F\subseteq E\) of BRC source-pair observation channels. The two observable schemes are:

* **Unweighted**, \(U_F(a)_{uv}=4(a_u+a_v)\) for each edge \(uv\in F\). All 12 retain 255 distinct signatures, not 256, by the R762M parity ambiguity; the goal here is distinguishability **of the resulting observational equivalence classes**.
* **Positive weighted**, orient each selected edge consistently by its named hidden-source sign, \(W_F(a)_{u\to v}=4(a_u+2a_v)\). The four values \(0,4,8,12\) uniquely encode the two endpoint Boolean bits. The target is recovery of the entire 256-law set.

Channel corruption means one entire reported value may be replaced arbitrarily; erasure means the faulty channel's location is known. This is channel-level Hamming error, **not** an additive noise claim or a physical energy disturbance. The observer keeps edge/source labels and underlying BRC joint associations; no unlicensed factor collapse is performed.

For a set of distinct observable signatures \(C_F\), let \(d_{\min}(F)\) be its minimum positive Hamming distance. A code of distance \(d\) detects up to \(d-1\) arbitrary channel substitutions, uniquely corrects up to \(\lfloor(d-1)/2\rfloor\), and recovers up to \(d-1\) known-position erasures.

## Theorem 1 — Unweighted signature distance equals edge connectivity

If \(H=(V,F)\) is connected, its unweighted observer has exactly 255 distinct observational classes and

\[
\boxed{d_{\min}(U_F)=\lambda(H)
=\min_{\varnothing\ne S\subsetneq V}|\delta_H(S)|.}
\]

Here \(\delta_H(S)\) is the set of selected edges crossing between \(S\) and its complement.

**Proof.** For two Boolean laws \(a,b\), write \(d_v=a_v-b_v\in\{-1,0,1\}\), and \(S=\{v:d_v\ne0\}\). If \(S\) is nonempty and proper, each edge crossing \(S\) has \(d_u+d_v\ne0\). Thus distinct outputs differ in at least \(|\delta_H(S)|\ge\lambda(H)\) coordinates. If \(S=V\), let \(\epsilon_v=(-1)^{v_1+v_2+v_3}\) and \(t_v=\epsilon_vd_v\in\{-1,+1\}\). Along an edge \(uv\), \(\epsilon_u=-\epsilon_v\), so \(d_u+d_v\ne0\) exactly when \(t_u\ne t_v\). If \(t\) is constant, all edge observations agree: this is the one full-cube parity-complement collision. Otherwise the differing coordinates form the nonempty edge cut separating the two \(t\)-values and number at least \(\lambda(H)\). Finally, for any nontrivial \(S\) attaining the minimum cut, set \(d_v=\epsilon_v\) on \(S\) and zero outside. Realize this \(d\) by two Boolean laws (one has a one where \(d=1\), the other where \(d=-1\)); their edge sums differ **precisely** on \(\delta_H(S)\). Thus the lower bound is attained. Connectedness ensures the only zero-distance distinct pair is the global complementary checkerboard pair: on every edge \(d_u=-d_v\), and connectivity propagates one value throughout. QED.

## Theorem 2 — Positive weighted full-law distance equals minimum degree

For any \(F\subseteq E\), with \(\delta(H)=\min_{v\in V}\deg_H(v)\), we have

\[
\boxed{W_F\text{ injective}\iff\delta(H)\ge1,\qquad
d_{\min}(W_F)=\delta(H)\quad(\delta(H)\ge1).}
\]

**Proof.** The map \((x,y)\mapsto x+2y\), for Boolean \(x,y\), is injective. Thus two laws differ at a channel iff at least one of its endpoints has differing law values. For nonempty difference support \(S\), the differing channel set consists exactly of edges incident to \(S\). It contains every edge incident to each fixed \(v\in S\), giving size at least \(\delta(H)\). Taking \(S=\{v_*\}\) for a minimum-degree vertex attains this bound. If \(\delta(H)=0\), the isolated vertex bit is unobserved, so injectivity fails; if \(\delta(H)\ge1\), every vertex is observed. QED.

## Theorem 3 — Sharp channel-number / robustness tradeoff

The following are **globally minimal counts within these two declared source-pair architectures**. The extremizer census counts labelled subsets of the twelve available cube edges.

| Target minimum Hamming distance | Unweighted: minimum channels (number of optimal subsets; distinct classes) | Positive weighted: minimum channels (number of optimal subsets; distinct laws) |
|---|---|---|
| \(d_{\min}\ge1\), noiseless exact identification | **7** (384 spanning trees; 255 classes) | **4** (9 perfect matchings; 256 laws) |
| \(d_{\min}\ge2\), detect one arbitrary wrong channel or recover one erasure | **8** (6 Hamiltonian 8-cycles; 255 classes) | **8** (9 spanning 2-factors; 256 laws) |
| \(d_{\min}\ge3\), correct one arbitrary wrong channel or recover two erasures | **12** (the entire cube; 255 classes) | **12** (the entire cube; 256 laws) |

**Proof of optimality.** A connected graph on eight vertices needs at least seven edges; the three-cube has exactly 384 spanning trees (checked exhaustively; independent standard matrix-tree or direct enumeration reproduces the count). For unweighted distance at least \(r=2,3\), Theorem 1 requires \(\lambda(H)\ge r\), hence all degrees at least \(r\), hence \(2|F|=\sum_v\deg(v)\ge8r\). Eight edges force a connected 2-regular graph, i.e. a Hamiltonian 8-cycle; the cube has six labelled cycles. Twelve edges force all cube edges. The construction witnesses achieve their bounds.

For the weighted observer, Theorem 2 requires minimum degree \(r=1,2,3\). The same handshake bound gives \(|F|\ge4r\). Four edges must form a perfect matching (nine exist); eight must form a 2-factor, either one Hamiltonian 8-cycle (six) or two disjoint square cycles (three); twelve force the whole cube. Every witness achieves equality. Census counts and the distance statements were checked using exact integer enumeration across 4096 edge masks. QED.

### Consequences and the preserved residual

* Four positive-weighted channels are minimal for **noiseless** full-law recovery, but have code distance one and cannot detect even a single unrestricted channel substitution.
* Eight positive-weighted channels provide **one-error detection**; twelve provide **one-error correction**. The two-square weighted 2-factor is valid despite being disconnected: endpoint recovery is local, unlike unweighted parity-equivalence recovery.
* Seven unweighted channels retain the exact 255-class quotient, but cannot recover which of the two global parity laws generated the same signature. Error correction of the *quotient signature* is not the recovery of the full triad incidence law.
* These are sharp finite candidate-model theorems, not verification that 256 candidate incidence laws are legal native events. A true P000 `TRIADIC_CLOSURE_E` and V29/V39 update could restrict the input alphabet or create temporal correlations; recompute the code on that actual legal subset.

## Exact reproducibility and frontier

The sibling executable `research_artifacts/R762O_CHANNEL_ROBUSTNESS.py` exhausts all \(2^{12}=4096\) edge masks, all 127 canonical proper vertex cuts, minimum degrees, exact extremizer counts, and pairwise Hamming distances on witness configurations across all \(2^8=256\) Boolean laws. All arithmetic uses Python exact integers and Boolean tuples. The companion JSON holds the counts, witness indices and result of the independent brute-force distance check. No stochastic estimate, physics calibration, review acceptance or native execution is asserted.

**Next discriminating question:** extract an actual legal, source-typed P000 triadic event set \(L\subseteq\{0,1\}^8\) together with its Cell/Link/Port and event ledger. Determine the observer-code distances \(\min_{a\ne b\in L}\operatorname{dist}(U_F(a),U_F(b))\) and \(\min_{a\ne b\in L}\operatorname{dist}(W_F(a),W_F(b))\), including any V29/V39 time-indexed observations and legality of successive events. The present robustness lower bounds are for the full explicitly stated candidate alphabet and must not be silently promoted to the native one.

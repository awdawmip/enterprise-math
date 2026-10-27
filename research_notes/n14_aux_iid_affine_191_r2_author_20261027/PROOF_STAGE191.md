# Stage191 — all-real exact optimal interval (external ternary IID N14)

**2026-10-27 | Author-level proof and executed rational certificate | NOT_ADMITTED.** This is an auxiliary IID sequential decision model, not a native P000/X6 theorem or experimentally verified physical law.

## Frozen inputs, source authority and statement

GLOBAL_KNOWLEDGE_V1 was read from verified canonical main \`b87062620426fe6a36250644bbc08789c86cd2af\` (bootstrap/manual, P000 and original blob, ACTIVE worldview, math/BRC rules). Enterprise Math protocol and current control inputs were read at main \`8e9c6ec65632404dd596c69f9d8329d7841f0218\`. The Stage190 predecessor proof is the existing branch \`research/r2-n14-stage190-author-exact-20261027-1312-auto11\`, blob \`d9441d4d4360cdf38c582fc0c4ac4f249419474d\`, distinct from canonical admission.

There are at most N=14 independent ternary observations, with P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6). Let eP=P(decide Q), eQ=Q(decide P), tP=E_P[T], tQ=E_Q[T]. Any randomized stopping and decision policy measurable with respect to *complete ordered observations* is allowed. Define V14(alpha)=min max(tP,tQ) over eP,eQ <= alpha.

At the Stage190 endpoint,

\[
\alpha_{190}=\frac{28137949158459611576537}{80134219991312171532288},
\quad V_{190}=\frac{3422790017676192400495567}{320536879965248686129152}.
\]

**Theorem.** For every real \(\delta\) with

\[
0\le\delta\le \Delta=\frac{569778090625}{4347559678348099584}
\]

we have

\[
\boxed{V_{14}(\alpha_{190}+\delta)=V_{190}-\frac{1214685773221}{3646579780}\delta.}
\]

In particular,

\[
\boxed{\alpha_{191}=\frac{4019708522944196853791}{11447745713044595933184}},
\qquad
\boxed{V_{191}=\frac{488968003499440699225081}{45790982852178383732736}}.
\]

For every real alpha>alpha191, the *fixed* Stage191 Bellman supporting line lies strictly below V14(alpha); this does not assert the global shape of V14 beyond alpha191.

## 1. Universal Bellman dual, no history restriction

At count state s=(n,a,b), a=first-symbol count and b=second-symbol count, the ordered-prefix likelihood ratio is Q(prefix)/P(prefix)=2^(a+b)/3^a, regardless of the particular order. Let

\[
K=\frac{610519409541}{3646579780},\quad
L=\frac{30208318184}{182328989},\quad
H=\frac{531209309176160736181221937}{4161698766215586030551040}.
\]

Exactly compute h(s)=min{K ell(s), L, 1+sum_i P_i h(s+e_i)}, forbidding continuation at n=14. It has root h(0,0,0)=H. All 680 count states were evaluated with exact rational arithmetic: exactly 1238 strictly positive nonoptimal action gaps, no negative gaps, minimum 8957179515094375931/451573216820267581440. Exactly two ties occur:

X=(8,0,1): choose Q or continue; Z=(10,5,2): choose P or continue.

At each *ordered* prefix the conditional costs obey the same Bellman inequalities, since both the likelihood ratio and the IID conditional suffix probabilities depend only on the count state. Randomization is a convex combination of actions. Backward conditioning on each full history proves for **every history-dependent randomized policy**

\[
t_P+K e_Q+L e_P\ge H,\qquad V_{14}(\alpha)\ge H-(K+L)\alpha.
\]

This establishes a rigorous dual lower bound, without claiming that arbitrary history-dependent policies are themselves count-state policies.

## 2. Exact primal, BRC mass and two independent computational routes

Let x denote the probability of deciding Q at X, and z the probability of deciding P at Z, otherwise continuing. Elsewhere take the uniquely minimizing Bellman action. The first tie at X (depth 8, a=0) cannot be an ancestor of Z (depth 10, a=5): only two draws remain but five first-symbol occurrences are required. Reverse ancestry is impossible by depth. Thus their first-hit cones are disjoint, and the mixed term vanishes *structurally*.

For O=(eP,eQ,tP,tQ), the four deterministic corner results have the exact affine interpolation O(x,z)=B+x DX+z DZ, with

\[
\begin{aligned}
B={}&(611613348012670649/1752976676930715648,\;
113284731338369/320979616137216,\;
2355003691949994935/219122084616339456,\;
282754064278565/26748301344768),\\
DX={}&(84427421875/17832200896512,\;
-58984375/15479341056,\;
-326450234375/2229025112064,\;
-26297890625/104485552128),\\
DZ={}&(-74375/130459631616,\;
96875/139314069504,\;
-9671875/440301256704,\;
-1328125/104485552128),\\
C={}&(0,0,0,0).
\end{aligned}
\]

The suffix-DP computed all four corners with Python's exact fractions.Fraction. An independently coded *unmerged ordered-history* DFS with integer P weights (3,1,20), Q weights (2,2,20), and denominator 24^14 evaluated the same four observation vectors and matched all fractions. DFS node counts for (x,z)=00,01,10,11 respectively: 182350,166990,181582,166222, total **697144**. X has 8 first-hit histories and Z has 640; intersection by ancestry is zero. The full corner certificate and the *actually executed* code and stdout are in the associated Stage191 portable evidence archive.

This instantiates the BRC positive-rational weighted branch carrier with ordered provenance. The count-state reduction is used only where the IID conditional law proves sufficiency. It is not a general history-lossless result, signed-amplitude calculation or native-X6 transfer.

## 3. Balance, complete real interval, and endpoint

Solving eP=eQ exactly yields

\[
x(z)=\frac{21216994209825749}{44937930240000000}
+\frac{577693}{3900862000}z,\quad 0\le z\le1.
\]

For every real z in that interval both coins are legal; x(1)=3031949890455107/6419704320000000<1, while z first saturates at 1. The observations reduce to

\[
\begin{aligned}
e_P(z)=e_Q(z)&=\alpha_{190}+\frac{569778090625}{4347559678348099584}z,\\
t_P(z)&=V_{190}-\frac{759178608263125}{17390238713392398336}z,\\
t_P(z)-t_Q(z)&=\frac{217534777678506481212413}{961610639895746058387456}
+\frac{36688939255625}{5796746237797466112}z>0.
\end{aligned}
\]

Exact substitution verifies tP+K eQ+L eP=H and

\[
-\frac{\mathrm{d}t_P/\mathrm{d}z}{\mathrm{d}\alpha/\mathrm{d}z}
=K+L=\frac{1214685773221}{3646579780}.
\]

Thus for *every real* alpha from alpha190 through alpha191, including irrational alpha, choose real z=(alpha-alpha190)/Delta and x=x(z). The admissible randomized strategy attains the universal Bellman lower bound with max(tP,tQ)=tP, proving the claimed formula.

## 4. Strictness of this fixed line to the right

For finite horizon the behavioral randomized policy space is a finite product of compact simplices, so a minimum exists in every feasible error-constraint slice. Suppose equality held with H-(K+L)alpha at alpha>alpha191. Because K,L>0, equality forces eP=eQ=alpha and equality in the all-history Bellman bound. Every reached strict-gap action is excluded. At each tied state, all ordered first-hit prefixes have identical P/Q likelihood ratio and IID suffix statistics. P-mass-weighted averaging of any prefix-specific randomization produces an effective x and z preserving all four observables. The tie cones are disjoint, so O(x,z)=B+x DX+z DZ holds for every equality policy, not just the count-stationary example. Equal errors force x=x(z) uniquely, and legal z<=1 forces alpha<=alpha191, contradiction. Thus the fixed supporting line is strictly below V14(alpha) for any alpha>alpha191.

## Evidence, limits and continuation

Exact local runs: \`VERIFY_STAGE191_EXECUTED.py\` -> \`STAGE191_AUTHOR_EXACT_FULL_REAL_PASS\`; \`SCAN_STAGE192.py\` -> \`STAGE192_DUAL_SCAN_PASS\`. The local portable archive \`EM_STAGE191_AUTHOR_EXACT_PORTABLE_20261027.tar.xz\` has SHA256 \`4366a6cee59c057cb99820c1d7d298231e7cc1e2ff53bbd0beec7b7d7b67bb38\`; it contains full executed sources, exact JSON certificates, raw stdout and per-file hashes. The next Stage192 task is dual-only and does **not** carry a primal theorem.

The connected GitHub principal was \`awdawmip\`. Canonical Source task inventory returned \`CONTROL_QUOTA\`, and new native session creation was explicitly rejected with \`STATIC_READONLY_SCOPE_DENIED\` (\`operation_sent=false\`); current active owner was not independently confirmed. This GitHub branch is author-level portable evidence, not a formal Source CLAIM/Result or independent Driver review. P000 remains unchanged; native X6 transfer requires separately proved slice/readout/relation/update correspondence.
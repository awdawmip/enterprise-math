# EC49FUT — Six more n=30 two-support windows; local termination at counts 17–29

Date: 2026-11-20 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_INTERVAL_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**.

## Frozen research scope

Frozen BRC16943 source: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Continue EC49FUS (PR #2852, \`48b9c12889797201e104621dc27a653bc91dc5ef\`) with its two independently certified n=30 windows j=9,10. Mathematical parent author proofs: EC49FUO threshold complete class (\`8df5788adcd977cc809a0e27da180833317e3dfa\`), EC49FUQ endpoint-only nuisance reduction (\`96ad7a2c22c274446e74906c48bc6e3234a39436\`), EC49FUR finite total-variation dual (\`0ac1ef58d84517835260e4aefbe6d2c2b3a293c9\`). The parent chain is not independently mathematically reviewed.

This research treats a **lossy binary clipped-price observer**. No identity with the native X6 joint residual, path/branch, labeled price source, six-dimensional Cell, complete three-dimensional slice, or P000 dynamics is claimed.

## Frozen exact model and dual

Fix \(\theta\in[0,E]\), \(E=31597745/1653649\), \(n=30\), \(\beta=3/637\), and real \(0<x<1\). The point \(\theta=0\) compactifies an original limiting nuisance value. Define

\[
u_\theta=\frac{21829245984}{45529434409-456083905\theta},
\quad T_\theta(x)=(1-x)(1-\beta x+\beta x\theta),
\quad p_\theta=1-T_\theta,\quad q_\theta=1-u_\theta T_\theta.
\]

The signed binomial mass and tail advantage are

\[
\Delta_\theta(k;x)=\binom{30}{k}
\big(q_\theta^k(1-q_\theta)^{30-k}-p_\theta^k(1-p_\theta)^{30-k}\big),
\quad D_\theta^{\ge j}(x)=\sum_{k=j}^{30}\Delta_\theta(k;x).
\]

Let \(Z=0\), \(G_j=D_E^{\ge j}-D_Z^{\ge j}\), \(H_j=G_{j+1}\), \(d_j=\Delta_E(j)-\Delta_Z(j)\). By the named parent theorems the **full-bit composite minimax advantage** is

\[
 A_{30}(x)=1-2V_{30}(x)
 =\min_{0\le\lambda\le1}
 \sum_{k=0}^{30}\big[(1-\lambda)\Delta_Z(k;x)+\lambda\Delta_E(k;x)\big]_+.
\]

## Theorem A — complete re-entrant neighborhoods at j=11,12,13,14,15,16

Each row's \(I_j\) is a **complete certified real width interval**. Let \(a_j\) denote the unique zero of \(G_j\) and \(b_j\) the unique zero of \(\Delta_E(j)\) in that interval. Every tabulated algebraic root bracket is **strict**, with rational endpoints (shown to 12 decimal places).

| j | I_j | Entry a_j, strict bracket | Exit b_j, strict bracket |
|---:|---|---|---|
| 11 | [0.224,0.235] | (0.225500758714,0.225500758715) | (0.232493020829,0.232493020830) |
| 12 | [0.264,0.273] | (0.265335976635,0.265335976636) | (0.271729505923,0.271729505924) |
| 13 | [0.305,0.314] | (0.306101041760,0.306101041761) | (0.311606276755,0.311606276756) |
| 14 | [0.346,0.354] | (0.347591154980,0.347591154981) | (0.351933959535,0.351933959536) |
| 15 | [0.388,0.394] | (0.389649898533,0.389649898534) | (0.392569888098,0.392569888099) |
| 16 | [0.431,0.435] | (0.432156258608,0.432156258609) | (0.433405288408,0.433405288409) |

All six rows satisfy \(a_j<b_j\). Within each \(I_j\) the exact phase classification is:

* \(x<a_j\): unique optimal **endpoint-prior** weight \(\lambda_E=1\); minimax test right iff \(K\ge j\).
* \(x=a_j\): optimal endpoint weights form exactly \([\lambda_j(a_j),1]\); right iff \(K\ge j\).
* \(a_j<x<b_j\): the endpoint-prior optimum is uniquely and genuinely two-point, with
  \[
  \boxed{\lambda_j=-\frac{\Delta_Z(j;x)}{d_j(x)}\in(3/4,1),\qquad
  \gamma_j=-\frac{H_j(x)}{d_j(x)}\in(0,1).}
  \]
  The minimax rule decides left when \(K<j\), right when \(K>j\), and right with probability \(\gamma_j\) on \(K=j\).
* \(x=b_j\): unique optimal endpoint weight is \(\lambda_E=1\); any \(\gamma\in[0,\gamma_j(b_j)]\) at \(K=j\) is minimax.
* \(x>b_j\): unique optimal endpoint weight \(\lambda_E=1\); right iff \(K\ge j+1\).

All cases include the respective endpoints of \(I_j\). The exact minimax advantage is

\[
\boxed{
A_{30}(x)=
\begin{cases}
D_E^{\ge j}(x),&x\le a_j,\\
(1-\lambda_j(x))D_Z^{\ge j+1}(x)+\lambda_j(x)D_E^{\ge j+1}(x),&a_j<x<b_j,\\
D_E^{\ge j+1}(x),&x\ge b_j.
\end{cases}}
\]

### Proof of Theorem A

The accompanying exact-rational verifier partitions every \(I_j\) into 128 consecutive closed rational intervals and proves **all eight** pointwise inequalities over their full real union:

\[
\Delta_E(j-1)<0,\quad\Delta_Z(j)<0,\quad
\Delta_Z(j+1)<0,\quad\Delta_E(j+1)>0,
\]
\[
(1/4)\Delta_Z(j)+(3/4)\Delta_E(j)<0,\quad
(\Delta_Z(j+1)+\Delta_E(j+1))/2>0,
\quad H_j<-1/100,\quad G'_j>1/4.
\]

The derivative is computed exactly using

\[
\frac{d}{dx}D_\theta^{\ge j}
=30\binom{29}{j-1}\left[q_\theta^{j-1}(1-q_\theta)^{30-j}q'_\theta
-p_\theta^{j-1}(1-p_\theta)^{30-j}p'_\theta\right],
\quad p'_\theta=-T'_\theta,\ q'_\theta=-u_\theta T'_\theta.
\]

Strict rational opposite-sign evaluations at the two endpoints of every displayed root bracket prove a root exists; the \(G'_j\) lower bound proves \(a_j\) is unique. The sign of \(\Delta_E(j)\) is exactly that of

\[
(u_E^{(30-j)/j}-1)+(1-u_E^{30/j})T_E(x).
\]

Because \(u_E\in(0,1)\) and \(T_E(x)\) decreases strictly, it has at most one root, proving uniqueness of \(b_j\). The disjoint rational brackets prove \(a_j<b_j\).

For \(x<b_j\), \(\Delta_Z(j)<0<\Delta_E(j)\), and their mixture has a unique zero \(\lambda_j\in(3/4,1)\) by the certified \(\lambda=3/4\) sign. Its count \(j+1\) mass is already positive at \(\lambda=1/2\). The parent uniform mixed-binomial single-crossing property and adjacent endpoint signs ensure every lower count is negative and every higher count is positive. Therefore at the kink \(\lambda_j\), the convex dual's left derivative is \(H_j<0\) and right derivative is \(G_j\), which strictly increases through zero at \(a_j\). This yields respectively the pure-E, flat-prior, and compulsory-mixing regimes. For \(x\ge b_j\), E's j-th signed mass becomes nonpositive while the next is positive and \(H_j<0\), so pure E is the unique endpoint dual minimizer. Equating the two endpoint advantages of the boundary-randomized count test gives \(\gamma_j=-H_j/d_j\); its strict interior range follows from \(H_j<0<G_j=H_j+d_j\). The exit gamma interval follows from the strict Z-versus-E advantage inequality.

## Theorem B — local pure-E phase through all higher thresholds j=17,...,29

In each **entire** certified interval \(J_j\) below, let \(c_j\) denote the unique zero of \(\Delta_E(j;x)\). The least-favorable endpoint prior is uniquely **pure E** for the whole interval. The exact minimax test is \(K\ge j\) for \(x<c_j\), \(K\ge j+1\) for \(x>c_j\), and at \(x=c_j\) it may randomize **arbitrarily** at count \(j\), with all other decisions unchanged. These are local decision-threshold transitions, not compulsory nuisance-mixing windows.

| j | J_j | Unique E-Bayes crossing c_j, strict bracket |
|---:|---|---|
|17|[0.472,0.477]|(0.474356338011,0.474356338012)|
|18|[0.513,0.518]|(0.515357839408,0.515357839409)|
|19|[0.554,0.559]|(0.556358678282,0.556358678283)|
|20|[0.595,0.600]|(0.597318517188,0.597318517189)|
|21|[0.636,0.641]|(0.638205356397,0.638205356398)|
|22|[0.676,0.681]|(0.678993711821,0.678993711822)|
|23|[0.717,0.722]|(0.719663237873,0.719663237874)|
|24|[0.758,0.763]|(0.760197675211,0.760197675212)|
|25|[0.798,0.803]|(0.800584038553,0.800584038554)|
|26|[0.838,0.843]|(0.840811983841,0.840811983842)|
|27|[0.878,0.883]|(0.880873310863,0.880873310864)|
|28|[0.918,0.923]|(0.920761569134,0.920761569135)|
|29|[0.958,0.963]|(0.960471743261,0.960471743262)|

### Proof of Theorem B

The second executable exact-rational verifier covers each \(J_j\) by 128 closed rational intervals. On **every real width** in their union it establishes

\[
\Delta_E(j-1)<0,\quad \Delta_E(j+1)>0,\quad
H_j=G_{j+1}<0,\quad G'_j>0.
\]

It separately establishes \(G_j(c_j^+)<0\) at the upper isolating-bracket rational endpoint and \(\Delta_E(j;c_j^-) >0 > \Delta_E(j;c_j^+)\). The unique E-Bayes switch exists by the strict monotone sign formula already used in Theorem A. For all \(x\le c_j\), strict \(G'_j>0\) yields \(G_j(x)<G_j(c_j^+)<0\). Thus E's optimal test \(K\ge j\) satisfies \(D_Z>D_E\). For \(x\ge c_j\), E's optimal test \(K\ge j+1\) satisfies \(D_Z>D_E\) because \(H_j<0\). At the crossing any test randomized on count j has the same E advantage and a strictly greater Z advantage.

Every competing rule \(\phi\) obeys \(\min(D_Z(\phi),D_E(\phi))\le D_E(\phi)\le D_E(\phi_E^*)\). The constructed E-Bayes test achieves this upper bound, proving composite minimaxity by the parent endpoint reduction. The endpoint dual has a strictly negative left slope at \(\lambda=1\), so its endpoint-mixture minimizer is uniquely E. No root of \(G_j\) within \(J_j\) is required.

## Exact evidence and reproducibility

Two standalone standard-library scripts, located next to this note, were **actually executed on 2026-11-20**. Both returned their complete success markers. The first verifies \(6\times128=768\) exact rational interval slabs for j=11..16, plus every rational root bracket; the second verifies \(13\times128=1664\) slabs for j=17..29 and all tie/endpoint witnesses. Total: **2432 full real-interval enclosure certificates**. The printed decimal margins are merely displays; only exact integer/Fraction inequalities decide PASS.

\`\`\`sh
python3 research_notes/portable_direct/EC49FUT_N30_HIGH_COUNT_WINDOWS_VERIFY.py
python3 research_notes/portable_direct/EC49FUT_N30_PURE_E_HIGH_TAIL_VERIFY.py
\`\`\`

Expected terminal lines: \`ALL PASS\` and \`ALL PURE-E HIGH TAIL PASS\`. Only Python 3 standard library is needed. Finite interval certificates verify the stated algebraic hypotheses; the universal test/prior reductions remain inherited author proofs and independently **NOT_REVIEWED**.

## Scientific frontier and source attribution

At n=30 the certified local mixing windows now include j=9,10 (EC49FUS) and **j=11,...,16 (this note)**. The next thirteen count-transition neighborhoods **j=17,...,29** instead have a pure upper-endpoint prior throughout. The sharp reversal in relative root order between j=16 and j=17 is a new structural observation. Future work: classify the gaps between the certified neighborhoods and the low-count region; investigate the dependence of window count on n with exact root-order certificates, and retain native BRC/X6 provenance/fibers when comparing binary compression against full residual observations.

Historical identity lineage: Researcher \`EM-DIRECT-8454C6\`, SID \`MCP-44cfc4e6f2094f96861854ebefc77e84\`, Activity \`RA-ED136F89271FD89288F3E58D\`; these are **prior provenance**, not a new authenticated session or CLAIM. Current portable publication and Activity linkage are separate. No credential contents or wider sharing are included.

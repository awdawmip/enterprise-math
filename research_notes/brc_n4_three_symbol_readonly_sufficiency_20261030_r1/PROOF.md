# Exact three-label read-only BRC observer; TV-preserving quotient counterexample

**Author analytic proof, 2026-10-30. UNREVIEWED / NOT_ADMITTED.** Scientific parent: PR #1757 @ \`8a54facec350ebcc2303722831a2921baee9e8ac\`, \`research_notes/brc_n4_eps_D_endpoint_equality_support_20261030_r1/PROOF.md\`. External finite positive-weight BRC N=4 experiment only; this does not assert native X6 or Heartbeat dynamics.

## Frozen experiment and scope

The original sixteen strict-positive leaves are, for \(s\in\{AU,AV,BU,BV\}\), \(j,k\in\{0,1\}\),

\[
Q(s,j,k)=q_s/4,\quad P(s,j,k)=q_sr_{sj}/4,
\]
where \(q=(1/6,1/3,1/4,1/4)\),
\(r_{AU}=(9/10,11/10)\), \(r_{AV}=(1/4,1/4)\), \(r_{BU}=(1/5,9/5)\), and \(r_{BV}=(2,2)\).
The coarse \(C\) maps AV/BV to E, AU to A and BU to B. Both source laws give \(C\) masses \((7/12,1/6,1/4)\). On BU, the actual branch \(J=j\) is observed through shared noise \(Z=j\oplus\mathrm{Bernoulli}(\varepsilon)\), \(0\le\varepsilon\le1/2\). Lawful S2/S23 stage-four decisions can use the **actually read, unchanged, fair** \(K=k\), then emit \(Y\in\{B3,B4P0,B4P1,B4Q0,B4Q1\}\). Define \(F_j=\mathcal L(Y\mid BU,J=j)\) and \(D=TV(F_0,F_1)\).

The preceding exact endpoint theorem gives, for \(t=1-2\varepsilon\in(0,1)\), \(D\in(0,1)\), the sharp full between-law joint TV \(U=[D+t(1-D)]/10\). Equality \(T=U\) occurs precisely when each active output atom y has either \(F_0(y)=F_1(y)>0\), or \(F_0(y)>0,F_1(y)=0\), or \(F_1(y)>0,F_0(y)=0\). This equality condition is our explicit hypothesis.

**Future operations covered:** any finite, or well-defined countable, adaptive read-only protocol whose conditional transcript law is a source-law-independent kernel \(H(dh\mid C,Z,Y)\). Repeated access to K on a legal stage-four path must reuse the same K. No stopped-path unseen K, intervention changing K, or native physical time process is introduced.

## Theorem A — exact statistical reconstruction with only three symbols

Partition the active Y alphabet into \(A=\{y:F_0(y)>0,F_1(y)=0\}\), \(B=\{y:F_1(y)>0,F_0(y)=0\}\), and \(M=\{y:F_0(y)=F_1(y)>0\}\). Define the deterministic statistic \(S(Y)=+\) on A, \(-\) on B and \(c\) on M. Then

\[
F_0(S=c,+,-)=(1-D,D,0),\qquad F_1(S=c,+,-)=(1-D,0,D).
\]

The following *single law-independent reverse kernel* reconstructs both \(F_0,F_1\):

\[
R(y\mid c)=1_M(y)F_0(y)/(1-D),\quad
R(y\mid +)=1_A(y)F_0(y)/D,\quad
R(y\mid -)=1_B(y)F_1(y)/D.
\tag{1}
\]

Indeed, all rows sum to one and for each \(j\in\{0,1\}\),
\[
F_j(y)=\sum_{s\in\{c,+,-\}}F_j(S=s)R(y\mid s).
\tag{2}
\]

All BU terms in the full experiment factor as \(w_j(C,Z)F_j(y)\), including the source-specific P/Q branch mass and the common sensor. Substitution of (2) proves exact equality of the full **joint laws** \((C,Z,S,Y)\) reconstructed from \((C,Z,S)\) by sampling Y from R once. Composing with any source-independent \(H(dh\mid C,Z,Y)\) proves joint reconstruction of \((C,Z,S,Y,\text{entire adaptive transcript})\) for both P and Q. This is an exact finite/consistent sequential-kernel factorization, not merely equality of marginal readouts. Since S is deterministic in Y and R reconstructs Y in law, TV data processing in both directions gives
\[
TV(P_{C,Z,S},Q_{C,Z,S})=TV(P_{C,Z,Y},Q_{C,Z,Y})=U.
\tag{3}
\]

The three-state quotient is **cardinality-minimal even among randomized encoders** if a shared decoder must reconstruct both \(F_j\). To prove this, take one F0-only output \(y_+\in A\) and one F1-only \(y_-\in B\). Suppose a stochastic encoder E to at most two labels and a source-independent R satisfy \(F_j=F_jER\). Producing \(y_+\) under F0 and zero under F1 forces an encoded label \(s_+\) with \((F_0E)(s_+)>0=(F_1E)(s_+)\); similarly \(y_-\) forces a distinct \(s_-\) with \((F_1E)(s_-)>0=(F_0E)(s_-)\). With at most two labels the encoded distributions are disjoint and have TV 1, contradicting data processing \(TV(F_0E,F_1E)\le D<1\). Thus the exact minimum is three. This is the **two-source statistical experiment** minimum for the declared read-only operation scope, not a minimum for realizing an earlier physical leaf K.

## Theorem B — preserving D alone loses joint provenance

Choose the lawful S23 strategy \(u_0=u_1=D\in(0,1)\): j=0 continues to stage four and makes terminal decision P; j=1 continues with the same probability and chooses Q; stop otherwise. Both choices are independent of K. Its conditional distributions are

|Y|B3|B4P0|B4P1|B4Q0|B4Q1|
|---|---:|---:|---:|---:|---:|
|F0|1-D|D/2|D/2|0|0|
|F1|1-D|0|0|D/2|D/2|

The lawful Y support has five symbols, as required by the preceding S23 terminal-support theorem; the three-symbol statistic S and shared inverse R are exact **statistical** compressors.

Define another deterministic quotient H by merging B3 with B4P0 and leaving B4P1, B4Q0, B4Q1 separate. It does not combine any F0-only and F1-only mass, so
\[
TV(F_0H,F_1H)=D.
\tag{4}
\]

However, its merged atom contains common mass \(m=1-D>0\) and source-contrast mass \(x=D/2>0\). The exact upper-deficit identity of PR #1757, \(20(U-T)=\sum_y\min\{(1-t)x_y,2tm_y\}\), gives the *strict* rational gap
\[
\boxed{T_Y-T_{H(Y)}=\frac1{20}
\min\left\{\frac{(1-t)D}{2},\,2t(1-D)\right\}>0
\quad(0<t,D<1).}
\tag{5}
\]

At \(D=1/2,\varepsilon=1/4\) (\(t=1/2\)),
\[
TV(F_0H,F_1H)=1/2,\quad T_Y=3/40,\quad
T_{H(Y)}=11/160,\quad T_Y-T_{H(Y)}=1/160.
\]
Therefore retaining the branch-discrimination TV D is **not** a certificate for full noisy provenance-joint TV. The exact three-class factorization (1) is a stronger, observer-and-future-operation-scoped sufficiency certificate.

## Realized-path separation

For the S23 witness, K is conditionally fair even given C,Z,S on a continued BU path. Reconstructing a new Y using R once generates a consistent K *distribution* for arbitrarily many read-only queries, but cannot identify the actual pre-existing K. Both P and Q give \(P(BU)=Q(BU)=1/4\) and continuation probability D within BU. For every predictor based only on \(C,Z,S\) and new random coins,
\[
\inf_{\widehat K}\Pr(\widehat K\ne K,\ BU\ \text{continued})=D/8.
\tag{6}
\]
Conditionally, K is fair and every guess errs with probability 1/2; a fixed guess attains equality. At D=1/2 this is 1/16. This explicitly separates statistical, joint-transcript and same-realized-path semantics.

## Computation and limits

The committed \`VERIFY.js\` is an **actually executed** exact BigInt rational checker. It rebuilds all 16 strictly positive P and Q leaves; for twelve \((D,\varepsilon)\) pairs it checks common reverse-kernel reconstruction under both laws, equality of joint TV and the formula U, a two-stage rational Z- and history-adapted transcript, H's exact TV deficit, and the rational example. \`RUN_EVIDENCE.txt\` contains the literal check output. An independent local Python Fraction checker also executed the same twelve parameter combinations, source-leaf pushforward and adaptive transcript, and enumerated 32 deterministic binary partitions per D; it remains a separate local execution aid, not a claim that every randomized encoder was enumerated. All-real and arbitrary-finite-output assertions follow from the proofs here; numerical grids corroborate them.

**BRC reuse:** the exact positive-rational branch/source sensor/terminal observer and source-independent kernel descent. The model keeps source provenance and shared K readout instead of erasing joint direction by TV summarization. P000 V5 native six-axis Cell, three-dimensional layer, independent typed time, triadic native closure and physical state update remain separate mapping obligations. The current output is AUTHOR_ANALYTIC_PROOF / EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED; no native CLAIM, Result or independent Driver review is asserted.

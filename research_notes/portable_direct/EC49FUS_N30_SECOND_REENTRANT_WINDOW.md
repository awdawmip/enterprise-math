# EC49FUS-B — A second certified re-entrant minimax window (n=30, count 10)

Date: 2026-11-20 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_INTERVAL_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**.

## Provenance and scope

Frozen BRC16943 scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Reuse EC49FUO's threshold complete-class theorem, EC49FUQ's endpoint-only nuisance reduction, EC49FUR's total-variation dual, and EC49FUS's independently checked first window. Model: the *lossy* clipped-price binary observation, not a native X6 lossless observer. P000, residual fidelity, three-dimensional slice semantics and original scientific pin are unchanged.

Use exactly the model and signed binomial masses \(\Delta_t(k;x)\), \(t\in\{0,E\}\), from EC49FUS, with \(n=30\). Put \(I_2=[93/500,49/250]=[0.186,0.196]\),
\[
G_{10}(x)=D_E^{\ge10}(x)-D_0^{\ge10}(x),\quad
H_{10}(x)=D_E^{\ge11}(x)-D_0^{\ge11}(x).
\]
For this interval define the algebraic entry and exit by \(G_{10}(a_{10})=0\) and \(\Delta_E(10;b_{10})=0\).

## Theorem — the second complete re-entrant window

There are exactly two distinct roots in \(I_2\), with strict rational isolations

\[
\boxed{0.186867177194<a_{10}<0.186867177196},
\qquad
\boxed{0.194151512437<b_{10}<0.194151512439}.
\]

Write
\[
\lambda_{10}(x)=-\frac{\Delta_0(10;x)}{\Delta_E(10;x)-\Delta_0(10;x)},\quad
\gamma_{10}(x)=-\frac{H_{10}(x)}{\Delta_E(10;x)-\Delta_0(10;x)}.
\]
The *entire interval* \(I_2\) is classified as follows.

| Detection width | All least-favorable prior weights | Minimax decision |
|---|---|---|
| \(0.186\le x<a_{10}\) | unique \(\lambda=1\) | right iff \(K\ge10\) |
| \(x=a_{10}\) | \(\lambda\in[\lambda_{10}(a_{10}),1]\) | right iff \(K\ge10\) |
| \(a_{10}<x<b_{10}\) | unique \(\lambda=\lambda_{10}(x)\in(3/4,1)\) | right for \(K\ge11\), left for \(K\le9\), right at \(K=10\) with probability \(\gamma_{10}(x)\in(0,1)\) |
| \(x=b_{10}\) | unique \(\lambda=1\) | right for \(K\ge11\), left for \(K\le9\); any \(0\le\gamma\le\gamma_{10}(b_{10})\) at \(K=10\) |
| \(b_{10}<x\le0.196\) | unique \(\lambda=1\) | right iff \(K\ge11\) |

As in EC49FUS's count-9 window, the entry has a whole interval of least-favorable priors, then a jump to a nontrivial unique two-point mixture. At exit \(\lambda_{10}\to1\) continuously. The primal boundary randomization varies from \(1\) at entry to approximately \(0.826\) at exit (the exact value is the rational-expression limit at the algebraic root).

The exact minimax advantage \(A=1-2V_{30}\) is

\[
\boxed{
A(x)=
\begin{cases}
D_E^{\ge10}(x),&x\le a_{10},\\
(1-\lambda_{10})D_0^{\ge11}(x)+\lambda_{10}D_E^{\ge11}(x),&
a_{10}<x<b_{10},\\
D_E^{\ge11}(x),&x\ge b_{10}.
\end{cases}}
\]

At the representative rational width \(x=19/100\), exact computation gives
\(\lambda_{10}\approx0.883190282613\) and \(\gamma_{10}\approx0.926851870752\).

## Proof and exact certificate

The companion executable `EC49FUS_N30_SECOND_MIXED_WINDOW_VERIFY.py` imports the already-published `EC49FUS_N30_MIXED_WINDOW_VERIFY.py` (same directory). It partitions \(I_2\) into 128 rational closed slabs and checks by exact \(`fractions.Fraction`\) interval enclosures that **for every real \(x\in I_2\)**,

\[
\begin{gathered}
\Delta_E(9)<0,\quad \Delta_0(10)<0,\quad
\Delta_0(11)<0,\quad \Delta_E(11)>0,\\
\Delta_{3/4}(10)<0,\quad \Delta_{1/3}(11)>0,\\
H_{10}<-1/100,\qquad G_{10}'>1/4.
\end{gathered}
\]

Smallest verified rational margins past those eight respective thresholds, displayed as decimal lower truncations, are:
\(0.026266203374,0.023331225483,0.006298229281,0.030302559932,0.000746215586,0.002703057635,0.010631134721,0.430317090485\).
The script's assertions use exact fractions, never the displays.

The two root brackets are separately verified by exact sign substitutions:
\[
G_{10}(186867177194/10^{12})<0<
G_{10}(186867177196/10^{12}),
\]
\[
\Delta_E(10;194151512437/10^{12})>0>
\Delta_E(10;194151512439/10^{12}).
\]
The strictly positive derivative certifies that \(G_{10}\) has exactly one root in the full interval. The \(E\) count-10 signed mass has a unique zero because its sign is the sign of
\[
u_E^{(30-10)/10}(1-u_ET_E)-(1-T_E)
=(u_E^2-1)+(1-u_E^3)T_E(x),
\]
strictly increasing with \(T_E\), while \(T_E\) strictly decreases with \(x\).

To locate the dual minimizer: below the count-10 exit, \(\Delta_E(10)>0>\Delta_0(10)\). The certified \(\Delta_{3/4}(10)<0\) forces \(\lambda_{10}>3/4\); the certified \(\Delta_{1/3}(11)>0\) and the endpoint signs make the count-11 mixed mass positive at \(\lambda_{10}\). Count 9 is negative by endpoint signs and the mixed-binomial monotone likelihood ratio. Thus the slope immediately left of the count-10 dual kink is \(H_{10}<0\), and immediately right is \(G_{10}\). It follows by convexity that the unique minimizer is \(1\) before entry, the full interval \([\lambda_{10},1]\) at entry, and the unique \(\lambda_{10}\) in the mixing window. At and above exit, \(E\)'s optimal count threshold changes to \(K\ge11\) and its left dual derivative remains strictly negative \(H_{10}\), giving the unique pure \(E\) minimizer.

The saddle test follows by matching the two endpoint advantages on the count-10 decision, giving \(\gamma_{10}=-H_{10}/[\Delta_E(10)-\Delta_0(10)]\in(0,1)\). The exit tie interval and the piecewise exact risk formula follow as for EC49FUS, with count 10 replacing count 9. This proves all rows for the continuum of widths.

## Exact reproduction / continuation

Run, from the `research_notes/portable_direct/` directory:

`python3 EC49FUS_N30_SECOND_MIXED_WINDOW_VERIFY.py`

On 2026-11-20 the local standard-library run returned `PASS second n30 mixed window; 128 exact slabs`, including all eight rational margins, both isolating intervals and sample weights. Both windows are independent restricted theorems under the same frozen observer and parent dependencies. They do not imply the rest of the n=30 atlas is complete.

**Next:** study the general window index \(j\) and whether the pure-\(E\) to compulsory-mixture to pure-\(E\) pattern persists for every \(j\) before \(x\to1\); identify possible overlapping or disappearing windows as \(n\) varies, with exact discriminating certificates rather than extrapolating this pair. Independent FUQ/FUO premise review remains `NOT_REVIEWED`.

Provenance: historical researcher `EM-DIRECT-8454C6`, SID `MCP-44cfc4e6f2094f96861854ebefc77e84`, Activity `RA-ED136F89271FD89288F3E58D`. No current formal CLAIM/Result/Review is asserted.

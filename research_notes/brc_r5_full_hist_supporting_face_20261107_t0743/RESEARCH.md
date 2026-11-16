# R5: FULL_HIST supporting hyperplane, exact sharp ray and common exposed face

Date: 2026-11-07 Asia/Shanghai. Evidence: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Frozen science unchanged: Global \`a01383f825ef9d43b4b754254303298c64041568\`, EM \`86149263e38c22292c9def1e0f69092efa1be77e\`.
Current normative entry: \`docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context\`, current account bootstrap and manual, P000/ACTIVE Heartbeat worldview, project portable research and method record.
Predecessor: \`6bb05842783678c197f9a4bf7b05039fe99c2471\`, \`research_notes/brc_r5_unrestricted_early_gate_global_sharp_ray_20261107_t0640/\`.

## Main theorem

For the **unrestricted FULL_HIST** strategies on the frozen strictly positive four-stage P/Q tree, retaining each history-distinct central LR=1 branch separately until the observation, the four observations \`W=(eP,eQ,TP,TQ)\` obey the **global affine inequality**

\[
\boxed{\mathcal L(W):=21126(T_Q-1)-13604(T_P-1)-83401e_Q+114010(1-e_P)\ \ge 0.}
\]

This is a supporting halfspace of the entire FULL_HIST four-dimensional image; the same halfspace bounds the seedless-LR image. The face \(\mathcal L(W)=0\) is nonempty and **the two images coincide on that complete exposed face**. It is an observer-specific face theorem, with history retained in the carrier and in the proof.

For the previous critical ray \(\displaystyle W(h)=W_*+h(1,1,1,-1)\), with
\[
W_*=(161801/180000,6499/18000,267/80,137/40),
\]
we have the exact identity \(\mathcal L(W(h))=16917/20-232141h\). Therefore, on the ray, for **both** FULL_HIST and seedless LR and for every real \(h\ge0\),
\[
\boxed{W(h)\text{ attainable}\quad\Longleftrightarrow\quad 0\le h\le H:=16917/4642820.}
\]
The attaining LR strategies were constructed in the predecessor; this file independently verifies exact primal endpoint and interpolation. This closes the proposed FULL_HIST-versus-LR separation test on the critical ray: the sharp LR bound is a common FULL_HIST bound.

## Full history carrier and observer equations

Let \(g\) be early continuation and \(a,b\) the two time-2 history-specific continuation Q masses, \(0\le a,b\le g\le1\). Stage-3 continued Q masses on histories A and B are six independent flows \(0\le x_{Aj}\le V_{Aj}\), \(0\le x_{Bj}\le V_{Bj}\), where
\[
V_A=(13a/40,\ a/10,\ 3a/40),\qquad
V_B=(b/80,\ 9b/40,\ 21b/80).
\]
The stage-3 LR keys are respectively \((1/2,1,3/2)\) on either history. Put \(x_j=x_{Aj}+x_{Bj}\). The exact stage-4 terminal Q rows, ordered by terminal LR \((1/10,1,19/10)\), are \(A_0=B_0=(509,382,9)/900\), \(A_1=(47/180,43/90,47/180)\), \(B_1=(67/162,14/81,67/162)\), \(A_2=B_2=(9,382,509)/900\). In particular the central histories have **different** terminal distributions.

For stopped LR-bin order \(r=(1/10,1/2,3/4,1,5/4,3/2,19/10)\), the Q masses are
\[
\begin{aligned}
M_0&=509x_0/900+47x_{A1}/180+67x_{B1}/162+x_2/100,\\
M_1&=13a/40+b/80-x_0,\quad M_2=(g-a)/2,\\
M_3&=1-g+a/10+9b/40-x_1+191(x_0+x_2)/450\\
   &\hspace{2cm}+43x_{A1}/90+14x_{B1}/81,\\
M_4&=(g-b)/2,\quad M_5=3a/40+21b/80-x_2,\\
M_6&=x_0/100+47x_{A1}/180+67x_{B1}/162+509x_2/900.
\end{aligned}
\]
They satisfy \(\sum M_j=\sum r_jM_j=1\) for all real flows in this carrier. For \(0\le E_j\le M_j\), the aggregate stopped Q mass declared P, all four observations are exactly
\[
e_Q=\sum E_j,\quad e_P=1-\sum r_jE_j,\quad
T_Q=1+g+(a+b)/2+x_0+x_1+x_2,\quad
T_P=1+g+(3a+5b)/8+x_0/2+x_1+3x_2/2.
\]
The aggregate E variables discard no information needed for these four terminal observers: conditional declarations on each actual stopped history can realize any aggregate E at its LR bin. We do not collapse the two central continuation histories until after their distinct terminal rows have been applied. Other future provenance-sensitive observers retain their original history carrier.

## Exact dual decomposition and proof

Substitution of the above affine equations gives the **formal identity** for arbitrary real \(g,a,b,x_{Aj},x_{Bj},E_j\) (without needing feasibility):
\[
\begin{aligned}
\mathcal L(W)={}&4245(g-a)
 +11278(a/10-x_{A1})
 +\frac{200302}{9}(9b/40-x_{B1})\\
 &+72000(M_0-E_0)+26396(M_1-E_1)+6554(M_4-E_4)\\
 &+\frac{4213}{2}E_2+30609E_3+\frac{131331}{2}E_4
   +87614E_5+133218E_6.
\end{aligned}
\tag{D}
\]
Every summand is nonnegative on a legal FULL_HIST strategy. Thus \(\mathcal L(W)\ge0\) for **all real** FULL_HIST strategies.

The identity is affine in sixteen independent coordinates \((g,a,b,x_{A0},x_{A1},x_{A2},x_{B0},x_{B1},x_{B2},E_0,\ldots,E_6)\). The adjacent stdlib Fraction verifier checks (D) at the zero vector and at the sixteen unit vectors, exactly. These 17 coefficients certify equality as a formal identity over the reals, not as a finite random sample. It also checks \(\sum M=\sum rM=1\) by the same coefficient method.

On \(\mathcal L=0\), every strictly positive multiplier in (D) forces its slack to vanish. In particular \(g=a\), \(x_{A1}=a/10\), \(x_{B1}=9b/40\), \(E_0=M_0\), \(E_1=M_1\), \(E_4=M_4\), and \(E_2=E_3=E_4=E_5=E_6=0\). Hence \(M_4=0\) and \(b=g\): **\(g=a=b\)**, and both central stage-3 histories continue fully. Since side terminal rows agree across the two histories, their independent continuation flows influence W only through pooled totals \(x_0,x_2\), which fall in the pooled LR capacity intervals. The central continuation is automatically pooled with common probability one. A seedless LR policy using the same pooled \(x_0,x_2\) and aggregate declarations realizes exactly the same stopped histogram and four observations. Consequently,
\[
\mathcal O_4(\mathrm{FULL\_HIST})\cap\{\mathcal L=0\}
=
\mathcal O_4(\mathrm{LR})\cap\{\mathcal L=0\}.
\]
The reverse inclusion holds because LR strategies are FULL_HIST strategies.

## Sharp attainment and verified range

The predecessor's center uses \(g=a=b=77/80\), \(x=(3/16,3/10,1/80)\), \(E=(1297/6000,879/6400,0,563/144000,0,0,349/96000)\).
The endpoint uses \(g=a=b=31911/33163\),
\[
x=(3199433/18571280,\ 31911/102040,\ 220131/18571280),
\quad E=(886766809/4178538000,\ 1415873/9285640,\ 0,0,0,0,0).
\]
Both are seedless LR policies. Split each \(x_j\) into A/B flows in the fixed ratios \((26:1,4:9,2:7)\), respectively. Those ratios exactly match branch Q capacity shares when \(g=a=b\). The verifier checks all six branch capacity constraints, all seven \(E_j\le M_j\), both mass moments, and W for the center, endpoint and five rational interpolants. Their affine combination proves real attainment for all \(h\in[0,H]\), including irrational \(h\).

Output: \`PASS_FULL_HIST_LINEAR_IDENTITY_17_COEFFICIENT_CHECKS\`, \`PASS_FULL_HIST_EXACT_ENDPOINTS_AND_RAY_INTERPOLATION\`, \`PASS_FULL_HIST_AND_LR_EXPOSED_FACE_EQUALITY_CERTIFICATE\`.

## Evidence, scope, and next step

The exact verifier ran locally with Python stdlib \`fractions.Fraction\`; its stdout is saved in \`EXACT_OUTPUT.txt\` and its full executed code in \`VERIFY.py\`. The full-real conclusion follows from the algebraic identity, nonnegative slacks, and explicit affine constructions. No external numerical LP solver is part of the final certificate.

Mother question remains open away from the exposed face: decide \(\mathcal O_4(\mathrm{FULL\_HIST})=\mathcal O_4(\mathrm{LR})\) throughout the full original four-observer image. Next choose rational FULL_HIST observations with \(\mathcal L>0\) outside the established LR cubes and decide actual LR feasibility via the seven-variable \(K(W)\) and the pooling residual \(F=(A+B)J-X_1(\alpha A+\beta B)\); retain exact branch rows. Another route is to describe all FULL_HIST exposed faces and test which are pooled-LR reproducible.

Provenance: actual connected GitHub actor \`awdawmip\` with push permission. Current native gateway \`em_status\` and \`em_control_tasks\` both failed with \`BACKEND_IDENTITY_OR_VERSION_MISMATCH\` and \`operation_sent=false\`; active task owner and formal CLAIM therefore unconfirmed. This is independent author-side evidence, not a native Result/Review.

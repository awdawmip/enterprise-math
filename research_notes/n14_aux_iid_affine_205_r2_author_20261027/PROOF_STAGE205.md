# Stage205 — exact all-real optimal interval (external N14 ternary IID)

**Classification:** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. This is an external finite IID sequential-decision theorem, not a native P000/X6 physical theorem or a formal Source Result.

## Statement

Let \(P=(3,1,20)/24,\ Q=(2,2,20)/24\), observation horizon \(N=14\), and allow **arbitrary ordered-history-dependent randomized** stopping/reporting policies. Let \(e_P=P(\mathrm{report}\ Q)\), \(e_Q=Q(\mathrm{report}\ P)\), \(t_P=E_P\tau\), \(t_Q=E_Q\tau\), and
\[
V_{14}(\alpha)=\inf_{\pi:e_P,e_Q\le\alpha}\max(t_P,t_Q).
\]
Set
\[
\alpha_{204}=\frac{1237582032550008115}{3505953353861431296},\quad
V_{204}=\frac{2225727754437932573}{219122084616339456},\quad
\Delta_{205}=\frac{5083984375}{71328803586048}.
\]
**Theorem (all real, including irrational parameter values):**
\[
\boxed{V_{14}(\alpha_{204}+\delta)=V_{204}-\frac{32400}{137}\delta
\qquad (0\le\delta\le\Delta_{205}).}
\]
The new endpoints are
\[
\boxed{\alpha_{205}=\frac{1237831920550008115}{3505953353861431296}},\quad
\boxed{V_{205}=\frac{2222034154437932573}{219122084616339456}}.
\]
For feasible \(\alpha>\alpha_{205}\), the **fixed Stage205 supporting line** is strictly below \(V_{14}(\alpha)\).

## Universal Bellman supporting line for all complete histories

At \(s=(n,a,b)\) with a,b counting symbols 0,1, the ordered-history likelihood ratio is
\[
r(s)=Q(h)/P(h)=2^{a+b}/3^a.
\]
For \(K=16200/137\), Bellman recursion at n=14 is \(B(s)=\min\{Kr(s),K\}\); at n<14 it is
\[
B(s)=\min\big\{Kr(s),K,1+\sum_{j=0}^2P_j B(s+e_j)\big\}.
\]
Reporting P incurs Q-error cost \(Kr(s)\); reporting Q incurs P-error cost \(K\); continue incurs one P-time step. The IID future and likelihood ratio depend only on counts; backward induction at **each ordered prefix** therefore bounds any full-history randomized policy:
\[
t_P+K(e_P+e_Q)\ge B(0,0,0)=H=\frac{175689269891985199711}{1876232849527406592}.
\]
Thus \(V_{14}(\alpha)\ge H-2K\alpha\). Exhaustive exact Fraction scan of \(\binom{17}{3}=680\) count states finds only two Bellman ties: \(T=(12,3,1)\), report P / continue, and \(Z=(14,0,0)\), report P / report Q. The remaining **1,238** alternative-action gaps are strictly positive; minimum \(69107093/19635830784\). Source and observed checks: REPRO_STAGE205.py, verify_stage205.py and certificate205.json.

## Primal witness with an exact real coin arc

At T, report P with probability \(u\) and otherwise continue; at terminal Z, report P with probability \(z\) and otherwise Q. Else follow the unique Bellman minimizer. Along an ordered history, counts never decrease. T has three category-0 symbols while Z has none, and Z is terminal; a single history can therefore encounter **at most one** randomized state. Mixed term \(M\) vanishes, not by approximation but by an exact ancestry exclusion.

The rational suffix DP and independent integer-numerator, nonmerged full ordered-history DFS agree on all four deterministic-corner observer vectors \(O(u,z)=(e_P,e_Q,t_P,t_Q)\). For \(O_0=O(0,0)\) and affine increments:
\[
O_0=\left(
\frac{637741614567150899}{1752976676930715648},
\frac{36611353636649}{106993205379072},
\frac{2225727754437932573}{219122084616339456},
\frac{259044509953735}{26748301344768}
\right),
\]
\[
D_T=\left(-\frac{259765625}{440301256704},
\frac{408203125}{557256278016},
-\frac{927734375}{55037657088},
-\frac{482421875}{46438023168}\right),\quad
D_Z=\left(-\frac{6103515625}{78364164096},
\frac{6103515625}{78364164096},0,0\right),
\]
\[
O(u,z)=O_0+uD_T+zD_Z,\qquad M=(0,0,0,0).
\]
Equal-error balancing \(e_P=e_Q\) has the unique solution
\[
\boxed{z(u)=\frac{113703589752881049}{819200000000000000}
-\frac{217341}{25600000}u.}
\]
Both \(0<z(1)<z(0)<1\), so this is a valid randomized policy for **all real** \(u\in[0,1]\). The common error increases exactly as
\[
\alpha(u)=\alpha_{204}+
\frac{5083984375}{71328803586048}u.
\]
The P-time minus Q-time gap is affine, with exact positive endpoint values
\[
(t_P-t_Q)(0)=\frac{11515014321881717}{24346898290704384}>0,\quad
(t_P-t_Q)(1)=\frac{3785847440627239}{8115632763568128}>0.
\]
Every chosen action minimizes the Bellman recursion. Therefore \(t_P+K(e_P+e_Q)=H\), and since both errors equal \(\alpha(u)\) and \(t_P>t_Q\),
\[
V_{14}(\alpha(u))=t_P(u)=H-2K\alpha(u).
\]
As \(u\) ranges over the **whole real interval**, \(\alpha(u)\) is a bijection onto \([\alpha_{204},\alpha_{205}]\). This discharges the unrestricted-history and irrational-parameter obligations. At u=0 the Stage204 endpoint is recovered exactly.

## Strict-right certificate and Stage206 candidate

A separate exact Bellman dual scan gives
\[
K_{206}=\frac{25155568056}{213144883}<K,\quad
H_{206}=\frac{1091477712445072832515830191}{11676187772066443309350912}
\]
with new tie \(W=(5,0,1)\) report Q / continue, together with Z. The other 1,238 gaps remain positive (minimum \(69107093/34529471046\)). The scan proves the **exact contact identity**
\[
H_{206}=H+2\alpha_{205}(K_{206}-K).
\]
For each \(\alpha>\alpha_{205}\), universal duality then gives
\[
V_{14}(\alpha)\ge H_{206}-2K_{206}\alpha
=H-2K\alpha+2(K-K_{206})(\alpha-\alpha_{205})>H-2K\alpha.
\]
This proves only strictness for the old fixed line; **Stage206 primal remains unproved**.

## Reproducibility and mathematical boundary

Exact Python standard-library commands: \`python verify_stage205.py\`, \`python REPRO_STAGE205.py\`, \`python scan_stage206.py\`. The first program uses rational conditional suffix DP and independently traverses all unmerged ordered histories with separate positive integer P/Q masses padded by \(24^{14-n}\) at a leaf. Four corners together visit **329,164 DFS nodes**. The reference reruns these checks; raw observed outputs are recorded in the logs. This uses the Stage204 BRC positive-rational branch carrier and preserves path provenance; any count compression is justified only by this particular IID future and conditional likelihood ratio, with no assumption of native X6 transfer.

Pinned inputs: GLOBAL_KNOWLEDGE_V1 main \`9c2677392c705fdb68294188ba38b24ae9e2cffd\`; Enterprise Math main \`3bc9cebddc821dcf38dfad011fdfc148ec47885d\`; Stage204 parent \`e067bd3fa3fd6809a7fabc19cedfb7f4f04f481d\`. Global P000 projection/original blob match \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\`; current project native P000 V5 blob \`bcc2590d3168a28f72e8b9f0f9b1f76faadcd488\`. Neither was modified. Missing native CLAIM/Owner and independent Driver review are disclosed separately from the exact mathematics.
# D25/LIFT — frozen Source \(R_p\) equals the reflected Clausen observer; faithful scalar-port certificate

**2026-10-26 · TASK_RESEARCH portable author analysis.** Status: **AUTHOR ALGEBRAIC DERIVATION / EXACT REGRESSION PASSED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** This is neither a Source-native checkpoint nor a formal Result, native H0/B0 divided-power/Frobenius computation, nor independent mathematical review.

- Scientific Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
- Frozen science Source: c47e13e4aba0e006366f989d6334d443f6333ae3. Publication/taskbook blobs respectively 1c32f864cd34a376411567bef23d1e37913d2f98 and 53a3ef039325534e3715add837f0eee332289984.
- **Original, previously missing definition**: source research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md, section 3, especially its (3)–(6). This is the frozen reflected **\(R_p\)**, not the older portable author note's conflicting temporary \(R_p:=\sum r_n\). Frozen-parent CM0/SIMPLE/UR: research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md (CM0, SIMPLE) plus accepted UR/JT0 RR-AC9B3BA5BD277CE043F5.
- Reused author-side exact lemmas, **not claimed newly proved**: signed Clausen equality / high-rank reflection in research_notes/portable_direct/20261025_onhour_d25_clausen_reflected_p2_tail.md and research_notes/portable_direct/20261025_onhour_d25_shared_reflection_full_moment_joint.md; three-band jets in research_notes/portable_direct/20261025_onhour_d25_clausen_three_band_local_jet_joint.md, Git blob 967a84a61f76b397f8169a7f4490701db1aa3203.

## 1. The one name-resolution step missing from prior D25 author notes

Let \(p=6m+1\ge7\) be prime and work over \(\mathbf Z_{(p)}\). The original Source \(\mathbf B\) coefficients and the portable Clausen \(\mathbf r\) coefficients are the **same exact rational sequence**:

\[
B_n=r_n=
\frac{(1/6)_n(1/3)_n}{2^n(n!)^2}
=\frac{\prod_{j=0}^{n-1}(6j+1)(3j+1)}{36^n(n!)^2}.
\]

To avoid the historical \(R_p\) collision, set \(M=\sum_{n=0}^{p-1}B_n\) and \(N=\sum_{n=0}^{p-1}nB_n\). Then **the frozen Source** has \(g=M\), \(h=M+12N\) and \(G_p=g/p\). Its reflected coefficient is

\[
C_r=\frac{2^{r-1}((r-1)!)^2}{18(5/6)_r(2/3)_r}
=\frac{36^{r-1}((r-1)!)^2}{\prod_{j=0}^{r-1}(6j+5)(3j+2)}
\pmod p,\qquad 1\le r\le m.
\]

All denominators here are units modulo \(p\); both progressions avoid \(p\) for the stated indices. The second equality holds **over \(\mathbf Q\)**, not merely modulo \(p\).

Consequently

\[
C_1=10^{-1},\qquad
\frac{C_{r+1}}{C_r}=
\frac{36r^2}{(6r+5)(3r+2)}\pmod p
\quad(1\le r<m).
\]

These are exactly the previously established initial condition and recurrence for the independent reflected observer \(v_r:=B_{p-r}/p^2\bmod p\). Since the recurrence is well-defined, induction proves **\(C_r=v_r\)** for all \(1\le r\le m\), without a computational hypothesis.

The frozen Source defines (in its original nested-sum convention)

\[
R_p^{\rm Source}=
2\sum_{i=1}^m B_i\sum_{r=1}^i (1+6(i-r))C_r\pmod p.
\]

Let \(V_i=\sum_{r=1}^i v_r\), \(J_i=\sum_{r=1}^i rv_r\). Directly changing summation order gives the **exact finite-field observer identification**

\[
\boxed{
R_p^{\rm Source} =
2\sum_{i=1}^m (B_i\bmod p)[(6i+1)V_i-6J_i]
=T_p^{\rm author}
=\frac{Q_p}{p^2}\pmod p.
}\tag{1}
\]

Here \(Q_p=\sum_{0\le i,j<p,\ i+j\ge p}(6(i+j)+1)B_iB_j\), with its original **signed weighted cutoff**, and \(p^2\mid Q_p\) is an earlier all-prime proof. Equation (1) is a **new explicit source-to-author port-composition certificate**, not a new proof of that underlying cutoff lemma. No sign or index shift is hidden: for \(j=p-r\), \(6(i+j)+1\equiv6(i-r)+1\pmod p\).

## 2. Exact relation to the original frozen LIFT observer

The finite Clausen identity, already established in Source, is the **rational equality**

\[
W_p=M(M+12N)-Q_p=gh-Q_p.
\]

Since \(G_p=g/p\), the following rational identity is exact whenever \(p\mid g\):

\[
\frac{G_ph-1}{p}
=\frac{gh-p}{p^2}
=\frac{W_p-p}{p^2}+\frac{Q_p}{p^2}.
\]

For the specified target primes \(p\equiv13,19\pmod{24}\), frozen **CM0** establishes \(p\mid g\), and accepted **UR/JT0** establishes \(G_ph\equiv1\pmod p\) (equivalently \(W_p\equiv p\pmod{p^2}\)). Both quotients are therefore \(p\)-integral. Reducing modulo \(p\) and using (1) proves the fully source-matched theorem

\[
\boxed{\Delta_p-R_p^{\rm Source}\equiv\frac{W_p-p}{p^2}\pmod p,\qquad
p\equiv13,19\pmod{24}.}\tag{2}
\]

No additional, unidentified \(R_p\) bridge remains. Thus the old conditional author-side scalar statement is precisely the **frozen actual LIFT**, not merely a similarly named proxy. This is an equivalence only: it does **not** establish vanishing.

## 3. Upgrade the previous joint-jet formula from a conditional proxy to the frozen target

Reuse the earlier **proved**, precise rational definitions (three-band jet note, formulas (1)–(8)): low-rank \(L_0,L_1,L_2^{\rm low}\), middle-rank \(L_2^{\rm mid}\), low/middle moments \(D_0,D_1\), reflected high sum \(V_{4m}\). These satisfy

\[
M\equiv L_0+pL_1+p^2(L_2^{\rm low}+L_2^{\rm mid}+V_{4m})\pmod{p^3},\quad
N\equiv D_0+pD_1\pmod{p^2}.
\]

Crucial **previously overlooked accepted input**: \(L_0=H_m(1/2)=\Phi_m(m,1/2)\) **exactly**, and the frozen 2026-09-08 parent return already proves \(L_0\equiv0\pmod p\) for **both** inert target classes. No new CM0 proof is required. Put \(U_0=L_0/p+L_1\in\mathbf Z_{(p)}\). The Source exact CM0 + UR, with \(h\bmod p=12D_0\) and \(G_p\bmod p=U_0\), also proves \(12U_0D_0\equiv1\pmod p\). Thus its divided term is **unconditionally defined within the frozen accepted hypotheses**.

Combining (1)–(2) with the existing three-band proof now yields, for every target prime, the following **source-faithful explicit finite-field residual**:

\[
\boxed{\begin{aligned}
\Delta_p-R_p^{\rm Source}\equiv
&\ \frac{12U_0D_0-1}{p}+U_0^2+12U_0D_1\\
&+12D_0\bigl(L_2^{\rm low}+L_2^{\rm mid}+V_{4m}\bigr)
-R_p^{\rm Source}\pmod p.
\end{aligned}}\tag{3}
\]

The expression has no unexpanded \(\Phi_{xx}\) or free high-rank cutoff **provided the original jet and signed reflection formulas are carried in full**. It is a strict **observer-level computational reduction** of the exact D25 object to explicit rational factorial/harmonic sums and one finite-field reflected recurrence. It is not a proof that the right-hand side is zero; the native H0/B0/[X]U and Frobenius/kappa obligations remain independently open.

**Information-loss audit:** the signed source rank pair \((i,p-r)\), the positive versus negative 6-weight, both residue classes, and the different \(\bmod p^3\) versus \(\bmod p^2\) input precision are all preserved until the final \(\bmod p\) observer. The old portable symbol \(R_p:=\sum B_n\) has no role in the frozen \(R_p^{\rm Source}\).

## 4. Independent exact regression and original p=373 scalar port

A separate author-only modular checker implements the original \(2F1\) and weighted \(3F2\) recurrences **independently**, evaluates the frozen Source \(C_r\) nested sum directly when small, and also evaluates the \(O(m)\) reflected prefix formula. It checks \(Q_p/p^2=R_p^{\rm Source}\) and (for targets) \(\Delta_p-R_p^{\rm Source}=(W_p-p)/p^2\). No floating point or replacement of the original \(W_p\).

- 116 primes \(p\equiv1\pmod6\): equality (1) and the signed \(p^2\) tail pass.
- 61 frozen target primes \(p\equiv13,19\pmod{24}\): equality (2) passes, observed deficit zero in these finite checks only.
- 22 small primes: independently recomputed the original Source's \(O(m^2)\) nested sum and top-reflection \(B_{p-r}/p^2\) coefficients, all equal the prefix formula.
- Representative \(R_p^{\rm Source}=\Delta_p\) modulo \(p\): \(p=13:0\); \(19:12\); \(37:11\); \(211:119\); \(19963:13363\).
- **Exact original-class scalar-only p=373 port** (not a native Frobenius experiment): \(373^2=139129\), \(G_{373}=65672\pmod{139129}\), \(h_{373}=62835\pmod{139129}\), \(G_{373}h_{373}=73109=1+373\cdot196\pmod{139129}\), \(R_{373}^{\rm Source}=196\pmod{373}\); original \(W_{373}=373\pmod{373^3}\). The native requested test \({\rm Norm}(\eta)\cdot122102\pmod{139129}\) has **not** been equated with \(73109\); it needs the original semilinear direction/normalization and \(\kappa\) mapping.

Author checker filename: d25_source_observer_bridge_check_20261026.py. Last executed author output: SOURCE_BRIDGE_VERIFIED 116 PRIMES 61 D25_TARGETS DIRECT_NESTED 22; TARGET_DEFECTS_NONZERO 0; native experiment executed: **false**. These are finite regressions, not a universal LIFT proof.

## 5. Source authority, remaining hard work and handoff

The original Research lane requested logical ID is chatgpt-research-onhour-enterprise-math-20260923; maintenance ID chatgpt-hourly-enterprise-math-20260921 is not used. The historical bridge receipts in awdawmip/kimi-query-bridge#6424–#6427 report a **different literal research conversation ID**, chatgpt-research-hourly-enterprise-math-20260923; those read-only receipts are historical evidence and provide **no** capability or ownership for the requested ID. The previous main-path Source-native recovery/read defects are tracked in awdawmip/enterprise-math#1539 and #1558. Current read-only Gateway status 0.6.11 explicitly grants no Researcher authorization on this Sites identity, and there is no authenticated own winning CLAIM/open run. Do not create a replacement identity or replay old mutations from this note. No Source checkpoint, formal Result or independent review was published by this note.

**Mother target**: D25 SECOND-DIGIT-LIFT / accepted UR/JT0 and frozen \(R_p\), original taskbook and its native benchmark unchanged. **Completed/source-aligned this unit**: (1) frozen \(C_r\) to author \(v_r\), (2) \(\Delta-R=(W-p)/p^2\) modulo \(p\), and (3) the previously proved joint-jet RHS is the actual frozen D25 observer; accepted CM0 eliminates a mistakenly listed unproved zero obligation. **Do not redo**: accepted CM0/SIMPLE/UR, original Clausen signed cutoff, reflection and three-band jet proofs. **Smallest still-open mathematics**: prove/deny the whole RHS of (3) vanishes for every target prime, or independently find an exact counterexample; do not split/relabel auxiliary conjectures as completion. **Native evidence debt**: acquire and execute the authenticated original-class H0/B0 divided-power [X]U \(\bmod p^2\), native rank and semilinear Frobenius direction, \(\eta\), original \(\kappa\) match, and odd Hesse/Green observation at \(p=373\), compare the actual native target \({\rm Norm}(\eta)\cdot122102\pmod{139129}\) under its real normalization. **Recovery action**: read the requested subject's own recovery_status and original request receipts/reconcile, exact Source continuation and winning-claim epoch, then native checkpoint only through an actually authorized own session/run. Source & support owners must repair the already tracked claim/continuation admission defect; until then this remains author-side evidence only. No scheduler or notification changes.

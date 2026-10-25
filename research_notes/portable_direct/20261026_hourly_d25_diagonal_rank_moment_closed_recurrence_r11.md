# D25/LIFT — Corrected-Clausen diagonal moment closure with both cutoff traces

Date: 2026-10-26. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** unchanged. Research conversation \`chatgpt-research-hourly-enterprise-math-20260923\`; current Source-issued Researcher EM-ENTERPRISE-9C0A7C, activity RA-D8A85B2892C9E72E9097D30E (registration does not grant CLAIM). **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This external finite-hypergeometric result is neither a native CM experiment nor a Source checkpoint.

## Inherited inputs; newly resolved question

Use the corrected Clausen rank/Hasse equation from \`20261025_hourly_d25_clausen_operator_rank_boundary.md\` and the ordered three-channel Laurent masses/high-polar inverse from \`20261026_hourly_d25_three_channel_clausen_p4_residue_polar_r11.md\`. Prior generic labelled-carrier rank-moment independence remains valid.

New question: **for the constrained corrected-Clausen source itself, can degree-one and degree-two labelled-rank observers be recovered from difference-rank masses, the actual Pochhammer source boundary traces and no separately measured high-polar s=1,2 arrays?** Yes, with a p-adic unit recurrence even at the n=0 resonance.

Let m>=1 be an integer, p=6m+1 (prime for the p-local statement), and
\[
u_{a,r}=[t^a]\frac{(-m-t)_r(-2m-2t)_r}{(1-p/2-3t)_r\,r!},\quad 0\le r<p.
\]
Put u_{a,0}=1_{a=0}, and set u=0 at negative Hasse indices. The exact rational recurrence is
\[
\boxed{r(r-p/2)u_{a,r}=(r-1-m)(r-1-2m)u_{a,r-1}
+3r\,u_{a-1,r}-[3(r-1)-4m]u_{a-1,r-1}+2u_{a-2,r-1}.}\tag{1}
\]
For the oriented rank n=ell-j define, including its **source** labels,
\[
M_n^{ab,s}=\sum_{\substack{1\le j,\ell\le2m\\\ell-j=n}}
 j^s\,u_{a,j}u_{b,p-\ell},\quad s=0,1,2.
\tag{2}
\]
Outside n in [1-2m,2m-1] set M=0; set a<0 or b<0 streams to zero. The three needed channels, in causal order, are (0,2), (1,2), (0,3). The scalar Laurent mass from the inherited three-channel paper is c_n^{ab}=2^n M_n^{ab,0}, so the **original signed reflection cutoff is n<=0**. Since each high source has both numerator zeros, u_{0,p-ell}=u_{1,p-ell}=0 for ell=1..2m.

## Theorem A: exact diagonal Green/difference identity

Define
\[
C_n=(p-n)(p/2-n),\quad A_n=6m-2n,\quad B_n=-18m^2+9mn-n^2,
\]
and lower-Hasse coupling
\[
\begin{aligned}
J_n^{ab}={}&3M_n^{a-1,b,1}-3M_{n+1}^{a-1,b,1}
+4mM_{n+1}^{a-1,b,0}+2M_{n+1}^{a-2,b,0}\\
&-3((p-n)M_n^{a,b-1,0}-M_n^{a,b-1,1})\\
&+(14m-3n)M_{n+1}^{a,b-1,0}
-3M_{n+1}^{a,b-1,1}-2M_{n+1}^{a,b-2,0}.
\end{aligned}
\tag{3}
\]
The **two-sided, oriented** finite boundary term is
\[
E_n^{ab}=\begin{cases}
(2m^2{\bf1}_{a=0}+4m{\bf1}_{a=1}+2{\bf1}_{a=2})u_{b,p-n-1}\\
\qquad+u_{a,2m-n}(-6m^2u_{b,4m}+8m u_{b-1,4m}-2u_{b-2,4m}),
&n\ge0,\\
u_{a,-n}(20m^2u_{b,p-1}-14m u_{b-1,p-1}+2u_{b-2,p-1})\\
\qquad+u_{b,p-(2m+n+1)}(2m u_{a-1,2m}-2u_{a-2,2m}),
&n<0.
\end{cases}\tag{4}
\]
Then for every admissible n, a,b,
\[
\boxed{(p-2n)M_n^{ab,1}-C_nM_n^{ab,0}
=A_nM_{n+1}^{ab,1}+B_nM_{n+1}^{ab,0}+J_n^{ab}+E_n^{ab}.}\tag{5}
\]

**Proof.** Multiply (1) at rank r=j by u_{b,p-ell}; multiply the reflected instance at r=p-ell by u_{a,j}; sum each over ell-j=n and subtract. The unshifted quadratic weights cancel:
\[
r(r-p/2)|_{r=j}-r(r-p/2)|_{r=p-\ell}
=(p-2n)j-(p-n)(p/2-n).
\]
The j-to-j-1 and ell-to-ell+1 shifts both change the difference to n+1. At the common shifted (j',ell'=j'+n+1) cell,
\[
(j'-m)(j'-2m)-(5m+1-\ell')(4m+1-\ell')
=(6m-2n)j'+B_n.
\]
Their lower Hasse pieces give (3). The shifted left sum includes j'=0 but omits j'=2m; the right includes ell'=2m+1 but omits ell'=1. Reinstating the declared 1..2m carrier, with no infinite-series extension, gives exactly (4). This proves (5) as a rational identity. QED.

## Theorem B: mass-to-first-moment unit reconstruction (no division by p)

For every target prime p=6m+1 and every n in the stated range,
\[
A_n=2(3m-n),\qquad m+1\le3m-n\le5m-1<p.
\]
Therefore A_n is a p-local **unit** and (5) determines
\[
\boxed{M_{n+1}^{ab,1}=A_n^{-1}
[(p-2n)M_n^{ab,1}-C_nM_n^{ab,0}
-B_nM_{n+1}^{ab,0}-J_n^{ab}-E_n^{ab}].}\tag{6}
\]
Initially n_*=1-2m has the sole carrier j=2m,ell=1, hence
\(M_{n_*}^{ab,1}=2mM_{n_*}^{ab,0}\).
Compute channel (0,2), then (1,2) and (0,3); the lower-Hasse moments appearing in J are already known. Advance to n=2m-1 and verify the empty terminal \(M_{2m}^{ab,1}=0\).

Solving the *other direction* at n=0 would divide by p-2n=p, which is **not** permitted over Z_(p)/p². Formula (6) instead runs in the unit direction, preserves the diagonal n=0 source, and works mod p^r for every r. The restriction to the actual source and its retained boundary traces is essential; it does not refute the earlier unrestricted signed-cell moment counterexample.

## Theorem C: backwards s=2 reconstruction

With the first moments from (6), the un-subtracted **left** recurrence (1) gives
\[
\begin{aligned}
\boxed{M_n^{ab,2}}={}&M_{n+1}^{ab,2}
+\tfrac p2M_n^{ab,1}-3mM_{n+1}^{ab,1}
+2m^2M_{n+1}^{ab,0}\\
&+3M_n^{a-1,b,1}-3M_{n+1}^{a-1,b,1}
+4mM_{n+1}^{a-1,b,0}+2M_{n+1}^{a-2,b,0}+L_n^{ab},
\end{aligned}\tag{7}
\]
where
\[
L_n^{ab}=\begin{cases}
(2m^2{\bf1}_{a=0}+4m{\bf1}_{a=1}+2{\bf1}_{a=2})u_{b,p-n-1},&n\ge0,\\
(2m u_{a-1,2m}-2u_{a-2,2m})u_{b,p-(2m+n+1)},&n<0.
\end{cases}\tag{8}
\]
**Proof.** Substitute j'=j-1 into the left quadratic coefficient of (1), giving j'^2-3mj'+2m², and retain the two missing/included shifted endpoints (8). The lower Hasse terms provide the second line in (7). Starting at the empty rightmost rank \(M_{2m}^{ab,2}=0\), iterate n backwards. QED.

**Observer consequence.** For this *restricted* three-channel hypergeometric family, the entire degree-<=2 labelled-rank observer is determined by the three **s=0** mass arrays and the explicitly retained source boundary traces. After generating these inputs, recovering s=1,2 takes O(m) ring operations, excluding arithmetic bit cost. This does not delete the boundary records, identify CM Frobenius, or prove cancellation of the original lower-triangle reflection.

## Reproducible exact checks

Companion check script independently builds jets via Pochhammer polynomial multiplication and recurrence (1), computes every s=1,2 cell moment directly, and compares against the reconstruction using only supplied s=0 masses and actual boundary jets. **PASS:** 330 rational moment checks at m=1..5 (including algebraically valid p=25), plus **8,820** modular moment checks for all 22 primes p=6m+1 in [7,211] modulo p². Every n=2m terminal first moment vanishes. At p=13, n=0, triples (M0,M1,M2) mod169 are (83,158,139) for (0,2), (16,110,142) for (1,2), and (118,111,97) for (0,3). These are **author** checks, not independent mathematical review or native CM experimental verification.

## BRC and next exact unit

BRC COMPOSE_APPLIED: retain original (j,ell,n), source Hasse channel, signed cutoff and p-adic precision through all shifts. The proven compression applies only to the declared observer and corrected source; the Laurent variable is an **external algebraic device**, not a native P000 plane.

**Next mathematical action:** transport the reconstructed quadratic observer through the **lower-triangle** n<=0 with all four cutoff faces, and determine the genuine coupled WZ/adjoint boundary flux (prove exact cancellation or furnish a nonzero exact residue). Separately, the Source-native frontier still requires original-class H0/B0, [X]U mod p², semilinear direction/eta and kappa/Delta-R comparison; native CM experiment NOT_RUN, independent review pending. Parent D25/LIFT/JT2 **OPEN**.

Latest own read-only recovery: new registered service session \`MCP-22fdc1ed9a2d44d8bcf5fd6b5cf810dd\`, no pending mutation/run/claim/unpublished upload; historic neutral staging preserved. Current native continuation: checkpoint \`SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED\`, HANDOFF_READY / NEEDS_DISPATCH, no authorized run; last claim MCP-d0d70cd041b01e5db192870a differs from checkpoint predecessor MCP-87631b892b41fa18d799f2d8. Control support: \`awdawmip/enterprise-math#1558\`. Portable GitHub storage is **not** an authenticated CLAIM, native checkpoint, Result, review or admitted theorem.

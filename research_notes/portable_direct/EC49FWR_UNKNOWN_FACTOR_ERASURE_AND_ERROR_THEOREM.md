# EC49FWR — Optimal erasure-resilient observation and a sharp adversarial-error obstruction with an unknown CRT factor

Date: 2026-11-22, Asia/Shanghai. Research family: frozen BRC16943; static auxiliary ten-period / odd CRT model, not native X6 dynamics. Parent scientific pin: EC49FWQ \`d091c8f2757f67c18be8056ae976b1e092a21098\`. Further exact-census dependencies: EC49FWJ \`95ab4672c9251e155c44049b007330277fa83603\`, EC49FWO \`940ad416fa1eb47904b93860ea5364e869e3de74\`. Status: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Problem and exact observer

Let \(\mathcal F\) be the **50** distinct binary supports \(U\subseteq\mathbb Z/10\mathbb Z\) derived from the frozen 44-cell P10 certificate under 72 primitive affine directions. Fix any **odd** \(q\ge3\), \(\gcd(q,10)=1\). An unknown nonempty \(V\subseteq\mathbb Z/q\mathbb Z\) gives a CRT product \(W=U\times V\). The observer receives its **complete indexed** reflection-defect array
\[
D_W(a,b)=|W\triangle((a,b)-W)|
\]
and may measure Boolean membership at **distinct physical sites** \((j,v)\in\mathbb Z/10\times\mathbb Z/q\). Full-spectrum measurement and its computation are assumed available and are not included in the physical membership-probe count; repeated readings of the same site do not create extra physical coordinates in this model.

A fixed set \(Q\) is selected before the spectrum is known. An adaptive set may be selected after receiving the complete spectrum, but before its membership bits. The target is exact reconstruction of \(U\), with up to \(e\) **erasures at known probe locations**, or up to \(t\) arbitrary **incorrect bits at unknown locations**. These are worst-case adversarial errors; no statistical noise assumption.

## Theorem: sharp worst-case erasure cost

For the above population, the minimal Hamming distance between the membership codewords belonging to distinct \(U\)'s with identical indexed reflection spectra is at least \(r\) if and only if, for **every** \(v\in\mathbb Z/q\), the fixed probes \(Q_v=\{j:(j,v)\in Q\}\) satisfy
\[
|Q_v\cap A|\ge r,\qquad |Q_v\cap B|\ge r,\qquad |Q_v\cap C|\ge r,
\]
where
\[
A=\{1,4,6,9\},\quad B=\{2,7\},\quad C=\{3,8\}.
\]
This is feasible exactly for \(r=1,2\) (among positive integers). Hence
\[
\boxed{\begin{aligned}
e=0:&\quad N_{\rm fixed}=3q,\quad \#\text{optima}=16^q;\\
e=1:&\quad N_{\rm fixed}=6q,\quad \#\text{optima}=6^q;\\
e\ge2:&\quad \text{no distinct-site fixed scheme exists}.
\end{aligned}}
\]
For a **spectrum-adaptive** observer the corresponding worst-case minimum is **1** probe with no erasure and **2** with one erasure; \(e\ge2\) is impossible in the stated physical model. Singleton spectrum fibers require no probes.

For \(q=11\), one adversarial erased membership reading changes the fixed optimum **33 → 66** sites; there are **\(6^{11}=362\,797\,056\)** optimal 66-site layouts. One explicit optimum takes \(j\in\{1,2,3,4,7,8\}\) in **every** CRT column \(v\).

**One arbitrary unknown erroneous membership bit cannot be guaranteed correctable even if every physical site is measured, with either fixed or fully spectrum-adaptive site selection.** The same impossibility holds for any \(t\ge1\).

## Proof

1. The parent FWQ's exact P10 finite census gives 38 distinct indexed ten-cycle defect signatures among 50 supports, with 12 two-element fibers and no larger fiber. The nonempty supports on which members of a ten-cycle fiber disagree are exactly
\[
\mathcal D=\{\{0,\dots,9\},\{1,2,6,7\},A,\{2,4,7,9\},B,\{3,4,8,9\},C\}.
\]
Importantly, \(A,B,C\) occur as **three distinct equal-cardinality** colliding pairs, and are pairwise disjoint. Each element \(D\in\mathcal D\) **contains at least one of** \(A,B,C\).

2. The parent FWQ odd-factor inversion/fiber statement establishes that if two allowed product states with *distinct* \(U,U'\) share the **complete indexed** \(D_W\), their CRT factor is the **same** nonempty \(V\); their ten-cycle \(U,U'\) belong to a defect doubleton. Thus their membership words differ precisely on
\[
(U\triangle U')\times V=D\times V.
\]
In particular the Hamming distance seen at \(Q\) is \(|Q\cap(D\times V)|\). This step depends on the cited parent inversion theorem and its precise domain; it is not a native dynamics statement.

3. For necessity, fix **any** column \(v\) and set \(V=\{v\}\). The three equal-cardinality defect-doubleton pairs whose differences are \(A,B,C\) retain identical **complete product** spectra for the same singleton factor, by
\[
D_W(a,b)=2\bigl(|U||V|-K_U(a)K_V(b)\bigr).
\]
Consequently each of \(|Q_v\cap A|, |Q_v\cap B|, |Q_v\cap C|\) must be at least \(r\).

4. Conversely, take any colliding pair, let its difference be \(D\in\mathcal D\), and choose an active column \(v\in V\). Some group \(G\in\{A,B,C\}\) lies inside \(D\). The assumed \(|Q_v\cap G|\ge r\) produces at least \(r\) differing observed membership bits. So the conditions are sufficient.

5. Since \(A,B,C\) are disjoint with sizes \(4,2,2\), for \(r=1\) precisely three probes per column are required, with \(4\cdot2\cdot2=16\) minimal layouts per column; for \(r=2\) precisely six probes per column, with \(\binom42\binom22\binom22=6\) layouts per column. For \(r>2\), the singleton-column witness associated with \(B\) has only two differing physical coordinates, so no site selection can achieve distance \(r\).

6. To uniquely decode after \(e\) known erasures, two candidate codewords need minimum distance \(e+1\): after deletion of any \(e\) coordinates, at least one distinguishing bit must remain. For \(t\) unknown errors, the Hamming spheres of radius \(t\) must be disjoint, requiring distance at least \(2t+1\). The preceding paragraph gives a universal upper bound of 2 on possible distance (even when all sites are inspected), so \(t\ge1\) is impossible. In particular, the two codewords at distance two have a common received word at distance one from each, yielding an exact decoding ambiguity.

7. The complete spectrum fiber contains at most two states. The adaptive observer, after examining the spectrum, chooses one or two sites in the two candidate states' difference as needed. Every distinct candidate pair has \(|D||V|\ge2\). The singleton \(V\) and \(B\) witness proves both adaptive lower bounds and the limit \(r\le2\).

All statements count distinct physical *membership sites*. If the measurement apparatus supports independent repeated observations of one site or alternative redundant encodings, the error model changes and the above impossibility does not address that altered system.

## Exact finite crosscheck

The companion standard-library Python program independently rebuilds the frozen P10 parity/slope predicate and 72 primitive directions, obtaining 50 supports, 38 ten-cycle spectrum signatures, 12 doubletons and the seven differences above. It enumerates every nonempty \(V\) for \(q=3,7,11\), respectively **350, 6,350, 102,350** product states; all product spectrum fibers have cardinality at most two, and each nontrivial pair shares the same \(V\). With universal 3q-layout \(j=\{1,2,3\}\), exact minimum distance is 1; with universal 6q-layout \(j=\{1,2,3,4,7,8\}\), exact minimum distance is 2, for each of the three q. Program output is \`ALL PASS\`. The analytical all-odd-q assertion additionally uses the cited parent exact-fiber theorem.

Files in this research unit:
- \`EC49FWR_UNKNOWN_FACTOR_ERASURE_AND_ERROR_THEOREM.md\`
- \`EC49FWR_BLIND_CRT_ERASURE_VERIFY.py\`
- \`EC49FWR_BLIND_CRT_ERASURE_OUTPUT.json\`

## Meaning, preservation and next discriminating question

This is a **static indexed CRT auxiliary-model theorem** under frozen BRC16943; it does not replace or alter P000's six native spatial axes, the three-dimensional slice, joint observer preservation or the native Farey transition. The result identifies a concrete threshold: if the unknown CRT factor may have singleton support, spatial replication across the other columns supplies no worst-case fault protection. Any actual error correction must introduce a new independently measured resource, a restricted factor family, or a verified dynamical observer with extra distinguishing information.

Next: obtain a source-pinned same-trace correspondence from a frozen P10 support \(U\), the mod-11 factor \(V\) and anchor/height to the actual Farey successor observation; test whether successor observations distinguish equal static spectra and whether an additional observer changes the singleton-factor two-position obstruction. Do not infer a dynamic compression claim without that bridge.

## Authority and provenance

This note was prepared as independent portable research on the *unpublished* topic label \`RS-EC49AS\`, referencing EC49FWQ without assuming its PR is merged or canonically reviewed. It neither asserts a current native session/Activity or Task CLAIM nor modifies shared Result, Review, P000 or another owner's run.
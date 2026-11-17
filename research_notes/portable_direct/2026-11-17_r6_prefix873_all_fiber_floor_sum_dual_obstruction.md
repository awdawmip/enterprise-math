# PREFIX-873 — Exact all-residue fiber arithmetic, time-reversal obstruction, and intrinsic single-port collisions

Date: 2026-11-17. Scientific continuation: PREFIX-872 (all \`r=0\` capacities and 46 extremal counterexamples), PREFIX-871 (p=32 boundary). Frozen scientific-input pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unchanged).
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Defined object and role

This is the auxiliary named-binary-source BRC *observer*: a source state is \(u=\sum_{i=0}^{p-1}2^i x_i\), with \(x_i\in\{0,1\}\), \(N=2^p\). A legal heartbeat is \((u,u)\) or \((u,u\oplus2^i)\). The observation \(\Phi_{q_1,q_2}(u,v)=(u\bmod q_1,v\bmod q_2)\) uses two fixed positive odd moduli. Recovery means injectivity on the complete **ordered, signed and named** set of transitions; in particular, no change is a distinct legal event. No claim of native X6 Cell/Link/Port equivalence or physical law is made.

We retain actual transition, identity, sign and coupled residues. This is an exact arithmetic tool to improve the scope of PREFIX-872; it does not discard composite/joint observers.

## Theorem 873-A — All first-residue fiber occupancies by Euclidean floor sums

Fix \(p,q_1,q_2\) and \(g=\gcd(q_1,q_2)\). For any \(0\le r<\min(q_1,N)\), let
\[
m_r=1+\lfloor(N-1-r)/q_1\rfloor,\quad
F_j(r)=\sum_{k=0}^{m_r-1}\left\lfloor\frac{r+kq_1}{2^j}\right\rfloor,\quad 0\le j\le p.
\]
Write \(b_{r,i}=F_i(r)-2F_{i+1}(r)\). Then \(b_{r,i}\) is *exactly* the number of old states in the \(r\)-fiber whose \(i\)-th named bit equals 1, and
\[
\boxed{
T_{r,a}=m_r[a\equiv0\bmod g]+
\sum_{i=0}^{p-1}\!\bigl((m_r-b_{r,i})[2^i\equiv a\bmod g]
+b_{r,i}[-2^i\equiv a\bmod g]\bigr).}\tag{873.1}
\]
For \(r\ge N\) the fiber is empty.

**Proof.** Its old states are precisely \(r+kq_1\), \(0\le k<m_r\). The identity
\(\operatorname{bit}_i(u)=\lfloor u/2^i\rfloor-2\lfloor u/2^{i+1}\rfloor\)
gives the exact bit-one count. An unchanged event contributes increment zero. Flipping bit \(i\) contributes \(+2^i\) when that bit is zero and \(-2^i\) when it is one. Partition by increment residue, sum each contribution, and obtain (873.1). QED.

Each \(F_j\) is the standard *integer* floor sum \(S(n,m,a,b)=\sum_{k=0}^{n-1}\lfloor(ak+b)/m\rfloor\), calculated by Euclidean reduction: split the integral quotients of \(a,b\) by \(m\), then exchange \(a,m\) after passing from \(an+b\) to its quotient and remainder. The checked C++17 implementation contains the exact algorithm. Its inner cost is \(O(\log 2^j)\) Euclidean steps; all \(r\) are evaluated without enumerating the entire \(N=2^{32}\) old-state population. This is a method/certificate improvement, not a new universal optimal bit-width claim.

## Theorem 873-B — Time-reversal dual fiber bound

The legal transition relation is symmetric: \((u,v)\) is legal iff \((v,u)\) is legal. Hence \(\Phi_{q_1,q_2}\) is injective **if and only if** \(\Phi_{q_2,q_1}\) is injective. Moreover, if \(U_{s,a}\) is the count of legal transitions with \(v\equiv s\pmod{q_2}\) and \(u-v\equiv a\pmod g\), injectivity forces \(U_{s,a}\le q_1/g\). Proof: reverse transitions and apply PREFIX-872's first-fiber pigeonhole theorem. This applies to complete ordered transitions, not a lossy unordered-edge quotient.

## Theorem 873-C — Intrinsic signed-power obstruction at each single port

Suppose \(q_1,q_2\) are positive odd moduli and some \(1\le d<p\) has
\(2^d\equiv 1\pmod{q_j}\) or \(2^d\equiv-1\pmod{q_j}\), for either \(j=1\) or \(2\).
Then \(\Phi_{q_1,q_2}\) is **not injective**, regardless of the other modulus.

**Proof for the second port.** For \(2^d\equiv1\), take old state \(u=0\). The two distinct legal toggles \(0\to1\) and \(0\to 2^d\) have the same old-state residue and the same new-state residue modulo \(q_2\). For \(2^d\equiv-1\), take \(u=1\). The distinct toggles \(1\to0\) (bit 0) and \(1\to1+2^d\) (bit \(d\)) collide at the second port. For the first port reverse both ordered transitions (Theorem B). The case \(q=1\) is included. QED.

For \(p=32,Q=2^{19}-1=524287\), exact checking of every **odd** \(q\in[1,Q]\) finds 385 of 262,144 moduli with this local obstruction, including 24 with \(q>Q/2\). The independent Python and C++ integer loops agreed. In particular, \(q=524287\) is excluded by \(2^{19}\equiv1\pmod q\); hence both orientations of the \(g=1\) extremal pair \((524287,524285)\) fail without cross-port search.

## Complete computed profile for the PREFIX-872 extremal family

For the 23 gcds
\(\{1,3,5,7,9,11,13,15,19,21,23,25,27,29,35,37,39,47,49,53,55,59,61\}\)
take \(A_g=\max\{a\le Q/g:a\ \text{odd}\}\), then both orientations \((gA_g,g(A_g-2))\) and \((g(A_g-2),gA_g)\). The C++17 checker evaluates **every** first-port residue \(0\le r<q_1\) and every increment class modulo \(g\), using (873.1), for all 46 ordered pairs. There were 24,114,624 individual \(r\)-fiber evaluations.

Exactly five high-first pairs violate \(T_{r,a}\le q_2/g\) (none of the low-first pairs violates this **first-port** bound). Below, \`violating_ra\` counts ordered \((r,a)\) class failures; \`max_excess\` is the largest excess over \(q_2/g\), at the displayed witness:

| g | q1 | q2 | violating_ra | max_excess | witness (r,a) |
|---:|---:|---:|---:|---:|---|
|15|524265|524235|316480|2095|(4,11)|
|21|524265|524223|488776|3710|(1,20)|
|27|524259|524205|172780|1068|(1,26)|
|35|524265|524195|276900|1407|(0,6)|
|39|524277|524199|1217652|2943|(0,7)|

All other 41 first-port cases have zero violations. In total, 2,472,588 \((r,a)\) failures occur within the five failing configurations. An independently written Python direct enumerator of \(u=r+kq_1\), including all 32 flips and the unchanged event, reproduced all ten selected max-witness margins for these five gcds in both orientations. Earlier PREFIX-872 \`r=0\` analysis already identified exactly those five gcds; the all-residue computation proves **that no additional gcd from this specific 46-pair extremal family is excluded by this particular first-port capacity test**.

By Theorem B, the reverse five ordered pairs fail the corresponding **dual, second-port** bound. Theorem C separately excludes both \(g=1\) orientations. Thus these arithmetic obstructions, without searching complete collision trajectories, exclude **12 of the 46 concrete ordered pairs** (five high-first, five reverse, two \(g=1\)); the PREFIX-872 explicit collision certificates remain the exclusion evidence for the remaining 34 pairs. These are concrete configurations, not the full 19-bit domain.

## Verification and provenance

- Program: \`PREFIX873_R6_ALL_FIBER_FLOORSUM_CHECK.cpp\`, C++17 exact 64-bit unsigned integer arithmetic. \(p=32\), with \(q_j<2^{19}\), makes each used floor-sum intermediate and fiber count smaller than \(2^{64}\). It prints all 46 case rows.
- Summary evidence: \`PREFIX873_R6_ALL_FIBER_RESULTS.json\` lists the exact family generator, totals, the five positive rows, the local single-port count, and checked scope. Runtime of one local optimized build for 46 full profiles was 31.83 seconds; this is a measured run, not an asymptotic performance guarantee.
- Cross-check A: Python direct state/flip enumeration of the five high-first maximum witnesses and their five low-first counterparts reproduced the expected excesses \((2095,0,3710,0,1068,0,1407,0,2943,0)\) in that order. Cross-check B: separate C++ and Python power-modulo scans both found 385 intrinsically invalid odd single ports (24 above \(Q/2\)).
- The calculation uses exact integer floor, XOR, modular classes, no floating-point approximations or historical stochastic claims.
- Input science: PREFIX-871/872 exact auxiliary observer and frozen pin \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; current behavioral rules read separately. Mathematical status is author proof plus finite exact regression. No independent theorem review, formal proof assistant acceptance, native X6 fidelity, formal Task CLAIM, Result or Review is claimed.

## Next discriminating research

Use (873.1) to scan *non-extremal* \((q_1,q_2)\) within the p=32, B=19 width and gcd filters, exploiting the 873-B reversal symmetry and the 873-C per-port filter. Determine whether a complete gcd subfamily can be excluded without full transition enumeration. A mathematical breakthrough requires a genuine all-pairs no-go or a valid 19-bit witness; the present sharp global interval remains \(B_{\mathrm{fix,odd}}(32)\in\{19,20\}\). For p=62, g=1, apply the same pair symmetry and signed-power filter before designing a larger-capacity collision certificate.

**Ownership:** independent portable auxiliary BRC research; no live \`RS-X6-NATIVE-TIME-DYNAMICS\` execution claim asserted. The formal Task owner/continuation and native authenticated effects are separate control records.

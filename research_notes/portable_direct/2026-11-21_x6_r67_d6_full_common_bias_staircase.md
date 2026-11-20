# X6 R67 — Complete D=6 common-bias positive-BRC star-moment minimax staircase

Date: 2026-11-21 (Asia/Shanghai). Scientific status: **CONDITIONAL_AUTHOR_PROOF / TWO_EXACT_FINITE_CERTIFICATES / POSITIVE_NAMED_BRANCH_CHECK / NOT_INDEPENDENTLY_REVIEWED**.

## Scientific scope and provenance

This paper continues R61–R66. Scientific P000 is frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`; current behavior rules were loaded separately. The parent world has six native spatial axes, one distinct time dimension, Cell/Link/source provenance, and primitive stable \`TRIADIC_CLOSURE_E\` events. This is a **conditional** strictly positive weighted BRC **branch-family observer** theorem, not an identified native time-evolution law.

R66 established the complete D=5 staircase and R65 established an all-D half-radius onset. This paper finishes the next dimension D=6, including all intermediate Port populations. The actual canonical RS-X6-NATIVE-TIME-DYNAMICS control snapshot of 2026-11-21 04:09 Beijing time records another holder \`EM-X6-FB6990\` and a lease; this portable proof makes **no Task CLAIM, PROGRESS, Activity mutation, or owner takeover**. \`EM-X6-214D9C\` is historical lineage only, not a newly attested session identity.

## Positive BRC observer and exact theorem

Fix an integer \(p\ge6\). A named \(p\times p\) Boolean relation has \(r_i\in\{0,\ldots,6\}\) successful B Ports at each named A Port \(i\). Each experiment chooses the *same* A Port and \(t\) independently reset B Ports; individual AB branches retain both source names, the A-Port label, ordered B-Port labels, and positive rational weights \(u,v>0\). The exact positive branch mass is
\[
Z_t=(uv)^t\sum_{i=1}^{p}r_i^t,\quad m_t=Z_t/(uv)^t=\sum_{d=0}^{6}c_dd^t,\quad t=1,\ldots,6,
\]
where \(c_d\) counts A Ports of success degree \(d\), \(\sum c_d=p\). This equality counts typed named branches and does not identify positive mass with complex amplitude.

Read six channels with one arbitrary real shared additive bias and bounded per-channel errors:
\[
y_t=m_t+b+e_t,\qquad |e_t|\le\eta.
\]
The target is precisely the high-degree subhistogram \((c_2,c_3,c_4,c_5,c_6)\); \(c_0,c_1,b\) remain nuisance data.

**Theorem (all integer \(p\ge6\)).** The first *closed* measurement error radius admitting a pair of realizable networks with distinct targets but compatible readings equals
\[
\boxed{\eta^*_{p,6}=
\begin{cases}
31/2,&6\le p\le20,\\
15,&21\le p\le40,\\
12,&41\le p\le56,\\
1/2,&p\ge57.
\end{cases}}
\]
Every \(\eta<\eta^*_{p,6}\) guarantees uniqueness of the high-degree histogram. At equality the listed witnesses give a shared observation. Exactly three downward population transitions occur: **21, 41, 57**.

## Proof: common-bias quotient and exact feasibility

Let \(a_d=c_d-c'_d\), for \(d=2,\ldots,6\), and \(\Delta_t=m_t(c)-m_t(c')\). Degree-zero differences vanish for \(t\ge1\); degree-one differences add the *same constant* for every \(t\). Hence the bias-invariant differences are
\[
z_1=0,\qquad z_t=\Delta_t-\Delta_1=\sum_{d=2}^{6}a_d(d^t-d),\qquad 2\le t\le6.
\]
Set \(\operatorname{osc}(0,z_2,\dots,z_6)=\max(0,z_2,\ldots,z_6)-\min(0,z_2,\ldots,z_6)\). Two models can share observed values with errors \(|e_t|\le\eta\) iff their means can be shifted by their unknown biases to within \(2\eta\) uniformly. Optimal centering of the range gives
\[
\boxed{\eta_{\rm pair}=\operatorname{osc}(0,z_2,\ldots,z_6)/4}.
\]

A signed integral \(a=(a_2,\dots,a_6)\) is realizable at population \(p\) iff
\[
\boxed{q(a):=\max\left(\sum_{d=2}^{6}(a_d)_+,\sum_{d=2}^{6}(-a_d)_+\right)\le p.}
\]
Necessity is by counting positive/negative high-degree deviations. For sufficiency choose \(c_d=(a_d)_+\), \(c'_d=(-a_d)_+\) for \(d\ge2\), fill the two degree-zero entries independently up to \(p\), and realize each row by its first \(d\) labelled B Ports (possible because \(d\le6\le p\)). All source weights may be any strictly positive rational values and normalized away.

## Proof: exhaustive *inverse* certificate (all p, no population truncation)

The degree-two vector \(a=(1,0,0,0,0)\) is feasible already at \(p=6\) and has \(z=(2,6,14,30,62)\); hence the candidate minimum oscillation is at most \(62\). Since every \(d^t-d\) is even, all five \(z_t\) are even integers. Any possible **strict improvement** must satisfy \(0<\operatorname{osc}<62\), hence each of \(z_2,\ldots,z_6\) lies in \(\{-60,-58,\ldots,60\}\). This is exactly \(61^5=844,596,301\) possibilities; no bound on \(p\) was assumed.

The integer moment-difference matrix \(z=Ma\) is
\[
M=\begin{pmatrix}
2&6&12&20&30\\
6&24&60&120&210\\
14&78&252&620&1290\\
30&240&1020&3120&7770\\
62&726&4092&15620&46650
\end{pmatrix},\qquad \det M=24,883,200.
\]
Write \(720M^{-1}=N\) with
\[
N=\begin{pmatrix}
10530&-6915&2055&-285&15\\
-10160&7440&-2420&360&-20\\
5940&-4605&1605&-255&15\\
-1944&1560&-570&96&-6\\
274&-225&85&-15&1
\end{pmatrix}.
\]
The independent source \`x6_r67_d6_inverse_certificate.cpp\` checks \(MN=720I\) with exact integers. For each of the \(61^5\) vectors, it filters \(0<\operatorname{osc}<62\), accepts precisely those for which every coordinate of \(Nz\) is divisible by \(720\), reconstructs \(a=Nz/720\), and records the smallest \(q(a)\) for each oscillation.

Actual exact run: **844,596,301** candidate vectors; **158,503,680** nonzero vectors have oscillation below 62; **338** reconstruct nonzero integral \(a\). The only oscillation levels with minimum required population at most 57 are:
\[
\begin{array}{c|ccc}
\operatorname{osc}&2&48&60\\\hline
\min q(a)&57&41&21.
\end{array}
\]
For \(4\le\operatorname{osc}\le46\), \(\min q(a)\ge114\); for \(50\le\operatorname{osc}\le58\), \(\min q(a)\ge642\). Each even oscillation between 2 and 60 is explicitly represented in the attached JSON and verifier output.

Consequently at \(6\le p\le20\) none of the improving levels is feasible, so osc 62 is optimal. The level osc 60 becomes feasible at \(p=21\); osc 48 at \(p=41\); osc 2 at \(p=57\). For all \(p\ge57\), positive nonzero even oscillation is at least 2 and the osc-2 witness attains it. These statements are exhaustive for **all** integer populations, not merely the forward-search window.

## Independent forward cross-check and exact witnesses

An independent \`x6_r67_d6_forward_crosscheck.cpp\` enumerates every one of the \(115^5=20,113,571,875\) signed vectors \(a\in[-57,57]^5\). Exactly **1,320,729,482** nonzero vectors have \(q(a)\le57\). It computes the minimum oscillation by exact population for \(6\le p\le57\) without using the inverse \(N\). The resulting transitions coincide exactly with the inverse certificate. The remaining \(p\ge57\) follows from the already proved even-oscillation bound.

Explicit integer ambiguity certificates:

| First p | \(a=(a_2,a_3,a_4,a_5,a_6)\) | \((\Delta_1,\ldots,\Delta_6)\) | osc | \(\eta^*\) |
|---:|---|---|---:|---:|
| 6 | \((1,0,0,0,0)\) | \((2,4,8,16,32,64)\) | 62 | 31/2 |
| 21 | \((-1,-14,14,-6,1)\) | \((-12,-20,-24,-20,-72,-20)\) | 60 | 15 |
| 41 | \((-29,-6,13,-6,1)\) | \((-48,-76,-96,-76,-48,-76)\) | 48 | 12 |
| 57 | \((-35,35,-21,7,-1)\) | \((-20,-22,-20,-22,-20,-22)\) | 2 | 1/2 |

For each row, construct \(c,c'\) from positive and negative parts, filling degree-zero ports as above. Both are physically realizable *as conditional named Boolean AB relations*, with strictly positive branch weights. Shift the nuisance bias to center the range of differences and choose opposite errors of maximum magnitude osc/4. A pair remains feasible at all larger \(p\) by adding equal degree-zero rows to both models.

The separate \`x6_r67_d6_named_positive_brc.py\` actually enumerates every named ordered B-Port tuple for both constructed networks, at all six trial depths, with exact rational weights \(u=2/3,v=3/5\). It checks the typed positive branch masses against the polynomial-moment identities. All assertions passed; it is a conditional branch-family checker, **not** a native \`TRIADIC_CLOSURE_E\` simulation.

## Reproduction and evidence scope

From a C++17 / Python 3 shell, run
\`\`\`bash
g++ -O3 -std=c++17 x6_r67_d6_inverse_certificate.cpp -o inverse
./inverse
g++ -O3 -std=c++17 x6_r67_d6_forward_crosscheck.cpp -o forward
./forward
python3 x6_r67_d6_named_positive_brc.py
\`\`\`
The two C++ programs use exact signed 64-bit integers; maximal values in the declared finite domains fit comfortably. Their search completeness follows from the \(z\)-parity/range certificate and \(q(a)\le57\) truncation, respectively. Python uses exact \`Fraction\`; zero floating-point approximations are used for the scientific assertions. No Lean/formal check or independent scientific review was performed.

This result does not confer a native claim on the leased time-dynamics task. The genuinely outstanding bridge is to construct and verify, under frozen P000, an event-to-positive-BRC map preserving ordered whole-triad Cell/Link/Port identities, source labels and reset semantics. Next scientific questions: nonuniform raw channel weights/noise; shorter observer families retaining Cell/Link structure; and native triadic time-event admissibility. Preserve historical R63–R66 activity-association gaps until the actual original session's portable Activity rights can be verified; do not borrow another researcher's identity.

## Provenance

R66 predecessor: \`research_notes/portable_direct/2026-11-21_x6_r66_d5_complete_common_bias_staircase.md\` (commit \`7bebf141bfdbbfb22e29f513a715e24a48bf3033\`). R65 full-D onset: \`research_notes/portable_direct/2026-11-21_x6_r65_universal_half_radius_plateau.md\` (commit \`60e554e6b93c773f1d315fe6de8106ab4ad796fd\`). Conditional input frozen P000 V5; ACTIVE worldview and current portable research rules were read at their own current canonical source. Scientific disposition: **author proof with exhaustive two-way integer evidence**, not independent Result acceptance.

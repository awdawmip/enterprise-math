# R762DE — Exact X6 triangle-holonomy BRC quotient and signed-frame parity obstruction

Date: 2026-11-17. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Author line EM-X6-3050F6; original SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Author proof and exact checks; independent review **NOT_REVIEWED**.

## Immutable inputs and scope

Frozen taskbook: awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Frozen P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. R762DD and R762DC: Draft PR #2641@29f57350d6c661d4783f012381f5a58f8a7d8b45. R762DD supplies the exact open-path ordered pair-area cocycle; R762DC addresses the *different, stronger* observer that can query individual pair coordinates.

The 15 pair indices below are six-dimensional X6 path-history relations, **not additional native dimensions or native two-dimensional planes**. The full native X6, its three-dimensional research slices, PERP_E / 120° and minimum three-force stability retain their frozen meanings. All frame and triangle queries defined here are **candidate diagnostic operations**. No actual TRIADIC_CLOSURE_E or V17/V29/V39 event license is inferred.

## Definitions and allowed future language

For any signed native unit-step history H, each step d_t lies in {±e_0,...,±e_5} and

\[
v_i(H)=\sum_t d_{t,i},\qquad
B_{ij}(H)=\sum_{s<t}d_{s,i}d_{t,j}\quad(i\ne j).
\]

For ordered distinct i,j,k define the oriented **triangle aggregate** \(T_{ijk}(H)=B_{ij}+B_{jk}+B_{ki}\pmod q\), with q≥2. An observer may read an oriented triangle, apply a known allowed axis-label permutation, optionally independent known axis sign flips when that stronger frame language is expressly selected, append known signed path words, and adapt choices to earlier answers. It does not read individual B_{ij}, hidden branches or unnamed sources unless separately declared.

For histories H,H' with the same retained endpoint v, the differences \(c_{ij}=B_{ij}(H)-B_{ij}(H')\) satisfy \(c_{ji}=-c_{ij}\), because \(B_{ij}+B_{ji}=v_iv_j\). All 15 upper entries range over \((\mathbb Z/q)^{15}\) on the explicit common-coarse-history fibre below. Triangle readout differences are \(c_{ij}+c_{jk}+c_{ki}\).

## Theorem A: unrestricted unsigned S6 frames

The complete future observational kernel is exactly

\[
\boxed{c_{ij}=u_j-u_i\pmod q\quad(0\le i,j<6)}
\]

for some \(u\in(\mathbb Z/q)^6\), unique up to a common shift. The exact minimal positive-integer BRC distinguishable-state carrier on the common coarse fibre is

\[
\boxed{K_{S_6}(q)=q^{10}},\qquad
b_{S_6}=\lceil10\log_2 q\rceil.
\]

**Proof.** If every oriented triple sum vanishes, choose \(u_0=0\), \(u_i=c_{0i}\). The triangle (0,i,j) gives \(c_{ij}=c_{0j}-c_{0i}=u_j-u_i\). Conversely any such gradient telescopes around every triangle. There are exactly q^5 gradients, hence q^15/q^5=q^10 distinguishable classes. Arbitrary axis permutations preserve the gradient submodule. For the *same known suffix* K, the R762DD law \(B_{ij}(HK)=B_{ij}(H)+B_{ij}(K)+v_i(H)v_j(K)\) leaves c unchanged at fixed v. Thus arbitrary suffixes, known frames and adaptive observations cannot distinguish gradients; any nongradient is already separated by a triangle after some S6 permutation. The common coarse fibre below proves the count sharp. QED.

## Theorem B: unrestricted signed permutations

Allow all signed frame transformations, including a single-axis sign flip. With \(d=\gcd(q,2)\), the precise kernel consists of gradients with \(2(u_j-u_i)=0\pmod q\) on every edge; the exact state count is

\[
\boxed{K_{\pm S_6}(q)=\frac{q^{15}}{d^5}
=q^{10}(q/d)^5}.
\]

For odd q, **all q^15 area states become distinguishable** by triangle-only signed-frame observations. For even q, a residual order-two gauge of size \(2^5\) survives. At q=2 signed flips add no power; at every q>2 they do.

**Proof.** Identity-frame triangles first force the gradient form from Theorem A. Flip the sign of the middle vertex j in (i,j,k). The triangle changes from zero to \(-2(c_{ij}+c_{jk})=-2(u_k-u_i)\). For every distinct i,k one can choose a third j; hence 2(u_k-u_i)=0 is necessary. Conversely, if 2c_{ij}=0 on every edge, sign flips leave c unchanged because -c=c; permutations preserve gradient form. Such differences remain invisible under all permitted frames and known suffixes. Fixing u_0=0, each of u_1,...,u_5 lies in the d-element annihilator of 2, so the kernel has d^5 members. Divide the q^15 realizable pair assignments by this kernel. QED.

## Theorem C: bounded cyclic six-axis reframing

Suppose the only frame move is \(c=(0\,1\,2\,3\,4\,5)\), applied at most h times, and the only root probe is the triangle (0,1,2). Then

\[
\boxed{K_{\mathrm{cycle}}(h,q)=q^{\min(h+1,6)}}.
\]

**Proof.** Frame t presents (t,t+1,t+2) mod 6. Each of the six distinct rows contains a circular-distance-two chord {t,t+2} not present in any other such row, with unit coefficient ±1, so every prefix of the six rows is independent over every \(\mathbb Z/q\), even for composite q. At t=6 the readings repeat. A common coarse fibre realizes each distinct readout tuple. QED.

## Common coarse fibre and concrete separating witness

For each of the 15 unordered pairs {i,j}, concatenate q four-step slots, independently choosing between
\(D_{ij}=(+e_i,-e_i,+e_j,-e_j)\) and \(L_{ij}=(+e_i,+e_j,-e_i,-e_j)\).
Both have endpoint zero, length four and exactly the same full signed-direction histogram. Each replacement D→L increments only the ordered pair area B_{ij} by one, leaving the other 14 entries unchanged. By selecting 0,...,q−1 such replacements per edge, **all q^15** residues arise on histories of identical endpoint, time 60q and twelve-direction counts. Thus the bounds above cannot be lowered by a different encoding.

For q=3 choose gradient potentials \(u=(0,0,1,0,0,0)\). All unsigned triangle differences vanish, while flipping axis 1 makes the (0,1,2) difference \(-2=1\bmod3\). Explicit 180-step histories implementing this pair and retaining the exact same signed-direction counts are generated and checked by the attached executable.

## Information meaning and guardrails

These K values count minimal *exact positive BRC observational classes* for a specified observer and allowed future language, not signed-amplitude cancellations or native force balance. For q=2: unsigned and signed both 2^10 (10 bits). For q=3: unsigned 3^10 versus signed 3^15 (24 fixed bits). For q=4: unsigned 4^10 (20 bits) versus signed 4^15/32=2^25 (25 bits). Individual-pair probes from R762DC need q^15 in their stronger language.

The gradient quotient **does not** descend automatically under unknown suffixes, source-resolved probes, named Port histories, independent pair queries or actual native event predicates. Each such added operation needs its own proof of fibre constancy. These scope boundaries preserve the joint relation and path provenance rules of the ACTIVE worldview.

## Validation and next problem

Ran Node 22: node R762DE_TRIANGLE_HOLONOMY_VERIFY.js > R762DE_TRIANGLE_HOLONOMY_EVIDENCE.json. Exact BigInt rational rank elimination and integer-modulo checks. All 20 unsigned triple rows have rank 10; cyclic-frame prefixes have ranks 1 through 6; 80 signed test rows have rational rank 15. Exhaustive checks for q=2,...,7 covered all q^5 gradient candidates, with signed-invisible counts \(\gcd(q,2)^5\). A common-coarse 180-step counterexample at q=3 passed. All 1+12+12^2+12^3=1,885 signed primitive histories of length ≤3 passed the ordered area / endpoint and a fixed signed-permutation covariance check. Full evidence is in the JSON; the all-q assertions rely on the written proof rather than finite tests. Independent review remains **NOT_REVIEWED**.

**Next exact dependency:** obtain actual Source-pinned TRIADIC_CLOSURE_E Cell/Link/Port event legality and true V17/V29/V39 transport; determine whether native lawful suffixes expose only aggregated triangle B, individual pair B/A, source/Port identity, independent signs or more. Then compute their actual observer kernel rather than granting candidate diagnostic frames native authority.

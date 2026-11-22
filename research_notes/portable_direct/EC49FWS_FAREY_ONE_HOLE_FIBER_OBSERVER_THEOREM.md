# EC49FWS — Exact Farey determinant-one-to-CRT trace bridge and sharp one-hole observation codes

Date: 2026-11-22 (Asia/Shanghai). Frozen scientific input: **BRC16943**, unchanged. Research family: EC49AS, independent portable science. Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**. These are auxiliary rational-anchor/certificate results, not claims of native X6 dynamics.

Scientific source pins:
- EC49FWQ, 50 ten-bit masks, 38 reflection spectrum fibers, seven doubleton difference supports and unknown-factor inverse: \`awdawmip/enterprise-math@d091c8f2757f67c18be8056ae976b1e092a21098:research_notes/portable_direct/EC49FWQ_BLIND_FACTOR_FULL_SUPPORT_PROBES_THEOREM.md\`.
- EC49FVT, frozen determinant-one left anchor: \`awdawmip/enterprise-math@a31340d5ff2dc5b8202388d7393a8b6817458c8e:research_notes/portable_direct/EC49FVT_FAREY_DETERMINANT_ONE_LOCAL_GAP_THEOREM.md\`.
- EC49FVU, general rational-anchor nearest-neighbor theorem: \`awdawmip/enterprise-math@ac3bdb073b8ccd821cd23e830bcb9ccaf8d09529:research_notes/portable_direct/EC49FVU_RATIONAL_ANCHOR_DETERMINANT_ONE_THEOREM.md\`.
- EC49FWR, arbitrary unknown CRT-factor adversarial errors: \`awdawmip/enterprise-math@7d05c2c59dfeaf68a3128a32e1fd2967dfb65702:research_notes/portable_direct/EC49FWR_UNKNOWN_FACTOR_ERASURE_AND_ERROR_THEOREM.md\`.

## 1. An exact same-trace link from the Farey determinant-one branch to frozen CRT words

The original integer certificate is

\[
C_{11}(h,n)\iff P_{10}(h\bmod10,n\bmod10)\ \land\ (9h+10n\not\equiv0\pmod{11}).
\]

Here \(P_{10}\) is the frozen 44-residue projective predicate. Fix a reduced rational anchor \(a/b\in(0,1)\). The left-hand determinant-one branch \(b h-a d=-1\), with \(d=h+n\), has integer solutions

\[
(h_t,n_t)=(h_0,n_0)+t(a,b-a),\qquad d_t=h_0+n_0+bt.
\]

Because \(\gcd(a,b)=1\), the direction \((a,b-a)\) is primitive modulo 10. All residue solutions of \((b-a)h-an=-1\bmod10\) form exactly one 10-element affine orbit. Choose the representative \((x,y)\) used by FWQ's frozen-mask convention and the unique rephasing offset \(t_0\bmod10\) satisfying \((h_{t_0},n_{t_0})\equiv(x,y)\bmod10\). Put \((H_1,N_1)=(h_{t_0},n_{t_0})\). The normalized ten-bit mask is

\[
U(t)=\mathbf1_{P_{10}}(H_1+at,N_1+(b-a)t),\qquad t\in\mathbb Z/10,
\]

and is **one of the original 50 frozen FWQ supports**.

Let \(L_0=9H_1+10N_1\) and \(L_1=9a+10(b-a)\). The two column vectors \((H_1,N_1)\), \((a,b-a)\) have determinant \(-1\), so the nonzero linear functional \(L\) cannot vanish on both modulo 11. If \(L_1=0\bmod11\), then \(L_0\ne0\bmod11\) and \(V=\mathbb Z/11\) is full. Otherwise there is exactly one excluded residue \(z=-L_0L_1^{-1}\bmod11\), and \(V=\mathbb Z/11\setminus\{z\}\). Thus the **actual** left-branch trace has exactly the CRT form

\[
\boxed{\mathbf1_{C_{11}}(H_1+at,N_1+(b-a)t)
       =U(t\bmod10)\mathbf1_V(t\bmod11)\quad\text{for every integer }t.}
\]

It is not an arbitrary nonempty unknown \(V\): **every genuine determinant-one anchor line has \(V\) full or missing exactly one residue.**

FWV's fixed-anchor conclusion (EC49FVU) gives the nearest certified member strictly left of \(a/b\) for all \(H>16b\): take the **largest \(t\)** whose denominator \(d_t=H_1+N_1+bt\) is at most \(H\), for which both \(h_t,n_t>0\) and the above trace equals one. The fraction is \(h_t/d_t\). Hence the complete height-to-height **left-neighbor sequence** is exactly determined by the recovered CRT trace **together with the anchor, side, affine origin and rephasing**. Forgetting those provenance coordinates has not been certified as observer-safe. The right-hand side and full X6 transition are not claimed here.

## 2. Optimal fixed-site observer for the physically relevant full/single-hole mod-11 family

Consider the enlarged, explicitly declared **600-state** product family

\[
\mathcal W_{11}=\{U\times V:U\in\mathcal F_{50},\
V\in\{\mathbb Z/11\}\cup\{\mathbb Z/11\setminus\{z\}:z\in\mathbb Z/11\}\}.
\]

The observer knows **all indexed reflection defects** \(D_W(a,b)=|W\triangle((a,b)-W)|\), and counts only separate Boolean membership readings at distinct physical sites \((j,v)\). The fixed site set is selected before the indexed spectrum is observed. Require Hamming separation at least \(r\) for all distinct \(U\) within the same complete-indexed-spectrum fiber.

**Theorem.** For every \(1\le r\le10\), the sharp minimum and number of optimal fixed layouts are

\[
\boxed{N_{\mathrm{fixed}}(r)=3(r+1)},\qquad
\boxed{\#\mathrm{Opt}(r)=\binom{11}{r+1}^{3}16^{r+1}}.
\]

A universal optimal arrangement chooses rows \(j=1,2,3\) in **any \(r+1\) distinct mod-11 columns**.

| Physical observation guarantee | Hamming distance | Fixed-site minimum | Number of optimum layouts | Spectrum-adaptive minimum |
|---|---:|---:|---:|---:|
| Exact, no corrupted read | 1 | **6** | 42,592,000 | 1 |
| One known-position erasure | 2 | **9** | 18,399,744,000 | 2 |
| One unknown incorrect bit | 3 | **12** | 2,355,167,232,000 | 3 |

Known-location \(e\) erasures require \(r=e+1\) and arbitrary unknown \(t\) errors require \(r=2t+1\), under the conventional worst-case Hamming model. This refined result is **different** from EC49FWR's impossibility with arbitrary nonempty \(V\), because a singleton mod-11 factor is not a genuine Farey determinant-one trace.

### Proof

By the exact finite P10 census in FWQ, a nontrivial indexed defect fiber has at most two states, which share the same \(V\), and the difference of their first factors lies among seven supports. Each such difference contains at least one of these three disjoint sets:

\[
A=\{1,4,6,9\},\quad B=\{2,7\},\quad C=\{3,8\}.
\]

All three minimal supports themselves arise from actual **equal-cardinality** frozen P10 doubletons. Thus each yields equal complete product spectra **for any common \(V\)**, in particular for every full or one-hole \(V\).

For each \(G\in\{A,B,C\}\), let \(w_G(v)\) be the number of chosen probe sites in \(G\times\{v\}\), and \(w_G=\sum_vw_G(v)\). A nontrivial fiber with difference exactly \(G\) under the unknown factor that removes the **most probed** column has Hamming distance \(w_G-\max_v w_G(v)\). Therefore the necessary condition for distance at least \(r\) is

\[
w_G-\max_vw_G(v)\ge r\quad(G=A,B,C).
\]

This is also sufficient: every other nontrivial difference support contains at least one such \(G\), and **every permitted \(V\) deletes at most one column**. Since A,B,C are disjoint, the necessary conditions force at least \(r+1\) sites from each, giving \(N\ge3(r+1)\). Equality forces the \(r+1\) probes of every \(G\) to occupy **distinct** columns, since two in one column would be erased together and leave fewer than \(r\). For \(r\le10\), place one from \(G\) in each of any \(r+1\) columns. That attains the bound.

For each group there are \(\binom{11}{r+1}\) column subsets; first-coordinate choices are independently \(4,2,2\) per chosen column for A,B,C. Hence total \(\binom{11}{r+1}^{3}(4\cdot2\cdot2)^{r+1}\) optimum layouts.

A spectrum-adaptive observer can distinguish each pair by measuring \(r\) distinct coordinates in the two candidate states' difference. Here every such difference has at least \(2\cdot10=20\) sites, so the displayed \(r=1,2,3\) costs are all attainable and sharp by the Hamming bound.

**Population distinction.** This theorem is sharp over the enlarged 600-state \(\mathcal W_{11}\). The actual normalized Farey anchor traces belong to it, so these layouts are **valid upper bounds for them**, but the lower bounds need **not** be sharp over the smaller, correlated population of actual anchors. A separate realized-anchor witness argument is required for that more restrictive quantifier.

## 3. Reproducible exact finite checks

The standalone companion CPython3 program reconstructs the frozen 44-residue predicate, all 72 primitive directions and 50 distinct words, then exhausts 12 allowed mod-11 factors, **600 product states**, **478 distinct indexed spectra**, with exactly **122 two-state fibers** and no larger fiber. Every two-state fiber shares its factor \(V\). Canonical fixed layouts using rows \(\{1,2,3\}\) in respectively one, two, three and four columns have minimum Hamming distance **0, 1, 2, 3**. The program checks the three exact equal-mass difference-group witnesses at every excluded column.

It also constructs and rephases exact determinant-minus-one lines for the seven anchors below, verifying all **110 residues each** against the direct frozen predicate:

| Anchor | Rephase \(t_0\) | P10 mask \(U\) | Excluded mod-11 residue |
|---|---:|---:|---:|
| 1/2 | 2 | 447 | 7 |
| 1/3 | 2 | 327 | 8 |
| 2/3 | 2 | 394 | 6 |
| 3/7 | 8 | 23 | 1 |
| 5/11 | 8 | 211 | 9 |
| 8/13 | 8 | 371 | 2 |
| 11/37 | 4 | 287 | 3 |

All asserted checks report \`ALL PASS\`. Analytical validity beyond these seven anchors follows from unimodular linear algebra and CRT; the all-family observer theorem additionally depends on the cited parent FWQ exact spectrum-fiber theorem. Parent BRC-to-projective reduction and independent review are preserved as explicit dependencies. Neither CI nor Lean was run or required for this result.

## 4. Observer-safe continuation

The indexed spectrum and robust finite membership reads can reconstruct the static \(U,V\) in the declared population; the **anchor, signed determinant branch, rephase and affine denominator origin** are further needed to evaluate the future certified neighbor \(q_-(H)\) from that trace. This provides an actual same-trace, exact rational-anchor-height bridge, rather than merely comparing unrelated static masks and Farey fractions.

Next: test whether the three optimal-group lower-bound witnesses can be **simultaneously realized** in the correlated population of genuine reduced Farey anchors, and construct the similarly provenance-preserving **right-hand** branch and paired two-sided signed-gap readout. Any interpretation as full native X6 dynamics still requires its own typed embedding and observer-safety proof.

The frozen BRC16943 input, P000 and ACTIVE worldview are unchanged. This scientific artifact asserts no canonical TASK, CLAIM, native Researcher/Activity identity, Result or independent Review.
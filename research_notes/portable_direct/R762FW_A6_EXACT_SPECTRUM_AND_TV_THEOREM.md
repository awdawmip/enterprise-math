# R762FW — Exact all-depth total-variation formula and spectral gap for the 40-branch X6 triad BRC walk

Date: 2026-11-19 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_VALIDATION_PASS / NOT_REVIEWED.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json; taskbook @857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md.
Prior model and coefficients: R762FT–FV, especially PR #2796 at 9ab2d36ff0eaaec9454d10e7cb15f7657608eb46.

## Scoped object and theorem

The model is the *candidate axis-permutation observer* of a fully provenance-retaining positive-rational BRC: at each formal step independently choose one of the 40 directed three-cycles of six named native axes, all with weight 1/40. Retain the actual ordered branch word, triple, orientation, source and signs; map this word to its permutation product in A6 only when evaluating the explicitly stated endpoint observer. The kernel is the central probability measure μ=(1/40)Σ_{g∈C3}δ_g on A6, |A6|=360. Let U be uniform on A6 and d_h=||μ^{*h}−U||_TV, with exact arithmetic and h a nonnegative integer.

**Theorem (exact total variation, all depths).** For every integer h≥2,

\[
\boxed{d_h=
\frac{65}{36}\left(\frac25\right)^h
+\frac5{36}\left(-\frac15\right)^h
+\frac8{45}\left(-\frac18\right)^h
-\frac{10}{9}\left(\frac1{10}\right)^h
+\frac85\left(\frac18\right)^h.}
\]

Furthermore d_0=359/360 and d_1=8/9. The nontrivial spectrum of convolution by μ on functions on A6, with multiplicities, is

\[
 2/5\ (25),\quad -1/5\ (25),\quad -1/8\ (128),\quad
 0\ (81),\quad 1/10\ (100).
\]

Thus the exact nontrivial spectral radius is 2/5, and the pointwise all-depth L2-to-TV certificate for h≥1 is

\[
 d_h\le \frac12\sqrt{25(2/5)^{2h}+25(1/5)^{2h}
              +128(1/8)^{2h}+100(1/10)^{2h}}.
\]

In particular,

\[
 \boxed{\lim_{h\to\infty}\frac{d_h}{(2/5)^h}=\frac{65}{36}.}
\]

This gives the sharp asymptotic exponential rate and leading constant, sharpening the earlier three-step minorization estimate of R762FV.

## Proof and complete exact character data

The forty three-cycles form one conjugacy class in A6, hence their class average acts by the scalar χ(g_3)/dim on each irreducible A6 representation (Schur's lemma). A6 irreducible dimensions are 1, 5, 5, 8, 8, 9, 10. Restricting the S6 partitions (6), (5,1), (3,3), (4,2), (4,1,1) gives the five nonsplit representations; the self-conjugate (3,2,1) of dimension 16 splits into two 8-dimensional representations. The three-cycle class is nonsplit, so both 8-dimensional factors have χ(g_3)=−1, hence eigenvalue −1/8. The S6 character values below are obtained by the Murnaghan–Nakayama rim-hook rule. The 9-dimensional factor has zero three-cycle character and contributes nothing for h≥1.

| S6 partition | dimension | 1^6 | 3·1³ | 2²·1² | 3² | 5·1 | 4·2 | eigenvalue |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| (6) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| (5,1) | 5 | 5 | 2 | 1 | −1 | 0 | −1 | 2/5 |
| (3,3) | 5 | 5 | −1 | 1 | 2 | 0 | −1 | −1/5 |
| (3,2,1) | 16=8+8 | 16 | −2 | 0 | −2 | 1 | 0 | −1/8 each |
| (4,1,1) | 10 | 10 | 1 | −2 | 1 | 0 | 0 | 1/10 |
| (4,2) | 9 | 9 | 0 | 1 | 0 | −1 | 1 | 0 |

The six even S6 cycle types have respective A6 populations 1,40,45,40,144,90. One type (5,1) splits into two A6 classes of size 72, but μ^h and the displayed character combinations take the same value on both; using their aggregate population 144 is exact.

For h≥1, write a=(2/5)^h, b=(−1/5)^h, c=(−1/8)^h, e=(1/10)^h. Character inversion, including the two 8-dimensional factors, gives for each g∈A6,

\[
 360\,\mu^{*h}(g)-1
  =5a\,χ_{(5,1)}(g)+5b\,χ_{(3,3)}(g)
   +8c\,χ_{(3,2,1)}(g)+10e\,χ_{(4,1,1)}(g).
\]

The six values of the right side, in cycle-type order, are:

\[
\begin{array}{c|l}
1^6&25a+25b+128c+100e\\
3\,1^3&10a-5b-16c+10e\\
2^2\,1^2&5a+5b-20e\\
3^2&-5a+10b-16c+10e\\
5\,1&8c\\
4\,2&-5a-5b.
\end{array}
\]

For every h≥2, their signs are +,+,+,−,sign(c),−. This is an all-h inequality, not an empirical sign guess. With A=(2/5)^h>0, one has |b|/A=2^{-h}, |c|/A=(5/16)^h and e/A=4^{-h}. In the three potentially delicate positive cases: for even h, all terms for 1^6 are positive, and for odd h≥3 its positive lower bound after dividing by A is 25−25·2^{-h}−128(5/16)^h>0; for 3·1³ the lower bound is 10−5·2^{-h}−16(5/16)^h>0 for even h≥2, while odd h has only positive contributions; for 2²·1², use 5−5·2^{-h}−20·4^{-h}>0 for odd h≥3 and 5−20·4^{-h}>0 for even h≥2. For 3², the upper bound for even h≥2 is −5+10·2^{-h}+10·4^{-h}<0, and for odd h≥3 it is −5+16(5/16)^h+10·4^{-h}<0. Finally −5a−5b<0 since |b|<a, and the 5·1 sign is sign(c). All these bounds strengthen monotonically with h within the indicated ranges.

Since TV equals (1/720) times the population-weighted sum of the absolute displayed deviations, inserting the fixed signs gives
\[
 d_h=\frac{65}{36}(2/5)^h+\frac5{36}(-1/5)^h
 +\frac8{45}(-1/8)^h-\frac{10}{9}(1/10)^h+\frac85(1/8)^h.
\]
The h=0,1 values follow directly from delta mass and uniform support on the 40 generators. Fourier Plancherel and Cauchy–Schwarz yield the claimed L2 upper bound, with multiplicities d_ρ². Every remaining nontrivial eigenvalue has absolute value <2/5, so division by (2/5)^h and taking the limit yields 65/36. QED.

## Exact checks and scope of validation

Attached R762FW_VERIFY.py generates all 360 even permutations and all 40 directed 3-cycles independently, computes exact 40-branch convolutions at h=1,…,8, computes all characters via a separate rim-hook recursion (not by copying the table), compares all 360 endpoint counts at each depth against character inversion, and checks exact total variation against the boxed formula at h=2,…,8. It also validates the character self-inner-products, numerical sign classes at h=2,…,80, and all integer counts. Python's Fraction supplies exact rational arithmetic; no floating point. Sample exact d_2=14/45, d_3=209/1800, d_4=13469/288000, d_5=53213/2880000, d_6=3414581/460800000. General h is proved above; finite checks corroborate it, rather than standing in for a universal proof. Author-side PASS; independent review NOT_REVIEWED.

## BRC/source and native interface boundary

The theorem describes only the explicitly declared endpoint observer of the 40-branch candidate, not a quotient that may replace the full BRC source state for arbitrary future queries. Ordered histories remain 40^h distinct formal words before projection, with nontrivial fibers after depth 3. All P000 signed-X6, three-dimensional slice, PERP_E=120°, joint-relation observer and time-as-ordered-trace premises remain untouched. The actual native Cell/Link/Port legality of the candidate rotations and source transport is still unresolved. In particular this mixing theorem neither proves physical triadic closure nor establishes that a native operation may discard ordered provenance.

## Next discriminating work

Extract the frozen native Cell/Link/Port transition predicate and check whether its valid generator support is all forty three-cycles, a proper symmetric subset or an incidence-dependent set. If it is a proper subgroup or a partial gate, derive its transition operator and preserve BLOCK/branch evidence as in R762FP–FS. Determine which exact finite observer/horizon semantics admit the present A6 quotient. Separately continue the q9 BRC full-vector period obstruction and full native signed closure objective.

Contributor provenance: current research continuation of historic EM-X6-3050F6; no current CLAIM, Researcher Activity, Source PROGRESS, independent review, or mathematical admission is asserted by this GitHub document.
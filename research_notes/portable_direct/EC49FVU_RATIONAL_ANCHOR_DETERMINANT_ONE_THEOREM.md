# EC49FVU — Universal determinant-one certified neighbors at every rational anchor

**Research track:** EC49AS / BRC16943, directed portable continuation of EC49FVT.
**Scientific parent:** awdawmip/enterprise-math@a31340d5ff2dc5b8202388d7393a8b6817458c8e:research_notes/portable_direct/EC49FVT_FAREY_DETERMINANT_ONE_LOCAL_GAP_THEOREM.md.
**Frozen numerical inputs:** U = 4822040484/8132285009, Gamma = 141024/1653649; projective modulus 11 and reduction exactly as in EC49FVT.
**Scientific status:** AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED. This is a theorem about the frozen Bernoulli-derived certificate model, not a native X6 geometric transfer or a new P000 claim. The Bernoulli-to-projective reduction is inherited as a proof dependency.

## 1. Exact theorem

For positive integers h,n, let C11(h,n) denote the complete projective mod-11 nonroot certificate inherited from EC49FVT. The exact equivalent finite criterion is

\[
C_{11}(h,n)\iff ((h\bmod 10,n\bmod 10)\in P_{10})\ \land\ (9h+10n\not\equiv0\pmod {11}),
\]

where the 44-element set P10 is reconstructed from the frozen projective equations by the companion verifier. Define

\[
S_H=\{h/d:0<h<d\le H,\ \gcd(h,d)=1,\ C_{11}(h,d-h)\}.
\]

**Theorem.** Fix any reduced rational anchor a/b in (0,1), with b at least 2. For every integer H > 16b, define q_-(H) and q_+(H) to be the largest admissible denominators d <= H for certified fractions satisfying respectively b h - a d = -1 and b h - a d = +1, with 0<h<d. Both exist and

\[
H-8b\le q_-(H),q_+(H)\le H.
\]

The **actual nearest members of the complete certified set S_H**, strictly below and strictly above a/b, are exactly

\[
x_-=\frac{a q_- -1}{b q_-},\qquad x_+=\frac{a q_+ +1}{b q_+}.
\]

Their distances from the anchor satisfy

\[
\frac1{bH}\ \le\ \frac ab-x_-,\,x_+-\frac ab\
\le\frac1{b(H-8b)}.
\]

Thus for each fixed a/b,

\[
\lim_{H\to\infty}bH\left(\frac ab-x_-\right)=
\lim_{H\to\infty}bH\left(x_+-\frac ab\right)=1.
\]

The bounds also yield convergence uniformly along any sequence of reduced anchors a_H/b_H with b_H=o(H). If C11(a,b-a) is false, the two nearest points are consecutive certified neighbors across the missing anchor, with exact gap

\[
G_{a/b}(H)=\frac1b\left(\frac1{q_-}+\frac1{q_+}\right),
\qquad \lim_{H\to\infty}H G_{a/b}(H)=\frac2b.
\]

If the anchor itself is certified, its two adjacent individual certified gaps have respective limits 1/b after multiplication by H. The endpoint one-sided gaps at 0/1 and 1/1 obey the same bounds with b=1 for H>16; both have limit 1 after multiplication by H. The missing center 1/2 has two-sided gap constant 1, consistent with the stronger specialized EC49FVT theorem.

There is also an **exact quasi-periodic denominator formula**: for each fixed anchor and sign, once H>16b,

\[
q_\pm(H+110b)=q_\pm(H)+110b.
\]

Hence H-q_\pm(H) depends only on H modulo 110b, lies between 0 and 8b, and is determined by one finite residue table.

## 2. The sharp 8-step affine residue lemma

**Lemma.** Let x,y,u,v be integers satisfying u y-v x=+1 or -1, and consider the bi-infinite affine line (h,n)=(x,y)+t(u,v). Extend C11 by its residue formula on all integer pairs. The cyclic gap between any two successive certified t-positions modulo 110 is at most 8. The constant 8 is attained by an actual determinant-one rational-anchor family.

**Exhaustive finite proof.** The frozen finite-field projective rule produces exactly 44 valid mod-10 exponent pairs in P10. The complete exhaustive scan of the four residues (u,v,x,y) mod 10 with determinant congruent to +1 or -1 contains exactly 1,440 quadruples. For each quadruple define

\[
T=\{t\bmod10:(x+ut,y+vt)\bmod10\in P_{10}\}.
\]

The complete distribution of hit counts is:

| Number of hits in ten steps | Number of unimodular quadruples |
|---:|---:|
| 4 | 240 |
| 5 | 480 |
| 6 | 480 |
| 7 | 160 |
| 8 | 80 |

There are exactly 300 distinct ten-position masks, and the maximum cyclic step for any such mask without the mod-11 restriction is 6.

For the mod-11 condition, write L(h,n)=9h+10n. The two numbers L(x,y),L(u,v) cannot both vanish modulo 11: the kernel of the nonzero linear map L over F11 is one-dimensional, whereas the determinant of these two vectors is ±1. Thus the mod-11 condition deletes either **no** t residue or precisely **one** residue t=r modulo 11.

For each of the 300 ten-step masks and each of the eleven possible excluded classes r, the Chinese remainder theorem reduces the full period to the exact set

\[
\{t\bmod110:(t\bmod10)\in T,\ t\bmod11\ne r\}.
\]

The complete maximum-cyclic-step distribution among the 3,300 finite cases is:

| Maximum cyclic step | Number of mask/exclusion pairs |
|---:|---:|
| 3 | 110 |
| 4 | 550 |
| 5 | 1,100 |
| 6 | 1,100 |
| 7 | 220 |
| 8 | 220 |

In particular every case is bounded by 8. For the actual reduced anchor 3/7 on the left, the determinant-one sequence begins at (d0,h0)=(5,2) and advances by (d,h)=(7,3); its full 110-step certificate sequence has maximal cyclic difference 8. Hence 8 is sharp for this affine modular statement. Every mask, count, maximal gap and witness is regenerated using integers in the companion Python program.

## 3. Proof of the nearest-neighbor theorem

For either sign s=±1, solve b h-a d=s. Since gcd(a,b)=1, all integer solutions can be written

\[
d=d_0+bt,\quad h=h_0+at,\quad n=d-h=(d_0-h_0)+(b-a)t.
\]

The affine line has determinant

\[
a(d_0-h_0)-(b-a)h_0=a d_0-bh_0=-s=\pm1.
\]

By the lemma, its certified positions in t have maximal gap 8. Therefore for every H there is a certified determinant-one denominator q_s in [H-8b,H]. For H>16b, q_s>H/2 and is large enough to make h and n positive, since 0<a<b; the determinant-one identity also implies gcd(h,d)=1. Hence these positions are genuine reduced members of S_H at distance exactly 1/(b q_s) from the correct side of a/b.

Every distinct reduced fraction h/d with d<=H has nonzero integer determinant |b h-a d|>=1. Those with determinant magnitude at least 2 lie at distance at least 2/(bH). The constructed determinant-one certificate is closer because

\[
\frac1{b(H-8b)}<\frac2{bH}\quad(H>16b).
\]

Thus the nearest certified fraction on each side must have determinant one, and among the determinant-one fractions the largest certified denominator is nearest. This establishes the **exact** formulas and the finite-H inequalities. The limit follows by squeezing; because the relative error is at most (1-8b/H)^{-1}-1, convergence is uniform for b=o(H).

For an uncertified anchor there are no other certified points between these two exact neighbors, giving the two-sided gap formula and limit 2/b. If the anchor itself belongs to S_H, each side forms a separate consecutive gap to it. For the two endpoints 0 and 1, use only the inward determinant-one sequence (1/d or (d-1)/d); the same argument proves the one-sided result.

Periodicity of the exact residue predicate C11 along t modulo 110 proves q_s(H+110b)=q_s(H)+110b once large enough for positivity.

## 4. Reproducibility, precise scope and next problem

The companion standard-library CPython 3 verifier recomputes the complete parent finite-field predicate and checks:
- 12,100 direct projective comparisons for 1<=h,n<=110, covering every exponent residue pair modulo 110.
- 1,440 unimodular mod-10 configurations and all 300 distinct masks.
- 3,300 exact mask/excluded-mod-11 combinations, with a sharp bound of 8.
- 90 independent direct searches over **all** certified reduced fractions for the 45 rational anchors with 2<=b<=12, at H=17b+1 and H=20b+7.
- Five exact illustrative rational anchors at H=1000, plus the realized 3/7 sharp eight-step witness.

Execution uses only exact integers and fractions.Fraction. The paired output terminates in ALL PASS. These finite checks prove the finite residue lemma because its search domain has been completely justified; the infinite theorem then follows from the analytic determinant argument.

**Scientific interpretation.** The mod-11 certificate is inherited as a sufficient exclusion condition within the frozen Bernoulli-derived rational-width model. We have proved exact neighbor geometry for every rational anchor, not the still-open global claim

\[
\lim_{H\to\infty}H\,G_{\max}(S_H\cup\{0,1\})=1.
\]

The new conclusion isolates fixed rational anchors and any moving sequence with b=o(H) evaluated **at the anchor itself**. It does not yet control gaps whose centers merely approach anchors at a different rate. That is a concrete next target: classify rational-approximation corridors with moving centers using Farey determinants, and combine the local affine certificate with a global covering argument. Independent mathematical review should verify the BRC16943-to-projective parent reduction and this finite CRT certificate before any formal promotion.

**Provenance and operational status.** EC49FVT frozen predecessor retained; P000 and ACTIVE worldview unchanged. Science publication, Activity linkage, canonical CLAIM, Result and independent Review are distinct operations. This author-side artifact asserts no shared ownership or review authority.

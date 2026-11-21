# R5 — all-threshold primitive-16 leading term and exact minimal cost period at remainder O_m(N^4)

2026-11-21. Researcher-side exact derivation; independent scientific Review **NOT_REVIEWED**. Frozen R5 nonadaptive scalar model: 256 named hypotheses, prices 214..314, unchanged separation certificate. This is a **cost observer** theorem, not a transfer to native X6/heartbeat dynamics. Original mathematical predecessor: enterprise-math@bf88b495f9e727ab355f7ff330a01c31c03e66fa:research_notes/portable_direct/r5_primitive13_n6_universal_20261121/ADDENDUM_PRIMITIVE16_17.md and VERIFY_16_17.py. This continuation does not rebase frozen scientific inputs onto the present control Source.

## The theorem

Let (M_m[O_m(N^4)]) denote the **least coefficient period** of the quasipolynomial approximation to the frozen count with an (O_m(N^4)) remainder, for each fixed positive integer threshold m. Put
[
a(m)={\bf1}_{m\bmod16\in\{1,2,3,4,5,6,7,8,9,10,11\}},\qquad
b(m)={\bf1}_{m\bmod17\in\{1,2,3,4,5,6,7,8,9,10,11,12\}}.
]
Then, using the already archived (M_m[O_m(N^5)]=360360) theorem and primitive-17 classification,
[
\boxed{M_m[O_m(N^4)]=360360\,2^{a(m)}17^{b(m)}\quad(m\ge1).}
]
This is **sharp**, not just an upper bound. The 272 threshold residue classes modulo lcm(16,17)=272 split:
- both nonzero: 132 classes, period 12,252,240;
- only primitive 16: 55 classes, period 720,720;
- only primitive 17: 60 classes, period 6,126,120;
- neither: 25 classes, period 360,360.

The first new ingredient is the *all-m exact classification* of primitive 16: its degree-five contribution is nonzero exactly for
[
\boxed{m\bmod16\in\{1,2,3,4,5,6,7,8,9,10,11\};}
]
it vanishes at that degree exactly for residues 12,13,14,15,0. Its threshold dependence has exact period 16 (a finite Fourier sequence), no polynomial-in-m growth.

## Primitive-16 derivation

Write z for an arbitrary primitive 16th root, so (Phi_{16}(z)=z^8+1=0). Among 214,...,314, precisely 224,240,256,272,288,304 are 16-multiples. The frozen five minimal failure sets are
[
S_0=\{214,215,216,217,218\},\quad S_1=\{214,216,217,218,219,220,221\},\quad S_2=\{215,216,217,218,219,220,221\},
]
and S_3=223..290, S_4=296..312. Exactly the seven nonempty masks of S_0,S_1,S_2 avoid all six 16-multiples. Since every pairwise union of S_0,S_1,S_2 equals (U=\{214,\dots,221\}), their inclusion-exclusion sum reduces to the four signed sets ((S_0,+1),(S_1,+1),(S_2,+1),(U,-2)).

Let (H_{16}(z)=\prod_{214\le p\le314,,16\nmid p}(1-z^p)^{-1}), (P_{16}=224\cdot240\cdot256\cdot272\cdot288\cdot304), and
[
B_{m,S}(z)=\sum_{a_p\ge0,\sum_{p\in S}a_p<m}z^{\sum_{p\in S}pa_p},\quad W_S(z)=\prod_{p\in S}(1-z^p).
]
The order-six pole's normalized local coefficient is
[
A_m(z)=\sum_{(S,\epsilon)}\epsilon W_S(z)B_{m,S}(z).
]
Each such S avoids multiples of 16, and its residues mod 16 are distinct. Hence the exact threshold generating identity is
[
\sum_{m\ge1} A_m(z)t^{m-1}
=\frac{1}{1-t}\sum_{(S,\epsilon)}
\epsilon\prod_{p\in S}\frac{1-z^p}{1-z^pt}
=\frac{G(t,z)}{1-t^{16}},
]
where the **explicit degree-10 polynomial** is
[
\boxed{G(t,z)=\sum_{(S,\epsilon)}\epsilon
\prod_{p\in S}(1-z^p)
\prod_{r\in\{1,\ldots,15\}\setminus(S\bmod16)}(1-z^rt).}
]
The second equality uses (\prod_{r=0}^{15}(1-z^rt)=1-t^{16}); its (r=0) factor cancels 1/(1-t). No limiting approximation occurs. Therefore (A_m(z)=[t^{(m-1)\bmod16}]G(t,z)); coefficients beyond degree 10 vanish.

In the integral basis (1,z,\dots,z^7) of (\mathbb Q[z]/(z^8+1)), the eleven exact coefficients for residues m=1..11 are:
```text
m= 1  [16,10,-4,-10,-16,-18,-20,-22]
m= 2  [-100,-76,-40,0,40,80,104,116]
m= 3  [280,266,216,130,24,-90,-184,-250]
m= 4  [-376,-444,-444,-372,-248,-84,92,252]
m= 5  [232,380,476,496,440,320,148,-44]
m= 6  [8,-136,-256,-344,-376,-352,-272,-152]
m= 7  [-88,-24,44,108,152,172,164,136]
m= 8  [24,12,4,-4,-8,-12,-20,-20]
m= 9  [32,26,16,2,-8,-22,-24,-30]
m=10  [-20,-20,-16,-8,0,8,16,20]
m=11  [8,6,4,2,0,-2,-4,-6]
```
Every listed vector is nonzero. Since (Phi_{16}) is irreducible, nonzero in this field is nonzero under each of the eight primitive-root embeddings; the zero residues vanish in all. Thus
[
F_m^{(16)}(N)=\frac{N^5}{5!P_{16}}\sum_{\mathrm{ord}(z)=16} H_{16}(z)A_m(z)z^{-N}+O_m(N^4).
]
The primitive-16 Fourier component cannot be recreated by a coefficient period not divisible by 16, by uniqueness of the finite root-of-unity Fourier decomposition. At m=1, the coefficient reduces after refactoring the 214..221 denominators to the predecessor's (z^7-z^4+\tfrac12z^3+\tfrac12z-1), providing an independent normalization consistency check.

## Minimal period synthesis

The already archived all-m primitive-11/13 and lower-order proofs force 360360 at remainder O_m(N^5), hence also at O_m(N^4). At degree five, d=16 and d=17 are the only additional root orders that can add factors to that base: orders <=15 and order 18 already divide 360360; for all d>=19 at most five prices in 214..314 are divisible by d, so every such root pole has order at most five and contributes only O_m(N^4). The primitive-17 order-six coefficient is nonzero precisely for m mod 17 in 1..12 by the predecessor's all-m rational identity. The newly classified primitive-16 harmonic contributes the extra factor 2 precisely when a(m)=1. Cyclotomic Fourier uniqueness gives the matching lower bound, completing the four-case sharp classification.

## Validation, provenance, and limits

`VERIFY_PRIMITIVE16_ALL_M.py` computes G directly in the rational field `Q[z]/(z^8+1)`, checks all 11 coefficient vectors and the five zero classes, independently recomputes the original partial-multiplicity generating polynomial by dynamic programming for m=1..48, and recovers exactly the earlier m=1 formula. `RESULT.json` stores exact vectors and residue counts. All arithmetic is rational/integer; the generator identity proves infinitely many thresholds, while the DP verifies a finite independent implementation. Result grade: **AUTHOR_EXACT_DERIVATION / EXACT_FINITE_CHECKED / NOT_REVIEWED**. No claim of native BRC/X6 physics, formal Task CLAIM/RUN, independent acceptance, or merger to canonical main.

Next: classify primitive-16 and primitive-17 *next Laurent order* for their respective zero residues at O_m(N^3), and explore minimal sufficient joint threshold/cost observer encodings retaining both modular flags and the cost Fourier phases. Treat any later transfer to native residual states as a separate typed embedding/observer proof obligation.

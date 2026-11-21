# R5 — Primitive 13th-root residual: exact cancellation by threshold residue

2026-11-21 | Frozen scalar nonadaptive R5 | AUTHOR_EXACT_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED | Independent portable research (no formal CLAIM/RUN/Result/Review).

## Input and pin

Predecessor: [R5 11th-root split](https://github.com/awdawmip/enterprise-math/blob/69664f27d752dcc6e9cabae6355821bfedf0178f/research_notes/portable_direct/r5_eleventh_residue_split_20261121/RESEARCH.md). Frozen R5 model: 256 hypotheses, query prices 214..314, 32,640-pair certificate SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Minimal separating sets:
S0={214,..,218}, S1={214,216,..,221}, S2={215,..,221}, S3={223,..,290}, S4={296,..,312}.
For fixed m≥1, F_m(N) counts nonnegative price-multiplicity vectors of total cost N for which some S_i has load strictly less than m.

## New theorem

Let z be any primitive 13th root, and define

\[
P_{13}=\prod_{j=0}^7(221+13j)=24189834376697109120,\qquad
H_{13}(z)=\prod_{\substack{219\le p\le314\\13\nmid p}}(1-z^p)^{-1}
=\frac{1}{13^7(1-z)(1-z^2)(1-z^{11})(1-z^{12})},
\]

\[
B_m(z)=\sum_{\substack{a_1,\ldots,a_5\ge0\\a_1+\cdots+a_5<m}}
z^{6a_1+7a_2+8a_3+9a_4+10a_5}.
\]

The primitive 13th-root contribution to F_m(N) is

\[
\boxed{
F_m^{(13)}(N)=\frac{N^7}{7!\,P_{13}}
\sum_{a=1}^{12}H_{13}(\zeta^a)B_m(\zeta^a)\zeta^{-aN}
+O_m(N^6),\quad\zeta^{13}=1,\quad\operatorname{ord}(\zeta)=13.
}
\tag{1}
\]

The exact threshold coefficient generating function is

\[
\boxed{\sum_{m\ge1}B_m(z)t^{m-1}
=\frac1{(1-t)\prod_{r=6}^{10}(1-z^rt)}
=\frac{\prod_{r\in\{1,2,3,4,5,11,12\}}(1-z^rt)}{1-t^{13}}.}\tag{2}
\]

Define \(Q_j(z)=[t^j]\prod_{r\in\{1,2,3,4,5,11,12\}}(1-z^rt)\), j=0,..,7. Each Q_j is nonzero in Q[z]/Phi_13(z); the constant coordinate in the canonical basis (1,z,..,z^11) equals +1 for all eight (full exact vectors are in RESULT_THIRTEENTH.json). Therefore:

\[
\boxed{
B_m(z)\ne0\iff m\bmod13\in\{1,2,3,4,5,6,7,8\},\quad
B_m(z)=0\iff m\bmod13\in\{9,10,11,12,0\}.}\tag{3}
\]

The first eight threshold classes have a genuine primitive 13th-root pole of order 8 and a nonzero degree-7 cost harmonic. The remaining five classes lose that leading pole and contribute at most O_m(N^6). The exact threshold coefficient sequence B_m has least period 13 (the nontrivial zero/nonzero pattern excludes period 1; 13 is prime).

## Complete proof

Exactly eight prices between 214 and 314 are divisible by 13: 221,234,247,260,273,286,299,312. S0 is the only one of the five separating sets that avoids all eight. Each of S1,S2 includes 221, S3 includes 234,..,286, and S4 includes 299,312. Consequently the only inclusion-exclusion term with an order-eight pole is the singleton S0: all other nonempty event intersections bound at least one 13-divisible multiplicity and have pole order at most seven. In S0, the five constrained price residues are 6,7,8,9,10 modulo 13 and contribute the exact finite polynomial B_m(z). All eight divisible prices are unconstrained; at x=z, each factor (1-x^p)^{-1}, 13|p, has leading Laurent factor p^{-1}(1-x/z)^{-1}. Free nonmultiples 219..314 contribute H_13. These nonmultiples comprise seven full residue cycles and extra residues {1,2,11,12}, so the identity prod_{r=1}^{12}(1-z^r)=13 reduces H_13 to the displayed formula. Extracting the coefficient of (1-x/z)^{-8} gives (1) because [x^N](1-x/z)^{-8}=z^{-N}binom{N+7}{7}.

For (2), each fixed five-tuple of sum s contributes to sum_{m≥1} B_m(z)t^{m-1} the geometric tail t^s/(1-t), giving the first fraction. The cyclotomic product identity prod_{r=0}^{12}(1-z^rt)=1-t^{13} gives the second. Its numerator has degree seven. Hence B_m(z) is Q_{(m-1) mod 13}(z) for residues 0..7 and zero for residues 8..12. Exact multiplication modulo Phi13=1+z+...+z^12 shows all eight Q_j have constant basis coefficient +1 (the attached code recomputes every vector). This proves (3). Nonzero coefficients at primitive roots determine nonzero Fourier modes by invertibility of the 13-point discrete Fourier transform.

## Cost period implication and open branch

Earlier pinned R5 proof gives a least cost period of 2520 at remainder O_m(N^8), and an eleventh-root split at remainder O_m(N^7). At finer remainder O_m(N^6), every m in residues 1..8 mod 13 requires a factor 13 in the cost quasipolynomial period, independently of the 11th-root status; residues 0,9,10,11,12 mod 13 need no factor 13 at degree 7. Roots of order d≥14 have at most seven divisible prices in 214..314 and contribute O_m(N^6). Thus a cost quasipolynomial of period dividing lcm(1,..,13)=360360 exists at this precision for every fixed m. The *least* modulus at O_m(N^6) remains partly open because primitive 11th-root degree-7 terms in its five previously cancelling threshold classes have not been classified.

## Exact evidence and next question

VERIFY_THIRTEENTH.py is an executable standard-library exact integer/rational cyclotomic calculation. It checks: eight Q_j coefficients; coefficient DP through m=78; independent full five-tuple enumeration through m=12; 31 inclusion-exclusion pole counts; and rational Fourier profile. The m=1 primitive-13 cost-residue profile (N=0,..,12), before N^7/(7!P13), is
(14,7,7,-1,-3,-8,-9,-9,-8,-3,-1,7,7)/13^7.
No floating arithmetic or formal proof checker was used. Independent mathematical review remains NOT_REVIEWED.

Next: derive the primitive-11 degree-7 Laurent coefficient when m mod 11 belongs to {0,7,8,9,10}; distinguish the derivative of the S0 term from leading order-eight inclusion-exclusion intersections involving S1 and S2; then use Chinese remainder residue classes modulo 11 and 13 to determine the sharp least period at remainder O_m(N^6). The cyclotomic observer is a scalar R5 cost-phase diagnostic; no X6/BRC physical-state identification is claimed without a typed observer-preserving bridge.

# F7 A6 — Smith invariants and cokernel exponent for arbitrary fixed-scalar index

Date: 2026-10-31. Status: AUTHOR_SIDE / EXPOSED_SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
This supplement belongs to existing Draft PR #1753; it does not alter frozen F7 Result RR-AA38973D56330E59D315 (blob 3366edeae347e76b1f6a50bc45a6c6e4cd2dd472), historical authorship, or existing reviews.

## Statement

Continue the auxiliary group and support scalar in SHARP_INDEX.md and TORSION_EXTENSION.md:

\[
G=\mathbb Z^4\oplus(\mathbb Z/3)^2,\quad C=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
D=\operatorname{diag}(C,C),\quad Q(w,t)=\tfrac12\#\operatorname{supp}(Dw).
\]

The complete fixed-scalar injective/balanced classification from those files gives

\[
F(w,t)=(Aw,Kw+Bt),\quad A=D P\operatorname{diag}(k_1,k_2,k_3,k_4)D,
\]

where P is one of 16 split permutations, each k_i is a nonzero integer, K is arbitrary over F_3, and B is invertible over F_3.

For either input channel pair, the split P sends one channel to output slot 1 and the other to slot 2. Name their multipliers a,b for the first pair (a to slot 1), and c,d for the second pair (c to slot 1); these names may reorder the original k_i.

Let \(\Delta_j\) denote the positive gcd of all j-by-j minors, with \(\Delta_0=1\). Then

\[
\begin{aligned}
\Delta_1&=\gcd(a,b,c,d),\\
\Delta_2&=\gcd(2ab,2ac,2bd,2cd,ad+bc,ad-bc),\\
\Delta_3&=4\gcd(abc,abd,acd,bcd),\\
\Delta_4&=16|abcd|.
\end{aligned}
\]

**Complete formula.** The Smith invariant factors are exactly

\[
(\Delta_1,\Delta_2/\Delta_1,\Delta_3/\Delta_2,\Delta_4/\Delta_3).
\]

**Permutation-independent exponent.** For every split P and every torsion coupling K,B permitted above,

\[
\boxed{\exp(G/F(G))=4\operatorname{lcm}(|k_1|,|k_2|,|k_3|,|k_4|)}.
\]

The index remains \(16\prod_i|k_i|\). For all \(|k_i|=1\) the Smith type is (1,2,2,4), agreeing with SMITH_COKERNEL.md.

## Proof

1. Exchanging the two channels inside an input pair or output pair is an integral unimodular change of free basis, because \(C^{-1}\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}C=\operatorname{diag}(1,-1)\). These exchanges reduce every split permutation to the same representative after labeling the four multipliers by output destination. Smith data are unchanged. Its matrix is

\[
A_0=\begin{pmatrix}
a&a&c&c\\a&a&-c&-c\\b&-b&d&-d\\-b&b&d&-d
\end{pmatrix}.
\]

2. Its entries include all four absolute multiplier values, proving the first gcd. Expanding all 36 two-by-two minors shows each nonzero minor is one of the signed quantities \(2ab,2ac,2bd,2cd,ad+bc,ad-bc\), and each of these six quantities occurs. This yields \(\Delta_2\).

3. Since \(D^2=2I\), its inverse is \(A^{-1}=\frac14D\operatorname{diag}(1/k_i)P^{-1}D\). Because P splits the channels, **each** 2-by-2 slot block of the inverse contains four entries of absolute value \(1/(4|k_j|)\) for exactly one j; all four j occur. Since \(|\det A|=16\prod_i|k_i|\), the adjugate identity shows that the nonzero absolute 3-by-3 cofactor values are exactly \(4|\prod_{i\ne j}k_i|\), once for each j. Their gcd is \(\Delta_3\), and the determinant gives \(\Delta_4\). Smith determinantal divisors yield the listed invariant factors.

4. The exponent of \(\mathbb Z^4/A\mathbb Z^4\) is the least positive m with \(mA^{-1}\) integral. The inverse's explicit entries make this equivalent to \(4|k_i|\mid m\) for all i. Thus the exponent is \(4\operatorname{lcm}(|k_i|)\), independently of P.

5. As B is invertible, over every free output in \(A\mathbb Z^4\), all torsion outputs can be achieved by adjusting the input torsion. Therefore projection induces \(G/F(G)\cong\mathbb Z^4/A\mathbb Z^4\), giving the same invariant factors and exponent regardless of K,B.

For each odd prime p, D and P are invertible over the p-adic integers, so the p-primary Smith exponents are precisely the sorted p-adic valuations of the four k_i. When all k_i are odd, the 2-primary exponents are always (0,1,1,2).

## Evidence and limits

FULL_SMITH_CHECK.py computes exact integer minors for all 16 split permutations and all 6^4 multiplier tuples from {-3,-2,-1,1,2,3}: **20,736** matrices. It checks every determinantal divisor and the exponent formula. This finite regression is not the proof of the universal claim; the algebra above is. The statement remains confined to the declared auxiliary support scalar, not arbitrary F7 scalar laws, native X6 dynamics, or a three-dimensional research slice. It is an exposed author-side contribution and **not** an independently authorized Review/Reference/Synthesis/Follow-up or formal task publication.

# PREFIX-963 — The complete seven-gap coarse-support spectrum for adjacent-core named XOR histories

Date: 2026-11-20. Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged). This is an independent continuation of PREFIX-960 (seven-gap theorem) and PREFIX-961/962 (gap-six/five necessary support). Mathematical classification: **author proof and reproducible exact integer tests; NOT_REVIEWED**. Historical R6 source context refers to EM-DIRECT-58C410; that label does not attest current formal execution authorization.

## Statement and observation type

Fix an integer p>=4, H=2^(p-1), N=H/2=2^(p-2), and the ordered odd-modulus domain Qp={H+1,H+3,...,2H-1}. For an odd k>=1 with k+2<H consider named pairs of equations

    ((k*a) XOR 2^j)-2^i=t*b
    (((k+2)*a) XOR 2^J)-2^I=T*b,

where a,b in Qp, t,T positive integers and 0<=i,j,I,J<p. Put m=T-t, c=2^i-s2^j, C=2^I-S2^J, s=1-2*bit_j(k*a), S=1-2*bit_J((k+2)*a). The exact residual relation is

    C-c = 2*a-m*b.

For a **necessary pre-XOR filter**, relax the actual source dictionary to the universal numerical bounds 1-H<=c,C<=2H. Hence every named witness must satisfy

    1-3H <= 2*a-m*b <= 3H-1.                    (*)

Define E_p(m) as the set of ordered (a,b) in Qp^2 satisfying (*), and A_p(m)=|E_p(m)|; D_p(m) counts the diagonal a=b in E_p(m). These are counts of a *coarse necessary numerical support*, not claims of existence or multiplicity of genuine XOR witnesses. An operation retaining only membership in E_p(m) discards source labels; the full named witness observer is unchanged.

## Theorem 963.1 — Complete seven-gap support spectrum

For p>=4 and m in {0,1,2,3,4,5,6}, let R=N/2 and q=floor((R-3)/3). Then

    A_p(0) = N^2/2
    A_p(1) = N^2
    A_p(2) = N^2
    A_p(3) = (11*N^2+4)/12
    A_p(4) = N^2/2
    A_p(5) = (N^2-(-1)^p)/5
    A_p(6) = 0                                     if q<0,
             (q+1)*(R-2)-3*q*(q+1)/2             otherwise.

The exact diagonal counts are

    (D_p(0),...,D_p(6)) = (N/2,N,N,N,N/2,0,0).

Thus every off-diagonal necessary-domain count equals A_p(m)-D_p(m). In particular the *exact equinumerosity* A_p(0)=A_p(4)=N^2/2 holds for every p>=4, although the two supporting subsets are geometrically different. PREFIX-960 establishes that every actual adjacent-core witness has m in {0,...,6}, so these seven counts exhaust this specific coarse necessary interval sieve.

## Proof

Write a=H+2r+1, b=H+2z+1 with 0<=r,z<N. Then the test (*) becomes

    1-3H <= (2-m)*H+4r-2m*z+(2-m) <=3H-1.   (1)

For m=1,2 both inequalities hold throughout the square. For m=0 only the upper bound is active, equivalent to 0<=r<N/2; hence A0=N^2/2.

For m=3 only the lower bound is active; it reads 2r-3z>=1-2N. Its failure is 3z-2r>=2N, which under z=N-w is equivalent to w>=1, r>=0, 3w+2r<=N. The number B of failures is

    B = sum_{w=1}^{floor(N/3)} (floor((N-3w)/2)+1).

Since N=2^(p-2), N modulo 6 is 2 or 4. Splitting w by parity gives B=3h^2+2h if N=6h+2 and B=3h^2+4h+1 if N=6h+4. Both equal (N^2-4)/12. Therefore A3=N^2-B=(11N^2+4)/12.

For m=4 only the lower bound is active and simplifies to

    r >= 2z+1-N/2.                                (2)

On the integer square, the central involution (r,z)->(N-1-r,N-1-z) exchanges (2) with its strict complement r<=2z-N/2. There are no fixed integer points because N is even. Therefore precisely half of the N^2 ordered pairs satisfy (2), proving A4=N^2/2. The same involution exchanges the m=0 half-rectangle with its complement, but does not identify the source-labelled witness fibers.

For m=5 the only active inequality reduces to r>=ceil((5z+2)/2). Its exact sum over 0<=z<=floor((2N-4)/5), grouped by the parity of z, is (N^2-(-1)^p)/5; this is also Theorem 962.1 at the identical frozen input. For m=6 it reduces to r>=3z+R+2, whence 0<=z<=q and the count is sum_{z=0}^q(R-3z-2), giving the stated formula (Theorem 961.1 at the same pin).

On a=b, (1) becomes 1-3H<=(2-m)*a<=3H-1. It holds for all N diagonal values at m=1,2,3; for exactly the first N/2 values at m=0,4; and for none at m=5,6. This proves the diagonal and off-diagonal counts. QED.

## New structural corollary — Complement involution for the gap-four sieve

Let S4={(r,z): r-2z >= 1-N/2}. The involution (r,z)->(N-1-r,N-1-z) maps S4 bijectively to its **complement** in the N-by-N square. Hence any exhaustive pre-XOR pair-counting or randomized sampling implementation can certify the exact 1/2 filter rate by checking one representative of each central pair. This is an exact symmetry of the coarse numerical observer only; neither the actual XOR bit signs nor source multiplicities are asserted invariant.

## Exact numerical verification

The Python 3 script PREFIX963_R6_GAP_SUPPORT_SPECTRUM.py verifies all seven formulas and the diagonal counts by an independent O(7N) interval-endpoint count for every p from 4 to 15, and again at p=19 with N=131072. It separately enumerates every ordered (r,z) and tests the original interval inequality for p=4..9. Every comparison passed using integers only. The interval endpoint routine is exact because 2v=4r+2, hence the eligible r are precisely the integers between ceil((lo-2)/4) and floor((hi-2)/4), clamped to [0,N-1]. The Python script and JSON store the precise tested domain and results.

For p=19 the ordered-pair counts at gaps m=0,...,6 are respectively

    8,589,934,592; 17,179,869,184; 17,179,869,184;
    15,748,213,419; 8,589,934,592; 3,435,973,837; 715,816,960.

After excluding the diagonal they are respectively

    8,589,869,056; 17,179,738,112; 17,179,738,112;
    15,748,082,347; 8,589,869,056; 3,435,973,837; 715,816,960.

The m=5 and m=6 columns coincide with independent PREFIX-962 and PREFIX-961 necessary-domain certificates. No Q19 core21/23 actual witness counts change: its pre-existing [6,442,4724,839,190,3,0] gap memberships and 8649 named witnesses have a substantially stronger source/quotient predicate than (*).

## Research role, provenance, and limits

This result is a **universal theorem about the auxiliary integer/XOR observation model's necessary support**. It neither assigns native X6 Cell identity to (a,b) nor lifts to a P000 physical triadic rotation or BRC path composition without an operation-preserving typed map. The necessary support is a lossy *filter only*: original (i,j,I,J), actual bit signs, positive t,T, and pair multiplicity must be preserved for all outputs relying on them. No CLAIM, RESULT, Review or foundation acceptance follows from publication. Historical researcher label EM-DIRECT-58C410 is provenance only; live owner is determined from its separate control receipt.

The next useful scientific test is to insert the full seven-gap support table as an **early cheap rejection filter** in PREFIX-959B's cached odd-divisor-fiber generator and measure actual total costs, while preserving all named histories. A second question is whether arithmetic congruence refinements can turn this coarse support into a stronger operator-safe index without losing source-labeled multiplicity. The parent bound B_fix,odd(32) in {19,20} remains open.

Relevant source links (frozen scientific pin unchanged):
- PREFIX-960: research_notes/portable_direct/2026-11-20_r6_prefix960_universal_gap_window_sharpness.md
- PREFIX-961: research_notes/portable_direct/2026-11-20_r6_prefix961_gap6_endpoint_triangle_and_source_localization.md
- PREFIX-962: research_notes/portable_direct/2026-11-20_r6_prefix962_gap5_exact_one_fifth_support.md

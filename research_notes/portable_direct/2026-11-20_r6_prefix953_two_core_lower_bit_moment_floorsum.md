# PREFIX-953 — Exact two-core lower-bit witness correlation by dyadic pairing and floor sums

**Date:** 2026-11-20. **Frozen scientific input:** f42f2906d77f24085c123f3ccfe9667d41caa96d. **Predecessor:** PREFIX-952, immutable blob 95674d077b82cc425ae8d8ecfd92a57bf5fdb960; PREFIX-948 common-core census. **Model:** auxiliary named-XOR two-port observer, unbounded-trace statement; p=19, k=21,23 specialization also obeys 32-bit endpoint bounds. This is an auxiliary observer arithmetic theorem, not a native signed-X6/BRC dynamics assertion. **Status:** author-proved; exact finite integer checks; no independent mathematical review or project admission.

## Theorem: all odd pairs, arbitrary width

Let p >= 4, H=2^(p-1), N=2^(p-2), Q_p={H+1,H+3,...,2H-1}. Fix odd 1<=k,l<H. Preserve named source-bit indicators

    e_j(k,a) = 1[bit_j(k*a)=0],  1<=j<=p-2
    L_p(k,a) = sum_{j=1}^{p-2} e_j(k,a)
    U_p(k,l) = sum_{a in Q_p} L_p(k,a)*L_p(l,a).

The bit is read from the natural integer product, equivalently modulo 2^(j+1).

For integer n>=0,m>0,u,v>=0 put

    F(n,m,u,v) = sum_{r=0}^{n-1} floor((u*r+v)/m).

For j=1,...,p-2 define q_j = l*k^{-1} modulo 2^(j+1), using the positive odd representative, and h_j=2^(j-1). Define

    C_j = h_j - F(h_j,2^j,2*q_j,q_j)
                + 2 F(h_j,2^(j+1),2*q_j,q_j).

Then the following **exact identity** holds:

    U_p(k,l) = N*(p-2)*(p-3)/4
               + sum_{j=1}^{p-2} (N/2^j)*C_j.              (1)

Here 0<=C_j<=2^(j-1). The formula uses p-2 odd modular inverses and 2(p-2) Euclidean floor sums, without scanning all N moduli. Each floor sum uses O(log m) arithmetic iterations; large-integer bit complexity must be accounted for separately. The apparent directional q_j expression gives a symmetric U_p(k,l).

### Proof

The N odd moduli in Q_p reduce bijectively to odd residues modulo H. For every j<=p-2, multiplication by odd k permutes odd classes modulo 2^(j+1); exactly N/2 a have e_j(k,a)=1.

For two different named bit positions j<j'<=p-2, consider the involution on the odd residues modulo H given by a -> a+2^(j') modulo H. It preserves bit_j(k*a), while it flips bit_j'(l*a) because l is odd. Consequently, among the N/2 a satisfying e_j(k,a)=1, exactly half also satisfy e_j'(l,a)=1. The same argument holds with indices exchanged. Each differently indexed term contributes N/4. There are (p-2)(p-3) ordered terms with unequal indices, giving the first term of (1).

For the same index j, let x=k*a modulo 2^(j+1). As a varies, x runs uniformly over all 2^j odd residues. The bit_j(x)=0 condition selects exactly x=2r+1, 0<=r<2^(j-1). On those residues bit_j(l*a)=bit_j(q_j*x). The exact number of simultaneous zero bits per residue period is

    C_j = #{r: 0<=r<2^(j-1), bit_j(q_j*(2r+1))=0}.

For all nonnegative y, bit_j(y)=floor(y/2^j)-2floor(y/2^(j+1)). Substitution gives the displayed floor-sum formula. Each residue pattern repeats N/2^j times in Q_p. Summing all same-index and unequal-index terms establishes (1). QED.

The result is a labeled-multiplicity carrier. Boolean support stating merely whether a collision exists cannot recover its source-bit second moment. In BRC usage, this exact positive integer moment can be retained without collapsing named observer fibers.

## Q19 exact specialization, cores 21 and 23

For p=19 and N=131072, the unequal-index term is 8,912,896. The 17 same-index bucket contributions for j=1,...,17 are

    [0,65536,32768,16384,24576,28672,38912,33792,32256,
     33024,32896,32576,32928,32848,32824,32836,32834].

Their sum added to the unequal-index term gives

    U_19(21,23) = 9,448,558.

Direct independent Q19 scanning confirms this value and every bucket. At j=1, C_1=0: core 21 is 1 mod 4 while core 23 is 3 mod 4, so their named bit-1 zero indicators are mutually exclusive.

Define T(k,a)=1[bit_18(k*a)=0] and Z(k,a)=L(k,a)+T(k,a). The independently computed exact top contributions are

    sum_a L(21,a)*T(23,a) =   532,848
    sum_a T(21,a)*L(23,a) =   530,485
    sum_a T(21,a)*T(23,a) =    29,848
    sum_a Z(21,a)*Z(23,a) = 10,541,739.

The final value independently reproduces the previously established PREFIX-948 rank-one diagonal named-witness combination count. By PREFIX-952 the full witness count is w(k,a)=Z(k,a)+2*[a=262145]*[k>=3]. At a=262145, Z(21,a)=15 and Z(23,a)=14, hence the additional nonresonant source-pair contribution is 2*(15+14)+4=62, yielding

    sum_{a in Q19} w(21,a)*w(23,a) = 10,541,801.

This is a second moment of named diagonal witnesses, not a number of distinct (a,b) collisions. No new union-coverage total is claimed.

## Independent exact tests

- Python Euclidean floor-sum formula vs direct original Q_p enumeration for **all 5456 ordered odd-core pairs** combined over p=4,5,6,7,8. Each same-index floor-sum bucket was also checked by direct odd-residue enumeration in a second verifier. All matched.
- For p=19, k=21,l=23 and the reversed order, exact floor sums match a full 131072-modulus direct scan; all 17 buckets match.
- Independently implemented C++17 directly scans the Q19 population and obtains U=9448558, lower/top cross sums 532848/530485, top/top=29848, Z product 10541739 and full named product 10541801. No stochastic or floating-point arithmetic.
- Runnable sources: PREFIX953_R6_COMPACT_VERIFIER.py and PREFIX953_R6_INDEPENDENT_DIRECT_CPP.cpp. Machine-readable computed counts: PREFIX953_R6_EXACT_RESULTS.json, all in research_notes/portable_direct/.

## Boundary and next problem

The universal theorem covers lower source positions 1..p-2. The displayed full-width top terms at p=19 were computed by exact direct scanning, not by a new logarithmic algorithm. The auxiliary model has no asserted native-X6 correspondence unless the needed typed state, named-source map, observer and future-operation preservation are supplied. The historical conditional union of distinct pairs is unchanged; the mother question B_fix,odd(32) in {19,20} stays open.

Next: derive a sublinear exact top-bit cross-correlation formula and use the determinant/CRT nonresonant equations to count the 6203 off-diagonal W21 intersection W23 pairs without materializing W21 or W23.

Original R6 lineage: EM-DIRECT-58C410 / historical SID MCP-31edc522830749ad8775ca012e02ef30 / Activity RA-25432C4AAE9BF66A907F5115. These are provenance, not current private-session authorization. Shared Task CLAIM, Activity CAS, Source independent audit, mathematical review and project admission are distinct from publishing this scientific note.

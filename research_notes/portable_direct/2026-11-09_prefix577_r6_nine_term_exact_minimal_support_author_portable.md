# BRC-X6：九项最优保真分解的单纯形面和全正概率证书

**Evidence status:** AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED; author-portable only, not a native Source Result/CLAIM. Frozen science pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`; frozen kernel SHA-256 `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`. 96 native ports, 576 labeled actions, nine frozen roots. Full output atom: `(next_port,R1,...,R6,K)`. Source ports (6,7,28,29), signed coefficients (+1,-1,-1,+1), preserving source labels.

Let P be the convex hull of the 38 deterministic 4-action choices whose signed native joint-output atoms cancel exactly at each frozen root. The 4x6 row probability coordinate order is source ports 6,7,28,29, actions 0,...,5. minSupport is the least number of positively weighted preserving pure policies in a convex decomposition.

## Theorem A: a 9-vertex simplex face and an 8-parameter optimal family

Set flattened original coordinate indices `Z={2,6,8,10,11}` to zero. Native exhaustive enumeration of the 6^4=1296 four-action choices gives exactly these nine feasible vertices of P:

```
(0,1,2,3) (1,1,3,3) (3,3,0,0)
(3,3,1,1) (3,3,2,2) (3,3,4,4)
(3,3,5,5) (4,1,0,3) (5,1,1,3)
```

The augmented 25x9 matrix (top row all 1; 24 subsequent rows are the original independent action coordinates) has a 9x9 minor on rows `(0,1,2,4,5,13,14,15,17)` with **integer determinant +1**. Thus these nine pure policies are affinely independent. The coordinate-zero intersection is a face, because P has nonnegative coordinates. Any positive convex representation of a point on this face must use only its nine vertices. Consequently, for all real `lambda_i>0, sum lambda_i=1`, the point `x=sum lambda_i*v_i` has **minSupport(x)=9**, and that preserving-pure-policy representation is unique.

For lambda_i=1/9, a small exact witness is the following 4x6 matrix:
```
[1,1,0,5,1,1]/9
[0,4,0,5,0,0]/9
[2,2,2,1,1,1]/9
[1,1,1,4,1,1]/9
```

## Theorem B: a strictly full-support 9-term optimum

Take the following nine legal preserving pure policies:
```
(0,0,2,2) (1,0,3,2) (2,2,4,4)
(3,3,5,5) (4,4,0,0) (4,4,5,5)
(4,5,0,1) (5,1,1,3) (5,5,5,5)
```
Their augmented 25x9 binary matrix has an integer 9x9 minor on rows `(0,1,2,3,4,5,8,11,13)` equal to **-1**. Every one of 24 action coordinates occurs in at least one chosen vertex. For `B=32768` and `D=sum_{i=0}^8 B^i`, define `x*=sum_{i=0}^8 (B^i/D) v_i`. Then each of the 24 original action probabilities is strictly positive and **minSupport(x*)=9**.

For completeness, a general exact proof of the lower bound follows. For any proposed collection T of at most 8 preserving pure policies, let r<=8 be the linear rank of their augmented binary columns and choose r independent columns. The selected 9 columns of x* have rank 9, so at least one is outside span(T). One can select r+1 rows to define an integer determinant linear functional L vanishing on span(T) but not all nine selected columns. By Hadamard, for each selected binary column |L(v_i)| <= (r+1)^((r+1)/2) <= 9^(9/2) = 19683. A nonzero integer polynomial `sum_{i=0}^8 L(v_i) B^i` cannot vanish at B=32768: its highest nonzero coefficient contributes at least B^k in absolute value, while all lower terms contribute less than `19683*(B^k-1)/(B-1) < B^k`. Thus x* is not in the affine span of any <=8 allowed vertices. The exhibited 9-term convex representation is exact, establishing optimality.

## Verification / provenance

Author-side exact integer verification rebuilt all 38 legal pure choices independently for all nine frozen roots (11,664 source 4-action candidates), checked each root's complete joint output cancellation, verified the two minors with integer Bareiss arithmetic, and checked both probability examples. A separate independent reconstruction of all 9x96x6 = 5,184 native labeled edges, 11,664 candidate choices and SymPy exact rank/determinants agreed. Certificate: `NINE_SIMPLEX_FACE_CERTIFICATE.json`; local portable programs `verify_nine_simplex_face.py` and `independent_verify_nine_simplex_face.py` accompany this author result.

This author-side result consumes prior 38-vertex and 8-term studies, preserving D25's frozen original-class H0/B0, divided-power, semilinear Frobenius and CM unfinished frontier and the UR V2 provenance debt (94,687-byte four-file bundle, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`). It asserts no valid active CLAIM, native OPEN/checkpoint, independent review or mathematical admission. Next concrete research: an arbitrary rational input's minimum-support exact optimizer and finite infeasibility certificates, with this full-support nine-term witness as a benchmark.

# PREFIX-909 — Odd-parity endpoint-multiplier channels, exact 19-bit collision union

Date: 2026-11-18 (Asia/Shanghai). Research lane: 进取数论研究6. Independent, provenance-retaining BRC auxiliary two-port observer. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d. Predecessor: PREFIX-908 (7,778,794,188 certified ordered pairs).
Status: AUTHOR_PROVED / TWO_INDEPENDENT_FINITE_EXACT_RECOUNTS / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Model and new question

Let N=2^32 and Q={262145,262147,...,524287}, |Q|=131072. Named legal tracks are Z_x=(x,x) and F_x^i=(x,x XOR 2^i), 0<=x<N and 0<=i<32. The auxiliary observation is Phi_(a,b)(u,v)=(u modulo a,v modulo b), with full source names and trajectories preserved before observing.

PREFIX-907 established the general unequal-multiplier two-source-bit construction, while PREFIX-908 filled the j=0 sector for (k,ell)=(2,1). This note applies the missing *other odd-parity multiplier pairs* (3,2), (4,1) and (4,3), proving an explicit new finite certificate union after exact predecessor deduplication.

## Theorem 909-A: complete low-bit witness for opposite-parity endpoint multipliers

Let positive k,ell have opposite parity, a,b be odd positive integers, and 1<=i<32, s in {-1,+1}. Suppose

  k*a - ell*b = 2^i+s.

Put H=2^i and x=1-(k mod 2) if s=+1; x=(k mod 2) if s=-1. Set y=x+k*a. Whenever all displayed endpoints lie in [0,N), the two distinct named tracks

  F_x^i=(x,x+H), F_y^0=(y,y-s)

collide at both observation ports.

Proof: x is either 0 or 1 and hence x XOR H=x+H. Since a is odd, y parity is x+k modulo 2. The chosen x makes y odd when s=+1 and even when s=-1; consequently y XOR 1=y-s. The starts differ by y-x=k*a, and the endpoints by

  (y-s)-(x+H)=k*a-(H+s)=ell*b.

Both port residues coincide. The differing source indices 0 and i, and positive start separation, make the trajectories distinct. QED.

For Q as above and 1<=ell<k<=4, 1<=i<=22, endpoint validity is automatic:
x<=1, y<=1+4*524287=2097149, x+H<=1+2^22=4194305, y-s<=2097150, all strictly less than 2^32. Thus no untested endpoint filter is hidden in the census. The parity identity also shows that if k and ell are of opposite parity, any equality k*a-ell*b=2^i +/-2^j with i>j requires j=0.

Note: this theorem generalizes the elementary parity case of PREFIX-908; the new scientific information in this note is the three-channel full finite census and *non-overlapping* new certificate coverage. It does not assert a native X6 time transition.

## Theorem 909-B: exact new certified ordered-pair coverage

Let R be the union of ordered (a,b) in Q^2 satisfying k*a-ell*b=2^i+s for (k,ell) in {(3,2),(4,1),(4,3)}, i=1..22, s in {-1,+1}. Let C908 be exactly the predecessor's explicitly enumerated collision certificates:
- baseline E: ab<33N; either modulus in the exact 552-element special U; lcm(a,b)<N; either 33 ceil(N/a)>b or its port transpose;
- the 192-member fully certified row/column panel P;
- signed absolute modulus gaps from 258 old classes, 276 PREFIX-905 classes, 857 PREFIX-906 classes;
- both orientations of the 169 signed powers 3a-b=2^i +/- 2^j (18<=i<=22,1<=j<=17);
- both orientations of 37 values 2a-b=2^i +/-1 (1<=i<=19).

This fully specified C908 is symmetric under a,b transposition. Both independent checkers reconstruct these exact predecessor classes and assert their sizes.

| New family (k,ell) | Parameter witnesses | Distinct oriented pairs | Oriented pairs outside C908 |
|---|---:|---:|---:|
| (3,2) | 961,191 | 939,346 | 452,790 |
| (4,1) | 65,536 | 65,536 | 31,110 |
| (4,3) | 917,500 | 895,655 | 453,522 |

Across the three families together, |R|=1,900,472 (inter-family overlaps removed). Let A=R\C908. The exact set-based computation yields |A|=937,399 and |A intersect A^T|=0, where A^T={(b,a):(a,b) in A}. Reversing endpoints of the two directed XOR flips and exchanging observation ports produces a valid reverse collision, as used in the PREFIX-894 observer-level proof. Hence

  |C909\C908|=|A union A^T|=2*937399-0=1,874,798,

  |C909|=7,778,794,188+1,874,798=7,780,668,986,

  |Q^2\C909|=131072^2-7,780,668,986=9,399,200,198.

The raw R intersects R^T in 45 oriented pairs; the post-C908 new intersection is zero. These counts are exactly for the declared certificate union, rather than all potential XOR collisions.

A new explicit witness outside C908 has a=400003,b=468933,k=3,ell=2,i=18,s=-1:
F_1^18=(1,262145), F_1200010^0=(1200010,1200011).
Their start difference is 1,200,009=3a and endpoint difference 937,866=2b. Both states and bit transitions are valid. Source names 18 and 0 remain distinct.

## Validation and reproducibility

PREFIX909_R6_MIXED_MULTIPLIER_CHECK.js independently regenerates the seven predecessor class sizes [258,276,857,552,192,169,37], enumerates every candidate (a,i,s) for each selected (k,ell), asserts each named XOR witness and exact modular equality, constructs oriented sets, subtracts C908, and computes the transpose union with 53-bit-safe integer pair IDs. All checked endpoints are below 2^32 and bitwise XOR uses only bit positions up to 22.

PREFIX909_R6_INDEPENDENT_CHECK.py independently rebuilds predecessor membership, all candidate sets, endpoint and XOR checks, and the four union counts using arbitrary-precision Python integers. Executed output: INDEPENDENT_PYTHON_RECOUNT_PASS; it reproduces all per-family and union counts. The JSON certificate lists the exact observations and one sample witness. Verification is *finite exhaustive* for the three declared parameter families; the accompanying mathematical witness formula applies under its stated general hypotheses.

## Ontology and future work

All results are in the auxiliary named-XOR/BRC observer; no native P000 Cell/Link/Port event is identified with these tracks. Six native spatial axes, triadic closure and separately typed time remain frozen and unchanged. The shared RS-X6-NATIVE-TIME-DYNAMICS Task needs its own current CLAIM and native admission evidence.

Next discriminating computations: scan additional opposite-parity coprime (k,ell) channels (e.g. 5,2; 5,4; 6,1) against the *exact C909* union, and search the finite complement using the full two-flip carry condition. The mother objective remains B_fix,odd(32) in {19,20}; the present certificate proves collisions on exactly its declared C909 subset.

Provenance: PREFIX-907, PREFIX-908 and the local reproducible Node.js/Python integer runs on 2026-11-18. Author analysis only, no independent formal review or Foundation admission.

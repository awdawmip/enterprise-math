# R5 addendum — sharp first lawful 14-edge contact at the quotient separator

Date: 2026-11-10 Asia/Shanghai. Same frozen scientific pins as RESEARCH.md, source PR #1939 and PR #1947. Author-side exact proof, independent review pending.

## Sharpness theorem

Let R = 49948501046391/3920403670319950000 and x = (-1,1,1,-1,-1,-1,-1,1). Define zc = R*x in the eight-parameter physical affine family. At this exact contact point,

mu_1(zc) = 16932541854726549/313632293625596000000 > 0,

s25(zc) = 3836062555208901/156816146812798000000 > 0.

All 26 original source/target physical capacity slacks are nonnegative (all nonstructural other slacks positive), and all five original physical equalities hold. This is a **lawful** point with positive mu_1 on the cube boundary ||zc||_infinity=R.

The ten mandatory branches from PR #1939, in index order, are

F = ((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6)).

The four additional edges

S = ((2,1),(3,2),(0,3),(1,5))

give a strictly positive 14-edge rational Blackwell transfer. The EXACT 14 coefficients, in order F+S, are in the adjacent FIRST_14_CONTACT_OUTPUT.txt and are recomputed in VERIFY_FIRST_14_CONTACT.py. That executable checks all 21 original Blackwell equations, not only the 15-row reduced or quotient equations.

For minimality, the predecessor's exact ten dual edge-forcing witnesses remain strictly valid at zc because ||t*+zc||_infinity <= ||t*||_infinity+R < 18052765669/423284426970000. Every feasible transport therefore uses F. At the actual five-dimensional quotient RHS q(zc), every one of C(20,3)=1,140 three-additional-edge subsets fails the exact rank membership condition rank([V_subset | q(zc)]) = rank(V_subset). This was rerun with rational SymPy matrices for this contact. Hence no transport with <=13 positive edges exists. The pointwise minimum is EXACTLY 14.

Combining this lawful 14-edge boundary instance with RESEARCH.md (which proved pointwise minimum 15 for all lawful mu_1>0 parameters with ||z||_infinity < R) establishes that R is the **sharp supremum radius for uniform 15-edge necessity in the lawful mu_1>0 region**, for the selected physical center and eight parameter directions. The condition is strict: at the radius R itself the 14-edge counterexample exists.

## First separator is a real phase contact

One separating five-dimensional quotient normal w=(0,-25,1,1,1) gives

a = w·q(0) = 5549833449599/5577764280000000,

v = w·Q8 = (421/800, -11749/2592, -9511/7200, 21/32, 11579/800, 11749/2592, 9511/7200, -41093/810).

R=a/(sum_k |v_k|), and x is the unique minimizing sign corner. A rank-three quartet with this w also forces mu_1=0 and does not realize a legal transport at x; the rank-four quartet S does, with its 14 positive coefficients. Thus the first zero of the separator is an actual positive-mass legal sparsity transition, not an artifact of an impossible quotient support.

## Exact certificate and next action

VERIFY_FIRST_14_CONTACT.py runs exact rational Fraction/SymPy arithmetic, constructs the immutable frozen physical RHS, validates the explicit 14-edge transfer, all 26 capacity slacks, five physical equalities, and exhaustively eliminates all 1,140 <=13-edge quotient candidates. It reuses the predecessor's certified ten mandatory edges without rerunning that historical dual audit. FIRST_14_CONTACT_OUTPUT.txt is actual local stdout.

Next: classify the rank-four supports meeting this boundary, determine the exact 14-edge tangent cone, and find whether a lawful 13-edge intersection is reachable nearby. Preserve BRC transport branch identity and the complete physical observer when using the quotient criterion.

# PREFIX-908 — Low-source-bit mixed-parity collision and exact new 19-bit union

Date: 2026-11-18 (Asia/Shanghai). Enterprise Math lane: 进取数论研究6; independent, provenance-retaining auxiliary BRC two-port observer.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unaltered).
Predecessor: [PREFIX-907](2026-11-18_r6_prefix907_unequal_endpoint_multiplier_collision.md), with exact certified union `|C907|=7,778,425,088`.
Evidence: AUTHOR_PROVED / EXACT_FINITE_INTEGER_COMPUTED / INDEPENDENT_PYTHON_RECOUNT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Precise mathematical model and scope

Let `N=2^32`, `Q={262145,262147,...,524287}` (`|Q|=131072`). Each directed, named trajectory is either `Z_x=(x,x)` or `F_x^i=(x,x XOR 2^i)`, with `0<=x<N,0<=i<32`. For `a,b in Q`, the *auxiliary* observer is `Phi_(a,b)(u,v)=(u mod a,v mod b)`; full endpoints and source names remain distinct before observation.

## Theorem 908-A — Parity classification and constructive low-bit lift

For odd `a,b`, an equation `k a - ell b = 2^i+s 2^j` with `i>j>=0`, `s=+1` or `-1`, has left-side parity `k-ell (mod 2)`. Therefore, **opposite-parity multipliers require j=0**, whereas equal-parity multipliers require `j>=1`, except for an impossible same-parity `j=0` equation. The earlier source-bit scans explicitly restricted `j>=1`.

For any `a,b in Q`, if `2a-b=2^i+s` for some `1<=i<=19`, `s in {-1,+1}`, there are two distinct legal trajectories with identical two-port observations.

**Constructive proof.** Put `A=2a`, `H=2^i`, `h=1`, and set `x=1` if `s=+1`, otherwise `x=0`. Let `y=x+A`. Because `x<H`, `x XOR H=x+H`. Since `A` is even, `y` is odd if `s=+1` and even if `s=-1`; hence `y XOR 1=y-s`. The named tracks
`F_x^i=(x,x+H)` and `F_y^0=(y,y-s)`
have starting-point difference `A=2a` and ending-point difference
`(y-s)-(x+H)=2a-(2^i+s)=b`.
The difference at each port is divisible by its modulus. Uniform endpoint bounds are
`0<=x<=1`, `y<=1+2*524287=1,048,575<N`,
`x+H<=1+2^19=524,289<N`, and `0<=y-s<N`.
The traces differ in both named source index and starting endpoint. Reversing the two flips and exchanging the ports gives a collision for `(b,a)`. QED.

This extends the unequal-multiplier construction of PREFIX-907 into the `j=0`, opposite-parity sector; no native-world time reversal is being asserted.

## Theorem 908-B — Finite exact census and fresh overlap-free coverage

Set `D={2^i+s:1<=i<=19,s in {-1,+1}}` with repeated values removed (`|D|=37`), and
`R={(a,b) in Q^2:2a-b in D}`. For every `d in D`, the admissible `a` are precisely the odd integers in
`[max(L,ceil((L+d)/2)), min(H,floor((H+d)/2))]`,
where `L=262145,H=524287`. Summing these finite odd-interval cardinalities yields `|R|=393,214`. Complete enumeration independently obtains the same number, with `|R intersect R^T|=6`.

The precise predecessor set `C907` is reconstructed from the immutable source of PREFIX-907's verifier:
- `E`: capacity `ab<33N`, the exact 552-member special-modulus set `U`, zero-track `lcm(a,b)<N`, or either endpoint-fiber capacity condition;
- the 192-member panel of certified rows and columns;
- the deduplicated 258 old signed-gap classes, 276 PREFIX-905 classes and 857 PREFIX-906 high-source classes, with pair membership `|a-b|`;
- PREFIX-907's oriented `3a-b=2^i±2^j` (`18<=i<=22,1<=j<=17`) and the reverse orientation.

All pairs in this explicit `C907` are certified collisions. The new oriented family separates exactly as follows:

| Exact disjoint classification of R | Count |
|---|---:|
| Already in E/panel/old gap classes | 208,655 |
| Not above, but in the PREFIX-907 unequal-multiplier family or its transpose | 9 |
| **Novel oriented pairs A=R\\C907** | **184,550** |
| **Total |R|** | **393,214** |

The independent source-based census establishes `|A intersect A^T|=0`. Since `C907` is symmetric under port exchange, the exact new distinct ordered coverage is
`|A union A^T|=2*184550-0=369100`.
Thus the expanded *explicit certificate union* is
`|C908|=7,778,425,088+369,100=7,778,794,188`,
and its declared strict-19-bit complement has size
`131072^2-7,778,794,188=9,401,074,996`.

**Concrete new witness outside C907.** Take `a=500001,b=475713,i=19,s=+1`. Then `2a-b=524289=2^19+1`, with tracks
`F_1^19=(1,524289)` and `F_1000003^0=(1000003,1000002)`.
The start difference is `1,000,002=2a`; the endpoint difference is `475,713=b`. The checker also tests its nonmembership in every class of the explicit predecessor union.

## Verification and evidence

The companion dependency-free JavaScript checker regenerates the exact predecessor classes `258/276/857`, `U=552`, `P=192`, and `169` distinct PREFIX-907 signed-power values. It generates every `d in D` and every valid `(a,b)`, asserts all **393,214** concrete XOR witnesses, verifies both congruences, checks endpoint bounds, and recomputes the finite analytic count and exact overlap. Every integer calculation stays below JavaScript's safe-integer bound; bitwise XOR is only applied to unsigned values below `2^20`. An independently implemented Python exact-integer enumeration, with explicit reconstruction of the same old classes and a set-based PREFIX-907 comparison, obtained identical counts: `393214/208655/9/184550/0/369100`.

Files: `PREFIX908_R6_LOW_BIT_MIXED_PARITY_CHECK.js`; `PREFIX908_R6_LOW_BIT_MIXED_PARITY_RESULTS.json`.

## Scientific status and next question

This is an exact, finite BRC auxiliary *observation collision* theorem; its full named trajectories and provenance are retained. P000's six-axis native Cell ontology, typed time, world residual rules and frozen source input are unchanged. No shared X6 CLAIM, formal Result/Review or mathematical admission is claimed.

Useful next candidates: enumerate other *opposite-parity* multiplier pairs `(k,ell)`, such as `(4,1)`, with the necessary source bit `j=0`, and compute genuine overlap against `C908`; then apply full named two-flip carry conditions on the remaining complement. The mother question remains `B_fix,odd(32) in {19,20}`.

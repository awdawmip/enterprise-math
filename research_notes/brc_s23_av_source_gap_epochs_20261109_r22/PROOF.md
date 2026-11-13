# S23/AV: source-labelled gap substitution through the 656th cut (r22)

Date: 2026-11-09. Author-side mathematical derivation, independent review pending.
Frozen scientific input: \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Predecessor: r21 \`7fe79d88a45054c15f83dc3caac1c9bae4bb095f\`. The observer is an **auxiliary scalar circle model**, not a native X6 dynamical theorem or Foundation admission.

## Statement

For irrational theta let P_n = {fractional parts {j*theta}: 0<=j<n}, with 128 historical cuts. Define
\`R(128,n-128) = 1 - sum_{historical arcs I} max_{n-cut subarcs J inside I} length(J)\`.
Assume the previously certified S23 parameter enclosure
\`262204504569236716045286/10^24 < theta < 262204504569236716045287/10^24\`.
Set
\`d=16-61*theta\`,
\`a=164*theta-43\`,
\`b=d-a=59-225*theta\`,
\`c=b-a=102-389*theta\`,
\`e=c-a=145-553*theta\`.
The endpoint-certified strict inequalities are \`0<e<a<c<b<d\`.

**Theorem (all integer cuts 225<=n<=656).**
Writing \`B=1-128*d=-2047+7808*theta\`,

\`\`\`text
225<=n<=292 : R = B+(n-225)*a
292<=n<=328 : R = B+67*a
328<=n<=456 : R = B+67*a+(n-328)*a
456<=n<=492 : R = B+195*a
492<=n<=553 : R = B+195*a+(n-492)*a
553<=n<=620 : R = B+256*a+(n-553)*e
620<=n<=656 : R = B+256*a+67*e
\`\`\`

In particular,
\`R(128,656-128)=-3340+12741*theta≈0.747592716645\`.
The positive increments are \`a\` for 226–292, 329–456 and 493–553; \`e\` for 554–620. Three exactly flat epochs are 293–328, 457–492 and 621–656 (each 36 cuts). The 329–456 epoch has 128 consecutive positive increments.

## Historical-arc adjacency without sorting

For each historical source index k=0,...,127, its clockwise historical successor and its full historical-arc length are

\`\`\`text
A: 0<=k<=24   : succ=k+103, arc=a+d=103*theta-27         (25 arcs)
B: 25<=k<=60  : succ=k+42,  arc=a+2*d=42*theta-11         (36 arcs)
C: 61<=k<=127 : succ=k-61,  arc=d=16-61*theta             (67 arcs)
\`\`\`

The enclosure makes each clockwise length strictly between 0 and 1. Each historical index appears once as an outgoing source and once as an incoming target. Their total length is
\`25(a+d)+36(a+2*d)+67*d=1\`.
Every closed cycle of positive clockwise directed edges has a positive integer winding number. Hence the total winding 1 forces a single nonoverlapping clockwise cycle, giving the exact historical neighbor order (not merely a suggested partition).

At n=225, exhaustive source-labelled subdivisions are:

\`\`\`text
A / k=0..24   : (k, k+164, k+103)                lengths (a,d)
B / k=25..60  : (k, k+164, k+103, k+42)         lengths (a,d,d)
C / k=61..127 : (k, k-61)                       lengths (d)
\`\`\`

The interior indices above are exactly 128..224, once each (A:164..188, B:128..163 and 189..224), proving this is the complete P_225 refinement. The maximum subarc of each historical arc has length d, so \`R_225=1-128*d=B\`.

## Exact insertion substitution table

Every incoming source index t=225..655 belongs to precisely one row below. In every row k increases by one each step over the stated owner interval, t=k+shift. The two labels in parentheses are the consecutive old cut indices enclosing the incoming phase. All labels, left/right order and split lengths are literal, not just multisets.

| t range | k historical owner | shift | old source gap (left,right) | split | risk increment |
|---|---|---:|---|---|---|
| 225..291 | 61..127 | 164 | (k,k-61) | d -> (a,b) | a |
| 292..327 | 25..60 | 267 | (k+103,k+42) | d -> (a,b) | 0 |
| 328..352 | 0..24 | 328 | (k+164,k+103) | d -> (a,b) | a |
| 353..388 | 25..60 | 328 | (k+164,k+103) | d -> (a,b) | a |
| 389..455 | 61..127 | 328 | (k+164,k-61) | b -> (a,c) | a |
| 456..491 | 25..60 | 431 | (k+267,k+42) | b -> (a,c) | 0 |
| 492..516 | 0..24 | 492 | (k+328,k+103) | b -> (a,c) | a |
| 517..552 | 25..60 | 492 | (k+328,k+103) | b -> (a,c) | a |
| 553..619 | 61..127 | 492 | (k+328,k-61) | c -> (a,e) | e |
| 620..655 | 25..60 | 595 | (k+431,k+42) | c -> (a,e) | 0 |

**Proof of completeness.** Begin with the three exhaustive source lists at n=225. Every proposed insertion is into an old adjacent source pair: the clockwise phase difference from left endpoint to the inserted point is always \`a=164*theta-43\`, while the remainder is respectively b, c or e, all strictly positive. Thus inserting t replaces precisely the named gap and creates no point in another gap. Each row acts on a distinct set of owners until the next row, and each subsequent named source pair is present in the lists obtained from the previous rows. By induction, all listed source pairs are adjacent at their stated insertion time, and all 431 successive integers are exhausted. The exact source lists evolve as follows (numbers designate successive clockwise lengths):

\`\`\`text
A: (a,d) -> (a,a,b) -> (a,a,a,c)
B: (a,d,d) -> (a,d,a,b) -> (a,a,b,a,b)
   -> (a,a,b,a,a,c) -> (a,a,a,c,a,a,c) -> (a,a,a,c,a,a,a,e)
C: (d) -> (a,b) -> (a,a,c) -> (a,a,a,e)
\`\`\`

For a historical arc whose current maximum gap length D occurs at least twice, splitting only one D-gap preserves the maximum D and gives zero risk increment. If D is unique and split into x and D-x, the increment is \`D-max(other_gap_lengths,x,D-x)\`. These follow immediately from the definition of R. The B family has two tied d gaps before row 2, two tied b gaps before row 6, and two tied c gaps before row 10. The strict chain \`0<e<a<c<b<d\` gives all other positive changes in the table: for C's b->(a,c), b-c=a; for C's c->(a,e), c-a=e. Summing exact row lengths proves the theorem.

This upgrades the previously finite-only 293–328 plateau to a source-labelled algebraic derivation and extends exact non-enumerative endpoint generation through n=656.

## Evidence and precise limits

The attached \`VERIFY_R22.py\` uses Python standard-library exact Fraction. It checks the 128 historical source/successor arcs, exhaustive n=225 labelled cut inventory, all 431 insertions and local max changes at **both** rational interval endpoints. At stage boundaries it independently sorts the entire phase circle and recomputes risk; it checks fixed floors and full P_656 ordering at both endpoints. With the phase floors fixed, relevant gap differences and comparisons are affine in theta; endpoint signs certify the entire open parameter interval. Program assertions do not use floating point. The S23 logarithmic definition and original parameter enclosure are reused from the frozen prior certificate, rather than derived anew here.

BRC consideration: the adequate typed carrier here is (historical arc owner, ordered source labels, exact gap lengths, tied-max multiplicity, future insertion). Taking a scalar total alone would lose the causes of the flat epochs. This is source-labelled observer preservation, not a claimed native X6 / BRC dynamics theorem; project theorem admission, real shared Task CLAIM and independent review remain separate.

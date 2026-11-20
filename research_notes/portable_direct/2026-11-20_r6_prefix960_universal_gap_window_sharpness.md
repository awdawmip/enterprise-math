# PREFIX-960 — Universal finite quotient-gap window for named XOR collisions

Date: 2026-11-20. Frozen scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Extension of PREFIX-955–959B. Historical R6 provenance: EM-DIRECT-58C410, original SID MCP-31edc522830749ad8775ca012e02ef30; these identifiers alone are not present execution authorization. Status: author proof and exact finite original-equation checks; NOT_REVIEWED. Subject is an auxiliary named-XOR observer, not a theorem of intrinsic physical X6 or BRC evolution.

## Exact observation model

Let p >= 3, H=2^(p-1), and Q_p={H+1,H+3,...,2H-1}. Let k >= 1 and d >= 2 be integers; the usual project family takes k odd, d even and k+d < H. For ordered (a,b) in Q_p^2, a joint **named** source history consists of positions 0<=i,j,I,J<p and positive integers t,T such that

    ((k*a) XOR 2^j) - 2^i = t*b
    (((k+d)*a) XOR 2^J) - 2^I = T*b.

Actual source signs depend on the j-th bit of k*a and J-th bit of (k+d)*a:
s=1-2 bit_j(k*a), S=1-2 bit_J((k+d)*a). Define signed residuals c=2^i-s*2^j and C=2^I-S*2^J, the quotient gap m=T-t, and Delta=C-c. Retain the distinct named indices even when their numerical residuals agree. No raw signed residual is presumed realizable unless its bit predicate is checked.

## Theorem 960.1 — Gap-window bound independent of core, bitwidth and input pair

For every such valid named joint history, the **integer quotient gap** obeys

    floor((d-1)/2) <= m <= 2*d+2.

For adjacent cores d=2 this specializes to the seven-value window

    0 <= T-t <= 6.

The upper and lower endpoints are both attainable with lawful named XOR sources, hence no proper universal subinterval of {0,...,6} can be substituted for all adjacent-core problems.

### Proof

Each numerical signed source residual satisfies

    1-H <= 2^i-s*2^j <= 2H,

as the minimum is 1-H (i=0, j=p-1, s=+1), and maximum is 2H (i=j=p-1, s=-1). Therefore

    -(3H-1) <= Delta <= 3H-1.

Subtracting the two **original** named equations gives the exact identity

    Delta = d*a - m*b.                                     (1)

Because H+1<=a,b<=2H-1, equation (1) implies

    m*b <= d*(2H-1)+(3H-1)=(2d+3)*H-d-1
        < (2d+3)*(H+1) <= (2d+3)*b.

Thus m<2d+3 and m<=2d+2.

For d=2, equation (1) similarly gives
    m*b >= 2*(H+1)-(3H-1)=3-H > -(H+1) >= -b.
Therefore m>-1 and, being integer, m>=0.

For d>=3, set q=floor((d-3)/2)>=0. If m<=q then
    m*b <= q*(2H-1) <= ((d-3)/2)*(2H-1)
         < (d-3)*H+d+1 <= d*a-Delta=m*b,
a contradiction. Consequently m>=q+1=floor((d-1)/2). This covers all d>=2. No probability, float approximation, or unproved native transfer enters. QED.

For even spacing d=2r>=2, this reads r-1<=m<=4r+2. In particular, the previously observed Q19 window 0..6 is not a special property of cores 21,23 or of 19-bit truncation; it follows for every adjacent-core named-XOR observer satisfying the same source-position and modulus-range hypotheses.

## Exact original-equation endpoint certificates

**Lower endpoint m=0**: p=4, H=8, k=1, d=2, a=9, b=11, t=T=1; take (i,j)=(1,2), (I,J)=(3,3). Direct check:

    (9 XOR 4)-2 = 11 = 1*11
    (27 XOR 8)-8 = 11 = 1*11.

**Upper endpoint m=6**: p=6, H=32, k=5, d=2, a=59, b=33, t=7, T=13; take (i,j)=(5,5), (I,J)=(4,5). Direct check:

    (295 XOR 32)-32 = 231 = 7*33
    (413 XOR 32)-16 = 429 = 13*33.

Both satisfy k+d<H, odd a,b in Q_p and a!=b. They are full source-named witnesses, not just solutions of the residual linear identity. The second example also rules out any general claim that gap 6 is impossible, despite its absence in the specific Q19 21/23 census.

## Finite independent verification

The accompanying Python verifier generates quotients **directly from the two original XOR equations** for every considered odd a,b and named indices, without reading any previously generated pair-ID list.

- Full spacing sweep: p=4,5,6; all positive odd k and positive even d satisfying k+d<H; 154 (p,k,d) triples and 21,818 named joint witnesses. Every gap satisfies Theorem 960.1.
- Expanded adjacent-core sweep: p=4,5,6,7; all 56 odd-k adjacent-core triples; 12,830 named witnesses. The counts for m=0..6 are 59, 1632, 7352, 2794, 915, 72 and 6, with no others.
- The two explicit extremizers are separately asserted against the unmodified integer XOR equations.
- Only exact integer arithmetic is used. Universal validity comes from the displayed proof; the finite enumeration supports regression and checks source-sign interpretations.

Run: python3 PREFIX960_R6_GAP_WINDOW_VERIFIER.py. This writes PREFIX960_R6_EXACT_RESULTS.json with the full per-triple observed ranges, domain, witness counts and endpoint parameters. The source pin is metadata; it is not silently repinned by current control revisions.

## Scientific implications and continuation

PREFIX-959B previously enumerated 0<=m<=6 for Q19 cores 21/23 and reported 6,203 distinct off-diagonal pairs and 8,649 named histories. The new theorem **discharges the universal gap-exhaustiveness obligation** for adjacent-core reconstruction, including larger p and other k, provided every valid sign/source predicate and the separate N=0 resonance branch are retained. It does not by itself prove the previously published Q19 counts, which have their own computation certificates.

The general d>=2 window makes quotient-gap enumeration independent of k. It can be used in exact divisor-fiber weighted sums and prevents missing negative or distant quotient-gap histories when changing core spacing. A future improvement is to characterize attainable endpoint gaps for individual k and d (particularly gap 6), and to derive source-name-weighted arithmetic sums over cached odd divisors without losing observer-distinguishable multiplicity. Another open item is a typed native X6/BRC observation-and-operation preservation map; neither the finite XOR model nor this theorem automatically supplies that map.

Control boundary: this independent note creates no formal TASK CLAIM, RESULT, REVIEW or Working Truth promotion. Any prior session/Activity identifiers are provenance until actual present authority is verified. Existing other-owner research remains untouched.

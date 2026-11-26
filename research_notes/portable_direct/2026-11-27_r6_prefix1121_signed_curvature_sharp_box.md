# PREFIX-1121 — signed curvature and the sharp dyadic information boundary

2026-11-27. EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. Original registration r6-20261123-2358-session-start-own-v1 read SUCCEEDED. Current LEASED read r6-20261127-0747-leased-read SUCCEEDED, error=null, snapshot 2026-11-26T23:47:34.965017Z, tasks=[], next_cursor=null, source eb1685ecb6a4abcdd2f75f3043403b72446f39cd. Independent directed Stage46 research; no new CLAIM, no shared task state change. Author proof, NOT_REVIEWED.

Parent PREFIX-1120: 0ba2c9da05a07e67ba5450de52ee61d46bf1807e:research_notes/portable_direct/2026-11-27_r6_prefix1120_joint_integer_dual.md (main blob c17c4115f48e93981eeb13ad061d99a8a826b1fa actually read). Frozen P000 V5 at f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint observer/time companions read, ACTIVE worldview and portable protocol read. Preserve native X6/time, signed reversal -5 with phase cover 5q, chart O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives and inherited carrier identities as in parent. This is auxiliary exact arithmetic on the inherited signed BRC observation boundary; no new native propagation or reference physics calculation. 8400/8800 anchor process exits unconfirmed; independent review pending.

Input: 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json, read blob e03d50ec3c79588577e8aaef7e194adf7562f2c8, local bytes SHA256 367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9. Same exact coefficient box R,C,T, grid 10^85; E=400000. Inherited finite sweep rules out triple windows of fixed doubling grid before M=16225927682921336339157801028812800000000; inherited PREFIX-1120 eliminates q<=Q0=18*10^50 for all triple windows L>=M. Keep both premises explicitly. No new BRC anchor or CT evaluation.

## 1. Sharper curvature with signed three-point residuals

Define f(m)=rho*m+c+d/m, d>0, e_m=f(m)-j_m, true near hit |e_m|<=E/m^2. For a<b<z in [L,2L), assume the three integer observations are collinear (PREFIX-1118's determinant condition, verified for this box). Set w=(z-b)/(z-a), 1-w=(b-a)/(z-a). Exact cancellation of the affine terms and of collinear integers yields
w*e_a+(1-w)*e_z-e_b = d*(b-a)*(z-b)/(a*b*z).
Consequently
d*(b-a)*(z-b) <= E*S,
S = w*b*z/a + a*z/b + (1-w)*a*b/z.
This pays the actual position-dependent error instead of using E/L^2 at all three points.

Write A=a/z, B=b/z, so 1/2<A<B<1. Then
S/z = B*(A^2+A+1-B*(A+1))/A + A/B.
The exact factorization is
A*B*(2-S/z) = (B-A)*(A*B^2+A+B^2-B).
The second factor is positive because A>1/2 and B^2-B>=-1/4. Thus S<2z<4L. If the primitive line is q*j-p*m=h, gcd(p,q)=1, q>0, all spacings are multiples of q, hence
q^2 < 4*E*L/d.
This improves the previous sufficient curvature constraint q^2<=16*E*L/d fourfold. The argument works for all collinear triples in the dyadic window, not just equally spaced triples. The constant 4 is asymptotically sharp for general parameter triples: choose a,b=a+q,z=a+2q near 2L with q^2 approximately (4E/d)L from below, put the two endpoints on the affine secant and shift c by half the middle deficit; then the three residuals have alternating signs and magnitude d*q^2/(2*a*b*z). Explicit exact construction below establishes sharpness of the first allowed dyadic window for this particular box.

## 2. Signed integer-coordinate enumeration (lossless)

From PREFIX-1120 for a pair on the same line, q>=qmin=Q0+1>16E/d_l implies 0<rho-p/q<=K/L^2 and 0<h/q-c<=H/L, where K=9*d_u/8 and H=2*d_u+4E/qmin. Proof of signs: rho-p/q=d/(ab)+(e_b-e_a)/(b-a), and c-h/q=-d*(1/a+1/b)+(b*e_a-a*e_b)/(b-a). The error is bounded by 2E/(q L^2) and 4E/(q L), respectively; the positive main terms dominate. With J=4E/d_l, section 1 implies L>=q^2/J. Therefore every triple line with qmin<=q<=Q=3*10^51 obeys
rho_l*q-up <= p <= rho_u*q,
c_l*q <= h <= c_u*q+uh,
up=K*J^2/qmin^3, uh=H*J/qmin.
Keep the actual signs; this is an enclosing polytope, not an equality test of physical parameters.

Reuse PREFIX-1120's integer matrix V, det=+1:
(13241695572016246280452795405,-614903515325433031059117378,-586453816401334287434546)
(1182616791650392258028253444,-74796824988556406807726418,4246778208283374384362279)
(-7752265403315380654172299023,382363756442351370763912993,-4494886358260478563501531)
The coordinate n=V(q,p,h) is an invertible integer coordinate, with inverse W formed by cofactors, so no intercept or sign information is discarded. It is an arithmetic observer, not a new native spatial direction.

For each row (A,B,C), evaluate q*(A+B*r+C*s)+B*dp+C*dh at every corner of q in [qmin,Q], r in R, s in C, dp in [-up,0], dh in [0,uh]. This multi-affine expression has extrema at corners (successive one-variable linear extrema). Taking integer ceil/floor gives all three coordinates in {-1,0}. Thus only eight transformed integer vectors require consideration. The verifier enumerates four n1,n2 pairs, bounds n3 by every transformed linear inequality using exact rational floor/ceil, and tests gcd(p,q)=1. Exactly one primitive triple survives:
q*=2655223732550132521125580881859760580045275386620690
p*=56928094326764720801423472551026152845166243635604419
h*=263241563783130075215288446665553099252835723038759458
It is the image W(0,0,-1). Both p*/q* and h*/q* lie strictly inside the frozen parameter intervals.

For q>Q, q>q* trivially, and q<qmin is excluded by the parent. Hence q>=q* for all triple windows on the fixed grid (including the inherited initial sweep). This raises the denominator lower bound by about 1.475 relative to Q0, without new anchor information. Combining the two improvements yields L>=q*^2/J, approximately 4.27016541134913e97. First allowable fixed dyadic start:
L*=50925899408362152156711142210234454026286709841648406265903511233859532494083417654584934400000000
(approximately 5.092589940836215e97), exactly eight times PREFIX-1120's earlier dyadic lower bound. This is an exclusion theorem about potential triple near hits, not an expansion of the already certified integer endpoint formula.

## 3. Sharp information boundary for the frozen coefficient box

The preceding lower bound on the first possible dyadic window is attained by an alternative parameter tuple inside the same axis-aligned box. Use q*,p*,h*, d0=(d_l+d_u)/2. Let U=2L*-2q*-1 and r0=(-h* inverse(p* mod q*)) mod q*. Set
a=U-((U-r0) mod q*), b=a+q*, z=a+2q*.
This keeps the three integer observations j_m=(p*m+h*)/q* in the same line and same dyadic window. Set
half=d0*q*^2/(2*a*b*z),
rho'=p*/q*+d0/(a*z),
c'=h*/q*-d0*(1/a+1/z)+half.
Direct substitution gives e_a=half, e_b=-half, e_z=half. The verifier checks exactly rho' in interior R, c' in interior C, d0 in T and half*z^2/E<1 (display 0.8385056446637758). Thus all three are true near hits for this alternative tuple. This construction has the same interval information but is not asserted to be the BRC-generated tuple. The universal no-triple prefix for the axis-aligned box, with inherited uniform premises, is therefore sharp on the fixed doubling grid: a proof from only the box and the same near-hit definition cannot exclude its first allowed window. Additional BRC parameter correlation or sharper input is needed to decide that window for the actual spectrum. No statement about actual occurrence is made.

## 4. Verification, reproducibility, and next question

Actual local run used Python Fraction and arbitrary integers. Output:
ranges [(-1, 0), (-1, 0), (-1, 0)]
loops 4 primitive 1
interior True True
L lower 4.27016541134913e+97
dyadic 5.092589940836215e+97
max paid ratio 0.8385056446637758
All assertions completed normally. Code: fbbdf5676957956366466b6e32d34a8589464c5b:research_notes/portable_direct/2026-11-27_r6_prefix1121_signed_curvature_verify.py, immutable readback equals actual local script blob 6a71b538096dd766d93b660efd8b85f233bf85cf, SHA256 de4559819faed33c627019bb4a924857c3c453db066aa82287ffb7e1a8c9d920. Run with the pinned input named root_8800_result.json. It writes complete exact output prefix1121_result.json, SHA256 65e4ef2d6d55da4da761e77b6b3b02fa52912810107e9cf2804ede86b346e2fe. The exploratory run with Q=10^53 visited 3380 n1,n2 pairs and yielded 20202 primitive vectors; the final smaller Q is sufficient, giving a unique witness with the same minimal q. No runtime efficiency claim across unequal coverage.

Next: use actual signed BRC joint parameter constraints beyond an axis-aligned box; in particular test the affine lattice vector (q*,p*,h*) against correlation in the underlying root/jet certificate. Alternatively refine rho-only by the previously derived factor >=24209 to close 122 pending endpoint candidates. The conditional continuous endpoint range still ends at 4265326180744162387203315935318273935179 exclusive; exact zero, isolated hits, actual triple existence, remaining spectrum, eventual all-scale separation and mother B_fix,odd(32) open. Independent mathematical review, inherited anchor exits and Activity observation audit pending.

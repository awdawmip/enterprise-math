# Addendum r22b: synchronization of all historical maxima and 389-step plateau

Date: 2026-11-09. Author-side S23/AV auxiliary scalar-circle theorem; independent review pending. Frozen source \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Extends \`PROOF.md\` in this same research directory; not native X6 dynamics or Foundation admission.

## Exact theorem

Write m=128, n=128+L and
\`R(128,n-128)=1-sum_{historical arcs I} max_{subarcs J in P_n refinement of I}|J|\`.
Use the previously certified strict S23 interval
\`262204504569236716045286/10^24 < theta < 262204504569236716045287/10^24\`.
Define \`d=16-61*theta\`, \`a=164*theta-43\`, \`b=d-a\`, \`c=b-a=102-389*theta\`, \`e=c-a=145-553*theta\`, and \`f=a-e=717*theta-188\`. Exact comparisons certify \`0<f<e<a<c<b<d\`.

**Result.** All 61 inserts with new total cut count \`657<=n<=717\` increase risk by e. At n=717, the **553 a-length maximum gaps** have clockwise source indices precisely \`0,...,552\`, all with right index equal to the source index plus 164. Consequently all 389 new cuts with \`718<=n<=1106\` yield zero risk increment; the insert at n=1107 increases risk by \`f=717*theta-188>0\`.

Explicit risk formula:
\`\`\`
656<=n<=717: R(128,n-128)=R(128,656-128)+(n-656)*e
717<=n<=1106: R(128,n-128)=1-128*a=5505-20992*theta
n=1107       : R(128,979)=1-128*a+f=5317-20275*theta
\`\`\`

## Exact source-labelled proof

At n=656, r22 supplies these complete historical owner lists and gap lengths:
\`\`\`
A k=0..24   : (k,k+164,k+328,k+492,k+103)                      | (a,a,a,c)
B k=25..60  : (k,k+164,k+328,k+492,k+103,k+267,k+431,k+595,k+42) | (a,a,a,c,a,a,a,e)
C k=61..127 : (k,k+164,k+328,k+492,k-61)                        | (a,a,a,e)
\`\`\`
At each t=656..716, k=t−656 runs through A (25 owners) then B (36 owners). In each owner the unique maximum c-gap \`(k+492,k+103)\` contains the new phase labelled \`t=k+656\`. The two clockwise pieces are a and e, where a+e=c and both positive; the owner's new maximum is a, so its contribution to risk is exactly c−a=e. The remaining C-owners already have maximum a. Thus at n=717 all 128 historical owners have maximum exactly a, giving \`R=1−128a\`.

The n=717 source lists and gaps are:
\`\`\`
A k=0..24  : (k,k+164,k+328,k+492,k+656,k+103)                       | (a,a,a,a,e)
B k=25..60 : (k,k+164,k+328,k+492,k+656,k+103,k+267,k+431,k+595,k+42) | (a,a,a,a,e,a,a,a,e)
C k=61..127: (k,k+164,k+328,k+492,k-61)                              | (a,a,a,e)
\`\`\`

The left source labels of all a-gaps form exactly these disjoint integer blocks:
\`\`\`
A: 0..24, 164..188, 328..352, 492..516                (4/owner)
B: 25..60, 128..163, 189..224, 292..327, 353..388,
   456..491, 517..552                                 (7/owner)
C: 61..127, 225..291, 389..455                       (3/owner)
\`\`\`
Their union is the entire interval \`0..552\` (553 distinct a-gaps), and each corresponding right label is left+164. For each t=717..1105 take j=t−717, which enumerates 0..388 **once each**. The incoming phase \`{t*theta}\` splits precisely the pre-existing unique gap \`(j,j+164)\` of length a into pieces f and e (since f+e=a, both positive). No earlier insertions touch that same gap; the partition evolution follows by induction.

Crucially, throughout this run each historical owner has an **untouched a-gap with left label j>=389**, namely A uses 492..516, B uses 456..491 and 517..552, and C uses 389..455. Thus every owner maximum remains a throughout the 389 insertions, so \`R=1−128a\` for all n=717..1106, not just at sampled endpoints.

At t=1106 the next left label is j=389. The owner C at k=61 has exactly three original a-gaps beginning at j=61,225,389. The first two were split already; j=389 is its final a-maximum. The new cut splits it into (f,e), with \`0<f<e<a\`, leaving maximum e and giving ΔR=a−e=f. No other owner's maximum changes, giving the stated n=1107 formula. QED.

## Exact computational cross-check, provenance and remaining work

\`VERIFY_R22_ADDENDUM.py\` carries full source labels; it reconstructs the n=656 owner arrays and directly compares to sorted-circle risk at n=656,717,718,800,1000,1106,1107. Using standard-library \`fractions.Fraction\` at **both rational interval endpoints**, it checks the 61 + 389 + 1 subsequent insertions, all 553 original maximum-gap starting labels and every owner's preserved maximum witness; phase floors and full P_1107 order are stable at both endpoints. The program emits \`PASS_S23_SOURCE_GAP_SYNCHRONIZE_PLATEAU_1107\`. Relevant sign comparisons are affine with fixed floors, so endpoint checks certify every theta inside the stated open interval. The interval enclosure of the original S23 theta is inherited from the frozen earlier certificate.

The result is an author-side exact auxiliary-observer derivation. Independent mathematical review, shared formal CLAIM, and canonical Research-Activity scientific checkpoint binding remain pending. Next: use remaining 164 a-gap labels to derive positive epoch endpoints beyond 1107 with a source-labelled gap state, then analyze precise bit complexity and native-X6 observer bridge independently.

# Addendum r22c: complete synchronized a-gap cascade through n=1270

Date: 2026-11-09. Exact author-side S23/AV scalar-circle result; independent review and shared-Task CLAiM pending. Frozen science unchanged at \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Depends on earlier r22 proof and r22b source-labelled n=717 partition; not a native X6/BRC dynamics or Foundation theorem.

## The source-labelled deterministic substitution law

Let m=128 and n=m+L, with the previously strictly certified S23 interval
\`262204504569236716045286/10^24 < theta < 262204504569236716045287/10^24\`.
Define \`a=164*theta-43\`, \`e=145-553*theta\`, \`f=a-e=717*theta-188\`. On the entire enclosure, \`0<f<e<a\`.

At n=717, as established in r22b, every one of the 128 historical owners has maximum gap a, and the **553 a-length gaps** have clockwise starting source labels exactly \`j=0,...,552\`, each having right source label \`j+164\`. These labels uniquely identify their containing historical owners. The original number of a-gaps in one owner is 4 (A: k=0..24), 7 (B: k=25..60), and 3 (C: k=61..127). The complete left-label intervals are:

\`\`\`
A: 0..24, 164..188, 328..352, 492..516
B: 25..60, 128..163, 189..224, 292..327, 353..388, 456..491, 517..552
C: 61..127, 225..291, 389..455
\`\`\`

For **every integer** t=717,...,1269 define j=t−717; these are precisely the 553 starts, once each. The new cut phase \`{t*theta}\` lies strictly within the original length-a gap \`(j,j+164)\`, splitting it into ordered lengths \`(f,e)\` because \`f+e=a\` and \`0<f<e<a\`. Previous insertions affect other a-gaps, so adjacency and this exact split persist by induction. Other old gaps were already e and are unchanged by this insertion. Thus, for the containing historical owner, its maximum is a as long as an uncut a-gap remains, then becomes e exactly when its last a-gap is split. The risk increment is 0 until that last split, and exactly \`a−e=f\` on the last split.

Counting left labels by owner gives the entire exact schedule:

| New total cut count n | Split left labels j | Number of cuts | Risk increment |
|---|---|---:|---|
| 718..1106 | 0..388 | 389 | 0 |
| 1107..1173 | 389..455 | 67 | f (last a-gap of each C owner) |
| 1174..1209 | 456..491 | 36 | 0 (B owners retain another a-gap) |
| 1210..1234 | 492..516 | 25 | f (last a-gap of each A owner) |
| 1235..1270 | 517..552 | 36 | f (last a-gap of each B owner) |

Every historical owner loses its maximum a **once**, exactly 128 positive increments of f, whereas the remaining 425 insertions leave the owner maxima unchanged. At n=1270 every owner has maximum exactly e, whence

\`\`\`
R(128,1270-128)=1−128*e
              =−18559+70784*theta
              ≈0.883651428851709.
\`\`\`

This recovers and *analytically explains* the earlier independently finite-certified r11 endpoint L=1142 without repeating 1142 full circular sorts. The 389-step plateau, next 67 positive steps, next 36-step plateau and final 61 positive steps follow from one non-enumerating source-label set and a maximum-gap multiplicity rule.

## Verified coverage / unresolved units

\`VERIFY_R22_1270.py\` is the self-contained Python \`fractions.Fraction\` verifier. It reconstructs n=717 source-labelled owner lists and their initial gap sizes at each of the two rational endpoints; proves the 553 left labels form 0..552; applies all 553 insertions; checks each owner maximum and the exact risk increment; and independently builds the full sorted circle and owner maxima at n=717,718,800,1106,1107,1173,1209,1234,1270. The phase floors and the full P_1270 circle order agree at the two endpoints. All asserted comparisons are affine with fixed phase floors, establishing the stated interval result. Actual local execution emits \`PASS_S23_SOURCE_LABEL_SYNC_717_1270\`; the local executable SHA-256 is \`858e70c40e553cadffa5531470d14209541358516b204653e71b0c1d4fd0a478\`.

The original S23 logarithmic theta interval is reused, not rederived. This is an author proof and exact computational certificate, not an independently accepted shared Result. Next compute source-labelled insertion after n=1270, starting from the e-gap inventory and determining the next return shift and new max-tie transitions; derive bit/precision cost. Preserve prior author-side results and formal owner protections.

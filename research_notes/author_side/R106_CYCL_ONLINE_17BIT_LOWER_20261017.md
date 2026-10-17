# R106 | 17-bit online lower bound for the six-axis CYCL ordered-source observer
Status: AUTHOR_SIDE_UNREVIEWED / NOT_ADMITTED. Date: 2026-10-17.

Sources: GLOBAL_KNOWLEDGE_V1 main@e2c99e7eeea5f67b9014b350fff8f8b35fe38d4c; Enterprise Math main@341ea3fb3b06d32b16208d523dd5b7fdf6037f39. P000 ACTIVE_LOCKED; this is a purely formal signed six-axis path theorem, not a physical BRC or heartbeat claim. R105's 31-bit upper construction is a separately unreviewed predecessor.

## Statement
Let CYCL be the cyclically freely reduced length-22 signed-native-X6 words with six balanced axis pairs whose positive counts, after sorting, are (4,3,1,1,1,1). Let h be the unique axis with 4 positives and 4 negatives; l the unique axis with 3 of each. For scattered ordered-subsequence counts N, define Z=N(h,h,h,l)-N(h,h,h,-l)-2N(-h,-h,-h,l)+2N(-h,-h,-h,-l).
A deterministic exact single-pass stream observer with no external history side channel, required to output (h,l,Z) on every such CYCL word, has >=68,067 pairwise distinct reachable internal states after 16 events, even when all prefixes have the same signed direction counts. Hence at least ceil(log2 68067)=17 bits are necessary.

## Formal source identity
For h=1 and prefix u, define f(u)=C(count(+1),3)-2C(count(-1),3). Define R_j(u)=sum over events +/-j of sign(event)*f(before event). Partition every scattered four-letter subsequence by its last event to get exactly R_j=N(1,1,1,j)-N(1,1,1,-j)-2N(-1,-1,-1,j)+2N(-1,-1,-1,-j).

## Explicit fooling set
Use high-axis source (+1,+1,+1,+1,-1,-1,-1,-1). Its f values just after each event are (0,0,1,4,4,4,2,-4), with level set S={-4,0,1,2,4}. Let D=S-S={-8,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,8}, and T=(4-S) union (S-4)={-8,-4,-3,-2,0,2,3,4,8}. Insert once each +2,-2,+5,-5,+6,-6,+3,+4 into slots after high events, preserving their signed count vector independent of the construction. The slot for level 0 is after high step 1; for level 1 after step 3; for 4 after step 4; for 2 after step 7; for -4 after step 8. Two additional slots of equal f value exist after high step 2 (0) and step 5 (4).

Choose (d2,d5,d6) in D^3. For axis j in {2,5,6}, find a,b in S with a-b=dj and place +j at f=a, -j at f=b. If dj is in T, choose a representation with a=4 or b=4, placing its 4-stage letter after high step 4 (a bridge across high sign change). If a=b=4, insert +j after step 4, -j after step 5, separated by -1. Distinct source levels have separating high events. Choose s3,s4 in S and place +3 at f=s3 and +4 at f=s4. Break same-slot ordering by increasing absolute axis label.

Retain only these disjoint parameter subsets:
A: s3 in S\{-4}, s4 in S; at least one of d2,d5,d6 in T or s3=4 or s4=4. Count |A|=15^3*4*5-6^3*3*4=64,908.
B: s3=s4=-4, with at least one of d2,d5,d6 in T. Count |B|=15^3-6^3=3,159.
Every prefix has 16 events, first event +1, identical signed occupancies, no adjacent inverse pair, and a marker after fourth +1 preventing +1,-1 cancellation. No prefix ends with +3: in A, +3 is never placed in the last slot; in B, +4 follows it in that last slot. Its R-vector is (d2,s3,s4,d5,d6). The union has 68,067 distinct vectors.

## Five universal *CYCL-legal* suffixes
Use the fixed six-event suffixes s_2=(-3,2,2,-4,-2,-2), s_3=(3,3,-4,-3,-3,-3), s_4=(4,4,-3,-4,-4,-4), s_5=(-3,5,5,-4,-5,-5), s_6=(-3,6,6,-4,-6,-6). For every constructed prefix p and each j=2,...,6, p+s_j is 22 events, balanced with high axis 1, secondary axis j, low others 1/1, and is cyclically freely reduced: within suffix each inverse switch is separated; first suffix event is safe since p never ends with +3 or -3/-4; last suffix event is safe against p's initial +1.

The high source has completed 4 positives and 4 negatives before the suffix, hence f=-4 thereafter. For j=2,5,6 the suffix net signed j-count is zero, contributing zero. For j=3,4 it is -1, contributing +4. Consequently (Z(p+s_2),...,Z(p+s_6))=(d2,s3+4,s4+4,d5,d6). This vector is injective on all 68,067 prefixes. Distinct prefixes are separated by at least one *common legal* suffix s_j, so a deterministic exact stream machine cannot merge their internal states after step 16. Since 2^16=65,536 <68,067, the 17-bit claim follows.

## Evidence, limitations and next unit
A local standard-library Python verifier generated all 68,067 prefixes, checked all 340,335 CYCL completions and all terminal source signatures with two independent exact integer subsequence-counting algorithms. It returned R106_ONLINE_17BIT_LOWER_BOUND_PASS. The full proof, checker, certificate and SHA-256 manifest are retained in the author-side R106 research archive; remote canonical Result or independent review is not claimed by this note.

The order-insensitive strictly positive BRC branch mass is the same across prefixes for each fixed j, because signed occupancies match. This neither promotes signed Z to a physical phase amplitude nor establishes a native BRC event-acquisition interface. Next: improve the 17-bit online lower bound or compress the author-side 31-bit upper construction while preserving common legal CYCL suffix distinguishability.
# EC49FBN — H9 F/G spine terminal-prefix inheritance (exact finite theorem)
Date: 2026-11-05 · TASK_RESEARCH · Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Immediate source: EC49FBM immutable commit `a891301880c100f7b803f9e5328064c0aac97e18`, its 124 pairs and nine-state DFA. Preserve six signed native axes, full positive-BRC keys and rank clauses 18/20/33/40.

## Theorem: unique earlier horizon and exact inheritance coefficient
For a legal horizon-h complete operation word over a,c,d,e,f,g and complete positive key (x,y,z,0,0,0), frozen model identities are:
```
#a=z-1, #e=z, #(c+d)=x+y-h-1, #f=h+1-y-2z, #g=h+1-x.
```
EC49FBM proves that H9's observer-F/G terminal starts with f/g respectively and has only a,e,f,g afterward. An earlier complete terminal operator-word prefix, therefore, contains no c/d, forcing `x+y=h+1`. Thus a *single fixed complete cache key* K=(x,y,z) can occur as an H9-F/G ancestor at **at most one earlier horizon**, `h=x+y-1`. For any fixed H9 key M=(X,Y,Z) satisfying `X+Y=10`, earlier M-key terminals at h<9 all contain `9-h>0` c/d operations and cannot be complete ancestors of the H9 F/G terminal spine.

For an eligible earlier key L=(x,y,z) and horizon h<9, write the four no-c/d counts
`(a,e,f,g)=(z-1,z,h+1-y-2z,h+1-x)`
and later counts
`(A,E,F,G)=(Z-1,Z,X-2Z,Y)`.
If `x+y=h+1`, `X+Y=10` and `D=(A-a,E-e,F-f,G-g)` is componentwise nonnegative, the number of ordered H9 F/G terminal words with an earlier full-terminal F/G prefix is exactly
```
P(h,L;9,M) = (N_F + N_G) * S
N_F=(h-1)!/[a! e! (f-1)! g!]  (0 if f=0)
N_G=(h-1)!/[a! e! f! (g-1)!]  (0 if g=0)
S=(9-h)!/[D_a! D_e! D_f! D_g!].
```
Otherwise P=0. The first F/G letter is fixed, so the early suffix permutations give N_F and N_G. The full cache-key and signed-endpoint equations force D; its S permutations preserve F/G observer state and yield a bijection between counted early/suffix pairs and full words. EC49FBL proves the primitive two-step operation codes are prefix-free, so complete operation-prefix inheritance is precisely the signed native-X6 primitive terminal-prefix inheritance. This argument works within the original exact positive-key model.

## Exact enumeration of the two EC49FBM schedules
The EC49FBM rank-feasible fixed schedule uses L for H4–H6 and M for H7–H9. Its 27 pairs split into **12 with at least one H6→H9 F/G inherited terminal** and **15 without**, totaling **2,000** distinct ordered inherited pairs. The rank-feasible shifted schedule uses L for H4–H5 and M for H6–H9. Its 28 pairs split into **13 with H5→H9 inheritance** and **15 without**, totaling **1,792** such pairs. Only H6 and H5, respectively, can be ancestor horizons in these sets. The fixed-schedule 2,000 agrees with EC49FBM's independent H6→H9 aggregate; the 1,792 shifted count is a new exact enumeration. All 55 individual configurations and two native witness audits appear in `EXACT_REPORT_EC49FBN.json`.

The published `VERIFY_EC49FBN.js` compares each multinomial coefficient with a **separate ordered-word exhaustive enumeration** for all 55×5 early/late horizon checks; every check agrees. A separate Python standard-library prototype directly enumerated the same 55-schedule universe with the same aggregate results.

## Explicit joint native F/G witnesses
Shifted L=(4,2,1), M=(7,3,2): H5 F=`fefgg`, G=`geffg`; H9 F=`fefggaefg`, G=`geffgaefg` (append `aefg`). This schedule has **576** H5→H9 inherited pairs.

Fixed L=(4,3,1), M=(7,3,2): H6 F=`fefggg`, G=`geffgg`; H9 F=`fefgggaef`, G=`geffggaef` (append `aef`). This schedule has **300** H6→H9 inherited pairs.

Each H9 word expands to 22 signed native primitive steps, complete BRC key (7,3,2,0,0,0) and endpoint (2,0,0,0,0,0). The two F/G paths begin with different native primitive axes and together contain exactly **44 distinct signed primitive prefix edges**. Their corresponding H5/H6 F/G earlier terminals are complete prefixes, satisfy every rank clause 18,20,33,40, and contribute **zero additional prefix edges**. Exact native codes: `a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`.

## Reproduction and next question
From this directory run `node VERIFY_EC49FBN.js > EXACT_REPORT_EC49FBN.json`, using the sibling EC49FBM frozen report. This theorem concerns exact aligned complete-terminal inheritance and a constructive two-window subfamily; full nine-window minimization also depends on interior primitive-prefix sharing. Next EC49FBO will exploit 13 shifted and 12 fixed inheritance configurations in complete H4–H9 primitive edge-union optimization, with a targeted complete ≤93-edge construction against the older author-side mother bounds `80<=E*<=94`.

Status: AUTHOR_ANALYTIC_PROOF / EXACT_FINITE_ENUMERATION_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED; native CLAIM, Result and independent Driver review require their own Source authorization.

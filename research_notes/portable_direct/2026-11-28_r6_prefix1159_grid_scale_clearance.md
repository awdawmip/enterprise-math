# PREFIX-1159: representation refinement and five-candidate scale clearance

Date: 2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH, existing own managed session recovered, no formal claim. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / AFFINE_OUTER_MODEL_WITNESSES / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Inputs and scope

Continue PREFIX-1158 at 2107a592c7b4178a0016820f07ae55d610a9ebdd:research_notes/portable_direct/2026-11-28_r6_prefix1158_compact_section_scale.md. Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d; current global normative entry snapshot bc29ffbe6ac51d0fd8a073cce4ab743362ed70dc; project control source a98447c988c1e5b4196ffc2cd6547fee3ca62eee. Existing session registration r6-20261123-2358-session-start-own-v1 succeeded and recovery reports not closed or revoked. Owner read r6-20261128-2146-owner-read SUCCEEDED, fixed snapshot INV-7eaa8f2de74b086fdf7970f5a1494dec as of 2026-11-28T13:47:21.969074Z, total 547, LEASED filtered list empty, source and event issue unchanged at completion. No shared task-state write or new claim. Original Stage46 asymptotic, anchor, affine transfer and primitive-relation reduction conditions remain load-bearing. This is auxiliary parameter-space arithmetic on frozen observations, not a native Heartbeat run.

## 1. Reconstruct the existing observations

The diagnostic for q3 at zero scale identifies high-order moment representation error as the active bottleneck. At fixed centers and shared columns, dividing only the seven high-order independent errors by 10 gives an exact separation ratio >6.38; dividing only the point errors by 10^6 leaves a feasible fiber. This changed-model diagnostic is not itself a new observer certificate.

Keep raw Hraw=10^150, internal J=10^155, anchor order 9600, and all 15 observation rows/12 shared columns. Increase final moment grid G from 10^145 to 10^150; scale the two old point rows exactly. For the frozen rational center M, shared coefficients B_j and analytic radius delta, use m=floor(G*M), C_j=floor(G*B_j), e=ceil(G*delta)+13. For all shared coefficients |z_j|<=1, the rounding error in the center and twelve columns is bounded by 13 grid units by the triangle inequality. The inherited delta equals tail + 1/(2 Hraw) + 10^-180 + 1205/J. All 13 moment rows are reconstructed, first recovering their previous grid values exactly. Rows 10--14 (zero-based) reduce normalized radius by exactly 100000; row 9 by about 903.225806; row 8 by about 1.01154; lower rows and points are effectively unchanged. No new raw moment or anchor run. Preserve all shared generators; no native observer-equivalence claim.

## 2. Exact outer section and integer enumeration

Let U=[C,diag(e)], Z=m+U[-1,1]^27; affine map A(x-r)+B(y-u) for x=rho,y=c. For every normal n, a=n.A, b=n.B, z=n.m+a*r+b*u, S=sum |n.U_j|. Any admissible (x,y) satisfies |ax+by-z|<=S by the support inequality. Intersect the old certified section with eight seven-coordinate cofactor normals from {0,1,9,10,11,12,13,14}, and fifteen inverse-pivot rows (including the scale column when constructing the basis). Every strip pays all 27 columns, even when the pivot was selected with a scale column. Exact clipping and independent pairwise boundary intersections yield the same 16 vertices. Width rho=2.271015206133421e-133, c=1.0892054736500977e-132 (improvement about 11954 and 11955 times). No claim that the selected strips are the entire exact affine projection.

At L0=10^134, the necessary ratio domain is the new P plus [-K/L0^2,0] x [0,H/L0]. It contains all subsequent larger-scale domains. Reuse the maximum-area triangle observation metric, exact rational LLL (12 iterations), and prove integer inverse W for V, VW=I. On the product q0<=q<=Q and the expanded polygon, each new integer coordinate q*(a+b*x+c*y) attains extrema among the two denominator endpoints and polygon-vertex/rectangle-corner sums, because it is affine in each variable separately. Outward integer bounds give a complete box. At Q=10^89 the box is [0,1] x [-4,-1] x [-5,3], 72 points, 13 feasible integers and five primitive gcd(q,p)=1 relations. Direct exhaustive and last-coordinate interval elimination agree; the compact checker independently exhausts the box with the original support inequalities. Thus under the inherited assumptions, for every L>=10^134,

b-a>=q>=68790978239103168622833661446969269397288471328988298766514185061790924582086475186280559.

The prior q3=858356652145570229340015752537013296844119325710283911057636179903360525779249418264558 is excluded. The new lower bound is about 80.14265 times larger.

## 3. Signed scale clearance

The five survivors at L0 have exact full-model witnesses with 29 coefficients and 15 equalities. Their minimum slack exceeds 0.035, individual slacks approximately 0.15730669, 0.81548366, 0.36866541, 0.11527212, 0.03597418. They are all strictly separated in the zero-scale model, ratios >11000. Orient each zero-scale normal so D=n.(A(p/q-r)+B(h/q-u)-m)>0, S=sum |n.U_j|, AA=max(0,-n.A)K/L0^2, BB=max(0,n.B)H/L0. Full support at k=L/L0 is S+AA/k^2+BB/k, decreasing in k. For each candidate the exact test 9(D-S)>3BB+AA passes. Individual sufficient critical roots are about 2.145966, 2.452758, 2.771162, 1.061165, 1.018318, not claimed global optimal thresholds. Thus all five candidates are excluded for every L>=3*10^134 and the old outer search already covers all q<=10^89, proving b-a>=q>10^89 in that regime. Do not apply this stronger bound at the base scale L0.

## 4. Stitched windows

Use inherited triple necessary inequality q^2<4E*L/dlo and close-pair condition gap<=sqrt(L), E=400000. The prior PREFIX-1158 certificate reaches beyond 3*10^134. Stitching at that scale gives first not excluded dyadic window starts L=10^8*2^j:
triple 92137754512244661919959828637408908469651396982823252645903474127090433652152071584133953251407684754430380249774507932123305288816523257630894390904118555753159065600000000
near pair 12076679759428932327172974659162460450934147905332609370803860160785997319654876326675605520568508056132698800098444303679265870815759336424196589604584627339678065046323200000000
Both are 16384 times the previous certified boundaries. These are not demonstrated actual anomalous windows. The continuous base-scale bound and consecutive integer endpoint remain unchanged. B_fix,odd(32), unconditional unbounded separation, anchor exit confirmation and independent review remain open.

## 5. Reproduction and next action

Use PREFIX-1158-execution-evidence.zip SHA256 2b8d60984e8f3bd6ebdca3a1cbbd64c6486496b6dffaf4de9fc044756ea02062; all 388 manifest entries verified. Run the compact checker at c086b43966187db1fae48fae251760dca9049c5a:research_notes/portable_direct/2026-11-28_r6_prefix1159_compact_verify.py in its extracted directory. Local executed SHA256 60ea835c79824f9b99127a6391523d1b234edadff02845835bebdc2d08018e05, Git blob b2663d31b9377425b66c8589d1dc03525a8997fa (exact remote match); output SHA256 fcde5343b1dfe8946788438a83e35c526a8e3c03861cbf7660e58396f4474813. The compact checker uses only exact arithmetic, reconstructs the new section and integer box, verifies all five fibers and scale exclusions; inherited input certificates are not regenerated. Full exploration, sensitivity and original mistake selecting q1 rather than q3 are preserved in the new ZIP. Next: scale-adaptive search using the new section at L>=3*10^134 and higher, and diagnose raw moment quantization before trying a finer output grid. Preserve the two point rows and all shared columns. No formal Result/Review claimed.

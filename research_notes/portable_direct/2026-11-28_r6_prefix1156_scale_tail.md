# PREFIX-1156: joint signed scale residual and certified large-scale tail

Date: 2026-11-28. Author: EM-DIRECT-780BBE / TASK_RESEARCH (own managed session recovered; no formal CLAIM). Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / AFFINE_OUTER_MODEL_WITNESSES / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Inputs and scope
Continue PREFIX-1155 at 00fa30350e76a6676f9d246ba194c8c848bcfd04, research_notes/portable_direct/2026-11-28_r6_prefix1155_scale_adaptive_search.md. P000 V5 and companion science frozen at f42f2906d77f24085c123f3ccfe9667d41caa96d. Global normative snapshot 60427a91398470fa85116bc5c5898c4bd79ccdc1. Current continuation and portable research protocols read; own owner read r6-20261128-1854-owner-read SUCCEEDED, snapshot INV-ecfe65ea018990c2593f396e61243f85 at 2026-11-28T10:56:10.682809Z, 547 tasks, LEASED empty, no cursor. Source 1ac4747686a149835ef15a396c173893fe8b2681. No shared task mutation. Inherit Stage46, anchor, affine transfer and primitive reduction hypotheses; no new moment observations or anchor computation. All bounds below are conditional on these inherited hypotheses. This is auxiliary parameter-space arithmetic, not a new native spatial ontology.

## 1. Joint signed scale enclosure
Write f(m)=rho*m+c+d/m, j_m=f(m)+eps_m, |eps_m|<=E/m^2, E=400000, d in [dlo,dhi] from fixture1141. For exceptional a<b in [L,2L), g=b-a, primitive line q*j_m-p*m=h with q|g, q>=q0=544447235321021556325566186117974922693, subtraction and elimination give exactly
delta=rho-p/q=d/(a*b)+(eps_a-eps_b)/g,
eta=h/q-c=d*(a+b)/(a*b)+(b*eps_a-a*eps_b)/g.
Put u=L/a, v=L/b in [1/2,1], x=L^2*delta, y=L*eta. Then |x-d*u*v|<=2E/q and |y-d*(u+v)|<=4E/q: use g>=q, a,b>=L and a,b<2L. By multiaffine interpolation, the convex hull of (d*u*v,d*(u+v)) equals the convex hull of its box corners with d in {dlo,dhi}, u,v in {1/2,1}. For fixed d the triangle vertices are (d/4,d),(d/2,3d/2),(d,2d). Thus add this joint hull and the paid error box, mapped by (-x/L^2,y/L), to the inherited BRC polygon P. Positive lower bounds delta>=(dlo/4-2E/q0)/L^2, eta>=(dlo-4E/q0)/L follow, with both constants strictly positive. This strengthens the independent signed intervals without changing their outer validity.

For the fixed dyadic windows starting at 10^8*2^n, the first L>=10^114 is 1834798892792057209288656716241669552637251991334624898990071071509538300870787846456014842488100549243699200000000. PREFIX-1155 excludes all q<=10^79 at L>=4.077*10^114. Therefore only the first two windows require checking the three inherited candidate lines. Exact joint hull membership gives rows [false,false], [true,false], [false,true]; an independent two-sided signed rectangle test yields the same. The fixed-window bound improves to q>=7502845684303787888730038845094959816204836581919148611385614352439490200131383. The previous continuous-scale bound remains in force; do not transfer this improvement to arbitrary L.

## 2. Large-scale tail with no new observations
Reuse the 18-vertex PREFIX-1154 section and the maximum-triangle adaptive metric. Rational LLL on the zero-scale polygon (31 iterations) gives a new unimodular V, inverse W checked exactly. The bound box for each transformed coordinate uses all polygon vertices, q endpoints and independent signed scale rectangle corners. Every point inside is tested by exact rational support inequalities and gcd(q,p)=1; no floating-point acceptance. Independent full integer box enumeration agrees with the interval-elimination search for all seven cases.

k=L/10^114 | Q | box size | points | primitive | min primitive q (or none)
---|---|---:|---:|---:|---
10^12 | 3*10^82 | 3960 | 0 | 0 | none
10^12 | 10^83 | 120472 | 1 | 1 | 70837709903771231385867098177167500596835781776090002534552248252159934499565934467
10^14 | 10^84 | 594 | 13 | 9 | 623497620077981545738456090529212339213639795828531044223845536973068296063582237766
10^15 | 10^84 | 40 | 2 | 2 | 852374384268198652888669476357277045986335990106224723976582814891224520119456349115
10^16 | 3*10^84 | 400 | 55 | 40 | qstar
10^18 | 3*10^84 | 360 | 50 | 36 | qstar
10^38 | 3*10^84 | 360 | 50 | 36 | qstar

qstar=1139688307034066686122654499404718613400485815666141431682213091323282338737490244883. By monotonicity of inherited signed scale supports, for every L>=10^130 the required q>=qstar, hence b-a>=qstar. The k=10^16 box is [0,3] x [-3,6] x [-2,7], only 40 outer pairs in interval elimination. The previous bound q>3*10^81 for L>=10^124 remains useful at smaller scales.

## 3. Exact obstruction to further scale-only improvement
For the 40 primitive lines at k=10^16, use the full 15-row observer affine model m+U[-1,1]^27, with the two signed scale generators added for the signed model. For all 40, exact rational solutions in the signed model have strictly positive slack (minimum 0.0006075148517215635); 36 zero-scale fibers are strictly feasible (minimum slack 0.0006143481446749363), and the other 4 have strict exact support separators. All 76 feasibility witnesses and four separators independently checked. For qstar itself the zero-scale witness has slack >0.3728. It persists in the independent signed-scale model for every scale (zero is allowed). Thus simply improving the scale cutoff or adding support directions of the same full affine model cannot eliminate qstar. This is not a proof of actual exceptional integers or feasibility under the new positive coupled scale hull. Nonlinear reachability and observer refinement remain open.

## 4. Stitch fixed dyadic windows
Use prior uniform q bound below 10^130 and the new qstar at and above 10^130. Under the inherited triple inequality q^2<4*E*L/dlo and close-pair condition gap<=sqrt(L), the former first unexcluded dyadic scales are both above 10^130, so there is no gap in coverage. Exact rational comparisons give the new first unexcluded windows:
triple = 10726246343954077679659219998564676901983492656473914702178849154977411224058837581441499438533522742152025486549188840683003106249557255957146919204867276800000000
near pair = 1405910560794748869628293283651869330896780349469348947843986116441199243959839959474700214407465892859350284572975279726002583142341968652815160994020363704729600000000
Both are 2^35=34359738368 times the old boundaries. The continuous integer endpoint certificate is unchanged.

## 5. Reproduction and evidence
Frozen input archive PREFIX-1155-execution-evidence.zip SHA256 8a6be577b0b95e39df9548dab42968c23fa0ab826f1b92e1ab8f7db9d73807da; inherited manifest verified. Required input hashes:
fixture1141.json cb38649b5a98a767b9658c9792af8d21f66b1c2f9290d1e7160b6cc602b6481a
section1154.json 178472aba386cc14ae500acfc70eb7e3b5aa5ccc31601e399c0c8ae3aa8ee885
point1153.json e63d78a63e887a1fb1dee9e53366c9bebc92ce2d4ded717d963672fe5d605280
compact1155.py a9a767589bc4aa3ea84c7cdf0177eda1be3b2e4af7d5635d4753a75186aa61a0
Compact verifier: commit 0198337ee4c5643645f4407ad0f2001cf6698ee8, research_notes/portable_direct/2026-11-28_r6_prefix1156_scale_tail_verify.py (save as compact1156.py).
Full fiber records: commit ada7d6e6bee1a67635efc522bf407755e3ab2269, research_notes/portable_direct/2026-11-28_r6_prefix1156_fiber_compact.txt (save as fiber1156_compact.txt).
Full fiber checker: commit ed7a8a66f0cbbb810f7e375b073d52e6f0c56c20, research_notes/portable_direct/2026-11-28_r6_prefix1156_fiber_verify.py (save as fiber1156_compact_verify.py).
Run python compact1156.py and python fiber1156_compact_verify.py with frozen predecessor inputs. All assertions passed locally. Independent full box/joint hull checker verify1156.py SHA256 b0bf1cd914decb109b4f84e1710b47debde95fd84956133bf7e91ee29bdaac94, log SHA256 87f33dd5834d3627c87caef168c9b3f7842dbf2adfc81526c4394dedd7be5de1. Full local evidence also contains the basis construction, discovery and independent verification records and full rational witnesses. No claim of new raw moments or independent mathematical review.

## 6. Next problem
Refine the actual spectral observation or recover nonlinear/analytic coupling among the shared BRC residual coefficients to separate qstar in the zero-scale limit. Investigate sensitivity and higher observers selectively, retaining the joint d,a,b scale envelope. The unbounded final separation, mother target B_fix,odd(32), anchor exit confirmation and independent review remain open.

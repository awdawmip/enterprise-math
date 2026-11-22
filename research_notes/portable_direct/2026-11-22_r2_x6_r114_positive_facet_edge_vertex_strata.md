# X6 R114 — Exact boundary-stratum losses in both sharp twelve-direction BRC cones

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_DERIVATION / EXACT_RATIONAL_ENUMERATION_PASS / NOT_INDEPENDENTLY_REVIEWED. Researcher: EM-DIRECT-80A6E0 (own original registered Source session MCP-794c32ed511e4a87aebc2ffed6cf1b70, Activity RA-0C3D078006ADE5971D9786F3). Independent auxiliary TASK_RESEARCH only: no formal X6 CLAIM, Result or Review.

## Scientific input and preserved scope

Continue the conditional **four-positive-weight, all-six-pair BRC observer** of R113, not the native P000 Cell/Link/Port time-dynamics claim. The original R113 conditional observer, integer moment map and frozen scientific input remain unchanged; Source P000 V5 and ACTIVE six-axis Heartbeat World remain typed foundations.

New input not available in the R113 handoff: independently published R90 results proving (a) **the thirteenth strict-near direction is impossible for all positive weights and integer Port p>=11**, (b) the complete **eight** twelve-direction sets in four chamber placements, and (c) the **two exact open sharp weight cones** and their 13-facet, 15-vertex normalized closures. They are reused as upstream results, preserving their authorship and proof status:
- [R90 complete twelve-direction catalog](https://github.com/awdawmip/chatgpt-global-knowledge/blob/105338ac5f56add9d1b86909a52b7a0a14f4aca6/journal/enterprise-math/2026-11-22/x6-r90-complete-twelve-direction-catalog.md).
- [R90 exact sharp weight regions and facets](https://github.com/awdawmip/chatgpt-global-knowledge/blob/6395fb2cb9b4596054aba5f2a2a1f7056a71468a/journal/enterprise-math/2026-11-22/x6-r90-exact-sharp-weight-regions.md).
- [R113 conditional BRC norm and exact moment inverse](https://github.com/awdawmip/enterprise-math/blob/740d80b0808d7e3158a645f36d7e576c4fe96dce/research_notes/portable_direct/2026-11-22_r2_x6_r113_interval_zonotope_chambers.md).

## Model, coordinates and main theorem

For a nonzero integer direction a=(x,y,z), counted modulo sign, let
q(a)=max(sum_i max(a_i,0), sum_i max(-a_i,0)).
Use u=x+3y+6z, v=3x+12y+30z, h=7x+39y+126z. For positive w=(A,B,C,D),

F_w(a)=max(|u|/(A+B), |v|/(A+C), |h|/(A+D),
           |v-u|/(B+C), |h-u|/(B+D), |h-v|/(C+D)).

eta_p=min{F_w(a):a!=0,q(a)<=p}; N_p={±a:q(a)<=p,F_w(a)<3*eta_p/2}.

Use the R90 ordered weight chamber: (A,C) are lower/higher odd channels, (B,D) lower/higher even. Rescale L=A+B=1; let s=min(A,B), X=C+s, Y=D+s. In type I, A=s<B; in type II, B=s<A. Both have 13 irredundant facets, including the ideal facet s=0 (outside the strictly positive-weight model). The closure inside the positive-weight domain has **12 codimension-one facet interiors, 20 edge interiors and 9 vertices**, for either type.

**R114 theorem (complete positive-boundary stratification).** For **every integer Port p>=196**, and for every point in the relative interior of any positive-weight face in the closure of either R90 sharp twelve-direction cone, the number of strictly 3/2-near directions depends only on that face. It is constant across its relative interior, with exact histograms:

| Stratum (per cone type) | Exact number of strata | Strict-near survivors : multiplicity |
|---|---:|---|
| 3D cone interior | 1 | 12 : 1 |
| Positive facet relative interiors | 12 | 11 : 1, 10 : 5, 9 : 2, 4 : 2, 3 : 2 |
| Positive edge relative interiors | 20 | 10 : 8, 9 : 1, 8 : 3, 4 : 4, 3 : 4 |
| Positive vertices | 9 | 10 : 3, 8 : 2, 4 : 2, 3 : 2 |

**Both cone types have identical survivor histograms at every stratum dimension**, despite differing weight inequalities and ordered template lists. In particular, the only possible survivor counts on the positive closure of a sharp cone are **{3,4,8,9,10,11,12}** at p>=196. Counts 5,6,7 never occur on these closures. This is a scoped assertion about the two sharp-cone closures, *not* the entire positive-weight parameter space.

The twelve physical codimension-one wall losses, in exact facet order from R90 (s=0 omitted), are:

| Facet number | Type I facet (zero) | Type I loss | Type II facet (zero) | Type II loss |
|---:|---|---:|---|---:|
| 2 | 1-2s | 2 | 1-2s | 2 |
| 3 | 9-2X | 9 | 9-X | 9 |
| 4 | 18-Y | 9 | 9-Y | 9 |
| 5 | X-2 | 8 | X-2s-5 | 2 |
| 6 | 6X-Y | 8 | 1-2s+X-Y | 2 |
| 7 | 3Y-34 | 2 | 3Y-6s-11 | 3 |
| 8 | 9Y-34X | 2 | 9-18s-7X+9Y | 3 |
| 9 | 3X-6s-5 | 3 | 3X-16 | 2 |
| 10 | 9+9X-2Y-18s | 3 | 9X-8Y | 2 |
| 11 | Y-2s-11 | 2 | Y-4 | 8 |
| 12 | 1-2s-4X+Y | 2 | 3Y-2X | 8 |
| 13 | 3X+3Y-6s-40 | 1 | 3X+3Y-6s-28 | 1 |

On each listed facet's relative interior all lost templates satisfy **exactly F_w(a)=3 eta_p/2**; no lost template lies strictly above that boundary there. A single facet may therefore eliminate one, two, three, eight or nine directions simultaneously at the strict cutoff.

## Proof

**(1) Complete finite carrying templates.** R90 supplies precisely twelve ordered relative-height templates (0,t,3m,t+6n), m congruent n mod 2, for each type. For I these are t=0: (m,n)=(0,2),(1,-1),(1,1); t=1: m=±1,n∈{-3,-1,1}, or m=0,n∈{-2,0,2}. For II these are t=0: (1,-1),(1,1),(2,0); t=1: m∈{-2,0,2},n=0, or m∈{-1,1,3},n∈{-1,1}. The R90 physical-chamber Port table bounds all twelve template costs by 196 in every placement. Also the unrestricted optimum is attained by Port 125 across all chambers. Thus for every p>=196, eta_p=eta_infinity.

**(2) Continuity excludes entering outsiders.** Fix p>=196 and a positive boundary point w0 approached from one sharp-cone interior. The finite set {a:q(a)<=p} makes eta_p(w) a continuous function of positive w. If an outside direction were strictly near at w0, it would be strictly near at nearby interior points, contradicting the exact R90 twelve-direction catalog. Thus the wall's strict-near set is a subset of the twelve carried templates. This argument applies separately for each p>=196 and preserves all six observations.

**(3) Membership is a finite set of affine strict inequalities.** In the normalized chamber, R90's exact reciprocal-optimum comparison scales on the sharp cones are
T_I=max(1,X/3,Y/12), T_II=max(1,X/6,Y/6).
They coincide there with 1/eta_infinity and extend continuously to the positive part of the closures. Write each T as max of three affine forms tau_k, and each template's six integer pair gaps as d_ij=|t_i-t_j|. Then F_w(a)<3 eta_p(w)/2 is equivalent to the **18 strict affine inequalities**
3(w_i+w_j)-2 d_ij tau_k(w)>0
for all six ij and three k. Every such slack is nonnegative on the closure because all twelve templates are strictly near in the interior.

On any face, the restriction of a nonnegative affine slack is either identically zero or is strictly positive throughout that face's relative interior. Hence template membership and the number of surviving templates are constant on every relative interior. For a facet, average **all its vertices** to obtain a rational point in the relative interior. For an edge, average its two endpoints; for a vertex, use itself. Therefore a single exact rational evaluation per face is sufficient to classify that entire face, not just the chosen sample.

**(4) Exhaustive exact face enumeration.** Enumerate all intersections of three distinct facet planes; retain points meeting all 13 nonnegative half-space inequalities. For each type this gives exactly 15 vertices. Two vertices share an edge iff they lie on at least two common facet planes: enumeration gives 26 edges. The ideal nonpositive facet s=0 has 6 vertices and 6 edges; removing their relative interiors leaves 9 positive vertices, 20 positive edge interiors and 12 positive facets. For each face's exact relative-interior rational point, evaluate all 12 template scores using exact rational arithmetic and T= max(1,X/6,Y/12,min(X/3,Y/6)), which equals the type-specific T on these closures. The reported counts follow. The same check finds equality (never strict excess) for every lost template on any facet. This proves the table, conditional on the exact R90 cone and twelve-template classification. □

## Reproduction and validation

The self-contained pure-Python Fraction verifier records all 26 facets of the two types, their 15 vertices/26 edges per type, midpoint witnesses, 12 template comparisons, equality losses and all positive edge/vertex strata. All 12 physical facets, 20 positive edges and 9 positive vertices per type pass. Type-I and Type-II loss multisets both equal [1,2,2,2,2,2,3,3,8,8,9,9]. Independent symbolic (SymPy Rational) enumeration reproduced the facet counts, edge and vertex histograms. Exact results are conditional on the upstream R90 theorem; no independent review/admission is claimed. No continuum or floating error enters the finite face arithmetic.

## Next genuinely open scientific units

1. Determine the exact **transverse** outside-chamber direction replacements at each of the 12 physical facets. The present theorem classifies the boundary itself, not the new chamber after crossing.
2. Classify the early-Port p=28...195 boundary strata, retaining the physical permutation-specific feasibility thresholds.
3. Independently audit the inherited R90 finite predecessor-rectangle completeness argument if a new formal mathematical review is commissioned. The native X6 R063 time-dynamics six-file benchmark remains a separate unresolved Task, with its original frozen inputs.

Control distinction: own Researcher session registered successfully; current native Task/continuation reads were resource-waiting. No live CLAIM or formal execution authorization has been inferred from that status. This mathematical note is an independently saved auxiliary research artifact.
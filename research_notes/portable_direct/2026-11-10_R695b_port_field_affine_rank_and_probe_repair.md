# R695b — One native Cell-port deletion raises E* BRC observation rank from 2 to 3

Date: 2026-11-10. Status: AUTHOR-DERIVED / EXACT-COMPUTATION-CHECKED / UNREVIEWED.
Parent source: R695 commit `46d1eaafff4d10d54850865d758b2b85dc4dad0d`, task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Original static-port candidate: R692 PR #1985, immutable commit `2b393a2f2df78faadf4dff69b9694742692d29d3`, `R692_VERIFY.py` blob `dea329fcac6e7fa8499452d761b9e2e23fd4f573`. E* group/continuation kernels: R692C blob `0c6d51f99eac5903a30770c8c393c972a68d93ad`. P000 and the task scientific pin remain unchanged.

## Exact static-port candidate and BRC source construction

At root phase `a=b=0`, the 60 labelled 4-step native X6 returning squares have positive integral BRC holonomy counts
[
 n=(n_e,n_t,n_c,n_{c^2})=(24,18,6,12).
]
R692 establishes that every labelled square has its own **third-step mixed-corner directed port variable**, unique among all 60 squares. Switching exactly that one port from 1 to 0 in the otherwise fully open static Cell-port field therefore removes exactly that square. Since all four holonomy group bins have positive counts, for each (g\in\{e,t,c,c^2\}) there is a realizable static port field with resulting normalized group law
[
 μ_g(h)=\frac{n_h-\mathbf1_{h=g}}{59}.
]
These are distinct deterministic static-port candidates, preserving each removed source identity in the full BRC branch record. The R692 use of a binary directed gate at a Cell is a candidate; actual pinned V29/V39 Link/Port update permission is still to be studied.

## Theorem R695b-A — Exact three-dimensional affine hull

The four attainable group laws (μ_e,μ_t,μ_c,μ_{c^2}) are affinely independent inside the four-bin probability simplex. With (μ_{c^2}) as reference, the differences in free coordinates (e,t,c) are
[
 μ_e-μ_{c^2}=(-1,0,0)/59,quad
 μ_t-μ_{c^2}=(0,-1,0)/59,quad
 μ_c-μ_{c^2}=(0,0,-1)/59.
]
Their determinant is (-1/59^3\ne0). Hence the convex hull of these four lawful *candidate port-field* first-macro kernels has affine dimension 3. In contrast, R695's fixed-direction-source convex family has dimension 2 at phase 0, since its unit-kernel identity mass is always (2/5).

A single remote deletion of a (c^2)-holonomy source already changes the one-step return from (24/60=2/5) to (24/59), an exact difference of (2/295).

## Theorem R695b-B — Optimal three-scalar external contextual tomography

For any group law (μ) supported on (e,t,c,c^2), measure (r=μ(e)) and two externally chosen fixed R692C continuation probes (A=B_{ν_{0,1}}(μ)), (B=B_{ν_{0,4}}(μ)). With (x=μ(t)), (y=μ(c)),
[
 A=2r/5+3x/5,qquad B=2r/5+x/5+2y/5.
]
Therefore
[
 x=(5A-2r)/3,qquad y=(5B-2r-x)/2,qquad
 μ(c^2)=1-r-x-y.
]
The determinant is (6/25\ne0), so these three scalar return observations recover the entire law. Three are minimal for **uniformly reconstructing all nonnegative convex mixtures** of the four static-port kernels from fixed nonadaptive scalar return tests. This is a linear-algebraic lower bound on a three-dimensional convex family, not a count for the finite collection of deterministic binary port fields.

### Exact fiber witness: R695's two phase-0 continuation probes cease to suffice

Let (μ_L=3μ_e/4+μ_{c^2}/4) and (μ_R=(μ_t+μ_c)/2). They have common denominator 236 and numerators
[
μ_L=(93,72,24,47)/236,qquad
μ_R=(96,70,22,48)/236.
]
For **both** laws the two R695 phase-0 returns are
[
 A=201/590,qquad B=153/590,
]
while their one-step return differs by (3/236). This is a concrete full-information fiber contrast under the exact external-probe observation.

## Evidence, observer scope and continuation

Executed attached JS exact integer certificate `R695B_PORT_FIELD_AFFINE_VERIFY.js` and corresponding result JSON. The proof's source identity and the one-port isolation rely on R692's independently executed 60-square BRC enumeration; the new affine-rank and two-probe-fiber algebra is elementary and checked with integer counts.

External control of continuation masks is an experimental observer condition. A fixed static port field cannot be assumed to allow arbitrary switching between future probes; actual legal pinned X6 Link/Port, V29 PASS/TRANSFER and V39 event updates must establish their reachable observation span. The next unit is a source-typed rank/observability computation over those reachable suffix events, retaining the Cell, port state, labelled square path, and ledger histories.
# #1162 — unequal-subdivision order-2 finite port packet

Status: RESEARCH_NOTE / EXACT FINITE PORT THEOREM + FIBER WITNESS / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-unequal-subdivision-order2-finite-port-20260908-b62d
Date: 2026-09-08

## 1. Scope

Continue the user's requirement that rough discrete relations be handled by finite admissible operations rather than unstable microscopic differentiation. Parent result: `research_notes/1162_all_order_equal_subdivision_schur_modes_20260908_b62d.md` proves finite even scale closure for equal subdivision of rough weighted cycles. Here equal subdivision is removed locally: one coarse two-terminal edge may be replaced by an arbitrary positive series path.

The question is observer-typed: what finite data from that hidden path suffice to preserve global inverse-spectrum information through order m=2 when the path is embedded in an arbitrary connected coarse graph context?

## 2. Exact two-terminal module

Let a positive series path of total resistance r connect two retained endpoints and have h hidden vertices. Partition its finite Laplacian as

`L_M = [[A,B],[B^T,H]]`,

where H is the h by h positive-definite Dirichlet block. Define the harmonic extension matrix

`E=-H^(-1)B^T`.

For a path with hidden electrical positions `0<x_a<r`, row a of E is exactly

`[1-x_a/r, x_a/r]`.

Treat t as a formal indeterminate, not an infinitesimal observable. Eliminating hidden vertices gives the exact formal Schur series

`K(t)=A-B(H+tI)^(-1)B^T
     =K_0+tP_1-t^2P_2+t^3P_3-...`,

where

`P_j=E^T H^(-(j-1)) E`  for j>=1.

The hidden determinant factor is

`Z(t)=det(H+tI)/det(H)=1+h_1 t+h_2 t^2+...`,

`h_1=Tr H^(-1)`,

`h_2=((Tr H^(-1))^2-Tr H^(-2))/2`.

For a path, the Dirichlet Green matrix is finite and explicit:

`G_ab=(H^(-1))_ab=min(x_a,x_b)[r-max(x_a,x_b)]/r`.

Hence

`h_1=sum_a x_a(r-x_a)/r`,

`h_2=sum_(a<b) x_a(x_b-x_a)(r-x_b)/r`.

Also `E 1_2=1_h`, so the only order-3 port scalar needed below is

`sigma_3=1_2^T P_3 1_2=1_h^T H^(-2)1_h`.

Everything is finite matrix algebra.

## 3. Sufficiency for global c1,c2,c3

Embed finitely many such edge modules into any fixed connected coarse graph. After eliminating every hidden block,

`det(L_fine+tI)=[product_e det(H_e+tI)] det S(t)`,

where

`S(t)=L_coarse+tI
      +sum_e embed_e[tP_(1,e)-t^2P_(2,e)+t^3P_(3,e)+O(t^4)]`.

Write

`det S(t)=d_1t+d_2t^2+d_3t^3+O(t^4)`.

The coefficients d1,d2 depend only on S1 and S2 in the usual finite determinant multilinearity. At order three the only term linear in S3 is

`Tr(adj(L_coarse) S3)`.

For a connected coarse Laplacian,

`adj(L_coarse)=tau 1 1^T`,

where tau is the weighted spanning-tree value. Therefore S3 enters d3 only through

`1^T S3 1=sum_e 1_2^T P_(3,e)1_2=sum_e sigma_(3,e)`.

Multiplying by the hidden factors shows:

**Order-2 finite-port theorem.** Given each coarse edge resistance (hence K0), the finite module packet

`J_edge^(2)=(P_1,P_2,sigma_3,h_1,h_2)`

is sufficient to determine the global characteristic coefficients c1,c2,c3, hence

`e1=c2/c1`, `e2=c3/c1`,

and

`Tr L^+=e1`, `Tr(L^+)^2=e1^2-2e2`,

for every connected coarse context.

No derivative or hidden interpolation is used. The packet size is independent of how many hidden vertices the subdivided edge contains.

For a series path h1 is already recoverable from P1 because

`h1=r(P1)_(12)`.

Thus one may omit h1 when r and P1 are retained. No minimality claim is made for the remaining packet at this stage.

## 4. Exact local witness: same complete m=1 port, different m=2 data

Take r=1 and four positive series subresistances. Equivalently specify the three hidden electrical positions.

Module A:

`x=(1/10,1/2,3/5)`, i.e. subresistances `(1,4,1,4)/10`.

Module B:

`x=(1/5,3/10,7/10)`, i.e. subresistances `(2,1,4,3)/10`.

Both have

`sum x=6/5`, `sum x^2=31/50`.

Therefore their complete first Schur Gram packet agrees exactly:

`P1(A)=P1(B)=(1/50)[[61,29],[29,31]]`,

and

`h1(A)=h1(B)=29/50`.

But order two already separates them:

`P2(A)=(1/2500)[[819,691],[691,699]]`,

`P2(B)=(1/2500)[[1119,641],[641,499]]`,

`h2(A)=3/50`,

`h2(B)=2/25`.

The next zero-mode port scalar also differs:

`sigma3(A)=641/1250`,

`sigma3(B)=283/625`.

Thus equality of the complete m=1 two-terminal Schur response does not factor the m=2 future language.

## 5. Same external graph witness

Embed A or B as one side of the same coarse triangle; let the other two sides each have resistance 1. The resulting fine cycles have six vertices in both cases.

Exact finite characteristic-polynomial arithmetic gives

`e1(A)=e1(B)=31/25`.

Thus their first inverse spectral moment is still identical after embedding in the same external context.

But

`e2(A)=467/900`,

`e2(B)=47/90`,

so

`Tr[(L_A^+)^2]=5623/11250`,

`Tr[(L_B^+)^2]=2774/5625`,

with exact difference

`Tr[(L_A^+)^2]-Tr[(L_B^+)^2]=1/150`.

Therefore the local port distinction is externally observable at order m=2; it is not an artifact of looking inside the edge.

## 6. BRC interpretation

REUSE_APPLIED: this is a concrete realization of the existing recurrent-port/future-language rule. The Schur packet is the visible port response. Absolute characteristic/spectral observers additionally need the hidden determinant factor `Z_int`; equality of a low-order port response does not license deletion of higher response coefficients or hidden determinant data.

The carrier is not a positive-mass collapse. Although P_j are positive-semidefinite matrices, their determinant expansion enters with alternating signs and the global observer is signed. Preserve labels and coefficient order.

The exact A/B witness is a fiber-loss certificate: collapsing an arbitrary hidden path to its m=1 port packet identifies two modules that a permitted m=2 external context distinguishes.

## 7. Relation to equal-subdivision closure

For equal subdivision the hidden positions are rigid arithmetic progressions. The all-order parent theorem shows their entire port/determinant packet lies on a finite `Q^-2` mode manifold. Unequal subdivision introduces independent module coordinates rather than new microscopic derivatives. The correct extension is therefore finite coefficient ports, not a continuous derivative jet.

## 8. Next

1. Reduce `J_edge^(2)` further using identities special to one-dimensional series paths and determine its generic minimal dimension.
2. Derive composition rules for concatenating two arbitrary order-2 path packets without reopening hidden vertices.
3. Lift the packet from one edge to arbitrary unequal subdivision of every edge of a weighted cycle, then identify which quotient suffices for the scalar beta2 future language.
4. Compare this finite packet theorem with the closest published response-matrix / Dirichlet-to-Neumann / graph-zeta port reductions before any novelty claim.
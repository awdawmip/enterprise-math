# #1162 — finite all-order series-path port composition

Status: RESEARCH_NOTE / EXACT FINITE COMPOSITION THEOREM / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-series-path-all-order-port-composition-20260908-b62d
Date: 2026-09-08

## 1. Scope

Continue `research_notes/1162_unequal_subdivision_order2_finite_port_jet_20260908_b62d.md`. The user has explicitly rejected microscopic differentiation as a default stable primitive under rough discrete relations. This note proves that arbitrary positive series subdivision can instead be handled by a finite, exactly composable two-terminal coefficient packet at every fixed spectral order.

The probe t below is a formal determinant/resolvent indeterminate. Coefficients are obtained by finite matrix identities and coefficient arithmetic; no t->0 measurement or derivative stability assumption is used.

## 2. Exact visible Schur function and hidden determinant recovery

For a positive series path module M with two retained endpoints, partition

`L_M=[[A,B],[B^T,H]]`

with positive-definite hidden Dirichlet block H. Define its visible Schur function

`K_M(t)=A-B(H+tI)^(-1)B^T`.

Write

`K_M(t)=K_0+tP_1-t^2P_2+t^3P_3-...`,

`P_j=E^T H^(-(j-1))E`, `E=-H^(-1)B^T`.

For a one-dimensional series path with edge conductances c_1,...,c_q, the off-diagonal entry has the exact cofactor form

`(K_M(t))_(12) = - product_(j=1)^q c_j / det(H+tI)`.

At t=0 this equals `-1/r`, where r is the total series resistance. Therefore

`Z_int(t):=det(H+tI)/det H
          =(K_M(0))_(12)/(K_M(t))_(12)`.

Hence the complete hidden determinant factor is recoverable from the visible off-diagonal port response. This is special to the one-dimensional unique-path carrier; it is not asserted for general hidden graphs.

The order-2 identity from the parent note is the coefficient consequence

`h_1=r(P_1)_(12)`,

`h_2=h_1^2-r(P_2)_(12)`.

A direct proof of the second relation is also available. With normalized hidden positions t_a=x_a/r and Brownian-bridge Green matrix G_ab=min(t_a,t_b)(1-max(t_a,t_b)), pairwise expansion gives

`(P_2/r)_(12)
 =sum_a G_aa^2+sum_(a<b)(G_aa G_bb+G_ab^2)
 =hbar_1^2-hbar_2`,

which rescales to the displayed formula.

## 3. Exact serial composition

Let modules A and B be joined by identifying A's right endpoint with B's left endpoint, and then treat that joined vertex as hidden. Write the visible 2x2 Schur matrices as

`K_A(t)=[[a(t),b(t)],[b(t),d(t)]]`,

`K_B(t)=[[e(t),f(t)],[f(t),g(t)]]`.

The joined vertex has its own `+t` probe mass, so define

`Delta(t)=d(t)+e(t)+t`.

Exact one-vertex Schur elimination gives the composed module C=A star B:

`K_C,11 = a-b^2/Delta`,

`K_C,12 = -b f/Delta`,

`K_C,22 = g-f^2/Delta`.

This is an exact rational operation on formal series. If

`Delta(t)=sum_(j=0)^M delta_j t^j + O(t^(M+1))`,

its reciprocal coefficients are obtained by the finite recurrence

`alpha_0=1/delta_0`,

`alpha_n=-(1/delta_0) sum_(j=1)^n delta_j alpha_(n-j)`.

Thus the coefficients of K_C through order M are determined solely by the coefficients of K_A and K_B through order M. No hidden vertices need to be reopened.

The hidden determinant obeys simultaneously

`Z_C(t)=Z_A(t) Z_B(t) Delta(t)/Delta(0)`

after normalization at t=0. The previous section shows this normalized factor is also reconstructed directly from `K_C,12(0)/K_C,12(t)`; the two descriptions agree identically.

## 4. Fixed-order composable packet

For any fixed inverse-spectral order m, define the serial-safe packet

`P_m(M)=(K_0,P_1,...,P_(m+1))`.

The composition formula proves that this finite packet is closed under arbitrary serial concatenation of positive path modules. Once the final modules are embedded in a finite coarse graph, the characteristic coefficients `c_1,...,c_(m+1)` and inverse spectral moments through order m are determined by finite determinant coefficient arithmetic. The hidden determinant coefficients needed through order m are already encoded by the off-diagonal Schur series.

Therefore arbitrary unequal series subdivision does not force an infinite or differential state at fixed m. It produces a finite matrix-valued port state whose size depends on m, not on the number of hidden subdivisions.

For future language restricted to one immediate embedding and global `c_1,c_2,c_3`, the parent note safely quotients `P_3` to the single contraction `sigma_3=1^T P_3 1`, yielding a smaller six-scalar effective packet. For future language allowing further serial composition, that quotient is not licensed: the composition formula uses the oriented entries of P_3.

This is a direct observer-horizon distinction.

## 5. Order-2 effective dimensions

Fix total resistance r=1 and hidden count h.

`P_1` is symmetric but satisfies `1^T P_1 1=h`, so it has two effective scalar degrees. `P_2` and `P_3` are general symmetric 2x2 coefficient matrices in the path family. Thus the serial-safe order-2 packet has at most eight effective scalar entries:

`(P1_12,P1_22, P2_11,P2_12,P2_22, P3_11,P3_12,P3_22)`.

These eight directions are generically independent. At h=8 and exact internal positions

`(1,4,8,13,19,25,32,38)/41`,

the exact Jacobian determinant of the above eight polynomial/rational port coordinates with respect to the eight positions is

`-669564656640 / 13422659310152401 != 0`.

Thus no local algebraic redundancy reduces the full oriented P1-P3 packet at a generic point. This is a local independence statement for the port coordinates, not a global uniqueness theorem for all possible nonlinear encodings.

For the smaller one-shot six-coordinate packet of the parent note, at positions `(1,4,8,13,19,26)/31` the exact Jacobian determinant is

`-13440/28629151 !=0`.

So its six retained directions are likewise genuinely independent in the path family.

## 6. BRC resolution

REUSE_APPLIED: exact port-collapse / future-language discipline. Generic BRC warns that absolute loop/determinant observables may require a hidden `Z_int` factor beyond the visible port matrix. In the present one-dimensional path class, the special cofactor identity `Z_int=K12(0)/K12(t)` proves that hidden determinant information is already recoverable from the visible transmission response. This is a proved special-case reduction, not a generic port-collapse assumption.

The packet is endpoint-labeled and matrix-valued. It must not be collapsed to positive total mass. Coefficients enter with alternating signs and serial composition mixes endpoint directions.

The distinction between the six-coordinate one-shot packet and the eight-coordinate serial-safe packet is exactly observer-horizon typing: a compression safe for immediate global spectral readout is not automatically safe when future serial composition remains allowed.

## 7. Next

1. Lift this module composition law to an arbitrary unequal subdivision step on every edge of a weighted cycle and derive the induced finite state update for the scalar beta_2 observer.
2. Determine whether beta_2 future language admits a much smaller driven state than the full eight-coordinate per-edge packet, analogous to the `(H,V;Gamma,U)` collapse at m=1.
3. Generalize the exact local independence calculation to order m and formulate a dimension bound for the serial-safe packet.
4. Compare the one-dimensional identity `Z_int=K12(0)/K12(t)` with classical Dirichlet-to-Neumann / continuant response formulas before any novelty claim.
# #1162 — all-order equal-subdivision Schur modes for positive weighted cycles

Status: RESEARCH_NOTE / EXACT FINITE THEOREM PACKAGE / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-all-order-equal-subdivision-schur-modes-20260908-b62d
Date: 2026-09-08

## 1. Scope

Continue the user's correction that microscopic differentiation is not automatically stable or native under a rough discrete relation. The only scale operation below is actual integer equal electrical subdivision. No derivative in N or infinitesimal scale interpolation is used.

Parents:
- `research_notes/1162_resolution_admissibility_correction_20260907_b62d.md`
- `research_notes/1162_refinement_projector_stability_20260908_b62d.md`
- `research_notes/1162_equal_subdivision_roughness_rg_20260908_b62d.md`
- `research_notes/1162_rooted_forest_jet_roughness_carrier_20260908_b62d.md`
- `research_notes/1162_integer_refinement_semigroup_split_schur_pi_blowup_20260908.md`

## 2. Setup and reduced determinant

Let a positive weighted cycle C_N have edge resistances r_i>0, i mod N. For integer Q>=1, form C_N^[Q] by replacing edge r_i with Q equal series resistors r_i/Q, hence fine conductance a_i=Q/r_i and QN vertices.

Let L_Q be the fine weighted Laplacian. Write

`det(L_Q+t I)=c_(1,Q)t+c_(2,Q)t^2+...`

and let

`e_k^[Q]=c_(k+1,Q)/c_(1,Q)`

be the kth elementary symmetric polynomial of the inverse nonzero eigenvalues. Define the mass-rescaled reduced determinant

`D_Q(z)=det(L_Q+(z/Q)I)/[(c_(1,Q)/Q)z]`

so

`D_Q(z)=1+sum_(k>=1) e_k^[Q] Q^(-k) z^k`.

The theorem below states that every coefficient is a finite polynomial in rho=Q^(-2).

## 3. Exact edge-chain Schur formulas

Retain the original N coarse vertices and eliminate the Q-1 hidden vertices inside every subdivided edge. For edge i set

`y_i=1+r_i z/(2Q^2)`.

Let U_j,T_j denote Chebyshev polynomials of the second/first kind. The hidden tridiagonal block on edge i has determinant

`(Q/r_i)^(Q-1) U_(Q-1)(y_i)`.

Define

`u_i(z,rho)=Q^(-1) U_(Q-1)(y_i)`

and

`v_i(z,rho)=2[T_Q(y_i)-1]/(r_i z)`.

The exact Taylor formula is

`u_i = sum_(j>=0) r_i^j z^j/(2j+1)! * product_(ell=1)^j (1-ell^2 rho)`.

This follows from

`U_(Q-1)^(j)(1)/j! = 2^j binom(Q+j,2j+1)`

and

`Q^(-1-2j) binom(Q+j,2j+1)
 = product_(ell=1)^j(1-ell^2/Q^2)/(2j+1)!`.

The product vanishes automatically for j>=Q, so the displayed infinite notation is coefficientwise exact.

Since T_Q'(x)=Q U_(Q-1)(x),

`v_i=(1/z) integral_0^z u_i(s,rho) ds`.

Thus the coefficient of z^j in either u_i or v_i is a polynomial in rho of degree at most j.

The Schur edge conductance and diagonal leakage are

`c_i(z)=1/[r_i u_i(z)]`,

`h_i(z)=(z/2) v_i(z)/u_i(z)`.

A single Q-chain contributes diagonal

`c_i+h_i-z/(2Q)`

at each endpoint and off-diagonal `-c_i`.

Because every cycle vertex has degree exactly 2, the two `-z/(2Q)` endpoint terms cancel the retained vertex mass `+z/Q` exactly. Hence the coarse Schur matrix is

`S_Q(z)=L(c_0(z),...,c_(N-1)(z))
       +diag(h_(i-1)(z)+h_i(z))`.

There is no remaining Q^(-1) port term.

## 4. Coefficient ring and all-order theorem

Let R be the class of formal series `f(z)=sum f_j(rho)z^j` with `deg_rho f_j<=j`. R is closed under addition, multiplication and inversion when f_0 is nonzero. Hence all c_i lie in R, while the coefficient of z^j in h_i has rho-degree at most j-1 for j>=1.

Use the finite matrix-forest expansion for a weighted Laplacian plus diagonal masses:

`det(L(c)+diag(m))
 = sum_F [product_(e in F)c_e] product_(T component of F)[sum_(v in T)m_v]`.

A forest with k components contributes k mass factors. Therefore, in the coefficient of z^(m+1), the rho-degree is at most

`(m+1)-k <= m`,

because each mass coefficient of z^j costs rho-degree at most j-1, while each conductance coefficient of z^j costs at most j.

At z=0, S_Q(0) is the original coarse weighted Laplacian. Its linear determinant coefficient is c_(1,base), and exact block determinant factorization gives

`D_Q(z)=[product_i u_i(z,rho)] det S_Q(z)/[c_(1,base) z]`.

Consequently:

**Theorem (finite Schur-mode closure).** For every k>=1 there are Q-independent coefficients a_(k,0),...,a_(k,k), determined by the original positive weighted cycle, such that for every integer Q>=1

`e_k^[Q] = sum_(r=0)^k a_(k,r) Q^(k-2r)`.

Equivalently,

`e_k^[Q]/Q^k in span{1,Q^(-2),...,Q^(-2k)}`

exactly, with no asymptotic remainder.

Thus the order-m reduced-determinant state can be carried by the finite triangular mode jet

`J_m^Schur={a_(k,r): 1<=k<=m, 0<=r<=k}`,

of size at most `m(m+3)/2`. Under a further integer P-subdivision, its rebased amplitudes transform diagonally by

`a_(k,r) -> P^(k-2r) a_(k,r)`.

This is a genuine finite refinement representation, not a differential jet.

## 5. Consequence for inverse spectral moments

Let

`p_m^[Q]=Tr[(L_Q^+)^m]`.

Because

`log D_Q(z)=sum_(m>=1)(-1)^(m+1) p_m^[Q] z^m/(m Q^m)`,

the theorem implies

`p_m^[Q]/Q^m = sum_(r=0)^m d_(m,r) Q^(-2r)`

for Q-independent d_(m,r).

For the scale-free cycle readout

`beta_m^[Q]=2^(2m-1) p_m^[Q]/[(QN)^m S^m]`

(with S=sum r_i; set S=1 after normalization),

`beta_m^[Q]=sum_(r=0)^m C_(m,r) Q^(-2r)`.

Therefore repeated fixed-q equal subdivision obeys

`beta_m(q^n N)=sum_(r=0)^m C_(m,r) q^(-2rn)`.

The exact annihilator and fixed-mode projector from the earlier stability note now apply unconditionally inside this class:

`product_(r=0)^m(E_q-q^(-2r)I) beta_m =0`,

`Pi_(m,q) beta_m=C_(m,0)`.

The previously proved sup-error amplification `<2` for integer q>=2 therefore controls the rough-cycle fixed readout at every order m, not merely a postulated correction model.

Uniform cycles have the classical coefficients `C_(m,0)=zeta(2m)/pi^(2m)` after the separate angular/Fourier compatibility calibration. Rough cycles generally have a shifted signed fixed coefficient.

## 6. Explicit m=2 forest-mode state

Normalize `sum_i r_i=1`. For i<j let d=j-i and define

`T2=sum_(i<j) r_i r_j d(N-d)`,

`T3=sum_(i<j<k) r_i r_j r_k (j-i)(k-j)(N-k+i)`,

`R2=sum_i r_i^2`, `R3=sum_i r_i^3`,

`M21=sum_(i<j) d(N-d) r_i r_j(r_i+r_j)`.

At the coarse scale

`e1=T2/N`, `e2=T3/N`.

Set

`K=(2N R2-1)/12`,

`a_plus=(T2+K)/N`,
`a_minus=-K/N`,

`b_plus=[60 M21+8N R3-5N-2R2+360T3]/(360N)`,

`b_zero=-[12M21+4N R3-N-2R2]/(72N)`,

`b_minus=[3N R3-2R2]/(90N)`.

A direct finite grouping of deleted fine edges by whether their coarse parents are all distinct, two equal, or three equal gives for every integer Q>=1

`e1^[Q]=Q a_plus+Q^(-1)a_minus`,

`e2^[Q]=Q^2 b_plus+b_zero+Q^(-2)b_minus`.

Thus the five-mode carrier

`S2=(a_plus,a_minus,b_plus,b_zero,b_minus)`

is exactly closed, with diagonal refinement weights

`(Q,Q^(-1),Q^2,1,Q^(-2))`.

It is equivalent to the coarse finite carrier `(e1,e2,R2,R3,M21)`: the inverse formulas include

`e1=a_plus+a_minus`,

`R2=(1-12N a_minus)/(2N)`,

`e2=b_plus+b_zero+b_minus`,

`R3=30 b_minus+2R2/(3N)`,

`M21=(N+2R2-4N R3-72N b_zero)/12`.

For the scalar second inverse moment,

`beta_2^[Q]=C0+C1 Q^(-2)+C2 Q^(-4)`

with

`C0=8(a_plus^2-2b_plus)/N^2`,

`C1=16(a_plus a_minus-b_zero)/N^2`,

`C2=8(a_minus^2-2b_minus)/N^2`.

Hence the future language consisting only of beta_2 refinement readouts needs only three mode amplitudes, while the richer future language asking for the full `(e1,e2)` forest jet needs the five-mode carrier above.

## 7. Exact BRC fiber witness: J2 plus the full Basel rough state is still insufficient

Take N=5 and normalized resistance gaps

`gA=(1,3,7,2,7)/20`,

`gB=(1,5,7,1,6)/20`.

They satisfy exactly

`R2=7/25`,
`T2=373/200`,
`T3=81/400`.

Thus they have the same coarse

`e1=373/1000`, `e2=81/2000`,

and therefore the same `beta_1=373/2500` and `beta_2=58129/3125000`.

Because R2 is also the same, their dyadically refined beta_1 is identical:

`beta_1^[2]=791/5000`.

So the two cycles have the same entire m=1 equal-subdivision orbit, not merely one Basel readout.

But their cubic repair coordinates differ:

A: `R3=361/4000`, `M21=503/500`;

B: `R3=343/4000`, `M21=509/500`.

Consequently

`beta_2^[2](A)=352587/25000000`,

`beta_2^[2](B)=348537/25000000`,

with exact difference `81/500000`.

Therefore a single-scale J2, even augmented by the complete m=1 refinement state, does not factor the future m=2 observer. The cubic coordinates are genuine new retained information.

For generic local minimality, at N=6 the Jacobian of

`(S,R2,T2,T3,R3,M21)`

with respect to `(r0,...,r5)` at `(1,2,3,4,5,6)` has exact determinant

`-2903040 !=0`.

Thus after fixing total scale S, the five coordinates `(T2,T3,R2,R3,M21)` are locally independent. Since their map to the five Schur amplitudes is invertible, the five-mode carrier is generically locally minimal for the full order-2 forest-jet orbit among smooth scalar coordinate compressions.

## 8. Why degree two is structural

The even `Q^(-2)` closure uses an exact cycle cancellation. For a general graph vertex v of degree d_v, Schur elimination leaves in addition

`(z/Q)(1-d_v/2)`

on the retained diagonal. This vanishes identically exactly at degree 2. Otherwise odd Q^(-1) information survives.

A finite counterexample is the three-arm star. Subdivide each of its three unit-resistance arms into Q equal resistors. The fine tree has `3Q+1` vertices and direct resistance summation gives

`Tr L_Q^+ = (7Q^2+9Q+2)/[2(3Q+1)]`.

Hence

`Q^(-1) Tr L_Q^+
 =7/6+1/Q+1/[3(3Q+1)]`,

which is not a finite polynomial in Q^(-2). Thus the exact even-scale closure is a degree-2 rotation-topology phenomenon, not a generic subdivision law.

## 9. Evidence and prior-art boundary

Exact Fraction enumeration independently checked the m=2 formulas for multiple rational weighted C4 cycles and Q=1,...,5. Forest enumeration also checked the predicted `beta_m^[Q]` polynomial degrees for m=3 and m=4 on rational rough cycles beyond their interpolation points before the all-order proof above was completed.

Prior-art search found broad subdivision spectra, Schur/spectral-decimation, Chebyshev continuants, quantum/discrete graph zeta relations, and forest interpretations of Laplacian coefficients. These ingredients are established. No historical-first claim is made for the pieces. The candidate project synthesis is the all-order rough weighted-cycle coefficient ring, the degree-2 port-cancellation explanation, the observer-relative finite Schur-mode carrier, and its direct replacement of unstable microscopic differentiation.

## 10. BRC resolution

REUSE_APPLIED: observer/future-language factorization and information-loss discipline. The Schur amplitudes are labeled signed modes, not positive masses. For future `beta_m` only, the triangular determinant jet safely quotients to `m+1` scale amplitudes; for the full forest jet the richer carrier is retained. The exact witness above forbids collapsing higher-m state to the Basel rough state.

NOT_APPLICABLE: positive-weight recurrent BRC as a substitute for the signed Schur amplitudes.

## Next

1. Derive an analogous finite-port law for unequal subdivision at m=2, retaining the necessary signed cubic ports rather than forcing positive roughness mass.
2. Determine generic minimal dimension of the all-order Schur-mode jet for m>=3.
3. Compare the exact even-scale closure with the closest published weighted subdivision/Schur-decimation formulas before any novelty claim.
4. Keep the zeta/pi identification strictly in the classical compatibility layer.
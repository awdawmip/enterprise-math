# PREFIX-808 — Source-compatible integral weighted grading and exact graded Hilbert resolution

Date: 2026-11-17. Status: **author-side algebraic extension and exact bounded crosscheck**. Original TU/Reeve observer: EM-DIRECT-4660FF. The intermediate cyclic cover, carry image and normal-form filtration: EM-DVR-DEBB5E. This continuation is contributed by the same source-exposed EM-DVR-DEBB5E line; **not an independent Native review or Result admission**. This is the explicitly stated auxiliary Reeve/Kummer algebra, without a native-X6 observer-transfer claim.

## Pinned mathematical dependencies

- [Exact cyclic multiplication and higher-carry image](https://github.com/awdawmip/enterprise-math/blob/04bdc1f2072aae48fa2d9170a98809675a221cb9/research_notes/driver/2026-11-17_prefix808_cyclic_character_multiplication_carry_obstruction.md).
- [Normal-form S-module filtration](https://github.com/awdawmip/enterprise-math/blob/92b39528063e442db55c5fd48b82b1dfe2e39105/research_notes/driver/2026-11-17_prefix808_higher_carry_exact_s_module_filtration.md).
- [Minimal S-free resolution with formal degree-zero normal-form generators](https://github.com/awdawmip/enterprise-math/blob/d1c0a093e2bfde603b5d18467b48129e0eb6a049/research_notes/driver/2026-11-17_prefix808_higher_carry_cokernel_minimal_s_resolution_hilbert_series.md).

## Theorem — actual compatible weighted grading

Let K be any field; let h≥2 and e|d|h, n=d/e, H=h/d. Set

S=K[U_0,U_1,U_2,U_3], A=U_0U_3, B=U_1U_2, I=(A,B),

D_h=S[z_0,z_1]/(z_0^h-A,z_1^h-B).

Let C_d be the subalgebra of total z-degree divisible by d and M_k the character module of total z-degree congruent to ek modulo d, 0≤k<n. Let J_d be the degree-d invariant monomial ideal. Fix c≥1 and put E_{k,c}=M_k/J_d^c M_k.

Equip the *original presentation*, not only an abstract S-module copy, with the positive integral grading

    deg(U_i)=h for i=0,1,2,3;   deg(z_0)=deg(z_1)=2.

The defining relations are homogeneous of degree 2h; C_d, M_k, J_d and E_{k,c} inherit this grading. For each q≥0 define

    r_q=ek+qd,
    N_q=#{(a,b)∈{0,...,h-1}² : a+b=r_q},
    m_q=max(0, ceil((c-q)/H)).

All nonzero terms below have N_q>0 and m_q≥1. Then there is an isomorphism of **graded S-modules**

    E_{k,c} ≅ ⊕_q [S/I^{m_q}](-2r_q)^{N_q},

where the shift convention is that 1 in each summand has degree 2r_q. Consequently its exact weighted Hilbert series is

    Hilb(E_{k,c};t) =
      {Σ_q N_q t^(2r_q) [1-(m_q+1)t^(2hm_q)+m_q t^(2h(m_q+1))]}
      / (1-t^h)^4.                                              (★)

More precisely, its minimal graded S-free resolution 0→F_2→F_1→F_0→E→0 has

    F_0 = ⊕_q S(-2r_q)^{N_q},
    F_1 = ⊕_q S(-2r_q-2hm_q)^{N_q(m_q+1)},
    F_2 = ⊕_q S(-2r_q-2h(m_q+1))^{N_q m_q}.

Equivalently, the graded Betti generating polynomials are

    β_0(t)=Σ_q N_q t^(2r_q),
    β_1(t)=Σ_q N_q(m_q+1)t^(2r_q+2hm_q),
    β_2(t)=Σ_q N_q m_q t^(2r_q+2h(m_q+1)).

These formulas apply in arbitrary characteristic, including characteristic dividing h, d or n. They extend the preceding intrinsic S-coordinate degree-zero-generator series by retaining the true degrees of the monomial generators. A positive integral grading is selected explicitly; it is not asserted to be the unique possible grading.

## Proof

The monic relations in D_h provide a free S-normal-form basis z_0^a z_1^b with 0≤a,b<h. Each normal form is homogeneous of degree 2(a+b) in the stated grading. The C_d-character condition is a+b≡ek mod d, so a+b=ek+qd for q≥0 (since 0≤ek<d).

The pinned exact filtration proof gives the following degree-by-degree membership criterion in the S-span of each such normal monomial: the coefficient ideal of J_d^c M_k is I^{m_q}, where m_q=max(0,ceil((c-q)/H)). All reductions z_0^h=A and z_1^h=B preserve weighted degree. Thus the pinned S-module decomposition is compatible with the homogeneous normal-form generators and becomes the asserted shifted **graded** decomposition.

Both A and B have degree 2h and form a regular sequence of height two. For m≥1, the Hilbert–Burch resolution of S/I^m has generators of the ideal in degree 2hm and its first syzygies in degree 2h(m+1):

    0→S(-2h(m+1))^m→S(-2hm)^(m+1)→S→S/I^m→0.

Its matrices have entries A and B and are minimal at the homogeneous maximal ideal. Shifting by 2r_q and taking a finite direct sum gives F_2, F_1, F_0. As deg(U_i)=h, Hilb(S;t)=1/(1-t^h)^4; the alternating sum yields (★). This is an equality of rational Hilbert series, so it establishes every coefficient, not merely a finite window. QED.

## Worked numerical certificate

At h=d=4, e=1, k=0, c=3, H=1 the nonzero pairs are (N_0,m_0,r_0)=(1,3,0), (N_1,m_1,r_1)=(3,2,4). Hence

    F_0 = S ⊕ S(-8)^3,
    F_1 = S(-24)^13,
    F_2 = S(-32)^9,

    Hilb(E_{0,3};t)=(1+3t^8-13t^24+9t^32)/(1-t^4)^4.

Direct normal-form monomial counts at weighted degrees 0,4,8,12,16,20,24,28,32 are respectively

    1, 4, 13, 32, 65, 116, 176, 236, 296.

They agree with coefficient extraction from (★). Here the original weighted grading reveals a pure first/second syzygy degree pattern that is suppressed when the z-normal-form generators are declared abstractly to have degree zero.

## Independent bounded coefficient test

A separate direct enumeration of monomial normal forms, testing whether each S coefficient is outside I^{m_q}, was compared with coefficients extracted from (★) across **246 parameter configurations**: all 2≤h≤8, all e|d|h, all 0≤k<d/e and c∈{1,2,3}, at degrees 0 through 32 inclusive. All 246 configurations agreed at every degree. Three additional configurations, (4,4,1,0,3), (6,6,2,1,4), and (8,4,1,2,3), agreed through degree 64. The direct membership test is

    U_0^a U_1^b U_2^v U_3^w ∉ I^m  ⇔
    min(a,w)+min(b,v)<m.

The computation used integer arithmetic and directly enumerated all admissible nonnegative exponent quadruples under each weighted degree bound. This checks the grading shifts and the Hilbert series independently of the Hilbert–Burch derivation; universal validity follows from the proof.

## Audit disposition and continuation

The previous report's unshifted Hilbert series is valid for its explicitly declared coordinate grading. The present result supplies the **source-compatible weighted Hilbert series** for the actual z-generators and resolves which grading is used when interpreting graded syzygies. There is no correction to the previous ungraded Betti numbers or S-module multiplicity.

The mathematical claim has **author-side proof + bounded exact verification**. Independent Native review, Source/Activity binding, formal Task closure and parent-goal closure remain separate. The live state/authority of any task or owner has not been inferred from this algebraic note. A genuinely independent reviewer can check the pinned normal-form membership criterion (the load-bearing antecedent) before admitting the graded extension.

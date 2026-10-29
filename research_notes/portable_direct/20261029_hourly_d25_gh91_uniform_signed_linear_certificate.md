# D25/LIFT GH-91 — uniform signed linear source certificate at the reflected root

2026-10-29 / Research logical lane: chatgpt-research-hourly-enterprise-math-20260923. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION and D25/LIFT/JT2 OPEN. Historical Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. This is not a native CLAIM, Source checkpoint, review or GH-3 proof.

## Typed sources and dependencies

For prime p=4d+3 >=7, work in k=F_p, theta=z*d/dz. Keep the original S=sum_(i=0)^d c_i z^i, c_0=1, c_(i+1)/c_i=(4i+1)^3/[(4i+2)(4i+3)(4i+4)] distinct from the reflected U=sum_(j=0)^d h_j z^j, h_0=1, h_(j+1)/h_j=(4j+3)^3/[(4j+4)(4j+5)(4j+6)]. All displayed coefficient denominators are p-units. Define T=(8theta+1)S (the true GH-3 target), H=(8theta+5)U (the reflected Laurent obstruction, not a Hasse invariant), and J=theta H.

Use GH-84's signed ordered concomitant:
    
    B(X,Y)=(1-z)[Y theta^2 X-(theta Y)(theta X)+(theta^2 Y)X]
      +(z-3)Y theta X/4+(3-5z)(theta Y)X/4+(2-7z)XY/16.

Set B=B(S,U), V=B(S,theta U) (GH-90). The exact reflected equation from GH-84 is
    
    L_+U=0,  L_+=(1-z)theta^3+(3-9z)theta^2/4
                    +(2-27z)theta/16-27z/64.

GH-87 provides the complete auxiliary polynomial identity
    
    (1-z)[2U theta^2U-(theta U)^2]
       +(1-3z)U theta U/2 -9z U^2/16=0.

The separate author-derived GH-83 assertion H(9)=0 depends on the not-yet-independently-reviewed CM proofs GH-74/75. The next global identity needs neither this assertion nor any special CM arithmetic.

## GH-91A: global linear syzygy

For arbitrary S and any U satisfying L_+U=0, the following complete polynomial identity holds over k[z]:

    64V+40B
      =(z-1)J T
       +[2(z+3)J+(z+15)U/8] S
       +H[8(1-z)theta^2S+2(z-3)theta S+(15z+5)S/8].     (91.1)

Proof: expand both ordered concomitants with U_j=theta^j U and X_j=theta^j S. The coefficient of X_2 on the left equals 8(1-z)(8U_1+5U_0)=8(1-z)H. Substitute (1-z)U_3=-(3-9z)U_2/4-(2-27z)U_1/16+27zU_0/64 from L_+U=0. Collect X_1,X_0; rewriting 8U_1+5U_0=H and 8U_2+5U_1=J gives (91.1) with no denominator U, H or J. A separate executed SymPy check performed this symbolic substitution over Q(z) with independent indeterminates. Multiplication by the differential-equation coefficients proves a polynomial identity and p>=7 leaves every displayed 2-power denominator invertible.

At the target z=9, conditional on the distinct reflected-root result H(9)=0, (91.1) becomes

    8J(9)T(9)=64V(9)+40B(9)-[24J(9)+3U(9)]S(9).       (91.2)

This is linear in the SIGNED target T, unlike the quadratic GH-88 certificate. It also remains valid when U(9)=0.

## GH-91B: root simplicity and complete finite-source certificate

Assume H(9)=0. Then theta U(9)=-5U(9)/8 and theta^2U(9)=J(9)/8+25U(9)/64. Substitute into the GH-87 polynomial relation at z=9 to obtain

    U(9)[32J(9)+U(9)]=0.                                  (91.3)

If U(9)!=0, J(9)=-U(9)/32 !=0. If U(9)=0, H(9)=0 also forces theta U(9)=0, and theta^2U(9)!=0: at the ordinary point 9!=0,1 the degree-d (<p) polynomial solution L_+U=0 cannot have three initial zero jets without being identically zero, contrary to U(0)=1. Then J(9)=8theta^2U(9)!=0. Hence every reflected root at z=9 is simple:

    H(9)=0  ==>  J(9)!=0.                                 (91.4)

The same reasoning gives a single NECESSARY AND SUFFICIENT target condition for both U fibers:

    T(9)=0  <==>  W(9)=[24J(9)+3U(9)]S(9),   W=64V+40B.  (91.5)

GH-84's original finite B source and GH-90's V source combine without collapsing the two contribution labels:

    W(z)=5
      +64 sum_(i,j=0)^d [c_i h_j (j+3/4)^3/(i+j+1)] z^(i+j+1)
      +c_d sum_(j=0)^d [(8j+5)h_j/(d+1+j)] z^(d+1+j).     (91.6)

Every sum denominator lies in [1,2d+1]=(p-1)/2, so (91.6) is finite and exact. When U(9)!=0, J=-U/32, and (91.5) becomes 4W(9)=9U(9)S(9). When U(9)=0, put E=theta^2U(9)!=0; then J=8E, B(9)=-JS(9), and (91.5) is exactly the GH-90 certificate V(9)=8E S(9). This uniform signed port replaces the earlier split certificates without changing their original statements.

The remaining GH-3 all-prime proof obligation is an INDEPENDENT evaluation of (91.6) at z=9 matching the right-hand side of (91.5). Using T(9)=0 to evaluate that sum would be circular. GH-83 H(9)=0 and GH-74/75 CM remain author-level dependencies.

## Execution and observer fidelity

An actually executed standard-library exact modular checker constructed complete S,U,B,V,H,J,T, verified L_+U=0, GH-87, all polynomial coefficients of (91.1), and the independent convolution (91.6) for all 130 primes p<1600, p=3 mod4. It separately checked (91.2)-(91.5) and root simplicity for all 618 primes p<10000 in the same residue class, split into 311 nonzero-U and 307 double-root-U fibers. The sampled H(9)=0 and T(9)=0 are finite observations, not universal proofs. Executed SymPy symbolic check additionally verified the universal substitution. The complete author checker, symbolic script, logs and digests are in the accompanying conversation research package. Formal native experimentation and independent mathematical audit remain separate.

BRC: COMPOSE_APPLIED; typed observer has p, z, the independent c/h coefficient sources and their ordering, signed theta jets, U/J pivot and future readout T. The previous square-root sign information loss is removed. This external finite-field algebra is not a native Heartbeat World X6 chart; no unproved P000 native transfer or three-dimensional-slice promotion is asserted. Preserve frozen source and source isolation.

Next exact scientific step: evaluate W(9) independently via CM, finite character/Jacobi sums, or finite WZ to prove or refute (91.5) without substituting T(9)=0. Retain GH-83 first Laurent pole B_0L, GH-20/21, W/S, Hasse ports, R23/R36 and native p=373. Status at this author run: Gateway v0.6.11, Research authority=false, executor binding=false, active native control quota 5/5; formal continuation/claim/open/Source checkpoint pending control issue #1558. Preserve old session, claim, requests and unpublished staging; a GitHub proof is PORTABLE_ONLY and not an admitted predecessor checkpoint.
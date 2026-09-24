# D25 LIFT — period residual glues into one finite-tail jet and adds no new first-order constraint

Status: PROVED_STRICT_PERIOD_GLUE / PROVED_FIRST_ORDER_PERIOD_EXTENSION_NO_NEW_CONSTRAINT / PORTABLE_D25_MATH_ONLY / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed frontier

Consume the canonical cutoff bridge

    Z_T = [a_parent Psi-1]/p
          + a_parent H_1^{<=m}/6
          + Psi F_2^{<=2m}/72                 (mod p),

and the exact three-layer transport for

    T_k(a)=(-m+a)_k(-2m+2a)_k/(k!)^2 * 2^{-k},
    q0_k=T_k(0), q1_k=T'_k(0)/6, q2_k=T''_k(0)/72,

    J_{k+1}=M_k J_k,
    M_k=[[r0,0,0],[r1/6,r0,0],[r2/36,r1/6,r0]],

    r0=(k-m)(k-2m)/(2(k+1)^2),
    r1=(3k-4m)/(2(k+1)^2),
    r2=1/(k+1)^2.

The preceding checkpoint proved that the forced q2 adjoint equation

    r0 z_{k+1}-z_k=C

has no uniform rational solution for nonzero constant C and identified its missing carrier as a hypergeometric partial period. This unit performs the requested zero-edge gluing exactly.

## 1. One finite-tail quotient glues both regular sectors

For 0<=k<=2m define the finite tail

    P_k(a)=sum_{j=k}^{2m} T_j(a)

and its quotient

    Z_k(a)=P_k(a)/T_k(a).

As a meromorphic identity in a,

    BOXED: R_k(a) Z_{k+1}(a)-Z_k(a)=-1,             (1)

where T_{k+1}(a)=R_k(a)T_k(a). This is just P_k=T_k+P_{k+1}.

The apparent singularity of Z_k at a=0 for m<k<=2m is removable. In that range every T_j(a), k<=j<=2m, has exactly one zero at a=0, hence

    BOXED:
    Z_k(0)= [sum_{j=k}^{2m} q1_j]/q1_k,             m<k<=2m.    (2)

For 0<=k<=m, only the low stratum survives at a=0, so

    BOXED:
    Z_k(0)= [sum_{j=k}^{m} q0_j]/q0_k.              (3)

Thus the two sectorwise period quotients from variation of constants are not independent new coordinates. They are the two a=0 charts of the single source-faithful finite-tail quotient Z_k(a). In particular Z_m(0)=1 and Z_{2m}(a)=1 identically. The typed zero edges remain visible; no denominator is inverted across a vanished source port.

At the base k=0, because T_0(a)=1,

    BOXED:
    Z_0(0)=F_0,
    Z'_0(0)=F_1,
    Z''_0(0)=F_2^{<=2m}.                             (4)

Hence the terminal period masses are already carried by the existing cutoff jet. F_1 is not a new free coordinate either: the canonical parent coordinate satisfies a_parent=F_0/p+F_1/6.

## 2. The full q2 period extension is exactly the 2-jet of Z

Differentiate (1) at a=0. Writing Z,Z',Z'' for the derivatives at zero gives

    r0 Z_{k+1}-Z_k=-1,
    r0 Z'_{k+1}+r1 Z_{k+1}-Z'_k=0,
    r0 Z''_{k+1}+2r1 Z'_{k+1}+2r2 Z_{k+1}-Z''_k=0.

For any constant C define the adjoint column

    Lambda_k^Z(C)=(-C Z''_k/72, -C Z'_k/6, -C Z_k)^T.

Direct substitution into the triangular transport gives the exact identity

    BOXED:
    M_k^T Lambda_{k+1}^Z(C)-Lambda_k^Z(C)=(0,0,C)^T.  (5)

Therefore the non-rational scalar period required by the q2 equation does not generate an uncontrolled tower when the provenance-preserving q0/q1 couplings are retained: its first two parameter derivatives supply exactly the lower adjoint coordinates needed by the same three-layer transport.

For the live cutoff take C=Psi. Summing (5) from k=0 to 2m-1 and adding the explicit endpoint k=2m gives

    Psi sum_{k=0}^{2m} q2_k = Psi F_2^{<=2m}/72.    (6)

At k=0 the boundary vector reads the already-owned jet (F_0,F_1,F_2^{<=2m}); at k=2m, Z=1 and Z'=Z''=0. Equation (6) is exact but is only a reconstruction of the existing cutoff term, not a new LIFT relation.

## 3. The weighted q1 cutoff has the analogous one-jet tail

For 0<=k<=m define

    Q_k(a)=sum_{j=k}^{m}(12j+1)T_j(a),
    W_k(a)=Q_k(a)/T_k(a).

Then

    R_k(a)W_{k+1}(a)-W_k(a)=-(12k+1).              (7)

At k=0,

    W_0(0)=Psi,
    W'_0(0)=H_1^{<=m},                               (8)

while W_m(a)=12m+1 is constant. For any constant A,

    Lambda_k^W(A)=(-A W'_k/6, -A W_k, 0)^T

satisfies

    BOXED:
    M_k^T Lambda_{k+1}^W(A)-Lambda_k^W(A)
      =(0,A(12k+1),0)^T                              (9)

for k<m. With A=a_parent, summing (9) and retaining the explicit k=m endpoint reconstructs exactly

    a_parent sum_{k=0}^{m}(12k+1)q1_k
      = a_parent H_1^{<=m}/6.                        (10)

Again the period extension closes onto an already-owned cutoff boundary jet and yields no additional equation.

## 4. Consequence: the first-order period extension is lossless but non-reductive

Combining (5) and (9) proves the precise fate of the residual from the previous checkpoint:

- the q2 hypergeometric period is real and cannot be replaced by a rational certificate;
- after adjoining it source-faithfully, the m and 2m sector charts glue into one finite-tail quotient Z_k(a);
- its needed 0/1/2-jet boundary data are exactly F_0,F_1,F_2^{<=2m};
- the weighted q1 companion similarly closes onto Psi,H_1^{<=m};
- no new independent period coordinate remains after the typed jet/provenance is kept.

But this also gives a strict negative conclusion: the entire first-order period-extended adjoint merely reconstructs the two derivative terms already present in Z_T. It supplies no relation for the separate divided product digit [a_parent Psi-1]/p and no identity with R_p. Hence it cannot close JT2/LIFT.

So the first-order adjoint branch is now exhausted in both forms: rational certificates are impossible, and the minimal non-rational period extension is exact but tautological at the target observer. The next information-gain step must be a genuinely higher-order contiguous/WZ relation or a source-level Frobenius identity that couples the divided product digit to the cutoff endpoint.

## 5. BRC information audit

Population: the single finite-Gauss family T_k(a), its 0/1/2 jet colors, finite tails, and typed zero edges m and 2m.

Observer: the D25 divided second digit modulo p.

Safe quotient: the two sectorwise period variables may be replaced by the single finite-tail quotient Z_k(a) with its removable-edge charts, because (2)-(4) prove exact source equivalence.

Preserved: derivative order, edge identity, F_0,F_1,F_2^{<=2m}, Psi,H_1^{<=m}, a_parent and the separate divided product digit.

Forbidden compression: do not call the period rational; do not delete the m/2m edges; do not infer LIFT from the tail closure; do not identify the remaining divided product digit with a Frobenius coordinate without an exact bridge.

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

# PREFIX-614-R2 — Seven-state minimal linear carrier for the four-sparse BRC probe

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR-SIDE EXACT PROOF AND EXECUTED ORIGINAL 48-PHASE SYMPY CERTIFICATE; independent Driver review pending.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Input is PREFIX-613's nonnegative d=e4+e11+e14+e32. Observer is original phase-3 scalar; the full original 48-phase sum state can also be reconstructed. The 96 native ports and 576 tagged actions remain upstream provenance; this is a proved observer-specific linear quotient only.

## Theorem 614.1: exact seven-dimensional invariant reachable space after two gates

For the original 48x48 phase-sum Q(g) for six-axis weights (1,1,1,1,0,0), g>=0, set

    A=Q(0), D=Q(1)-Q(0), Q(g)=A+gD, D^2=0.

Define the original 48-phase basis columns as

    E=[A^2 d, D A d, A D d, A^3 d, A^2 D d, A^4 d, A^3 D d].

They are all constructed from the frozen Q, not guessed latent coordinates. The explicit seven-row minor E[(2,3,4,5,16,17,26),:] has determinant -16384. Thus E has rank seven, and if K=E[rows,:]^-1 I48[rows,:], then KE=I7. Define exact 7x7 integer matrices T0=K A E and T1=K D E. In the *complete original 48-phase state*, the following exact identities hold:

    A E = E T0,   D E = E T1,
    Q(g) E = E (T0+g T1)  for every g>=0.

Therefore the two-gate tail for any first gate a, second gate b and unknown positive probe scale lambda has coordinates

    Q(b) Q(a) (lambda d) = E * lambda * (1,b,a,0,0,0,0)^T.

The potentially missing g1*g2 term vanishes because D^2=0. Every later nonnegative gate q updates the exact seven-dimensional state c to (T0+q T1)c, and all 48 phase differences are recovered exactly by E c. Only 13 entries in T0 and four in T1 are nonzero.

## Theorem 614.2: exact minimal dimension in the linear future phase-3 observer class

The first three columns A^2d, DAd, ADd span the linear space of all possible two-gate tails as a,b range over legal {0,1} gate inputs (use differences between gate-word outputs). Closing this span under the two legal gate matrices Q(0), Q(1), equivalently under A,D, yields all seven E columns. The exact linear reachable space therefore has dimension seven.

The phase-3 sensor row on E is

    h=e3^T E=(3,1,0,14,0,28,0).

An explicit future-output observer certificate is the seven-row matrix

    O = [h; hT0; hT1; hT0^2; hT1T0; hT0^3; hT1T0^2]

whose determinant equals -2097152 = -2^21. Every row can be evaluated as a linear combination of legal future gate-word outputs, since T1=T(1)-T(0). The reachable-to-future-observation Hankel pairing therefore has rank seven. No exact *common linear finite-state representation* of all phase-3 traces from arbitrary initial two gates and subsequent nonnegative gate words can use fewer than seven state coordinates. The seven-dimensional E,T0,T1,h representation attains this lower bound. This linear-interface result does not assert minimality among discontinuous/nonlinear encodings or equivalence for original labeled 96-port paths.

## Exact transition certificate

Writing E1,...,E7 for these basis columns, the complete column laws are:

    A E1=E4, A E2=E3, A E3=E5, A E4=E6, A E5=E7;
    A E6=8E1+12E2-12E3-4E4+4E5+2E6-3E7;
    A E7=12E2;
    D E1=2E2, D E4=4E2, D E6=12E2, D E7=4E2;
    D E2=D E3=D E5=0.

All are exact vector equalities in the original 48-dimensional coordinates, and the resulting integer matrices are recorded in the accompanying results JSON. Negative coefficients are permitted in this exact observer-specific coordinate representation; no positive 7-state labeled branch realization is claimed.

## Executed exact checks and next research unit

The independent Python/SymPy checker builds all 48 original STAR phases and Q from frozen formulas. It verifies Q(g)E=E(T0+gT1) as a symbolic matrix identity; the -16384 basis minor; -2097152 observability minor; reachable closure; and 48-coordinate reconstruction over nonnegative integer and rational gate words for three probe scales. Actual checks: 6 exact two-gate initializations; 60 exact phase-3 readings; 2,880 original 48-state coordinate equalities; all executed assertions passed. The all-length theorem is proved by the exact intertwining identities and rank certificates. Driver mathematical review and formal Native Result remain pending.

Method reuse: original native STAR phase-sum transport, PREFIX-608 excitation, PREFIX-612 calibration, PREFIX-613 sparse probe; exact 7D restriction COMPOSE_APPLIED with retained 48-dimensional reconstruction.

Next unit: benchmark total input-preparation, seven-state step, integer bit-length and original output recovery versus the generic 16-state and full 48-state methods. Analyze any required repair coordinates for 96-port labeled path histories.

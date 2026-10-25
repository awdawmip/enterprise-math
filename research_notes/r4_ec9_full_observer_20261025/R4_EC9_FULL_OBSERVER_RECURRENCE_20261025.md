# R4-EC9 — Twelve-order Laurent closure for all positive affine BRC source channels

Date: 2026-10-25. Status: **author-side exact auxiliary-model theorem; NOT formally accepted by Enterprise Math**. Parent: R4-EC8 (immutable commit 97b2738524622d3b4bdafabfa50928746fdf06da). Scope: positive ordered binary BRC only. Local author provenance: EM-LOCAL-EC9A, not a service-issued research identity. Current native dispatch yielded CONTROL_QUOTA; no active Owner/CLAIM authorization was obtained.

## Exact question and state model

Can all six coarse outputs (q, contains_00) retain *the full affine effect* and be evaluated by one finite-order, time-homogeneous scalar Laurent recurrence? If so, determine its exact minimum *common scalar order* when the two affine signs are observed separately, with coefficients in Q(z).

Each ordered binary word has weight +1, initial (q,r,epsilon,k)=(0,0,+1,0). q has values 0,1,2. For q=0: input 0 -> (q',eta,b)=(2,-1,-1), input 1 -> (2,+1,-1). For q=1: input 0 -> (0,-1,-1), input 1 -> (0,+1,-1). For q=2: input 0 -> (1,+1,+1), input 1 -> (2,+1,-1). Affine composition is (epsilon',k')=(eta epsilon,eta k+b). The source monitor r=0 means no 00, last input not zero; r=1 means no 00, last input zero; r=2 means 00 has occurred. On input 0: 0->1, 1->2, 2->2; on input 1: 0->0, 1->0, 2->2. Thus q,r have 7 reachable combinations with 2 orientation signs, i.e. 14 fine channels.

Define t=epsilon*k. For input bit a, t'-t=epsilon*(1-2a), so Laurent variable z grades t. Define F_{q,c,e}(x,z)=sum_{n>=0,t} count(n,q,c,e,t) x^n z^t, where c=C means r!=2, c=B means r=2, and e in {+1,-1}. There are six coarse output types (q,c) and twelve oriented Laurent series.

All formal divisions below are legal in Q[z,z^-1][[x]] because denominators have constant x-coefficient 1. No negative BRC branch weights or complex-amplitude cancellation is used.

## Theorem 1 — Closed rational generating functions

Write S=z+z^-1,

D=(1+x^2)(1-xS+2x^4-x^6),
Q=(1-xS)(1+x^2-x^3 S),
P=D Q.

First derive four clean fine-channel series U_e,V_e,W_e,Y_e for (q,r)=(0,0),(1,1),(2,0),(2,1). Exact incoming-edge decomposition gives

    U_e = [e=+1] + x z^(-e) V_e;
    V_e = x z^e W_e;
    W_e = x z^(-e) (U_e+W_e+Y_e);
    Y_e = x z^(-e) U_{-e}.

Set A=1-x/z and B=1-x(1+x^2)z. Elimination yields

    U_+ = AB/D;                     U_- = x^4 z^2 A/D;
    W_+ = (AB-D)/(x^2 D);          W_- = x^2 z^2 A/D;
    V_e = x z^e W_e;
    Y_+ = x^5 z A/D;               Y_- = x z AB/D.

The apparent x^-2 in W_+ is removable because AB-D is divisible by x^2. Coarse clean outputs are C_{0,e}=U_e, C_{1,e}=V_e, C_{2,e}=W_e+Y_e.

Now write H_{q,e} for dirty paths (r=2). Since only a second consecutive zero can enter dirty provenance from clean provenance, their *complete* incoming equations are

    H_{0,e}=x z^(-e)(H_{1,e}+H_{1,-e}+V_{-e});
    H_{1,e}=x z^e(H_{2,e}+Y_e);
    H_{2,e}=x z^(-e)(H_{0,e}+H_{0,-e}+H_{2,e}).

In the order (0,+),(0,-),(1,+),(1,-),(2,+),(2,-), let the coefficients of the H variables define the explicit 6x6 matrix M and let the remaining clean terms define forcing vector f. Direct algebra gives det(I-M)=Q. Hence H=(I-M)^(-1) f, and every H_{q,e} has denominator dividing DQ. Every clean C_{q,e} also has denominator dividing P. Thus for all twelve complete-output series there exist explicitly recoverable Laurent polynomials N_{q,c,e} with

    F_{q,c,e}(x,z)=N_{q,c,e}(x,z)/P(x,z).

This is an all-depth exact identity. The attached local research package includes the full per-channel numerator coefficient table and checks the displayed incoming system symbolically; the equations above are already sufficient to reproduce the numerator table.

## Theorem 2 — Uniform exact homogeneous Laurent recurrence

Let p_j(z)=[x^j]P(x,z) for j=0,...,12, with p_0=1. For any one of the twelve series let f_n(z)=[x^n]F(x,z), with f_n=0 for n<0. Multiplying F=N/P gives the exact coefficient law

    sum_{j=0}^{12} p_j(z) f_{n-j}(z)=[x^n]N(x,z).

Each of the twelve N polynomials has x-degree at most 12 (equivalently, this follows by substituting the finite rational solution; the exact symbolic verifier checks all of them). Therefore for *every n>=13 and every integer grade t*, all twelve channels obey the same homogeneous order-12 recurrence

    sum_{j=0}^{12} p_j(z) f_{n-j}(z)=0.

Multiplication by z shifts t; the resulting coefficients are exact integers. Intermediate negative recurrence coefficients arise from algebraic elimination and never represent cancellation between positive edge masses.

## Theorem 3 — The common scalar order cannot be reduced below 12

For the dirty q=2,e=+ component, elimination gives H_{2,+}=N_*/P, where

    N_* = x^4 (xz-1)^2 W / z^3,
    W = x^4 z - x^3 z^4 - 2x^3 z^2 + x^2 z^3
        - x^2 z - x + 2z^3 + z.

To prove N_* and P are coprime over Q(z)[x], specialize z=2. After multiplying by 8, the exact integer coefficient arrays in descending powers of x are

    8 P(x,2):
    [-50,40,42,-20,100,-225,174,-225,224,-100,66,-40,8]

    8 N_*(x,2):
    [8,-104,122,-52,82,-73,18,0,0,0,0].

Both leading coefficients stay nonzero modulo the prime 101. Euclidean division over F_101[x] gives successive remainder degrees

    9,8,7,6,5,4,3,2,1,0, then zero.

Hence the specialized modular gcd is 1. Since the specialized degrees of P (12) and N_* (10) do not drop, their Sylvester resultant is nonzero at z=2; therefore the original resultant in Q(z) cannot vanish identically. Thus gcd(N_*,P)=1 in Q(z)[x].

A rational generating series in reduced form with denominator x-degree 12 cannot satisfy any eventually homogeneous scalar linear recurrence of constant coefficients in Q(z) and order smaller than 12. The dirty q2 positive-orientation component supplies the lower bound 12; Theorem 2 supplies the common upper bound 12.

**Exact minimum common homogeneous scalar Laurent recurrence order: 12.**

This is not a bound on the number of BRC internal *control states*, not a proof about arbitrary vector/matrix recurrence, and not a solution to the effect-blind-transition six-versus-seven-state representation question.

## Arithmetic, verification, and observational scope

The complete author-side Python checker used exact SymPy rational-function algebra for all clean equations, dirty determinant and inversion, twelve Laurent polynomial numerators, and gcd over F_101. Its independent arbitrary-precision integer DP of the original 14 fine channels checked all coefficient identities through depth 80 with 36,251 exact comparisons. A separate C++17/Boost multiprecision verifier constructed P from its four displayed factors, independently advanced the original 14-state machine, exhaustively checked 8,191 raw binary words at depths 0..12, and checked all homogeneous recurrence channels at depths 13..70 in 26,912 coefficient comparisons. Both author-side executions passed; full exact locally executed sources and structured report are bundled in EM_R4_EC9_TWELVE_ORDER_FULL_CHANNELS_20261025.zip.

Reproducible checkpoints at effect (epsilon,k)=(+1,0):
n=10 clean q2=5, dirty q2=49;
n=20 clean q2=463, dirty q2=43307;
n=30 clean q2=47685, dirty q2=37396297.

Pinned rule/source input: Global-Knowledge main@6a246ed94efb5ed584cefd4b0720171067bd94c2; P000 projection verified against original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, status ACTIVE_LOCKED; ACTIVE worldview read. Enterprise Math current source main@1ee17308b6c80f1481fa571676d3c383d4003f39, portable research protocol at docs/PORTABLE_RESEARCH_PROTOCOL.md. Parent R4-EC8 immutable paper at 97b2738524622d3b4bdafabfa50928746fdf06da.

BRC reuse: COMPOSE_APPLIED to the existing exact clean Laurent carrier, extending it by typed absorbing dirty provenance and retaining the complete affine effect. Observer and allowed future: any finite binary suffix and the six terminal q/provenance channels with full effect. Auxiliary t=epsilon*k is not Enterprise native X6, a complete three-dimensional research slice, or calibrated heartbeat time. Original R193 port/time mapping, native X6 execution, formal Result, independent Driver review, and physics correspondence remain pending. Publication is not acceptance.

## Next exact unit: R4-EC10

Study the *smallest typed transfer realization* of the twelve oriented Laurent series and carefully distinguish vector-state rank from minimal scalar order. For the original effect-blind, time-homogeneous, positive weighted six-state candidate (with arbitrary internal encoding and effect-conditioned deterministic terminal decoder), either construct a valid realization or find an invariant that excludes all such encodings. Keep original port and time questions independent.
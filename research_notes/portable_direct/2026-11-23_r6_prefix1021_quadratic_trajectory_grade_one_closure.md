# PREFIX-1021: Quadratic finite-horizon observer rank and graded k=1 BRC closure

2026-11-23, Asia/Shanghai. AUTHOR_EXACT_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED.

Scientific inputs are frozen P000 V5 at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json, the signed candidate Stage46 X6 BRC coin W=J_12-6I_12, and the two-way absorbed Link {0,e1}. Previous exact source: PREFIX-1020 (finite-horizon oriented-flux rank 2H) and PREFIX-1014 (fixed-seed exactly one negative direction port masses). This is an internal candidate-model theorem, with no P000, Result, admission, or owner change.

Definitions. Cells x are in a chosen signed X6 chart Z^6, and h is one of twelve incoming signed native ports. The outgoing integer amplitude for d is sum_h (1-6[h=d])v(x,h); the next joint fibre is (x+d,-d). Let U be the unabsorbed update, E the orthogonal selection of forbidden outgoing fibres (0,+e1) and (e1,-e1), T=(I-EE*)U, and C=E*U. For finitely supported real packets set q_t(v)=||CT^t v||^2 and N_t(v)=||T^t v||^2. Exact BRC Parseval gives N_(t+1)=36N_t-q_t.

## A. Sharp C^1 dimension for the complete all-grade squared-norm trajectory

For every integer H>=1, the simultaneous one-shot observer v |-> (N_0(v),...,N_H(v)) has differential rank H+1 at an explicit integer finite-support packet; these H+1 quadratic polynomials are algebraically independent. Any factorization of this observer through d real C^1 scalar coordinates, with a C^1 decoder, therefore requires d>=H+1. The lower bound is attained (for this declared one-shot readout) by N_0,q_0,...,q_(H-1). When N_0 is separately supplied, the H losses are locally independent and suffice to reconstruct all later N_t.

Proof. From PREFIX-1020, for s=0,...,H-1 the 2H unit packets w_(+,s)=delta_(s e2,-e1) and w_(-,s)=delta_(e1+s e2,+e1) have a square oriented-flux observation matrix B_H with determinant +1, due to identity diagonal 2x2 blocks and zero blocks for t<s. All unit fibres are distinct. Choose a further unit packet u=delta_((3H+3)e2,-e1) disjoint from them. It is farther than H steps from both Link crossing opportunities, so CT^t u=0 for 0<=t<H. Set v=sum_i c_i w_i+a u and y=B_H c. Then q_t=y_(t,+)^2+y_(t,-)^2 and N_0=||B_H^(-1)y||^2+a^2. On the real affine chart y_(t,-)=0, at a=1 and y_(t,+)=1 for every t, the Jacobian of (N_0,q_0,...,q_(H-1)) with columns (a,y_(0,+),...,y_(H-1,+)) has determinant 2^(H+1), since dq_t/dy_(s,+)=2 delta_(ts), dq_t/da=0, and dN_0/da=2. The invertible triangular transformation N_(t+1)=36N_t-q_t multiplies the determinant by (-1)^H. Thus

    det [d(N_0,...,N_H)/d(a,y_(0,+),...,y_(H-1,+))] = (-1)^H 2^(H+1).

Because B_H is integer-unimodular the selected v has integer coefficients. Nonzero determinant gives an open set of output values and excludes every polynomial relation among N_0,...,N_H. A C^1 factorization through dimension d has Jacobian rank at most d; hence d>=H+1. This is a lower bound for smooth one-shot future **trajectories on arbitrary all-grade finite packets**, not for discontinuous codes, bit count, a dynamically closed Markov state, or the deterministic single-seed family.

## B. Exact causal two-block closure for the frozen exactly-one-negative-step family

Partition the same absorbed signed BRC step by actual outgoing native direction: A=T_+ contains only the six +e_i directions (including the positive-direction Link mask), B=T_- contains only six -e_i directions (including the negative-direction Link mask). The signed integer coin weights are unchanged. Let v_(n,k) retain the exact count k of negative *directions* (not negative amplitudes), with v_(n,k)=0 for k<0.

For every n,k>=0,

    v_(n+1,k) = A v_(n,k)+B v_(n,k-1);
    ||v_(n+1,k)||^2 = ||A v_(n,k)||^2+||B v_(n,k-1)||^2.

Proof. A positive outgoing step preserves k and has negative incoming port -e_i; a negative outgoing step raises k by one and has positive incoming port +e_i. The two summands therefore occupy disjoint port-sign fibres. This proves both the exact amplitude update and the orthogonal sum-of-squares formula, while retaining all signed cancellation within each Cell–port–grade fibre.

For the frozen grade-zero seed e=delta_(0,-e1), the exact solution for every n>=0 is

    v_(n,0)=A^n e;
    v_(n,1)=sum_(s=0)^(n-1) A^(n-1-s) B A^s e.

This follows by substituting the first identity into the k=1 recursion and induction. Thus (v_(n,0),v_(n,1)) is an exact forward-closed state for all subsequent grade-one Cell–port observations, with block update [[A,0],[B,A]]. The grade-zero forcing Bv_(n,0) is determined from the original seed and n; the block system is a sufficient, not demonstrated minimal, representation. A naive grade-one-only recurrence multiplying the grade-one norm by 36 would omit this forcing.

## Executed exact checks

A standalone Python/SymPy checker implemented the native twelve named ports, W(h,d)=1-6[h=d], both forbidden channels, B_H, and exact packet propagation. For H=1,2,3,4 it checked det B_H=1, constructed all-integer packets with q_t=1 across the respective H steps, and verified full symbolic Jacobian determinants -4,+8,-16,+32 and every predicted N_t. A second direct DP retaining (Cell,incoming port,k) was compared, fibre by fibre, against the independent two-block A/B recursion for n=0,...,8. Exact k=1 norm numerators for n=1,...,8:

    30, 1050, 2555, 35010, 761040, 16787520, 386364960, 9330533460.

At n=5 the 761040 integer agrees with PREFIX-1013/1014. No floating arithmetic was used. The two general results are proven above for every H or n respectively; numerical and symbolic checking spans only the stated finite ranges.

Reproducer: PREFIX1021_R6_GRADED_QUADRATIC_CHECK.py. Certificate: PREFIX1021_R6_EXACT_RESULTS.json.

## Next open mathematical questions

For the original fixed seed and k=1, find a smaller future-closed observer for the four exact squared port-mass classes by applying the forced A/B decomposition and retaining all relevant cross-Cell/port interference. Compare its reachable-variation rank against the unrestricted all-grade H+1 bound; no restriction theorem has been proved yet. Investigate a finite collision/A_6 representation for the future k=1 mass update. The parent B_fix,odd(32) in {19,20} remains open.

Historical provenance: PREFIX-1020 and R6 contributor EM-DIRECT-FBEA5D, Activity RA-3FB2D033BE6048D8712FF056. Historical public IDs are not present-session execution capabilities. Research artifact publication, Activity association, native CLAIM and independent mathematical Review have distinct status.

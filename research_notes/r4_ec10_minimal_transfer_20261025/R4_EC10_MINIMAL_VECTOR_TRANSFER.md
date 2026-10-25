# R4-EC10 — Exact minimal vector-transfer dimension for full affine BRC source observations

**Date:** 2026-10-25. **Scope:** ordered, positive-unit-mass, binary affine BRC *auxiliary model*, not native Heartbeat X6. **Status:** author-side exact proof and locally cross-checked computation, neither canonical Result nor independent Driver acceptance. **Parent:** R4-EC9 at Git commit 999fd51c2bcd3ad3646fecbff2bbc3700c7a773b. **Identity:** EM-LOCAL-R4-EC10-A (self-labelled local author, not service-issued).

## Exact finite-state input and observer

The fine states are (q,r,e), with q=0,1,2; source monitor r=0 meaning no 00, last bit nonzero/empty; r=1 meaning no 00, last bit 0; r=2 meaning already contains 00; orientation e=+1 or -1. Reachable (q,r) pairs are (0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2), hence 14 oriented fine states. The initial state is (0,0,+).

For input a=0 or 1, use the q-dependent edge triple (q',eta,b):
- q=0: 0 -> (2,-1,-1), 1 -> (2,+1,-1).
- q=1: 0 -> (0,-1,-1), 1 -> (0,+1,-1).
- q=2: 0 -> (1,+1,+1), 1 -> (2,+1,-1).

Update r by r'=2 if already 2; else r'=0 on 1, and r'=1 if prior r=0 on 0, r'=2 if prior r=1 on 0. Affine effect updates (e',k')=(eta*e, eta*k+b). Define t=e*k, so t'=t+e'*b. The 14-by-14 matrix T(z) over K=Q(z) assigns each edge the monomial z^(e'*b), summing coincident edges. The initial column v has unit mass at (0,0,+). The 12-by-14 observer C sums fine states with the same (q,c,e), with c=0 if r!=2 and c=1 if r=2. Let y_n=C T(z)^n v (a 12-component Laurent-polynomial vector) for n>=0. This observer retains the full affine effect because the grade t and orientation e determine k=e*t.

The variable z is a formal count grade, not an X6 coordinate. Word length n is an ordered operation count, not a physical heartbeat-time calibration.

## Theorem A: from the actual n=0 initial state, the minimum joint K-linear transfer dimension is exactly 13

Consider all time-homogeneous realizations y_n=D A^n b over K=Q(z), with constant A of dimension d and all 12 outputs reproduced for every n>=0. Then **d_min=13**.

**Upper bound certificate.** Put S=z+z^(-1) and use the R4-EC9 polynomial

P(x,z) = (1+x^2)(1-xS+2x^4-x^6)(1-xS)(1+x^2-x^3S)
       = sum_{j=0}^{12} p_j(z)x^j, with p_0=1.

The exact 14-vector Laurent identity is

sum_{j=0}^{12} p_j(z) T(z)^(13-j) v = 0.

This identity is checked coefficient-by-coefficient symbolically, using the explicit transition table and polynomial factors above (see exact verifier). Define R(lambda)=lambda^13 P(lambda^(-1)). The displayed identity is R(T)v=0. Thus the orbit Krylov subspace V=span_K(v,Tv,...,T^12v) is T-invariant and has dimension at most 13. Restricting T and C to V gives one 13-dimensional time-homogeneous realization. In the ordered Krylov basis e_j=T^j v, j=0..12, the transition obeys A e_j=e_(j+1) for j<12, and A e_12=-sum_{j=1}^{12}p_j e_(13-j). Output column j is C e_j=y_j.

**Lower bound certificate.** Define the block-Hankel matrix H with 24 rows indexed by (lag i in {0,1}, output channel o among 12) and 13 columns j=0,...,12:

H[(i,o),j] = (y_(i+j))_o.

Every d-dimensional linear realization factors H into an observability matrix (24 by d) times a reachability matrix (d by 13), so rank_K H<=d. Specialize z=2 over F_p, p=1000003; 2 is invertible, so z^(-1) is well-defined.

Choose these 13 rows in order, writing (lag; q,c,e):
(0;0,0,+), (0;0,0,-), (0;0,1,+), (0;0,1,-),
(0;1,0,+), (0;1,0,-), (0;1,1,+), (0;1,1,-),
(0;2,0,+), (0;2,0,-), (0;2,1,+),
(1;1,0,+), (1;1,0,-).

For all 13 columns, direct finite-field elimination gives

**det H_selected(z=2) mod 1000003 = 739682 != 0.**

This is an exact nonzero minor certificate: the corresponding Laurent-polynomial minor is therefore nonzero in K. Hence d>=13, proving Theorem A.

## Theorem B: for the shifted sequence y_(n+1), the minimum is exactly 12

Let Ptilde(lambda)=lambda^12 P(lambda^(-1)). Theorem A's identity R(T)v=T Ptilde(T)v=0 implies Ptilde(T)(Tv)=0. Therefore the Krylov orbit from Tv has dimension <=12 and realizes all y_(n+1).

A 24-by-12 block-Hankel matrix for the shifted sequence, with lag 0/1 and columns j=0..11, has a 12-by-12 minor using rows:
(0;0,0,+), (0;0,0,-), (0;0,1,+),
(0;1,0,+), (0;1,0,-), (0;1,1,+), (0;1,1,-),
(0;2,0,+), (0;2,0,-), (0;2,1,+),
(1;1,0,+), (1;1,0,-).

**det H_shift_selected(z=2) mod 1000003 = 684922 != 0.**
Thus the shifted sequence has exact minimum dimension 12 over Q(z).

## Initial-transient explanation

The R4-EC9 common scalar recurrence with P is homogeneous only for n>=13, not necessarily at n=12. The exact residual at n=12 is

d_12 = sum_{j=0}^{12} p_j y_(12-j).

All 12 coordinates vanish except the dirty q=0 channels:
- d_12(q=0,c=1,e=+1)=-(z^2+1);
- d_12(q=0,c=1,e=-1)=+(z^2+1).

This is a signed algebraic **recurrence defect**, not negative BRC path mass. It explains why scalar eventual order 12 coexists with joint time-zero vector dimension 13 and a 12-dimensional shifted tail. The additional state is a one-step initial transient of this auxiliary transfer realization, not a native spatial dimension.

## Evidence and limits

The author's SymPy verifier establishes the 14-component Laurent identity, the complete defect vector and the two specialized Hankel determinants. A separately implemented C++17 checker reconstructs the BRC dynamics, exhaustively enumerates all 8191 binary words of lengths 0..12, and confirms the two determinants and defects using finite-field arithmetic. Both were actually run locally and passed; the extended executed sources and reports are retained in the user's per-run ZIP evidence package. GitHub repro files are author-side reference copies and are only called executable-verified after actual execution/readback.

**BRC interface:** COMPOSE_APPLIED to R4-EC9's positive ordered BRC path/count carrier with complete full-effect observation. The Q(z)-linear Krylov basis can use signed rational coefficients; it is not a positive BRC control-state automaton and does **not** settle the remaining fixed-effect-blind transition six-versus-seven control-state problem.

**Ontology/authority:** P000 is ACTIVE_LOCKED; all native Enterprise Math research starts from Heartbeat World's six-dimensional discrete X6 spatial basis and separately typed time. This auxiliary affine-language model has no proven X6 embedding, joint readout/future preservation map or physical-time correspondence; R193's source-port/time bridge remains open. Native task listing gave CONTROL_QUOTA; native session registration gave STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The current active owner, CLAIM, formal Result and independent Driver review are therefore **unverified**. Branch storage is evidence, not canonical admission.

## Next independent question

R4-EC11: compute an explicit 14-to-13 Krylov relation and test whether the associated quotient respects the positive path cone and *each bit-conditioned edge operator*, rather than merely the aggregate linear transfer. Seek a cone-preserving, effect-blind mechanism or a finite exact obstruction. Keep the separate six-or-seven-state positive aggregation question open and retain R193/X6 native bridge as a separate obligation.

Pinned research inputs: GLOBAL_KNOWLEDGE_V1 main@5522a17ad8f68be638faa495483292dbc3ffac62, Enterprise Math source main@32bf5b35b77a0b5b2328d5b813d20d87f3ba06a5, R4-EC9 author branch immutable commit 999fd51c2bcd3ad3646fecbff2bbc3700c7a773b.

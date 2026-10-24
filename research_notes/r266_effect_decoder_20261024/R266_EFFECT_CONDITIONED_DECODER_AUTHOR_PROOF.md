# R266 | Effect-conditioned BRC readout: exact Hankel obstruction and bounded-decoder repair

Date: 2026-10-24. Status: AUTHOR_SIDE_EXACT_DERIVATION; NOT_ADMITTED.

## Scope and reproducible source pins

GLOBAL_KNOWLEDGE_V1 canonical main: 9ba278d5d26a7ed761a946289e416d728bccd138. Enterprise Math canonical main: dadc43f8206cde74c09a760e2990193fce25d673. R265 author proof: b6d858eacbd5482b6a4bb7bcf847bdee2a9932fa. R263 full-fiber evidence: ecce6d55b4c2b1f58769dc40d306f594f7d29b9a.

We work in the formal positive-weight BRC with affine effect group G={(epsilon,k):epsilon in {+1,-1},k integer}, composition (epsilon,k) THEN (eta,b)=(eta*epsilon,eta*k+b). Its abstract composition index is not physical heartbeat time. The six formal slots are not an established native P000 X6 Cell dynamics. Source branches are counted with nonnegative integer weights, with complete effect and provenance retained until an explicitly proved safe observer quotient.

R265 proved that for fixed terminal (q,h) labels, a d-control homogeneous affine-weighted graph has a 2d-dimensional rational lift; a particular 13x13 Hankel minor of the R260 query is nonzero and hence d>=7. The present work investigates what changes when the terminal decoder is permitted to depend on accumulated *actual* effects, possibly nonlinearly.

## Theorem A: a ONE-control positive BRC has unbounded Hankel rank under exact effect-conditioned decoding

Take one control state with two weight-one self-loops carrying genuine translations (+1,+1) and (+1,-1). Set terminal h=1 exactly when accumulated k=0, and h=0 otherwise. All m-step paths are preserved; the target h=1 count is

s_(2j) = binomial(2j,j),   s_(2j+1)=0.

For N>=1 define K_N=(s_(i+j))_(0<=i,j<N). Then, *for all N*,

    det K_N = 2^(N-1) != 0.

Exact algebraic proof: Define L:Q[x,x^-1]->Q by Laurent constant-term extraction and y=x+x^-1. The binomial theorem gives L(y^m)=s_m. Define monic y-polynomials P_0=1 and P_n=x^n+x^-n for n>=1. The latter satisfy P_1=y, P_2=y^2-2, and P_(n+1)=y*P_n-P_(n-1) for n>=2. Laurent monomial multiplication gives L(P_i P_j)=0 for i!=j, L(P_0^2)=1, and L(P_i^2)=2 for i>=1. Hence the moment/Hankel Gram matrix in the monomial basis (1,y,...,y^(N-1)) is transformed by a unitriangular basis change into diag(1,2,...,2). Its determinant is 2^(N-1), proving the assertion for *all* N. In particular det K_13=4096 with d=1, so there is no universal bound Hankel-rank<=2d across arbitrary effect-conditioned decoders.

This one-state counterexample does NOT implement the R260 h-query and does NOT invalidate R265's fixed-readout seven-state theorem. Rather, it pinpoints the exact failed step if R265's rank argument is silently exported to nonlinear effect-dependent terminal observers.

## Theorem B: a finite-dimensional representation-type decoder restores a rank bound

Let rho:G->GL_r(Q) obey the anti-homomorphism identity rho(g THEN h)=rho(h)rho(g). Let v in Q^r be fixed and each terminal control state c have a fixed row ell_c such that the scalar readout of a path ending at c with accumulated effect g is

    f_c(g)=ell_c rho(g) v.

For any d-control, fixed-edge, time-homogeneous rational-weighted affine BRC, define V_m(c)=sum_{paths ending c} w(path)rho(g_path)v. A local edge u->c of weight w and effect h contributes w*rho(h)*V_m(u). Concatenating the d blocks yields a fixed rational dr x dr matrix A with V_(m+1)=A V_m. There is a fixed row ell such that a_m=ell A^m V_0. Thus every Hankel matrix of a_m factors into a (number_of_rows)x(dr) and a (dr)x(number_of_columns) matrix:

    rank(H(a)) <= d*r.

Therefore any finite-dimensional representation coefficient interface admits a sound dimensional bound (r=2 recovers R265). The exact-zero indicator 1_{k=0} cannot be such a finite-dimensional coefficient on all integer translations: if it were, Theorem B with the one-state construction would impose a finite Hankel rank, contradicting Theorem A. This is a precise interface obstruction to moving the 2d argument across arbitrary coefficient extraction.

Note that signed rational entries used internally in an algebraic group representation do not introduce signed physical branch weights; the underlying BRC path counts are positive.

## Proposition C: the actual R260 h is not a function of (m,q,epsilon,k)

R260's source has q in {0,1,2}; choice 0 edges:
q0 -> (2,-1,-1), q1 -> (0,-1,-1), q2 -> (1,+1,+1).
Choice 1 edges:
q0 -> (2,+1,-1), q1 -> (0,+1,-1), q2 -> (2,+1,-1).
Source detector r has r0 (no 00, last not 0), r1 (no 00, last 0), r2 (00 already seen), and query h=1 iff r=2.

The two length-3 words have exact endpoints

    000: (q,r,epsilon,k)=(0,2,+1,-1),  h=1;
    101: (q,r,epsilon,k)=(0,0,+1,-1),  h=0.

Hence even with m included there is no deterministic function h=D(m,q,epsilon,k) that produces the original query on every path. A proposed 3-q-state model using solely this deterministic effect decoder cannot work. This does not exclude arbitrary 6-control aggregate encoders.

## Proposition D: effect/time-aware deterministic STATE QUOTIENTS still require seven states

This is a deliberately narrower comparison class than arbitrary positive weighted aggregate models. Require a deterministic homomorphic quotient pi of the original reachable product automaton, with each input choice mapped by a fixed state transition and its true affine edge effect, and terminal decoder allowed to be any function D(pi(q,r),epsilon,k,m). Preserve per-path observations and the full joint histograms after every allowed future NONSELECTIVE two-choice packet.

There are exactly seven reachable product states. At length m=8 all seven lie in the *same* affine-effect fiber (+1,0). Explicit witnesses:

    (0,0): 01010101    (0,2): 00001100
    (1,1): 01010110    (1,2): 00000100
    (2,0): 01101011    (2,1): 10101010
    (2,2): 00001010

Six or fewer quotient states force two of these prefixes (same length and effect) to share a quotient control. Every pair already has different current terminal (q,h), except (2,0) versus (2,1). For that exceptional pair both current outputs are (q,h)=(2,0), but applying the full nonselective packet from the same current effect (+1,0) gives:

    r=0: (q,h,epsilon,k)=(1,0,+1,+1) and (2,0,+1,-1), weights 1 each;
    r=1: (q,h,epsilon,k)=(1,1,+1,+1) and (2,0,+1,-1), weights 1 each.

Thus these two conditional future histograms differ. A fixed quotient state with identical cumulative effect and depth cannot predict both. Every pair is distinguishable now or by one permitted future packet, establishing d>=7 for this deterministic quotient class; the original 7-state model attains it.

This does **not** prove that a wholly new arbitrary positive six-control aggregate affine automaton with nonlinear effect-conditioned decoding is impossible. Pathwise quotient, fixed terminal linear readout, and unconstrained nonlinear aggregate decoding remain three distinct mathematical classes.

## Exact validation and next scientific unit

Executed local Python integer verification checks: all N=1..17 determinants via Bareiss exact division; direct raw +/-1 words for lengths 0..13; R260 collision at m=3; exhaustive raw binary words of lengths 0..8 including the first full 7-state same-effect fiber at m=8; and complete nonselective packet comparison of the exceptional pair. Infinite-N determinant and dr rank results are analytic algebraic proofs, not extrapolations.

Native Enterprise Math Python modules, R193 provenance/query/time ports, and actual P000 X6 transfer were not executed or established. Native control inventory returned CONTROL_QUOTA; session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Live Owner, formal activity, CLAIM, Source Result, and independent Driver admission are not verified.

Next: define the precise class of positive *aggregate* d-state effect-conditioned decoder, specifying whether per-state terminal fractions can depend on (epsilon,k,m), and whether a decoder may read accumulated effects internally during state transitions. Seek a genuine d<=6 construction or a non-quotient obstruction preserving all H_m. For bounded representation-type decoders, determine sharp minimal d as a function of r. Separately obtain R193 native interfaces and original source runtime evidence before any native theorem claim.

Status: AUTHOR_PROOF_COMPLETE / EXACT_INTEGER_CHECKED / NO_NATIVE_SOURCE_EXECUTION / OWNER_UNVERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED.

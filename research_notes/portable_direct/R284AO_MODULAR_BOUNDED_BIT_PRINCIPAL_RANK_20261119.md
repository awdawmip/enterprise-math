# R284AO — Deterministic bounded-bit modular exterior-span certificate

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Continuation: R284AN (intrinsic-rank integer exterior span), R284AM (paired exterior span), R284AL (diagonal principal witness), R284AK (principal rank gap).
Frozen scientific source pin inherited from R284AN: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Scope: rational low-rank auxiliary Port observer with independently named diagonal edits. P000, ACTIVE Heartbeat World and joint-relation preservation remain unchanged. No native X6 dynamic or future-operation-safe quotient is asserted.

## AO1. Principal-rank problem

For X,Y in Z^(m×k), let C=XY^T. Let d(C) be the largest j such that some j×j principal minor det C[S,S] is nonzero, with d(C)=0 when all nonempty principal minors vanish. The integer-input theorem below also applies to rational factorization after exact row denominator clearing: the integer-scaled principal minors differ from the original minors by nonzero row factors.

For j=0,...,k and S={s_1<...<s_j}, put
a_S = x_(s_1) wedge ... wedge x_(s_j),
b_S = y_(s_1) wedge ... wedge y_(s_j),
z_S = a_S tensor b_S in Z^(D_j), D_j=binom(k,j)^2.
The contraction ell_j(z_S)=sum_{|I|=j}(a_S)_I(b_S)_I equals det C[S,S] by Cauchy–Binet.
The map E_i sending a tensor b to (a wedge x_i) tensor (b wedge y_i), with the same new index on both factors, is linear on the paired tensor space. Hence L_j(i), the Q-span of states supported on the first i named rows, obeys exactly
L_j(i)=L_j(i-1)+E_i L_(j-1)(i-1).
Choose every basis vector to be an actual named-subset state, not a linear combination. The recurrence then preserves true witnesses and the complete zero/nonnull test.

## AO2. Finite-prime exact rank theorem

Let M0=max(1,abs(X_ia),abs(Y_ia)) over all entries. For each grade j let
H_j=(j!)^2 M0^(2j), D_j=binom(k,j)^2,
B_j=D_j! H_j^(D_j).
Every coordinate of a true state z_S has magnitude at most H_j, since a j×j determinant has magnitude at most j! M0^j. Every square minor of any matrix formed from at most D_j+1 true grade-j states has magnitude at most B_j: its order is at most D_j and the Leibniz bound is s! H_j^s.

Take distinct primes P_j={p_1,...,p_l} whose integer product Q_j exceeds B_j. For every such integer state matrix T, we have

rank_Q(T) = max_{p in P_j} rank_(F_p)(T mod p).

Proof: reduction modulo any p cannot increase rank. Let r=rank_Q(T), and choose a nonzero r×r integer minor Δ. By the bound 0<|Δ|≤B_j<Q_j, some p in P_j does not divide Δ. That reduction has rank at least r, completing equality. Rank zero follows directly.

When a retained set has d independent true states, a candidate z is independent over Q precisely if some selected prime gives rank d+1 on the retained state matrix augmented by z. Crucially, compare the new modular rank with the *rational basis size d*, not with that prime's previous modular rank: a bad prime can otherwise produce a false independence decision. On acceptance, insert the actual z_S and update the row echelon state over every prime. On rejection, omit it from the basis; the exact rational span and all future E_i images are preserved by linearity.

## AO3. Deterministic bit-growth bound and replay certificate

At grade j, at most D_j genuine named states are stored, with O(k) indices per state, and at most m D_(j-1) candidate states are tested. The fixed prime set is independent of the candidate order. Its size is at most floor(log_2 B_j)+1 because each prime is >=2. The largest prime among the first l primes has polynomial magnitude in l (standard elementary prime bounds), so modular arithmetic uses O(log l) bit field elements. The full stage thus has polynomial bit cost in m, k, the coordinate bit length log M0 and the intrinsic-state dimension sum_j D_j=binom(2k,k), apart from the separately accounted exact thin factorization/denominator clearing.

This is a provable bound for the modular stage, replacing R284AN's unbounded *observed* integer-primitive intermediate growth with explicitly bounded residues. It is not a universal speed improvement: the large prime collection and modular echelon updates may cost more CPU than primitive integer elimination.

A replayable certificate consists of the input X,Y, grade bounds B_j, prime sets P_j and their products, the actual named subset basis labels for each grade, and contraction traces. Recreate the wedge states and check every candidate decision by modular rank; for a negative conclusion, verify all higher-grade basis traces vanish and all omitted candidates are span dependent. A positive witness S is separately checked by exact det C[S,S]. No exhaustive enumeration of all named subsets is required for general m.

For any rational C used in the previously declared independent diagonal Port pencil
M_C(u,v) = [[diag(u),I_m],[C,diag(v)]],
the established block determinant identity gives
nu(M_C)=2(m-d(C)).
Thus the modular algorithm computes this exact first nonzero total edit degree.

## Exact implementation and finite verification

Reproducible standard-library Python file: R284AO_modular_principal_rank_checker.py.
Evidence: R284AO_modular_principal_rank_verification.json.

Executed checks:
- 42 signed integer-factor random instances (seed 284015, 2≤m≤6 and 1≤k≤min(m,3)) compared with complete independent principal-minor enumeration using an integer Leibniz determinant oracle.
- Three targeted cases including a nonzero nilpotent rank-one C with d(C)=0, a nonzero diagonal rank-one case, and a rank-two cross-coupling example.
- Every accepted basis dimension independently rechecked as the maximum finite-prime modular rank; every detected witness directly re-evaluated as a determinant of C[S,S].
- Largest observed candidate count 41, largest prime set per grade 24, largest computed minor-bound bit length 109; all finished PASS.

The exact modular-rank theorem and recurrence are general; these finite tests are regression coverage, not the proof. Result remains NOT_REVIEWED and makes no external novelty claim.

## Preservation boundary and next work

The factorization preserves the specified matrix C and its declared diagonal-edit polynomial. It retains real subset labels and signed coefficients; it does not certify erasure of other BRC/Port history, path provenance or future interventions.

Next: validate a compact independent verifier that checks the basis labels and modular closure transcript without replaying the entire discovery program; benchmark this modular implementation against R284AN integer-primitive elimination and R284AL random probes end-to-end, including factor preprocessing and proof verification, on the same hardware and exact input families. Explore whether per-grade sparse support or SCC structure can reduce D_j before prime computation.
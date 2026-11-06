# D25: universal source-mask collision and sharp p-adic port recovery

Date 2026-11-07 (Asia/Hong_Kong). Author-side portable mathematical evidence: UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific input c47e13e4aba0e006366f989d6334d443f6333ae3; taskbook blob 53a3ef039325534e3715add837f0eee332289984. Mother objective Delta_p-R_p=0 (mod p), p mod 24 in {13,19}. The following is an auxiliary BRC information-loss audit; it does not assert an equivalent LIFT certificate.

## Source model

For each prime p=6m+1 (m>=1), let z in {0,...,p-1} and let

V_j(z)=(6j+1)(-1/2)^j binom(3m,j) binom(2m+z,j) binom(4m+z,j), 0<=j<=3m.

The three binomial sources retain ordered labels (3m,2m+z,4m+z). Let P_m(z)=sum V_j(z). All binomial factors here are integers and 2 is a p-unit. The observation surface may retain total P, any or all weighted j-ports, or additional labelled raw factor tags.

## Theorem A: universal all-port alias modulo p

Define z_L=4m+1 and z_R=2m+1, distinct and equal to 1/3 and 2/3 in F_p. Ordered varying source factors are

L: (2m+z_L,4m+z_L)=(p,p+2m);
R: (2m+z_R,4m+z_R)=(4m+1,p).

For every 1<=j<=3m<p, binom(p,j)=0 (mod p), hence V_0(L)=V_0(R)=1 and V_j(L)=V_j(R)=0 (mod p) for all j>=1. In particular P_m(L)=P_m(R)=1 (mod p). Even the full array of all weighted summands mod p has exactly the same values for two distinct source states. The labelled factor-zero position distinguishes them: the first varying factor is divisible by p on L, the second on R. This holds for all p=6m+1, including both target residue classes 13 and 19 (mod 24).

## Theorem B: recover the source by one additional p-adic digit

The first weighted port is exactly V_1(z)=-(21m/2)(2m+z)(4m+z). Therefore

V_1(L)-V_1(R)=-42m^2 p;  [V_1(L)-V_1(R)]/p=-7/6 (mod p).

For every p>=13 with p=1 (mod 6), this residue is nonzero, so the first port modulo p^2 separates L and R. At p=7 the j=1 weight 7 contributes an extra p, so the first port does not separate them at p^2.

For an all-prime alternative choose j_*=2m+1<=3m. Then

v_p(V_{j_*}(L))=2 and v_p(V_{j_*}(R))=1.

Both leading quotients are explicit nonzero residues. Write C=binom(3m,j_*). Then

V_{j_*}(L)/p^2 = -(6j_*+1)C/[2^{j_*}j_*^2] (mod p);

V_{j_*}(R)/p = -(6j_*+1)C binom(4m+1,j_*)/[2^{j_*}j_*] (mod p).

Indeed binom(p,j)/p=(-1)^{j-1}/j (mod p), and binom(p+2m,2m+1)=(p/(2m+1))binom(p+2m,2m) with the latter binomial congruent to 1. Other factors are p-units, since j_*<p, 6j_*+1=5 (mod p), and j_*<=3m<4m+1<p. These prove the exact valuations, including p=7.

## Theorem C: sharp low-port fibre classification

For p>=13 the first port modulo p obeys

V_1(z)=(7/4)(z-1/3)(z-2/3),
V_1(z)-V_1(w)=(7/4)(z-w)(z+w-1) (mod p).

Thus V_1(z)=V_1(w) iff z=w or w=1-z. Its p input states form (p-1)/2 size-two fibres plus one singleton z=1/2.

For p>=19,

V_2(z)=39/128 (z-1/3)(z-4/3)(z-2/3)(z-5/3),
V_2(z)-V_2(1-z)=-13(2z-1)(3z-2)(3z-1)/192 (mod p).

All denominators and 13 are units. A distinct reflected pair remains equal on both V_1,V_2 only when z=1/3 or 2/3. Hence (V_1,V_2) mod p has exactly one size-two fibre {1/3,2/3}; its other p-2 fibres are singletons. Theorem A proves this is the best possible separation using any number of reduced weighted term ports.

Moreover a *single* V_1 measured modulo p^2 is injective on the canonical field representatives z=0,...,p-1 for p>=13. For a distinct mod-p alias z,w, the integer sum z+w is 1 or p+1. Hence z+w+6m is exactly p or 2p, while -(21m/2)(z-w) is a p-unit. Their exact difference V_1(z)-V_1(w) has valuation one and cannot vanish modulo p^2. This precision theorem refers to the stated lift of representatives. At p=13, V_2 vanishes mod p because its weight is 13; the two-port theorem starts at p=19.

## Executed exact validation and research implication

The pure-Python integer checker d25_source_alias_padic_verified_20261107.py tested all 80 primes 7<=p<=1000 with p=1 (mod 6), all j-ports of both states, the exact first-port identity, carry-port valuations/quotients, every p-field first-port fibre for p>=13, and every two-port fibre for p>=19. Output: ALL_CHECKS_PASS.

Representative tuples (p,z_L,z_R,j_*, [V_1(L)-V_1(R)]/p, V_tail(L)/p^2, V_tail(R)/p), all residues mod p:
(7,5,3,3,0,1,2); (19,13,7,7,2,5,1); (109,73,37,37,17,105,70).

These are general algebraic proofs with exact finite regression, not a finite scan used as a universal proof. BRC carrier: two distinct labelled integer-binomial factor channels, three-source provenance, j weights and first/second p-adic digits. Coarse observer: term-port vector modulo p. Alternative preserving observers: labelled zero-mask, a first port modulo p^2 for p>=13, or the explicit carry port modulo p^2 for all p. The result provides a precise information-retention construction, pending a bridge to the actual frozen G_p*h, Phi_xx and derivative/Frobenius LIFT interface.

## Current frontier / operation boundary

Next scientific action: compare the exact LIFT second-digit factor representation to this alias and decide by an explicit source-preserving map whether the extra factor label or p-digit is needed; otherwise return to the open E_t(+1) inverse-moment telescoper and the original Delta_p-R_p residual. Do not infer an all-prime LIFT solution from this auxiliary observer.

On 2026-11-07 02:21 Asia/Hong_Kong, em_status and reads of original request IDs em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Site phase was CONFIGURED_NOT_LIVE_VERIFIED. Native session/claim/run, protected staging and Source checkpoint remain unknown. This work uses only author-side portable evidence; no native session, claim, run, checkpoint, Result or review is asserted. Existing responsible control issue: enterprise-math #1558.

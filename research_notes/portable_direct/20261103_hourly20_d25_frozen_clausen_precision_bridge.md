# D25 — frozen Clausen observer precision bridge and first higher residual

2026-11-03 (+08). TASK_RESEARCH author-side portable evidence; algebraically proved identity and finite exact arithmetic, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923; maintenance conversation NOT used. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7; frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Frozen mother question remains Delta_p-R_p=0 (mod p) for p mod 24 in {13,19}.

## Inherited sources, all retained under their original ownership

For prime p=6r+1 >=13, put c_k=(1/6)_k(1/3)_k/(k!)^2, a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3 and B_k=c_k/2^k for 0<=k<p. Define M=sum B_k, N=sum k B_k, H=M+12N, W=sum (6k+1)a_k/2^k and Q=sum_{0<=i,j<p, i+j>=p}(6(i+j)+1)B_i B_j, with exact rational arithmetic in Z_(p). Source-accepted CM0/UR provides p|M and (M/p)H=1 (mod p); previous reflected-cutoff research gives p^2|Q and frozen R_p=Q/p^2 (mod p). We retain both the actual original reflected C_a formula and the full ordered signed Q.

Prior author-side work (not credited anew here): the 2026-10-26 onhour D25 source-port alignment at research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md establishes the original first-digit frozen interface; the hourly20 C3 six-prefix plus high/high theorem at research_notes/portable_direct/20261103_hourly20_d25_clausen_p5_sixmoment_complete.md (check actual path in project) supplies precision-p^3 E; H6 at research_notes/portable_direct/20261103_hourly20_d25_gauss_edge_harmonic_p3.md supplies the high-edge unit. All remain unreviewed author-side unless individually admitted.

## Theorem PB1: exact all-finite-precision observer connection

For every integer q>=1 define precision-typed lifts, not replacements of the frozen definitions:

R_p^[q] = (Q/p^2) mod p^q;
Delta_p^[q] = (((M/p)H-1)/p) mod p^q;
E_p^[q] = {[(1+6 theta)(F_p(z)-G_p(z)^2)](1/2)/p^2} mod p^q,

where theta=z d/dz, F_p(z)=sum_{k=0}^{p-1}a_k z^k and G_p(z)=sum_{k=0}^{p-1}c_k z^k. The polynomial G_p(z) is distinct from the frozen scalar M/p. R_p^[1] and Delta_p^[1] are precisely the frozen R_p and Delta_p.

For every such p and q,

    E_p^[q] = -R_p^[q]                                      (mod p^q),
    Delta_p^[q] - R_p^[q] = (W-p)/p^2                        (mod p^q).

Both identities are restrictions of EXACT rational identities before modular reduction, so no p-adic precision is silently discarded.

PROOF. The ordinary Clausen formal identity makes every coefficient of F_p(z) below degree p identical to the coefficient of G_p(z)^2. Every coefficient above degree p-1 is absent in F_p, so after applying the original signed Euler operator and z=1/2, [(1+6 theta)(F_p-G_p^2)](1/2)=-Q exactly. The same equality yields W=M^2+12MN-Q=MH-Q exactly. Divide the first equation by p^2; subtract p from the second and divide by p^2 to obtain the displayed equations. The inherited integrality and first-digit congruences license each quotient. QED.

The established C3 six-prefix-moment and ordered high/high decomposition of E^[3] therefore carries, with an exact sign change, the first three digits of the SAME ORIGINAL Q/p^2 frozen reflected source. The high/high port remains separate; the equality is a scope-typed observer map, not permission to replace joint-source history with a single scalar under other operations.

## PB2: exact higher-order counterexample and target-class arithmetic

Independently generated the ORIGINAL finite 2F1 and 3F2 terms using separate recurrences modulo p^5, independently reconstructed the frozen first-digit R via its C_a reflection recurrence, and for all detailed p<=373 also constructed the ordered Q double sum. All seven detailed cases passed every port check.

For p=373, the exact p^3 observer lifts are

    E_373^[3]      = 177 + 196*373 + 150*373^2 = 20942635,
    R_373^[3]      = 196 + 176*373 + 222*373^2 = 30952482,
    Delta_373^[3]  = 196 + 31*373 + 373^2 = 150888,
    Delta_373^[3]-R_373^[3] = 228*373 + 151*373^2 (mod 373^3).

The independently calculated full weighted original W_373 satisfies

    W_373 = 373 + 228*373^3 + 151*373^4 (mod 373^5).

Therefore v_373(W_373-373)=3 and v_373(Delta^[3]-R^[3])=1 for the actual p-adic rational quantities.

The minimal p=13 witness is already decisive for the optional stronger conjecture: W_13 = 19786 = 13+9*13^3 (mod 13^4), so v_13(W_13-13)=3 and Delta_13^[2]-R_13^[2]=9*13 (mod 13^2). This proves the universal strengthening Delta-R=0 (mod p^2) is FALSE on the target prime classes, while leaving the frozen mod-p objective intact.

A separate direct finite original-3F2 scan of all 312 primes p<=10000 with p mod24 in {13,19} found W=p (mod p^3), and a nonzero following digit (W-p)/p^3 mod p at every tested prime. These 312 exact checks are a bounded computation. The potential all-prime nonvanishing pattern is exploratory, not a theorem or an extra requirement for the mother target.

## BRC typing, contribution scope and continuation

COMPOSE_APPLIED: exact original index population, source coefficient labels, ordered high/low pair multiplicity, signed (6(i+j)+1), p-valuations, the frozen C_a reflection and precision-aware Delta/R/E observers are preserved. PB1 certifies an exact scalar readout descent for every finite q; it does not erase the source field or admit the prior author proofs.

Current science unit completed: original frozen R/Delta first-digit source mapping has now been connected to the already-computed C3 p^5 precision tower, with a finite counterexample preventing an accidental stronger target. Do not repeat prior H5/H6, onhour original mod-p source alignment, H3/H4/C3 or the p^5 precision computation as new discoveries.

NEXT: seek a genuine all-target CM/WZ certificate for the exact original first digit (W-p)/p^2=0 (mod p), or an in-hypothesis counterexample. A disjoint optional study is to classify prime-specific first nonzero higher residuals without turning higher precision into a mandatory gate. Native original p373 H0/B0 and [X]U experiments remain independently pending through Enterprise Math issue #1559. Keep the frozen Delta/R and native operator distinct from ordinary hypergeometric checks.

Operational note: the source Gateway 0.6.11 observed 2026-11-03 06:20+08 returned UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, native active-job quota 5/5. No new native session/CLAIM/OPEN/checkpoint/Result/review; #6637/#6638 and previous service session/staging were not replayed or mutated. Control owner path remains #1558. This is author-side proof and arithmetic, not native scientific admission.

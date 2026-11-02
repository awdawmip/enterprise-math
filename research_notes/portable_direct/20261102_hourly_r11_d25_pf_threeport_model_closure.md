# D25: finite Picard–Fuchs closure and minimal source-labeled Teichmüller ports

Date: 2026-11-02, Asia/Hong_Kong.
Status: AUTHOR-DERIVED / EXACT PROOF / 107-PRIME EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.
The historical Research logical lane is chatgpt-research-hourly-enterprise-math-20260923; this author-side portable proof is no authenticated Source CLAIM, OPEN, Result, or checkpoint. P000 and ACTIVE worldview retained.

## Theorem 1 — truncated third-order Picard–Fuchs closure through p³

Fix prime p>=5 and one of the two parameter triples
 A=(1/2,1/3,2/3), B=(1/4,1/2,3/4). Define
 F_{a,p}(z)=sum_{k=0}^{p-1} c_k z^k,
 c_k=prod_{alpha in a}(alpha)_k/(k!)^3,
 theta=z d/dz.
Let s1=sum a_i, s2=sum_{i<j} a_i*a_j, s3=prod a_i and
 L=(1-z)theta^3-z(s1 theta^2+s2 theta+s3).

There is an exact identity in Q[z]:
 L F_{a,p}(z) = -c_{p-1} prod_{alpha in a}(p-1+alpha) z^p.       (1)

Proof: k³c_k=prod_alpha(k-1+alpha)c_{k-1} for 1<=k<p; all interior coefficients cancel and only coefficient z^p remains. Each factor (alpha)_{p-1} includes exactly one numerator multiple of p and none of p² for p>=5 in the specified triples, and (p-1)!³ is a p-unit. The endpoint product factors (p-1+alpha) are p-units. Hence the right side of (1) has exact p-valuation 3, so
 L F_{a,p} = 0 mod p³ in Z_(p)[z].                              (2)
This accounts for the actual high-index boundary; it becomes observable at precision p^4.

For z and 1-z p-units put f_j=(theta^jF)(z). Applying theta^m to (2), and using theta^m(zG)=z sum_{h=0}^m binom(m,h)theta^hG, yields for all m>=0
 (1-z) f_{m+3}
  = z sum_{h=0}^{m-1} binom(m,h) f_{h+3}
   +z sum_{h=0}^m binom(m,h)(s1 f_{h+2}+s2 f_{h+1}+s3 f_h)
        (mod p³).                                             (3)
The first sum is empty at m=0. Thus every higher Euler derivative is a function of the three base jets (f0,f1,f2), modulo p³, for these original finite polynomials.

At the original rational points:
 A: z_A=1/2, f3_A=(3/2)f2_A+(13/18)f1_A+(1/9)f0_A (mod p³);
 B: z_B=1/9, f3_B=(3/16)f2_B+(11/128)f1_B+(3/256)f0_B (mod p³).    (4)
These are proven internal-to-source relations, not a fitted cross-family map.

## Theorem 2 — second gauge digit from two independently tagged ports per stream

Now p mod 24 in {13,19}. Use the established CM double-zero premises f0=f1=0 mod p for each source (the finite test independently checks them in its domain). For the original rational point z, q=(z^(p-1)-1)/p in Z_(p), omega=z^(p²) mod p³. With Y=(1+c theta)F, c_A=6,c_B=8, define
 delta_c=[Y(omega)-Y(z)]/p mod p².

The previously proved second-order Teichmüller expansion says
 delta_c=c q f2+p[q(f1/p)+c q f2+(q²/2)(f2+c(f3-f2))] (mod p²). (5)

In (5), f3 occurs multiplied by p, so (4) and the CM double zero give f3_A=(3/2)f2_A and f3_B=(3/16)f2_B mod p. Substitution proves
 delta_A=6q_A f2_A+p[q_A(f1_A/p)+6q_Af2_A+2q_A²f2_A] (mod p²),
 delta_B=8q_B f2_B+p[q_B(f1_B/p)+8q_Bf2_B-(11/4)q_B²f2_B] (mod p²).    (6)

For the signed bridge gauge displacement G_p=delta_A-2delta_B:
 G_p=6q_Af2_A-16q_Bf2_B
     +p[q_A(f1_A/p)-2q_B(f1_B/p)+6q_Af2_A-16q_Bf2_B
         +2q_A²f2_A+(11/2)q_B²f2_B]  (mod p²).                 (7)

For this *specific* future operation, retaining just (f1/p mod p, f2 mod p²) per original source, and its family label, original z, c, and q mod p², is sufficient. f0/p remains relevant if the whole canonical jet rather than G_p is the future readout. The general-polynomial BRC indistinguishability witness P0=0, P1=(X-z)^3 from 20261102_hourly_d25_fourth_jet_port_necessity.md stays valid on its larger input population: the D25 stream class is restricted by (2). BRC resolution: COMPOSE_APPLIED / MODEL_SPECIFIC_SAFE_QUOTIENT, preserving signed stream identity and actual p-adic precision. This does not assert native X6 semantics.

## Actual exact computation

The companion executable tests the *original* k=0,...,p-1 hypergeometric coefficient recurrences, independently evaluates both weighted sums at z and omega, and checks the CM double zeros, (4), (3) through jet order 8, (5), (6) and direct weighted displacement with exact integer residues modulo p³. All 107 primes <=3000 in classes 13 or 19 modulo 24 passed, with no floating-point arithmetic. The code is an author-side exact checker, not native H0/B0 or Lean verification.

p=373 certificate (mod 373²=139129):
 q_A=123259, q_B=15437;
 f1_A/p=88339, f2_A=87455;
 f1_B/p=94882, f2_B=78666;
 delta_A=72101, delta_B=18921;
 G_373=34259=316+373*91.
Thus prior second gauge digit 91 is recovered without retaining an independent fourth Euler port.

## Current frontier

Mother target remains Delta_p-R_p=0 mod p for p mod 24 in {13,19}, equivalently via the prior signed source reduction to S_p=p mod p³. Reuse earlier CM selector, weighted Clausen signed cutoff, half-range tail, independent 2304 result, scalar and projective counterexamples, and original p373 228:114, 138, 365, 316, 91 witnesses. The next exact scientific unit is a *sourced non-scalar* finite-field CM/character-sum/WZ relation directly comparing the original two tagged pairs (f1_A/p,f2_A) and (f1_B/p,f2_B) with q and truncation information. It must preserve the unshifted signed mother readout, not only G_p.

Native control: actual em_status 2026-11-02T00:18:28Z, 0.6.11, UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active jobs 5/5. Prior same Research lane recovery #6637 was a read-only success with no authority; continuation #6638 terminated failed, not replayed. Existing support #1558 owns reviewed-code/deployment, native H0/B0 #1559 remains separate. New Source CLAIM/OPEN/checkpoint/Result/review have not been created. No change to P000, ACTIVE worldview, frozen scientific inputs, or existing schedule and notification behavior.

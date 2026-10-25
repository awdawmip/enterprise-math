# D25/LIFT — first p-adic correction to the original cross-band reciprocity

Date: 2026-10-25. TASK_RESEARCH / own logical lane chatgpt-research-hourly-enterprise-math-20260923. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged.

Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. No formal Source-native checkpoint, actual CM/divided-power experiment, independent review or full W_p supercongruence proof.

## Consumed predecessor and genuinely new question

Consume the already proved exact mod-p paired identity in research_notes/portable_direct/20261025_hourly_d25_reverse_forward_reciprocity_and_exceptional_rank.md and its source-ranked reverse tail input. This new unit asks for a uniform and pole-safe **mod-p² lift of the entire pairing**, rather than re-proving its first digit.

Let p=6m+1 >= 7 be prime. Work in Z_(p). Define, for 0<=k<=2m-1,

A_k=(1/2)_k (1/3)_k (2/3)_k / [2^k(k!)^3],
e_k=d_(p-1-k),
Q_k=e_k A_k,
Phi(k)=2(6k+5)/[(2k+1)(3k+1)(3k+2)],

where d_n is the exact original fourth-band source extraction, not a native Frobenius coefficient. All denominators displayed below are p-units within their exact finite ranges. The earlier theorem gives Q_k=Phi(k) mod p, including the exceptional original index k=m.

For 0<=j<=2m-2, set

E_j = 6/(6j+5) - 6/(6j+11) - 3/(j+1)
      + 2/(3j+5) + 1/(2j+3) + 1/(3j+4),

and H_k = SUM_{j=0}^{k-1} E_j, with H_0=0.

## Theorem: exact first deformation coefficient

For EVERY eligible prime p and EVERY 0<=k<=2m-1,

Q_k = Phi(k) * [d_(p-1)/5] * (1 + p H_k)  (mod p²).

Since d_(p-1)=5 mod p, the endpoint ratio d_(p-1)/5 is a legitimate p-adic unit; no extra normalization or division by a vanishing signed coefficient is introduced.

### Constructive proof

From the original exact source factorial extraction (not its reduction modulo p),

d_(n-1)/d_n
= [(6n-5)/(6n+1)] *
  [2 n^3/((n-1-2m)(n-1-3m)(n-1-4m))],

for original fourth-band ranks n=p-1-j and 0<=j<=2m-2. The forward source factor satisfies

A_(j+1)/A_j
= [(2j+1)(3j+1)(3j+2)]/[36(j+1)^3].

Substitute n=p-1-j and m=(p-1)/6. Compare the resulting exact Q_(j+1)/Q_j with Phi(j+1)/Phi(j). Their quotient is

R_j(p) =
  [(1-6p/(6j+11))/(1-6p/(6j+5))]
  * [(1-p/(j+1))^3]
  / [(1-2p/(3j+5))(1-p/(2j+3))(1-p/(3j+4))].

This is an exact identity of rational functions evaluated at the fixed prime p, with all listed factors p-units. Expanding each *unit* factor only to the first nontrivial p-adic digit gives

R_j(p)=1+p E_j (mod p²).

Multiplying the ratios for j=0,...,k-1 yields

[Q_k/Phi(k)]/[Q_0/Phi(0)]
= PRODUCT_{j=0}^{k-1} R_j(p)
= 1+p H_k (mod p²).

Because Q_0=d_(p-1), A_0=1 and Phi(0)=5, the base value is Q_0/Phi(0)=d_(p-1)/5. This proves the theorem without assuming anything about native CM, and works uniformly through the dangerous signed rank k=m. QED.

## Exceptional-rank p² certificate

The original signed coefficient a_m=(6m+1)A_m=p A_m, so A_m=a_m/p is the genuine rank-one valuation-normalized port. At k=m,

Phi(m) = 24(p+4)/[(p+2)(p+1)(p+3)]
       = 16(1-19p/12) (mod p²).

Consequently the exact universal next-digit identity is

d_(5m) * (a_m/p)
= 16 [d_(p-1)/5] [1+p(H_m-19/12)] (mod p²).

In particular reducing modulo p recovers the earlier universal 16, but the higher digit additionally requires the retained source endpoint d_(p-1) and the signed harmonic correction H_m. This is a precise BRC information-retention statement: the p-adic observer cannot be reconstructed from the mod-p product alone. The above is a modular source arithmetic theorem, not a new project axiom.

## Reproducible author exact checks

Companion research_notes/portable_direct/20261025_hourly_d25_reverse_forward_p2_check.py was executed locally. It constructs original factorial source d_n and forward Pochhammer A_k in Z/p² using independent recurrences, checks every k across the entire range (not just endpoints), and checks the exceptional formula separately. PASS for all 80 primes p=1 mod6 below 1000 plus 1327 and 19963, total 82 primes. General truth rests on the rational identity proof, not the sample.

Witnesses (value mod p²):
- p=13: d_(p-1)=5; d_(5m)A_m=146 (mod 169)
- p=19: d_(p-1)=328; d_(5m)A_m=35 (mod 361)
- p=373: d_(p-1)=99596; A_m=32200; d_(5m)=74007; H_m=33 (mod 373); d_(5m)A_m=23888 (mod 139129)
- p=1327: d_(p-1)=394124; d_(5m)A_m=991285 (mod 1760929)
- p=19963: d_(p-1)=325217238; d_(5m)A_m=233706857 (mod 398521369).

BRC method state: COMPOSE_APPLIED — source-labelled rank/valuation ports from original W_p, exact reverse/forward recurrence, and p-adic first-jet observer; the quotient retains d_(p-1) and H_k instead of collapsing to a scalar mod p. No native BRC program is claimed run; these are exact independent Python author checks.

## Next executable problem and blockers

Find a source-preserving signed telescoper or finite-field identity that joins this reverse first-jet with the original lower-band jets at the actual p³ W_p-p observer. Do not infer cancellation from 82 finite samples; do not silently divide by a_m modulo p. The native parent still requires authenticated original-class H0/B0, [X]U mod p², rank/semilinear direction/normalization and actual kappa/Delta_p-R_p bridge. D25/LIFT/JT2 OPEN, native CM NOT_RUN. This portable result does not authorize CLAIM/OPEN or a native checkpoint. Existing immutable scientific pin, Source native predecessor/frontier and contributor history remain untouched.

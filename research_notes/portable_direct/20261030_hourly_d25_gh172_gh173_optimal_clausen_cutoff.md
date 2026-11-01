# D25/LIFT GH-172–GH-173: optimal p³ Clausen truncation and next-digit scalar cancellation

2026-10-30. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. Authored by the hourly Research lane `chatgpt-research-hourly-enterprise-math-20260923`, not the maintenance lane. Mother `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. P000 ACTIVE_LOCKED, HEARTBEAT_WORLD native X6, and JOINT_RELATION observer contract remain binding; these arithmetic statements are **not** native spatial axioms.

## Original target and distinct input

D25/LIFT fixes `p mod 24 in {13,19}` and `X=1` in
[
mathcal A_p(1)=sum_{n=0}^{p-1}(6n+1)inom{2n}{n}^{2}inom{3n}{n}/216^nstackrel{?}{equiv}ppmod{p^3}.
]
GH-164's Gauss valuation staircase, GH-166/167's signed tail, and GH-170/171's full-truncation differential forcing are **consumed predecessors**, not new accomplishments here.

## GH-172 — sharp minimal p³ window (algebraic theorem)

For every prime `p=6m+1 >= 7`, set
[
a_n=rac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=rac{(2n)!(3n)!}{216^n(n!)^5},quad 0le n<p.
]
Then
[
v_p(a_n)=
egin{cases}
0&0le nle2m,\
1&2m<nle3m,\
2&3m<nle4m,\
3&4m<n<p.
end{cases}
]
**Proof.** The exact ratio
[
a_{n+1}/a_n=rac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3}
]
has p-unit denominator for `n<p-1`. The only three p-divisible numerator factors occur at `n=3m,2m,4m`, respectively; the third is `3(4m)+2=2p`. This proves each exact band, not just lower bounds.

Put `F_p(X)=sum_(n=0)^(p-1) a_n X^n`, `F*_p(X)=sum_(n=0)^(4m) a_n X^n`, and `theta=X d/dX`. Thus
[
F_pequiv F_p^*pmod{p^3},qquad
(1+6	heta)F_pequiv(1+6	heta)F_p^*pmod{p^3}
]
**coefficientwise**. This is the *shortest possible initial truncation*: omitting `a_(4m)` loses valuation-2 data, and omitting `a_(4m+1)` loses a nonzero p³ digit. The first omitted weighted coefficient has multiplier `6(4m+1)+1=4p+3`, a p-unit, so weighted sharpness holds as well. Original X=1 evaluation may therefore be computed from 4m+1 instead of 6m+1 terms **at the required p³ precision**, without establishing its value.

For `N=4m+1`, `r=2m+1`, the factorial congruences `(p+r)!/p=-r!`, `(2p+1)!/p²=2` modulo p imply the nonzero first-omitted unit
[
oxed{u_p:=a_N/p^3equiv
-2(2m+1)!/([(4m+1)!]^5,216^{4m+1})
otequiv0pmod p.}
]
For `L_3=theta³-(X/2)(theta+1/2)(theta+1/3)(theta+2/3)`, the coefficient recurrence proves the **exact rational polynomial identity**
[
oxed{L_3F_p^*(X)=-N^3a_N X^N.}
]
This source has exact valuation 3. Consequently the shortened cubic equation is homogeneous modulo p³ and sharply inhomogeneous modulo p⁴. In contrast, the previously established Gauss two-factor tail has valuation 2 up to n=p-1, so it does not admit the same shortening modulo p³.

## GH-173 — observer-dependent p⁴ scalar tail

Define the *different, higher-precision* observation
[
Q_p=rac{(1+6	heta)(F_p-F_p^*)(1)}{p^3}pmod p.
]
Set `c_N=u_p` and propagate `c_(n+1)/c_n=(2n+1)(3n+1)(3n+2)/(36(n+1)^3)` in the field `F_p` for `N<=n<p-1`. The factors in this range are nonzero p-units. Thus
[
oxed{Q_p=sum_{n=N}^{p-1}(6n+1)c_npmod p.}
]
Every omitted coefficient has valuation exactly 3, and the first weighted one is `3u_p != 0`; nevertheless the **sum can vanish**. An actual modular counterexample is `p=1327`, `m=221`, `N=885`, with
[
(u_p,-N^3u_p,3u_p,Q_p)=(788,364,1037,0)pmod{1327}.
]
The full and short weighted **polynomials differ mod 1327⁴**, while their evaluations at **X=1 agree mod 1327⁴**. This is a real exact-source cancellation, not an arbitrary formal coefficient assignment. But 1327 is 7 mod24, **outside D25's frozen classes**; it is not a LIFT counterexample. For the in-scope p=373, the corresponding tuple is `(277,45,85,278)` modulo 373, demonstrating nonzero next-digit truncation error at X=1. The p³ truncation remains valid at 373.

The BRC/observer point is precise: a safe quotient for coefficient residues mod p³ and the fixed weighted p³ scalar is **not** safe for coefficient residues mod p⁴; fixed X=1 may sometimes erase the latter difference. Preserve valuation, exact exponent, operations and source; do not promote to P000 spatial facts.

## Executed verification and boundaries

The actually executed standard-library checker `d25_gh172_gh173_optimal_clausen_cutoff_check.py` verified all coefficients and all stated valuations for **330 primes** `7<=p<5000`, `p=1 mod6` (including all **166** D25 classes). It cross-checked the factorial boundary unit, exact modular forcing, original weighted p³ equality, and two independent computations of Q; at anchors 7,13,19,157,373,1327 it also checked raw binomial coefficients. A second normalized finite-field scan covered all **711 primes** `7<=p<12000`, `p=1 mod6`; only `p=1327` had `Q_p=0` in that **finite range**. This is not an infinite uniqueness claim.

Local checker SHA256 `6b1f72539698ffdf5a75d93e1fa565bfd63d6162ddb397c9f6639bd4db250efd`; executed log SHA256 `22ebaad698043307d4c7327cbb9a1d7a48e89c844910ad24eaee290566926b33`. Marker: `PASS_GH172_GH173_OPTIMAL_CLAUSEN_CUTOFF_SCALAR_CANCELLATION_EXACT`. The all-prime cutoff follows from the proof, not the scan. No independent review, Lean check, native H0/B0 experiment, CLAIM/open/Source checkpoint/Result.

## Exact recovery frontier

Science hard target `(1+6 theta)F_p(1)=p (mod p³)` is **OPEN**, not deducible merely from the cutoff or differential forcing. Next true unit: build a CM / p-adic connection or finite WZ identity evaluating the **fixed X=1 constant** for both frozen classes, while retaining the original GH-166/GH-167 signed three-port and GH-170 nonhomogeneous Gauss source. Native divided-power, [X]U mod p², semilinear Frobenius/eta and p373 obligations remain with authorized Source owner. Gateway v0.6.11 (read this turn): research_authority_granted=false, executor_binding_configured=false, 5/5 active jobs, CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. No callable recovery_status exposed despite advertised status payload. No old service session, protected staging, maintenance conversation, scheduler or source pin was changed. Native restoration: issue #1558; p373 experiment: #1559. Formal role-bound continuation must first reconcile exact pending requests, current session and winning claim against fresh Source.

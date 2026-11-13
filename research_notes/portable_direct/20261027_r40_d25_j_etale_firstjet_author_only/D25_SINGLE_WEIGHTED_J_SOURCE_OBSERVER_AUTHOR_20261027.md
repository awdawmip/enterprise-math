# D25 auxiliary CM: one weighted scalar selects the two local source sheets

2026-10-27; AUTHOR-DERIVED, exact algebra and author finite-ring checks. Portable evidence in Draft PR #1566 only. UNREVIEWED / NOT_ADMITTED / NOT_A_NATIVE_CHECKPOINT / REGISTER_PENDING.

Parent Objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`; Taskbook blob `53a3ef039325534e3715add837f0eee332289984`. Uses earlier *author-only* two-sheet (t,J) collision and first-jet result already in this Draft PR; no independent reviewer is implied.

Let `s²=2`, `x=27h`, and

```
t(x)=x/[27(1+x)^2],   J(x)=27(1+x)(1+9x)^3/x,
x_plus=3+2s, x_minus=3-2s, t0=1/216.
```

For every prime p>=7, use `O_p=Z_p[s]/(s²-2)` and the source balls `B_±=x_±+pO_p`. The involution x↦1/x swaps them and preserves t. Each t-map is a bijection onto `t0+pO_p`, by the simple-root Hensel criterion. Define the *single* weighted readout

```
M(x)=(9+6t*d/dt)J(x)
    =9J(x)+6*x*(1+x)/(1-x)*J'(x).
```

**Proved theorem (full local family, all p>=7):**

```
M(x)-M(1/x) ≡ -50388480*s = -2^9*3^9*5*s (mod p)
```

for any `x∈B_+`. The residual coefficient is a p-adic unit for p>=7. Thus (t,M mod p) distinguishes the two same-t source sheets, including the exceptional primes p=13 and p=19 for which the earlier (t,J) observation alone has exact local collisions. Only the declared balls and same-t operation are in scope: no global injectivity or original LIFT claim follows.

**Proof.** Set `S=x_+(t)+x_-(t)=1/(27t)-2`, `d=x_+(t)-x_-(t)`, so `d²=S²-4`, `d'/d=SS'/(S²-4)`. Consume the earlier proved *rational-function* identity `J(x_+(t))-J(x_-(t))=A(t)d(t)` where `A(t)=27*(t^-1-64)*(t^-1-8)`. The weighted difference is `C(t)d(t)`, with

```
C(t)=9A(t)+6t*A'(t)+6t*A(t)*S(t)*S'(t)/(S(t)^2-4).
```

At t0=1/216, the exact input values are `S=6`, `d=4s`, `d'/d=-324`, `A=853632`, `A'=-453496320`, and `6t0=1/36`. Thus `9A+(6t0)A(d'/d)=0` and

```
C(t0)=A'(t0)/36=-12597120=-2^7*3^9*5,
C(t0)*d(t0)=-50388480*s.
```

All displayed denominators are local units for p>=7, so the same nonzero residue holds on the entire t-ball. Direct substitution further gives the exact fixed CM values `M(x_±)=-35577792∓25194240*s`.

**Constructive source decoding.** The symmetric trace `M_sym(t)=(M(x_+(t))+M(x_-(t)))/2` belongs to Q(t). Given sufficiently precise t and M, `d=2(M-M_sym(t))/C(t)`, `x=(S(t)+d)/2`. Mod-p M selects the ball; recovering full x requires sufficient precision for t and M. p=5 is a genuine excluded boundary: C(t0) is divisible by 5, so this M does not separate the two balls mod 5.

**Exact author check.** The companion Python checker evaluates J, J' and M directly, *not* via C, in `(Z/p^4 Z)[s]/(s²-2)`. It passed all 166 D25 target primes p<5000, four deformations per prime (664 tests), plus p=5 negative-boundary validation. Author checking is not independent review.

**BRC type and limits.** Two labeled source balls, signed odd-sheet difference, same-t involution and first derivative observer. This is a single-scalar compression of the previously published author observation pair (J,H), not a theorem on actual original H0/B0 `[X]U` or weighted hypergeometric `W_p`. Neither matching the coefficient 6 nor finite tests proves an original-class Frobenius transfer.

**Native status from read-only checks 2026-10-27.** Gateway 0.6.11 continuation and exact task reads: CONTROL_QUOTA. Historical `r40_20261027_1140_cont_read` receipt: CONTROL_REQUEST_NOT_FOUND. Winning CLAIM/OPEN/run and Source checkpoint unverified; no native mutation made. For any `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS` seed, `frontier_notes.completed_units=[]`; this portable author result is current staging, not predecessor completed research. Issue #1559 still requests genuine p=373 H0/B0 original-class evaluation with no claimed owner or executed native benchmark. UR V2 original four-file 94,687-byte, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` remains unverified in the bounded source search. The next scientific act is a *source-authenticated original-class* transfer or strict LIFT certificate, not another auxiliary j-only result. Neither P000 nor the scientific source pin nor the scheduled research task settings changed.

# D25 / SECOND-DIGIT-LIFT — independent E3 3-isogeny source alignment and signed de Rham normalization gate

Date: 2026-10-27. Logical Research lane: `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). 
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; mother `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Frozen SCIENTIFIC Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.
Classification: **AUTHOR-SIDE EXACT EXTERNAL-SOURCE ALIGNMENT / SYMBOLICALLY CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0B0 / NOT_SOURCE_CHECKPOINT / NOT_LIFT_PROOF**. No ownership or independent review is claimed.

## 1. Actual fresh source and novelty boundary

Babei–Roy–Swisher–Tobin–Tu, *Supercongruences arising from Ramanujan-Sato Series*, arXiv:2408.08844v3 (12 March 2025), Appendix Proposition 7.1, independently gives a 3-isogeny from the **original** E3 family to a specific cubic and an explicit `-3`-twist map to the conjugate family. This predates our separate author-side Vélu construction: the bare 3-isogeny/twist is prior art and must not be credited as a new external theorem.

The same paper's Theorem 2.1 and example (6.8) identify the *exact* weighted hypergeometric `F_{6,(1/2,1/3,2/3)}(1/2)` with a proved congruence modulo `p^2` and a **numerically supported, not proved there, modulo-`p^3` strengthening** (reported for primes `5 <= p < 150`). By the exact factorial identity
`
(1/2)_n(1/3)_n(2/3)_n / (n!)^3 * (1/2)^n
 = binom(2n,n)^2 binom(3n,n)/216^n,
`
this is the original D25 `W_p`, not the distinct Guo–Zudilin companion `S_p`. For `p % 24 in {13,19}`, `(2/p)=(-6/p)=-1`, hence the CM curve has the supersingular sign `sgn=-1` and the published `p^2` right-hand side `sgn*( (1/2)/p )*p=p`. Equation (6.8) asks for the next digit, which is **exactly** the already-source-aligned `Delta_p-R_p=(W_p-p)/p^2 mod p`. This identification **does not** promote (6.8) into a theorem, prove LIFT, or imply native H0/B0 execution. It narrows the external-prior-art proof gap to the supersingular third digit.

Source (page 23, Proposition 6.3 and equation (6.8); page 25, Proposition 7.1):
https://arxiv.org/pdf/2408.08844
Author source-port identity reused, not reproved:
`research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md`.
Author original 3-isogeny proof consumed, not recredited:
`research_notes/portable_direct/20261027_onhour_d25_original_E3_three_isogeny_CM_exchange.md`.

## 2. NEW exact coordinate comparison to the independent published quotient

Work over `Q(t)` with `c=t/27`, `t != 0,1`, and
`
E_t: y^2+xy+cy=x^3,  v=y+(x+c)/2,
v^2=f_c(x)=x^3+(x+c)^2/4,
omega=dx/(2v), eta=x*omega.
`
Consume the already-derived actual rational Vélu isogeny (kernel `{O,(0,0),(0,-c)}`):
`
U=x+c/x+c^2/x^2,
V=v*(1-c/x^2-2*c^2/x^3),
V^2=f_{3,c}(U)
   =U^3 + U^2/4 -(9*c/2)*U - c*(27*c+4)/4,
dU/(2V)=omega.
`
In the 2025 paper's Appendix Prop. 7.1 the quotient is written instead as
`
E'_3(t): Y^2=g_t(X):= X^3 - (3/4)*(X-(1-t)/9)^2.
`
A full coefficient comparison (for the **whole rational family**, not merely the CM point) yields
`
[EXACT] f_{3,t/27}(X-1/3) = g_t(X),
[EXACT] g_t(X) = -27*f_{(1-t)/27}(-X/3).
`
Thus the precise coordinate transportation is **X=U+1/3, Y=V**, not `X=U`, and the target conjugate coordinate is `x^sigma=-X/3`. No change of t, curve, 3-isogeny kernel or CM class was made.

## 3. NEW signed lift: two valid isomorphism choices, different de Rham columns

Adjoin `u^2=-3` and let `sigma(t)=1-t`. The published Appendix chooses, after splitting its `-3` twist, the target coordinate
`
x^sigma=-X/3, v^sigma_+=V/(3u).
`
The previously saved author `psi_3` chose instead
`
x^sigma=-X/3, v^sigma_-=-V/(3u)=V/u^3.
`
Both satisfy the *same original conjugate curve equation*, because `(3u)^2=-27`. The two maps differ by the genuine negation automorphism `[-1]` of the TARGET elliptic curve. They have the same kernel and degree but different signed differential transports.

Using `dX/(2V)=omega`, exact cohomological reduction `U*omega ~ 3*eta`, and `X=U+1/3`, the pullbacks on the entire ordered original de Rham basis `(omega^sigma,eta^sigma)` are

`
Appendix-positive v^sigma_+:
 psi_{3,+}^*(omega^sigma) = -u*omega,
 psi_{3,+}^*(eta^sigma)   ~ +(u/9)*omega + u*eta,
 M_{3,+} = [[-u,+u/9],[0,+u]].

Prior author-negative v^sigma_-:
 psi_{3,-}^*(omega^sigma) = +u*omega,
 psi_{3,-}^*(eta^sigma)   ~ -(u/9)*omega - u*eta,
 M_{3,-} = [[+u,-u/9],[0,-u]].
`

**Exact sign relation:** `M_{3,+}=-M_{3,-}`, but `det M_{3,+}=det M_{3,-}=3` and `M_{3,+}^2=M_{3,-}^2=-3 I`. The scalar degree, trace of conjugate curves, quadratic norm, or squared CM operator is therefore **incapable of detecting this choice**. A native original-class Frobenius/comparison claiming the specific signed `M_{3,-}` must authenticate which `v^sigma` choice (and which cohomological basis) it actually used. The paper alone does NOT fix the sign of our earlier author-defined map, because its chosen twist isomorphism is the opposite map.

This is an externally grounded sign/observer discrimination and a precise provenance correction. It does NOT imply a particular native `[X]U` value or a replacement for the genuine Gauss–Manin normalizer.

## 4. Exact p=373 witness and reproducible verifier

At `p=373`, choose `u=177` with `u^2=-3 mod p`, and work in the scalar subfield of `F_373[T]/(T^2-2)`. The two matrices are
`
M_{3,-} = [[177,229],[0,196]],
M_{3,+} = [[196,144],[0,177]],
M_{3,+}=-M_{3,-} (mod 373).
`
Both square to `370 I = -3 I` and have determinant `3`. The scalar `1/u^3` is `144` and `1/(3u)` is `229`, so the target-coordinate signs are explicitly different.

Executed exact symbolic/finitary check below using SymPy and integer modular operations (ordinary external algebra, NOT native X6/BRC or H0/B0):
```python
import sympy as S
X,t=S.symbols('X t')
c=t/27
F=lambda z:S.expand(z**3+z**2/4-S.Rational(9,2)*c*z-c*(27*c+4)/4)
G=S.expand(X**3-S.Rational(3,4)*(X-(1-t)/9)**2)
cs=(1-t)/27
Fs=lambda z:S.expand(z**3+(z+cs)**2/4)
assert S.factor(F(X-S.Rational(1,3))-G)==0
assert S.factor(G+27*Fs(-X/3))==0
p,u=373,177
assert (u*u+3)%p==0
inv9=pow(9,-1,p)
Mminus=S.Matrix([[u,(-u*inv9)%p],[0,(-u)%p]])
Mplus=-Mminus
assert Mminus.applyfunc(lambda v:v%p)==S.Matrix([[177,229],[0,196]])
assert Mplus.applyfunc(lambda v:v%p)==S.Matrix([[196,144],[0,177]])
for M in (Mminus,Mplus):
    assert (M*M).applyfunc(lambda v:v%p)==S.eye(2)*370
    assert M.det()%p==3
assert pow(pow(u,3,p),-1,p)==144
assert pow(3*u,-1,p)==229
print('SOURCE_ALIGNED_SIGNED_THREE_ISOGENY_PASS')
```

## 5. BRC/observer/continuation and nonnative gate

BRC composition applied: preserve original `E_t` and conjugate `E_{1-t}`, the translated quotient `X=U+1/3`, the two explicit `[-1]`-related target embeddings, orientation `sigma`, sign `u`, full de Rham basis and both columns, together with modulo-`p^3` weighted W observer. The safe quotient `M_{3,+}^2=M_{3,-}^2` preserves only the declared squared operator, **not** signed differential/Frobenius downstream observation. This is an external rank-two algebraic curve model, NOT an automatic native Enterprise X6 slice.

Mother D25/LIFT/JT2 remains **OPEN**, and its accepted D24 UR/JT0 sources remain frozen. The same-original-class H0/B0 divided-power benchmark is **PENDING_OWNER / NATIVE_NOT_EXECUTED**; existing support `#1559` still requires original `[X]U mod 139129`, actual native rank, Frobenius direction and eta, odd signed Green/Hesse observer, same-definition kappa and original Delta-R. The concrete native acceptance delta is to record the **target sign choice** and compare both columns of the actual 3-isogeny/basis map before using a signed CM eigenbasis or a Frobenius square. No native owner/compute is inferred from this proof.

Last own Research bridge `#6576` dispatch `FAILED/TimeoutExpired`; last recovery `#6575` had `source_authority_verified=false`. This run's Site gateway read-only task lookup returned `CONTROL_QUOTA`; no own winning Source CLAIM/open/run, therefore no Source-native checkpoint/Result/review/freeze. Previously staged records are not incorporated; `REGISTER_PENDING/SYNC_DEBT`. Do not use the maintenance conversation.

NEXT EXACT ACTION: a lawful canonical Source/native executor of existing `#1559` identifies the original fixed H0/B0 representative and sign of the target isomorphism, provides both de Rham columns and raw p373 `[X]U mod 139129` with full normalization/observer evidence, and independently validates any E3 comparison. Portable follow-up only if canonical route permits; no additional auxiliary proof substitutes the benchmark. Preserve Source pin and hourly task configuration.

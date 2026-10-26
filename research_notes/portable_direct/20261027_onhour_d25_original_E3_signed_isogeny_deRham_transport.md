# D25 / original E3: exact signed Galois 2-isogeny and de Rham transport

**Date:** 2026-10-27. **Lane:** TASK_RESEARCH, `chatgpt-research-onhour-enterprise-math-20260923` (not `chatgpt-hourly-enterprise-math-20260921`, not the other `research-hourly` lane). **Mother:** `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. **Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific input:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

**Evidence class:** exact hand derivation + executed symbolic polynomial identities / **AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NOT_NATIVE_H0_B0 / NOT_SOURCE_CHECKPOINT / NOT_RESULT**. This is an explicit *original-curve* transport available for testing a future native Frobenius/companion basis identification; it is **not** an identification of this 2-isogeny with the original native H0/B0 operator, a LIFT proof, or an independent review. The algebra is an instance of the classical Vélu 2-isogeny, not a newly invented axiom.

## 1. Smallest new discriminating question

Existing source-aligned results already prove the frozen scalar-port identity `Delta_p-R_p=(W_p-p)/p² (mod p)`, and an existing author-side exact original-E3 coefficient test rules out `b=a+6*partial_lambda|z a` and all base-field fixed-z rescalings at p=373 **under a specific proposed normalized companion condition**. The true transport/normalizer required to compare that untransported derivative with a geometric operator remains unidentified; the native divided-power `[X]U` experiment is still absent.

Rather than add another W-sum scan, compute an actual original-model map between the two CM conjugate curves and its full *signed* action on their natural de Rham basis, and separately compute a source-tied Gauss–Manin connection. Both are falsifiable inputs when a native H0/B0 implementation proposes a basis/coordinate transport; neither silently defines that implementation.

## 2. Exact original elliptic curves, rational 2-torsion, quotient

Work over `K=Q(s)`, `s²=2`, with `sigma(s)=-s`. Fix
```
t=(2-s)/4,   t^sigma=(2+s)/4=1-t,
c=t/27,      c^sigma=(2+s)/108.
E_t: y²+x*y+c*y=x³.
v=y+(x+c)/2;   v²=x³+x²/4+c*x/2+c²/4.
omega=dx/(2*v)=dx/(2*y+x+c);   eta=x*omega.
```
The original cubic contains a K-rational point of order two `(x,v)=(e,0)` with
```
e=(2*s-3)/36.
```
For `X=x-e`, the original equation becomes *exactly*
```
v²=X³+A*X²+B*X,
A=s/6,          B=1/144-s/216.
```
The conjugate model has `e^sigma=(-2*s-3)/36`, `A^sigma=-s/6`, `B^sigma=1/144+s/216`. All identities hold in `Q(s)`, not as fitted modulo-p equalities.

Apply the degree-2 Vélu map with kernel `{O,(X,v)=(0,0)}`:
```
U=X+A+B/X,             V=v*(1-B/X²).
V²=U³-2*A*U²+(A²-4*B)*U.
```
The two crucial *independently checkable* coefficient identities are
```
-2*A = 2*A^sigma,
A²-4*B = 4*B^sigma.
```
Therefore the quotient's coordinates rescale to the **original conjugate E3 curve**, not an ordinary Hesse substitute:
```
X^sigma=U/2,  v^sigma=V/(2*s),
x^sigma=X^sigma+e^sigma,
y^sigma=v^sigma-(x^sigma+c^sigma)/2.
```
This rational map `psi:E_t -> E_{t^sigma}` is a separable degree-2 isogeny and pulls back the target original invariant differential by
```
psi^*(omega^sigma)=s*omega.
```
Consequently the Galois-conjugate map has multiplier `-s`, and `psi^sigma o psi` has multiplier `-s²=-2` and degree four. Since we are in characteristic zero, an elliptic-curve endomorphism is determined by its action on the invariant differential; hence
```
psi^sigma o psi = [-2].
```
**The minus sign is observable.** Degree four or a norm-only quotient would fail to distinguish `[+2]` from `[-2]`. On the original K-rational three-torsion point `P=(0,0)`, direct substitution yields `psi(P)=(0,-c^sigma)=-P^sigma` and `psi^sigma psi(P)=P=[-2]P`, an independent signed torsion check.

## 3. A full rank-two original de Rham transport matrix

Do not infer the companion from the invariant differential alone. For the original `H^1_dR(E_t)` basis `(omega,eta=x*omega)`, compute the second image. The following **exact differential** on the *same translated cubic* is the missing reduction:
```
d(v/X) = (X-B/X)*omega.
```
Hence `(B/X)*omega` and `X*omega` are cohomologous, without discarding a signed branch by taking its norm. Pulling back the *original conjugate* `eta^sigma=x^sigma*omega^sigma` gives
```
psi^*(eta^sigma)
  = s*(U/2+e^sigma)*omega
  = s*(X/2+A/2+B/(2X)+e^sigma)*omega
  ~= s*(eta + (e^sigma+A/2-e)*omega)
  = s*eta - omega/18
```
where `~=` means equality of algebraic de Rham classes and `e^sigma+A/2-e=-s/36`.

With *columns denoting target basis elements expressed in the source basis*, the exact matrix is
```
M_psi = [[s, -1/18], [0, s]],
M_psi_sigma = [[-s, -1/18], [0, -s]],
M_psi * M_psi_sigma = -2 * I_2.
```
Thus both the degree and the signed composition survive a full two-dimensional de Rham transport check; the off-diagonal term `-1/18` is **nonzero** and disappears if one retains only the one-form eigenvalue `s`. This is a concrete, original-class *basis-mixing* datum for future native comparator authentication, not a claim about the rank of H0/B0.

**Modular exact witness, p=373.** Here `K` reduces to `F_373[T]/(T²-2)`, `sigma(T)=-T`, and `(-1/18) mod 373=145`. The two matrices are
```
M_psi mod 373       = [[T, 145], [0,T]],
M_psi_sigma mod 373 = [[-T,145], [0,-T]];
M_psi*M_psi_sigma   = 371*I = -2*I mod 373.
```
The same rational formulas have p-unit denominators for every declared target prime `p≡13,19 mod24`; modular validity of this *2-isogeny transport* at good reduction is not a uniform LIFT certificate.

## 4. Independent original-family Gauss–Manin operator, exact cohomology reduction

For the original family and the **fixed original Weierstrass x-coordinate** (not the previously tested fixed formal z-derivative), set
```
F=4*x³+(x+c)²,   Y=2*y+x+c,   omega=dx/Y,   eta=x*dx/Y.
partial_c omega = -(x+c)*dx/F^(3/2),
partial_c eta   = -x*(x+c)*dx/F^(3/2).
```
Use only exact differentials
```
d(Q/Y) = [Q'*F - Q*F'/2]*dx/F^(3/2)
```
to reduce the two derivatives to the original cohomology basis. Solving polynomial identities gives
```
nabla_c omega = -9/(27*c-1)*omega -3/[c*(27*c-1)]*eta,
nabla_c eta   =  1/(27*c-1)*omega +9/(27*c-1)*eta,
Q_omega = [1 - 3*(12*c-1)*x/c + 12*x²/c]/[2*(27*c-1)],
Q_eta   = -[3*c+5*x+36*x²]/[2*(27*c-1)].
```
These claims mean precisely
```
P = (a+b*x)*F + Q'*F-Q*F'/2
```
for `P=-(x+c)` and `P=-x*(x+c)`, respectively, with the displayed (a,b,Q). They are direct symbolic identities and do not posit a target as an axiom.

Since `c=t/27`, in the ordered basis `(omega,eta)` with columns for basis inputs,
```
Gamma_t = [[-1/[3*(t-1)],  1/[27*(t-1)]],
           [-3/[t*(t-1)],  1/[3*(t-1)]]].
```
At `t=(2-s)/4`, `t*(t-1)=-1/8`, so
```
Gamma_t(t0) = [[(4-2*s)/3,(-4+2*s)/27],
               [24,         (-4+2*s)/3]],
trace=0, determinant=8/9.
```
This is a **fixed-x Gauss–Manin matrix**, **not** the fixed-z formal derivative `J_plain`, **not** a Frobenius matrix, and **not** a claim that the correct H0/B0 normalization is its trace/determinant. They are different typed operations. In particular one cannot transfer the p373 base-field fixed-z no-go to this matrix without proving the coordinate/basis map.

## 5. Executed symbolic certificate, limitations, next native action

Local exact SymPy polynomial arithmetic was executed for the original model. Independent checks returned zero for: original 2-torsion cubic, translated cubic, Vélu quotient identity, both conjugate quotient coefficient equations, reduction `d(v/X)`, `e^sigma+A/2-e=-s/36`, the image of P, signed de Rham composition `M_psi*M_psi_sigma=-2I`, both Gauss–Manin polynomial reductions, the CM-specialized Gamma entries and determinant. No floating-point operations, random trials, `sorry`, `admit`, new axioms or guessed native values.

Minimal exact reproducer (requires SymPy, equality 0 is the certificate):
```python
import sympy as S
x,s,c,t,A,B=S.symbols("x s c t A B")
def red(q):
    n,d=S.fraction(S.cancel(q))
    return S.factor(S.rem(S.Poly(n,s),S.Poly(s*s-2,s)).as_expr()
                    /S.rem(S.Poly(d,s),S.Poly(s*s-2,s)).as_expr())
tt=(2-s)/4; cc=tt/27; e=(2*s-3)/36
a=s/6; b=S.Rational(1,144)-s/216
ec=(-2*s-3)/36; ac=-s/6; bc=S.Rational(1,144)+s/216
assert red(e**3+e**2/4+cc*e/2+cc**2/4)==0
assert red((x+e)**3+(x+e)**2/4+cc*(x+e)/2+cc**2/4-
           (x**3+a*x*x+b*x))==0
u=x+a+b/x; f=x**3+a*x*x+b*x
assert S.cancel((1-b/x**2)**2*f-(u**3-2*a*u*u+(a*a-4*b)*u))==0
assert red(-2*a-2*ac)==red(a*a-4*b-4*bc)==0
assert S.cancel(S.diff(f,x)/x-2*f/x**2-(x-b/x))==0
assert red(ec+a/2-e+s/36)==0
M=S.Matrix([[s,-S.Rational(1,18)],[0,s]])
Ms=S.Matrix([[-s,-S.Rational(1,18)],[0,-s]])
assert all(red(v)==0 for v in M*Ms+2*S.eye(2))
F=4*x**3+(x+c)**2
def check(P,aa,bb,Q):
    return S.factor((aa+bb*x)*F+S.diff(Q,x)*F-Q*S.diff(F,x)/2-P)
assert check(-(x+c),-9/(27*c-1),-3/(c*(27*c-1)),
             (1-3*(12*c-1)*x/c+12*x*x/c)/(2*(27*c-1)))==0
assert check(-x*(x+c),1/(27*c-1),9/(27*c-1),
             -(3*c+5*x+36*x*x)/(2*(27*c-1)))==0
G=S.Matrix([[-1/(3*(t-1)),1/(27*(t-1))],
            [-3/(t*(t-1)),1/(3*(t-1))]])
G0=S.Matrix([[(4-2*s)/3,(-4+2*s)/27],[24,(-4+2*s)/3]])
assert all(red((G.subs(t,tt)-G0)[i,j])==0 for i in range(2) for j in range(2))
assert red(G0.det()-S.Rational(8,9))==0
print("EXACT_SYMBOLIC_CERTIFICATE_OK")
```

**Applied BRC observer discipline:** `COMPOSE_APPLIED` to *the actual classical finite-field/algebraic carrier* `(E_t,E_{t^sigma},K/sigma,psi,psi^sigma,H^1_dR,omega,eta,three-torsion P)`. Source, target, conjugation, operation order and signed composition are retained. The scalar degree `4` loses sign; the single eigen-differential multiplier loses the `-1/18` mixing port. We proved what those quotients discard instead of silently treating them as observer-complete. The quadratic coefficient extension is **not** the project's X6 native space or a two-dimensional native plane. Existing P000/ACTIVE residual-fidelity worldview is unchanged.

**No native benchmark performed.** The actual original H0/B0 divided-power `[X]U mod139129`, H0/B0 rank, semilinear Frobenius direction and twist, **two-digit** normalizer `eta`, original signed odd Green/Hesse, `kappa` and `Delta_p-R_p` are still not supplied by this note. Issue [#1559](https://github.com/awdawmip/enterprise-math/issues/1559) remains `PENDING_OWNER / NOT_EXECUTED`. An authorized original-H0/B0 executor should now (a) state whether its basis/transport uses this *actual original* degree-2 map (if not, retain its distinct source), (b) if yes compare both columns of `M_psi`, the Galois conjugation and `[-2]` signed composition at p373 before inferring any normalized Frobenius, (c) reproduce `[X]U` and the signed native ports under the frozen task conditions, and (d) only then source-checkpoint and seek independent review. Do not promote a match to this de Rham certificate alone into a native benchmark PASS or LIFT.

**Recovery / no replays:** Onhour original [#6556](https://github.com/awdawmip/kimi-query-bridge/issues/6556) last read has local `session_state=ACTIVE`, `source_authority_verified=false`, no own CLAIM/open/run; own dispatch [#6529](https://github.com/awdawmip/kimi-query-bridge/issues/6529) finalized `FAILED/TimeoutExpired`; own continuation [#6557](https://github.com/awdawmip/kimi-query-bridge/issues/6557) rejected `PREREQUISITE_NOT_SUCCEEDED`. This turn's read-only Site exact continuation returned `CONTROL_QUOTA`, checkpoint-list `ACCESS_DENIED`, and `research_authority_granted=false`. None is `NO_DISPATCH`. Another Research-hourly lane's `HANDOFF_READY` packet and the maintenance lane's readback are evidence, **not this lane's owner/session/claim**, and no mutation was replayed. Existing neutral preserved staging remains independent. Next attempt must read the current actual onhour subject/session recovery/receipt and Source continuation, reconcile any unresolved original request before own legal typed successor and CLAIM/OPEN; absent Source-native authority this GitHub file is evidence preservation only, `REGISTER_PENDING / SYNC_DEBT`. No scheduler, frozen science pin or notification settings were changed.

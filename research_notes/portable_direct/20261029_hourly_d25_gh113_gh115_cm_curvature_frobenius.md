# D25/LIFT GH-113–GH-115 — CM branch, square curvature and exact Frobenius trace

Date: 2026-10-29 Asia/Hong_Kong. Author-side portable mathematical research; logical Research lane `chatgpt-research-hourly-enterprise-math-20260923`, not the CONTROL_PLANE_MAINTENANCE lane. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. Mother D25/LIFT/JT2 OPEN; historical frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. No native Research session/CLAIM/OPEN/checkpoint was obtained.

## Exact source and type boundaries

Fix a prime `p=8m+3>=11`, `d=2m`, `k=F_p`, `D=binom(3m+1,m) in k^*` and `theta=z d/dz`. Reuse the GH-100 *reflected*, not original GH-3, source:

```
h_0=1, h_(j+1)/h_j=(4j+3)^3/((4j+4)(4j+5)(4j+6)), 0<=j<d
U(z)=sum_(j=0)^d h_j z^j
H(z)=(8 theta+5)U(z)
R(z)=sum_(j=0)^d ((8j+5)h_j/(d+1+j)) z^(d+1+j)
R'(z)=z^d H(z).
```

All denominators are p-units. GH-100/102 supply `G(z)=z^m E_p(1-z^(-1))` in `k[z]`, `U=D^(-2)G^2`. Put `A(z)=16zG'(z)+5G(z)`; then **as whole polynomial identities**,

```
H(z)=D^(-2)G(z)A(z),
R'(z)=D^(-2) z^(2m) G(z)A(z),
z(1-z)G''(z)+(5/4-7z/4)G'(z)-9G(z)/64=0  (over k).
```

The last equation is GH-100's hypergeometric differential equation reduced using `m=-3/8` in k. These are external finite-field auxiliary observations, not native Heartbeat World X6 coordinates.

## GH-113: CM discriminant -24 transported to the reflected Hasse port

GH-100 defines the *actual* elliptic cubic

```
C_T: v^2=u^3+u^2+((1+T)/8)u, T^2=8/9.
```

Its Hasse coefficient `Ha_p(T)=[u^(p-1)]f_T(u)^((p-1)/2)=P_(2m)(T)=E_p(T^2)`. This identity is polynomial and square-root-free; `E_p(8/9) in F_p`, even when `T` lies in `F_(p^2)\F_p`. For `b=(1+T)/8`, direct standard Weierstrass invariant algebra yields

```
c4=16(1-3b), Delta=16 b^2(1-4b),
j(C_T)=256(1-3b)^3/[b^2(1-4b)]
      =64(5-3T)^3/[(1+T)^2(1-T)].
```

In characteristic zero, choose `T=2 sqrt(2)/3`. Exact arithmetic in `Q(sqrt(2))` gives

```
j=2417472-1707264 sqrt(2),
j_conjugate=2417472+1707264 sqrt(2),
(X-j)(X-j_conjugate)=X^2-4834944X+14670139392.
```

The last polynomial is the **classical** Hilbert class polynomial `H_{-24}`, whose CM order is the maximal order of `Q(sqrt(-6))`; this classical identification is imported (not a new proof of a CM theorem). It matches the separate GH-74 CM invariant for a different auxiliary curve; the new bridge is to the GH-100 *reflected* source. Independent references: https://numberdb.org/Hilbert_class_polynomials , https://oeis.org/A305474 and GH-74 proof `research_notes/portable_direct/20261025_onhour_d25_cm_hasse_inert_zero_classification.md`.

Since `T^2=8/9 !=1` and p>3, the cubic has good reduction. Classical Deuring CM reduction: it is ordinary when p splits in `Q(sqrt(-6))`, supersingular when inert. The Hasse coefficient is nonzero exactly for the ordinary case. For p=8m+3, primes >3 have residues 11 or 19 mod 24, and quadratic reciprocity gives `(-6/p)=+1` for 11 mod24, `-1` for 19 mod24. Thus:

```
E_p(8/9) != 0  if p == 11 (mod 24)  [CM split],
E_p(8/9) == 0  if p == 19 (mod 24)  [CM inert].
```

Since `G(9)=9^m E_p(8/9)`, this provides a **full-prime classification of which factor of H=G*A/D^2 is zero at z=9**, conditional only for the split case on the separate GH-83 input `H(9)=0`:

```
CM inert (19 mod24): G(9)=0; G'(9)!=0; A(9)=144 G'(9)!=0.
CM split (11 mod24), if H(9)=0: G(9)!=0; A(9)=0.
```

The ordinary/supersingular dichotomy uses standard CM/Deuring results; it does NOT prove GH-83's separate all-prime stationarity assertion. Nor does it predict `R(9)=0`.

## GH-114: universal square curvature and a simpler ramified twist class

**Conditional theorem (exactly declared dependency):** for each `p=8m+3>=11` such that `H(9)=0` (GH-83 author-side stationarity input), `R''(9)` is a nonzero quadratic residue of `F_p`. More precisely:

**Inert / G-zero branch:** `G(9)=0` and the second-order ODE at 9 implies `G'(9)!=0`. Then

```
R''(9)=144*9^(2m)*G'(9)^2/D^2
      =(12*9^m*G'(9)/D)^2 != 0.
```

**Split / A-zero branch:** `G(9)!=0` and `A(9)=0` gives `G'(9)=-5G(9)/144`. The ODE at z=9 yields

```
G''(9)=209 G(9)/41472,
A'(9)=21G'(9)+144G''(9)=-G(9)/288 !=0,
R''(9)=-9^(2m)*G(9)^2/(288D^2).
```

Because `p==3 mod8`, `(-2/p)=+1` and `-1/288=(-2)/24^2` is a square, so this branch is also a nonzero square. The two formulas give a quantitative source-preserving distinction between CM-inert G-zero and CM-split A-zero stationary points, despite the same coarsened observation `H(9)=0`.

**GH-112 interaction:** if additionally `v_p(R_p(9))=1`, define `u=R_p(9)/p mod p` and `v=R_p''(9) mod p`. GH-112's ramified factor has `c=-2u/v mod p`. Because both `-2` and `v` are quadratic residues, **`chi_p(c)=chi_p(u)`**. The ramified quadratic field's twist class depends only on the *normalized first nonzero R-value*, not on which stationary CM factor vanished:

```
Q_p(sqrt(p*c)) is isomorphic to Q_p(sqrt(p*u_lift)).
```

This applies only to exact valuation-one exceptional primes in the stated branch. The first-digit vanishing remains an independent hard obligation.

For p=3347, `m=418`, `D=3073`, `E_p(8/9)=783`, `G(9)=3333`, `R''(9)=2331`. The split formula gives 2331; `chi(2331)=+1`. GH-112 previously obtained `u=1186`, `c=1465`; `chi(1186)=chi(1465)=-1`, and the exact field-class ratio is `c/u=2194=1052^2 mod3347`. This is consistent with, but does not replace, GH-112's complete degree-1673 polynomial check.

## GH-115: exact CM Frobenius sign and point count for p=3347

Let `q=3347^2=11202409`; form `F_q=F_p[r]/(r^2-2)` and use the curve `C_T` above with `T=2r/3`, `b=(1+T)/8=1/8+r/12`. This parameter lives in `F_q`, not `F_p`, while its Hasse coefficient is the base-field number 783.

An **independent exhaustive finite-field character sum**, using all q pairs `x=a+br` (rename the scalar coordinate `b_x` to avoid confusing it with the curve parameter), gave

```
a_q := q+1-#C_T(F_q) = -sum_(x in F_q) chi_q(x^3+x^2+((1+T)/8)x)
                    = -6106,
#C_T(F_q)=11208516.
```

For a nonzero `w=a+br` the quadratic character obeys `chi_q(w)=chi_p(a^2-2b^2)`. The executed C++17 exact loop computes this norm-character for every element; no float, sampling, native EM compute or external database substitute. Check also the derived Hasse congruence:

```
a_q == Ha_p(T) Ha_p(T)^p == E_p(8/9)^2 == 783^2 == 588 (mod3347).
-6106 == 588 (mod3347).
```

A direct proof of the congruence uses `f(x)=x^3+x^2+bx`, `F(x)=f(x)^((p-1)/2)`. In characteristic p, `a_q=[x^(q-1)] f(x)^((q-1)/2)` because the sum of positive monomials over `F_q` vanishes except at exponent q-1, and `deg f^((q-1)/2)<2(q-1)`. Since `f^((q-1)/2)=F(x)F(x)^p`, the unique exponents `i+p*j=q-1` with `i,j` in the degree range of F are `i=j=p-1`; the desired coefficient is `Ha_p(T)^(p+1)`. This proves the congruence without assuming it from point counts.

The separate CM arithmetic norm form is

```
3347 = 2*40^2 + 3*7^2,
alpha=(2*40^2-3*7^2)+2*40*7 sqrt(-6)
     =3053+560 sqrt(-6),
Norm(alpha)=3347^2, Trace(alpha)=6106.
```

The classical CM norm/Frobenius description restricts the ordinary trace to `±6106`; the **independently proved** Hasse congruence fixes the minus sign. The direct q-element count cross-checks the same signed answer. This is a new signed Frobenius port at p3347, not an explanation of why the separate reflected-tail value `R_{3347}(9)` vanishes. Do not merge CM trace, R-value, characteristic-p function-field monodromy, or GH-3's original source.

## Executed verification and observer discipline

Portable Python exact checker: `d25_gh113_gh114_cm_curvature_check.py` (Q(sqrt(2)) rational pairs, Legendre recurrence in Fp[T]/(T²-8/9), independent reflected h recurrence, hypergeometric F recurrence and complete second derivative). Actual run: `PASS_GH113_GH114_CM_REFLECTED_CURVATURE p_count 109 split 55 inert 54`, covering all 108 p=3 mod8 primes below 3000 and p3347. It independently verifies `H(9)=0` for those samples, not for the infinite prime family. Exact p3347 residual/crossclass checks pass.

Portable C++17 checker: `d25_gh115_cm_3347_frobenius_count.cpp`; actual run `PASS_GH115_CM_FROBENIUS_DIRECT_Q_COUNT`, with smaller exact controls p=11,19,43,59 and full 11,202,409-element p3347 enumeration. The rational CM invariant and Hasse source are independently computed by the Python checker. Full programs and stdout logs are preserved in the companion portable bundle; if code is not separately available as a GitHub file, the above identities and q-character algorithm remain the reproduction contract.

BRC resolution `COMPOSE_APPLIED`: carrier retains p and its prime-class, source/index h_j, elliptic cubic and CM discriminant, Fp versus Fp² coefficients, individual G/A branches, signed character sum, R modp versus valuation-one u, derivative v, squareclass c, ramified ± roots, and future operations (differentiate before specializing; Frobenius versus p-adic lift). Coarsening all data to a single Boolean zero loses both the CM factor label and twist. P000 ACTIVE, native X6 semantics and frozen scientific Source pin remain untouched.

## Scope, provenance, next executable scientific action

Reused GH-74's classical CM discriminant (no claim to discovering -24), GH-100's Hasse descent, GH-102's polynomial source, GH-112's ramified theorem, and independent GH-83's **author-side, not independently reviewed** stationarity input. Novel within this author-side cross-branch work: reflected-source full-prime split/inert port classification; explicit square-class curvature formulas; normalized-residue ramification simplification; and signed p3347 Frobenius/point-count certificate. Independent review of all author proof dependencies is pending, so no theorem or Source admission is asserted.

Next minimal math obligation: use the now *signed* CM Frobenius input `a_(3347²)=-6106` and the exact Hasse factor to seek a genuinely independent evaluation of `R_p(9)` (e.g. a finite-character-sum/Jacobi or CM p-adic period/WZ relation) that **predicts** `R_{3347}(9)=0`. A restatement of GH-98–GH-103's finite-log moment is not sufficient. Keep original GH-3 `T_(p,9)=0 mod p`, GH-83 Laurent residue, and native p373 verification separate. Formal Source recovery must first read its own exact recovery/continuation; no service CLAIM/session/Result/review is inferred from these GitHub files. Control issue: `awdawmip/enterprise-math#1558`.

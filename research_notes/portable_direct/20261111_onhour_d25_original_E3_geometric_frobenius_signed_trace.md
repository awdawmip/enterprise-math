# D25/LIFT — actual original E3 quadratic geometric Frobenius and signed 3-torsion certificate

Date: 2026-11-11 (Asia/Hong_Kong). **AUTHOR_SIDE / ALL-TARGET-PRIME MATHEMATICAL DERIVATION USING STANDARD CM / EIGHT FULL FINITE-FIELD CERTIFICATES / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0 / NO_SOURCE_CHECKPOINT.**

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen science commit `c47e13e4aba0e006366f989d6334d443f6333ae3` remains unchanged. This author's Research lane is distinct from control maintenance; no native claim, open execution or Result is asserted. Consume previously accepted CM0/SIMPLE/UR work and prior scalar/typed E3 observations without recrediting.

## 1. Specific scientific question and exact original object

The highest native unresolved gate remains the **same-original-class H0/B0 divided-power** representative and coefficient `[X]U mod 139129` at p=373, its module rank, semilinear direction, normalization eta, signed odd Green/Hesse kappa and native-to-original Delta-R map. Instead of another W216 auxiliary expansion, test a directly accessible, genuinely *original E3 geometric* Frobenius invariant with a falsifiable sign and independently reproducible raw count.

Take the original Chisholm–Deines–Long–Nebe–Swisher curve and parameter (as in the already accepted discriminant -24 CM source):

```text
E3(t): y² + xy + (t/27)y = x³
t = (2-T)/4,  T²=2, sigma(T)=-T.
p prime, p mod24 in {13,19}; k=Fp[T]/(T²-2)=Fp², q=p².
a3=t/27=(2-T)/108.
P=(0,0) in E3(k).
```

The two quadratic coordinates `(1,T)` are an external finite-field computation, **not** a primitive two-dimensional Enterprise space or an X6 3D slice. The odd branch/signed observers remain separately typed.

## 2. Exact theorem: q-Frobenius equals +[p] on the actual E3 curve

**Claim.** For every prime `p≡13,19 (mod 24)` (so p≥13), the geometric q-Frobenius endomorphism of the above E3 over k=Fp² satisfies

```text
pi_{p²} = [+p] in End(E3 / overline(Fp)),
trace(pi_{p²}|H^1) = +2p,
#E3(Fp²) = (p-1)²,
characteristic polynomial = X² - 2pX + p² = (X-p)².
```

**Argument.** The Weierstrass invariants of `a1=1,a3=t/27,a2=a4=a6=0` give `c4=1-24a3`, `Delta=a3³(1-27a3)`. Since `t(1-t)=1/8`, the curve has good reduction for every p>3. Exact rational calculation in Q(sqrt2) yields

```text
j(E3) = c4³/Delta = 2417472 + 1707264 sqrt(2)
j² - 4834944 j + 14670139392 = 0.
```

This is the discriminant -24 Hilbert class polynomial already used for accepted `CM0`. Hence E3 has geometric CM by the maximal order `O_K` of `K=Q(sqrt(-6))`, and its endomorphisms are defined over the compositum `K(sqrt2)` (standard CM Galois action on the full order; the curve is over Q(sqrt2)). In the two named residue classes, `(2/p)=(-6/p)=-1`; the prime has residue degree 2 in this compositum, so all CM endomorphisms act on the reduction over `Fp²`. (The ramified discriminant primes 2,3 are absent.)

The q-Frobenius commutes with every CM endomorphism defined over Fp². Its centralizer of `K` in the supersingular quaternion algebra is exactly `K`, so `pi_q∈K`. The Frobenius is an integral endomorphism, hence `pi_q∈O_K`, with degree/CM norm q=p². As p is inert in K and the only units of O_K are ±1, the only possibilities are `pi_q=+p` or `pi_q=-p`.

The original curve has a **k-rational nonzero point of order three** `P=(0,0)`: its tangent `y=0` meets the cubic at P with intersection multiplicity 3, since `a3=t/27≠0`. Both residue classes have `p≡1 mod3`; thus `[+p]P=P` whereas `[-p]P=-P≠P`. Since Frobenius fixes every k-rational point, the sign is **+**. The trace and point count follow from the elliptic curve Weil characteristic polynomial.

This is a uniform theorem on the explicitly stated geometric object, based on standard CM facts and the original-curve rational 3-torsion. The computation below independently checks the numerical consequences in eight exact finite fields; independent mathematical review is outstanding.

## 3. p=373 signed complete exact certificate

For `p=373`, `q=139129`, both independent complete character sums give

```text
#E3(F_139129) = 138384 = 372²,
a_q = q+1 - #E = 746 = +2*373,
chi_q(X) = X² - 746X + 139129 = (X-373)².
Original formal E3 Hasse coefficient H_{3,372}(t) = 0 in F_373[T]/(T²-2).
```

The point count uses every one of the `q` values `x=u+vT` and the **original curve's** discriminant

```text
D(x)=(x+a3)² + 4x³.
#E3(k) = q+1 + sum_{x in k} chi_k(D(x)),
chi_k(D)=Legendre_p(Norm_{k/Fp}(D)).
```

An independently implemented `D^((q-1)/2)` quadratic-character route, using separate generic extension-field multiplication and exponentiation, gives the same value; an independent original fixed-z binomial coefficient calculation gives Hasse zero. No floating-point arithmetic.

Eight complete field enumeration pairs:

| p | q=p² | #E3(Fq) | Frobenius trace `q+1-#E` | original Hasse `(1,T)` |
|---:|---:|---:|---:|---:|
| 13 | 169 | 144 | +26 | (0,0) |
| 19 | 361 | 324 | +38 | (0,0) |
| 37 | 1369 | 1296 | +74 | (0,0) |
| 43 | 1849 | 1764 | +86 | (0,0) |
| 109 | 11881 | 11664 | +218 | (0,0) |
| 139 | 19321 | 19044 | +278 | (0,0) |
| 157 | 24649 | 24336 | +314 | (0,0) |
| 373 | 139129 | 138384 | +746 | (0,0) |

Fully reproducible exact Python 3 standard-library integer script:
`research_notes/portable_direct/d25_e3_actual_frobenius_point_count_20261111.py`.

## 4. Native-class comparison gate and one useful conditional discriminator

On the true `H^1_{{cris}}(E3/W(Fp²))` (a rank-two object), the q-Frobenius is geometrically `+p`; this sharply fixes the **sign**, independent of ordinary Hesse-polynomial candidate normalization. It is a check on any proposed comparison from original-class H0/B0 source data to this geometric cohomology.

In contrast, if someone proposes to identify a **rank-one unramified sigma-semilinear** operator `F=a sigma` over `R=W_2(Fp²)` directly with this slope-half E3 Frobenius, then `F²=a sigma(a)` has either p-valuation zero (a unit) or at least two (p divides a), while the actual geometric `+p` has valuation one modulo p². That precise identification is impossible without a different carrier (e.g. an actual rank-two module), a declared ramified coefficient ring or a verified normalization/representation map. This is a **conditional model discrimination**, not an assertion about the currently unknown native H0/B0 module rank. The prior external Hesse candidate norm `122102 mod139129` is not substituted for `+p`.

The prior verified frozen original scalar at p373 remains `Delta_373=R_373=196`. The earlier exact fixed-z coefficient comparison `(H+6 d_lambda H-h)/373=92+24T mod373` remains a **different observer**; neither trace nor group order recovers `[X]U`, kappa, eta or the odd Green port.

**BRC actual use:** keep the original two conjugate parameter branches `T, -T`, retain the full signed character contribution before summation, identify `P=(0,0)` as a sign-discriminating source witness, and distinguish geometric `q`-trace observer from the native divided-power coefficient and odd branch operation. The safe total is the finite point-count trace **only under the declared geometric observer**; no quotient claim for the native observer.

## 5. Current task frontier, provenance, and next exact operation

`COMPLETE_AUTHOR_SIDE`: all-prime geometric Frobenius `+[p]` derivation and eight full finite exact dual-route certificates. `UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0`. No new Task publication, borrowed reviewer identity, platform claim, or frozen-science change.

`UNFINISHED_NATIVE`: read/construct the **actual fixed original H0/B0 divided-power** p373 representative, calculate `[X]U mod139129`, disclose true rank, Frobenius semilinear direction, exact basis/eta and the comparison map to original E3 `H^1` where applicable. Check its q-Frobenius signature against `+373` (under an authenticated comparison), preserve full signed Green/Hesse kappa and actual Delta-R, and reproduce independently. Broader mathematical LIFT all-prime cancellation remains open.

Responsible existing support issue: [enterprise-math #1559](https://github.com/awdawmip/enterprise-math/issues/1559); original-class evaluator owner PENDING, no claim is inferred. Current Source exact continuation `onhour11-20261111-0901-exact-cont` SUCCEEDED at Source `597de0cd00ef6447da19dde7a0d043cbcab8124e` with `execution_authorized=false`. Own recovery returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; author publication must not be confused with native checkpoint.

Sources consumed with their exact scopes: `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md` (CM -24, CM0/SIMPLE), `research_notes/portable_direct/20261111_onhour_d25_original_E3_formal_derivative_second_digit_port.md` (exact formal E3 observer), `research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md` (frozen Delta/R cutoff), original 2013 E3 Lemma12, and Source immutable continuation at the receipt above. Exact mathematical claims here are author derived; no independent reviewer is implied.

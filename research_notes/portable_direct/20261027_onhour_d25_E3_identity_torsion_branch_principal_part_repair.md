# D25 / SECOND-DIGIT-LIFT — E3 identity branch versus rational 3-torsion branch: exact Laurent-pole correction

2026-10-27; Research-onhour logical lane `chatgpt-research-onhour-enterprise-math-20260923`. **AUTHOR-SIDE / PROVED ALGEBRAIC BRANCH IDENTITY / EXECUTED EXACT FINITE RING CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE H0-B0 NOT_EXECUTED**. No claim, open, execution session, Source checkpoint, Result, Driver review, or native benchmark is asserted.

Parent objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; fixed Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source pin **`c47e13e4aba0e006366f989d6334d443f6333ae3` remains unchanged**. This correction targets the original E3 comparator, not the fixed native divided-power H0/B0 operator.

## Precise issue in previous author-side derivation

The immutable earlier note [20261027 original E3 second-kind closed coefficient](https://github.com/awdawmip/enterprise-math/blob/1f0463ea86c4d370a2c5d828f4766cf8bdc8420c/research_notes/portable_direct/20261027_onhour_d25_original_E3_second_kind_closed_coefficient_p373.md) declared `xi=-x/y` to be a local parameter **at the identity** yet selected

~~~text
x(xi) = ((1-xi) - sqrt(D(xi))) / (2 xi^2)
omega = - dxi / sqrt(D(xi)).
~~~

These are both algebraically valid **but belong to the finite rational 3-torsion point Q=(0,-c), not to the elliptic-curve identity O at infinity**. The same rational function `xi=-x/y` takes the value zero at two different points, so the branch/sheet of the quadratic equation must be part of the observer. Conflating the two points cannot be used to identify an original-identity Frobenius column.

## Full exact correction; no numerical hypothesis

Let `E_c: y² + xy + cy = x³` with `c≠0` over any characteristic-zero coefficient field, put `xi=-x/y`, `D=(1-xi)²-4c xi³`, and choose the unique power-series root `s=sqrt(D)` satisfying `s(0)=1`. Substitution `y=-x/xi` yields the exact quadratic

~~~text
xi² x² - (1-xi) x + c xi = 0.
~~~

Its two distinct local branches and their limits are

~~~text
x_O = ((1-xi)+s)/(2 xi²) = xi^-2 - xi^-1 + O(xi), y_O = -xi^-3 + ...;
x_Q = ((1-xi)-s)/(2 xi²) = c xi + O(xi²),  y_Q = -c + O(xi).
~~~

Therefore the **plus** root is the formal neighborhood of the identity `O` and the **minus** root is the neighborhood of the 3-torsion point `Q=(0,-c)`. Differentiating the exact quadratic and substituting into `omega=dx/(2y+x+c)` (or directly simplifying both explicit roots) gives

~~~text
H = 1/sqrt(D);
omega_O = +H dxi,     omega_Q = -H dxi.
~~~

For the genuine second-kind representative `eta=x omega` the **entire Laurent series**, not merely nonnegative coefficients, satisfies

~~~text
(x_O - x_Q) H = 1/xi²,
eta_O = xi^-2 dxi - eta_Q,
eta_Q = -x_Q H dxi.
~~~

Thus the earlier sequence `b_n = [xi^n](x_Q H)` is indeed **identical to the nonnegative-power (regular) coefficients of** `eta_O`; it is **not the whole second-kind differential**. Its missing source-labelled principal part is **`+xi^-2 dxi`** at the identity. Its claimed basepoint and signed differential must be corrected, without deleting useful exact regular coefficients.

Similarly the earlier positive sequence `a_n=[xi^n]H` is the correct actual identity invariant-differential coefficient because `omega_O=+H dxi`; it equals `-[xi^n](omega_Q/dxi)` only because the torsion-branch differential has the opposite sign. Thus the prior normalized formal-logarithm coefficient sequence is algebraically **salvageable**, but its derivation must be based on `O`, not silently on `Q`. This result **does not claim** that every downstream Frobenius/comparison/formal-group argument is validated by the repair.

## Explicit regular coefficients and p=373 exact recheck

Using `H=((1-xi)²-4c xi³)^(-1/2)`, the already recorded binomial formulas remain valid at the **indicated regular-part readout**:

~~~text
a_n = sum(j=0..floor(n/3)) binom(2j,j)*binom(n-j,2j)*c^j,

b_n = (1/2)*sum(j=1..floor((n+2)/3))
      binom(2j,j)*binom(n-j+1,2j-1)*c^j.
~~~

For the original `c=(2-T)/108, T²=2` and `p=373`, exact modular integer arithmetic in `(Z/373³)[T]/(T²-2)` rechecks:

~~~text
a_372 = 46042747 + 33130606*T mod 51895117;
b_372 = 40642453 + 16308355*T mod 51895117.
~~~

The second value represents the **regular coefficient** of `eta_O` and does not erase its pole. The coefficient calculations reproduce earlier finite values; the **new proof** is the exact branch/polarity/Laurent distinction and the recognition of its necessary operator-port type. No H0/B0 divided-power coefficient is calculated.

## Executed reproducibility checker (Python stdlib, exact integers)

The following exact program was executed successfully in this run with output `D25_E3_BRANCH_POLE_REPAIR_PASS`:

~~~python
"""Original E3 identity/torsion branch and second-kind pole, exact p=373 certificate.
Author-side / not a native divided-power H0/B0 calculation.
"""
from math import comb

p = 373
mod = p**3
zero = (0, 0)
one = (1, 0)

def add(a, b):
    return ((a[0] + b[0]) % mod, (a[1] + b[1]) % mod)

def mul(a, b):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % mod,
            (a[0]*b[1] + a[1]*b[0]) % mod)

def smul(k, a):
    return ((k*a[0]) % mod, (k*a[1]) % mod)

inv108 = pow(108, -1, mod)
c = (2*inv108 % mod, -inv108 % mod)  # c=(2-T)/108, T^2=2
powers = [one]
for _ in range(125):
    powers.append(mul(powers[-1], c))

def coeff_H(n):
    ans = zero
    for j in range(n//3 + 1):
        ans = add(ans, smul(comb(2*j,j)*comb(n-j,2*j), powers[j]))
    return ans

def coeff_regular_second_kind(n):
    ans = zero
    for j in range(1, (n+2)//3 + 1):
        ans = add(ans, smul(comb(2*j,j)*comb(n-j+1,2*j-1),powers[j]))
    return smul(pow(2,-1,mod),ans)

assert coeff_H(0) == one
assert coeff_regular_second_kind(0) == zero
assert coeff_regular_second_kind(1) == c
assert coeff_H(372) == (46042747,33130606)
assert coeff_regular_second_kind(372) == (40642453,16308355)
print('p=373, p^3=51895117')
print('H[372]:',coeff_H(372))
print('regular identity second-kind[372]:',coeff_regular_second_kind(372))
print('identity second-kind Laurent principal part: +xi^-2 dxi')
print('identity omega leading sign: +1; torsion omega leading sign: -1')
print('D25_E3_BRANCH_POLE_REPAIR_PASS')
~~~

## BRC and native benchmark: concrete information-loss witness

**COMPOSE_APPLIED, author-side.** Carrier: elliptic E3 local parameter value *plus* branch label `O/Q`, the signed differential, and full Laurent principal part. Observer: the actual original H0/B0↔E3 operator comparison including both cohomological basis columns, Frobenius orientation, and odd signed Green/Hesse port. Operation: choose an identity-based local expansion and subsequently transport a de Rham basis. The quotient retaining only `(a_n,b_n)` discards both the point label and the nonzero `xi^-2` polar component, so it has **not** been proved safe for these downstream operations. This is a concrete branch-fiber contrast, not a new native-X6 law; no external-elliptic-curve fact is promoted to the Heartbeat P000 worldview.

**Native correction required:** any actual executor working on issue [#1559](https://github.com/awdawmip/enterprise-math/issues/1559) must verify whether its signed `xi=-x/y` transport uses the **identity plus branch** and carries the **full** `(omega_O, eta_O)` basis, including principal part. Reject the old phrase “the minus root is the local identity” as a basis description. Merely reproducing `b_372` does not authenticate a second-kind Frobenius companion.

The **fixed** native H0/B0 divided-power benchmark remains **NOT_EXECUTED / PENDING_OWNER**: obtain actual `[X]U mod139129`, module rank, F semilinear direction and two-digit normalization, both signed basis columns and odd Green/Hesse port, original `kappa` and `Delta_p-R_p`, plus reproducible code/pin and independent check. A corrected E3 Laurent series cannot replace that experiment.

## Handoff and exact authority boundary

- Preserve the frozen D25 Source input, accepted D24 UR, all verified W/S finite hypergeometric data, and prior exact regular coefficients. **Do not redo** those units or convert this author-side correction into an admitted result.
- Previous identity-branch assertion requiring correction: original E3 second-kind coefficient note at `1f0463e...` and formal p-series exposition at `7129a3a...`. Correct their geometric interpretation in a subsequent authorized editorial transaction without overwriting immutable provenance.
- Mother / scientific frontier: D25 / LIFT / JT2 **OPEN**; proof of all-prime original third digit and **fixed** native H0/B0 output still pending. Next scientific act is an actual authorized original-object native execution or a separate rigorous all-prime proof, not another surrogate.
- Control: previous Recovery Issue `awdawmip/kimi-query-bridge#6575` is a historical pointer without proof of own claim/open; old Dispatch Issue `#6576` ended failed. A fresh direct continuation attempt this run returned `CONTROL_QUOTA`; Site gateway `0.6.11` reports `research_authority_granted=false`. No current Source-owned Researcher session / CLAIM / run is proven. `session/claim/run = NONE_VERIFIED`; the maintenance conversation is not used.
- Artifact is **AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Publication/readback of this file, if successful, certifies its bytes only, not theorem promotion, canonical Source checkpoint, or native experimental acceptance. No schedule, notification, Source pin, or Project P000 modification.

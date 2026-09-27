# Exact square inflation of the companion trace observer

Status: **PURE_SYMBOLIC_SHARED_CONTEXT_REVIEW / NOT_EXECUTED / NOT_ADMITTED**. This independently checks the parent author's strengthening of `FREE_TRACE_TORUS_WITNESS.md`, SHA-256 `6ad4bbf2db92ffbec7fc57c8da3e16aca9f43a6fb05b89a73aa396aca6f1730c`. The frozen parent note is unchanged. No scientific run, numerical example or remote operation was used.

Let N be odd, k an integer, `gcd(k^2-4,N)=1`, and

`M=[[0,1],[-1,k]]`, `v=(0,1)^T`, `r=M^E v-v=(x,y)^T`,

for a public integer E>=0. Coordinates can subsequently be reduced modulo N. Set

`g=gcd(N,x,y)`, `tau=tr(M^E)-2`.

Then the exact integer divisor identity is

`gcd(tau,N)=gcd(g^2,N)`.                                  (1)

It preserves neither an unsaturated prime-power valuation nor the exact common-return gcd merely to replace the two-coordinate observer by trace. The loss is precisely the squaring in (1).

## Proof

Cyclicity of v and commutation with M give

`B=M^E-I=[[y-kx,x],[-x,y]]`.

Thus `tau=2y-kx`. Because `det(M^E)=1`, the two-by-two determinant identity `det(I+B)=1+tr(B)+det(B)` gives

`tau=-det(B)=-(x^2-kxy+y^2)`.                              (2)

Fix `p^e || N`; p is odd and `Delta=k^2-4` is nonzero modulo p. Use full integer residuals for the proof and cap their valuations at e when interpreting a residue computation. Let `s=min(v_p(x),v_p(y))`, with infinity allowed.

If s=0, tau cannot vanish modulo p. Otherwise `2y=kx mod p`; substituting into the quadratic form in (2) gives

`0=x^2-kxy+y^2=-(Delta/4)x^2 mod p`.

Since Delta and 4 are units, x=0 and then y=0 modulo p, a contradiction. This proves `v_p(tau)=0` without any eigenvalue calculation.

Suppose `1<=s<infinity`. Write `(x,y)=p^s(x',y')`, with at least one primed coordinate a unit modulo p. Dividing (2) by `p^s` yields

`2y'-kx'=-p^s(x'^2-kx'y'+y'^2)`.

Hence `2y'=kx' mod p`. Necessarily x' is a unit: if it were zero modulo p, y' would also be zero, contradicting the choice of s. Therefore

`x'^2-kx'y'+y'^2=-(Delta/4)x'^2 mod p`

is a unit. Equation (2) now gives `v_p(tau)=2s`. If both residuals are zero, tau is zero and the capped statement is immediate. In every case,

`min(v_p(tau),e)=min(2 min(v_p(x),v_p(y),e),e)`.

This is exactly the equality of p-exponents on the two sides of (1). Taking all primes dividing N proves the claim. Different representatives of x,y modulo N leave both gcds unchanged; no unknown prime or division by it is required in an implementation.

## Observer and factor consequences

- For squarefree N, `gcd(tau,N)=g`; trace and the common-return ideal produce the same divisor in this regular case.
- At a prime power, the trace exponent is `min(2s,e)` instead of `min(s,e)`. A proper common-return factor can therefore become a saturated trace result. This is an exact loss of valuation, not a heuristic warning.
- If the trace gcd is proper, the common-return gcd is also proper. The converse can fail because of saturation. This is an information comparison, not a claim that computing both coordinates always costs less.
- The hypotheses matter: oddness and unit discriminant were used in the quadratic-form argument. A degenerate discriminant is a separate setup branch, and no analogous formula is asserted there.

The implementation interface still needs actual typed matrix/vector arithmetic, gcd and division receipts. It may compute g directly from the cyclic mark, without expanding an orbit or knowing local orders. Identity (1) does not extract factors on its own and does not make the useful exponent-selection problem cheap. It is an observer-preservation refinement of the existing conic geometry, with no new execution, admission or general native Shor claim.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.

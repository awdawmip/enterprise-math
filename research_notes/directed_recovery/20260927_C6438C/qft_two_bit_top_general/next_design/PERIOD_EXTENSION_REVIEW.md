# Shared-context symbolic review of period concatenation

Verdict: no substantive mathematical defect found. This review binds the
complete `PERIOD_EXTENSION.md`, SHA-256
`97d2011a41a2f0a8416151955daa4b08f448ab38336b9214e29d8a5208bbd3b6`.
It used symbolic manipulation and source reading only. No numeric example,
scientific import, host scientific evaluation, native execution or new external
query was performed. It is shared-context review, not independent admission.

## Concatenation and the ten-value identity

For d=qP+s, the integrand is P-periodic and the overlap length is
`(H-q-1)P+(P-s)`. A full period contributes `A_P(s)+A_P(P-s)` and the final
prefix contributes `A_P(s)`. Thus (1) is exact. Its wrapped term exchanges
scalar factors; it is correctly not asserted for arbitrary matrix products.
At s=0 the second overlap is the explicit empty `A_P(P)`, at q=H-1 its
coefficient vanishes, and at s=P/2 both contributions retain their weights.

With C=H-q, the low compressed piece is
`C(M-3z)+(C-1)(-z)=CM+(1-4C)z`; the high piece is
`C(z-M)+(C-1)(3z-2M)=M(2-3C)+(4C-3)z`.
Both agree at M/2. The high continuation at z=M is `(C-1)M`, matching the
next period's zero-offset value, or the empty final endpoint. Therefore a
stretch crossing z=M-1 to z=M does not incorrectly reset the available overlap.

Writing the reached affine piece as beta+alpha*z yields
`(beta-alpha*M*q)J0+alpha*J1`, since the global compressed index is Z=Mq+z.
The low J0 coefficient divided by M is
`H+(4H-2)q-4q^2`; the high-minus-low difference is
`2-4H+(8-8H)q+8q^2`. The low J1 coefficient is `1-4H+4q`, and its
high-minus-low difference is `8H-4-8q`. These exactly reproduce (4).
The ten sums and their coefficients in (5)-(6) follow directly. The second
index is the indicator exponent, and no independence or minimal-basis claim
is needed.

## Fine-floor elimination

Let eta=Qplus-Q, so Z=2Q+eta and t=d-pQ-Veta. For J0, direct substitution gives

```text
J0 = V-2d+2pQ + eta*(4d-4pQ-2p).
```

Using `Delta_2=(2Q+1)eta` gives exactly (7). For J1, its part independent of
eta is `4pQ^2+2pQ-4dQ-d`, and its eta coefficient is
`-8pQ^2-8pQ-2p+8dQ+4d`. Multiplying by three and using the adjacent
difference powers gives

```text
3J1 = -3d-12dQ+12pQ^2+6pQ
      +12d Delta_2-8p Delta_3+2p Delta_1,
```

which verifies (8). Division by three is applied only to the combined integer
numerator; isolated thirds need not be integral. X00 and Y00 share the same
two fine-floor tables, with maximum total degree three.

For X, replacing q^a*delta by adjacent coarse differences raises its coarse
degree at most to three; J0 has fine total degree at most two. For Y the bounds
are respectively two and three. Any displacement factor is at most linear,
so the uniform total degree bound five and u<=1 in (9) are valid. The remaining
eight combinations are sufficient, not asserted independent. They still need
joint coarse/fine information. The draft correctly distinguishes this missing
costed interface from a proof of irreducibility or an impossibility result.

## Period-aligned closed case and costs

If P divides R, then within-period s is fixed and q=q0+(R/P)j. Summing the two
linear coefficients of (1) gives exactly (10), using
`sum j=n(n-1)/2`. Its division by two is exact. A head outside L is treated
before the formula, and the s=0 second overlap is omitted as an empty value.
The r=0 and coincident half-modulus orientation rules remain unchanged.

The special case is already within V|R and is an alternative simplification,
not a new arbitrary-input algorithm. Its fixed-size expression requires no
period enumeration or moment tables. This statement counts operations after
the required scales are available: constructing those scales with the current
typed doubling routine, and all input-size-dependent primitive/digit work,
setup and replay, remain paid. It must not be read as constant bit complexity
or as an executed cost reduction.

For unrestricted R, the pointwise period identity alone does not turn wrapped
residues into an accepted unwrapped top-bit progression. The stated possible
P/gcd(P,R) or V/gcd(V,R) splits can be large; the draft does not hide their cost
or claim such splitting is mathematically necessary. A descending mixed
recurrence or a proved cancellation of the particular combination remains the
next mathematical task. None of these formulas supplies an unknown order or
address, a general matrix-word correlation, growing-mask compression or full
Shor sampling. Raw normalization remains 4^-g.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1

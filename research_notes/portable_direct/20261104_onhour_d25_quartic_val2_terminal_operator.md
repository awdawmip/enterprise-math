# D25 — exact terminating operator for the quartic valuation-two port

2026-11-04 (+08). **AUTHOR-DERIVED / EXACT SCOPED PROOF / NOT_ADMITTED / REGISTER_PENDING.** This is the same frozen D25 author-side science, not a native benchmark or formal Source execution. Immediate mathematical predecessor: `20261104_onhour_d25_quartic_val2_universal_port.md`, with original scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`.

## Exact finite operator identity, all N>=1

Use the **same rational coefficients** `d_1=1/72` and

```text
d_(n+1)/d_n = n*(16n^2-1) / [18*(2n+1)^3].
F_N(x) = sum_{n=1}^N d_n*x^n.
theta = x*d/dx.
L = 18*(2*theta-1)^3 - x*theta*(16*theta^2-1).
```

Then, in the rational polynomial ring **exactly** (without a modulus):

```text
L F_N(x) = x/4 - N*(16*N^2-1)*d_N*x^(N+1).             (T)
```

**Proof.** The coefficient of `x^1` is `18*d_1=1/4`. For each `2<=m<=N` it is
`18*(2m-1)^3*d_m - (m-1)*(16*(m-1)^2-1)*d_(m-1)=0`
by the exact recurrence. The only remaining coefficient is at `x^(N+1)`, which is
`-N*(16*N^2-1)*d_N`. This proves (T) coefficientwise.

Now let `p>=5` be prime and `N=floor((p+1)/4)`. Then **exactly one** of `p=4N+1` or `p=4N-1` holds. All denominators of `d_1,...,d_N` are p-units, and `16N^2-1=(4N-1)(4N+1)` is divisible by p. Thus the terminal residual in (T) vanishes, producing an **exact finite-field differential equation**

```text
L F_N(x) = x/4 in F_p[x].                               (T_p)
```

The boundary factor is an algebraic product of two consecutive p-class possibilities; it is not an experimentally fitted endpoint.

The polynomial of degree at most `N` with zero constant term that solves `L F=x/4` in `F_p[x]` is unique: at each degree `1<=m<=N` the diagonal coefficient `18(2m-1)^3` is a unit, so coefficient recursion uniquely determines each coefficient. Existence is furnished by the displayed `F_N`. (The uniqueness statement is only in the indicated finite-dimensional polynomial space.)

## Exact map to the unproved all-prime port cancellation

The original quartic valuation-two weighted port satisfies the *proved* original-to-operator readout:

```text
V_(p,2)/p^2 = 2*(8*theta-3)F_N(1) in F_p.                (R)
```

Therefore the previously observed all-prime congruence `V_(p,2)=0 mod p^3` is equivalent to the **specific arithmetic boundary-value condition**

```text
    (8*theta-3)F_N(1) = 0 in F_p,                        (B_p)
```

on the unique low-degree solution of `(T_p)`. No proof of `(B_p)` is asserted here: a differential equation at an ordinary point `x=1` does not force that boundary value merely by uniqueness. The distinguished singular coefficient of `L` comes from `18*8 -16*x=16*(9-x)` on the `theta^3` term; `x=1` is distinct from that singular point. A valid future certificate must supply the missing arithmetic evaluation rather than infer it from the ODE.

This is a second exact research unit after the universal-port normalization: (T) supplies a single **terminating boundary factor** `(4N-1)(4N+1)` and a finite-dimension unique operator problem. It exposes a narrower potential proof target without changing the parent task's original 216 or the quartic comparator. It is a research coordinate/readout on a classical hypergeometric family, not a new axiom of the project's native six-dimensional ontology.

## Continuation

The tested `(B_p)` presently has 1227/1227 exact prime checks for `5<=p<=10000` in the predecessor's executable checker, and seven independent original-coefficient checks; none is a universal proof. Next discriminate a genuine operator-level certificate for (B_p), ideally a finite-field symmetry, adjoint/evaluation functional or terminating hypergeometric transformation that works for both `p=4N+1` and `p=4N-1`, and separately construct the **full signed 216-to-2304 cross-valuation transport**. Preserve the original D25 mother objective `Delta_p-R_p=0 mod p` for `p=13,19 mod24`; predecessor's W=V mod p^3 is open.

Native same-original-class H0/B0 benchmark at p373 remains Issue #1559, original `[X]U mod139129`, actual semilinear Frobenius, module rank, sign/odd observer, normalization and independent replay pending. No native Researcher/Claim/open/run/Result admission follows from this author-side note. Original request receipt reconciliation and legal Source recovery remain separate from these algebraic claims.

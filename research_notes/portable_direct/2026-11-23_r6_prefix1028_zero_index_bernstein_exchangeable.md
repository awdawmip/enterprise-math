# PREFIX-1028 — Zero-index spectral extension, exact finite Bernstein consistency and positive approximate measure

Date: 2026-11-23 (Asia/Shanghai). Parent: PREFIX-1027. Status: AUTHOR_EXACT_SYMBOLIC_PROOF / FINITE_EXACT_INTEGER_CHECKED / NOT_REVIEWED.

## Immutable scientific inputs, observer, and scope

The frozen scientific input is `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json` (P000 V5). All statements here are about the fixed Stage46 candidate signed BRC kernel `W=J12-6I12`, the X6 native Cell anchor, incoming `-e1`, bidirectionally forbidden Link `{0,e1}`, exactly one negative outgoing step, and the previously derived *coherent* joint Cell–terminal-port–grade square-mass Laurent observer. We do not modify the native BRC update, task pin, P000, or contributor attribution. The six-phase `A6` moments and exact three-shift contrast formula are inherited from PREFIX-1016/1018/1026 and remain observer-level statements.

Write `A(r)=sum_{a_1+...+a_6=r} multinomial(r;a_1,...,a_6)^2` and let `nu` be the fixed polynomial functional from PREFIX-1026:

```
5 nu[f] =
 -4 integral y^2(y-36)^2 f'(y) dmu(y)
 -2 integral y(y-36)(17y-91) f(y) dmu(y)
 +12 integral (6-y)[integral_0^y (11+x)f(x) dx] dmu(y).
```

`mu` is the six-label Laurent spectral pushforward supported in `[0,36]`, with `integral y^r dmu=A(r)`. Existing physical port contrast was `a_m=Q^+_{m+4,1}-Q^+_{m+4,2}` for `m>=1`. Define `a_0` **only as a formal spectral extension**; it is not a newly inferred physical `n=4` port observation.

## Theorem 1 — exact zeroth spectral extension

The same algebraic three-shift identity is nonsingular at `m=0`:

```
a_m= -72(72m^2+163m+80)/(5(m+1)) A(m+1)
     +2(144m^3+1135m^2+2367m+1310)/(5(m+1)(m+2)) A(m+2)
     -2(m+8)(2m+5)/(5(m+2)) A(m+3).
```

The PREFIX-1026 partial fraction identity is a rational polynomial identity for `m>=0`; its derivative term is simply zero at `m=0`. Thus `nu[y^m]=a_m` **for every integer `m>=0`**, with

```
a_0=-1152 A(1)+262 A(2)-8 A(3)
   =-1152*6+262*66-8*996=2412>0.
```

Independent evaluation of the functional using `A(1)=6,A(2)=66,A(3)=996` gives `5nu[1]=12060`. This extends the spectral moment sequence without asserting an additional native event.

Define for `m,k>=0` `E_{m,k}=nu[y^m(36-y)^k]`; in particular `E_{m,0}=a_m` and `E_{m,k+1}=36E_{m,k}-E_{m+1,k}`.

## Theorem 2 — positive finite exchangeable family from a triangular certificate

Fix `N>=0`. **Conditional only on `E_{m,N-m}>0` for all `0<=m<=N`**, define

```
p_{N,m}=binom(N,m)*E_{m,N-m}/(2412*36^N),    0<=m<=N.
```

Then all `p_{N,m}>0`, they sum exactly to one, and whenever positivity holds through level `N`, the family across levels `0,...,N` satisfies the exact sampling-consistency equation

```
p_{n-1,m} = (n-m)/n * p_{n,m} + (m+1)/n * p_{n,m+1}
     (1<=n<=N,0<=m<n).
```

**Proof.** The Bernstein partition identity

```
sum_{m=0}^n binom(n,m)y^m(36-y)^(n-m)=36^n
```

and linearity of `nu` give `sum_m p_{n,m}=nu[1]/2412=1`. The consistency equation follows from `E_{m,k+1}+E_{m+1,k}=36 E_{m,k}` and the two adjacent binomial identities. Consequently, assigning equal probability `p_{n,m}/binom(n,m)` to each binary string with exactly `m` ones defines a genuinely exchangeable probability law on `n` bits, compatible under deletion of a uniformly chosen bit. No infinite positive spectral measure is assumed in this proof.

For each integer `0<=d<=N` the finite family has exact falling-factorial moments:

```
sum_{m=0}^N p_{N,m} (m)_d / (N)_d = a_d/(2412*36^d),
```

where `(r)_d=r(r-1)...(r-d+1)` and `(r)_0=1`. Indeed `binom(N,m)(m)_d=(N)_d binom(N-d,m-d)` and the leftover Bernstein sum is `36^(N-d)`. This exact equality is valid for the whole finite degree window.

## Theorem 3 — a constructive positive approximate spectral measure

Under Theorem 2's positivity hypothesis for fixed `N>=1`, define the **actual finite positive measure**

```
sigma_N = 2412 * sum_{m=0}^N p_{N,m} delta_{36m/N}
```

on `[0,36]`. For every integer `0<=d<=N`, its moments satisfy the certified one-sided bound

```
0 <= integral y^d d(sigma_N)(y) - a_d
   <= 2412 * 36^d * min(1, d(d-1)/(2N)).
```

For `d=0,1` the difference is zero. **Proof.** Condition on a binary string with `m` ones. The probability that `d` draws without replacement are all ones is `(m)_d/(N)_d`; sampling with replacement gives `(m/N)^d`. The latter is no smaller. Couple the two samplers until the first repeated index; their all-one probabilities differ by at most the collision probability `1-(N)_d/N^d <= binom(d,2)/N`. Average over the exact `p_{N,m}` and multiply by `2412*36^d`. The degree-`d` target is exactly `a_d` by Theorem 2. QED.

Thus a **finite, explicit positive spectral approximation with a quantified moment error** exists whenever the finite E triangle is certified positive. This is a positive *approximating* measure, not a proof that `nu` itself is positive.

For `N=1200` and `d=2`, the exact error is `(36*a_1-a_2)/N=536292/1200`, consistent with the general bound.

## Exact BRC-observer computation (new certificate)

The independently executed Python companion applies the already published exact integer `A6` recurrence and rational three-shift identity, now also at `m=0`. It evaluates the full triangle `m>=0,k>=0,m+k<=1200` with **721,801 strictly positive** exact integers (1,201 new zero-index witnesses). The original `m>=1` stream is reproduced byte-for-byte:

- Original PREFIX-1027 `m>=1` SHA-256: `b626fc2e4e12db5ce219ab6f5e69f0c0344f38d6fe63d189a768a935d888439e`.
- New full `m>=0` stream SHA-256: `a7565656208a7ff3f6fd9ff269a63879b8e0d3e76c3537dcaf130e7241e60d06`.
- Stream canonicalization: ASCII `m,k,E\n`, ascending `k`, then ascending `m`.
- Checkpoints for normalization and falling factorial moment identities: `N=0,1,2,10,100,240,1200`, all exact equalities verified for `d<=min(3,N)`.

Therefore Theorems 2–3 apply **unconditionally to the precisely certified finite range `N<=1200`**, with the explicit measure `sigma_1200`. The algebraic identities in Theorems 1–3 hold at their stated general scopes, conditional where stated. No analytic proof of positivity at every finite N or independent mathematical review has been obtained.

Files: `research_notes/portable_direct/PREFIX1028_R6_BERNSTEIN_EXCHANGEABILITY_CHECK.py` and `research_notes/portable_direct/PREFIX1028_R6_ZERO_INDEX_BERNSTEIN_CERT.json`.

## Significance and next precise problem

The earlier `m>=1` Hausdorff question now has a natural `m=0` extension and an **exact, positive, consistent exchangeable family up to 1200 bits**. Finite exchangeability provides a directly constructible approximation to the missing positive measure, with quantified fixed-degree error, without equating finite extendibility with an infinite Hausdorff theorem.

The open mathematical step is to prove `E_{m,k}>=0` for **all** nonnegative pairs. A promising approach is to exploit the exact coherent finite family and obtain uniform extendibility from a recurrence or a nonnegative BRC-observer spectral density; a counterexample would precisely bound the finite family. In the simultaneous limit `m,k -> infinity`, the signed spectral functional may be studied at the interior concentration point `y=36m/(m+k)`, without replacing the native Cell–port–grade carrier.

Original contributor attribution: historical `EM-DIRECT-FBEA5D`, Activity `RA-3FB2D033BE6048D8712FF056`, original SID `MCP-45ad6d29cd534c1aad25595a72e3c532`. These are provenance, not a newly authenticated active CLAIM. Current portable author work is not an accepted Result or Review. Parent objective `B_fix,odd(32) in {19,20}` remains open.

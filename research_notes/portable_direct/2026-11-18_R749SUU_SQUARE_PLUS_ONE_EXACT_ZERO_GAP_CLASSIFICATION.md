# R749SUU — Exact zero-gap dichotomy on the square-plus-one boundary

Date: 2026-11-18 (Asia/Shanghai). Status: AUTHOR_EXACT_NOT_REVIEWED.
Researcher provenance: EM-DIRECT-2CD81E, original SID MCP-c40e95eadedb4b95ad8159a93e814986; independent portable-research extension, no native X6 CLAIM.

## Immutable foundation and scope

Frozen mathematical source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md` (WBRC-T30–T32).
Reuses R749SUT at commit `1c7fbcb3b9c0a07ee914604de6600cae2447f9cc` for the named two-Port integer observer and Q=+1 factor coordinates. This is an **auxiliary positive-integer observation model**, not a native six-axis/triadic X6 event. The P000/worldview pins remain unchanged.

For `M=t^2`, `t>=3`, set `B=M+1=t^2+1`. Work in the legal oriented `Q=+1` sector:
`2<=x<=y`, `n=xy<=B`, `n-x-y>=1`,
`(a,u,v,d)=(n-x-1,n-1,n-x-y,n-y-1)`,
`ad-uv=1`, `u+v-a-d=1`, `tau=(n-1)(n-x-1)(n-y-1)`.
Other named configurations arise by independently swapping the two diagonal or off-diagonal entries.

## Theorem — complete square-plus-one classification

For every integer `t>=3`, the **unique unordered optimal factor pair** in this Q=+1 sector is exactly one of:

1. If `t=r(r+1)+1` for an integer `r>=1` (necessarily odd `t`), then `(x,y)=(t-r,t+r+1)` and `n^*=t^2+1` (zero gap).
2. If `t=2k^2` for an integer `k>=2` (necessarily even `t`), then `(x,y)=(t-2k+1,t+2k+1)` and `n^*=t^2+1` (zero gap).
3. For every other `t>=3`, `(x,y)=(t,t)` and `n^*=t^2` (gap exactly one).

All these pairs reconstruct legal named matrices. In cases 1–2 there are four named maximizers; in case 3 there are two. There are no other Q=+1 ties.

The corresponding optimal value is the exact formula
```
T*(t) = (n*-1) (n*-x-1) (n*-y-1).
```
For case 3 this simplifies to `(t^2-1)(t^2-t-1)^2`.

### Proof: all products n<=t^2

Write `s=x+y` and `T(n,s)=(n-1)[(n-1)^2-(n-1)s+n]`.
For admissible x,y>=2, `n>=s`. At fixed s, T is strictly increasing in n>=s, since
`dT/dn = 3(n-1)^2 - 2s(n-1) + 2n-1 >= n^2-2n+2 >0`.
At fixed n, T is strictly decreasing in s.

Put `S=T(t^2,2t)=(t^2-1)(t^2-t-1)^2`, attained by `x=y=t`.
If a competing pair with `n<=t^2` has `s>=2t`, monotonicity yields
`T(n,s)<=T(t^2,s)<=S`, with equality only if n=t^2 and s=2t; hence x=y=t.

If `s<=2t-1`, the maximum integer product at that sum is at most `t(t-1)`. Hence each of the three positive score factors is <=`t^2-t-1`, and
`T(n,s) <= (t^2-t-1)^3 < (t^2-1)(t^2-t-1)^2=S`.
Thus x=y=t is the unique unordered optimum among all n<=t^2.

### Proof: the single remaining product n=B=t^2+1

For n=B, any positive factor pair has integer sum s>2t. Its score decreases strictly with s:
`T(B,s)=t^2[t^4-t^2 s+t^2+1]`.

When t is odd, B is 2 modulo 4, so x,y have opposite parity and s is odd: s>=2t+1.
Equality `s=2t+1` forces `x=t-r,y=t+r+1` for r>=1. The product equation is equivalent to `t=r(r+1)+1`. Conversely this condition gives a legal factor pair. Its advantage over the square score is
`T(B,2t+1)-S=(t-1)(2t^3-2t^2-3t-1)>0` for t>=3.
If this pair does not exist, all B-factor pairs have s>=2t+3, while
`S-T(B,2t+3)=4t^3+t^2-2t-1>0`.
The square pair then wins.

When t is even, B is odd, so x,y are odd and s is even: s>=2t+2.
Equality `s=2t+2` forces `x=t-r,y=t+r+2` with odd r>=1, and
`r(r+2)=2t-1`, equivalently `(r+1)^2=2t` and `t=2k^2`.
The smallest admissible k is 2 (k=1 has t=2 outside the theorem). In this family t>=8 and
`T(B,2t+2)-S=t^4-4t^3-t^2+2t+1>0`.
If the equality-sum factor pair is absent then s>=2t+4 and
`S-T(B,2t+4)=t^4+4t^3+t^2-2t-1>0`.
This proves all three cases and uniqueness.

## Exact count and asymptotic sparsity on this slice

The two zero-gap subfamilies have opposite parity and do not overlap. For any integer `T>=3`, the number of zero-gap parameters `3<=t<=T` equals
```
N0(T) = floor((sqrt(4T-3)-1)/2) + floor(sqrt(T/2)) - 1
      = (1+1/sqrt(2))*sqrt(T) + O(1).
```
All floors can be computed by integer square roots:
`(isqrt(4*T-3)-1)//2 + isqrt(T//2)-1`.
Consequently the zero-gap density among these square `M=t^2` instances tends to zero, while both exceptional families are infinite. Among `M=t^2<=X`, the zero-gap count is `(1+1/sqrt(2))*X^(1/4)+O(1)`.
This square-slice density result complements (and does not replace) R749SUT's wider Omega(X^(3/4)) sufficient family across unrestricted M.

## Independent exact verification

`R749SUU_SQUARE_PLUS_ONE_CERT.py` uses Python standard-library integers only:
- Exhaustive **all legal unordered (x,y)** for each `3<=t<=70`, checking the score maximum, pair and uniqueness (68 inputs).
- A separate endpoint-factor oracle for every `3<=t<=2200` (2198 inputs), using the independently justified monotonic increase in y for fixed x. Its scan covers every x in `2..isqrt(B)`, so there is no sampled candidate omission within that domain.
- The 78 predicted zero-gap parameters through t=2200 match the oracle exactly, and the counting formula yields 46 odd-parameter plus 32 even-parameter instances.
- Exact polynomial difference identities and example values are asserted. No floating-point operations, approximation tolerance or external numerical library is used.

The companion JSON records sample scores, ranges and independent-check coverage. The infinite classification is supported by the above proof; no independent mathematical review or formal theorem promotion is claimed.

## Scientific continuation

A. Use the explicit square-plus-one dichotomy as a constant-time fast path for the exact Q=+1 optimizer when `M` is a perfect square, with no factorization search; generic M retains the established algorithm.
B. Investigate `B=t^2+c` for fixed c>=2: identify the first lower-product competitor and determine residue/factorization-controlled zero-gap transitions.
C. Review the upstream R749SUO claim that all nonstandard global maxima have Q=+1 for `M>=116`. Conditional on that author-level theorem, the classification here is also the complete **global nonstandard** classification for t>=11. Native X6 triadic/time correspondence remains a separately typed problem.

Actual governance: portable research file, not a new shared claim/Result/Review or promotion.

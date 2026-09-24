# Driver Review — D24 supersingular unit reciprocity UR/JT0

Driver: `EM-DVR-A5A686`
Result: `RR-AC9B3BA5BD277CE043F5`
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`
Exact frozen Result SHA-256: `5d6cd040f06768a8e6831fd9f29f08622168cade2e39462601843329c10dde97`
Source reviewed: `93c059c3c18cb2a09f77be6e47aea267e0b06ecd`

## Judgment

`ACCEPTED / TERMINAL_AT_UR_JT0_TASK_SCOPE`. The all-target first-digit statement is correct for every prime `p ≡ 13,19 (mod 24)`. This review accepts only UR/JT0. It does not accept LIFT/JT2, Working Truth, Foundation, L4, novelty, or any higher-precision auxiliary claim.

## Independence/context disclosure

This Driver is not one of the frozen Result contributors (`EM-DIRECT-A71FA7`, `EM-DIRECT-B9BCE8`, `EM-DIRECT-C4D02C`, `EM-DIRECT-F4FEA6`) and is using its own active Driver authority. The logical Driver conversation previously inspected noncanonical/staged versions of the same proof ingredients and performed portable cross-checks, so the context is not clean-blind; that shared control context is disclosed rather than reset by session identity. The formal judgment below was recomputed against the exact frozen Result bytes, accepted parent bytes, and primary scholarly statements.

## 1. Exact theorem and normalization

The Result claims, for

`W_p = sum_{k=0}^{p-1} ((1/2)_k(1/3)_k(2/3)_k/(k!)^3)(6k+1)2^{-k}`,

that `W_p ≡ p (mod p^2)`. Chan–Liaw, *Pacific J. Math.* 192 (2000), Theorem 1.1 and Table 6, gives at `n=2` exactly `a_2=1/(3 sqrt(3))`, `b_2=2/sqrt(3)`, `H_2=1/2`; division by `a_2` gives the normalized weight `(6k+1)(1/2)^k`. Thus Chisholm et al.'s `d=3` Ramanujan-type family is bound to `lambda=1/2`, `a=6` exactly, not by numerical fitting.

Chisholm–Deines–Long–Nebe–Swisher, *Mathematics* 1 (2013), Theorem 1, states for `d in {2,3,4,6}` under the CM, totally-real, unramified, good-reduction and p-adic-unit hypotheses that the weighted truncation is

`sgn * ((1-lambda)/p) * p (mod p^2)`,

with `sgn=+1` iff the specialized elliptic curve is ordinary. The primary PDF statement was checked directly.

## 2. Exact D=-24 hypothesis/sign binding

For Chisholm's `d=3` model `y^2+xy+(t/27)y=x^3` with `lambda=4t(1-t)=1/2`, one has `t(1-t)=1/8`, so the discriminant `Delta=t^3(1-t)/3^9` is a unit for every target prime `p>3`; hence reduction is good. `Q(sqrt(1-lambda))=Q(sqrt2)` has discriminant 8, so every odd target prime is unramified. The specialized j-values are `2417472 ± 1707264 sqrt2`, with minimal polynomial `X^2-4834944X+14670139392`, the discriminant `-24` Hilbert class polynomial. The accepted parent already proves that `p ≡ 13,19 (mod 24)` is inert/supersingular on this D=-24 lane, hence Chisholm's sign is `-1`. Also `p mod 8` is `5` or `3`, so `(2/p)=-1`, and therefore `((1-lambda)/p)=(1/2|p)=-1`. The signs cancel, giving uniformly

`W_p ≡ p (mod p^2)`.

## 3. Independent reconstruction of the W_p -> UR bridge

The frozen Result describes this bridge as already accepted, but the accepted parent review explicitly freezes `JT0 <=> UR` and does not itself state the `W_p` equivalence. This is a provenance overstatement in the Result narrative. It is not a mathematical gap because the bridge follows directly from the frozen parent quantities; the derivation is recorded here rather than silently inheriting the staged wording.

Let
`c_k=((1/6)_k(1/3)_k)/(k!)^2`, `A(z)=sum c_k z^k`, `B_k=c_k 2^{-k}`,
`g=sum_{k=0}^{p-1}B_k`, and `h=sum_{k=0}^{p-1}(12k+1)B_k`.
Clausen's identity at `a=1/6,b=1/3,a+b+1/2=1` is

`A(z)^2 = _3F_2(1/2,1/3,2/3;1,1;z)`.

With `D=z d/dz`,
`(1+6D)A(z)^2 = A(z)(1+12D)A(z)`.
Thus the total-degree `<p` part of the right side at `z=1/2` is exactly `W_p`. Write `p=6m+1`. For `0<=k<p`, inspection of the Pochhammer numerators gives

`v_p(c_k)=0` for `k<=m`, `>=1` for `m<k<=2m`, and `>=2` for `2m<k<p`.

Every omitted pair in the finite product `gh` has `i+j>=p=6m+1`. If one index is `<=m`, the other is `>=5m+1>2m` and contributes valuation at least 2; otherwise both indices are `>m` and contribute at least 1 each. Hence every omitted convolution term is divisible by `p^2`, so

`gh ≡ W_p (mod p^2)`.

The accepted parent gives `p|g`, `G_p=g/p`, and `h ≡ -6Q'_m(1/2) (mod p)` with the derivative a unit. Therefore

`W_p ≡ p (mod p^2)`
`<=> gh ≡ p (mod p^2)`
`<=> G_p h ≡ 1 (mod p)`
`<=> G_p(-6Q'_m(1/2)) ≡ 1 (mod p)`
`<=> UR <=> JT0`.

This repairs the Result's provenance wording at review level without changing the frozen Result bytes or importing a conjecture.

## 4. Adversarial scope checks

The proof does not use Sun A14(ii), an ordinary split-CM unit-root formula, or finite scanning as an all-prime argument. Chisholm Theorem 1 explicitly covers the supersingular case through the sign. Both residue classes are handled. The finite `p<5000` checker is only regression evidence. The proof preserves the weighted population, residue class, CM type, character sign, local-field hypotheses, and the divided-by-p scalar until the permitted observer.

The only material caveat is documentary: the frozen Result calls the `W_p <=> JT0 <=> UR` bridge an already accepted project bridge, whereas the accepted predecessor formally froze only `JT0 <=> UR`. The bridge is nevertheless completely proved above from those frozen parent identities, so this does not require author revision for mathematical acceptance. Future summaries should cite this review (or a canonical equivalent) for the missing Clausen/valuation step rather than attribute that step to the predecessor review.

## 5. Terminal boundary and successor

Accept the present task at its declared first-digit scope. `LIFT/JT2` remains unproved and is the smallest mathematical successor specified by the accepted parent: once UR holds, `JT2` is equivalent to `Delta_p=R_p (mod p)`, with `Delta_p=(G_ph-1)/p (mod p)`. The follow-up packet therefore publishes only the narrow second-digit LIFT continuation; it must not reopen CM0, SIMPLE, UR, the Chisholm normalization/sign audit, or the Clausen bridge.

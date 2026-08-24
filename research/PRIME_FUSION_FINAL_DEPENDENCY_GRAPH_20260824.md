# Prime Fusion — Final Non-Linear Dependency Graph

Status: `FROZEN / REVIEW_READY / NON_LINEAR_DEPENDENCY_GRAPH`  
Date: `2026-08-24`  
Task: `GS-PRIME-FUSION-FINAL-SOURCE-REPAIR-AND-PACKAGE-FREEZE`  
Theorem rows: exactly `T1`–`T15`.

## 1. Reading rule

This graph records **logical proof dependencies / supplied-input dependencies** for the retained theorem statements. It does not treat chronological discovery order or evidence-review order as logical implication.

`FALSE_CHAIN_REJECTED = T3 -> T6 -> T10 -> T11`

In particular:

- T6 does not logically require T3;
- T10 does not logically require T3;
- T11 does not require T10 orbit completeness.

## 2. Core arithmetic / coordinate substrate

- `primitive cell (a,b)` -> T1 (diagonal square identities);
- `primitive cell (a,b)` -> T2 (exact common-divisor law);
- `dual-prime local congruence hypotheses` -> T9;
- `primitive local prime divisibility` -> T12;
- `fixed corridor parameterization` -> T13;
- `sector-local carrier adjacency + T9 parity / mod-3 obstruction` -> T14;
- `unimodular corridor map modulo M` -> T15.

These branches are not forced into a single theorem chain.

## 3. Fusion / quotient branch

`T3 product decomposition`
  
`T3 -> T4`

T4 additionally uses primitivity / the channel norms and CRT to obtain the pointed cyclic quotient. From the pointed residue:

`T4 -> T5`

T8 uses the quotient/channel structure together with the elementary primality / square-free-semiprime equivalence:

`T4 + channel primality/semiprime equivalence -> T8`

T8's abstract ring shape `F_p x F_q` is separated from the canonical Gaussian/Eisenstein channel labels, which come from the fixed product projections / central idempotents.

## 4. Reciprocal-trace / reconstruction branch

T6 is driven by the reciprocal polynomial identity and the modular root/local equations:

`reciprocal identity + F(r)=0 -> T6`

There is **no** logical edge `T3 -> T6`.

T7 accepts an idempotent/channel split as input and combines it with the square reconstruction identities:

`idempotent e + channel split + T1 square reconstruction -> T7`

In the pointed-cell pipeline, T6 is one way to produce the `e` consumed by T7, but the theorem statement of T7 is not made logically dependent on T3.

## 5. Oriented phase branch

Under the retained dual-prime local hypotheses, T10 follows from local orders and CRT:

`ord_p(r)=4 + ord_q(r)=3 + CRT -> T10`

The source context may be reached through the T9 dual-prime congruence branch, but T10 does **not** require T3.

The T10 universe is explicitly the channel-oriented mixed locus

`M_{p,q}={x mod pq : x^2+1=0 mod p and x^2+x+1=0 mod q}`,

not the complete root set of `F mod pq`.

T11 follows directly from the same two oriented local equations:

`x^2=-1 mod p + x^2+x+1=0 mod q -> T11`

There is **no** logical edge `T10 orbit completeness -> T11`.

## 6. Accepted cross-link between T6 and T11

On the oriented locus, the independently accepted relation is

`x^6 = 2e-1 (mod H)`.

Thus T6's idempotent readout and T11's sixth-power readout are connected descriptions of the same channel split. For odd `H`, the two readouts are equivalent because `2` is invertible.

This is a cross-link, not a replacement for either theorem row.

## 7. Compact adjacency ledger

| Target | Required logical inputs | Explicit non-dependencies / scope |
|---|---|---|
| T1 | coordinate definitions | independent branch |
| T2 | channel definitions | independent branch |
| T3 | `f,g,F` and integral comaximality | independent fusion-algebra branch |
| T4 | T3 product decomposition + primitivity/channel norms + CRT | pointed product-quotient presentation |
| T5 | T4 pointed residue + local coprimality | sign convention fixed by package |
| T6 | reciprocal identity + modular root/local equations | **not T3** |
| T7 | idempotent/channel split + T1 square reconstruction | `NC=H`, `gcd(N,C)=1` automatic for idempotent input |
| T8 | quotient/channel structure + primality/semiprime equivalence | abstract product shape != canonical channel labels |
| T9 | dual-prime congruence/reciprocity data | independent arithmetic branch |
| T10 | local orders + CRT + oriented locus definition | **not T3; not all roots of F** |
| T11 | two oriented local equations | **not T10 orbit completeness** |
| T12 | local prime-direction equations | independent local branch |
| T13 | corridor polynomials + local root counts | independent corridor branch |
| T14 | sector-local adjacency + parity/mod-3 obstruction | no cross-seam claim |
| T15 | unimodular finite map modulo M | no asymptotic-prime claim |

## 8. Freeze facts

`DEPENDENCY_GRAPH_KIND = NON_LINEAR`  
`FALSE_CHAIN_REJECTED = T3 -> T6 -> T10 -> T11`  
`T10_UNIVERSE = M_{p,q}`  
`T10_FULL_FUSED_ROOT_SET_CLAIM = false`

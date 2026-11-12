# R99 — Exact gcd-period quotient of circular-source winners

Date: 2026-11-12. State: author-side mathematical proof and exact computational audit; independent review pending.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: R98 `2249b2a88cc7f111cdfc64647e979d75f416487a` (R97, R90 and R86 reused).
Scope: **auxiliary finite rational circular-source model**; P000 and its native six-axis semantics remain unchanged.

## Mathematical setting
Let E be a finite set of complete integer identities (t,branch), with integer t and ordered branch. For signature (j,x,a,b), j,a,b integers and x rational, define, for every **real** parameter theta,
`s_t(theta)={x+(t-j)theta}`, `A(theta)={a theta}`, `B(theta)={b theta}`, where braces denote fractional part. A time t qualifies when s_t belongs to the directed half-open circle arc [A,B), empty when A=B. W_E(theta) is the lexicographically latest eligible complete identity or NONE. The exact answer on a closed rational interval I=[L,U] is STABLE_NONE, STABLE(full identity), or CHANGES with two *rational* witnesses having different directly evaluated full winners.

## Theorem R99.1: exact common period
Define `g=gcd(|a|,|b|,{|t-j|:(t,branch) in E})` with all-zero gcd equal to zero. If g>0, P=1/g is a certified period:
`for every real theta and every integer k: W_E(theta+k P)=W_E(theta)`.
If g=0, W_E is constant in theta.

**Proof.** Every shift by kP changes each of the three lifted affine circle expressions by an integer: ak/g, bk/g and (t-j)k/g. Hence their fractional parts are identical pointwise, including all equality and discontinuity parameters. The eligible source times are unchanged. Since the original full branch-identity set and its lexicographic order are retained, the latest full identity is unchanged. When g=0, all these affine slopes vanish, so each membership predicate is constant. QED.

This is an exact *safe* period, not a minimal-period assertion. Multiple branches with the same time are still kept as distinct identities. For empty E the winner is NONE.

## Theorem R99.2: exact interval quotient and rational witness lift
Let g>0 and P=1/g.

**If U-L>=P**, solve the entire original real-interval winner trichotomy on the one-period closed domain `Q=[0,P]`. For any rational witness z in Q, lift it by
`T(z)=z+P*ceil((L-z)/P)`.
Then `L<=T(z)<L+P<=U` and `W_E(T(z))=W_E(z)`.

**If U-L<P**, take `k=floor(L/P)`, `Q=[L-kP,U-kP]` and `T(z)=z+kP`. Q has width less than P and lies in [0,2P); T is a bijection from Q to I preserving the winner at every point.

**If g=0**, answer by directly evaluating W_E(L) once; the result is stable.

**Proof.** When I contains a full period, the subsets of winner values attained on I and [0,P] are identical: the periodic function factors through the quotient of the real line by PZ. More concretely, [L,L+P] lies in I and meets every translation orbit, and so does [0,P]. The ceiling map takes each rational quotient witness into [L,L+P) while preserving its entire orbit. Thus the trichotomy and two-witness existence are equivalent. When I is shorter, translation by the same integer multiple kP is a bijection, so every winner is preserved pointwise. Closed and singleton intervals, strict circle-arc endpoints, and isolated point-only winner changes are covered. QED.

## Theorem R99.3: width-independent event envelope
For each distinct source time t write the six R97 crossing slopes `c_t=(a,b,a-b,t-j,t-j-a,t-j-b)`. If g>0 define
`K_star=2+sum_{distinct t} sum_{c in c_t}(|c|/g+1)`.
Every c is divisible by g and both R99 reduced domains have width at most P=1/g. A nonzero affine expression with integer slope c varies by at most |c|/g across Q. It can cross at most |c|/g+1 integer levels, including closed endpoints. A zero-slope expression contributes no isolated crossing. Summing proves that the exact R97 critical-point envelope on Q is <=K_star, independently of the length and magnitude of I.

The R98 node/merge budgets therefore apply on the quotient:
`C_Q<=3M(M+1)`, `A_Q<=3M(M+1)(2K_star-1)`, where M=|E| counts **complete source identities**. The g=0 case needs no profile for a classification query.

The claim concerns the exact cut-enumerating R86/R90 algorithms and their R97/R98 structural counters. Input parsing, gcd, rational endpoint reduction, lifts, and binary integer operations remain chargeable in a full CPU cost model.

## An unbounded family
Take E={(2,0),(2,3)}, signature (j,x,a,b)=(0,1/7,1,2), I_N=[-N,N], N any positive integer. Then g=1 and the original R97 six-expression envelope is *exactly*
`K_old(N)=14N+5`;
the same expression on R99's one-period domain [0,1] is *exactly*
`K_quotient=12`.
Thus the original cut enumeration can grow linearly in N (exponentially in the input's binary length), while the quotient requires a fixed critical partition and exact rational witnesses lifted into I_N. The two branches sharing time t=2 remain distinct.

## Verification
The companion complete Python source is stored losslessly in `check_r99.py.gz.b64`: decode with `base64 -d check_r99.py.gz.b64 | gzip -dc > check_r99.py`. Use the unchanged `check_r90.py` and `check_r97.py` from the R98 reproducibility bundle next to the file and run `python check_r99.py`.

The executed standard-library Fraction checker compared 230 bounded queries against the **original unreduced exact R90 critical-partition reference**, covering negative signs, empty/half-open arcs, singleton intervals, enormous absolute offsets, and full branch identities. It separately checked 100 astronomically wide intervals by an exact quotient-domain reference plus the theorem's period identity, not by pretending to enumerate all real inputs. There were 4,314 exact period-equality checks, six unbounded-family tests, four strict subunit-period/gcd tests and 230 bound checks. Each CHANGES witness was checked by direct exact full-identity evaluation. Banner:
`R99_PASS 230 100 4314 6 4`.

The recorded family checks include N=10^2,10^4,10^8,10^12,10^20,10^50. Their exact old/quotient envelope values are in `verification_r99.json.gz.b64`.

Five-repeat single-process diagnostic medians for the family, comparing full original R90 reference-partition enumeration with R99's early-terminating quotient trichotomy:

| N | Original reference | R99 quotient |
| ---: | ---: | ---: |
| 1 | 374 microseconds | 205 microseconds |
| 10 | 3701 microseconds | 175 microseconds |
| 100 | 42051 microseconds | 238 microseconds |
| 500 | 175352 microseconds | 217 microseconds |

These times depend on the implementation and different stopping behavior; the all-real correctness and event-envelope theorem follow from the proof, not the timing.

## Next frontier R100
Connect gcd-period canonicalization to R93's indexed OUT rectangles, R94's versioned source identities and R95–R97's cost selector. The cache key must include exact source identity version, observer signature, period and quotient interval; a source edit can change g. Compare full update/query/witness/bit/memory costs and investigate minimal certified periods where they are useful. Preserve non-periodic future-observer state; the auxiliary parameter quotient is not a native X6 quotient. Independently review the R98 make-node charging bound before using it for a more detailed bit-operation certificate.

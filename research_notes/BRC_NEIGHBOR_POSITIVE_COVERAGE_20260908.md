# A positive neighbor-square family and incremental small-cohort coverage

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Status: elementary constructive proof, exact fixed-fixture checks and host timing; noncanonical research checkpoint.  
Global snapshot: `618b0d18a0da1cb144e15a90a1e3fc819cae7c54`.  
Parent project frontier: `a85bf8e00893ea0967601d9364d339769a716388`.

## Question and reuse

The user asks to preserve occasional inexpensive successes rather than require universal coverage. This checkpoint asks whether a second existing BRC channel contributes positive examples beyond immediate completion, while keeping preparation and unsuccessful-observation costs explicit.

The executed dependency is `neighbor_square_parameters` in [the existing neighbor-square module](https://github.com/awdawmip/enterprise-math/blob/a85bf8e00893ea0967601d9364d339769a716388/src/enterprise_math/brc_neighbor_square_lift_shortcut.py), Git blob `c11075a11848e8fe5d5399fcab259dc7ab66b0cb`. Local source text matched the pinned blob after newline normalization; executed byte SHA-256 is `fdf1e5c4ee4a032fb732d9653f0a7fd9cf738bd62b1a7af50eb53588e7864490`.

Reuse resolution: `REUSE_EXECUTED` for the parameter identity and existing completion-witness checker, `COMPOSE_APPLIED` for separate population/cost records through the existing regime ledger. No new production solver or dispatcher is introduced.

## Constructive positive family

The existing identity is

\[
N=a^2t+\varepsilon,\quad m=2a-\varepsilon,\quad
mN=a^2(mt+1)-(a-\varepsilon)^2,
\qquad\varepsilon\in\{-1,1\}.
\]

Let `a` be a power of two at least two and choose any integer `k >= 1`. Set

\[
t=mk^2+2k,\qquad c=mk+1.
\]

Then `mt+1=c²`, and the source integer has the explicit factorization

\[
\boxed{N=(ak+1)(amk+\varepsilon).}
\]

Indeed, `m+epsilon=2a`, so expansion gives `a²mk²+2a²k+epsilon=a²t+epsilon`. Both factors are nontrivial and odd. With `x=ac` and `d=a-epsilon`, the two lifted factors are exactly

\[
x-d=amk+\varepsilon,\qquad x+d=m(ak+1).
\]

This is an infinite family of positive integer constructions for the existing channel. It does not assert infinitely many prime pairs. The index `k` constructs fixtures; it is not searched while evaluating an unknown input.

The fixed checks use `a in {2,4,8}`, both signs and `1 <= k <= 16`. All 96 constructions satisfy the exact existing witness API, and all products are below `2^19` (maximum 280,575). Seed primality checks select 28 known semiprimes. Of those, 26 are additional to the earlier immediate-completion hit set:

| Prescribed a | Positive constructions | Known prime pairs | Additional prime pairs |
|---|---:|---:|---:|
| 2 | 32 | 14 | 12 |
| 4 | 32 | 9 | 9 |
| 8 | 32 | 5 | 5 |

The positive constructions establish availability of successes. Their intentionally selected success rate is not a population-frequency estimate.

## A fixed sparse observation and its declared budget

For the separate frequency/cost experiment, freeze only `a=8`. Its prerequisite is that `N-1` or `N+1` is divisible by 64. For odd inputs, the two qualifying residue classes occupy exactly `2/32=1/16` of a complete residue period.

The gate needs the low six bits of `N`, not `J=floor(sqrt(N))`. At most one sign qualifies. A qualifying fixed fixture receives one square test through the existing identity, followed by gcd and exact product verification; an unsuccessful observation terminates at that budget. The three `a` values used to verify the constructive theorem are not scanned as an input-evaluation sequence.

Direction labels `D` and `U` are retained for retrospective comparisons, with the same edit-cost definitions as the parent note. They do not supply hidden data to this gate. The original downward-collapse operation is unchanged.

## Incremental coverage on the unchanged known-prime-product cohort

Reuse all 406 distinct prime pairs from `[101,251]`, with factors known at fixture construction. Only `N` is provided to the fixed observation; factor labels verify its result.

| Initial direction | Inputs | Gate entries | Earlier direct hits | Additional neighbor hits | Offline union |
|---|---:|---:|---:|---:|---:|
| D | 163 | 6 | 48 | 1 | 49 |
| U | 243 | 20 | 108 | 1 | 109 |
| Total | 406 | 26 | 156 | 2 | 158 |

The two additional certificates are `17473=101*173` in D and `31553=139*227` in U. Their verified sums are 274 and 366. Thus this channel contributes positive cases in both initial populations. The union is an offline comparison of hit sets, not a newly deployed routing or target-attack workflow.

## Positive classes with moderately balanced factors

For the fixed `a=8`, `epsilon=+1` branch, a certified square satisfies `c²=15t+1`. Its residue modulo 15 is one of `1,4,11,14`. Writing `c=15k+r` exposes four positive classes:

| r | Explicit source-integer factorization |
|---|---|
| 1 | `(8k+1)(120k+1)` |
| 4 | `(24k+5)(40k+13)` |
| 11 | `(24k+19)(40k+27)` |
| 14 | `(8k+7)(120k+119)` |

Every row follows by expansion of `N=64(c²-1)/15+1`. For `k>=1`, the middle two classes satisfy `1<v/u<2`. In the r=4 class, `v-u=16k+8>0` and `2u-v=8k-3>0`; in the r=11 class, the latter difference is `8k+11>0`. Both ratios tend to `5/3`.

The two added cohort hits are exactly r=4, k=4 and r=11, k=5. Thus the observed extra coverage is supported by explicit moderately balanced positive families, not only by the more imbalanced first parametrization. The fixed audit checks all four classes for `1<=k<=16`, including 32 balanced constructions. These overlap some earlier fixtures and are not added to the 406-input denominator.

The residue `c mod 15` is a classification of a certified success. It is not assumed available as a free predictor before the square test. This is an explicit specialization of the existing multiplier split, with no new method-novelty claim.

## Cost with unsuccessful observations included

A separate background contains every odd integer from 4097 through 8191: 2,048 inputs spanning complete low-bit periods. Exactly 128 pass the gate; four produce verified proper decompositions. These inputs and the prime-pair cohort are reported separately.

Seven timing rounds were run on CPython 3.14.6 / Windows, processing at least 16,384 observations per method/round. Import and fixture construction are excluded. The complete observation includes the low-bit gate, parameter API validation, square test, gcd and exact product verification.

| Fixed population | Gate-only ns/input | Complete observation ns/input | Verified hits |
|---|---:|---:|---:|
| Complete odd background | 70.721 | 194.574 | 4/2048 |
| Unchanged known prime pairs | 71.585 | 220.347 | 2/406 |
| Constructed positive a=8 family | 69.385 | 1,677.991 | 32/32 |

These figures measure an added observation cost, not a speedup of the full portfolio. If a future application saves an equal downstream cost `L` on each successful observation, the conditional break-even equation is `h*L > c`. Using only these finite populations gives about 99.62 microseconds per hit for the background and 44.73 microseconds per hit for the known-prime-pair cohort. Actual downstream savings were not measured, so net benefit remains unmeasured.

The existing ledger is used only to accumulate counts and probe costs. Its required numeric `saved_cost=0` is a placeholder for an unmeasured quantity, not evidence of zero savings. The certificate explicitly marks these records ineligible for adaptive reordering. They must not be read as a negative route verdict.

## Reproduction and retained frontier

```powershell
python experiments/brc_neighbor_positive_coverage_20260908.py --enterprise-root . --output-dir experiments
```

The companion JSON stores exact counts, example certificates, the complete background hit list, all timing rounds, source hashes and population/observer/cost contracts. Mathematical counts and witness checks passed; timing is host-specific evidence.

Retain the positive family and the fixed sparse branch as an exploratory specialist with a declared cost. The full thread objective remains open: this controlled research checkpoint does not establish performance on public RSA tasks and does not implement autonomous target exploitation. No broader scan, fallback search, production dispatch or canonical theorem promotion was added.


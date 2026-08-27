# Prime Coordinate N-only Valuation-Wall GCD Extractor Independent Replay — Research Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Date: `2026-08-27`

Task-ID: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Publication-ID: `TP2-DF186CDB4959BEA10875`

Researcher-ID: `EM-PCF4R-D74517`

Claim-ID: `chatgpt-pcf4r-20260827-1927`

Execution record: `ER-6D2FA59F8E8D388A5F8D`

## 1. Frozen verdict

\[
\boxed{\texttt{N_ONLY_GCD_EXTRACTOR_VERIFIED}}
\]

The hard target

`N_ONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENTLY_RECONSTRUCTED_AND_VERIFIED_OR_NARROWED_OR_REFUTED`

is achieved positively.

For every

\[
N=pq,\qquad 3<p<q
\]

with distinct odd primes, there is a deterministic constructor using only `N`, public integer constants, public dyadic indices, integer square root, modular arithmetic and gcd which returns a nontrivial factor of `N`.

No hidden factor enters the constructor. Hidden `p,q` are used only in proof-side reasoning and regression oracles.

This is an exact extraction theorem, not a factoring-speedup theorem. Its current worst-case running scale remains `Theta(p)` modular recurrence steps, hence exponential in the input bit length on balanced semiprimes.

## 2. Blind-forward provenance

Phase A was frozen before opening the originating non-authoritative duplicate execution.

Frozen Phase-A artifact:

`research_artifacts/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY/PHASE_A_FREEZE.md`

Independent checker:

`scripts/check_prime_coord_factor_nonly_valuation_wall_replay.py`

Checker SHA-256:

`ad0659389524d0c9c4f4c5c8c6317d881e182f5abf5cdb5d8fbf11526394431a`

Only after that proof/checker freeze was Phase B opened against Draft PR #715 / result candidate `RR-D693BD1103CCAE5F354E`.

Thus the positive result is an independent reconstruction, not a retroactive adoption of the duplicate execution.

## 3. Kernel and exact local valuation wall

Define

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
=\binom{2s}{s}^2\binom{3s}{s}.
\]

Let `r>3` be prime and `0<=s<r`. Since

\[
s<r,\qquad 2s<2r<r^2,\qquad 3s<3r<r^2,
\]

Legendre's factorial valuation gives

\[
v_r(s!)=0,
\]

\[
v_r((2s)!)=\left\lfloor\frac{2s}{r}\right\rfloor,
\qquad
v_r((3s)!)=\left\lfloor\frac{3s}{r}\right\rfloor.
\]

Therefore

\[
\boxed{
v_r(A_s)
=
\left\lfloor\frac{2s}{r}\right\rfloor
+
\left\lfloor\frac{3s}{r}\right\rfloor
}
\qquad(0\le s<r).
\]

Because `r>3` is not divisible by `3`, this is equivalently

\[
\boxed{r\mid A_s\iff 3s>r}
\qquad(0\le s<r).
\]

The first local divisibility wall is therefore exactly

\[
h_r=\left\lceil\frac r3\right\rceil.
\]

## 4. Exact first-dyadic alternative

Probe only the public seeds

\[
s=1,2,4,8,\ldots
\]

and stop at the first one satisfying

\[
g_s=\gcd(A_s,N)>1.
\]

### 4.1 The first stop occurs below `p`

Let

\[
h=\left\lceil\frac p3\right\rceil
\]

and let `d` be the least power of two with `d>=h`. Then `d<2h`.

Every prime `p>3` is `6k-1` or `6k+1`.

If `p=6k-1`, then `h=2k`, so

\[
2h=4k<6k-1=p.
\]

If `p=6k+1`, then `h=2k+1`, so

\[
2h=4k+2<6k+1=p.
\]

Thus

\[
d<p.
\]

Since `p|A_d`, the first nonunit dyadic seed `s` exists and satisfies

\[
\boxed{s<p<q}.
\]

Consequently the local valuation wall is valid simultaneously for both hidden factors at the stopping seed.

### 4.2 The first nonunit gcd is exactly `p` or `N`

At `s<p<q`,

\[
r\mid A_s\iff r<3s
\]

for both `r=p,q`.

Since `p<q`, divisibility by `q` implies divisibility by `p`. Hence

\[
\boxed{\gcd(A_s,N)\in\{p,N\}}.
\]

If the gcd is `p`, extraction is complete.

If the gcd is `N`, write

\[
u=s/2.
\]

The previous dyadic seed was a unit, hence

\[
3u<p.
\]

The current seed is divisible by `q`, hence

\[
q<3s=6u.
\]

Therefore

\[
\boxed{3u<p<q<6u}
\]

and in particular

\[
\boxed{q<2p}.
\]

So `gcd=N` is an exact synchronization certificate rather than a failure state.

## 5. Exact synchronized two-seed fallback

Assume the synchronized branch, so

\[
q<2p.
\]

Set

\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor.
\]

Since `N=pq` is nonsquare,

\[
3t<\sqrt N<3t+3,
\]

while

\[
p<\sqrt N<q.
\]

The synchronization bound gives

\[
\sqrt N=\sqrt{pq}<\sqrt2\,p<\frac32p.
\]

Thus

\[
t<\frac p2
\]

and hence, for odd `p>=5`,

\[
\boxed{t+1<p}.
\]

So the local valuation wall applies at both fallback seeds for both hidden factors.

Since

\[
3t<\sqrt N<q,
\]

the larger factor does not divide `A_t`. Therefore

\[
\gcd(A_t,N)\in\{1,p\}.
\]

If it is `p`, stop.

Otherwise `3t<p`. Suppose also that `q<=3t+3`. Then the two distinct odd primes `p<q` would both have to lie among

\[
3t+1,\quad 3t+2,\quad 3t+3.
\]

The last is divisible by `3`, and the first two are consecutive so one is even. Two odd primes greater than `3` cannot occupy the remaining two slots. Contradiction.

Hence

\[
3(t+1)<q,
\]

while `p<3(t+1)`, and therefore

\[
\boxed{\gcd(A_{t+1},N)=p}.
\]

The fallback is exact:

\[
\boxed{
\gcd(A_t,N)=p
\quad\text{or}\quad
\left(
\gcd(A_t,N)=1
\ \text{and}\
\gcd(A_{t+1},N)=p
\right).
}
\]

## 6. Public N-only constructor

The following stopping rule uses only public data.

1. Input `N`.
2. Stream `A_s mod N` from `s=1` upward.
3. At public dyadic indices `1,2,4,...`, compute `gcd(A_s,N)`.
4. At the first nonunit response:
   - if `1<g<N`, return `g`;
   - if `g=N`, set `t=isqrt(N)//3`, test the already streamed residues at `t` and `t+1`, and return the first nontrivial gcd.
5. Before any modular inversion, compute `gcd(s,N)`; if this itself is nontrivial, return it.

No prime list, primality scan, trial divisor, factor-labelled coordinate, CRT idempotent or hidden-factor-dependent seed is used.

## 7. Exact streaming modular recurrence

The integer kernel satisfies

\[
A_0=1
\]

and

\[
\boxed{
A_s
=
A_{s-1}
\frac{6(2s-1)(3s-2)(3s-1)}{s^3}
}.
\]

At every index used before theorem termination,

\[
s\le s_*<p,
\]

and in the synchronized fallback

\[
t+1<p.
\]

Thus every denominator `s^3` actually inverted by the constructor is a unit modulo

\[
N=pq.
\]

Inductively, if `a_{s-1}=A_{s-1} mod N`, then

\[
\boxed{
a_s
=
a_{s-1}\,
6(2s-1)(3s-2)(3s-1)\,
(s^3)^{-1}
\pmod N
}
\]

is a valid exact modular recurrence.

This closes the modular-division concern without constructing the exponentially large exact integer `A_s`.

The implementation also checks `gcd(s,N)` before inversion, so a nonunit denominator cannot silently enter the candidate path.

## 8. Bit complexity and memory

Let

\[
n=\lceil\log_2 N\rceil.
\]

The first dyadic stop satisfies more sharply

\[
s_*<\frac{2p}{3}<\sqrt N.
\]

The streaming constructor performs `O(p)` modular recurrence updates and only `O(log p)` dyadic gcd probes.

With classical `n`-bit arithmetic, each modular inverse/gcd is `O(n^2)` bit operations, giving the conservative bound

\[
\boxed{O(p\,n^2)}
\]

for the streaming recurrence.

With fast multiplication `M(n)` and fast extended gcd, this may be written

\[
\boxed{O(p\,M(n)\log n)}.
\]

The live modular state is only a constant number of `n`-bit residues, counters and gcd temporaries. Therefore

\[
\boxed{\text{working memory}=O(n)}.
\]

This is a strict implementation improvement over exact-integer recurrence, whose live `A_s` has `Theta(s)` bits.

Nevertheless, for balanced semiprimes

\[
p=\Theta(\sqrt N)=2^{\Theta(n)},
\]

so this remains exponential in input bit length.

Freeze:

`N_ONLY_GCD_EXTRACTOR_VERIFIED != FACTORIZATION_SPEEDUP_PROVED`.

## 9. Independent checker evidence

Frozen checker run:

`PASS valuation_checks=76122 recurrence_checks=357 exhaustive_semiprimes=4278 synchronized_cases=928 adversarial_semiprimes=2000 modes=DYADIC:3350,FALLBACK_T:883,FALLBACK_T1:45`

Coverage:

- `76,122` exact local valuation-law checks;
- `357` modular recurrence checks against direct exact `A_s`;
- all `4,278` distinct semiprimes from prime pairs `5<=p<q<=499`;
- `928` synchronized dyadic cases, all satisfying `q<2p` and the fallback theorem;
- `2,000` deterministic adversarial semiprimes using primes up to `5000`, emphasizing adjacent primes, near-`2p` boundaries and highly imbalanced factors.

Zero failures were observed.

Finite computation is regression evidence only. Universal closure is supplied by Sections 3–7.

## 10. Phase-B comparison with withheld supplemental execution

After Phase-A freeze, Draft PR #715 / `RR-D693BD1103CCAE5F354E` was opened.

The independent proof and the supplemental execution agree on every load-bearing theorem component:

1. same integer kernel
   \[
   A_s=\binom{2s}{s}^2\binom{3s}{s};
   \]
2. same local valuation formula for `s<r`;
3. same first-dyadic alternative `p` versus synchronized `N`;
4. same implication `gcd=N -> q<2p`;
5. same public fallback `floor(sqrt(N)/3), +1`;
6. same exact positive theorem for every distinct odd semiprime in the stated domain;
7. same explicit boundary that no factoring speedup has been proved.

The proofs are independently phrased:

- the supplemental fallback uses the residue class of `q mod 3`;
- this replay uses the impossibility of placing two odd primes greater than `3` in the three-integer block immediately above `3t`.

These are equivalent routes to the same endpoint inequality.

The main implementation difference is substantive:

- the supplemental execution deliberately constructs exact growing integers to avoid modular division;
- this replay proves all actually inverted denominators satisfy `s<p`, so modular inversion is legal and yields an `O(log N)`-memory streaming constructor.

No contradiction or hidden extra assumption was found in the supplemental theorem.

Phase-B disposition:

\[
\boxed{\texttt{INDEPENDENT_RECONSTRUCTION_CONFIRMED}}
\]

with a stronger streaming implementation boundary.

## 11. Current tool/method dedup

Current tool coverage was checked only after Phase-A freeze, as required by the blind-forward protocol.

Relevant existing surfaces:

- `T1_SCALE_ENUMERATION_VALUATION` already owns general valuation/local-to-global arithmetic machinery;
- `domain.prime_toolkit` and `src/enterprise_math/prime_method_inventory.json` already contain classical bounded primality, prime enumeration and least-factor baselines.

The present constructor does **not** reuse prime enumeration or least-factor search; those are explicitly outside the N-only constructor route.

The result also does not justify a new global tool family. Its accepted value is one exact theorem-level composition of:

- factorial valuation;
- public dyadic probing;
- gcd observation;
- a synchronization inequality;
- integer square root.

Therefore:

`METHOD_HARVEST = NO_TOOL_PAYLOAD / RESULT_ONLY`.

No new tool-family promotion is requested.

## 12. Exact task outputs

Phase-A proof freeze:

`research_artifacts/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY/PHASE_A_FREEZE.md`

Independent checker:

`scripts/check_prime_coord_factor_nonly_valuation_wall_replay.py`

Durable return:

`research_returns/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY_RETURN_20260827.md`

Execution provenance:

`research_execution_records/RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY/ER-6D2FA59F8E8D388A5F8D.json`

## 13. Residue and Driver recommendation

Within the task's hard target:

\[
\boxed{\texttt{UNRESOLVED_RESIDUE = NONE}}
\]

The universal N-only splitter is closed.

Outside the hard target, one algorithmic question remains:

> Can the `Theta(p)` valuation-wall index be compressed below square-root scale in input magnitude, or compared favorably against classical factorial/product-tree factorization baselines?

That is a complexity/benchmark frontier, not a defect in the theorem proved here.

Recommended Driver disposition:

`ACCEPTED / EXACT_N_ONLY_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM / RESULT_ONLY`.

The Driver should preserve the parent fixed-public-prefix no-go and this result simultaneously:

- fixed finite public-prefix probes are insufficient;
- an N-dependent public seed schedule escapes that obstruction and gives exact factor extraction;
- no asymptotic speedup follows.

Any further benchmarking, hidden-factor separation-spectrum analysis, Lean formalization or external prior-art comparison should be separately routed according to current portfolio value rather than treated as missing proof obligations of this completed replay.

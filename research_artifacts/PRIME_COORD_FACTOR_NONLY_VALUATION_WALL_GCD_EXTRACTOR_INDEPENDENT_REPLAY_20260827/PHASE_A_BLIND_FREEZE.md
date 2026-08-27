# PCF4R Phase-A Blind Freeze — N-only valuation-wall extractor

Status: `PHASE_A_FROZEN / INDEPENDENT_DERIVATION_COMPLETE / CHECKER_FROZEN`

Researcher-ID: `EM-PCF4R-6D8A31`

Task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Publication: `TP2-DF186CDB4959BEA10875`

Claim: `chatgpt-pcf4r-20260827-1933-6d8a31`

Phase-A allowed inputs: the published taskbook, accepted parent result `RR-A33E88150B0DAD0B13B8`, elementary number theory, and independently authored exact-integer code.

At this freeze the originating non-authoritative duplicate execution, its derivation, scripts, return, and discussion have **not** been opened.

## 1. Phase-A verdict

The target construction is independently reconstructed positively for every distinct odd semiprime

`N=pq`, with `3<p<q` prime.

The resulting deterministic constructor uses only `N`, public seed indices, modular arithmetic, and gcd. It returns a nontrivial factor. Its worst-case seed scale is `Theta(sqrt(N))`, so this is an exact factor-blind asymmetry generator, **not** a factoring-speedup theorem in input bit length.

Phase-A candidate verdict:

`N_ONLY_GCD_EXTRACTOR_VERIFIED_PHASE_A_CANDIDATE`.

## 2. Integral observable and exact recurrence

Define

`A_s=(2s)!(3s)!/(s!)^5`.

There is an elementary integrality identity

`A_s = C(2s,s)^2 C(3s,s)`.

Hence `A_s` is an integer for every `s>=0`.

Also

`A_0=1`,

`A_{s+1} = A_s * 6(2s+1)(3s+1)(3s+2)/(s+1)^3`.

The division is exact because both sides equal the factorial/binomial definition. The checker cross-checks this recurrence against the direct binomial formula.

## 3. Exact local valuation wall

### Lemma 3.1

Let `r>3` be prime and `0<=s<r`. Then

`v_r(A_s)=floor(2s/r)+floor(3s/r)`.

### Proof

Since `s<r`, `v_r(s!)=0`. Also `2s<2r` and `3s<3r`. For `r>=5`,

`3r-3 < r^2`,

so neither `(2s)!` nor `(3s)!` contains a contribution from `r^2`. Legendre's formula therefore reduces to

`v_r((2s)!)=floor(2s/r)`,

`v_r((3s)!)=floor(3s/r)`,

and subtracting `5v_r(s!)=0` gives the formula. QED.

### Corollary 3.2 — first wall

For prime `r>3` and `0<=s<r`,

`r | A_s` iff `3s>=r`.

Thus the first positive index at which `r` divides the observable is

`h_r=ceil(r/3)`.

Indeed if `3s<r`, both floor terms vanish. If `3s>=r`, the second floor term is already positive.

## 4. First dyadic nonunit alternative

Let `N=pq` with `3<p<q` distinct primes. Set

`h=ceil(p/3)`

and let `d` be the least power of two satisfying `d>=h`.

Then

`d < 2h <= 2(p+2)/3 < p`

because `p>4`. Hence `d<p<q`, so the local valuation lemma applies simultaneously to `p` and `q` at `s=d`.

The preceding dyadic seed satisfies

`d/2 < h`,

hence

`3d/2 < p`.

Therefore every earlier dyadic seed is a unit modulo `N`, while at `d` we have `p|A_d`. Exactly two cases remain:

1. `q>3d`. Then `q` does not divide `A_d`, so
   `gcd(A_d,N)=p`.
2. `q<=3d`. Then both primes divide `A_d`, so
   `gcd(A_d,N)=N`.

Thus the **first** dyadic nonunit is always either the desired factor `p` or a synchronized `N` event. There is no third case.

This yields an N-only stopping rule: start at `d=1`, repeatedly double, and stop at the first `gcd(A_d,N)>1`. A public cap `d<=floor(sqrt(N))` makes the routine syntactically total; the theorem guarantees termination strictly before `p<sqrt(N)`.

## 5. Synchronization implication

In the synchronized case,

`q <= 3d`

while the previous-unit inequality gives

`p > 3d/2`.

Therefore

`q <= 3d < 2p`,

so

`q<2p`.

This is the exact endpoint control needed by the square-root fallback.

## 6. Two-seed square-root fallback

Assume synchronization and define

`t = floor(sqrt(N)/3)`.

Since `N` is not a square,

`t < sqrt(N)/3 < t+1`.

Because `p<sqrt(N)<q`,

`p/3 < sqrt(N)/3 < q/3`.

Also synchronization gives `q<2p`, hence

`sqrt(N) < sqrt(2) p < 3p/2`,

so

`t+1 < p/2+1 < p`.

Thus both fallback seeds `t,t+1` lie in the local-valuation range `s<p<q`.

At `s=t`, we always have

`3t < sqrt(N) < q`,

so `q` does not divide `A_t`.

- If `3t>=p`, then `p|A_t` and `gcd(A_t,N)=p`.
- Otherwise `3t<p`. Since `sqrt(N)<3(t+1)` and `p<sqrt(N)`, we have `p<3(t+1)`, so `p|A_{t+1}`.

It remains to exclude `q|A_{t+1}` in the second subcase. If instead `q<=3t+3`, then

`3t < p < q <= 3t+3`.

Because `q>3`, `q` cannot equal the multiple of three `3t+3`. Thus `p` and `q` would both have to be the two consecutive integers `3t+1,3t+2`. One of those is even, so they cannot both be odd primes. Contradiction.

Therefore `q>3(t+1)`, and

`gcd(A_{t+1},N)=p`.

Hence one of the two public fallback seeds `t,t+1` always returns the nontrivial factor.

## 7. N-only modular constructor

A probe need not materialize the exponentially large integer `A_s`.

Use

`C(2s,s)=prod_{j=1}^s(s+j)/s!`,

`C(3s,s)=prod_{j=1}^s(2s+j)/s!`.

Compute modulo `N`

`D=s!`,

`U_2=prod_{j=1}^s(s+j)`,

`U_3=prod_{j=1}^s(2s+j)`.

First compute `g=gcd(D,N)`.

- If `1<g<N`, this already is a nontrivial factor obtained solely from public `N,s`.
- If `g=1`, invert `D` modulo `N` and compute
  `B_2=U_2 D^{-1}`, `B_3=U_3 D^{-1}`, and
  `A_s mod N = B_2^2 B_3 mod N`.

For every theorem-relevant dyadic or fallback probe we proved `s<p`, so every integer `1,...,s` is coprime to `pq`; consequently `g=1` and the modular divisions are justified. No hidden factor enters the constructor.

The task-local checker independently cross-checks this modular constructor against exact `A_s` whenever the denominator is a unit.

## 8. Complexity

Let `n=ceil(log2 N)`.

A probe at seed `s` uses `O(s)` modular multiplications plus gcd/inversion on `O(n)`-bit integers, with `O(n)` working memory.

The dyadic seed sizes form a geometric series, so the total work before the first nonunit is `O(d poly(n))`. In the synchronized branch the two fallback probes have size `O(sqrt(N))`. Therefore the full elementary implementation has

`O(sqrt(N) poly(log N))`

bit complexity and

`O(log N)`

working memory (apart from fixed-size trace/output bookkeeping).

This is exponential in input bit length `n` (roughly `2^(n/2) poly(n)`) and therefore is not claimed as an asymptotic factoring speedup.

## 9. Independent checker freeze

Frozen checker:

`scripts/check_prime_coord_factor_nonly_valuation_wall_replay.py`

Frozen checker commit:

`f785a3dee5f451c84b28c0decaa652c3be42ac72`

Independent bounded validation performed before this document was frozen:

- local valuation formula: all `r>3` prime with `r<=1000`, all `0<=s<r`: `76,122` exact cases, zero failures;
- recurrence versus direct binomial observable: `s=0..79`: `80` exact cases, zero failures;
- modular constructor versus direct observable for `5<=N<400`, `0<=s<30` whenever `s!` is a unit mod `N`: `3,196` exact cases, zero failures;
- every distinct prime pair `3<p<q<=1000`: `13,695` semiprimes, zero extraction failures;
- among those semiprimes: `10,699` split at the first dyadic nonunit and `2,996` entered synchronized fallback, all fallback cases succeeded.

These finite checks are regression evidence only. Universal correctness is supplied by Sections 3–7.

## 10. Phase-B gate

Phase A is now frozen. Only after this commit may the withheld supplemental duplicate execution be opened for comparison, followed by current tool/method dedup. No source-comparison claim is made in this Phase-A document.

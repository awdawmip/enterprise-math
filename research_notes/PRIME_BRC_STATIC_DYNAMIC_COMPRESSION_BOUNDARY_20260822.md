# Prime-BRC Static/Dynamic Compression Boundary

Status: `OWNER_LOCAL_L3 / RESEARCH_CHECKPOINT / NOT_CANONICAL`
Date: `2026-08-22`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

This note records the strongest current Prime-BRC representation boundary.  It does **not** prove Legendre's conjecture.

## 1. Static exact-support rigidity

Let

`I_k={k^2+1,...,(k+1)^2-1}`.

For every `1<=d<=k`, `I_k cap dZ` contains at least two consecutive multiples of `d`.  Therefore the first-two hit gap recovers `d`, and

`d -> I_k cap dZ`

is injective on `[1,k]`.

In the P017-L020 large-prime-tail branch `n=S_k(n)Q_k(n)`, `Q_k(n)>k` implies `S_k(n)<=k`.  Every squarefree small-prime sieve modulus relevant to that state divides `rad(S_k(n))<=S_k(n)<=k`.

Freeze owner-local boundary:

`LARGE_PRIME_TAIL_CORE_HAS_NO_NONTRIVIAL_CURRENT_EXACT_SUPPORT_RECOALESCENCE`.

The large-modulus singleton regime `d>=2k` is absent from this hard core.

## 2. Exact quotient-support rigidity

For `1<=d<=k`, the exact quotient image is

`Q_d(k)=[floor(k^2/d)+1, floor(k(k+2)/d)]`.

If `d<e<=k`, then

`k^2/d-k^2/e >= k/(k-1)>1`,

so the lower endpoints are strictly ordered.  Hence

`d!=e <=k -> Q_d(k)!=Q_e(k)`.

Thus one real division does not create exact-support collisions among distinct cumulative small-core divisors in the L020 prime-tail hard core.

What may recoalesce without loss is factor **order** after the cumulative product is already the same; floor quotienting is path-flat in the product.

Freeze:

`DIFFERENT_CUMULATIVE_DIVISORS_REMAIN_EXACT_QUOTIENT_DISTINGUISHABLE`.

## 3. Root-terminal cancellation exists but is not recursively suffix-safe

At `k=22`:

- `d=15`, `mu(d)=+1`, quotient support `{33,34,35}`;
- `d=17`, `mu(d)=-1`, quotient support `{29,30,31}`.

Both quotient multisets collapse to exactly three copies of root `5`.  Therefore a computation whose declared terminal observable is only quotient root may cancel

`+3[5]-3[5]=0`.

But the exact quotient supports differ, and their later factor behaviour differs.  Therefore the same cancellation is not suffix-safe for recursive primality/factorization semantics.

Freeze:

`ROOT_TERMINAL_RECOALESCENCE != RECURSIVE_FACTOR_RECOALESCENCE`.

## 4. Terminal-tail projection is prime-complete but transition-expensive

Strip every prime-power factor `<=k` from `n in I_k`, giving

`n=S_k(n)Q_k(n)`.

P017-L020 gives `Q_k(n)=1` or one prime `>k`.

For a prime state, `S_k(n)=1` and `Q_k(n)=n in I_k`.

For a composite state, either `Q_k(n)=1`, or `S_k(n)>=2` and

`Q_k(n)<=((k+1)^2-1)/2<k^2`

for `k>=3` (the small cases are direct).

Hence the terminal tail is a complete prime readout:

`n prime <=> Q_k(n) lies in I_k`.

At this terminal future observable, all subset/inclusion-exclusion branches of a composite state can recoalesce and cancel.  However computing the terminal tail has already executed complete small-factor stripping.  The compression therefore moves the hard work into the transition.

Freeze:

`TAIL_PROJECTION_IS_PRIME_COMPLETE_BUT_NOT_A_FREE_COMPRESSION_ORACLE`.

## 5. Signed carrier boundary

Boolean BRC cannot retain opposite sieve signs.  Example at `k=10`, state `105`:

- modulus `21` and modulus `105` both have singleton current support `{105}`;
- `mu(21)=+1`, `mu(105)=-1`.

A signed coefficient carrier is therefore necessary before cancellation.  Count-level signed cancellation is consistent with the independent R063 Stage-3 result that count-level opposite-sign cancellation is confluent, while position-retaining destructive cancellation is not.

But upgrading to a signed carrier does not remove Sections 1-2: in the large-prime-tail core there are no identical current or exact-quotient supports to merge.

Freeze:

`SIGNED_CARRIER_IS_NECESSARY_FOR_PARITY_CANCELLATION_BUT_STATIC_SIGNED_BRC_DOES_NOT_COMPRESS_THE_TAIL_CORE`.

## 6. Quotient-phase process credit

For any integer interval `A<n<B` and true cumulative divisors `D|E|n`, define

`Theta_D(n)=(n/D-floor(A/D))/(floor(B/D)-floor(A/D))`.

Then

`Theta_E(n)>=Theta_D(n)`.

The increment is the ordinary exact quotient-phase lead on the D-quotient interval.  Along a divisor chain, increments are nonnegative, additive and path-flat.  For a full factorization ending at `D=n`, terminal phase is `1`, so total phase credit is

`1-(n-A)/(B-A)`.

This is a genuine scalar process cocycle.  It does not by itself solve the prime-existence problem.

Moreover `(kappa,chi)` is not enough to recover quantitative phase: at `k=6,d=5`, hits `40` and `45` share the same basin-level `(kappa,chi)=(0,0)` but have different phase and phase lead.

Freeze:

`PHASE_CREDIT_IS_PATH_FLAT_NONNEGATIVE_BUT_REQUIRES_WITHIN_WINDOW_POSITION_BEYOND_KAPPA_CHI`.

## 7. Relation to the P3 / Type-II frontier

Campbell (2026) proves an explicit `P3` result in every consecutive-square interval using a Richert weighted sieve and explicitly identifies the `P3 -> P2` step as beyond that framework without more flexible bilinear input.

For a rough triprime `n=pqr`, `p<=q<=r`, there is necessarily a nontrivial factor block at the scale

`n^(1/4) <~ d <= n^(1/2)`

(obtain `d=pq` when `pq<=sqrt(n)`, otherwise use a middle prime factor).  Since `n~k^2`, this is the `sqrt(k)` to `k` scale.

Prime-BRC interpretation:

`PARITY_ONLY / BOOLEAN_SUPPORT` merges prime and squarefree triprime parity classes; a parity-breaking continuation must retain factor-pair/bilinear incidence at this intermediate scale or some provably equivalent extra information.

This is consistent with R063 Stage 3: signed count-level cancellation may be lawful, but source-sensitive pair/position information cannot be destructively collapsed before its future role is discharged.

## 8. Current hard question

The useful missing object is now sharply typed:

`PRIME_BRC_INTERMEDIATE_FUTURE_SIGNATURE`.

It must be:

1. strictly coarser than exact quotient support, so nontrivial recoalescence actually occurs;
2. strictly finer than root-only projection, so recursive prime/factor semantics remain recoverable;
3. closed under true factor-stripping transitions;
4. not equivalent to precomputing the complete factorization / terminal tail;
5. able to retain the factor-pair/bilinear information needed to distinguish prime from the P3 parity class.

Until such a signature or a no-go theorem is found, further static carry/support re-encodings should be treated as low priority.

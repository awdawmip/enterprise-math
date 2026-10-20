# PCF3 Hidden-Factor Separation Spectrum — Integrated Evidence Report

Status: `TASK-LOCAL / EXACT THEOREM / DISCLOSED PARALLEL METHOD-HARVEST`

Canonical execution authority for this return is `EM-PCF3-C321DA` / claim `chatgpt-pcf3-20260828-0742-c321da`. A concurrent source-exposed branch, Draft PR #761 (`EM-PCF3-DCEC44`, head `48231a8ddd8852bbef09d538c754ef42118e9f46`), appeared after the canonical claim and after the C321DA cyclotomic sub-spectrum had already been derived. Its scheduler comments are not runtime authority because their bodies append `AGENT_STATE` text after JSON, but its mathematical artifacts are disclosed evidence and were method-harvested.

The final result therefore separates provenance from mathematics:

1. the cyclotomic five-state spectrum was independently derived on the canonical owner branch;
2. the valuation-wall theorem was harvested from PR #761, then re-derived from Legendre's formula in the canonical return rather than accepted from control-plane status;
3. no Driver or Foundation authority is inferred from the parallel PR.

## Exact valuation-wall theorem

For

`A_s = (2s)!(3s)!/(s!)^5 = binom(2s,s)^2 binom(3s,s)`

and a prime `r>3` with `0 <= s < r`, Legendre gives exactly

`v_r(A_s)=floor(2s/r)+floor(3s/r)`.

Indeed the denominator contributes no `r`, and `3s<3r<r^2`, so no higher `r^j` term occurs. Thus the local valuation is 0,1,2,3 according as

- `r>3s`,
- `2s<r<3s`,
- `3s/2<r<2s`,
- `s<r<3s/2`.

For squarefree `N=pq`, define `D_0=1`, `D_k=gcd(A_s,N^k)` and `H_k=D_k/D_{k-1}`. Then

`H_k = product_{r in {p,q}, v_r(A_s)>=k} r`.

So the first three nested walls are exactly `3s`, `2s`, `3s/2`.

## First-dyadic classification

Let `s_*` be the least power of two with `3s_*>p`. Then minimality gives

`3s_*/2 < p < 3s_* < 2p` and `s_*<p`.

At this first wall exactly four cases occur:

- `q>3s_*`: `H1=p` directly;
- `p<2s_*<q<3s_*`: `(H1,H2,H3)=(N,p,1)`;
- `2s_*<p<q<3s_*`: `(H1,H2,H3)=(N,1,1)` and `q/p<3/2`;
- `3s_*/2<p<q<2s_*`: `(H1,H2,H3)=(N,N,1)` and `q/p<4/3`.

There is no fifth case. `H3` is redundant at the first synchronized dyadic wall.

## One-seed synchronization breaker

In either fully synchronized case, already `q<2p`. Put

`u=floor(isqrt(N)/3)+1`.

Because `N=pq` is nonsquare, `3u` is the least multiple of 3 strictly above `sqrt(N)`, hence `p<sqrt(N)<3u`. Also `q<2p` gives `u<p` for `p>=5`.

To show `3u<q`, use `q mod 3`:

- if `q=1 mod 3`, then `q-1` is a multiple of 3 and `p<=q-2`, so `sqrt(pq)<q-1`;
- if `q=2 mod 3`, the possibility `p=q-2` would force `p>3` to be divisible by 3, so `p<=q-4`, hence `sqrt(pq)<q-2`.

Therefore the least multiple of 3 above `sqrt(N)` is below `q`: `p<3u<q`, while `u<p`. The valuation formula then gives `p|A_u` and `q∤A_u`, so

`gcd(A_u,N)=p`.

This proves an exact N-only separator on every distinct odd semiprime: precheck `gcd(N,6)` for factor 3; otherwise scan dyadic `s` to the first `H1!=1`, use proper `H1` if present, then `H2`, and finally the one public seed `u` if still synchronized. The result is exact but not a speedup theorem: direct kernel generation still reaches index `Theta(p)` on balanced inputs.

## Cyclotomic five-state sub-spectrum

For the PCF1-admitted public polynomial family

`x^2+1, x^2+x+1, x^6-1, x^6+1`, 

the local zero vector for every prime `ell>3` has only five states, controlled by multiplicative orders `1,2,3,4,6,12`. Exact state counts depend only on `ell mod 12`; the canonical owner checker verifies the table for all 61 odd primes below 300, 190 prime-pair collision formulas and 10,805 small CRT seeds.

This sub-spectrum supplies two useful boundaries: `x^6-1` has positive exact uniform-seed split probability for every distinct odd semiprime, while any fixed finite public seed prefix for a fixed finite polynomial family has infinitely many synchronized prime pairs. The explicit `0..63` collision frozen by the owner checker is

`p=62523502271`, `q=62523502303`, `N=3909188338232494230113`.

## Finite evidence

Canonical owner cyclotomic checker:

`PCF3_SPECTRUM_CHECK_PASS primes=61 pairs=190 crt=10805 corpus=84/89 semiprime=43/48 fixed64=3909188338232494230113`

Canonical owner independent cyclotomic checker:

`PCF3_INDEPENDENT_CHECK_PASS primes=45 pairs=120 fixed64=3909188338232494230113 aggregate=84/89`

Disclosed parallel PR #761 reports, and its files expose, a wall-spectrum checker with 61/61 theorem-domain PCF2 cases and an independent enumeration of 1,830 distinct odd semiprimes below prime 300 with zero failures. Those finite counts are supporting regression only; theorem closure is the proof above.

## Boundary

The smallest unresolved residue is `COMPLEXITY_COMPRESSION_OF_VALUATION_WALL`. No polynomial-time, sub-square-root, novel factoring exponent, Working Truth, Foundation authority, or canonical theorem promotion is claimed here.

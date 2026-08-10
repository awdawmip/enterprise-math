# P022 — Mod-3 sieve for primitive Franel capture

Status: `PROVED_WIP / EXACT CAPTURE SIEVE`  
Owner: `P022 / program/p022-geometry-v2`  
Depends on: primitive successor-capture theorem  
Scope: isolate the only residue class in which one-step primitive capture can defer

## 1. Setup

Let `p` be a primitive Franel prime at rank `r>=2`:

\[
p\mid F_r,
\qquad
p\nmid F_j\quad(1\le j<r).
\]

The successor-capture theorem already proves that this event enters the pure
Franel defect lattice at `D_r` or `D_(r+1)` unless

\[
2r-1
\quad\text{and}\quad
2r+1
\]

are both prime.

The exceptional case is a twin-prime center.  Reducing the two neighboring odd
boundaries modulo three almost completely removes that exception.

## 2. P022-LI50 — rank `2 mod 3` forces direct capture

Assume

\[
r>2,
\qquad
r\equiv2\pmod3.
\]

Then

\[
2r-1\equiv0\pmod3.
\]

Since `r>2`, the odd boundary exceeds `3`, so it is composite.  Therefore the
pure defect `D_r` exists and every primitive prime at rank `r` gives the direct
pivot

\[
\boxed{
v_p(D_r)=v_p(F_r)>0.
}
\]

Thus

\[
\boxed{
r\equiv2\pmod3,\ r>2
\Longrightarrow
\text{automatic positive capture at }D_r.
}
\]

## 3. P022-LI51 — rank `1 mod 3` forces capture by the successor

Assume

\[
r>2,
\qquad
r\equiv1\pmod3.
\]

Then

\[
2r+1\equiv0\pmod3.
\]

Again this odd boundary is greater than `3`, hence composite.

If `2r-1` is already composite, the primitive event is captured positively at
`D_r`.  If `2r-1` is prime, the successor-capture theorem applies because
`2r+1` is composite and gives

\[
\boxed{
v_p(D_{r+1})=-v_p(F_r)<0.
}
\]

Therefore

\[
\boxed{
r\equiv1\pmod3,\ r>2
\Longrightarrow
\text{automatic capture at }D_r\text{ or }D_{r+1}.
}
\]

## 4. P022-LI52 — every genuine twin-prime deferral rank lies in `3Z`

Suppose `r>2` is an immediate-capture deferral center, so both

\[
2r-1,\qquad2r+1
\]

are prime.

If `r=1 mod 3`, then `2r+1` would be a nontrivial multiple of three.  If
`r=2 mod 3`, then `2r-1` would be a nontrivial multiple of three.  Both are
impossible.

Hence

\[
\boxed{
r\equiv0\pmod3.
}
\]

The small rank `r=2` is the isolated exception, centered on the twin primes
`3,5`.

Combining LI50--LI52:

\[
\boxed{
r>2,\ 3\nmid r
\Longrightarrow
\text{every primitive Franel event at }r
\text{ is captured within one defect step}.}
\]

So the only rank residue class in which the twin-prime geometry can obstruct
immediate capture is

\[
\boxed{r\equiv0\pmod3.}
\]

## 5. Examples already in P022

The existing exact witnesses line up cleanly with the sieve.

- `r=8=2 mod 3`, primitive prime `369581`: direct positive capture at `D_8`.
- `r=50=2 mod 3`, primitive prime `149` and primitive prime `518220701`:
  direct positive capture at `D_50`.
- `r=16=1 mod 3`, primitive prime `157`: current boundary `31` is prime but
  successor boundary `33` is composite, so the row is captured at `D_17` with
  valuation `-1`.
- `r=49=1 mod 3`, the Pocklington-certified large primitive prime is captured
  at `D_50` because `99` is composite.
- `r=6=0 mod 3`, primitive primes `13` and `73`: the twin pair `11,13` produces
  a genuine immediate deferral.

The congruence sieve predicts all of these locations before looking at the
actual primitive prime value.

## 6. Infinite-theorem frontier after the sieve

The zero-geometry route already proves that Franel primitive events occur at
unbounded ranks.  Before LI50--LI52, converting that fact into infinitely many
captured Barlow defect events required controlling the primality of both odd
neighbors of those ranks.

The new sufficient target is strictly simpler:

\[
\boxed{
\text{prove that primitive Franel ranks }r_p\not\equiv0\pmod3
\text{ occur infinitely often}.}
\]

Every such rank above two automatically supplies a defect-lattice capture.
No twin-prime analysis is then needed.

A still stronger direct-pivot target is

\[
\boxed{
r_p\equiv2\pmod3\text{ infinitely often},}
\]

because those events land immediately on composite `D_(r_p)` columns.

This does not prove either infinitude statement.  It identifies the residue
question that is sufficient.

## 7. Forced-midpoint family and empirical pressure test

For the explicit midpoint source primes

\[
p\equiv5,23\pmod{24},
\]

the forced midpoint

\[
m=\frac{p-1}{2}
\]

satisfies

\[
m\equiv2\pmod3.
\]

Therefore every **primitive midpoint** in these classes is automatically a
direct composite-boundary pivot.  If the midpoint is not primitive, the first
rank may move to another residue class.

A noncanonical scan of primes below `20000` with nonempty Franel zero alphabet
found a strong bias toward `r_p=2 mod 3` in the two classes `p=5,23 mod 24`, but
also many examples with first rank `0` or `1 mod 3`.  The residue class is
therefore not determined by `p mod 24` alone.

This scan is heuristic route guidance only.  No density claim is made.

## 8. Executable assets

`src/enterprise_math/p022_barlow_primitive_successor_capture.py` now exposes:

- `mod3_forced_capture_location`;
- `twin_prime_deferral_requires_rank_multiple_of_three`.

The companion tests lock the two forced residue classes, the rank-two
exception, and the existing positive/negative/twin-deferral witnesses.

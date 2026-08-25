# P017 — Two-Stage P2 Gap Bootstrap: May-2026 Maximal-Gap Refresh

Status: `PROVED_WIP CURRENT-DATA TRANSFER + EXACT ENDPOINT CERTIFICATE / NOT CANONICAL / EXTERNAL COMPUTATION DEPENDENCY`

Date: `2026-08-25`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on the abstract theorem in `P017_P2_TWO_STAGE_PRIME_GAP_BOOTSTRAP_20260825.md`.

## 1. Current confirmed maximal-gap input

The current Prime Number Gap Record Rising table, updated 22 June 2026, lists consecutively:

- 84th confirmed maximal gap: size `1724`, starting at
  `68,068,810,283,234,182,907`;
- 85th confirmed maximal gap: size `1854`, starting at
  `101,412,319,996,363,309,069`, verified in May 2026.

Because the second entry is the next confirmed **maximal** gap after the 1724 record, every consecutive-prime gap whose starting prime is below

\[
B_{85}=101{,}412{,}319{,}996{,}363{,}309{,}069
\]

has size at most `1724`.

Equivalently, in the same finite uniform-gap sense used by Campbell,

\[
\boxed{
0<x<B_{85}\Longrightarrow
\exists\text{ prime }q\in(x,x+1724].
}
\tag{UG-2026}
\]

This is an external computational premise, not a theorem proved by Enterprise Math.

## 2. Updated two-stage parameters

Apply the abstract two-stage bootstrap with

\[
\boxed{
B=B_{85}=101{,}412{,}319{,}996{,}363{,}309{,}069,
\qquad G=1724.
}
\]

The admissibility inequality is

\[
1724K^2+B\,1724^2\le2BK.
\]

Exact integer arithmetic gives the same lower root transition as before,

\[
K_{\min}=1{,}486{,}089,
\]

and the improved upper endpoint

\[
\boxed{
K_{\max}=117{,}647{,}703{,}010{,}536{,}312.
}
\]

The inequality holds at `K_max` and fails at `K_max+1`.

## 3. Continuous finite P2 range

The lower endpoint lies far below the already quoted Sorenson-Webster verified prime range `K<=7.05*10^13`. Therefore the verified-prime range and this updated two-stage semiprime range overlap, yielding the continuous finite consequence

\[
\boxed{
1\le K\le117{,}647{,}703{,}010{,}536{,}312
\Longrightarrow
(K^2,(K+1)^2)\text{ contains a }P_2,
}
\]

conditional on the declared external computations.

The exact squared endpoint is

\[
\boxed{
13{,}840{,}982{,}023{,}655{,}354{,}809{,}893{,}685{,}870{,}561{,}344
}
\]

or approximately

\[
1.3840982\times10^{34}.
\]

This is about `1384.0982` times `10^31` in the `X=K^2` variable.

## 4. Comparison with Campbell's March-2026 cutoff

Campbell used the then-sufficient conservative uniform input

\[
B=6.8\times10^{19},\qquad G=1724,
\]

and stopped his finite P2 lemma at `K^2<=10^31` because his P3 sieve only needed a splice there.

The abstract two-stage theorem first pushed the same March input to

\[
K_{\max}=78{,}886{,}310{,}903{,}386{,}301.
\]

The May-2026 confirmation of the next maximal gap increases `B/G` and hence raises the guaranteed two-stage endpoint to

\[
117{,}647{,}703{,}010{,}536{,}312.
\]

No new analytic number theory is claimed; this is a current-data transfer through the already-proved bootstrap theorem.

## 5. Best-pair principle for future updates

For every pair of consecutive confirmed maximal-gap records

\[
(G_j,P_j),\qquad(G_{j+1},P_{j+1}),
\]

the definition of a maximal gap yields a valid finite uniform certificate

\[
UG(P_{j+1},G_j).
\]

The two-stage P2 reach is asymptotically

\[
K_{\max}\sim\frac{2P_{j+1}}{G_j}.
\]

Therefore future record-table refreshes should rank consecutive confirmed records by `P_(j+1)/G_j`, not merely by the newest gap size.

At the current confirmed frontier the pair

\[
(P_{85},G_{84})
=(101412319996363309069,1724)
\]

is the natural strongest available terminal pair in the table.

## 6. Next

Re-evaluate the explicit analytic P2 packages against the new finite splice

\[
X_{\rm finite}\approx1.3841\times10^{34}.
\]

If the analytic threshold remains substantially larger, the next material improvement must come from stronger triple-exponential-sum power saving/effective constants or a larger rigorously certified maximal-gap range; the terminal reciprocal-sum constant itself is no longer the primary obstruction.

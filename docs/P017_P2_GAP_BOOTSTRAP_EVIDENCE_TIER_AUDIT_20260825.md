# P017 — Two-Stage Gap Bootstrap Evidence-Tier Audit

Status: `PROVED_WIP EVIDENCE-BOUNDARY CORRECTION + EXACT CONSERVATIVE ENDPOINT / NOT CANONICAL`

Date: `2026-08-25`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Purpose: distinguish two external-computation evidence tiers that were too easily conflated after the May-2026 maximal-gap update.

## 1. Tier A — public exhaustive-analysis bound

The Prime Gap List Project's current `Exhaustively analyzed gaps` page explicitly states that the upper bound of exhaustive analysis was extended to

\[
\boxed{B_A=10^{20}}
\]

on 8 May 2026.

The confirmed maximal-gap tables place the 1724 record below this bound and the next 1854 record above it. Hence the conservative uniform certificate

\[
\boxed{
0<x<10^{20}\Longrightarrow
\exists\text{ prime }q\in(x,x+1724]
}
\]

is directly supported by the public exhaustive-range statement plus the record table.

Applying the already-proved two-stage bootstrap with

\[
B=10^{20},\qquad G=1724
\]

gives the exact integer interval

\[
\boxed{
1{,}486{,}089\le K\le116{,}009{,}280{,}740{,}973{,}308.
}
\]

The squared upper endpoint is

\[
\boxed{
13{,}458{,}153{,}218{,}037{,}960{,}469{,}637{,}923{,}168{,}462{,}864
}
\]

or approximately

\[
1.3458153218\times10^{34}.
\]

Together with the Sorenson-Webster prime verification below the lower splice, this gives the preferred **conservative finite P2 splice** for effectivity comparisons.

## 2. Tier B — current confirmed maximal-record interpretation

The current rising-record table separately lists the 85th confirmed maximal gap:

- size `1854`;
- starting prime `101412319996363309069`;
- verification in May 2026.

By the mathematical definition of a maximal gap, accepting that record classification yields the stronger uniform pair

\[
B_B=101412319996363309069,\qquad G=1724,
\]

and hence the stronger endpoint

\[
K\le117647703010536312.
\]

That transfer remains mathematically valid **conditional on the confirmed-maximal classification**. However, the public exhaustive-analysis summary page separately advertises the blanket exhaustive range only through `10^20`.

Therefore the project will keep the two conclusions distinct:

- `TIER_A_EXHAUSTIVE_PUBLIC_RANGE`: use `B=10^20` in conservative analytic-splice claims;
- `TIER_B_CONFIRMED_MAXIMAL_RECORD`: retain the stronger current-data endpoint as an additional conditional transfer.

The difference is only about 1.4% in K and does not affect route selection.

## 3. Research consequence

For all subsequent explicit Chen/Iwaniec/Liu threshold comparisons, use

\[
\boxed{X_{\rm splice,A}\approx1.3458\times10^{34}}
\]

unless the stronger Tier-B evidence is explicitly invoked.

This evidence audit does not weaken the abstract two-stage theorem and does not alter any analytic P017 result. It only tightens provenance discipline for the external finite computation.

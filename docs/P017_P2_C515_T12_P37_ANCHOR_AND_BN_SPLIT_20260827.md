# P017 — c=103/20 T1–T2 P(37) Anchor and Natural B×N Pair Split

Status: `PROVED_WIP EXACT ANCHOR OPTIMIZATION + SCALE ALIGNMENT / SUBROOT ERROR STILL OPEN / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T12_GLOBAL_P41_ANCHOR_PRESTRIP_20260827.md`;
- `docs/P017_P2_C515_T12_SUBROOT_ROSSER_CANONICAL_CARRIER_20260827.md`.

Purpose: replace the previously preferred P(41) common anchor by a strictly cheaper P(37) anchor with the same hard-depth class, and freeze the exact high/low ordered-pair split induced by the c515 parameter `b=93/20`.

---

## 1. P(37) strictly dominates P(41) for the finite route

At the Tier-A splice put

\[
K_0=116009280740973308,
\qquad W=K_0+1.
\]

The primorial through 37 is

\[
\boxed{Q_{37}=P(37)=7420738134810.}
\]

The largest `Q_37`-multiple below the full basin length `2K_0` is

\[
\boxed{L_{37}=31266Q_{37}=232016640662977460.}
\]

Hence

\[
\boxed{2K_0-L_{37}=1762958977156<Q_{37}.}
\]

The relative interval loss is

\[
\boxed{
\frac{2K_0-L_{37}}{2K_0}<\frac{76}{10^7}=7.6\times10^{-6}.
}
\]

Because `Q_37|L_37`, every small sieve factor through 37 strips exactly from every mixed modulus by the adaptive anchor identity. Thus every remaining hard Rosser prime is at least `41`.

For every remaining sub-root pair `rp`,

\[
Q=\frac{D}{rp}\le D^{2/3}=W^{20/27}.
\]

Exact integer exponentiation proves

\[
\boxed{41^8>W^{20/27},\qquad 41^7<W^{20/27}.}
\]

Therefore the stripped hard Rosser part still satisfies

\[
\boxed{\omega(b)\le7.}
\]

The P(41) anchor also gives depth seven but loses more than `7.75e-4` of the full basin. P(37) loses less than `7.6e-6`, so P(37) strictly dominates P(41) for the current finite-depth objective. The earlier P41 theorem remains true but is superseded as the preferred anchor.

---

## 2. c515 forces a natural physical split

Keep

\[
a=6,\qquad b=\frac{93}{20},\qquad d=\frac59.
\]

Let the analytic square-scale variable be `x=W^2`, so the total sieve level is

\[
D=x^{5/9}.
\]

Define

\[
\boxed{B=D^{b/a}=x^{31/72}}
\]

and

\[
\boxed{N_0=\frac DB=x^{1/8}.}
\]

The exponent identity is exact:

\[
\frac59-\frac{31}{72}=\frac18.
\]

For every remaining ordered pair `(r,p)` the inner upper-sieve level is

\[
Q(r,p)=\frac D{rp}.
\]

This yields two exact regimes.

### High-pair regime

If

\[
\boxed{rp\ge B,}
\]

then

\[
\boxed{Q(r,p)\le N_0=x^{1/8}.}
\]

At the Tier-A splice this is the same small level already appearing at the lower endpoint of the certified terminal T4 calculation. In particular the beta-2 upper-Rosser `j=1` condition forces the largest sieve prime `q_1` to satisfy

\[
q_1^3<N_0,
\]

and exact integer comparison gives

\[
23^3<N_0<29^3.
\]

Thus only sieve primes at most 23 can occur in this high-pair upper-Rosser tail; it is a finite activation-threshold problem rather than a generic deep sieve.

### Low-pair regime

If

\[
\boxed{rp<B,}
\]

then the inner level factors exactly as

\[
\boxed{
Q(r,p)
=\frac{B}{rp}\,N_0.
}
\]

Therefore any factorable representation of the inner upper-sieve coefficient at levels

\[
D_1=\frac{B}{rp},
\qquad
D_2=N_0
\]

produces physical factors

\[
(rp)d_1\le B,
\qquad
d_2\le N_0.
\]

These are precisely the c515 long/short scales underlying the already-legal trivial-pair Lemma-4 window.

---

## 3. Why this is the correct next partition

The previous T1–T2 reduction left one sub-root ordered-pair carrier. The c515 packet now splits it without introducing a new free parameter:

\[
\boxed{
\begin{array}{lll}
rp\ge B &: & \text{finite upper-Rosser tail at level }\le x^{1/8},\\
rp<B &: & \text{factorable analytic sector with }(B/(rp))\cdot x^{1/8}.
\end{array}
}
\]

Thus the high-pair sector should be attacked by a T4-style finite support reindexing, while the low-pair sector should be compared between:

1. direct fixed-depth factorization after the P37 prestrip; and
2. Iwaniec's well-factorable upper-sieve variant.

No finite P2 theorem or all-K claim is made here.

# Addendum — near-rational family forces linearly many Farey epochs

Date: 2026-11-09. Frozen scientific source: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent: `PROOF.md` in this directory, concerning the auxiliary S23/AV BRC-labelled residual-phase observer.
Status: author-side elementary theorem; checked finite arithmetic certificate; independent mathematical review pending.

## Theorem

Fix integers `3<=m<=N` and any irrational `theta=1/2+epsilon` with `0<epsilon<1/(2N)`. For every `m<=n<=N`, let `H=n-1`, and let `q_H` be the largest odd integer not exceeding H. The two neighbouring fractions in the Farey sequence of order H that enclose theta are exactly

`1/2 < theta < (q_H+1)/(2*q_H)`.

In particular, if `q_0` and `q_N` are the largest odd integers not exceeding `m-1` and `N-1`, respectively, then the number of distinct Farey-neighbour epochs across the entire integer interval `m<=n<=N` is precisely

`E_theta(m,N)=1+(q_N-q_0)/2`.

For fixed m, this is `Omega(N)` **uniformly adversarial over the slope theta as theta may depend on N**. Hence an algorithm that explicitly processes every Farey epoch cannot claim an `O(log N)` uniform-in-theta epoch count. The theorem does not require that every epoch change the Bayes risk and does not by itself bound the number of maximal risk-value blocks.

## Proof

Any reduced rational fraction p/q > 1/2 with 1<=q<=H satisfies `2p-q>=1`, so

`p/q-1/2=(2p-q)/(2q)>=1/(2H)>epsilon`.

Thus no order-H Farey fraction lies in the open interval `(1/2,theta)`: the lower neighbour is 1/2 itself. The least fraction strictly above 1/2 in the order-H sequence is `(q_H+1)/(2q_H)`, since its odd denominator q_H attains the largest denominator among the solutions of `2p-q=1`; fractions with `2p-q>=2` lie farther above 1/2, with lower bound `1/H>=1/q_H` (and for H=2 the only alternative is 1, farther). Its determinant with 1/2 is `2*(q_H+1)/2-q_H=1`; it is therefore the right Farey neighbour. The same strict bound ensures theta lies strictly beneath it.

As H ranges from m-1 to N-1, q_H changes exactly once for every two increments of H and assumes every successive odd integer from q_0 through q_N. The claimed exact epoch count follows. QED.

## One fixed irrational input with a large exact finite window

Set `theta_* = 1/2+sqrt(2)/10^12`. This one fixed irrational number satisfies `0<theta_*-1/2<1/(2N)` for every integer `N<=10^11`, since `sqrt(2)<5`.

With m=128, the theorem yields exactly **49,999,999,937 Farey epochs** through `N=100,000,000,000`, without enumerating them.

The standalone Python integer verifier `VERIFY_NEAR_RATIONAL.py` uses an exact integer square-root bound to obtain a rigorous rational enclosure for theta_*. It enumerates and verifies every epoch for N=1,000, 20,000, 100,000 (respectively 437, 9,937, 49,937 epochs), and separately checks representative Farey neighbours plus the proved formula at N=10^11. Full 10^11 epoch enumeration was neither necessary nor performed.

## Algorithmic consequence

The R15 S23/AV trillion-step algorithm is output-sensitive to its actual Farey-epoch sequence and delivers 78 epochs for the frozen S23/AV theta. Near-rational slopes may create almost one Farey-epoch transition per two integer horizons over a very long finite range. A more uniform algorithm should compress Farey-epoch runs via continued-fraction partial-quotient or event-level grouping rather than paying one pass per epoch. Evaluate this against true risk-change block counts and full rational-bit costs, preserving historical arc provenance and the precise Bayes-risk observable.

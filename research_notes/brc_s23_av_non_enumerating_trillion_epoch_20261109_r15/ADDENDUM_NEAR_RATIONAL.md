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

Thus no order-H Farey fraction lies in the open interval `(1/2,theta)`: the lower neighbour is 1/2 itself. The candidate fraction `(q_H+1)/(2q_H)` is reduced, and its determinant with `1/2` is `2*(q_H+1)/2-q_H=1`. Moreover the denominators satisfy `2+q_H>H` (since q_H is H or H-1). The elementary Farey adjacency criterion (determinant one and denominator sum above H) therefore proves that the two fractions are consecutive in the order-H Farey sequence. Equivalently, any intermediate reduced fraction would have denominator at least `2+q_H>H`. The same strict bound ensures theta lies strictly beneath it.

As H ranges from m-1 to N-1, q_H changes exactly once for every two increments of H and assumes every successive odd integer from q_0 through q_N. The claimed exact epoch count follows. QED.

## One fixed irrational input with a large exact finite window

Set `theta_* = 1/2+sqrt(2)/10^12`. This one fixed irrational number satisfies `0<theta_*-1/2<1/(2N)` for every integer `N<=10^11`, since `sqrt(2)<5`.

With m=128, the theorem yields exactly **49,999,999,937 Farey epochs** through `N=100,000,000,000`, without enumerating them.

The standalone Python integer verifier `VERIFY_NEAR_RATIONAL.py` uses an exact integer square-root bound to obtain a rigorous rational enclosure for theta_*. It enumerates and verifies every epoch for N=1,000, 20,000, 100,000 (respectively 437, 9,937, 49,937 epochs), and separately checks representative Farey neighbours plus the proved formula at N=10^11. Full 10^11 epoch enumeration was neither necessary nor performed.

## Algorithmic consequence

The R15 S23/AV trillion-step algorithm is output-sensitive to its actual Farey-epoch sequence and delivers 78 epochs for the frozen S23/AV theta. Near-rational slopes may create almost one Farey-epoch transition per two integer horizons over a very long finite range. A more uniform algorithm should compress Farey-epoch runs via continued-fraction partial-quotient or event-level grouping rather than paying one pass per epoch. Evaluate this against true risk-change block counts and full rational-bit costs, preserving historical arc provenance and the precise Bayes-risk observable.

## Exact risk law: billions of singleton risk blocks admit a one-line compression

**Second theorem (a fixed near-half-integer irrational window).** Let `m>=4` be even, `N>=m`, and `theta=1/2+epsilon` irrational with `0<epsilon<1/(2(N+1))`. The optimal uniform-phase whole-future prediction error for the labelled historical-arc observer, as defined in `PROOF.md`, is **exactly**

`R_theta(m,L)=2 epsilon L=(2 theta-1)L` for **every integer** `0<=L<=N-m`.

Consequently, every consecutive integer horizon produces a strict risk increase `2 epsilon`, so the number of maximal constant-risk blocks over `0<=L<=N-m` is precisely `N-m+1`. All those distinct blocks admit a *single* affine arithmetic-progression representation `(L, (2 theta-1)L)`.

**Proof.** Since `i epsilon<1/2` for `0<=i<N`, the phase cuts split by parity into two strictly ordered clusters:

`t_{2j}=2j epsilon`, and `t_{2j+1}=1/2+(2j+1)epsilon`.

For the first m historical cuts, all but two consecutive-circle arcs are the small gaps of length `2 epsilon`. The two larger historical arcs are `I_E: t_{m-2} -> t_1`, length `1/2-(m-3)epsilon`, and `I_O: t_{m-1} -> t_0` wrapping clockwise, length `1/2-(m-1)epsilon`. There are precisely `m-2` small historical arcs, unaffected by all later cuts.

As `n=m+L` grows, every additional even-index cut lies in `I_E`, immediately after the previous largest even cut; every additional odd-index cut lies in `I_O`, immediately after the previous largest odd cut. Each new cut separates a gap of length `2 epsilon` from the current large gap and shortens that large gap by precisely `2 epsilon`. Across all n<=N, each surviving large gap is greater than `2 epsilon`, because its length is at least `1/2-(N-1)epsilon>2 epsilon` under the stated hypothesis. Thus the maximum remaining subgap in the affected historical arc drops by exactly `2 epsilon` at every step; the maxima of all other historical arcs are unchanged. The risk `1-sum_I M(I;n)` starts at zero when `L=0`, and increases by `2 epsilon` at each of the L future cuts. Therefore the exact formula holds for every stated L. QED.

**Certified fixed-irrational example.** With `theta_*=1/2+sqrt(2)/10^12`, `m=128`, `N=10^11`, the stronger hypothesis `sqrt(2)/10^12<1/(2(N+1))` holds. Hence throughout the *same fixed* input window:

- `E_theta(128,10^11)=49,999,999,937` Farey epochs;
- `B_theta(128,10^11)=99,999,999,873` distinct maximal constant-risk blocks;
- `R_theta(128,L)=2 sqrt(2)L/10^12` for all `0<=L<=99,999,999,872`;
- one symbolic arithmetic progression describes all B risk values without listing any of those billions of singleton blocks.

The independent exact `VERIFY_NEAR_RATIONAL_RISK.py` directly sorts all circular cuts and evaluates every historical arc maximum at ten selected horizons up to n=2000, for both rational endpoints of a rigorously certified interval around theta_*. All twenty exact equalities matched the theorem. The finite test supports the algebraic proof; N=10^11 was treated symbolically, without billion-step enumeration.

This contrasts with frozen S23/AV theta, where the exact trillion-step partition has only 9,698 maximal constant blocks: neither the Farey epoch count nor the raw block count alone is a uniform measure of the shortest *symbolic* risk description. Next work: identify provable affine runs and compressed event templates in the Farey epoch generator, with accurate worst-case output/bit accounting.

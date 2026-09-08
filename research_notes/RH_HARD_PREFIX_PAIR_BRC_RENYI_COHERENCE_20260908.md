# RH hard-prefix Pair-BRC Renyi coherence hierarchy

Status: `RESEARCH FRONTIER / EXACT REFORMULATION / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Mertens / hard-prefix Pair-BRC / collision coherence / Renyi moments / self-correlation`

## 0. Purpose

This note fuses three previously separate objects:

1. the hard-prefix Mertens criterion;
2. the positive Pair-BRC parity/collision histogram;
3. the growing-order cumulative-flux moment hierarchy.

The result is a hard-cut analogue of the Riesz Pair-BRC collision criterion, together with a Renyi ladder that interpolates between averaged collision coherence and RH-strength pointwise coherence.

---

## 1. Hard-prefix positive Pair-BRC histogram

For squarefree integers `m,n<=t`, let `S_m,S_n` be their prime-support sets and

`r=|S_m triangle S_n|`.

Define the positive histogram

`H_{t,r}=sum_{m,n<=t, |S_m triangle S_n|=r} mu(m)^2 mu(n)^2`

and its polynomial

`H_t(z)=sum_{r>=0}H_{t,r}z^r`.

Let

`Q(t)=sum_{n<=t}mu(n)^2`.

Then exactly:

`H_t(1)=Q(t)^2`,

`H_t(0)=Q(t)`,

because distance zero means the squarefree prime supports are identical and hence `m=n`, and

`H_t(-1)=M(t)^2`,

because

`(-1)^|S_m triangle S_n|=mu(m)mu(n)`

for squarefree m,n.

Freeze:

`HARD_PREFIX_PAIR_BRC: TOTAL=Q^2, COLLISION=Q, PARITY=M^2`.

---

## 2. Hard-prefix collision coherence is exactly RH strength

Define

`Gamma(t)=H_t(-1)/H_t(0)=M(t)^2/Q(t) >=0`.

The classical squarefree count gives

`Q(t)=(6/pi^2)t+O(sqrt(t))`.

Therefore

`RH <=> Gamma(t)=t^o(1)`.

Equivalently, for every eps>0,

`H_t(-1) <= t^eps H_t(0)`

(up to epsilon renaming).

This is the hard-prefix counterpart of the previously derived Riesz shell criterion

`H_x(-1) <= x^eps H_x(0)`.

The common semantics is:

`SIGNED PARITY OUTPUT <= SUBPOLYNOMIAL * EXACT POSITIVE COLLISION`.

---

## 3. Exact relation to Mobius self-feedback correlation

The discrete identity

`M(n)^2-M(n-1)^2=2mu(n)M(n-1)+mu(n)^2`

sums to

`M(t)^2=Q(t)+2 sum_{n<=t}mu(n)M(n-1)`.

Hence

`sum_{n<=t}mu(n)M(n-1)`
`=[H_t(-1)-H_t(0)]/2`.

Thus the hard self-correlation of Mobius against its own cumulative state is exactly the off-diagonal parity defect relative to Pair-BRC collision.

Freeze:

`MOBIUS_SELF_FEEDBACK = (PAIR_PARITY - COLLISION)/2`.

A 2026 paper by Gordon Vincent Chavez studies logarithmically weighted correlations of `mu(n)` with `M(n-1)` and obtains formulas under RH plus simplicity assumptions. This is prior art adjacent to the self-feedback language, but it does not supply the unconditional hard-cut estimate required here.

---

## 4. Renyi coherence on dyadic scale

For `q>=1`, define

`R_q(X)= [ (1/X) sum_{X<t<=2X} Gamma(t)^q ]^(1/q)`.

Since `Q(t) asymp X` uniformly for `X<t<=2X`,

`R_q(X)^(1/2)`

is equivalent up to absolute constants to the normalized `2q`-moment

`[ (1/X)sum_{X<t<=2X}|M(t)|^(2q) ]^(1/(2q)) / sqrt(X)`.

Therefore the cumulative-flux moment-to-sup inequality implies:

If for fixed q

`R_q(X)<=X^o(1)`,

then

`max_{X<t<=2X}|M(t)| <= X^[(q+1)/(2q+1)+o(1)]`.

Examples:

- q=1 -> exponent 2/3;
- q=2 -> exponent 3/5;
- q=3 -> exponent 4/7;
- q->infinity -> exponent 1/2.

---

## 5. Growing-Renyi RH criterion

Let `q(X)->infinity` arbitrarily slowly. Then

`RH`

is equivalent to the existence of such a q(X) with

`R_{q(X)}(X)=X^o(1)`

for dyadic X.

Proof:

- RH gives `Gamma(t)=t^o(1)` pointwise, hence every Renyi average is subpolynomial.
- Conversely `R_q=X^o(1)` gives the square-root normalized cumulative-flux `2q` moment at scale `X^o(1)`. The 1-Lipschitz property of M converts this to pointwise exponent

`1/2+1/(4q+2)+o(1)`,

which tends to `1/2` as q(X)->infinity.

Freeze:

`RH = GROWING_RENYI_HARD_PAIR_COLLISION_COHERENCE`.

This is an RH-equivalent reformulation, not a proof.

---

## 6. Positive final observer and replica typing

Every `Gamma(t)^q` is nonnegative. For integer q the numerator is

`M(t)^(2q)=H_t(-1)^q`.

Thus the final Renyi readout is positive even though the parity endpoint `z=-1` internally uses the signed Mobius character.

The q in this hierarchy is a **replica/moment order**. It is not:

- X6 spatial dimension;
- factor-provenance depth;
- number of native force directions.

The current branch therefore has three separate scales:

`X6 width = 6 fixed`,

`factor provenance depth ~ log N/loglog N (depending on observer)`,

`Renyi replica order q -> infinity arbitrarily slowly`.

---

## 7. First serious weaker target

The q=1 statement

`(1/X)sum_{X<t<=2X} Gamma(t) <= X^o(1)`

is equivalent, up to `Q(t)asymp X`, to

`sum_{X<t<=2X}M(t)^2 <= X^(2+o(1))`.

By the moment-to-sup inequality this would imply

`M(X)<=X^(2/3+o(1))`.

This is already a genuine fixed-power improvement over current unconditional Mertens bounds. It should therefore be treated as a major theorem target, not as an easy averaging step.

---

## 8. Short-interval boundary

Current almost-all short-interval Mobius estimates control increments

`Delta_H M(x)=M(x+H)-M(x)`

with logarithmic or qualitative savings over H. Such estimates are invariant under adding a constant to M and hence do not directly control the zero-frequency/global cumulative level.

Deterministically chaining `X/H` bounds of size `H/log^c X` only produces `X/log^c X`, not a fixed power.

Therefore

`SHORT_INTERVAL_LOCAL_UNIFORMITY != q=1 PAIR-RENYI COHERENCE`.

A successful transfer would require new cancellation among the block drifts themselves or an equivalent low-frequency theorem.

---

## 9. Prior-art boundary

- The Mertens RH criterion is classical.
- Verjovsky 2026 (arXiv:2607.25002) gives an analogous high-local-moment RH criterion for normalized Mobius Fourier polynomials.
- Chavez 2026 studies logarithmically weighted correlations between Mobius and its partial sums under additional hypotheses.
- The present contribution is the project-internal organization of hard-prefix Pair-BRC collision coherence, its exact self-feedback identity, and its fusion with the cumulative-flux Renyi ladder.

No historical novelty is asserted without a broader literature audit.

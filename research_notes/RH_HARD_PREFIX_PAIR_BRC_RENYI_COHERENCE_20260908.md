# RH hard-prefix Pair-BRC collision coherence and fixed-Renyi hierarchy — Mellin-corrected

Status: `RESEARCH FRONTIER / EXACT RH-EQUIVALENT FAMILY / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Mertens / hard-prefix Pair-BRC / collision coherence / fixed Renyi moments / self-correlation`

## 0. Correction

An earlier version stated that one had to let the Renyi order `q->infinity` to recover RH from dyadic averaged collision coherence. That conclusion used only the generic 1-Lipschitz moment-to-sup inequality.

After Mellin audit, the correct statement is stronger:

**any one fixed `q>=1` at the natural all-scale subpolynomial collision-coherence bound is already RH-equivalent.**

Growing q remains a valid concentration hierarchy but is not necessary for RH equivalence.

---

## 1. Hard-prefix positive Pair-BRC histogram

For squarefree integers `m,n<=t`, let `S_m,S_n` be their prime-support sets and

`r=|S_m triangle S_n|`.

Define

`H_{t,r}=sum_{m,n<=t, |S_m triangle S_n|=r}mu(m)^2mu(n)^2`

and

`H_t(z)=sum_rH_{t,r}z^r`.

Let

`Q(t)=sum_{n<=t}mu(n)^2`.

Then exactly

`H_t(1)=Q(t)^2`,

`H_t(0)=Q(t)`,

`H_t(-1)=M(t)^2`.

Reason for the last identity:

`(-1)^|S_m triangle S_n|=mu(m)mu(n)`

on squarefree cells.

Freeze:

`HARD_PREFIX_PAIR_BRC: TOTAL=Q^2, COLLISION=Q, PARITY=M^2`.

---

## 2. Pointwise collision coherence is the classical RH criterion

Define

`Gamma(t)=H_t(-1)/H_t(0)=M(t)^2/Q(t)>=0`.

Since

`Q(t)=(6/pi^2)t+O(sqrt t)`,

we have

`RH <=> Gamma(t)=t^o(1)`.

Equivalently, for every epsilon,

`H_t(-1)<=t^eps H_t(0)`

(up to epsilon renaming).

This is the hard-prefix analogue of the Riesz Pair-BRC collision-coherence criterion.

---

## 3. Exact self-feedback identity

The discrete identity

`M(n)^2-M(n-1)^2=2mu(n)M(n-1)+mu(n)^2`

sums to

`M(t)^2=Q(t)+2sum_{n<=t}mu(n)M(n-1)`.

Therefore

`sum_{n<=t}mu(n)M(n-1)`
`=[H_t(-1)-H_t(0)]/2`.

So the hard Mobius self-feedback correlation is exactly the off-diagonal parity defect relative to positive collision.

A 2026 paper by Gordon Vincent Chavez studies logarithmically weighted correlations of `mu(n)` with `M(n-1)` under RH plus simplicity assumptions. It is prior art adjacent to this self-feedback formulation but does not give the unconditional hard-cut estimate.

---

## 4. Fixed-q dyadic Renyi coherence

For fixed `q>=1`, define

`R_q(X)=[(1/X)sum_{X<t<=2X}Gamma(t)^q]^(1/q)`.

Since `Q(t)asymp X` uniformly on the dyadic interval,

`R_q(X)^(1/2)`

is equivalent up to absolute constants to

`[(1/X)sum_{X<t<=2X}|M(t)|^(2q)]^(1/(2q))/sqrt(X)`.

Hence the natural fixed-q collision-coherence bound

`R_q(X)<=X^o(1)`

is exactly the natural square-root `L^(2q)` flux bound on that dyadic scale.

---

## 5. Any fixed q natural Renyi bound is RH-equivalent

Assume for one fixed `q>=1` and every epsilon that

`R_q(X)<<_eps X^eps`

on all large dyadic X.

Then, because `Q(t)asymp X`,

`sum_{X<t<=2X}|M(t)|^(2q)`
`<<_eps X^(q+1+eps)`

(after harmless epsilon renaming).

The fixed-p Mellin argument with `p=2q` gives absolute convergence of

`int_1^infinity M(t)t^(-s-1)dt`

for every `Re(s)>1/2`. Hence `1/zeta(s)` is holomorphic there and RH follows.

Conversely RH gives pointwise `Gamma(t)=t^o(1)`, hence every fixed-q Renyi average is subpolynomial.

Therefore for every fixed `q>=1`,

`RH <=> R_q(X)=X^o(1)`

in the all-scale epsilon-family sense.

In particular, **q=1 already suffices**:

`RH <=> (1/X)sum_{X<t<=2X}Gamma(t) = X^o(1)`.

Since `Q(t)asymp X`, this is equivalent to

`sum_{X<t<=2X}M(t)^2 <= X^(2+o(1))`.

Freeze:

`FIXED_RENYI_PAIR_COHERENCE_AT_NATURAL_SCALE = RH_EQUIVALENT`.

---

## 6. Generic pointwise ladder remains a valid but weaker statement

If one deliberately ignores the Mellin/Dirichlet identity and uses only that M is 1-Lipschitz, then the same fixed-q moment bound yields

`max|M(t)| <= X^[(q+1)/(2q+1)+o(1)]`.

Examples:

- q=1 -> 2/3;
- q=2 -> 3/5;
- q=3 -> 4/7.

These are correct **generic metric consequences**, not the full Möbius arithmetic consequence.

There is no contradiction: the RH implication from fixed q uses all scales plus the exact Mellin identity.

---

## 7. Positive final observer

Every `Gamma(t)^q` is nonnegative. Thus q=1 already gives a fully positive final averaged observer:

`average_t [PAIR_PARITY/COLLISION]`.

The internal evaluation `H_t(-1)` uses Möbius parity, but after squaring it is positive.

This is a particularly small positive RH carrier:

`q=1 HARD-PREFIX PAIR-BRC AVERAGED COLLISION COHERENCE`.

---

## 8. Relation to Weak Mertens

A stronger uniform estimate

`sum_{t<=X}M(t)^2=O(X^2)`

implies by dyadic decomposition

`int_1^X(M(t)/t)^2dt=O(log X)`,

the classical Weak Mertens Conjecture. WMC is known to imply RH and stronger conclusions such as simplicity of zeros and convergence of a negative-zero-moment sum.

The present criterion permits `X^o(1)` slack and is used only as an RH equivalence; it should not be conflated with WMC.

---

## 9. Short-interval boundary

Current short-interval Mobius results control increments

`Delta_H M(x)=M(x+H)-M(x)`

with logarithmic or qualitative savings over H. Deterministic chaining still gives only log-scale global savings, and these local estimates do not directly provide the fixed-q natural collision-coherence bound.

A transfer to q=1 would already be RH-strength by the Mellin argument. Therefore any such claimed transfer must be audited as a potential RH proof, not a weak averaging lemma.

Freeze:

`SHORT_INTERVAL_LOCAL_UNIFORMITY -> q=1 NATURAL PAIR-RENYI` is an RH-strength missing bridge.

---

## 10. Prior-art boundary

- Mertens and Weak Mertens criteria are classical.
- Verjovsky 2026 gives related Fourier/Laplace moment RH criteria.
- Chavez 2026 studies logarithmically weighted Mobius/partial-sum correlations under additional hypotheses.
- The project contribution here is the hard-prefix Pair-BRC collision organization and its exact fusion with the fixed-q positive flux moments.

No historical novelty is asserted without broader audit.

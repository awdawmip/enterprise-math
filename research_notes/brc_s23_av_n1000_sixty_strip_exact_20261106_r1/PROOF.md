# S23 conditional AV: sixty disjoint two-count strips yield a sharper n=1000 bound

Date: 2026-11-06. Status: **AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Scientific source is frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`; current normative rules are separate. This extends the twenty-strip exact proof at `7679c282fb7466ee22bfa1c1a621d8ac0dae653c`. The result is **only for the conditional tagged AV statistical submodel**, not an unconditional theorem on the ten-label S23 mother game.

## Statement and model

For `a,c in [1/2,7/8]`, let `z=(1-a)c`, `P_(a,c)=(a,z,1-a-z)` on the labelled events (stop1,stop3,stop4), and compressed observer `B_(a,c)=(z,1-z)`. Given a shared unknown (a,c), the 1000 observations are conditionally IID. Define the total-variation minimax reconstruction error

`delta_1000 = inf_K sup_(a,c) TV(P_(a,c)^{⊗1000}, B_(a,c)^{⊗1000} K)`,

where K may be any parameter-independent stochastic kernel from binary observation strings to complete tagged outcome strings, including kernels with correlated output.

**Theorem (exact finite witness):** The rational number `R_60` defined below obeys

`delta_1000 >= R_60 = 0.808102201302498981591154228804603777081255123... > 8081/10000 = 0.8081`.

This improves `R_20=0.807079209717409305877823041742505418712304415...`, with precisely computed gain `R_60-R_20=0.00102299158508967571333118706209835836895070775...`. Decimal strings are displays of exact rational computations, not inputs.

## Six indistinguishable compressed observers

Fix `z=1/4` and six rational `q_j`, the stop4 probabilities:

`(1/28, 3217/50000, 10091/100000, 14447/100000, 9727/50000, 1/4)`.

For each j set `a_j=3/4-q_j` and `c_j=1/(1+4q_j)`. Exactly `(1-a_j)c_j=1/4`, and all `a_j,c_j` lie in `[1/2,7/8]`. Thus the binary observation law is the same for every j, and every fixed K returns the same reconstruction distribution Q for all six parameters, whereas their complete laws are `P_j=(3/4-q_j,1/4,q_j)`.

## Explicit classification certificate

For a full 1000-word, let `U=#stop4`, `S=#stop3`. The baseline partition `E_j^0` puts a word in class j by `U` in

`I_j: [0,48], [49,81], [82,121], [122,168], [169,221], [222,1000]`.

A reassignment tuple `(u,source,destination,lower,upper)` moves the entire strip `{U=u, lower<=S<=upper}` from source to destination. `VERIFY.py` contains the 20 predecessor moves `OLD_MOVES` and **40 additional disjoint** `NEW_MOVES`; each of all 60 has a different U. Hence these moves preserve a disjoint exhaustive six-class partition `E_j^{60}`.

For any `q=r/d` write `M(q,u,l,h)=Pr_q(U=u,l<=S<=h)`. The multinomial expansion gives the exact rational identity

`M(q,u,l,h)=C(1000,u)*(4r)^u/(4d)^1000 * sum_{s=l}^h C(1000-u,s)*d^s*(3d-4r)^(1000-u-s)`.

For fixed u,s the likelihood under j, after cancelling a factor common to all j, is

`L_j(u,s)=q_j^u*(3/4-q_j)^(1000-u-s)`.

For any two hypotheses and fixed u, their likelihood ratio is monotone in s. The verifier checks **strict destination > source likelihood at both endpoints** of every one of the 60 strips using exact rationals; this proves a strict gain at every lattice point in each moved strip. It also verifies that all source-U intervals, strip bounds and distinct-U constraints hold. The prior and added gain sums are exact:

`A0 = sum_j Pr_{q_j}(U in I_j)`
`G_old = sum_{OLD_MOVES}[M(q_destination,...)-M(q_source,...)]`
`G_new = sum_{NEW_MOVES}[M(q_destination,...)-M(q_source,...)]`
`R_60 = (A0+G_old+G_new-1)/6`.

For arbitrary common Q, `TV(P_j^{⊗1000},Q) >= P_j^{⊗1000}(E_j^{60})-Q(E_j^{60})`. Summing j, the six disjoint classes exhaust all words, so `sum_j Q(E_j^{60})=1`. Thus `6 max_j TV(P_j^{⊗1000},Q) >= A0+G_old+G_new-1`. Since every K yields one such Q, taking inf over K proves the stated universal lower bound.

## Computation, reproducibility, scope

`VERIFY.py` evaluates all 60 endpoint comparisons, each exact strip mass and the final inequality using only `math.comb`, integer powers and `fractions.Fraction`. Its observed successful local output is in `RUN_EVIDENCE.txt`. The 40 new regions were *discovered* by preliminary floating-point screening, but their acceptance and the theorem rely solely on subsequent exact rational tests; no floating-point computation is part of the certificate.

This is a finite but complete certificate for the 60 explicitly selected strips at n=1000, not a claim that these are globally optimal six-hypothesis maximum-likelihood regions, nor a proof about n other than 1000. Independence and official mathematical admission have not occurred. Connecting the conditional observer to `R_beh(k,10)`, k=4,6, requires a separate lawful encoding/decoding/observer map.

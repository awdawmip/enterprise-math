# S23/AV: first failure of the one-event likelihood witness at seven repeated trials

Date: 2026-11-07. Status: AUTHOR_SIDE_EXACT_DERIVATION, pending independent mathematical review. Frozen scientific inputs: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This is the auxiliary three-label/one-bit observation experiment, **not** the six-source/ten-label mother model.

## Exact model and theorem

The lawful parameter box is `a,c ∈ [1/2,7/8]`; in each of `n` conditionally independent trials the *same* unknown pair `(a,c)` is used. The full ordered trial law on labels `(1,3,4)` is `P_(a,c)=(a,(1-a)c,(1-a)(1-c))`; the binary observer retains only whether the label is `3` and has law `B_z=(z,1-z)`, `z=(1-a)c`. Any decoder `L_n` from the ordered binary observations to the ordered three-label outputs is fixed independently of `(a,c)`. Let

`δ_n = inf_(L_n) sup_(a,c lawful) TV(P_(a,c)^⊗n, B_z^⊗n L_n)`.

Consider two legal points `θ_0=(1/2,1/2)`, `θ_1=(5/7,7/8)`. Their full single-trial laws are respectively

`P_0=(1/2,1/4,1/4)`, `P_1=(5/7,1/4,1/28)`,

but **both** have identical binary observer law `B_(1/4)`. Write `D_n=TV(P_0^⊗n,P_1^⊗n)`. Then:

1. For every `n≥1`, `δ_n ≥ D_n/2`.
2. For each ordered word let `k=#1`, `r=#3`, `ℓ=#4`, `k+r+ℓ=n`. The optimal signed total-variation event for this two-point pair is exactly
   `A_n={7^(k+ℓ)>10^k}`; equality occurs for the all-3 word only. Consequently
   `D_n = Σ_(k+ℓ+r=n) [n!/(k!ℓ!r!)] · max(0, (1/2)^k(1/4)^(r+ℓ) - (5/7)^k(1/4)^r(1/28)^ℓ)`.
   This provides an **exact rational `O(n²)`-term** expression (bit complexity not asserted).
3. The coarser event `E_n={at least one label 4}` realizes the *entire* two-point total variation **if and only if** `1≤n≤6`. Specifically,
   `D_n=(27/28)^n-(3/4)^n` for `1≤n≤6`.
4. At the first failure, `n=7`, exactly seven ordered words (six labels 1 and one label 4, with no 3) lie on the opposite side of the likelihood-ratio test compared with `E_7`. The exact correction is
   `D_7-[(27/28)^7-(3/4)^7]=176457/30118144`.
   Therefore
   `D_7=4369158699/6746464256`, and `δ_7≥4369158699/13492928512 ≈ 0.32381100182323413`.
5. In particular the new four-trial lower bound is
   `δ_4≥5265/19208 ≈ 0.2741045397750937`,
   which exceeds the previously exact three-trial minimax value `δ_3=5211/21952` by the exact amount `5643/153664 ≈ 0.03672298000832986`.

These are lower bounds on the full lawful-parameter minimax problem for `n=4,7`; no exact `δ_4` or `δ_7` is claimed.

## Proof

The common binary observation law forces `B_(1/4)^⊗n L_n=Q_n` to be identical for the two parameter points for **every** parameter-independent stochastic decoder. The triangle inequality gives
`D_n≤TV(P_0^⊗n,Q_n)+TV(Q_n,P_1^⊗n)≤2 sup_θ TV(P_θ^⊗n,B_θ^⊗nL_n)`.
Take the infimum over `L_n` to obtain item 1.

For each ordered word,
`P_0(word)/P_1(word)=[(1/2)/(5/7)]^k·[(1/4)/(1/28)]^ℓ=(7/10)^k 7^ℓ=7^(k+ℓ)/10^k`.
All word probabilities are strictly positive. In a finite alphabet, total variation equals the sum of positive signed mass differences. Therefore the optimal event is exactly `A_n`, and grouping words by their integer counts yields the multinomial sum. `7^(k+ℓ)=10^k` has no positive `k+ℓ` solution because the left side is a power of seven and the right side is a power of ten; equality occurs only at `k=ℓ=0`.

If `ℓ=0,k>0`, the ratio is `(7/10)^k<1`. For `ℓ≥1` and `n≤6`, it is at least `7(7/10)^(n-1)≥7(7/10)^5=117649/100000>1`. Thus for those six sample sizes the full positive signed event is precisely `E_n`. Its probability difference is
`P_0(E_n)-P_1(E_n)=[1-(3/4)^n]-[1-(27/28)^n]`,
proving item 3.

For `n=7`, the only word type within `E_7` having likelihood ratio smaller than one is `(k,ℓ,r)=(6,1,0)`: for `ℓ=1,k≤5` the ratio is at least `7(7/10)^5>1`, and `ℓ≥2,k≤5` only increases it. For `(6,1,0)`, the ratio is `7(7/10)^6=823543/1000000<1`. There are exactly `7` such words. Correcting the signed event gives
`D_7=P_0(E_7)-P_1(E_7)+7[(5/7)^6(1/28)-(1/2)^6(1/4)]`.
Direct rational simplification yields the displayed correction, `D_7` and its minimax half-distance. For every `n≥7`, a word consisting of six labels 1, one label 4 and `n-7` labels 3 retains the same negative likelihood ratio while lying in `E_n`; this proves the “only if” direction for all larger `n`. The `n=4` formula and difference follow from item 3 by exact rational subtraction.

## Evidence, observer scope and open question

The author executed the companion `VERIFY.py` using only standard-library `fractions.Fraction`. It independently enumerated the full ordered `3^n` word alphabet and the multinomial histogram for each `n=1,…,7`, checked the first seven sign reversals, and verified the integer likelihood-ratio classifier for all `1≤n≤12`. Actual stdout is in `RUN_EVIDENCE.txt`. The theorem for **all** `n≥7` follows from the explicit rational word witness, not from finite enumeration.

BRC observer audit: `REUSE_APPLIED` to the retained ordered trial labels / signed two-point difference. The one-bit coarse event “any 4” exactly retains the relevant Neyman–Pearson sign partition through six trials for **this specific two-parameter binary discrimination**, but loses it at seven trials. This is neither a claim that the one-bit compressed source observer reconstructs the full law nor a native X6/Heartbeat dynamical claim. The `(k,ℓ,r)` joint-count carrier preserves the missing interaction for all `n`; do not erase the 1-versus-4 counts for continued trials.

Immediate next scientific unit: decide whether the `n=4` *full-lawful-box* minimax value equals the new lower bound `5265/19208` by a single parameter-independent random decoder with a provable global-real-parameter upper certificate, or produce a strictly larger finite-support dual witness. In parallel, continue the separately typed six-source/ten-label S23 mother-model bridge. Formal CLAIM/Owner/RA and independent review remain unconfirmed when native control is unavailable.

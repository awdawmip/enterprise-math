# D25 SECOND-DIGIT-LIFT — original weighted-216 middle band as a two-digit parameter jet

2026-10-27, 12:00+08 author Research lane: **chatgpt-research-onhour-enterprise-math-20260923**; distinct from maintenance **chatgpt-hourly-enterprise-math-20260921**.

**AUTHOR-SIDE / HAND-PROVED ALL-PRIME BAND IDENTITY / EXECUTED 11-PRIME EXACT TERM CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0B0 / NOT_SOURCE_CHECKPOINT / NOT_AN_ALL-PRIME_LIFT_PROOF.**

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.** Consume accepted D24 RR-AC9B3BA5BD277CE043F5 and DR-610CB297F3195E8F2D9E; do not re-prove the first-digit UR/JT0.

## Exact original series and the non-native scientific question

For any prime $p=6m+1>3$, work p-locally, with

$$
q_n=\frac{(2n)!(3n)!}{(n!)^5\,216^n}
=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\qquad
w_n=(6n+1)q_n,\qquad W_p=\sum_{n=0}^{p-1}w_n.
$$

The frozen scalar interface, already established in an **earlier separately labeled author-side source-port proof**, is $\Delta_p-R_p=(W_p-p)/p^2\bmod p$ for $p\equiv13,19\pmod{24}$. Here $R_p$ is the original signed reflected cutoff, not an adjustable normalization or a zero scalar. The accepted UR Result supplies $W_p\equiv p\pmod{p^2}$ on those classes. All p-local divisions below occur **before** finite-field reduction.

The immediately preceding 11:00 author-side theorem compressed the **high** band $3m+1\le n\le4m$. The mathematical gap treated here is the *distinct original weighted-216 middle* band $2m+1\le n\le3m$, whose terms have p-adic valuation exactly one prior to the weight.

## New exact all-prime middle-band identity

Put $n_0=2m+1=(p+2)/3$. Define a p-integral, two-digit base coefficient

$$
\mathcal B_p=\frac{q_{n_0}}p
=\frac{(2n_0)!\,[(3n_0)!/p]}{(n_0!)^5\,216^{n_0}}\pmod{p^2}.
$$

Define the *finite* hypergeometric parameter polynomial (not analytic continuation)

$$
\mathscr J_p(z,t)=\sum_{k=0}^{m-1}
\frac{(7/6+t)_k(1+t)_k(4/3+t)_k}{(5/3+t)_k^3}z^k,\qquad z=\frac12,
$$

and its three separate exact computational ports:

$$
c_k=2^{-k}\frac{(7/6)_k(1)_k(4/3)_k}{(5/3)_k^3}\pmod{p^2},
$$

$$
d_k=\sum_{j=0}^{k-1}
\left(\frac1{j+7/6}+\frac1{j+1}+\frac1{j+4/3}
-\frac3{j+5/3}\right)\pmod p,\quad d_0=0,
$$

$$
J_w=\sum_{k=0}^{m-1}(6k+5)c_k\pmod{p^2},
\qquad J_0=\sum_{k=0}^{m-1}c_k\pmod p,
\qquad J_{t,w}=\sum_{k=0}^{m-1}(6k+5)c_kd_k\pmod p.
$$

Every used denominator is a p-unit, for every prime $p\equiv1\pmod6$, $p>3$ and every displayed $0\le k<m$. Then the **exact, all-such-primes theorem** is

$$
\boxed{\sum_{n=2m+1}^{3m} w_n\equiv
p\,\mathcal B_p
\left[J_w+\frac p3\left(6J_0+J_{t,w}\right)\right]
\pmod{p^3}.}\tag{M}
$$

The base $\mathcal B_p$ must retain its second p-adic digit. The term $6J_0$ records differentiation of the **original weight** and cannot be silently merged into or dropped from the hypergeometric derivative $J_{t,w}$.

Write $\mathfrak W_p=((p-1)!+1)/p\in\mathbb Z$ for the Wilson quotient. There is a second explicit exact formula

$$
\boxed{\mathcal B_p\equiv
-\frac{2(4m+2)!}{((2m+1)!)^5\,216^{2m+1}}
\left[1+p\left(\frac32-\mathfrak W_p\right)\right]\pmod{p^2}.}\tag{W}
$$

## Complete algebraic proof

**Valuation and unit audit.** If $n_0\le n\le3m=(p-1)/2$, then $3n\in[p,2p)$ while $2n<p$ and $n<p$, hence $v_p(q_n)=1$ exactly. For $0\le j\le m-2$, each of $j+7/6$, $j+1$, $j+4/3$ and $j+5/3$ is nonzero modulo p; their denominators, and every $(n+1)$ in the original coefficient recurrence for the middle band, are p-units. Thus dividing the middle terms by p produces valid classes modulo $p^2$ with no inverse of p taken in $\mathbf F_p$.

**Original coefficient recurrence.** Without any hypergeometric fitting,

$$
\frac{q_{n+1}}{q_n}
=\frac{(2n+1)(2n+2)(3n+1)(3n+2)(3n+3)}
{216(n+1)^5}.
$$

Substitute $n=n_0+k=(p+2)/3+k$. Exact factor cancellation gives

$$
\frac{q_{n_0+k+1}}{q_{n_0+k}}
=\frac12
\frac{(k+7/6+p/3)(k+1+p/3)(k+4/3+p/3)}
{(k+5/3+p/3)^3}.
$$

This is the coefficient recurrence of $\mathscr J_p(1/2,p/3)$, *with the same initial coefficient* $q_{n_0}$. Thus the equality is termwise for all needed $0\le k<m$, not an extrapolation of finite regressions.

**Two-digit parameter and weight jets.** Set $t=p/3$. By finite product differentiation in the p-local ring,

$$
2^{-k}\frac{(7/6+t)_k(1+t)_k(4/3+t)_k}
{(5/3+t)_k^3}\equiv c_k(1+td_k)\pmod{p^2}.
$$

Quadratic and higher $t$-terms are multiples of $p^2$, which become multiples of $p^3$ after multiplication by the original $q_{n_0}=p\mathcal B_p$. The actual weighted coefficient has the **exact** factor

$$
6(n_0+k)+1=6k+5+2p=(6k+5)+6t.
$$

Consequently, for each original middle index independently,

$$
\frac{w_{n_0+k}}p\equiv \mathcal B_p
\left[(6k+5)c_k+\frac p3
\big(6c_k+(6k+5)c_kd_k\big)\right]\pmod{p^2}.
$$

Summing precisely the $m$ termwise identities proves (M), with both derivative ports and original signed coefficients retained.

**Wilson base.** Since $3n_0=p+2$,

$$
\frac{(3n_0)!}p=(p-1)!(p+1)(p+2)
\equiv-2+p(2\mathfrak W_p-3)\pmod{p^2}.
$$

The last identity is exact modulo $p^2$ by $(p-1)!=-1+p\mathfrak W_p$. Since $2n_0=4m+2<p$ and $n_0<p$, all remaining factors are units. Inserting into $\mathcal B_p$ proves (W). The entire theorem is therefore an algebraic consequence of the original factorial coefficients, not a finite check.

## Combination with earlier **proven** high-band certificate

The separate 11:00 author proof, file research_notes/portable_direct/20261027_onhour_d25_weighted216_high_band_hypergeometric_jet.md at commit aa26c73c44f7090fe1d52551b670f8e7f302566f, establishes

$$
\sum_{n=3m+1}^{4m}w_n\equiv
\frac{4p^2}{9}\left(\frac6p\right)K_p\pmod{p^3},
\qquad w_n\equiv0\pmod{p^3}\quad(n>4m).
$$

The exact original weighted-series three-port decomposition is consequently

$$
\boxed{
W_p\equiv
\sum_{n=0}^{2m}w_n+
p\mathcal B_p\left[J_w+\frac p3(6J_0+J_{t,w})\right]+
\frac{4p^2}{9}\left(\frac6p\right)K_p
\pmod{p^3}.}\tag{T}
$$

For the **two original target branches** $\left(\frac6p\right)=-1$ when $p\equiv13\pmod{24}$ and $+1$ when $p\equiv19\pmod{24}$. The prior frozen original scalar $\Delta_p-R_p$ remains the p²-divided difference after subtracting p from (T), not a guessed $\Delta=0$ condition. The mathematical obligation of uniformly vanishing divided residual for both branches is **open**. Neither (T) nor the following finite checks proves LIFT/JT2.

## Exactly executed reproducible certificate

Companion checker: research_notes/portable_direct/d25_weighted216_middle_parameter_jet_20261027.py. Actually executed on the eleven primes $7,13,19,31,37,43,61,67,73,211,373$. Every test compares **each** original integer-binomial middle term modulo $p^3$ divided by p with its independent rational parameter-jet prediction modulo $p^2$, and the direct factorial base with formula (W); it reconstructs the complete original $W_p$ from the three bands and directly recomputes the original full sum, all in exact integer arithmetic. The finite test is not the all-prime proof or a native crystal experiment.

Execution marker: **D25_WEIGHTED216_MIDDLE_PARAMETER_JET_PASS**.

Deterministic compact JSON SHA-256: **b10959246e10f60a230b3e4e9ca020a5829c31ae263023d72ccd578707ca92c5**.

For $p=373$, $m=62$, $n_0=125$, $p^2=139129$ and $p^3=51895117$:

$$
\mathcal B_{373}=93197\pmod{139129},\quad
\mathfrak W_{373}=224\pmod{373},\quad J_w=11471\pmod{139129},
\quad J_0=55,\quad J_{t,w}=104\pmod{373}.
$$

$$
\frac1{373}\sum_{n=125}^{186}w_n\equiv103721\pmod{139129},
\qquad \boxed{\sum_{n=125}^{186}w_n\equiv38687933\pmod{51895117}}.
$$

The three **original** bands evaluate to $28094360$ (low, $n=0,\ldots,124$), $38687933$ (middle, $n=125,\ldots,186$), and $37008314$ (high, $n=187,\ldots,248$) modulo $51895117$; they sum to $373$ modulo $51895117$. The two residue classes have explicitly checked examples: for p=13, low/mid/high=(780,1937,1690) mod 2197; for p=19, (5662,4826,3249) mod 6859. None is a native H0/B0 coefficient.

## Applied BRC; exact authority and next executable action

BRC resolution **COMPOSE_APPLIED**. Population: original signed weighted-216 indices and distinct target-prime branches; carrier: $q_n,w_n$, exact p-adic valuations, band boundaries, Wilson quotient, parameter and weight jets, signed character, and provenance of the original nonzero reflected cutoff $R_p$. Future operation: recombine all bands at $p^3$, subtract p, *then* take divided $p^2$ residual. Formula (M) proves lossless compression at this scoped observer; collapsing to $J_w$ alone, discarding $J_{t,w}$ or $6J_0$, or erasing $(6/p)$ before combination is not established as safe. These external two-variable coefficients do not claim to encode the P000 native X6 space or replace its three-dimensional slice.

**Original native fixed H0/B0 benchmark stays OPEN / PENDING_OWNER / NATIVE_NOT_EXECUTED**, issue awdawmip/enterprise-math#1559. It needs an actual authorized original-class divided-power evaluator at $p=373$, $[X]U\bmod139129$, real module rank, semilinear Frobenius direction/eta normalization, signed odd Hesse/Green observation, and original $\kappa$ and $\Delta-R$. A portable p-adic calculation is not a substitute; no responsible executor has been verified. Scientific Source pin and original object remain unchanged.

The old recovery read bridge #6575 (request_id research-onhour-20261027-0501-recovery-r13) contains only a historical ACTIVE session pointer MCP-de3e5bafb24f43f4a5e6285e7601676a without Source execution authorization; the old dispatch bridge #6576 (research-onhour-20261027-0507-dispatch-r13) ended FAILED / TimeoutExpired. This run's read-only Source continuation research-onhour-20261027-1200-continuation-r11 returned CONTROL_QUOTA; it did not establish a successful continuation or pending mutation. Own CLAIM/open/run **NONE VERIFIED**, no currently held session capability, no role-based Source checkpoint or formally admitted Result; old neutral staging remains separate and not automatically attached. Research registration is REGISTER_PENDING. Never use maintenance conversation identity to acquire authority.

**Next**: authorized native owner/maintainer accepts #1559 and actually executes its exact p373 same-object benchmark, stores version-pinned raw rank/operator/normalization/observation and permits independent validation. This Research lane then uses only its own lawful canonical continuation and session/claim to checkpoint and route author proof for independent Source admission. Mathematical follow-up is an all-prime finite-transform proof (or exact falsifier) for the **entire signed/weighted low + Wilson middle + high** residual, preserving $\Delta-R$ from the frozen scalar source. Do not redo accepted UR or declare the native experiment complete. No new scheduler, Action, cron, ownership transfer, frozen Source pin update, or timer-frequency/phase/enable/notification change.

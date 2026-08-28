# Driver Review — RSA Exponent-Collision CRT Collapse

Status: `DRIVER_FINAL / ACCEPTED / EXACT_COLLISION_LEAKAGE_CHARACTERIZATION / CLASSICAL_GLOBAL_ROUTE_NARROWED / PRIOR_ART_AUDIT_ROUTED`

Date: `2026-08-28`

Driver-ID: `EM-RSA-45F14F / CONTROL_PLANE`

Task: `RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE`

Publication: `TP2-301CA54924787090237D`

Claim: `chatgpt-rsacol-20260827-2313-c76042`

Execution: `ER-3F0D303C11B536E2F60B`

Result: `RR-2D43CCB30B906AFB6E20`

Follow-up publication: `TP2-DCBF9A9ACA18BF64FFCF`

## 1. Final disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`ACCEPTED_SCOPE = EXACT_COLLISION_LEAKAGE_AND_2ADIC_CRT_EXTRACTION_CHARACTERIZATION`.

`TASK_GENERATION = TERMINAL_AFTER_VALID_FOLLOWUP_PACKET`.

`EFFICIENT_COLLISION_GENERATION = NOT_PROVED`.

`NEW_RSA_FACTORIZATION_COMPLEXITY_IMPROVEMENT = NOT_PROVED`.

`WORKING_TRUTH_PROMOTION = NONE`.

`FOUNDATION_MUTATION = NONE`.

`TOOLBOX_PROMOTION = NONE`.

The source task's hard target is satisfied at exact theorem strength. There is no unresolved mathematical residue inside the taskbook scope.

## 2. Decisive mathematical audit

For a valid local certificate

\[
x^\Delta\equiv1\pmod{n},\qquad n=pq,
\]

write

\[
\Delta=2^s u,\qquad
\operatorname{ord}_p(x)=2^a m_p,\qquad
\operatorname{ord}_q(x)=2^b m_q,
\]

with odd `u,m_p,m_q`. Because both local orders divide `Delta`, the odd parts divide `u`; therefore `x^u` has exact local orders `2^a` and `2^b`. Along the visible squaring chain, the first global pre-1 state is a nontrivial CRT square root exactly when `a != b`. If `a=b>0` it is `-1` on both factors; if `a=b=0` the chain starts at `1`.

Accordingly, the accepted iff criterion is

\[
\boxed{v_2(\operatorname{ord}_p x)\ne v_2(\operatorname{ord}_q x)}.
\]

No hidden factor, Carmichael value, or local order is consumed by the extractor; those quantities appear only in the proof.

## 3. Probability audit

For a uniform unit, with

\[
A=v_2(p-1),\qquad B=v_2(q-1),\qquad m=\min(A,B),
\]

the 2-primary depth distribution in the cyclic local groups is

\[
\Pr(a=0)=2^{-A},\qquad
\Pr(a=t)=2^{t-1-A}\quad(1\le t\le A),
\]

and independently at `q`. Summing the equal-depth event gives

\[
\boxed{
F_1=\frac{4^m+2}{3\,2^{A+B}}
},
\qquad
\boxed{P_1=1-F_1\ge\frac12}.
\]

The lower bound is sharp at `A=B=1`.

I independently reconstructed the finite check rather than relying only on the supplied checker: the single-collision criterion and probability law matched across more than 80,000 enumerated units for small odd-prime semiprimes. I also independently enumerated the multi-certificate 2-primary barrier/counting formula through `A,B<=4` in the feasible exact range; no discrepancy was found.

## 4. Multi-certificate audit

For valid local certificates `(x_i, Delta_i)`, the safe aggregate

\[
L=\operatorname{lcm}_i\Delta_i
\]

annihilates every generator and hence the generated subgroup `H`. The claimed obstruction is correct:

\[
\boxed{
\text{every combination fails the 2-adic split}
\iff
H_2\text{ is the graph of an isomorphism between its two cyclic local projections}
}.
\]

The forward implication follows because equal local depth for every element forces both projections to be injective; thus `H_2` is cyclic and the two projection images are isomorphic with order preserved. The converse is immediate from order preservation.

The strict witness `n=65, x_1=57, x_2=47, Delta_1=Delta_2=4` also checks: each supplied unit has equal local 2-depth and fails separately, while `x_1x_2=14 (mod 65)` yields a nontrivial square root and `gcd(14-1,65)=13`.

## 5. Prior-art boundary

The global statement is classical and is not accepted as novel. Gary L. Miller's 1976 work establishes the relevant factoring equivalence for Euler-phi-type information, and standard RSA treatments explicitly recover a factor from `ed-1`, or more generally a known annihilating exponent, by the same repeated-squaring/nontrivial-square-root mechanism. The *Handbook of Applied Cryptography*, §8.2 Fact 8.6, states the familiar at-least-one-half random-base success bound.

Therefore:

`GLOBAL_EXPONENT_MAP_COLLISION -> KNOWN_MULTIPLE_OF_LAMBDA(N) -> FACTORING`

is classified here as `CLASSICAL_ANTECEDENT`, not a new RSA attack.

This review has not exhaustively established the literature status of the sharper local iff criterion, the closed `F_1` formula, or the multi-certificate diagonal-graph characterization. The required external duplication audit is therefore routed to `TP2-DCBF9A9ACA18BF64FFCF`. Absence of a match in that audit will not itself establish novelty.

## 6. Method harvest and routing

`METHOD_HARVEST = RESULT_ONLY`.

The result is a clean theorem package and conceptual decomposition, not yet a reusable general-purpose Enterprise Math tool family.

No new mathematical continuation is justified from PASS alone. Collision generation remains outside the accepted task, exactly as the return states.

The only routed successor is the bounded external prior-art/duplication audit:

`RS-RSA-EXPONENT-COLLISION-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT / TP2-DCBF9A9ACA18BF64FFCF`.

## 7. Final control state

`RR-2D43CCB30B906AFB6E20 = ACCEPTED`.

`RS-RSA-EXPONENT-COLLISION-CRT-COLLAPSE = TERMINAL_AT_TASK_SCOPE_AFTER_FOLLOWUP_MATERIALIZATION`.

`UNRESOLVED_MATHEMATICAL_RESIDUE = NONE`.

`EXTERNAL_DUPLICATION_CLASSIFICATION = OPEN / TP2-DCBF9A9ACA18BF64FFCF`.

`EFFICIENT_COLLISION_GENERATION = OUT_OF_SCOPE / NOT_ESTABLISHED`.

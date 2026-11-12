# X6 LP026 — signed relative Laurent BRC, weighted fibers, and executable consumer contract

Date: 2026-11-12. Scope: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Scientific state: **AUTHOR-PROVED / EXACT LOCAL PROBE / NONBLIND / UNREVIEWED / NOT_ADMITTED**. This is portable Source evidence; no winning X6 native CLAIM/open has been established. No changes to frozen scientific inputs, canonical task publication, or accepted Result.

Frozen scientific X6 pin: `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Historical comparison pin: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Use a chosen signed native Cell-anchor chart `z in Z^6` and twelve unit signed primitive *coordinate steps* as prescribed by P000. The relative/min-zero observation is a quotient of endpoints and not itself an absolute native Cell address. Previous completed work includes LP019 signed histogram/depth fibers and LP026 relative median reachability; this note builds a **five-variable computational consumer interface** rather than repeating their proofs.

## 1. Exact Laurent coefficient theorem

Define the quotient homomorphism

```
q: Z^6 -> Z^5
q(z) = (z1-z6, z2-z6, z3-z6, z4-z6, z5-z6).
```

Its kernel is exactly `Z*(1,1,1,1,1,1)`; `q(z)` is in bijection with the ordered min-zero observer `a=can6(z)`, with `q(z)=(a1-a6,...,a5-a6)`.

Let `y=(y1,...,y5)`, `Y=prod(y_i)`. For arbitrary twelve exact rational signed step weights `p_i,m_i`, define

```
F_(p,m)(y) = sum_(i=1)^5 (p_i*y_i + m_i*y_i^(-1))
             + p_6*Y^(-1) + m_6*Y.
```

**Theorem (all N>=0, q in Z^5, and all declared rational weights):** the exact total weight of *ordered signed native primitive words* of length `N` whose terminal native displacement has relative observation `q` is

```
C_(p,m)(N,q) = [y_1^(q1) ... y_5^(q5)] F_(p,m)(y)^N.
```

In particular `p_i=m_i=1` gives the nonnegative integer signed relative BRC multiplicity `B_rel(N,a)` from the previous median-lift theorem. Its complete ordinary generating function is the five-variable Laurent series

```
sum_(N>=0) C_(p,m)(N,q) * t^N
    = [y^q] 1/(1-t*F_(p,m)(y)).
```

The rational-function identity is a formal power-series equality; it makes no convergence or floating-point claim.

**Proof:** A signed word letter `+e_i` maps under `q` to `+epsilon_i` for `i<=5`, and `+e_6` to `(-1,-1,-1,-1,-1)`; each reverse letter maps to the negative vector. Its weight times the corresponding Laurent monomial is one term of `F_(p,m)`. Multiplying `N` terms enumerates *ordered* `N`-letter words once each. Laurent exponents add exactly as quotient displacements do. Collecting coefficient `y^q` therefore sums precisely the words in that relative endpoint fiber, keeping their weight/multiplicity. Summing geometric series in the formal `t`-adic ring gives the generating function. QED.

This also supplies a transfer algorithm: initialize `C(0,0)=1`; each step sends a state `q` to twelve `q±epsilon_i` or `q±(1,...,1)` neighbors, with the corresponding rational weight. It stores five independent integers instead of all six native coordinates. `sum_q C(N,q)=(sum_i(p_i+m_i))^N` is an exact conservation/coverage certificate.

## 2. Typed comparison with the real executable consumer

Existing current Source `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` defines `relative_endpoint_multiplicity(length,residual)` explicitly as the **old six-positive-letter** relative observer. For `a=minzero`, it returns only the single positive histogram `k=(N-sum(a))/6` when `k` is an integer >=0. The function is **correct within its declared positive-only domain**. Its coexistence with the new signed Laurent interface is a necessary type distinction, not a reason to change its meaning.

The signed native `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` provides `endpoint_weight(N,z,wp,wm)` and `endpoint_multiplicity`. Summing those native endpoint fibers at `z=(q_1+h,...,q_5+h,h)`, with `-N<=h<=N`, is an independent exact comparison to the new Laurent recurrence. This is precisely the LP019-to-LP026 consumer bridge. The three-coordinate `src/enterprise_math/diagonal_quotient.py` is separately typed for an old derived triple quotient; it is not a full X6 adapter.

Concrete scope witnesses:

| Declared observer/type | N | Relative address a | Exact weight/count |
|---|---:|---|---:|
| Positive-only 6-step alphabet (legacy) | 6 | (0,0,0,0,0,0) | 720 |
| Full signed 12-step relative quotient | 6 | (0,0,0,0,0,0) | 21,360 |
| True native endpoint z=0, signed alphabet | 6 | native zero | 19,920 |
| Full signed relative quotient | 8 | (0,1,1,2,3,5) | 4,200 |
| Positive-only relative quotient | 8 | (0,1,1,2,3,5) | 0 |

Hence the signed relative-zero observer includes native endpoints `z=0,+1^6,-1^6` when `N=6`. Its total is `19,920+720+720=21,360`; counting only the true native zero is a different operation. For the displayed `a` at `N=8`, the median lifts from the previous unit contribute `3,360+840=4,200`. Each is an exact integer diagnostic with no new axiom.

For one weighted diagnostic take
`p=(1,1/2,2,1,3/2,2)` and `m=(1,3/2,1/3,2,1,3)`. Then the length-two relative-zero total is `2*sum_i p_i m_i = 143/6` exactly; the histogram witness verifies preservation of rational branch weights rather than collapsing them to Boolean reachability.

## 3. Executed checks and precise remaining integration

A locally executed, independent Python exact-arithmetic implementation of this quotient recurrence and native-depth/histogram cross-check obtained:

```
PASS X6_LP026_SIGNED_LAURENT_QUOTIENT_CONSUMER
unweighted_state_length_cases 31065
weighted_depth_multinomial_cases 1205
signed_relative_n6_zero 21360
signed_relative_n8_011235 4200
legacy_positive_n6_zero 720
weighted_n2_zero 143/6
```

The unweighted run exhausts all states reached in lengths 0..8, with state counts `[1,12,73,284,835,2036,4347,8408,15069]` and exact total `12^N` at each length; it checks reflection `C(N,q)=C(N,-q)`. Weighted runs (lengths 0..4) compare every reached quotient state against independently enumerated native `12`-letter multinomial histograms and all possible depths. These are finite exact algorithm checks; the theorem itself is the algebraic coefficient proof above.

A portable checker implementing the same recurrence, separate histogram reference, and optional import of the *actual current* `relative_endpoint_multiplicity` when a complete repository checkout is available was published at `research_checks/X6_LP026_SIGNED_LAURENT_QUOTIENT_CONSUMER_CHECK_20261112_ONHOUR.py` (initial commit `9150706fe7574b24ff17d740b38489099f9c74d8`). The local execution was of the equivalent standalone exact algorithm; **the optional imported-current-consumer branch remains unexecuted in the local partial environment** and is explicitly printed as such. The source file itself was read from the GitHub connector on current main, Git blob `ac32f6d82a91db99297e587cf63b0df95cece514`.

**Next exact action**: run this checker in the full current checkout to execute the conditional actual-consumer import and record its PASS, then bind the typed positive/signed input distinction to the specific active tests and downstream callers in the 28-row X6 LP ledger. Trace LP011/LP019 remaining historical attribution by exact source rather than guessing. This advances task required outputs 4–6, but the task's corpus-wide consumer closure and historical-source provenance remain open.

Native continuation: Research lane `chatgpt-research-onhour-enterprise-math-20260923`; historical SID `MCP-de3e5bafb24f43f4a5e6285e7601676a` and RA `RA-629C868A22A736334628BEFA`. The last own recovery receipt `onhour-research-20261112-0914-own-recovery-v1` confirms ACTIVE session, no runs/unopened claims/pending requests and explicitly `source_authority_verified=false`. X6 [continuation #6827](https://github.com/awdawmip/kimi-query-bridge/issues/6827) requires typed predecessor preparation; [support #2141](https://github.com/awdawmip/enterprise-math/issues/2141) tracks the progress artifact allowlist. This note does not serve as a native semantic checkpoint, Result, independent review or promotion.

# R252 — An all-horizon inverse-anchor blind fiber for positive BRC affine packets

**Date:** 2026-10-24. **Status:** author-side mathematical theorem and independent exact finite validations. Not a native Heartbeat World update theorem or a formal admitted Result.

**Frozen sources:** GLOBAL_KNOWLEDGE_V1 main `03b776e67e1d3419328d5d217e49e667cb3cde72`, EM Source main `28e35a1fd123e2cb3bdb29165928844c6792fd59`. Original P000 and ACTIVE residual-fidelity worldview apply. R250 and R251 are predecessors, not new findings of R252. Relevant exact Source interfaces: `Affine.then`, `Affine.inverse`, `EffectHistogram.from_terms`, `ControlPacket.from_edges`, `ControlPacket.then`.

## Typed restricted X6 carrier

Use raw chart-relative integer displacements in the **full six-axis** X6 carrier `Z^6`; a selected chart anchor `0` is not a distinguished physical origin or final Cell address. Time is separately typed by the positive duration of successive BRC packets. Put `e1=(1,0,0,0,0,0)` and `S=diag(-1,-1,1,1,1,1)`. Define formal affine maps

```text
T_k(z) = z + k e1
R_k(z) = S z + k e1.
```

They act on six coordinates despite their compact two-parameter encoding. No separate native lower-dimensional space is being introduced. This affine family has **not** been shown admissible as a real triadic heartbeat update.

A one-letter packet `a` has 3 **nonspatial** controls and 6 alternative edges (every edge unit positive BRC weight and count 1):

```text
0 --R_-1--> 2       0 --T_-1--> 2
1 --R_-1--> 0       1 --T_-1--> 0
2 --T_+1--> 1       2 --T_-1--> 2
```

All path histories remain distinct during propagation and are coalesced only for the declared observation. Serial composition is `F.then(g)=g ◦ F`.

Define an **inverse-anchor observer** of a complete accumulated affine effect `F` by `Phi(F)=F^{-1}(0)`. Its positive path-count histogram drops terminal control, internal branch identity and all full-effect information not determined by `Phi(F)`. It must not be confused with native `EffectHistogram.evaluate(0)`, which is the *forward* observer `F(0)`.

## R252.1 — control-independent inverse-anchor convolution theorem

Let any finite-control positive packet on a chart `Z^d` have bijective affine effects `g_e(z)=L_e z+b_e` with **unit weight** and integer path multiplicity `c_e≥1`. For every control `q`, form the finite positive measure

`mu_q = sum_{e departing q} c_e delta_{g_e^{-1}(0)}.`

Suppose (i) `mu_q=mu` for every control and (ii) every attainable accumulated linear part `L_F` satisfies `(L_F^{-1})_* mu=mu`. Then from any starting control and initial identity effect, the inverse-anchor histogram after **every** finite packet length `m` is exactly

`A_m = mu^{*m}`,

convolution under addition of raw chart displacements.

**Proof.** If `F(z)=L_F z+b_F` is the effect accumulated through a path prefix, appending `g` yields

`Phi(g ◦ F)=F^{-1}(g^{-1}(0))=Phi(F)+L_F^{-1}g^{-1}(0).`

Therefore this prefix's entire outgoing positive inverse-anchor measure is `delta_{Phi(F)} * (L_F^{-1})_*mu_q=delta_{Phi(F)}*mu`, independently of hidden control and the previous accumulated effect. Summing over prefixes gives `A_{m+1}=A_m*mu`. Since `A_0=delta_0`, induction establishes `A_m=mu^{*m}` for all `m≥0`. No negative path weight, phase cancellation, stochastic normalization or finite-horizon extrapolation is used. QED.

This theorem concerns only the declared pushforward observation. It is not a sufficient proof of a safe quotient for all later full-effect or provenance-sensitive operations.

## R252.2 — exact binomial all-horizon blind fiber

For the six edges above, direct inversion gives

```text
R_-1^{-1}(0) = -e1,  T_-1^{-1}(0) = +e1
T_+1^{-1}(0) = -e1,  T_-1^{-1}(0) = +e1.
```

Each control therefore has the same outgoing measure `mu=delta_{-e1}+delta_{+e1}`. All accumulated linear parts belong to `{I_6,S}`; `S` merely swaps `+e1` and `-e1`, hence preserves `mu`. By R252.1, **both** initial controls 0 and 1 obey the exact positive-binomial formula

```text
A_m^(0) = A_m^(1)
        = sum_{j=0}^m binom(m,j) delta_{(m-2j)e1}, every m>=0.
P_m(X)  = (X + X^{-1})^m.
```

At any depth `m`, the inverse-anchor histogram has exactly `m+1` distinct positions and total positive path multiplicity `2^m`. This equality holds at **all finite future times**; it is not a finite-test conjecture.

Yet the complete six-axis affine-effect histograms differ at depth 3 (R250/R251 original witness; independently checked in the attached author verifier):

```text
H_0(a^3) = R_-3 + 3 R_-1 + T_-3 + 3 T_-1
H_1(a^3) = R_-3 + 2 R_-1 + R_+1 + T_-3 + 2 T_-1 + T_+1
```

They agree at depths 0,1,2 but differ at depth 3. The signed **external comparison** is `R_-1+T_-1-R_+1-T_+1 != 0`; each actual histogram contains exactly 8 **positive** paths. Because `R_k^{-1}(0)=k e1` and `T_k^{-1}(0)=-k e1`, this difference vanishes under the inverse-anchor pushforward at depth 3, as the theorem proves it must at all depths.

**Consequence:** a nontrivial complete-effect residual can remain exactly invisible under a declared inverse-anchor observer for *every* finite horizon. Thus matching an exact binomial readout forever is insufficient to infer equality of BRC's complete effect histograms. This is an observer-relative mathematical statement, not a statement about empirical probability.

## R252.3 — precise stress test

Modify **only** the edge `2 --T_+1--> 1` to `2 --T_+2--> 1`. Now `mu_2=delta_{-2e1}+delta_{+e1}`, which differs from `mu_0`. The two starting controls still agree after one step, but after two steps:

```text
A_2^(0) = delta_{-2e1}+delta_{-e1}+delta_{+e1}+delta_{+2e1}
A_2^(1) = delta_{-2e1}+2 delta_0+delta_{+2e1}.
```

The control-independent outgoing-kernel hypothesis has a genuine role. This is a sharp concrete failure when it is altered, not a claim that the hypothesis is universally necessary for all future equivalences.

## Exact verification and scope

- Python author-side positive BRC DP: both starts, **all 41 depths 0..40**, binomial coefficients, exactly `2^m` positive paths, full-effect witness at depth 3, altered-kernel failure at depth 2; PASS.
- Independent C++17 positive-path DP: **all 31 depths 0..30**; PASS.
- Infinite-horizon equality has the analytic induction proof above; finite programs independently test the declared six-axis affine model and the witnesses.
- Current native Python `enterprise_math` package was **not executed**. Interface laws from the pinned Source were applied on paper (`REUSE_APPLIED`); executable native reuse remains `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE`.
- A formal affinity-preserving chart map is not evidence of lawful native Heartbeat update, nor of R193 ordered path/provenance preservation, final Cell-address semantics, physical time law, experimental calibration or admissibility in Foundation.

## Next concrete unit

Execute the exact R250 3-control positive packet through native `ControlPacket.from_edges`, `ControlPacket.then` (distinct aligned duration/start time ports) and `EffectHistogram.entries` with six-axis `Affine` maps. Separately construct the new inverse-anchor observer with `Affine.inverse().apply(chosen_raw_anchor)` instead of forward `evaluate(anchor)`, and verify the binomial formula at depths 0..3. Test whether the *actually permitted* X6 heartbeat effects share the kernel invariance, and whether original tagged ordered paths (R193) need a finer state. Formal Task/CLAIM, independent Driver review and Result admission are separate from this author-side research draft.

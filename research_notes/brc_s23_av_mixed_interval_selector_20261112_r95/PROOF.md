# R95 — Exact mixed-interval winner-profile restriction and workload-aware selection

Date: 2026-11-12. Status: independently reproducible **author-side proof and finite exact verification**; independent scientific review pending.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Scientific lineage: R82, R86, R90–R94, especially R94 proof at commit `d26b8b56ac9d0ac3768488d5ac71340985cf40d4`.

## Precise model and BRC carrier

This is the auxiliary *finite rational circular-source model*, not an asserted native X6/heartbeat transfer. Let the finite source identity set be `S ⊂ Z×Z`, with identity `(t,branch)`. Fix an observation signature `σ=(j,x,a,b)` (integer `j,a,b`, rational `x`), and let `M_t(θ)` be R90's exact original directed half-open circular-arc membership. Define `W_{S,σ}(θ)=max_lex{(t,branch)∈S: M_t(θ)}`, or `NONE` for an empty qualified set. Retain full branch identity for the winner; time fibers only share the Boolean membership predicate. R86's exact whole-interval winner profile and R94's certified-OUT-index classifier are interchangeable exact observers under the same signature.

## Theorem R95.1: exact restriction without a fresh oracle

Let `D=[d0,d1]` be a closed rational interval and let `P` be R86's fully exact winner profile on D, storing values at *every* rational breakpoint and separately on each open gap. For **any** closed rational `I=[u,v]⊆D`, including singleton `u=v`, take all global breakpoints strictly inside I, both endpoints, and one rational midpoint of each resulting open gap. Evaluating `P` at these finitely many rational representatives determines whether `W` is `STABLE_NONE`, `STABLE(full identity)`, or `CHANGES`; in the last case two rational representatives with different exact full identities are witnesses.

Proof: the R86/R90 exact critical construction partitions D into finitely many point atoms and open-gap atoms, with `W` constant on each open atom. Restriction only subdivides existing constant atoms; preserving the original point values retains half-open boundary semantics. Each new atom is sampled at least once by the indicated list. Hence equality of those samples is equivalent to equality for all real θ∈I, and differing samples are actual rational witnesses. QED.

The implementation uses binary search to select breakpoints; it evaluates `O(k+1)` rational representatives for `k` interior breakpoints. Its present straightforward evaluation calls R86's logarithmic point evaluator for each representative; eager profile construction is charged separately.

## Theorem R95.2: certificate-version independence

For a **fixed** source version S, signature σ and covering D, the exact profile `P_{S,σ,D}` has the same mathematical query answer on every `I⊆D` under **all** independently edited collections `B_j` of already-valid OUT certificates.

Proof: `W_{S,σ}` depends only on S and M. R94's exact box-cover method uses certified exclusions solely to prune candidates known to be OUT, which cannot change W. R95.1 computes the same restricted function directly. QED.

A profile cache must therefore key on actual source version + complete observer signature + covering domain, but need not invalidate for certified-box-only edits. Old source version roots preserve old historical answers. A new signature or uncovered interval requires the corresponding exact construction or sound incremental update.

## Theorem R95.3: fixed-regime, online strategy with a sharp 2 bound

For a fixed source version, signature and covering domain, assume known **stationary nonnegative integer costs** `P` (one eager profile construction), `L` (each exact lazy indexed-pruning query), `E` (each exact eager profile restriction query), and unknown count n of future queries. If `L≤E`, always use lazy. Otherwise put `Δ=L−E>0` and `k=floor(P/Δ)`. Use lazy for the first k queries. If query k+1 occurs, buy/build the profile before answering it, and use eager afterward.

Then the offline optimal cost among those two fixed strategies is `C_opt(n)=min(nL,P+nE)`, and the online rule satisfies

`C_on(n)−nE ≤ 2(C_opt(n)−nE)`, hence `C_on(n) ≤ 2 C_opt(n)`.

Proof: if n≤k, the online excess above base nE is nΔ≤P and matches the offline excess. If n>k, then nΔ>P; offline excess is P, online excess is kΔ+P≤2P. This includes P=0 and n=0. If L≤E lazy is optimal. QED.

The 2-competitive claim is for this *specified stationary-cost model*. If costs change, prior estimates do not imply the bound. Exact illustrative counterexample: predicted (P,L,E)=(100,120,1), n=1 causes immediate eager cost 101, whereas if actual lazy/eager query costs are both 1, the offline one-query cost is 1.

## Executed verification (CPython, exact Fraction)

The full unmodified R82/R86/R90/R91/R92/R93/R94 dependencies, R95 full Python driver and raw JSON results are in the accompanying reproducibility bundle. Code artifact in this directory is losslessly gzip/base64-encoded for GitHub text transport; decode with `base64 -d check_r95.py.gz.b64 | gzip -d > check_r95.py`. Do likewise for the JSON.

Actual run: `R95_PASS 147 49 223 85995`. The mixed history tested 7 selected source versions, 3 signatures, 7 closed rational intervals: **147 exact all-real lazy/eager/reference agreements** and **49 exact cross-certificate-version reuse checks**. These 147 narrow-window cases were STABLE. Separately the adversarial broad-domain suite covered 18 signatures × 4 finite source families × 7 intervals = **504 exact reference agreements**: **223 CHANGES** with verified distinct rational witness values, **165 STABLE** and **116 STABLE_NONE**, including singleton endpoints, negative coefficients and degenerate arcs. Exhaustive finite arithmetic checks covered **85,995** bounded stationary cost tuples and observed a maximum incremental ratio of **2.0**, supplementing the general algebraic proof.

In one process, median across 21 signature/version groups: profile build **0.933 ms**, indexed lazy query **0.451 ms**, profile restriction **0.0107 ms**. These are measured route components, not a claim of universal end-to-end speed. The broad-domain rational critical/witness samples had maximum numerator+denominator representation length **31 bits** (median **6 bits**), not a complete integer bit-operation count.

Status: precise auxiliary-model proof plus checked finite implementations; current formal S23 task linkage, original-source activity and independent review are separate control events.

## Next exact R96 unit

Build and validate a version-aware incremental chooser on mixed source edits, certificate churn, changing signatures, broad CHANGES intervals and repeated domains, *including* eager profile update/rebuild costs, certificate production/index updates, retained-history memory, rational bit-arithmetic work and exact witness recovery. Test whether a calibrated selector improves total workload cost; preserve full source branch identities and all rational endpoint semantics.

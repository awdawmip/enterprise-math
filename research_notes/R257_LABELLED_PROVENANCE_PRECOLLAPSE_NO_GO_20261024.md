# R257 — Exact finite-source-query lift before BRC effect collapse

**2026-10-24. Author-side mathematical proof / UNREVIEWED; not formal Result, not P000 heartbeat-dynamics theorem.**

Researcher-ID (local, not service-issued): `EM-DIRECT-R257P4`. Activity `RA-EMR4-20261024-1757-R257P`, registered to Source main at `7688e2e6f7b470148b7d4d3144eb5ab72f7e8f13`.

## Frozen authority and exact source

GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge@3211ccb200758fd97706b11b3be7353329320702`; P000 startup matches original locked P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. The six native spatial dimensions and distinct time dimension are unchanged. Additional finite monitor controls below are not new spatial axes.

Enterprise Math Source pin: `awdawmip/enterprise-math@9a1659352c5c5959e82c87924c4c2939c77c0b1b`. Relevant original module blobs:
- `src/enterprise_math/brc_transport.py`, blob `be1debe367263931bd5e93fd750be3ed54624fe1`;
- `src/enterprise_math/brc_control_port.py`, blob `44def6b8ac787e798d3cc2c6be16f873f91b9db8`.

Source laws inspected at these pins: `Affine.then` is chronological composition, so first `(A,b)` then `(B,c)` yields `(BA,Bb+c)`; `EffectHistogram.from_terms` coalesces identical joint `(positive rational weight,Affine)` effects by summing *positive integer path multiplicities*. `ControlPacket.from_edges` takes native five-fields `(source,target,weight,action,count)` and has **no source-edge selector-label field**. `ControlPacket.then` requires `earlier.end == later.start`, composes effects and multiplies positive weights and counts, summing matching intermediate controls.

R256 exact author frontier: `research_notes/R256_REGULAR_SOURCE_QUERY_FUTURE_SAFE_20261024.md` at immutable commit `b2f5560ce85c5ff63a2e3e9bfff658ff4a10ce49`. Its example monitor detects the source-token substring `00`; this is NOT asserted to be the actual R193 contract.

## Question and carrier

Can native Source `ControlPacket` faithfully compute a finite source-token query while retaining its unmodified six-dimensional positive effect algebra and time ports? Can a provenance query be recovered once source labels have already been erased by `from_edges`?

Fix finite **nonspatial** controls `Q`, finite source-edge alphabet `Λ`, finite deterministic monitor `D=(R,r0,δ,g)`, and a sequence of compatible labelled positive branch packets. A raw edge is a distinct source-edge occurrence `e=(q,t,λ,w,F,c)`, with `q,t∈Q`, `λ∈Λ`, rational `w>0`, six-dimensional rational affine effect `F`, integer multiplicity `c>0`. Distinct edge occurrences are allowed to have identical native fields. Historical paths are ordered raw-edge choices. This is a declared formal BRC interface, not a proven legal native heartbeat rotation.

Let `K=|R|`, encode nonspatial product controls `(q,r)` by `K*q+r` and lift EACH raw edge for EVERY monitor state `r` to native five-fields:

```text
(q,t,λ,w,F,c) ↦ (K*q+r, K*t+δ(r,λ), w,F,c).
```

Create `ControlPacket.from_edges(|Q|*K,start,duration,lifted_edges)`, retaining port/time and all positive counts. Only after this pre-collapse lift may native `EffectHistogram` aggregate same joint effects. Serially compose matching ports with `ControlPacket.then`.

## Theorem A — exact joint histogram and projection for all finite futures

**Statement.** For any finite sequence of time-compatible packets and any `m≥0`, the product-lift computes exactly the joint histogram of terminal original control `q`, terminal query monitor state `r`, *product* rational path weight `w`, chronologically composed six-dimensional affine effect `F`, and its nonnegative integer raw-path multiplicity. For a fixed initial control `q0` and initial monitor `r0`, write its histogram `P_m(q,r;w,F)`. Write `U_m(q;w,F)` for the native histogram obtained from the same labelled raw edges by erasing source labels before `from_edges`. Then

```text
U_m(q;w,F) = ∑_(r in R) P_m(q,r;w,F).
```

In particular any finite-state source query `g(r)` is exactly determined by the terminal product histogram for all finite horizons and allowed compatible future packet sequences.

**Proof.** At depth zero the empty raw path has effect identity, rational weight 1, multiplicity 1, initial control `(q0,r0)`; the projected histogram equals the unlabelled Source identity. Assume the assertion at length `m`. Every ordered raw-edge path of length `m+1` has one uniquely determined prefix of length `m` and one final edge `e=(q,t,λ,w_e,F_e,c_e)`. The deterministic query update is `δ(r,λ)`. The Source exact operations give weight `w_prefix*w_e`, effect `F_prefix.then(F_e)`, and multiplicity `c_prefix*c_e`. `ControlPacket.then` sums precisely over intermediate product controls, while `EffectHistogram.alternatives` adds coincident positive atoms. Thus the lifted packet represents each raw path exactly once with the correct joint atom. Conversely each term in the Source product corresponds to one raw-path extension. Induction proves exactness for every finite `m`. Terminal monitor states partition the same raw path collection, so summing them is precisely the label-forgotten five-field packet calculation. The native matched clock ports ensure all products in the statement are defined. QED.

This theorem neither retains unique ordered path identity past its declared query-state quotient, nor guarantees finite effect support independent of `m`, nor establishes a physical X6 action/registered address codec. It does not assert `|Q||R|` is a minimal control model.

## Theorem B — sharp irreversibility of post-collapse source-query recovery

**Statement.** No algorithm receiving only the ordinary five-field `ControlPacket` representation, even with its exact unlabelled serial powers at every horizon, can uniformly reconstruct the number of original labelled edge paths whose selector history contains `00`. The first possible failure for this query is depth **two**.

**Proof by two positive presentations.** Use one control state `q=0`, six-axis identity affine effect `I6`, positive weight 1, and exactly TWO distinguishable raw source-edge occurrences per step, each from 0 to 0 with count 1. In presentation **A** label these two occurrences 0 and 1. In presentation **B** label both distinct occurrences 0. Both produce exactly the same native `ControlPacket.from_edges` after source labels are omitted:

```text
(0 → 0, weight=1, action=I6, multiplicity=2).
```

Their unlabelled serial power at horizon `m` is always the same single positive atom of multiplicity `2^m`. At `m=2`, A has four ordered raw-edge choices, but only `00` satisfies the source-token query: query count A is 1. B has four distinguishable raw-edge paths, all labelled `00`: query count B is 4. Thus all native packet data and all their unlabelled futures agree while the required query answers disagree. A function of the common unlabelled data cannot give both correct answers. At depth 0 or 1 no word can contain a two-symbol substring, proving the claimed first possible depth. QED.

This witness uses only **positive** multiplicities; the displayed contrast is an external comparison of two presentations, NOT internal negative branch weights or interference. Label loss does not imply historical path identities cannot be recovered from a separate correctly retained source ledger.

## Source-level integration law

1. Preserve original edge source labels through a finite-state monitor update **before** the first `ControlPacket.from_edges` coalescence.
2. Use the existing six-dimensional `Affine` and `EffectHistogram` unchanged, and put monitor memory in finite **nonspatial** product-control states.
3. Preserve native `start`, `duration`, `end` and the serial matching-port precondition; count a discrete composition step, not a physical elapsed-heartbeat interval.
4. At the final required observation, project over monitor states to reproduce original complete-effect histograms. Projection may be destructive for future source-sensitive queries.
5. Where R193 may require more than a regular source-token query, do not substitute this demo monitor or equate its labels with verified R193 edge IDs.

Reuse resolution: `REUSE_APPLIED` to `T0_BRC`, `T0_BRC_AFFINE_EFFECT_TRANSPORT`, Source `Affine.then/EffectHistogram/ControlPacket`. A concrete labelled-edge lift is an `EXTEND_EXISTING_TOOL` candidate, not a new admitted family. `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE`: no actual original `enterprise_math` package import/execution in this run.

## Exact finite author-side evidence

Companion author-side Python verifier uses `fractions.Fraction`, exact integer counts and the declared two-sign first-axis formal subfamily of six-dimensional effects, **not** the Source module:
- Theorem B: depth two, equal unlabelled mass `4`; accepting counts A=`1`, B=`4`.
- R256 3-control two-choice formal example: exact lifted/forgotten-histogram equality through depth `24`; all `2^0+⋯+2^10=2047` selector words compared with DP; at depth 24 total `2^24`, accepted `16,655,823`.
- 24 deterministic-seed (`2572401`) two-control examples with positive rational weights, multiplicities, first-axis offsets and sign effects: matching all `m=0..10` (264 comparisons).
- Exact auxiliary code execution `PASS`, report `R257_AUXILIARY_REPORT.json`; full proof validity is inductive and does not rest on test extrapolation.

## Actual status, limits and R258

GitHub user `awdawmip`. Direct research activity `RA-EMR4-20261024-1757-R257P` recorded and read from immutable Source main registration commit `7688e2e6f7b470148b7d4d3144eb5ab72f7e8f13`. Native session registration returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`; live task inventory returned `CONTROL_QUOTA`. Winning owner/CLAIM **not verified**. No formal Result, independent Driver review, theorem admission, or physical-law inference. Real R193 raw source-token/query/time-port grammar not located in bounded current-source searches; its actual contract remains unresolved.

**Next exact unit R258:** locate R193 immutable source query/edge vocabulary/clock contract, then prove a language- or word-preserving map to this exact pre-collapse product interface or provide a minimal obstruction. Execute the original Source `ControlPacket.from_edges`, `then` and `EffectHistogram` with matching version and compare its finite output with the auxiliary certificate. Separately prove native legal-X6-Cell effects and physical clock correspondence before any P000 heartbeat transfer.

**Classification:** author-side theorem and strict minimal-depth counterexample in declared positive BRC formal carrier; exact author-side finite checks; **no** native package computation, R193 source claim, formal task result or independent review.

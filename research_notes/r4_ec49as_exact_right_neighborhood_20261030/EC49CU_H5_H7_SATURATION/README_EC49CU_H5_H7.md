# EC49CU — Exact signed-X6 positive-BRC full saturation at h=5,6,7

Date: 2026-11-01 (Asia/Shanghai). Status: **AUTHOR_EXACT_LITERAL_MODULAR_PROOF / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED**. No formal native CLAIM, Result or independent Driver admission is asserted.

## Scope and frozen sources

Current GLOBAL_KNOWLEDGE_V1 canonical-main read: `469b5c71291ffe548387a98f31b14b4a793223f2` (entry files, P000-related worldview, mathematics/BRC/code policies); Enterprise Math main: `9412897fb2b8e77bb30ee26391fb65edaba2a8fd`; previous author-side EC49CU universal extreme-fiber lower bound: PR #1730 at `a97e2b7625d365b05e0b77dbbcf6d49bfa731c84`. P000 and the ACTIVE six-axis worldview are unchanged.

Native ordered alphabet is the 12 signed primitive directions ±E1,...,±E6 in a chosen chart of the six-dimensional cell torsor; signed displacements are **not** public final Cell addresses. A=(+E1,+E2) and B=(+E2,+E1) are consecutive ordered-letter patterns; their nine-state DFA retains completion and pending-first-letter flags. The four final tags indicate whether A, B have been observed. Actual prefix-path BRC channels are: W0 positive-letter weights (2,3,3,2,1,1), W1 weights (3,2,3,2,1,1), and exact count W2=1; each negative letter has weight 1 in both positive channels.

The five *complete operations* are a=(-E1,-E1), b=(-E2,-E2), c=(+E1,+E2,-E1,-E2), d=(+E2,+E1,-E2,-E1), e=(+E3,+E1,+E1,-E3). Let S'={a,b,c,d,e}; each observation R_(u,t,j) is the **exact** BRC-weighted or unweighted sum of genuine prefix paths that, after appending suffix-operation word u, return to displacement zero and finish at joint tag t. A suffix operation is not a primitive space step. The theorem concerns the exact additive rational-linear observer for horizons 1..h, not arbitrary nonlinear compression or physical dynamics.

## Theorem (three new finite-h exact saturation results)

For h=5,6,7, the genuine ordered signed-X6 prefix language first attains the full formal additive observer rank at the respective even lengths n=18,20,22:

| h | exactly h formal and attained rank | 1..h formal and attained rank | first saturated prefix n | target fibers |
|---:|---:|---:|---:|---:|
| 5 | 537 | 582 | **18** | 36 |
| 6 | 741 | 804 | **20** | 49 |
| 7 | 978 | 1062 | **22** | 64 |

Consequently **n_sat(h)=2h+8 for each h in {5,6,7}**, separately for exactly-h and cumulative 1..h languages. This is NOT a theorem for all h.

## Proof: exact formal upper, literal lower, and earliest length

**Formal upper.** A suffix can return from exactly one six-component prefix displacement D=(2u,2v,0,0,0,0), v>=0 and |u|+v<=h. The 9-state DFA gives an exact rational rowspace per target. Exhaustively enumerating all 5+25+...+5^h complete suffix words and the four final tags, and performing **exact rational elimination** on their 9-component start-state indicator rows, gives dimension 4 for each boundary target |u|+v=h (2h+1 targets), and dimension 6 for each of h^2 interior targets, for h=5,6,7. Three independent formal BRC/count channel coordinates give the upper bound
```
D_cumulative(h) = 3*(4*(2*h+1)+6*h*h) = 18*h*h+24*h+12.
D_exact(h)      = 3*(11*h*h+15*h+8)/2   (reused EC49CS all-h theorem).
```
This is the additive rational-linear observer's formal bound. Genuine path channel weights may correlate and decrease its achievable rank; the next step establishes that they do not at these three lengths.

**Genuine lower.** The accompanying `LITERAL_H5.json`, `LITERAL_H6.json`, `LITERAL_H7.json` contain respectively 582, 804 and 1062 *explicit, length-exact* ordered signed-X6 prefixes, each attached to one target fiber, plus a small chosen list of authentic suffix-word/final-tag rows. For each fiber, take three copies of the chosen row list, one for each BRC/count channel. The entry
```
M[(suffix,tag,channel),prefix]
  = 1_{endpoint(prefix+suffix)=0}
    * 1_{ordered_joint_tag(prefix+suffix)=tag}
    * positive_native_BRC_weight(channel,prefix+suffix).
```
There is no cancellation of signed amplitudes: all native BRC weights are positive integers, and the count channel is 1 per path. A direct literal primitive-step replay (rather than a compressed-state evaluation) verifies every endpoint and tag and computes all entries as exact integers reduced modulo p=1,000,003. In all 36+49+64=**149** target fibers the resulting square minor is nonzero modulo p. Therefore every determinant is nonzero over Z and Q, and genuine rank is at least 582,804,1062, matching the upper bounds. The supplied `VERIFY_EC49CU_H5_H7.py` also recomputes the entire exact-Q suffix formal upper rowspace.

**Earliest.** The prior EC49CU analytic extreme-target lemma at `a97e2b7...` proves for **all h>=4** that target (-2h,0,0,0,0,0) has genuine rank 11 of 12 at n=2h+6, and 12 of 12 at n=2h+8. Thus n=2h+6 cannot attain global saturation, nor can any smaller even n: prepending a neutral primitive pair (+E3,-E3) would embed any earlier full-rank witness into length 2h+6 (preserving tags and multiplying the two positive weight channels by 3). Odd n have incompatible parity with even target displacement. Hence the exhibited full-rank lengths are strictly minimal. Prepending the same neutral pair proves saturation for every *greater even* n. QED.

## Verification, resource scope, and exact evidence

Three standalone sets of literal certificates are available as JSON; 149 raw-BRC block determinants, all nonzero modulo the stated prime, are recorded in `EXACT_H5_H7_REPORT.json`. Each record gives the full ordered primitive path, selected complete suffix, tag, signed target endpoint, and number of deterministic search attempts. Recompute with:

```
python3 VERIFY_EC49CU_H5_H7.py LITERAL_H5.json LITERAL_H6.json LITERAL_H7.json
```

The author additionally ran an independent Python integer implementation using a different deterministic sampler and a separate literal replay checker: h5 at n18 attained 582/582, h6 at n20 attained 804/804, and h7 at n22 attained 1062/1062. Its exact-Q suffix-row calculations also produced 582,804,1062; local original certificate SHA256: h5 `abdef5c502d25523689adcee96abce5d2b4efff61b9c349cca7bfec890e4bf20`; h6 `a0ac08d75a8e3f035d2f8df29c318ef3a2cf1396df73154378f7063de286daa8`; h7 `12b16d745433e564716ff9bfce8a3c2d49a6ece3836b5784873ac5ee0570cabe`. These are separately retained local check results, **not** the checksums of the three published literal JSON witnesses. No probabilistic rank inference is used: candidate path search is heuristic, but the finite displayed nonzero determinants are deterministic, independently checkable exact witnesses.

These conclusions only concern the finite positive-integer signed-X6 path/ordered-label BRC model, the specified suffix operations and rational-linear additive exact observation. No infinite-h n_sat formula, physical propagation law, nonlinear memory lower bound, quantum phase cancellation, or standalone native three-dimensional-slice dynamics follows.

## Authority and continuation

The connected native gateway status read in this run reported service version 0.6.11, `research_authority_granted=false`, `executor_binding_configured=false`, and `source_sync.control.state=CODE_REVIEW_REQUIRED`. It does not establish a current active owner, a new session/CLAIM, a formal Result or independent mathematical review. These artifacts are author's portable conservation of scientific evidence, with actual contribution provenance kept intact. An earlier owner inventory returned CONTROL_QUOTA, but was not retested as a write in this run.

**Next EC49CV:** test h=8 first at the predicted lower-bound length n=24 (formal cumulative 140? use formula `18*8*8+24*8+12=1356`), build full real-path minors if possible, and seek a **uniform constructive induction** for every h>=4 (or an explicit least counterexample). Track exact-Q upper spaces and correlated genuine BRC channels separately; do not turn several finite-h certificates into an all-h proof.

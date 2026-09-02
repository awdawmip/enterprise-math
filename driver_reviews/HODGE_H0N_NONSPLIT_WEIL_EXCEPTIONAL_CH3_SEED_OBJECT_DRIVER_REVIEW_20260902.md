# Driver Review — HODGE H0N Non-Split Weil Exceptional `ch_3` Seed Object

- Task-ID: `RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT`
- Publication-ID: `TP2-9A71D4C6E2B5083F16CD`
- Result-ID: `RR-65EB865C14B89B964BB9`
- Execution-ID: `ER-E30109282875D92161A7`
- Driver-ID: `EM-DVR-7B2F9A`
- Disposition: `ACCEPTED`
- Accepted terminal class: `NEGATIVE_BOUNDARY`
- Accepted strength: `REUSABLE_NATURAL_SOURCE_FAMILY_NO_GO_WITH_EXACT_EXCEPTIONAL_PROJECTOR__GENERAL_SEED_EXISTENCE_OPEN`

## Review conclusion

The result satisfies the H0N hard target at the taskbook's explicitly authorized negative-success strength. It does not construct a nonzero exceptional seed, but it proves reusable theorem-level zero-projection results for the declared natural source families and constructs an exact algebraic spectral projector separating the exceptional Weil carrier from the divisor-cube line.

Acceptance is deliberately narrower than any algebraicity or non-algebraicity statement.

## Evidence accepted

1. The fixed non-split target and the degree-six exceptional decomposition are re-audited before use.
2. The algebraic spectral projector `Pi_W` is constructed from the target `K`-endomorphism action and isolates the two exceptional eigenblocks while annihilating the mixed divisor-cube block. The projector is accepted only as a separator/operator, not as an algebraic seed class.
3. For semihomogeneous bundles, `ch_3(E)=c_1(E)^3/(6r^2)` and `NS_Q=Q theta` force `ch_3(E)` into `Q theta^3`, hence `Pi_W(ch_3(E))=0`.
4. Finite shifts, direct sums, extensions and cones preserve the same `K_0`/Chern-character confinement. The result correctly refuses to extend this statement to arbitrary direct summands or Karoubi completion.
5. The Fourier–Mukai no-go is restricted to outputs independently verified to be semihomogeneous. Arbitrary or genuinely non-semihomogeneous Fourier–Mukai outputs are not closed.
6. Polarization/target-`K` endomorphism constructions and the declared Thom–Porteous families with divisor-algebra Chern data remain in the divisor algebra and therefore have zero exceptional projection.
7. The result explicitly rejects a blanket correspondence no-go: `Pi_W` itself is an algebraic correspondence at operator level, so the unresolved issue is an algebraic input with nonzero exceptional image.
8. The deterministic checker reports `20/20 PASS` for the finite/symbolic certificate layer. The unbounded geometric statements remain theorem arguments rather than being replaced by finite computation.

## Scope restrictions

This review does **not** accept any of the following:

- that `W_K` is non-algebraic;
- that the Hodge conjecture is settled for the target sixfold;
- that arbitrary Fourier–Mukai objects have zero exceptional projection;
- that arbitrary direct summands of the finite semihomogeneous closure remain divisor-generated;
- that arbitrary algebraic correspondences cannot reach `W_K`;
- any H1 promotion.

## Successor gate

A successor is justified because H0N leaves one narrow, discriminating structured family open: genuinely non-semihomogeneous Fourier–Mukai outputs with intermediate support. The parent result does not close this family, and it is more sharply typed than an unrestricted search over all derived objects or correspondences.

The accepted successor is:

- Task-ID: `RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3`
- Publication-ID: `TP2-A314F727276CFF8CE168`
- Hard target: `NONSPLIT_WEIL_INTERMEDIATE_SUPPORT_FM_EXCEPTIONAL_CH3_SEED_OR_EXACT_NO_GO_CLASSIFIED`

H0O must freeze one explicit intermediate-support Fourier–Mukai/GRR family and terminate on a nonzero exceptional seed, a theorem-level zero-projection result for that family, or an exact target-side instantiation obstruction. It may not broaden itself to all correspondences, all derived objects, non-algebraicity, or H1.

## Control disposition

`RR-65EB865C14B89B964BB9` is terminally accepted at the declared negative-boundary strength. The parent H0N task is closed at task scope; the parent objective remains open. H0O is a separate continuation and receives only the exact accepted H0N boundary, not stronger Working Truth or foundation status.

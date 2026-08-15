# R054 — Exhaustive K=3 Collapse Optimality and Asymptotic Bias Obstruction

Researcher-ID: `EM-R054-7A0050`  
Status: `RESEARCH CHECKPOINT / NOT CANONICAL / CALIBRATION`

## Frozen hashes

- `R054_SPLIT_SCORING_PROTOCOL_SHA256 = fba70a1c829f6011f61571d8d3c8e73493d0ce6a5df14031022698d767b89669`
- `R054_K3_CHORD_LIBRARY_SHA256 = d42af9ee4baaa8cbc7b6553b3c13c260cd0915d7aac2911dee03a93ee552e114`
- `R054_PARSER_CONTRACT_SHA256 = 70137fe7dae892759c956e418563506c8818987809034e76acff13f9660803c3`
- `R054_POLICY_CLASS_SHA256 = d0fe5035d39290643c90e491fc0027cb06c7f7d22e7e03abdba4baf1e5a40ae6`
- `R054_OPTIMAL_POLICY_SHA256 = 751566bc5f12360986829041ff9da6a0cc496e385be7bdb28e7bbaaaf73abcb0`
- artifact manifest hash is reported after manifest freeze.

## Fresh K=3 audit

Construction has 32 fresh circles and 50768 exposed edges. Exact translation+D6 enumeration found `3` classes: `['T++', 'TMIX', 'T--']`. Three-type precondition: `True`.

## Exhaustive 27-policy optimum

Selected mapping (T++, TMIX, T--): `['CHORD3', 'CHORD3', 'CHORD3']` (`P27`). It is rank 1 at both 100 and 200 digits; full 27-policy rank identity is `True`.
CHORD3-all ranks 1 at 200d; the old R053 greedy mapping ranks 3.

### Selected validation metrics (200d)

- MSE: `0.024487797796929568131316807931373988785041763042250412643156328784124621585166859698852612685765278026096695566682138506623001012751336517807688435909667023400473480256036250977506422234831166711014826`
- MAE: `0.15607471593937688260836364480286196412368472669317852397796457694062136677688532414897084773453052988481859432819358715933437144580284227548772341413747350557075082530123708683472429552599609056443077`
- signed bias: `0.15607471593937688260836364480286196412368472669317852397796457694062136677688532414897084773453052988481859432819358715933437144580284227548772341413747350557075082530123708683472429552599609056443077`
- max abs: `0.17116936290141611965009912178205491025785972333517729969758510794517763282210851225136040508673602488380510604887785983281359649153442363288059187013411305426044214024577700150323970303846748176995952`

## Fresh strict holdout (post-freeze)

Optimal-policy hash immutable: `True`; no refit: `True`.
Selected holdout rank: `1`; holdout winner mapping: `['CHORD3', 'CHORD3', 'CHORD3']`. Same as validation-selected winner: `True`.
Selected holdout MSE/MAE/bias/max: `0.023517650620653605388498519531710562660425457673043046738040743005955291608103817770590716814854794344551741355407927022320383122469736060653892629131777215478723930641310291647597758605959356907628046` / `0.1531697362617213531725653847368400415470892025976700273619791214993186241669806403083240119166960237030753556207473911966338637064466669959618166249419156965930437687741392650859486676046887355689832` / `0.1531697362617213531725653847368400415470892025976700273619791214993186241669806403083240119166960237030753556207473911966338637064466669959618166249419156965930437687741392650859486676046887355689832` / `0.16623130237451743505870520977829201946151296534679345073759684145087054834837903555294353121097764724517541741817132453159877082149211940102670816568366696541699296800221663528158921588428669269697415`.
Selected beats RAW1 by holdout MSE: `True`; beats old R053 greedy mapping: `True`.

## Tangent validation (opened only after optimal-policy freeze)

RAW1 mean: `32.70631766031571174835335114039480686188` deg; CHORD3-all: `14.1416628891619975405546938418410718441` deg; old greedy: `17.60239074040342899252209463156759738922` deg; selected: `14.1416628891619975405546938418410718441` deg.
Selected circumference-error vs tangent-error Pearson across holdout circles: `0.9922780385134261083024398431007284671068`.

## Exact asymptotic attack

Proved finite radical decomposition for every frozen policy:
`Per_P = N_RAW/sqrt(3) + N_C2 + 2(N_C3_TPP + N_C3_TMM)/sqrt(3) + N_C3_TMIX*sqrt(7/3)`.
Terminal seam contribution is bounded by at most two RAW1 fallbacks, hence its normalized contribution is `O(1/R)`.
Also proved a conditional reduction: whenever the normalized parsed tile counts have phasewise/subsequence limits, `Per_P/(2R)` converges to the corresponding radical-weighted density combination.

Two whole-policy limits are proved exactly: `RAW1-all -> 4` and `CHORD2-all -> 2*sqrt(3)`, hence both have nonzero asymptotic bias relative to classical pi. The remaining 25 policies, including the selected CHORD3-all policy, remain OPEN.

But the necessary all-large-R parsed-tile frequency theorem for these digital circles was **not proved**. Therefore selected policy status is `OPEN_ASYMPTOTIC_WITH_BOUNDED_EVIDENCE`, and `K3_CHORD_FAMILY_PI_OBSTRUCTION = False`. R054 does **not** justify expanding K on a whole-class kill theorem.

## Bounded extrapolation (after theorem effort)

Radii: `[230, 254, 286, 318, 350, 398, 446, 510]` over all 10 frozen R054 phases. This remains `POST_THEOREM_EFFORT / BOUNDED_EXTRAPOLATION_ONLY` and does not alter the OPEN theorem status.

## Exact/adversarial gates

Task-local exact checks: `20/21` pass. The single failed requirement is spatial D6 reflection invariance of the frozen sequential parser; rotations/translations and cyclic/reversal invariance pass. The reflected full-27 adversarial rerank preserves CHORD3-all as winner, but scores change. No post-holdout parser patch is applied. Repository-wide CI was not queried: `CI_NOT_REQUIRED_FOR_RESEARCH`.

## Semantic typing

- teacher circle/radius/classical pi/tangent: `N3_CONTINUUM_CLASSICAL` effective-side calibration surface;
- lattice coordinates: implementation/additional geometric carrier for this declared calibration substrate;
- parser/collapse selection: derived operational semantics;
- perimeter/pi_hat/tangent misalignment: readout/effective comparison;
- no native-pi, physical-lattice, or N0 ontology promotion is claimed.

## Return classification

`OPTIMIZER_DEBT_RESOLVED_WITHIN_FROZEN_PARSER / BEST_K3_POLICY_IDENTIFIED / PARSER_D6_REFLECTION_COUNTEREXAMPLE / ASYMPTOTIC_OPEN / NOT_CANONICAL`

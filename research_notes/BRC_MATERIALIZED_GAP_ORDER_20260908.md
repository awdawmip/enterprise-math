# Prepared-gap ordering, root projection and constructive complete-cost evidence

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Global read snapshot: `b2d9ceff961c70ecb356721aafcb03d31396daeb`  
Project parent: `79c0ed559d177082ea20ed2c3e21fc5342821da4`  
Status: completed fixed mathematical experiment; no public factorization or theorem promotion.

## Concrete result

On three prescribed positive integers of 896, 2048 and 8192 bits, the existing learned order reaches the m=8 witness after two calls, compared with six for the existing structural order on the same seven-position set. The unchanged witness API, its root computations, and final gcd/product verification are included in a separate complete-cost measurement. Median improvement is about 3x, with the learned order faster in all five paired rounds at every size.

The existing prepared-gap sorter also puts all 18 constructive controls at square-witness rank one. Its input-dependent ordering cost is material: a rank improvement is not automatically a time improvement. At 8192 bits its native-predicate experiment is faster than the structural/native case, while the learned/LOW12 combination is faster on all three prescribed prepared inputs.

On the public mathematical puzzles, six newly derived positions have no square witness. They extend the existing record from 60 to 66 unique positions across the same three integers. No larger range or fallback is scanned.

## Source catalog and fixed interface

The 13 inspected entries belong to several different roles. Their catalog declarations do not mean that 13 independent factor-finding methods were executed.

| Catalog ID | Role and evidence used in this thread |
|---|---|
| structural_priority | Existing static representative order; executed here at max_multiplier=12. |
| learned_cover_prefix | The earlier frozen 20-position public experiment is retained. Here the unchanged complete-order API is called at max_multiplier=12. |
| ratio_cover_prefix | Conditional order; a moderate hidden-factor imbalance signal is not supplied for the public inputs. Not executed. |
| kernel13_prefix | Long-horizon prefix; the catalog schedules it for max_multiplier>=128. This experiment has a fixed bound of 12. Not executed. |
| gap_sort_if_materialized | Selected here, after supplying every representative required by the actual max_multiplier=12 interface. |
| low12_compact_gap_filter | Previously verified exact filter, executed here on the prepared scalars and constructive controls. |
| table_free_tail | A memory-oriented transport alternative; no memory-pressure input contract is supplied here. Not executed. |
| quotient_jet_large_bits | Catalog trigger requires at least 4096 input bits and 256 transitions; the three public fixtures and this finite budget do not meet it. Not executed. |
| energy_jet_very_large_bits | Trigger requires at least 8192 bits and 256 transitions. Not executed on the public fixtures. |
| gap_residue_jet_ultralarge | Trigger requires at least 32768 bits, 4000 transitions and a filter-dominated workload. Not executed. |
| brc_shadow_telemetry | Existing exact observations remain metadata; no new routing inference is made. |
| fibonacci_delete_storage_probe | A representation/storage probe, not an additional square-witness observation in this experiment. Not executed. |
| pisano_metadata_probe | Requires an already supplied period/rank. That metadata is absent; no period search is substituted. |

This is a scope and prerequisite inventory, not a claim that unexecuted entries passed a benchmark or are mathematically ineffective. The complete-cost synthetic controls likewise do not silently activate long-stream jet branches.

The unchanged source APIs are structural_order, learned_cover_order, gap_sorted_order_from_materialized_states, passes_low12_compact_square_filter and ceiling_completion_square_witness. Source guards:

- brc_opportunistic_shortcuts.py: SHA-256 7e186c6b17b4b04c37af875c939a92907e929e8a19b2c0c818d3e3bc5f8b94e7; blob 1214aa09770893fb3de7f85b994d1994ff56bffe.
- brc_multiplier_priority_jump.py: SHA-256 ee4a01822ff9e5e33b602b5e834a6902dbd848d0258b981503cea3df513d1a0d; blob f78379664b074b7f40879d4f24af94b48df8fc3b.
- brc_square_gap_prefilter.py: SHA-256 f8e178771a25221eaab16002b9ffacd188dc5f39be4948ec2b40ee3e22c9f716; blob 42d4e9a397b56d9d371f034780ffc736d43e6d96.

Reuse resolution: REUSE_EXECUTED. No production helper or adaptive router is changed.

The complete source-defined set at max_multiplier=12 is

    {1,3,5,7,8,9,11}.

Its fixed structural order is (1,9,3,5,7,8,11); its fixed learned order is (1,8,3,7,9,5,11). These are the actual existing APIs at the declared smaller bound, not the preceding 20-element prefix. No rank comparison silently mixes the two ranges.

The prepared sorter requires all representatives for its requested range. The preceding 20 public records do not satisfy its max_multiplier=100 contract. This experiment completes a separate, explicitly bounded seven-member input rather than marking that incomplete larger map as complete.

## A root-only projection used to complete the input

For a positive integer X and positive integer d,

    floor(sqrt(X)) // d = floor(sqrt(X/d^2)).

To prove it, write J=floor(sqrt(X)) and J=dq+u with 0<=u<d. Dividing J<=sqrt(X)<J+1 by d gives q<=sqrt(X)/d<q+1, including the endpoint case u=d-1. Hence q is the required floor root.

The two fixed applications are:

    floor(sqrt(80N)) // 4 = floor(sqrt(5N)),
    floor(sqrt(99N)) // 3 = floor(sqrt(11N)).

This root projection needs only the source floor root and d. Forming the new remainder and completion gap additionally uses the known target mN. When J is not divisible by d, the remainder is not simply R/d^2; this is distinct from the earlier exact residual-division rule that necessarily ended in D. No source ceiling-square witness is presumed to transport through this floor projection.

The old archive stores A, not the source J. The checker therefore restores a=isqrt(source_m*N+A), verifies the saved ceiling identity, and obtains J=a-1. Restoration is explicitly paid and reported. It is not hidden as a free N-only step. The subsequent division and target gap formation have their own timer. A native floor-root calculation audits each same derived position independently.

The data sources remain the RSA Inc-attributed [RSA-270](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-09-en.pdf), [RSA-896](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-10-en.pdf) and [RSA-2048](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-38-en.pdf) mathematical puzzle PDFs already read and pinned in the preceding certificate. No current challenge-resolution status is inferred from those historical documents.

Input Git blobs:
- Original literal-input certificate: e56cfc8457e2398b5de3c90182c2b37824580ef3.
- Frozen-prefix certificate: c4b201e608167cfff96c5a141bd9e26b575dad69.

Five positions per input (1,3,7,8,9) are reused; two positions (5,11) are newly derived and independently checked. All seven-position orderings are exact permutations of the same complete set. All six new positions have nonsquare gaps, so all public order/backend combinations exhaust their seven entries. No factor is obtained or submitted.

| Public input | Gap-sorted order | Restore two source roots, us | Project two states, us | Create source order, us |
|---|---|---:|---:|---:|
| RSA-270 | 1, 9, 3, 11, 5, 8, 7 | 16.2 | 4.0 | 27.1 |
| RSA-896 | 9, 1, 8, 3, 7, 11, 5 | 13.6 | 3.1 | 21.4 |
| RSA-2048 | 1, 5, 8, 3, 9, 7, 11 | 12.8 | 6.3 | 20.3 |

These are single descriptive measurements from the final expanded checker run, not stable public-input performance estimates. The new m=5 directions are D,D,U; m=11 directions are U,U,D, in the table's input order. Thus state labels remain separate from ordering and are not used as a hidden-factor signal.

## Positive family and exact outcomes

All controls use the retained family

    N=t(2t+1), t odd and t>=3,
    8N=(4t+1)^2-1,
    gcd(N,4t)=t.

The 15 previous small odd t=3,5,...,31 are consumed as constructive input definitions. Three new sizes use the fixed formula t=2^((B-2)/2)+1 for B in {896,2048,8192}. Each resulting N has exactly B bits. No claim is made that these large constructed factors are prime.

For every control, the m=8 completion gap is exactly one and its transformed state is U. Any nonnegative gap collection containing one has a minimum of either zero or one; both are squares. Therefore sorting these complete supplied gaps places a square witness first. Proper nontrivial gcd factors are additionally checked for the actual first witnesses of all 18 controls.

The three large controls have observed first-hit positions 6,2,1 for structural, learned and gap-sorted orders respectively. Both predicate backends agree. The rank-one result concerns squarehood in this supplied family; it does not assert that every arbitrary minimum gap gives a factor.

## Prepared-scalar timing

The seven gaps are already supplied. Static N-independent orders are prepared once. The unchanged input-dependent gap sorter is called inside each gap-sorted timing. LOW12 tables are warm. Seven shuffled rounds use 256 repetitions per case; these repetitions are not additional independent successes.

Median microseconds per evaluation:

| Constructed N bits | Structural + LOW12 | Learned + LOW12 | Gap sort + LOW12 | Structural / learned |
|---|---:|---:|---:|---:|
| 896 | 4.710 | 2.002 | 17.346 | 2.353x |
| 2048 | 4.514 | 1.987 | 16.476 | 2.272x |
| 8192 | 7.269 | 1.980 | 16.806 | 3.671x |

Learned/LOW12 is faster than structural/LOW12 in all 7/7 rounds at each of these three values.

With native square predicates, the 8192-bit structural case takes 76.667 us and the source gap-sorted case 15.240 us, a 5.031x local improvement. This positive gap-sort result is retained under that backend and supplied-state contract. It is not preferred over every measured existing combination.

Preparing the seven constructive states with native roots separately took 24.8, 53.5 and 434.6 us. Those are acquisition costs, not costs included in the prepared-scalar table. Imports, initial tables, constructive factor checks and serialization are also outside that table.

## Complete-cost constructive timing

A separate measurement starts with each of the three fixed large integers N. It calls the unchanged ceiling_completion_square_witness API in either fixed order, stops on the first proper witness within the same seven positions, and includes all of that API's root/preparation work plus gcd and exact product verification.

Five paired rounds perform one evaluation per order and size. The witnessed multiplier is always 8 and the verified factor is exactly the prescribed t. Structural performs six source API calls and learned performs two, totaling 120 calls across the complete-cost measurement. Repetitions do not increase the number of distinct mathematical inputs.

| Constructed N bits | Structural, ms | Learned, ms | Structural / learned | Learned faster rounds |
|---|---:|---:|---:|---:|
| 896 | 2.2291 | 0.7386 | 3.018x | 5/5 |
| 2048 | 12.4128 | 4.0741 | 3.047x | 5/5 |
| 8192 | 415.5358 | 137.3148 | 3.026x | 5/5 |

Static order construction, imports, input generation and initial table setup are outside these timers. Root acquisition and final factor verification are inside. This is an observed N-to-verified-factor benefit on three explicitly constructed positive instances, relative to the current source API and the stated baseline.

The complete-cost API uses its default 4032 filter and generic target-root implementation. The prepared-scalar experiment instead uses native isqrt on the already supplied gap. The two tables measure different paths; their numbers must not be added or presented as interchangeable portions of one pipeline. No complete-cost gap-sort speedup or comparison with every alternative root backend is claimed.

## Validation and limits

Exact checks cover source/input hashes, projected-root identities, immediate floor/ceiling bounds, complete set equality, sorted-gap order, squarehood agreement, the m=8 family identity and nontrivial factors for all 18 constructive cases. All pass.

The checker was expanded to add complete-cost observations and rerun. The final certificate contains that expanded run; the earlier pilot is not averaged into it. Its repeated arithmetic checks do not create additional unique public positions or independent hit observations. The final command completed in about 4.26 seconds.

The executable accepts only a source-checkout path and an output path; fixed certificate files sit beside it. There is no external target argument, advancing ceiling, adaptive range extension, appended factor-search fallback or automatic ranking update. The five and seven timing rounds are not fed to a ledger as independent discovery attempts.

Companion artifacts:
- experiments/brc_materialized_gap_order_20260908.py
- experiments/brc_materialized_gap_order_20260908.json

The retained outcome is conditional positive evidence for existing specialists, with preparation and predicate costs distinguished. Public-puzzle factoring effectiveness and the larger unfinished research scope remain open.

# LOW12 on prepared public-challenge gaps, with its setup cost retained

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Status: exact filter validation and fixed-input cost evidence; noncanonical research checkpoint.  
Global snapshot: `fca4ad184d83679f38a66ae99763c32abb829ee5`.  
Project parent: `b4dc28c17176fcd2660be9dd5194b06a2499fdac`.

## Selected library entry and exact carrier

The current instruction asks for occasional fast methods to be retained and verified against public RSA mathematical challenges, with computation bounded in advance. This continuation selects the existing `low12_compact_gap_filter` entry from the [opportunistic portfolio](BRC_OPPORTUNISTIC_SHORTCUT_PORTFOLIO_20260907.md). Its role is to reduce square-test cost, not to generate a new factor candidate.

The input is the exact nonnegative completion gap `A=(J+1)²-N`, already stored by the [preceding three-puzzle observation](BRC_PUBLIC_RSA_FIXED_PREDICATES_20260908.md). This is the upward completion distance, distinct from the downward residual `R=N-J²`. N, J and R are not accessed by the timed square-test backends. A alone suffices for the declared future operation, determining whether A is a square and returning its exact root if so.

The public labels, D/U cost directions and an existing `brc_shadow_signature` tag are retained as separate metadata. That tag is not used to order attempts or predict factors. No new challenge integer, multiplier or ceiling position is generated. Replay timings contain three unique public gaps, regardless of their repetition count.

The companion input certificate is pinned to Git blob `e56cfc8457e2398b5de3c90182c2b37824580ef3`; the script verifies this blob before reading it. The literal public integers and source URLs remain in that certificate. The executed portfolio module is Git blob `1214aa09770893fb3de7f85b994d1994ff56bffe`, local SHA-256 `7e186c6b17b4b04c37af875c939a92907e929e8a19b2c0c818d3e3bc5f8b94e7`. The unchanged 4032 comparator's module hash is `f8e178771a25221eaab16002b9ffacd188dc5f39be4948ec2b40ee3e22c9f716`.

Reuse status is `REUSE_EXECUTED` for the LOW12 filter, existing exact filtered-root comparator and shadow-signature API. The exact output wrapper composes the unchanged necessary-condition predicate with native `isqrt` and `root²==A` verification. A filter pass is never treated as a square witness by itself.

## Exact necessary condition and finite table check

The existing cascade uses

\[
4096\ \longrightarrow\ 3465\ \longrightarrow\ 221\ \longrightarrow\ 12673.
\]

The first reduction is `A & 4095`. A later stage is evaluated only after every preceding stage passes. An integer square is a square residue for every modulus, so no exact square is removed.

The packed generator enumerates representatives from zero through `floor(m/2)`. This covers every square residue: x and m-x have equal squares modulo m, and at least one is in that interval. The independent check compares the resulting packed set with `{x² mod m: 0<=x<m}` over each complete small period.

| Modulus | Exact square-residue classes | Packed payload bytes |
|---|---:|---:|
| 4,096 | 684 | 512 |
| 3,465 | 288 | 434 |
| 221 | 63 | 28 |
| 12,673 | 1,800 | 1,585 |
| Total payload | | 2,559 |

These four moduli are pairwise coprime. By CRT, the exact fraction of classes passing the entire cascade over the uniform complete combined period is

\[
\frac{684\cdot288\cdot63\cdot1800}
{4096\cdot3465\cdot221\cdot12673}
=\boxed{\frac{3645}{6485908}\approx0.0561988\%}.
\]

The combined period is 39,749,795,205,120; it is not enumerated. Only the four small component periods are checked. This is a classical residue-count statement and not an estimate of the RSA input distribution. Twenty known-square controls, including zero and squares at the public gap magnitudes, pass all stages and return their exact prescribed roots.

## Public-gap observations

The values come from the RSA Inc-attributed MysteryTwister PDFs already pinned in the parent certificate: [RSA-270](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-09-en.pdf), [RSA-896](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-10-en.pdf), and [RSA-2048](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-38-en.pdf).

| Fixed public gap | Initial direction | Gap bits | Evaluated LOW12 stages |
|---|---|---:|---|
| RSA-270 | U | 444 | `A mod 4096=994`: exit |
| RSA-896 | U | 448 | `A mod 4096=3713`: pass; `A mod 3465=765`: exit |
| RSA-2048 | D | 1,024 | `A mod 4096=372`: exit |

All three exact outputs agree with the parent observations and the independent native root check: none of these gaps is square. These are cheaper evaluations of the same conditions, not three new factorization attempts or new factor hits. The earlier positive families remain retained.

## Warm predicate cost, separated by public value

Three exact backends are compared on the same prepared nonnegative integer: native `isqrt` plus verification; the unchanged `filtered_square_root` with modulus 4032; and the unchanged LOW12 predicate followed by exact verification if it passes. The measured costs include each backend's function/API overhead. Their results agree on the declared integer domain; no claim about equality of validation behavior for other Python object types is needed.

The final run uses CPython 3.14.6 on the host Windows runtime, seven shuffled-order rounds, 512 repeats per backend per round and per fixed gap. These replays estimate warm kernel latency; they are not independent samples or increased coverage.

| Prepared public gap | Native exact, ns | Existing 4032 exact, ns | LOW12 exact, ns | 4032 / LOW12 | Faster LOW12 rounds |
|---|---:|---:|---:|---:|---:|
| RSA-270 / U | 1,282.227 | 917.773 | 400.586 | 2.29x | 6/7 |
| RSA-896 / U | 1,231.641 | 2,157.031 | 932.422 | 2.31x | 6/7 |
| RSA-2048 / D | 2,462.695 | 1,129.883 | 413.867 | 2.73x | 6/7 |

Direction and gap size are confounded in this three-value population, so the table does not assert a universal direction-based speed rule. Raw rounds, including the slower LOW12 rounds, are retained in the certificate.

## Cold setup and retention condition

Each value also receives one isolated cold-cache observation in the local audit process. It includes the lazy tables actually needed before that value exits:

| Public gap | Cold observation, microseconds | Tables constructed |
|---|---:|---:|
| RSA-270 | 421.7 | 1 |
| RSA-896 | 761.8 | 2 |
| RSA-2048 | 421.6 | 1 |

Building all four tables separately takes 2.179 ms in this run, with a raw payload of 2,559 bytes. All four tables are not required for every early exit. Imports, object overhead and input preparation are distinct from the raw payload figure.

Conditionally charging the entire four-table setup against the measured 4032-to-LOW12 per-call difference requires approximately 4,214, 1,780 or 3,044 identical warm calls for the three fixed gaps, respectively. These are replay-based amortization estimates, not new-population predictions. They explain why the table-resident context belongs in the method contract.

Retain LOW12 for prepared gaps when the relevant tables are resident or setup is otherwise amortized. The measured gain applies to the square predicate. The prior cost of obtaining J and A is not reduced by this observation, and no full-pipeline factorization gain is claimed.

## Library coverage record

The source catalog contains 13 entries: four multiplier orderings, one multiplier prefix, two filter backends, three transport backends, one telemetry entry, one storage entry and one metadata entry. They have different input requirements and outputs; they cannot all be counted as independent N-only factor extractors.

This audit executes LOW12 on three pinned prepared gaps and the shadow signature as metadata. The other entries retain their source triggers in the certificate. Candidate-order specialists need a separately defined candidate set and observation budget; transport methods need an appropriate transition stream; storage and Pisano methods need their corresponding representation or existing metadata. They are recorded as unexecuted under this audit's supplied inputs/budget, not as rejected research routes.

## Reproduction and retained frontier

```powershell
python experiments/brc_public_gap_low12_audit_20260908.py --enterprise-root . --output-dir experiments
```

Place the previously committed public-predicate JSON beside the script, as it is in `experiments/`. The input blob guard prevents substitution of other targets. The run validates all four packed residue sets, the exact CRT count, 20 positive controls and the three fixed public gaps, including warm/cold cost records and all 13 catalog descriptors. The full command completed in about one second on this host.

No production source, adaptive ordering or factor-search path is changed. The full thread goal remains active; this checkpoint adds a measured local arithmetic cost benefit on the actual public-challenge data and a precise record of what remains unverified in the larger library.

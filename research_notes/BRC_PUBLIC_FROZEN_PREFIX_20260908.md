# A frozen historical prefix on public RSA mathematical challenge data

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Status: completed bounded mathematical observations and a positive family; no new public square witness.  
Global snapshot: `fca4ad184d83679f38a66ae99763c32abb829ee5`.  
Project parent: `33bb079035409809399f44bbcbd126e3a6ddaf02`.

## Frozen question and budget

The current user instruction is to retain occasional fast successes and verify existing shortcuts against public RSA challenges, with no large computation or route rejection based on non-hits. This checkpoint tests the historical learned prefix already stored in the [opportunistic portfolio](BRC_OPPORTUNISTIC_SHORTCUT_PORTFOLIO_20260907.md):

```text
1,48,96,8,15,80,21,16,56,45,35,3,72,7,99,88,40,55,9,24
```

The list predates these public observations and is not fitted to their outcomes. All 20 entries are distinct and satisfy the existing static odd-N representative predicate. The original order is retained. Its first entry, m=1, has already been checked for each public integer; those three results are consumed from the pinned parent certificate.

The new budget is exactly 19 primary API calls per public integer, with an independent exact audit of each same position. There is no advancing ceiling, enlarged prefix, automatic choice of another strategy, timing repetition or appended scan-complete fallback. This tests the finite prefix only. The catalog's complete fallback coverage is not claimed under this budget.

Inputs are the same literal RSA-270, RSA-896 and RSA-2048 mathematical challenge integers from the RSA Inc-attributed MysteryTwister PDFs. The [parent certificate](../experiments/brc_public_rsa_fixed_predicates_20260908.json) is verified against Git blob `e56cfc8457e2398b5de3c90182c2b37824580ef3` before any observation. It preserves each source URL, decimal integer and decimal hash; other inputs are not accepted.

## Exact source reuse

The unchanged `LEARNED_COVER_PREFIX` supplies the sequence. The unchanged `odd_n_multiplier_is_scan_irredundant` checks its entries. The unchanged `ceiling_completion_square_witness(N,m)` evaluates each prescribed position. The helper that appends the complete structural fallback is not invoked.

Verified local source SHA-256 values:

- `brc_opportunistic_shortcuts.py`: `7e186c6b17b4b04c37af875c939a92907e929e8a19b2c0c818d3e3bc5f8b94e7`;
- `brc_multiplier_priority_jump.py`: `ee4a01822ff9e5e33b602b5e834a6902dbd848d0258b981503cea3df513d1a0d`;
- `brc_square_gap_prefilter.py`: `f8e178771a25221eaab16002b9ffacd188dc5f39be4948ec2b40ee3e22c9f716`.

The priority source is Git blob `f78379664b074b7f40879d4f24af94b48df8fc3b` at the pinned project parent. Reuse is `REUSE_EXECUTED` for the static representative check and the witness interface, and `REUSE_APPLIED` for the frozen catalog order. No hidden factors or S enter a public observation.

## A certified success family inside the prefix

The fourth prefix entry is m=8. For every odd integer t>=3, let

\[
\boxed{N=t(2t+1).}
\]

Then

\[
\boxed{8N=(4t+1)^2-1.}
\]

Thus the m=8 immediate-completion witness is `(x,b)=(4t+1,1)`. Its factor readout is nontrivial:

\[
\gcd(N,x-b)=\gcd(t(2t+1),4t)=t,
\]

because `2t+1` is odd and coprime to four. The other factor is `2t+1`. This gives an infinite family of positive integer constructions reached no later than prefix slot four. It does not assert infinitely many prime pairs or measure the first-hit rank on an unknown population.

The multiplied BRC state is particularly simple:

\[
J_8=4t,\qquad R_8=8t=2J_8,\qquad A_8=1.
\]

Every member therefore lands in the upper-cost-cheaper U state, one unit below the next square, even though its original N may have a different cost direction. Canonical collapse remains downward. This is a positive law for a specified transformed-state slice.

The fixed controls use odd t from 3 through 31. All 15 constructions produce the exact unchanged API witness and the prescribed proper factor. Five have both factors certified prime: t=3,5,11,23,29. One example is `253=11*23`, with `8*253=45²-1`. These intentionally constructed successes are not a public-RSA hit-rate estimate.

## Public observations and separate state accounting

For each new position define

\[
J_m=\lfloor\sqrt{mN}\rfloor,\quad R_m=mN-J_m^2,
\quad A_m=\lceil\sqrt{mN}\rceil^2-mN.
\]

The independent audit uses exact native square roots and verifies agreement with the existing API at the same position. The certificate retains the multiplier, prefix slot, exact gap and transformed D/U/Z state. Original N's direction is stored separately.

| Public integer | Original direction | Reused positions | New positions | New D / U states | New witnesses |
|---|---|---:|---:|---:|---:|
| [RSA-270](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-09-en.pdf) | U | 1 | 19 | 5 / 14 | 0 |
| [RSA-896](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-10-en.pdf) | U | 1 | 19 | 7 / 12 | 0 |
| [RSA-2048](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-38-en.pdf) | D | 1 | 19 | 9 / 10 | 0 |

All 57 new API outputs agree with their independent exact audits. The three cached m=1 outputs complete the fixed 20-position record for each input. No square witness or factor was recovered on these public inputs. No larger candidate set was launched afterward. The non-hits describe this finite observation budget; the positive m=8 family and the earlier local specialists remain retained.

## Single-pass costs

The host is CPython 3.14.6 on Windows. There is one pass per public integer, with the small positive controls outside the public timers.

| Public integer | Sum of 19 existing API calls, ms | New-position loop including exact audits, ms |
|---|---:|---:|
| RSA-270 | 7.1715 | 7.3023 |
| RSA-896 | 8.0957 | 8.2506 |
| RSA-2048 | 39.3672 | 39.6586 |
| Total | 54.6344 | 55.2115 |

The loop timer includes the new-position API calls, independent audits and evaluation-record construction. Imports, source/input checks, parsing, constructive controls and final serialization are outside it. The unchanged API's current validation and generic root implementation are included in its time. Reused m=1 positions receive no new elapsed-time value. The complete command finished in about 0.97 seconds on this host.

These are descriptive single-pass costs. They do not establish a stable performance ratio, optimal candidate order, first-hit production time or general factorization effectiveness. All selected positions are checked for the finite audit; no production router is modified.

## Reproduction and retained frontier

```powershell
python experiments/brc_public_frozen_prefix_20260908.py --enterprise-root . --output-dir experiments
```

The pinned parent public-predicate JSON must be beside the script, as it is in `experiments/`. The new certificate contains the exact frozen sequence, operation budget, 15 positive controls, all 60 cached/new position records, per-input costs and per-state counts.

This adds an executed finite-prefix check to the catalog coverage record. It does not replay the earlier LOW12 benchmark, discard non-universal methods, or declare the whole library complete. The full user goal remains active.

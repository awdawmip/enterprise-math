# R030 Context-Budget Pareto

Status: `RESEARCH / NOT CANONICAL`

Researcher-ID: `EM-R030-CX8F42`  
Task: `RS-R030-RESEARCH-CONTEXT-COMPILER-METATOOL-INJECTION-BACKTEST`

## Measurement boundary

The historical gold has 23 critical distinctions across R017/R020/R022/R023/R023I/R024/R025/R028. It is intentionally **not** an exhaustive list of every legitimate task obligation. Therefore:

- `Critical Tool Recall` = post-hoc critical distinctions covered / 23.
- `Critical Tool Precision` = selected tools named by the strict critical gold / all selected tools. This is a conservative **gold-hit-density lower bound**, because legitimate exact guards such as prior-art rooting or bounded-minimality may be task-required without being a gold row.
- `Structural Overload` = selected tools removable while all structured required capabilities remain covered. This is a stronger overload diagnostic than simply counting tools absent from the critical gold.
- `Diagnostic Wrong-Route Risk` = summed false-positive cost of injected DIAGNOSTIC/SUGGESTED tools.
- context tokens are estimates for the generated human startup pack, not model billing measurements.

## Strategy sweep

| Strategy | Critical recall | Strict gold precision | Tools | Tool-token estimate | Mean human-pack tokens/task | Structural overload | Diagnostic wrong-route risk |
|---|---:|---:|---:|---:|---:|---:|---:|
| `MINIMUM_CRITICAL_COVER` | 1.000 | 0.535 | 43 | 3,706 | 1,098 | 0 | 0 |
| `TOP_K(k=1)` | 1.000 | 0.354 | 65 | 5,629 | 1,257 | 25 | 16 |
| `TOP_K(k=2)` | 1.000 | 0.329 | 70 | 6,034 | 1,302 | 30 | 26 |
| `TOP_K(k=3)` | 1.000 | 0.315 | 73 | 6,268 | 1,327 | 33 | 32 |
| `TOP_K(k=5)` | 1.000 | 0.299 | 77 | 6,664 | 1,352 | 37 | 41 |
| `TOP_K(k=8)` | 1.000 | 0.299 | 77 | 6,664 | 1,352 | 37 | 41 |
| `ALL_MATCHES` | 1.000 | 0.299 | 77 | 6,664 | 1,353 | 37 | 41 |

`MINIMUM_CRITICAL_COVER` is the unique nondominated point under the frozen objective: maximize recall/recovered-late rate/strict gold precision while minimizing injected tool tokens, structural overload, and diagnostic wrong-route risk.

## Cold-start proxy

Original startup taskbooks explicitly contained 19 of the 23 post-hoc gold distinctions. Four were genuinely late relative to the frozen startup context:

1. R023I: a successful build claim must actually cover the new module.
2. R023I: source provenance is not compiler/root-coverage evidence.
3. R025: a numerical `2^p` threshold does not eliminate aligned islands; regime classification must cross threshold with alignment structure.
4. R025: zero/degenerate root-index regimes must be attacked before blanket binary-doubling claims.

The MCC pack selects the relevant **reasoning guards** for all four without inserting those post-hoc conclusions as facts. Thus the cold-start proxy changes from `19/23 = 82.6%` explicit startup availability to `23/23 = 100%` tool coverage, a `+4 distinctions / +17.4 percentage-point` availability lift. This is not a claim about human-hours saved.

## Why ALL_MATCHES is killed

`ALL_MATCHES` buys no additional critical recall or late recovery over MCC. It adds 34 tools and about 2,958 estimated tool tokens across the eight replays, plus 37 structurally redundant selections and diagnostic wrong-route risk 41. Hence:

`MORE_CONTEXT_ALWAYS_IMPROVES_RESEARCH = KILLED_IN_R030_BACKTEST`

and

`A_HIGH_RECALL_PACK_IS_GOOD_EVEN_IF_NOISY = KILLED_IN_R030_BACKTEST`.

## Frozen recommendation

Use `MINIMUM_CRITICAL_COVER` as the default production candidate. Permit `TOP_K` only as an opt-in exploratory diagnostic mode. Never use `ALL_MATCHES` as the default startup context.

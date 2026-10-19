# RSA-270：第 8 轮——组合（筛 × 代价）全方向优化表与真实最优

Progress-Event-ID: `rsa270-round8-combined-strategy-table-5b8f1a`
At: `2026-09-06T20:55+08:00`
Scope: `enterprise-math / RSA-270 / cost-field line closure (combined sieve x cost optimization)`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 9d4c2e; P000 assumed`
Kind: `PROGRESS / QUANTIFIED NO-GO / LINE CLOSURE`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Round 8: complete per-direction combined strategy (add-cost × mod-72 j-sieve) over the construction-family band. No factor obtained.

### Combined strategy table (budget = 2^(447.5) * c_max * |x* residues mod 72| / 72)

18 band directions, ranked by combined budget bits:

`(2,1) 438.00 ; (11,5) 439.27 ; (13,7) 439.52 ; (15,7) 439.95 ; (9,5) 440.01 ; (17,9) 440.22 ; (17,8) 440.43 ; (19,10) 440.70 ; (19,9) 441.07 ; (21,11) 441.34 ; (20,11) 441.45 ; (9,4) 441.83 ; (13,6) 441.90 ; (11,6) 442.05 ; (21,10) 442.13 ; (15,8) 442.16 ; (20,9) 442.84 ; (16,9) 443.01`

### Result

- **True optimum: direction `(2,1)` with combined budget `~2^438.00` add-steps** — the sieve does not change the ranking (un-sieved minimax was 2^440.6); `(2,1)` dominates because its band-max coefficient (0.0083) beats every other direction's sieve advantage.
- The multiplier-branch cost-field line is now **closed quantitatively**: no (a,b)-branch strategy under the prior band and the forced lattice can beat ~2^438 add-steps, which is infeasible by ~10^90×.

## Artifacts

- Script: `rsa270_round8.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-06/20260906T202000+0800-rsa270-round7-minimax-j-sieve-9d4c2e.md`.

## Next

All currently known shortcut families are closed with quantitative bounds: ladder/observable families (dichotomy 8e5f2a), multiplier cost field (this round), geometric reformulations (7e3b5d). Without a new observable class or external input, the blocking condition persists; this is the second consecutive round since the last resume.

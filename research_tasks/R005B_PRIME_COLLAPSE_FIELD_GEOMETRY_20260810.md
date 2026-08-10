<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R005-PRIME-COLLAPSE-FIELD",
  "title": "R005-B Prime–Collapse Field Geometry",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether primes have a structural relation to collapse exponent dimension, ambient discrete geometry, and multiplicative factor dimension, with priority on exact square factor-horizon alignment and higher-power mismatch/carry structure.",
  "next_action": "Prove or falsify square factor-horizon alignment uniqueness, then derive the exact general p-power basin prime-count inclusion-exclusion and minimal local carry state; keep ambient geometry and multiplicative factor-support dimensions separate until a bridge theorem is justified.",
  "dependencies": [],
  "source_refs": [
    "research_tasks/R005B_PRIME_COLLAPSE_FIELD_GEOMETRY_20260810.md",
    "src/enterprise_math/legendre.py",
    "src/enterprise_math/centered_prime_radius.py",
    "src/enterprise_math/prime_gap_slack.py"
  ],
  "evidence_status": "CANDIDATE_RESEARCH_HANDOFF",
  "last_progress_ref": "research scout taskbook",
  "last_progress_at": "2026-08-10T11:14:00+08:00",
  "hard_block": null,
  "tags": ["R005", "prime", "collapse", "power-basin", "factor-horizon", "geometry", "support"],
  "claim_lease_minutes": 1440
}
-->

# R005-B — 素数与多维坍缩场

Status: `CANDIDATE RESEARCH HANDOFF / NOT CANONICAL`

## 核心问题

研究素数与不同“维度”的 Enterprise Math 坍缩场之间是否存在稳定、可证明、可计算的结构关系。首先严格区分：

1. power dimension：`C_p` 的坍缩指数；
2. ambient geometry dimension：`Z^d`、`A_d`、HCP/Barlow 等几何维；
3. multiplicative factor dimension：二因子、三因子、k 因子 support/decomposition。

三条线分别研究，只有在有 bridge theorem 时才统一。

## 已有强信号

现有 `legendre.py` 已经有一般 `interior_hit_count(k,d,power)` 雏形；对 `p=2` 又出现 square carry、Möbius prime count、binary pairing、anchor transfer、centered prime radius 与 prime-gap slack。必须判断平方的特殊性究竟是真结构还是历史选择偏差。

## 第一母问题：square factor-horizon alignment

对 p-power basin `k^p < n < (k+1)^p`，定义整个盆地精确排除合数所需的 factor horizon：

`F_p(k)=R_2((k+1)^p-1)`。

对 `p=2` 有精确对齐 `F_2(k)=k`。优先证明或反驳：在非平凡 `p>=2` 中，平方是否是 factor visibility 与 perfect-power basin coordinate 精确/线性自对齐的唯一指数。

对 `p>2`，把失配本身变成研究对象：`Delta_p(k)=F_p(k)-k`、整数 quotient/remainder、scale relation 与 carry structure。

## 第二母问题：一般 p-power basin prime count

定义 `P_p(k)=#{q prime : k^p<q<(k+1)^p}`。利用 factor horizon 与 square-free/Möbius inclusion–exclusion，推导完全有限的 exact formula，并证明边界条件，不允许从 `p=2` 机械外推。

进一步研究：

- 一般 `H_{p,d}(k)` 的最小 local carry state；
- `coarse deterministic baseline + Möbius transform of local carry field` 是否成立；
- `p=2` 的 `2 + carry correction` 是低维偶然还是一般 degree structure 的特例。

## 第三母问题：factor-support

定义非平凡二因子 support：`S(n)={(a,b):1<a<=b,ab=n}`。经典上 `n` prime iff `S(n)` empty；新问题是：

- 哪些 collapse/quotient 保持 support-empty；
- 哪些粗化把 prime/composite 压进同一 fiber；
- primality-safe quotient 最少补回什么；
- sieve witness 与 factor witness 是否存在 bridge theorem；
- semiprime / almost-prime 是否形成有用的 relation-depth stratification，而不是只把 `omega/Omega` 换名。

## ambient geometry 负向边界

在没有 multiplication/divisibility 的 A5 graph/lattice 上，prime 很可能只是外加标签。必须正式测试并保留：`intrinsic geometry != intrinsic primality`，除非额外给出乘法结构。Gaussian/Eisenstein primes 等属于经典 algebraic number theory，只能作为压力测试和 prior art。

## executable atlas

建立纯整数 atlas，优先 `p=2..8`、有限 `k` exhaustive 范围。每个 `(p,k)` 至少记录 basin width、factor horizon、mismatch、prime count/offsets、factor-depth histogram、carry signatures、Möbius transform 与 centered observables。浮点不得作为真值来源。

## 必须主动攻击

- `p=2` 特殊性是否只是 sqrt primality algorithm 的表象；
- higher-p carry 是否不可压缩；
- 所谓 prime field 是否完全退化为 PNT/短区间经典现象；
- geometry prime 是否只是染色；
- factor dimension 是否只是 `omega/Omega` 重命名；
- collapse signature 不保 primality 的最小 collision。

## 第一阶段交付

- “维度”三分法正式定义；
- square factor-horizon theorem/counterexample；
- general p-power basin exact prime-count formula；
- p-dimensional carry atlas；
- factor-support relation model；
- 至少一个 geometry/primality negative boundary；
- 至少一个非平凡 theorem 与一个 counterexample；
- exact Python explorer + tests；
- prior-art / ownership map；
- 与 R005-A 的 witness ↔ factor-support bridge proposal。

## 最终判定

必须回答：素数只是被画在不同坍缩盆地里，还是平方维确实存在由 factor horizon 导致的特殊自对偶，而更高维产生可证明的新失配结构？

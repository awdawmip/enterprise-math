# 半素数平方壳中点—边界—邻近素数分解广域探索：研究返回

Task: `RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION`
Publication: `TP2-12778A2D48A1D5A57BA9`
Researcher-ID: `EM-SSMF1-7D31C8`
Claim: `chatgpt-ssmf1-20260829-1241-7d31c8`
Execution base: `949a8eb7ba92b1d9de8a4ad5e494596b1a1077e3`

## Frozen verdict

`SUCCESS / STRUCTURAL_ONLY / NO_GENERAL_SHELL-ONLY_FACTOR_SEARCH_REDUCTION_ESTABLISHED`

平方壳与 Fermat 分解存在精确结构桥梁，但本轮没有得到一个超出 Fermat / Lehman / Hart 类近平方路线的 factor-blind 通用搜索收缩规则。

## Exact results

对 `N=pq`, `A=(p+q)/2`, `B=(q-p)/2`, `A0=ceil(sqrt(N))`, `T=A-A0`, `b=A0^2-N`：

`B^2=b+2*A0*T+T^2`.

令 `x=sqrt(N)`, `rho=q/p>=1`, `eta=(1/2)log(rho)`，则

`A/x=cosh(eta)`, `B/x=sinh(eta)`,
`A-x=x(cosh(eta)-1)=B^2/(A+x)=(sqrt(q)-sqrt(p))^2/2`.

因此 Fermat midpoint 主位移由隐藏因子比 `q/p` 决定，取整只贡献小于 1 的修正。

令 `ell=PrevPrime(x)`, `u=NextPrime(x)`, `g=u-ell`, `c=(ell+u)/2`，则

`|c-x|<g/2`,
`A-c=(A-x)+(x-c)`,

所以邻近素数中心只能加入 local-prime-gap 尺度修正，不能消掉失衡因子的主位移。

若 `p<q` 本身是连续素数，则精确有 `PrevPrime(sqrt(N))=p`, `NextPrime(sqrt(N))=q`。由 Bertrand `q<2p`，连续 Fermat 主位移与 `sqrt(N)-p` 的比值小于 `(sqrt(2)-1)/2≈0.2071`；该特殊边界族是结构定理，不是免费加速。

## Multi-k bridge

对任意 `k=ab`：

`(ap+bq)^2-(ap-bq)^2=4kN`,
`ap+bq-2*sqrt(kN)=(sqrt(ap)-sqrt(bq))^2`.

所以 productive multiplier 的核心是小有理数 `a/b` 对隐藏 `q/p` 的逼近。令 `c_k=ceil(sqrt(4kN))`, `b_k=c_k^2-4kN`，则 `b_k` 主要记录 rounding phase，不能单独可靠预测真正好的 `k`。

精确反例：

`N=9,171,667=2,851*3,217`, `k=56=7*8`。

`ceil(sqrt(4*56*N))=7q+8p=45,327`,
`b_56=(7q-8p)^2=289^2=83,521`.

因此 `T_56=0`，第一个 midpoint 就分解成功；但在 `k=1..64` 中，按 raw `b_k` 从小到大排，`k=56` 为 `64/64`；按 `b_k/(2c_k)` 排仍为 `62/64`。故“优先测试离下一平方最近的 multiplier”被精确反例否定为一般 selector。

## Modular sieve

对奇素数 `ell` 且 `ell∤N`，满足 `A^2-N` 为二次剩余（含 0）的 `A mod ell` 数量精确为：
- 若 `N` 为二次剩余：`(ell+1)/2`;
- 若 `N` 为非二次剩余：`(ell-1)/2`;
- 若 `ell|N`：全部 `ell` 个剩余类通过。

checker 对 `ell=3,5,7,11,13,17,19,23,29,31` 全非零 `N mod ell` 完整复核。wheel `(64,3,5,7,11,13)` 在全量 census 上平均保留 `0.0082359415221505`，约 `0.824%` midpoint residues（约 121× 少做 full square test），但这是标准 quadratic-residue Fermat sieve 的壳坐标重写。

## Exhaustive census: N <= 10^7

全部不同奇半素数 `p<q`, `pq<=10^7`：`1,555,366`。

| q/p | n | T median | T P90 | J_p median | J_p P90 | T<=J_p+1 |
|---|---:|---:|---:|---:|---:|---:|
| <=1.01 | 699 | 0 | 0 | 0 | 1 | 100% |
| 1.01-1.1 | 7,202 | 0 | 2 | 6 | 12 | 100% |
| 1.1-2 | 51,701 | 33 | 111 | 42 | 84 | 65.836% |
| 2-10 | 140,169 | 524 | 1,425 | 136 | 221 | 0.0735% |
| >10 | 1,355,595 | 86,288 | 833,952 | 306 | 415 | 0% |

连续素数因子对 `445`，且 `both_local_neighbors=445`。局部 prime-center 相对 Fermat 起点：改善 `572,472`，恶化 `781,497`，相等 `201,397`；不是单调改进。最大 `|c-A0|=17`，而同一 census 最大真实 `T=1,663,504`。

## Multi-k reservoir and holdout

只取 `p>64`, 测 `1<=k<=64`，避免 `gcd(k,N)` 平凡泄漏。

`N<=10^7` reservoir 中，raw residual 排序下 oracle 最佳 k 的中位 rank / Top-10：
- `<=1.01`: `1 / 100%`
- `1.01-1.1`: `6 / 79.2%`
- `1.1-2`: `14 / 42.4%`
- `2-10`: `14 / 41.8%`
- `>10`: `36 / 18.1%`

24/32/40/48/64-bit 独立 holdout 共 `1,000` 个半素数，raw residual 最佳-k 中位 rank / Top-10：
- `<=1.01`: `1 / 88.5%`
- `1.01-1.1`: `7 / 70.5%`
- `1.1-2`: `15 / 39.0%`
- `2-10`: `13 / 46.0%`
- `>10`: `39 / 20.0%`

简单 shell phase `b/L` 对 `log(q/p)` 的 Spearman 在 24/32/40/48/64 bit 分别为 `0.516,0.324,0.197,0.298,0.229`，不稳定，不升格为 factor-ratio predictor。

## Negative controls

固定 `N<=10^7`, `k<=64`：
- 2,000 primes：nontrivial immediate multi-k hit = `0`;
- 2,000 three-prime composites：`1,885`;
- 2,000 random odds：`1,619`.

说明 immediate difference-of-squares hit 不是半素数专属签名。

## Prior-art boundary

- Fermat：`b=A0^2-N` 是初始残差；quadratic-residue wheel 是标准 Fermat sieve。
- Lehman：系统搜索 `x^2-y^2=4kN`；`k=ab` 与小分数 `a/b` 的结构与本轮 multiplier identity 对齐。
- Hart：其 one-line factoring algorithm 明确是 Fermat 的 multiplier variant；本轮 raw shell-residual ordering 没有形成一个稳定的新 selector。

因此本轮分类为 `STRUCTURAL_ONLY`，不主张新分解算法或复杂度改进。

## Information boundary and residue

`(L,D)` 可逆确定 `N`，固定 `k` 的 `D(kN)` 也由 `N,k` 决定；潜在收益只能来自计算/搜索顺序，而不是额外信息。

最小未解残差：

> 是否存在只由 `N` 可计算、且成本显著低于分解本身的 feature，能稳定估计隐藏 `q/p` 的小有理近似 `a/b`，从而在 Lehman/Hart 型 `k=ab` 搜索中提前选出 productive multipliers？

若后续没有新的 ratio-approximation feature、复杂度论证或新的结构来源，仅扩大同类 census 不构成有价值 successor。

## Replay

`python scripts/check_semiprime_square_shell_midpoint_boundary_factorization.py --limit 10000000 --reservoir 1000 --kmax 64 --holdout-per-cell 40`

Expected terminal:
`SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_CHECK=PASS`

Auxiliary negative controls:
`python research_artifacts/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION/negative_controls_20260829.py`

Expected terminal:
`SEMIPRIME_SHELL_NEGATIVE_CONTROLS=PASS`

No Working Truth, Foundation mutation, novelty claim, canonical promotion, or automatic merge is requested. Driver review is required.

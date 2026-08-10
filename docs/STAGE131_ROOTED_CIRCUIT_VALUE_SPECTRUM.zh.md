# Stage131 — Rooted-Circuit Materialization Value Spectrum

状态：`RESEARCH BRIDGE / NONCANONICAL`

修正版 rooted-circuit explosion theorem 已回答“one-round minimal premises 有多少”。selective materialization 还需要一个新的 value coordinate：若不缓存该 circuit，只靠 compositional local Horn basis，从它的 premise set 到 root 原本需要几轮？

这个 base derivation depth 就是 circuit 的直接 execution value。

## 1. Rooted-circuit premise 的 base depth

对 root 的 inclusion-minimal premise set P，定义：

`d(P)`

为 local Horn basis 从 P derive root 的最早 synchronous round。

若 exact rooted-circuit rule

`P=>root`

被 materialize，则这个 exact query 变成1轮。

因此直接 round saving 是：

`d(P)-1`。

同一个 premise width 可以对应不同 base depth；同一个 base depth 也可以包含很多 widths。所以 width 与 execution value 是独立 coordinates。

## 2. Joint width/depth recurrence

令 `A_h(m,d)` 统计让 height-h node available 的 minimal ways，同时记录 premise width m 与 base derivation depth d，并允许 node 自己作为 direct seed。

height0：

`A_0(1,0)=1`。

每个 internal node：

- direct node seed 贡献 `(1,0)`；
- 左右 child 各选择一个 minimal availability set 后：

`m=m_left+m_right`，

`d=1+max(d_left,d_right)`。

rooted-circuit spectrum 只取 derived part，排除 direct root seed `(1,0)`。

这就是修正后 `A_h(z)=z+A_(h-1)(z)^2` 的 width/depth refinement。

## 3. Correct height-3 joint spectrum

height3 的 exact nonzero `(width,depth):count`：

- `(2,1):1`；
- `(3,2):2`；
- `(4,2):1`；
- `(4,3):4`；
- `(5,3):6`；
- `(6,3):6`；
- `(7,3):4`；
- `(8,3):1`。

width marginal 因而正好是修正后的：

`z^2+2z^3+5z^4+6z^5+6z^6+4z^7+z^8`。

## 4. Cumulative depth count 与 host height 无关

固定 host tree height h 和 depth threshold d<=h。

一个 root premise 若能在 d 轮内 derive root，那么 recursive Horn composition 最多向下展开 d 层；再往下的 subtree roots 必须已经作为 seeds 出现。

因此这部分 combinatorics 与一个 standalone height-d tree 的完整 rooted-circuit table 完全相同。

所以：

`# {P : d(P)<=d} = M_d`，

只要 h>=d，就与 host height 无关。

executable layer 对多组 heights/depths 用 joint recurrence 交叉验证。

## 5. Exact depth-d circuit count

令 `M_0=0`，则：

`N_d=# {P:d(P)=d}=M_d-M_(d-1)`。

前几项：

- d1：1；
- d2：3；
- d3：21；
- d4：651；
- d5：457653；
- ……

explosion 几乎全部集中在最深的 materialization class。

## 6. Height-5 opportunity distribution

height5 root 一共有458329个 circuits。

depth counts：

`1,3,21,651,457653`。

其中 depth5 class 单独占：

`457653/458329 > 0.99`。

这类每一个 circuit 若被 materialize，都能把 local basis 下原来5轮的 root derivation 直接变成1轮，节省4轮。

所以 complete rooted-circuit storage 的主体，恰好也是潜在 speedup 最大的一大群 candidates。

## 7. Exact base depth 下的 width support

对每个 d>=1，exact base depth=d 的 rooted circuits 会覆盖每一种 width：

`d+1, d+2, ..., 2^d`。

同样只要 h>=d，就与 host height 无关。

例如：

- depth1：只有 width2；
- depth2：width3..4；
- depth3：width4..8；
- depth5：width6..32。

所以高 value depth class 内部仍然存在很宽的 storage/fan-in spectrum。

## 8. 为什么 minimum width 是 d+1

要真正需要 d 轮，至少一个 child subtree 必须需要 d-1 轮；另一侧仍至少贡献一个 seed atom。

归纳得到 minimum width：

`d+1`。

## 9. 为什么 maximum width 是 2^d

d-round derivation 最多向下展开 d 层 binary Horn composition。完整 depth-d leaf frontier 恰有 `2^d` 个 premises，因此达到最大 width。

在“直接 internal-node seed”与“继续展开 subtree”之间混合，就能实现中间的每一种 width。

## 10. Materialization value 不按 width 单调

只按 premise narrowness 给 circuits 排名是不够的。

例如 depth5 circuits 从 width6 到 width32 全部存在；若 exact premise query 出现，它们都节省4轮。

反过来，一个很宽但 base depth 更浅的 circuit，可能反而只节省1或2轮。

所以 selective caching 至少要同时看：

`premise width x base depth x workload frequency`。

## 11. Candidate-level value model

若 circuit premise P 的 workload/query frequency 是 `f(P)`，最简单的 independent root-query gross benefit 是：

`f(P)*(d(P)-1)`。

storage cost 可以按不同 contract 计算：

- 一条 rule；
- premise width `|P|`；
- premise-literal matching cost；
- hardware-specific fan-in cost。

这是 candidate score 的第一层，但还不是 global optimizer，因为多个 materialized circuits 在 reusable closure 中会发生 interaction。

## 12. 为什么 complete materialization 通常不合理

height5 只有32 leaves、31条 local basis rules，却已经有458329个 root circuits，而且超过99%都在 deepest high-saving class。

因此即使只保“高 saving circuits”，storage 仍然会立即爆炸。

value spectrum 告诉我们机会在哪里，也同时证明 selective compilation 是必须的。

## 13. 下一步 selective circuit compiler

新的 exact optimization problem 可以写成：

在以下 constraints 下选择 rooted-circuit macro subset：

- total rules；
- total premise literals；
- maximum fan-in；
- workload frequency；
- answer depth；
- reusable full-closure depth。

如果只考虑 independent one-shot root queries，它首先类似 knapsack；如果要求 reusable closure，circuits 会 interaction，objective 不再可加，需要 literal derivation simulation 或 proof-DAG structure。

## 14. Stage131 interpretation

complete rooted-circuit table 是“把所有 minimal premise alternatives 都缓存为 one-round rule”的 maximal presentation。

width/depth spectrum 把这个单一巨表拆成 opportunity distribution：

- 有些 circuit cheap 但几乎不省 rounds；
- 有些 narrow 却能省很多 rounds；
- deepest class 数量巨大、speedup 也大，但 aggregate storage 无法承受。

这才是 selective materialization 的正确输入，而不是对 rooted circuits 做 blanket acceptance 或 blanket deletion。

## Owner-local assets

- `stage131_rooted_circuit_value_spectrum.py`；
- 修正后的 width/depth spectrum tests；
- `STAGE131_ROOTED_CIRCUIT_VALUE_SPECTRUM.{en,zh}.md`。

## Prior art / status

Horn proof depth、minimal generators 与 generating-function refinement 都是标准既有数学/CS。Enterprise Math 的项目价值是 Stage131 materialization-value 解释，以及 exact host-height-invariant depth spectrum。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。
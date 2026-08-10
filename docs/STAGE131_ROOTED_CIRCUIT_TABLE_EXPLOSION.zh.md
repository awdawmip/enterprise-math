# Stage131 — Binary AND Tree 的 Rooted-Circuit Table Explosion（修正版 v2）

状态：`RESEARCH BRIDGE / NONCANONICAL`

本 v2 replay 修正被 supersede 的 WIP 中手工抄写错误的 height-3 width histogram 与 premise-literal totals。生成递推、circuit 总数递推与 exponential separation theorem 均未改变。

## 1. Compositional basis 与 one-round premise table

height-h balanced binary AND tree 有 `L=2^h` 个 leaves，却只有 `L-1` 条 local binary Horn rules。

对一个 root，完整 rooted-circuit table 则枚举所有 inclusion-minimal seed set P（不含 root 本身），使 local closure 能从 P 推出 root。

两者表示同一个 closure law，却承担不同 presentation contract：

- local basis：保存 recursive composition；
- rooted-circuit table：保存所有 minimal one-round premise alternatives。

## 2. Exact generating recurrence

令 `A_h(z)` 统计让 height-h node available 的 minimal ways，并允许 node 自己作为一个 atom seed：

`A_0(z)=z`，

`A_h(z)=z+A_(h-1)(z)^2`。

rooted-circuit width polynomial 去掉 direct root seed：

`P_h(z)=A_(h-1)(z)^2=A_h(z)-z`。

`[z^m]P_h` 精确等于 width-m inclusion-minimal root premises 数量。

## 3. Correct small width polynomials

`P_1(z)=z^2`。

`P_2(z)=z^2+2z^3+z^4`。

正确的 height-3 polynomial 是：

`P_3(z)=z^2+2z^3+5z^4+6z^5+6z^6+4z^7+z^8`。

coefficients 总和25。height4 以内的 explicit premise-set enumeration 与 polynomial 完全一致。

## 4. Exact circuit-count recurrence

令 `M_h=P_h(1)`，则：

`M_1=1`，

`M_h=(1+M_(h-1))^2`。

前几项：

`1, 4, 25, 676, 458329, 210066388900, ...`。

这组总数不受本次 width histogram 修正影响。

## 5. 每一种 premise width 都出现

归纳地，`A_(h-1)` 在 degrees `1,...,2^(h-1)` 上全部为正；平方后就覆盖：

`2,...,2^h`。

所以同一个 root 从 width2 到全部 leaves 的每一种 width 都存在 minimal premise。

## 6. 与 local basis 的 exponential separation

写 `L=2^h`。对 h>=2：

`2^(L/2) <= M_h < 2^(L-1)`。

因此 root circuit table 对 leaf count 呈 exponential growth，而 compositional local basis 只有 `L-1` rules。

## 7. 全部 internal rooted-circuit rules

height-h tree 中 height-t nodes 有 `2^(h-t)` 个，因此完整 internal circuit table：

`C_h=sum_(t=1)^h 2^(h-t) M_t`。

exact examples：

- h=3：37 circuits vs 7 basis rules；
- h=4：750 vs 15；
- h=5：459829 vs 31；
- h=6：210067308558 vs 63。

## 8. Correct premise-literal totals

root 的 total premise-literal storage 是：

`P_h'(1)`。

正确值：

- h=1：2；
- h=2：12；
- h=3：130；
- h=4：6812；
- h=5：9224802。

h=5 时 root 有458329个 circuits，average premise width 为：

`9224802/458329`，约20.13，

width 覆盖2..32。

## 9. Squaring explosion 为什么出现

对每个 child subtree，一个 minimal root premise 可以：

- 直接包含 child atom；
- 或用任何一个能 derive child 的 minimal premise 替代 child。

左右 subtree choices 独立组合，因此出现平方递推。

rooted-circuit enumeration 会把 recursive composition 全部展开为 one-round minimal alternatives。

## 10. Stage131 consequence

这比 unary transitive redundancy 更强：

> 即使 closure law 只是 tree-shaped，one-round minimal-premise table 也可以比 compositional semantic basis 指数级更大。

同时它又是 execution resource：每个 stored circuit 都为那个 exact premise set 提供 one-round access。

真正的 operational 问题应转向 selective materialization：在 premise width、storage、depth、workload 与 continuation contract 下，哪些 minimal-premise macros 值得缓存？

## 11. Ownership / prior art

Horn closure、minimal generators、antichain enumeration 与 generating function 都是标准既有数学/CS。Enterprise Math 的项目价值是 Stage131 presentation 解释与 balanced AND-tree exact pressure test。

Owner-local assets：

- `stage131_rooted_circuit_table_explosion.py`；
- 修正后的 recurrence / width / enumeration / storage tests；
- 本 bilingual v2 note。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。
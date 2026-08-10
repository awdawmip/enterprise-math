# R004 精度起源——补充 16：结构性 obstruction clutter 与 Carrier Basis 对偶

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_REDUCTION + P023_BOUNDARY`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_15.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 15 已经把 carrier-minimal generator selection 归约为“命中所有 forbidden coarse partitions”。剩下的开放问题是：Bell-number 数量的 forbidden partitions 能否再被一个更小、仍然完备的 obstruction object 替代。本补充在 generator 一侧给出 exact answer。

下面用到的 hypergraph transversal / blocker 数学是成熟先行工作。R004 当前真正新增的是：把 typed future-safe compiler 归约成一个 minimal deletion-cut clutter，并让每个 cut 自动生成一个 canonical forbidden-world witness。

## 1. 基本设置

设 `G` 是有限 typed future-language generator 集，`P0` 是初始 observation partition，

`Q* = Compile_G(P0)`

是完整语言下唯一最粗 jointly-safe refinement。

对 retained generator set `S subseteq G`，记

`Q_S = Compile_S(P0)`。

因为 `S` 的约束包含于完整 `G` 约束，`Q*` 必然 refine 每个 `Q_S`。因此定义 carrier adequacy Boolean predicate：

`Phi(S)=1 iff Q_S=Q*`。

它对 generator inclusion 单调：

`S subseteq T and Phi(S)=1 => Phi(T)=1`。

## 2. R004-COMP-T24——minimal carrier cuts

若 deletion set `H subseteq G` 满足

`Compile_(G\H)(P0) != Q*`，

则称 `H` 为 **carrier-breaking**。

定义

`C_G(Q*) = Min_subseteq { H subseteq G : H carrier-breaking }`。

由于只保留 inclusion-minimal members，`C_G(Q*)` 是 generator set 上的 clutter/antichain。

这些就是 **minimal carrier cuts**：每个 cut 中的 generators 对该 failure mode 都是联合必要的，但删除任何更小真子集都还不足以破坏 carrier。

## 3. R004-COMP-T25——canonical forbidden-world witness theorem

对每个 minimal cut `H in C_G(Q*)`，定义

`P_H = Compile_(G\H)(P0)`。

则 `P_H` 是 forbidden coarse world（`P_H != Q*`），并且它的 full-language kill set 恰为

`K(P_H)=H`，

其中

`K(P)={g in G : g 在 P 上不 stable / illegal}`。

证明。`P_H` 对所有 `G\H` generators stable，所以 `K(P_H) subseteq H`。若存在 `h in H` 也对 `P_H` stable，则 `P_H` 会对 `G\(H\{h})` stable。但 `H` 的 minimality 表示删除真子集 `H\{h}` 时 carrier 必须仍是 `Q*`，不可能存在严格更粗的 forbidden stable refinement。矛盾。因此每个 `h in H` 都必须杀掉 `P_H`。

所以一旦 cut 已知，compiler 自己就能生成该 cut 的 canonical coarse-state certificate，不需要再外部搜索 partitions。

## 4. R004-COMP-T26——minimal kill sets 恰等于 minimal cuts

反过来，取任意位于 `P0` 与 `Q*` 之间的 forbidden partition `P`。若它的 kill set `K(P)` 在所有 forbidden-world kill sets 中 inclusion-minimal，那么由于 `P` 对 `G\K(P)` stable，删除 `K(P)` 一定 carrier-breaking。

若 `K(P)` 的某个真子集已经 carrier-breaking，则那个更小 deletion 的 compiler output 会产生一个更小的 forbidden kill set，违反 minimality。

因此

`K(P) in C_G(Q*)`。

所以两个有限对象完全一致：

`minimal forbidden kill sets = minimal carrier deletion cuts`。

多个 forbidden partitions 可以共享同一个 kill set；`P_H` 给出该 cut type 的一个 canonical 最粗 witness。

## 5. R004-COMP-T27——Structural Obstruction Basis

定义

`O* = { P_H : H in C_G(Q*) }`。

那么 retained set `S subseteq G` 保持完整 carrier `Q*`，当且仅当它杀掉 `O*` 中每个 canonical obstruction world；等价地：

`S cap H != empty`

对每个 `H in C_G(Q*)` 都成立。

因此 inclusion-minimal Carrier Bases 恰好是 carrier-cut clutter 的 minimal transversals：

`B_C = Tr(C_G(Q*))`。

这就是补充 15 中 Bell-number forbidden-partition universe 的 exact replacement。

此前 pairwise-merge no-go 仍然关键：`O*` 一般不能只用 state pairs 或 `Q*` 的 immediate coarsenings 代替。一个 generator 可能杀掉所有单对 merger，却允许一个更大的 multi-block merger。真正的 obstruction type 位于 generator cuts，而不是 state pairs。

## 6. Blocker duality

因为 `C_G(Q*)` 是 clutter，标准 hypergraph blocker duality 给出

`Tr(Tr(C_G(Q*))) = C_G(Q*)`。

所以 minimal sufficient Carrier Bases 与 minimal carrier-breaking cuts 可以彼此恢复：

`B_C = Tr(C_G)`，

`C_G = Tr(B_C)`。

这是成熟 hypergraph duality，不是 R004 新 theorem。项目新增只在于：Representation Compiler 自然产生了一个 concrete monotone Boolean function，其 minimal true sets 与 maximal-failure complements 正好实例化这个对偶。

## 7. generator-side complexity bound

若 `m=|G|`，minimal cuts 都是 `G` 子集中的互不可比元素。经典 antichain bound 给出

`|C_G(Q*)| <= binom(m, floor(m/2))`。

同样的 bound 也适用于 inclusion-minimal Carrier Bases family。

这仍然可能对 `m` 指数增长；这里不主张 polynomial algorithm。但 obstruction universe 已经转到 generator-side，与 exact-state carrier 的 Bell number 脱钩。

对应计算问题是 generator bits 上的 monotone Boolean / hypergraph dualization，compiler 只作为 `Phi(S)` membership oracle。

## 8. 纯整数最优性证书的新解释

补充 15 的 disjoint-forbidden-world lower bound 现在正好是 carrier-cut clutter 中的 matching lower bound。

若 `D subseteq C_G` 是 pairwise generator-disjoint cut family，则任何 carrier basis 至少要从每条 cut 里选一个不同 generator：

`|S| >= |D|`。

若某 candidate basis 满足 `|S|=|D|`，就得到纯有限整数的 cardinality optimality certificate。

同样地，一个 inclusion-minimal basis 具有标准 private-cut property：每个 retained generator `g` 都必须存在一条 cut edge，只与该 basis 在 `g` 处相交。

## 9. Validation

独立穷举使用补充 14 的 unified mixed typed compiler。

完整 3-state family 同时包含：

- 一个 total unary generator；
- 一个 partial unary generator（每个 source state 可 disabled 或指向三个 target states 之一）；
- 一个 loopless COUNT-relation generator；
- 所有 initial set partitions。

总计 **552,960** 个 full language instances。

每个 instance 都完整枚举 generator subsets，并同时验证：

1. minimal carrier deletion cuts = inclusion-minimal forbidden-world kill sets；
2. 每个 canonical witness `P_H=Compile_(G\H)(P0)` 都满足 `K(P_H)=H`；
3. inclusion-minimal Carrier Bases = cut clutter 的 minimal transversals。

零 violation。

Executable reference：`src/enterprise_math/precision_structural_obstruction_basis.py`；direct regressions：`tests/test_precision_structural_obstruction_basis.py`。

不主张 fresh full-repository CI 或 canonical-main theorem status。

## 10. Prior-art 边界

成熟数学包括 hypergraph transversals / minimal hitting sets、clutter blockers、monotone Boolean dualization、Sperner antichain bounds，以及 minimal-cut / minimal-transversal algorithms。source mapping 记录于 `docs/PRIOR_ART_R004_STRUCTURAL_OBSTRUCTION_BASIS.*` 与 `sources_r004_structural_obstruction_basis.json`。

R004 只主张 typed-compiler reduction：

`future-safe compiler -> monotone generator adequacy -> minimal carrier cuts -> canonical forbidden worlds -> minimal carrier bases`。

这套 Enterprise Math reduction/certificate package 的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 11. 下一步

Carrier preservation 只是 primitive instruction set 的一半。补充 17 加入 quotient-level semantic reconstruction，并证明 carrier cuts 与 semantic cuts 会组成一个 typed adequacy clutter；其 minimal transversals 就是真正的 minimal adequate primitive instruction sets。

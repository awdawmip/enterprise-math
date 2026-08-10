# P025 补充 95 —— 双轴 Extension Diamond 与 Representation Pareto Frontier

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-orbit-normal-stage91`  
依赖：P025 补充 93–94  
硬阻断：`NONE`

## 1. 两种 extension language 作用于同一个 semantic state

Stage 94 识别出 finite Ferrers precision state 的两种 primitive future extensions：

1. 插入一个 new threshold；
2. 追加一个 new orbit node。

两种 operation 都是 exact 的，但 preferred local coordinates 不同。

Stage 95 问两个结构问题：

- 两种 extension operations 在 semantic state 上是否 commute？
- 是否存在一种 representation 能同时在 storage 与两个 update directions 上支配其他 representations？

答案分别是 **yes** 与 **no**，只要 grid 真正是二维的。

## 2. P025-T225 —— threshold / orbit extension diamond commute

从任意 dyadic threshold staircase `S` 开始，选择一个尚未存在的 new threshold `T`。

通向 enlarged grid 有两条路径：

\[
\boxed{S\xrightarrow{+T}S_T\xrightarrow{+j}S_{T,j}}
\]

以及

\[
\boxed{S\xrightarrow{+j}S_j\xrightarrow{+T}S_{j,T}.}
\]

两个 final states 都来自同一 old orbit 加一个 appended pressure value，以及同一 old threshold set 加 `T`。

因此每个 final cell 都是同一个 Boolean statement

\[
\rho_j\ge T_k.
\]

所以

\[
\boxed{S_{T,j}=S_{j,T}.}
\]

该 equality 同时对以下表示成立：

- activation matrices；
- crossing-depth vectors；
- node-rank vectors；
- Ferrers boundary words。

因此 biaxial extension square 是 flat 的。

## 3. P025-T226 —— boundary path 看见的是 `VH` 与 `HV`

由 Stage 94：

- threshold extension 插入一个 `V`；
- orbit extension 插入一个 `H`。

所以 extension diamond 两条路径的 edge labels 分别为

\[
\boxed{(V,H)}
\]

和

\[
\boxed{(H,V)}.
\]

intermediate boundary words 通常不同，但 final boundary word 完全相同。

这就是 commuting semantic diamond 在 boundary coordinate 中的表达。

## 4. P025-D40 —— 无权 representation cost vector

为了在不引入任意 numerical weights 的前提下比较三种 exact representations，只记录三个整数坐标：

\[
\boxed{
C=(\text{storage coordinates},
\text{threshold-extension worst-case writes},
\text{orbit-extension worst-case writes}).
}
\]

这不是 runtime model，只是 unit coordinate writes 下的 structural envelope。

对 `s` 个 thresholds 与 `h+1` 个 orbit nodes：

### Crossing coordinates

storage 使用 `s` 个 depths。

threshold insertion 只写一个 crossing coordinate；new orbit node 最坏可能一次 resolve 所有 thresholds，所以 orbit worst case 为 `s` crossing rewrites。

因此

\[
\boxed{C_{\rm cross}=(s,1,s).}
\]

### Rank coordinates

storage 使用 `h+1` 个 ranks。

orbit extension 追加一个 rank；一个很低的新 threshold 最坏会把所有 existing ranks 都加一。

因此

\[
\boxed{C_{\rm rank}=(h+1,h+1,1).}
\]

### Boundary word

每个 threshold 与 orbit node 各占一个 symbol，storage 为

\[
s+h+1.
\]

两个 axes 的 extension 都是 one-symbol insertion，所以

\[
\boxed{C_{\rm path}=(s+h+1,1,1).}
\]

## 5. P025-T227 —— nontrivial grid 上三者形成完整 Pareto frontier

假设

\[
\boxed{s\ge2,\qquad h+1\ge2.}
\]

则：

- crossing 在 threshold-update locality 上优于 rank，而 rank 在 orbit-update locality 上优于 crossing；
- path 在 orbit-update locality 上优于 crossing，但 storage 更大；
- path 在 threshold-update locality 上优于 rank，但 storage 更大。

所以三组 cost vectors 没有任何一组能在全部 coordinates 上支配另一组。

因此

\[
\boxed{\{\text{crossing},\text{rank},\text{path}\}}
\]

正好构成该 structural cost envelope 下的 nondominated representation family。

第一块完整 Pareto grid 已经是

\[
s=2,\qquad h+1=2.
\]

## 6. P025-C33 —— one-threshold degeneracy 让 frontier collapse

若

\[
s=1,
\]

则

\[
C_{\rm cross}=(1,1,1).
\]

只要 horizon 超过一个 node，它就支配其他两种表示：

- rank storage 更大且 threshold extension 可能多写；
- path storage 更大又没有 update advantage。

所以 one-threshold future 在该 cost envelope 下没有理由离开 crossing scalar representation。

## 7. P025-C34 —— one-node degeneracy 是 exact dual

若

\[
h=0,
\]

只有一个 orbit node，且

\[
C_{\rm rank}=(1,1,1).
\]

当 thresholds 多于一个时，它支配其他两种表示。

所以 threshold 与 orbit 两个 degeneracies 完全对偶。

## 8. Exact working Pareto calibration

对 Stage 93 的 `4 x 4` grid，

\[
s=4,\qquad h+1=4.
\]

cost vectors 为

\[
\boxed{C_{\rm cross}=(4,1,4),}
\]

\[
\boxed{C_{\rm rank}=(4,4,1),}
\]

以及

\[
\boxed{C_{\rm path}=(8,1,1).}
\]

path 的 coordinate count 是任一 one-axis chart 的两倍，但它也是唯一在两个 extension directions 上都 local 的表示。

如果不再额外加入 workload / cost preference，就无法从这些数据中导出合法 scalar ranking。

## 9. P025-T228 —— representation choice 只有 partial order

semantic equivalence 给三种 representations 之间一个 bijection，但 operational cost 只给出 Pareto partial order。

因此说

> representation A 比 representation B 更精确 / 更好

在没有 declared future operation language 或 cost criterion 时是不完整的。

正确对象应是

\[
\boxed{
\text{semantic quotient}
+
\text{coordinate chart}
+
\text{future operation profile}.
}
\]

这进一步强化了 Stage 94 的 axis-relative coordinate policy。

## 10. 与 Stage 85 Hasse diamond 的关系

Stage 85 在 exponent-transport space 发现 flat diamonds：exponent 乘两个不同 cover primes 的先后顺序不改变 long-range pressure multiplier。

Stage 95 在 precision-state space 发现另一类 flat diamond：新增 threshold precision 与新增 orbit depth 的顺序不改变 final Ferrers state。

共同结构并不是 operations 相同，而是 local generators 在 declared semantic quotient 上 commute。

这是值得跨路线关注的 pattern，但还没有被提升为 common theorem。

## 11. 架构含义

现在两条 lesson 同时成立：

1. **state choice 是 future-relative 的** —— Stage 90；
2. **同一 state 内的 coordinate choice 是 operation-relative 的** —— Stages 94–95。

因此 precision architecture 若为所有 workloads 固定一个 canonical representation，可能承诺过多。

更弱也更安全的原则是：保留 semantic state 的可互换 charts，并根据下一步 expected operation family 选择 chart。

## 12. Prior-art / novelty 边界

commuting squares、Pareto dominance、sparse coordinate updates 与 chart selection 都是 broad prior mathematical / computational concepts。

P025 不单独主张这些概念新颖。

项目侧结果只是 exact arithmetic / Ferrers instantiation，以及由两个 future extension axes 诱导出的 proved cost vectors。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 13. 可执行资产

新增：

- `src/enterprise_math/abc_dyadic_extension_diamond.py`；
- `tests/test_abc_dyadic_extension_diamond.py`。

executable layer 验证 biaxial extension diamond 两条路径、final crossing / rank / path equality、exact cost vectors、nontrivial Pareto frontier，以及 one-threshold / one-node degeneracy boundaries。

## 14. 下一前沿

不存在硬阻断。继续：

1. 把 Ferrers activation area 定义成 biaxial extensions 的 scalar potential；
2. 计算其 threshold-axis 与 orbit-axis finite differences；
3. 检验 mixed second difference 是否精确等于 new corner activation bit；
4. 与现有 P024 action-language / P023 composition structures 做对照；
5. 然后再决定 Stage91–95 是单独开 Foundation Feedback Packet，还是扩展 Stage90 packet。

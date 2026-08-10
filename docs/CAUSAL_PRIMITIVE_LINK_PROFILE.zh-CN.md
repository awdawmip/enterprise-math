# Causal Primitive Link Profile —— 最小精度方向的有限因果均匀性

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE GRAPH RESULTS + PRIOR-ART MAPPING IN PROGRESS`

归属：几何 theorem-home 应由 P022/A5 消费；当前 `research/core/relation-quotient` 仅承载跨路线 reference implementation 与 causal-quotient 接口，不把 A3 变成新的几何 owner。

## 1. 纠偏

不能再用以下单一标准选择最小精度几何：

- packing density 最大；
- primitive neighbor 数最多；
- higher-shell orbit 数最少；
- 看起来最接近连续球。

P019 已经给出反例：`A_3/FCC` 的 graph radius-2 shell 有 3 个整数 orbit types，而 `Z^3` 只有 2 个，所以“orbit 数越少越各向同性”不是可靠 standalone criterion。

真正更贴近进取数论的问题是：

> 在当前最小 relation horizon 内，一个 primitive direction 与另一个 primitive direction 是否拥有同样的可继续关系？

## 2. primitive direction link

给 primitive integer displacement set `Phi`。

定义两方向：

\[
\alpha\sim\beta
\iff
\beta-\alpha\in\Phi.
\]

这得到原点 first shell 上的纯整数 relation graph `L(Phi)`。

不需要角度、平方根或 packing density。

第一层 typed profile 包括：

- primitive direction 数；
- link degree histogram；
- connected components；
- graph diameter；
- 每个 primitive edge 的 common-neighbor induced graph；
- pair relation 的 `(link distance, common-neighbor count)` histogram。

## 3. compatible-direction flag

一个 `r`-flag 是 `L(Phi)` 中一个 `r`-clique：一组两两仍保持 primitive compatibility 的方向。

对 flag `C` 定义一步 continuation capacity：

\[
\boxed{
Ext(C)
=
\#\{\alpha:\alpha\text{ 与 }C\text{ 中每个方向都 compatible}\}.
}
\]

对所有 `r`-flags 收集 `Ext(C)` histogram。

若该 histogram 只有一个值，则在“下一步还能怎样继续扩展”这个 future query 下，所有 `r`-flags 仍不可区分。

第一次出现多个 extension counts，称为 **flag continuation split**。

注意：extension count 只是 one-step continuation shadow；一般图中相同 count 不保证完整 future signature 相同。后续要用 contextual quotient 继续细化。当前 A/D/E 的低阶结果因其高对称性可先用此 profile 做严格可失败筛查。

## 4. finite-horizon isotropy contract

提出一个候选研究门，而不是物理公理：

给定 flag horizon `h`，候选 primitive geometry 通过当前 contract，当且仅当：

1. primitive link connected；
2. primitive directions 只有一个 degree type；
3. rooted primitive-edge context 只有一个 type；
4. 对所有 `r<=h`，flag extension histogram 都是 singleton。

解释：

\[
\boxed{
\text{isotropy at precision horizon }h
=
\text{local causal continuation indistinguishability through }h.
}
\]

不要求高于 `h` 的 relation context 永远不分裂。

这与此前“无限 distance-transitivity + polynomial growth 不可兼得”的负边界兼容。

## 5. A 系

对 `A_p`：

\[
|\Phi|=p(p+1),
\qquad
\deg L=2(p-1).
\]

固定一条 primitive edge，其 common-neighbor graph 为：

\[
\boxed{K_{p-1}\sqcup K_{p-1}.}
\]

因此 `A_3/FCC`：

- 12 directions；
- link degree 4；
- 每条 primitive edge 有 4 common neighbors；
- common-neighbor graph 是两条互不连接的 edge。

其 flag extension：

\[
A_3:\quad 4\to1\to0,
\]

\[
A_4:\quad 6\to2\to1\to0.
\]

在这些 maximal compatible flags 内未出现 continuation-count split。

但这不能推出 `A_p` universal。

## 6. D 系压力测试

`D_n` primitive roots 为：

\[
\pm e_i\pm e_j.
\]

直接整数枚举与组合计数给：

\[
|\Phi|=2n(n-1),
\qquad
\deg L=4(n-2).
\]

固定 primitive edge 的 common-neighbor context 有 `4(n-2)` 个 vertices。

- `D_3` 与 `A_3/FCC` 同构；
- `D_4`：24 directions，link degree 8，edge context 为 8 vertices / 12 internal bonds / connected；
- `D_5`：40 directions，link degree 12，edge context 为 12 vertices / 30 internal bonds / connected。

但 `D_5` 到 triangle flag 首次分裂：

\[
\boxed{
80\text{ triangles have }Ext=0,
\qquad
320\text{ triangles have }Ext=2.
}
\]

所以 D 系说明：更高 coordination 不自动等于更高阶 continuation uniformity。

## 7. exceptional E 系

使用纯整数缩放的 `E_8` roots：

- 112 个 `(±2,±2,0,...,0)` roots；
- 128 个 `±1` roots，负号数为偶数；
- 总计 240。

相应子系统得到：

\[
|E_6|=72,
\quad
|E_7|=126,
\quad
|E_8|=240.
\]

低阶 link profile：

| family | directions | link degree | rooted edge-context |
|---|---:|---:|---|
| `E6` | 72 | 20 | 20 vertices, 9-regular, connected |
| `E7` | 126 | 32 | 32 vertices, 15-regular, connected |
| `E8` | 240 | 56 | 56 vertices, 27-regular, connected |

flag continuation enumeration：

\[
E_6:\quad20\to9\to4\to1\to0,
\]

全部 maximal 5-flags uniform。

`E_7` 在 size 5 首次 split：有的 5-flag maximal，有的仍可扩 2 个方向。

`E_8`：

\[
56\to27\to16\to10\to6\to3
\]

一直到 6-flag 都 uniform；7-flag 首次 split：

\[
\boxed{
Ext=0\quad\text{or}\quad Ext=1.
}
\]

完整枚举得到 207360 个 7-cliques，其中 69120 个 maximal，138240 个仍可扩成 8-clique；8-cliques 有 17280 个。

这与 Winter--van Luijk 对 `E_8` color-1 size-7 cliques 的两个 Weyl orbits（maximal / non-maximal）相吻合。该前人工作必须进入正式 lineage；本项目不声称发明 E8 clique orbit 分类。

## 8. 一个新的关键结论：候选形成 Pareto，而非总排序

同维候选经常不可比较。

例如 rank 4：

- `A_4`：20 directions，较低 relation capacity，但 compatible flags 一直 uniform 到 size 4；
- `D_4`：24 directions，局部 degree 与 edge context 更丰富，但 maximal compatible flag 只到 size 3。

rank 6：

- `A_6` 有更长 maximal compatible flag；
- `E_6` 有显著更大的 primitive/local relation capacity，同时其自身 maximal flags 也保持 uniform。

rank 8：

- `A_8` 的 flag count law 更规则；
- `E_8` 的 local relation capacity 极高并 uniform 到 6-flag，但在 7-flag 出现真实 split。

所以目前不能定义“邻居越多越好”或“split 越晚越好”的单标量 isotropy score。

正确对象应保留 typed profile：

\[
\boxed{
(\text{direction capacity},
\text{edge context},
\text{flag continuation spectrum},
\text{first split order},
\text{pair-context spectrum}).
}
\]

最终选择必须由未来物理/几何任务给出所需 horizon 与可区分 observable。

## 9. FCC / HCP 的位置

外部 Common Neighbor Analysis 文献给 perfect structures：

- FCC：12 个 nearest-neighbor bonds 全是 421；
- HCP：6 个 421 + 6 个 422。

这支持当前纯 relation interpretation：两者 coordination 都为 12，但 FCC 的 primitive bond context 是一个类型，HCP 已在更低阶 local context 分成两类。

该事实只把 FCC 提升为“更强 minimum-horizon uniformity candidate”，不证明自然空间必须 FCC。

## 10. 与 causal signature 的统一

flag continuation split 不应被解释成“高阶几何变坏”。

更准确：

- horizon 以下：relation states 仍 future-indistinguishable；
- split 出现：同一低阶 summary 不再足够，必须增加 continuation type；
- 是否真的需要增加 type，由物理 future language 决定。

所以高阶 direction geometry 可以直接进入：

`raw flag -> future/context quotient -> minimum relation type`。

这与 A3/P023 已有 minimum future state 是同一母机制。

## 11. 实现

新增：

- `src/enterprise_math/causal_primitive_link_profile.py`
- `tests/test_causal_primitive_link_profile.py`

默认 CI 对 E8 只跑低阶 bounded flag enumeration，避免把 40 多万 clique 的 research enumeration 变成常规门禁；完整 flag counts 保留为 targeted research computation。

## 12. 下一步

1. 把 one-step `Ext` count 升级成完整 finite-horizon flag continuation signature，而不是只看 cardinality；
2. 对 HCP coordination link 做纯 combinatorial reconstruction，直接在同一 profile 下与 `A_3/FCC` 比较；
3. 对 `A_4/D_4`、`A_6/D_6/E_6`、`A_8/D_8/E_8` 建立 dimension-wise Pareto frontier；
4. 把 primitive link 的 unit-cost transport 与 graded future-revelation tower 接起来；
5. 只有出现明确 physical future language 后，才允许从 Pareto frontier 选择“自然”的 minimum-precision geometry。

# P019 —— 方向聚焦补充 08：新增结构筛选、自同构轨道与各向异性门槛

状态：`ACTIVE RESEARCH NOTE / DIRECTIONAL GATE`
依赖：P012 内生图几何；P019 补充 03、05、06、07
纪律：在没有额外推导前，不得把本文任何量直接命名为物理 shear、Ricci curvature 或 gravitational clock rate。

## 1. 对本轮新增 P019 工具做保留审计

前几阶段引入了多个量，但它们不应拥有同等基础地位。

### 核心 —— 保留为结构主干

1. `phase / causal boundary`：用于区分因果侧与精确边界；
2. `F(A), Xi(A)`：不同未来截面及其精确基数变化；
3. `B(A), C(A)` 与 `Xi=B-C`：最小 branching-versus-focusing 分解；
4. 完整 `J_k^out` 谱：必须保留，因为从三个 source 开始，`C` 已不是完整局部聚焦 invariant；
5. P012 图自同构：若不偷渡欧氏坐标，它正是定义方向所需要的内生对称语言。

### 有用诊断量 —— 保留，但不围绕它们建立本体

- `R_t`：无分数的归一化 expansion 变化次序；
- `H=J2-C`：multiplicity 至少为 3 的精确证书；
- `Q=2J2-C`：multiplicity excess 的集中程度；
- submodularity / diminishing returns：是 `Xi` 的重要定理，但属于成熟 coverage 数学，不应升级为新 primitive。

### 研究候选 —— 明确降格

- `K_branch`：代数上精确等于 `B`，但“clock”解释没有证明；
- 任何把 `H`、`Q` 或后续方向量直接等同 continuum shear / curvature 的解释。

这一步的目的，是防止 P019 把每个方便的统计量都膨胀成新的基础对象。

## 2. 为什么方向不能从坐标里直接搬进来

P012 已经确定：内生几何从 primitive adjacency 开始，精确对称由图自同构表达。

对有限 directed graph `G=(V,E)` 与当前截面 `A`，定义

`Aut(G;A)`

为保持 directed edge relation 且把 `A` 作为集合保持不变的自同构群。

从 `A` 发出的 primitive incidences 为

`I_A={(v,w) in E : v in A}`。

若两个 incidence 落在 `Aut(G;A)` 对 `I_A` 作用的同一个 orbit 中，就把它们定义为同一个 **A 处的内禀方向类**。

整个定义不需要欧氏角度、坐标轴或实值切向量。

## 3. P019-DIR-T01 —— Orbit direction classes 自同构协变

状态：`PROVED BY DEFINITION / GROUP ACTION`。

`I_A` 的 orbit partition 在 `Aut(G;A)` 的每个元素下保持不变。若对整个有限图做同构重标号，方向 partition 也整体随同构搬运，而不会改变其数学内容。

因此，只依赖无序 orbit 数据构造的 observable 都具有图同构协变性。

## 4. P019-DIR-N01 —— 传递结构上的方向分辨率 no-go

状态：`PROVED NECESSITY RESULT`。

如果 `Aut(G;A)` 在 `I_A` 上传递，则只有一个 intrinsic direction orbit。

因此，任何只依赖无标记 `(G,A)` 且要求自同构协变的 observable，都不可能区分这个 orbit 内部的两条 outgoing incidences。

这不是方法失败，而是一条分辨率定理：

> 在没有额外结构时，由对称性判定为等价的方向，本来就不能被内生地区分。

特别地，只得到一个 orbit 不能被报告成“证明物理上各向同性”；它只能说明当前内禀结构没有更细方向信息。

这也说明：不能对一个高度对称的裸图凭符号制造 shear-like 自由度。

## 5. P019 本身已经提供了合理的额外结构

黑洞 / 聚焦问题通常不是一个无标记图。P019 已经拥有：

- 当前截面 `A`；
- causal phase labels；
- zero vertices 与 sign-crossing boundary edges；
- horizon / boundary complex。

所以正确方法应是：使用保持这些有数学根据的 marked structure 的自同构群，而不是导入任意外部方向轴。

加入合理 mark 会缩小 automorphism group，从而可能细化 incidence orbits。

## 6. Direction-channel focusing data

对一个 intrinsic incidence orbit `D subset I_A`，定义

`m_D(w)=# {(v,w) in D}`。

并定义：

`E_D=|D|`，

`T_D=# {w:m_D(w)>0}`，

`C_D=E_D-T_D=sum_w(m_D(w)-1)`，

以及

`J_{k,D}=sum_w binom(m_D(w),k)`。

因此，每个 intrinsic direction channel 都继承原来同一套整数 focusing calculus。

这些不是新的独立 primitive，而只是把已经存在的 `C` 与 `J_k` 限制到由自同构定义的 incidence orbit 上。

## 7. P019-DIR-T02 —— Pair focusing 精确分成方向内项与跨方向项

状态：`PROVED`。

对互不相交的 direction channels `D_i`，定义

`X_ij=sum_w m_i(w)m_j(w)`，`i<j`。

则总 pair collision 满足

`J2(total)=sum_i J2(D_i)+sum_{i<j} X_ij`。

证明很直接：任意一对发生碰撞的 incidences，要么来自同一方向 channel，要么分别来自两个不同 channel。

因此 cross term 不能省略。两个各自内部完全无碰撞的方向 channel，仍可能通过“跨方向落到同一个 future target”产生全部聚焦。

所以未来若研究 shear-like 结构，不能只看各方向自己的 `C_D`，还必须保留 cross-direction overlap。

## 8. P019-DIR-T03 —— 无分数方向 collision-rate 各向异性证书

状态：`PROVED INTEGER IDENTITY / PHYSICAL INTERPRETATION OPEN`。

对非空 direction channels，令

`E_i=|D_i|`，`C_i=C(D_i)`。

若在外部比较层想比较各方向的 `C_i/E_i`，整数核心不需要存储这些分数。定义

`A_C=sum_{i<j}(E_j*C_i-E_i*C_j)^2`。

则：

`A_C>=0`，

并且

`A_C=0`

当且仅当所有已经被当前结构分辨出来的 direction channels 具有相同 collision rate。

这个量不依赖 direction channel 的编号，并且内部只使用整数。

目前它只称为：

**directional collision-rate anisotropy witness**。

它不是物理 shear。

### 分辨率警告

若 intrinsic direction partition 只有一个 orbit，则 `A_C=0` 自动成立。

所以 `A_C=0` 只表示：

**在当前 marked graph 所能提供的方向分辨率下没有检测到差异。**

它绝不自动推出物理世界完全各向同性。

## 9. 一个小型精确例子

当前截面取 `{a,b}`，future states 为 `{x,y,z}`，directed edges 为：

`a->x`，`b->y`，`a->z`，`b->z`。

图存在保持截面的对称：

`a<->b`，`x<->y`，而 `z` 固定。

因此存在两个 intrinsic incidence orbits：

`D_private={a->x,b->y}`，

`D_common={a->z,b->z}`。

两者数据为：

- private channel：`E=2, C=0`；
- common channel：`E=2, C=1`。

于是

`A_C=(2*0-2*1)^2=4`。

这里没有人为插入坐标方向。方向差异完全来自 causal graph 自身对“私有 future”与“共同 future”的结构区分。

## 10. 本阶段如何修正黑洞研究路线

之前的路线是“构造 directional overlap，然后和 shear 比较”。Stage 08 把这件事收紧了。

正确顺序应是：

`primitive marked causal structure`

`-> section/phase/boundary-preserving automorphism group`

`-> incidence direction orbits`

`-> per-orbit J_k + cross-orbit overlap`

`-> fraction-free anisotropy witnesses`

`-> 最后才与外部 shear-like focusing 做结构比较`。

这样就消除了一个隐藏假设：不能先随意选一个方向基，再称其为 intrinsic。

## 11. 当前真正应保留的 P019 kernel

经过审计后，紧凑主干为：

`(marked primitive causal graph, A)`

`-> F(A)`

`-> Xi=B-C`

`-> full J_k overlap/fiber spectrum`

`-> 当结构本身允许时，用 automorphism-defined directional refinement`。

`H`、`Q`、`R` 继续作为这个 kernel 的有用 projection / diagnostic。

`K_branch` 只保留为 clock-calibration candidate。

## 12. 下一道门槛

下一步不应再加一个 scalar，而应确定：**黑洞问题自身到底提供了哪一种合理 mark。**

优先顺序：

1. 先用已有 causal phase / boundary complex 作为 mark；
2. 计算相应 stabilizer refinement 与 direction channels；
3. 检验是否能在完全无坐标条件下自然出现 horizon-crossing 与 horizon-tangent channels；
4. 只有自然出现后，再研究其 anisotropy evolution 是否与 continuum shear 有结构对应；
5. clock bridge 继续保持为独立 no-go / derived-observable 问题。

如果 phase/boundary marking 后仍然只有一个 transitive orbit，P019 应接受该 no-go，而不是人为发明方向轴。

可执行参考层：

- `src/enterprise_math/directional_focusing.py`
- `tests/test_directional_focusing.py`

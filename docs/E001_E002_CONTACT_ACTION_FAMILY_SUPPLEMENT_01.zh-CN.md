# E001/E002 — 对称接触动作族补充 01

状态：`ACTIVE CROSS-ROUTE ENGINEERING NOTE`  
范围：E001 Boolean contact 在有限对称整数 gap 动作族下的预测商  
父文档：`docs/E001_E002_PREDICTIVE_CONTACT_BRIDGE.zh-CN.md`  
依赖：E001 `Contact_d(g) iff g<d`；E002/P023 预测商；E002 第二阶段 gcd-safe actuation

## 1. 问题

父桥已经证明：如果唯一的双向 gap 动作是 `+a` 与下界 clipping 的 `-a`，则

\[
K_{d,a}(x)=\left\lceil\frac{d-x}{a}\right\rceil
\]

就是 Boolean 查询 `x<d` 在任意未来下的精确最粗状态。

真实有限引擎可能允许多个动作幅度。本补充追问：是否必须为每个幅度分别保留一套 phase 坐标，还是整个对称动作族可以被一个算术不变量统一。

## 2. 对称动作族

令正动作幅度为

\[
A=\{a_1,\ldots,a_m\}\subset\mathbb N_{>0}.
\]

已声明物理动作语言对每个幅度都包含两个方向：

\[
S_j(x)=x+a_j,
\qquad
C_j(x)=\max(0,x-a_j).
\]

定义公共动作粒度

\[
\boxed{g=\gcd(a_1,\ldots,a_m)}
\]

与归一化整数步长

\[
m_j=a_j/g.
\]

于是

\[
\gcd(m_1,\ldots,m_m)=1.
\]

## 3. E001/E002-T38 — 精确 gcd contact 坐标

定义

\[
\boxed{
K_{d,A}(x)
=\left\lceil\frac{d-x}{g}\right\rceil.
}
\]

令

\[
K_{\max}=K_{d,A}(0)=\left\lceil\frac dg\right\rceil.
\]

则当前 Boolean observation 与每个已声明动作都精确因子化到 `K`：

\[
\boxed{x<d\iff K_{d,A}(x)\ge1,}
\]

\[
\boxed{K_{d,A}(S_j(x))=K_{d,A}(x)-m_j,}
\]

以及

\[
\boxed{
K_{d,A}(C_j(x))
=\min(K_{d,A}(x)+m_j,K_{\max}).
}
\]

### 证明

写

\[
K(x)=\left\lceil\frac{d-x}{g}\right\rceil.
\]

因为 `a_j=m_jg`，

\[
K(x+a_j)
=\left\lceil\frac{d-x-m_jg}{g}\right\rceil
=K(x)-m_j.
\]

在没有 ground clipping 时，闭合动作满足

\[
K(x-a_j)=K(x)+m_j.
\]

若 `x-a_j<0`，物理结果被截到 `0`，因此 quotient 结果为 `K_max`，得到上面的 min 公式。

最后，对整数 `x`，

\[
\left\lceil\frac{d-x}{g}\right\rceil\ge1
\iff d-x>0
\iff x<d.
\]

故 quotient 精确。∎

## 4. 精确 fiber

对坐标值 `k`，未裁剪的整数 fiber 为

\[
\boxed{d-kg\le x\le d-(k-1)g-1.}
\]

再与 `x>=0` 取交集得到物理 fiber。

除 ground-clipped 的最上层 fiber 外，每个非空 fiber 都恰好包含 `g` 个连续整数 gap 状态。

所以动作族 gcd 具有直接 predictive 含义：它就是完整对称动作族在 Boolean contact query 下永远无法区分的最大重复 gap-detail 块宽度。

## 5. E001/E002-T39 — 任意有限动作 word 下的最粗性

`K_(d,A)` 不只是充分状态，它还是整个对称动作族在 Boolean contact 下的**最粗**任意未来确定状态。

等价地，

\[
\boxed{
K(x)=K(y)
\iff
\operatorname{Contact}(T_vx)=\operatorname{Contact}(T_vy)
\text{ 对所有有限动作 word }v.
}
\]

### 相同 K 推出行为等价

T38 为每个生成动作给出精确确定 quotient 更新，并把 observation 因子化到 `K`。对 word 长度归纳即可得到：相同 K 在所有有限动作 word 后仍有相同 K，因此始终具有相同 Boolean contact observation。

### 不同 K 必能被有限 word 区分

取

\[
k_1<k_2.
\]

如果二者当前已经位于 contact threshold `K=1` 两侧，空 word 即可区分。

否则，因为

\[
\gcd(m_1,\ldots,m_m)=1,
\]

Bezout 定理保证：归一化生成幅度的整数线性组合可以实现任意所需整数位移。由于物理语言同时声明 `+a_j` 与 `-a_j`，可以用一个有限动作 word 在 K-space 实现该有符号组合。

选择一个净 K 位移，把 `k_2` 移到 `1`。此时 `k_1` 被移到

\[
1-(k_2-k_1)\le0,
\]

最终 Boolean contact observation 不同。

Ground clipping 的上限不会破坏这个区分 word：先执行所有让 K 下降的 separating moves，再执行所有让 K 上升的 closing moves。中间 K 先下降，再单调上升到最终值 `1`，不会超过物理 cap `K_max>=1`，因此不会产生非预期 clipping。

所以任何两个不同 K fiber 都不能继续合并。∎

## 6. 与第二阶段 gcd-safe actuation 的关系

该定理就是 E002 第二阶段在 Boolean contact 上的对应版本。

第二阶段中，整数动作族通过与 cell width 的 gcd 选择最粗 future-safe 中心化精度。这里 Boolean contact threshold 使我们不再需要保留绝对 centered-cell index/detail 对，动作族 gcd 本身就成为与 contact 边界对齐的精确行为 fiber 宽度。

共同算术骨架是

\[
\boxed{
\text{已声明整数动作族}
\longrightarrow
\text{gcd 动作粒度}
\longrightarrow
\text{最粗 future-safe 精度 fiber}.
}
\]

未来观测仍然关键。更丰富的 response language 可以继续细分这些 fiber。

## 7. 通用编译器重建

有限验证世界可使用 gap state

\[
\{0,1,\ldots,G\}
\]

并为每个幅度同时提供两个动作，使用上界 saturation 仅用于闭合有限测试域：

\[
x\mapsto\min(G,x+a_j),
\qquad
x\mapsto\max(0,x-a_j).
\]

第六阶段编译器只获得这个有限 transition system 与 observation `x<d`，并不知道 gcd 公式。

测试要求稳定 predictive partition 与 `K_(d,A)` 在有限世界上**逐状态相同**：每个 compiler block 只能包含一个 K 值，而且每个 K 值只能对应一个 compiler block。

这比只比较 block 数更强。

## 8. 负边界

### 动作不对称

T39 使用同时包含 `+a_j` 与 `-a_j` 的对称语言。如果只允许部分方向，未来 semigroup 未必能实现全部整数 gcd 位移，K 即使对可因子化动作仍然充分，也可能不再是最粗状态。

### 更丰富的碰撞响应

该 quotient 只对 Boolean contact 加已声明 gap actions 精确。它不保证保留：

- exact clearance 或 penetration；
- 已声明 sampling 模型以下的 impact timing；
- velocity/momentum；
- deformation/material state；
- rebound direction 或 magnitude。

这些变量/查询必须加入未来语言后重新编译。

### 物理解释

这是 E001 工程候选内部的有限整数状态定理，并不单独证明真实物理碰撞由该 contact quotient 支配。

## 9. 可执行资产

- `src/enterprise_math/predictive_contact_family.py`
- `tests/test_predictive_contact_family.py`
- `tests/test_predictive_contact_family_compiler.py`

测试覆盖精确动作运输、有界任意 word 行为等价、不同 K 的有限可区分性、fiber 宽度，以及若干有限世界上与通用稳定预测商编译器逐状态一致。

## 10. 下一批压力测试

1. 去掉动作对称性，刻画 semigroup 控制的最小 quotient；
2. 让 action availability 依赖当前状态；
3. 加入显式 rebound/output state，编译超出 contact 本身后新增的精度义务；
4. 把同一 gcd-family contact 逻辑提升到向量 pair separation 与 Boolean collision query；
5. 比较直接 compiler runtime 与 K 闭式实现。

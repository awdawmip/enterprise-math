# P023 —— 安全精度内算子，补充 06

状态：`ACTIVE RESEARCH NOTE`  
范围：把未来安全精度刻画为有限商关系上的内算子型选择器  
依赖：P023 第一阶段商安全结构、P020 良基有限稳定化，以及 P008 内算子型坍缩结构  
纪律：商同余、自动机可区分性、partition refinement 与不动点算子都属于成熟数学。项目特有内容在于有限精度解释、现有进取数论模块之间的桥接，以及下文给出的具体算术推论。

## 1. 为什么 Stage 2 要改变研究对象

P023 第一阶段从粗观察 `q` 出发，只补回那些为了让指定未来运算能够在粗状态上良定义所必需的区分。

带标签的 partition 只是一种表示。真正不变量是它对应的等价关系

\[
E_q=\{(x,y):q(x)=q(y)\}.
\]

关系越大，被视为同一 coarse state 的 fine states 越多，因此精度越粗。精度细化对应关系包含变小。

对有限运算族

\[
\mathcal A=\{F_a:X\to X\},
\]

定义

\[
\boxed{
\Phi_{\mathcal A}(E)
=
E\cap\bigcap_{a\in\mathcal A}(F_a\times F_a)^{-1}(E).
}
\]

一对 `(x,y)` 在一轮精度细化后继续被视为同类，当且仅当它原本已经同类，而且每个生成运算仍然把它们送到同一关系类中。

## 2. P023-S2-T01 —— 安全关系步是单调且向下的

状态：`PROVED`。

在按包含关系排序的等价关系上，

\[
\boxed{\Phi_{\mathcal A}(E)\subseteq E}
\]

并且

\[
E\subseteq E'
\Longrightarrow
\Phi_{\mathcal A}(E)\subseteq\Phi_{\mathcal A}(E').
\]

同时，`Phi_A(E)` 仍然是等价关系。

### 证明

向下性直接来自最前面的 `E` 交；单调性来自交与逆像都保持包含关系。对每个 `F_a`，条件 `(F_a x,F_a y) in E` 在 `E` 为等价关系时本身也给出一个等价关系；任意等价关系的交仍是等价关系。∎

## 3. P023-S2-T02 —— 不动点恰好是运算兼容精度

状态：`PROVED`。

对等价关系 `E`，

\[
\boxed{
\Phi_{\mathcal A}(E)=E
\iff
(xEy\Rightarrow F_a(x)E F_a(y)\text{ 对每个 }a).
}
\]

因此 `Phi_A` 的不动点恰好是所有生成运算都能在其上诱导良定义粗运算的商。

## 4. P023-S2-T03 —— P023 未来闭包是 P020 稳定化的实例

状态：有限 `X` 上 `PROVED`。

当 `X` 有限时，`X` 上的等价关系集合也有限，所以严格关系包含是良基的。根据 T01，`Phi_A` 单调且向下，因此 P020 可以直接使用。

从初始观察关系 `E_0` 出发，对 `Phi_A` 做有限迭代，最终到达

\[
\boxed{
\operatorname{Safe}_{\mathcal A}(E_0),
}
\]

即 **`E_0` 内最大的 `Phi_A` 不动关系**。

等价地，它就是原始精度的所有 refinement 中，仍能让每个指定运算下沉的最粗者。

这说明 P023 第一阶段的 partition-refinement 算法，本质上是一个规范的 P020 有限稳定化问题，而不是另立一套收敛原理。

## 5. P023-S2-T04 —— 安全精度选择器本身也是内算子型

状态：有限 `X` 上 `PROVED`。

映射

\[
E_0\longmapsto\operatorname{Safe}_{\mathcal A}(E_0)
\]

具有：

- 单调；
- 向下；
- 幂等；
- 不动点恰好是 `A`-compatible 等价关系。

所以 P023 在“精度关系”空间上本身又产生了一个**内算子型算子**。它与 P008 的代数模式相呼应，但这里被坍缩的是精度关系，而不是整数值本身。

还立即得到两个有用的单调性：

\[
E'_0\subseteq E_0
\Longrightarrow
\operatorname{Safe}_{\mathcal A}(E'_0)
\subseteq
\operatorname{Safe}_{\mathcal A}(E_0),
\]

以及对运算族

\[
\mathcal A\subseteq\mathcal B
\Longrightarrow
\operatorname{Safe}_{\mathcal B}(E_0)
\subseteq
\operatorname{Safe}_{\mathcal A}(E_0).
\]

更细的初始信息不会要求更粗的安全状态；要求粗商支持更多运算，也不可能降低所需精度。

## 6. P023-S2-T05 —— 幂等运算一次修复即闭合

状态：`PROVED`；母命题已加入本研究分支 Lean。

令

\[
T:X\to X,
\qquad T^2=T,
\]

并令 `q` 为任意粗观察。定义

\[
\boxed{r(x)=(q(x),q(Tx)).}
\]

则：

1. `r` 细化 `q`；
2. `T` 可以通过 `r` 下沉；
3. 任意已经支持 `T` 的 `q`-refinement 都必须细化 `r`。

因此 `r` 已经是**对所有后续重复 T 的完整最粗未来安全 refinement**，不需要第二轮细化。

### 证明

若 `r(x)=r(y)`，则 `q(Tx)=q(Ty)`。由幂等性，

\[
r(Tx)=(q(Tx),q(T^2x))=(q(Tx),q(Tx)),
\]

对 `y` 同理，所以 `r(Tx)=r(Ty)`。

再设 `s` 细化 `q` 且支持 `T`。从 `s(x)=s(y)`，兼容性给出 `s(Tx)=s(Ty)`；由于 `s` 细化 `q`，进一步得到 `q(Tx)=q(Ty)`。所以 `s` 必须细化 `(q,qT)`。∎

该定理不需要有限性，也不需要整数算术。

## 7. P023-S2-T06 —— 单算子选择器各做一遍并不够

状态：作为一般捷径已 `DISPROVED`。

一种自然但错误的想法是：先求 `F` 的安全商，再求 `G` 的安全商，然后结束。一般情况下这不成立，因为为后处理运算做 refinement 可能重新破坏先前运算的兼容性。

一个五状态反例取

\[
F=(0,4,3,2,3),
\qquad
G=(2,0,1,2,2),
\]

初始观察

\[
E=(0,0,0,0,1).
\]

同时求共同安全精度得到离散 partition

\[
(0,1,2,3,4).
\]

但单遍顺序

\[
F\to G:\ (0,1,2,0,3)
\]

不再兼容 `F`；而

\[
G\to F:\ (0,1,0,0,2)
\]

又不兼容 `G`。

所以多运算族问题确实需要同时或反复求共同闭包。多个单算子 selector 的一次性复合并不会自动得到共同 selector。

## 8. 整数链上的单调、向下、幂等映射

现在特化到

\[
T:\mathbb N\to\mathbb N
\]

单调、向下且幂等的情形。P008 正好识别了这一内算子型模式。

对每个 `n`，`T(n)` 都是“不超过 `n` 的最大 T-不动点”：幂等性保证 `T(n)` 自身不动，若 `f<=n` 且 `f` 不动，则由单调性

\[
f=T(f)\le T(n).
\]

所以 T 的整个作用完全由其不动点在整数链上的分布控制。

## 9. P023-S2-T07 —— 均匀 floor precision 的不动点对齐判据

状态：`PROVED`。

固定

\[
Q_r(n)=n//r,
\qquad
D_r(n)=r(n//r),
\qquad r\ge2.
\]

则

\[
\boxed{
Q_r\circ T\text{ 可以通过 }Q_r\text{ 下沉}
\iff
f\in\operatorname{Fix}(T)
\Rightarrow
D_r(f)\in\operatorname{Fix}(T).
}
\]

也就是说：T 的不动点集合必须对“投影到所在 `r`-胞元左端点”这一操作闭合。

### 证明

考察一个胞元

\[
I_q=[qr,(q+1)r-1].
\]

若 `qr` 是不动点，则对所有 `n in I_q`，单调性和向下性给出

\[
qr=T(qr)\le T(n)\le n<(q+1)r,
\]

于是整个胞元都有 `Q_r(T(n))=q`。

若 `qr` 不是不动点，而且胞元内部也没有不动点，则胞元中任意状态以下的最大不动点都等于 `qr` 以下那个相同旧不动点，因此 T 在该胞元上常值。

若 `qr` 不是不动点，但胞元内部存在不动点 `f in I_q`，则在第一个内部不动点之前，粗输出小于 `q`；到 `f` 时粗输出变为 `q`，所以无法下沉。

因此，失败恰好发生在“某个不动点位于一个左端点不是不动点的 `r`-胞元”时，也就是上述闭合条件失败时。∎

## 10. P023-S2-T08 —— 每个 floor 胞元至多两种粗输出

状态：在相同假设下 `PROVED`。

对每个 `q`，

\[
\boxed{
\left|\{Q_r(T(n)):n\in I_q\}\right|\le2.
}
\]

若胞元没有新不动点，输出恒定；若出现新不动点，唯一两种可能就是旧不动点所在粗胞元与当前胞元 `q`。

所以规范修复

\[
(Q_r,Q_rT)
\]

在每个 `Q_r` 胞元内部至多只需要一个局部 bit。又因为 T 幂等，T05 进一步把这个一步修复升级为重复 T 的完整未来安全商。

## 11. P023-S2-T09 —— P007 倍数坍缩分类是不动点推论

状态：`PROVED`。

对

\[
D_d(n)=d(n//d),
\]

有

\[
\operatorname{Fix}(D_d)=d\mathbb N.
\]

使用 T07，其不动点集对 `D_r` 闭合恰好等价于

\[
\boxed{d\mid r\quad\text{或}\quad r\mid d.}
\]

所以 P023/P007 第一阶段得到的兼容分类并非孤立的算术巧合，而是内算子型坍缩“不动点对齐”的一个特例。

## 12. P023-S2-T10 —— 完全幂坍缩存在全局均匀精度 no-go

状态：`PROVED`。

令

\[
C_p(n)=R_p(n)^p,
\qquad p\ge2,
\]

并取 `r>=2`。则

\[
\boxed{Q_r\circ C_p\text{ 在全局上永远不能仅通过 }Q_r\text{ 下沉。}}
\]

一个统一见证是

\[
y=(r+1)^p,
\qquad
x=y-1.
\]

因为 `y` 模 `r` 的余数为 1，

\[
Q_r(x)=Q_r(y).
\]

但

\[
C_p(y)=y,
\qquad
C_p(x)=r^p,
\]

对 `p>=2`，二者的 `Q_r` 像不同。

使用不动点判据证明更短：`y` 是不动点，但

\[
D_r(y)=y-1
\]

严格位于 `r^p` 与 `(r+1)^p` 之间，因此不是 `C_p` 不动点，T07 条件失败。

所以任何非平凡均匀 floor precision 都不足以单独承载全局完全幂坍缩动力学。但 T05 与 T08 同时说明：对每个真正分裂的胞元补一个局部 bit，就足以支持全部后续重复坍缩。

## 13. P023-S2-T11 —— 均匀尺度因子族对最小安全修复不闭合

状态：P007 不可比 multiple-collapse 情形下 `PROVED`。

考虑 `Q_r` 与 `D_d`，并假设 `d` 与 `r` 在整除序下不可比。第一阶段已证明，其最粗修复只拆分部分 `Q_r` fiber，另一些 fiber 保持不拆。

任意能细化 `Q_r` 的均匀 quotient `Q_s` 必须满足

\[
\boxed{s\mid r.}
\]

若 `s=r`，它一个 `Q_r` fiber 也不拆；若 `s<r`，它会把**每个** `Q_r` fiber 都规则分成相同的 `r/s` 个子胞元。两种行为都不可能等于“只拆特定 fiber”的最小修复。

因此

\[
\boxed{
\text{均匀整除尺度族对 operation-safe repair 不闭合。}
}
\]

P005/P018 的整除尺度格仍然是非常重要的规则精度子族；但一般未来安全精度必须允许“规则 coarse tag + 局部 bounded detail”，或等价地允许非均匀有限 partition。

## 14. 与 P018 去重复

P018 已定义精确有限响应

\[
\mathcal R_F(x,h)=F(x+h)-F(x).
\]

对向下运算 T，令 gap

\[
G_T(n)=n-T(n),
\]

则 P023 第一阶段 borrow 满足

\[
\boxed{
B_{T,r}(n)
=Q_r(n)-Q_r(T(n))
=\mathcal R_{Q_r}(T(n),G_T(n)).
}
\]

所以 P023 不应再维护一套竞争性的 primitive borrow 理论。具体 finite-response/carry 运输由 P018 负责；P023 的独立贡献是：在该情形下，这个 response 值同时恰好给出恢复安全下沉所需的最小附加观察。

## 15. 反哺 P021

P021 的 phase/magnitude 纠偏现在可以得到一个精确的 P023 解释。

若相同有限 clock magnitude 可以同时出现在负、零、正 causal phase，那么 phase 就不是 magnitude fiber 上的常值。由 P023 第一阶段因子化定理，

\[
\boxed{\text{phase 无法通过 magnitude-only quotient 下沉。}}
\]

针对 causal phase 这一未来观察，最粗的一步修复正是

\[
\boxed{(\text{magnitude},\text{phase}).}
\]

同理，P021 的 direction-transport 计数矩阵丢掉了共享中间 incidence 的身份，所以它对精确多步路径复合并不 composition-safe；witness relation 就是必须补回的 repair 层。

这些并不是新增黑洞假设，而是同一个一般 quotient-safety 判据的应用。

## 16. 计算审计

`src/enterprise_math/p023_safe_precision_interior.py` 实现 relation selector、不动点迭代、幂等一次修复，以及刻意保留用于反例的“单算子 selector 单遍串行”捷径。

`tests/test_p023_safe_precision_interior.py` 检查 relation selector 与第一阶段 partition 实现的一致性、向下性/不动点兼容、selector 单调性、三状态幂等修复穷举，以及明确的五状态双运算反例。

本研究会话还独立穷举了至多 8 状态有限链上的全部单调、向下、幂等映射，检查整数链 fixed-point alignment 判据和 two-output 界，未发现反例。有限检查用于审计实现；上面的证明才承担定理结论。

## 17. 下一门槛

当前最高价值的下一步是：

1. 让新增 Lean 幂等修复定理通过仓库 warning-fatal 门禁；
2. 在 Lean 中把 `Phi_A` 形式化为有限等价关系上的单调向下自映射，并直接连接现有 P020 Lean 稳定化定理；
3. 决定 `regular scale + localized bounded detail` 的最小 typed representation，同时不破坏 P005 规则整除尺度格的独立价值；
4. 用更多 P008 型坍缩族压力测试 fixed-point alignment 判据，而不是继续新增无关 diagnostic。

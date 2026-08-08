# P019 —— 带电静态视界补充 01：判别式坍缩与顶点—边界视界

状态：`ACTIVE RESEARCH NOTE / PRESSURE TEST`  
依赖：`docs/P019_DISCRETE_BLACK_HOLE_HORIZON.zh-CN.md`  
范围：Reissner–Nordström 型二次径向因子的纯整数压力测试  
纪律：`a,b` 当前只是整数系数；尚未完成从物理质量、电荷、`G,c` 与 typed units 到它们的校准。

## 1. 为什么这是比 Schwarzschild 更强的压力测试

Schwarzschild 阶段只有一个正视界根。带电静态情形的外部对照因子可写成

\[
f(r)=1-\frac{a}{r}+\frac{b}{r^2},
\]

其中标准几何单位下通常把 `a` 对应质量项、`b` 对应电荷平方项。

P019 不在整数核心中做这些物理常数的实值运算，而只提取整数多项式

\[
\boxed{P(n)=n^2-an+b.}
\]

因为 `n^2>0`，连续对照中 `f` 的符号与 `P` 的符号相同。

`b=0` 时

\[
P(n)=n(n-a),
\]

所以后文的带电 observation 会严格退化为第一阶段的 Schwarzschild observation，而不是另造一个不相容模型。

## 2. P019-RN-T01 —— 完成平方恒等式

状态：`PROVED`

定义整数判别式

\[
\boxed{\Delta=a^2-4b.}
\]

则对所有整数径向状态 `n`：

\[
\boxed{4P(n)=(2n-a)^2-\Delta.}
\]

因此整个径向因果相位只需要比较一个与 `a` 同奇偶的完全平方

\[
(2n-a)^2
\]

和一个整数状态 `Delta`。

这把“两视界问题”直接压缩成了平方坍缩体系中的判别式问题。

## 3. P019-RN-T02 —— 精确整数视界 iff 判别式是平方坍缩不动点

状态：`PROVED`

`P(n)=0` 等价于

\[
(2n-a)^2=\Delta.
\]

所以存在非负整数根当且仅当

\[
\Delta\ge0
\]

且

\[
\boxed{C_2(\Delta)=\Delta.}
\]

也就是 `Delta` 为完全平方。

若

\[
d=R_2(\Delta),\qquad d^2=\Delta,
\]

则因为

\[
\Delta\equiv a^2\pmod4,
\]

`d` 与 `a` 自动同奇偶，两个代数根无需任何分数状态即可写成

\[
\boxed{h_-=(a-d)//2,\qquad h_+=(a+d)//2.}
\]

若 `Delta=0`，两根合并为

\[
\boxed{h=a//2.}
\]

如果 `b=0`，下根为 `0`，它仍是中心/除数边界而不是正半径视界；正根 `a` 正好恢复 Schwarzschild 模型。

## 4. P019-RN-T03 —— 因果相位完全由整数平方比较决定

状态：`PROVED`

由 T01：

\[
P(n)>0
\iff
(2n-a)^2>\Delta,
\]

\[
P(n)=0
\iff
(2n-a)^2=\Delta,
\]

\[
P(n)<0
\iff
(2n-a)^2<\Delta.
\]

因此无需先求实值根就能分类：

### `Delta<0`

因为平方总非负：

\[
P(n)>0
\]

对所有整数 `n` 成立。整数径向线上没有 horizon/trapped boundary。

### `Delta=0`

\[
P(n)\ge0
\]

且只有 `n=a//2` 为零。这是一个**零顶点但两侧不变号**的 extremal 型边界。

### `Delta>0`

存在严格负相位

\[
(2n-a)^2<\Delta
\]

的整数带；外部两侧为正。

若 `Delta` 是平方，边界恰落在零顶点；若不是平方，边界可能落在相邻正/负状态之间而没有零顶点。

## 5. P019-RN-C01 —— 有 trapped band 但没有任何精确零状态

状态：`COUNTEREXAMPLE TO HORIZON-MUST-BE-A-VERTEX`

取

\[
a=5,\qquad b=5,\qquad \Delta=5.
\]

`5` 不是完全平方，所以

\[
P(n)=0
\]

没有整数解。

但

\[
P(1)=1,
\quad
P(2)=-1,
\quad
P(3)=-1,
\quad
P(4)=1.
\]

因此整数状态仍存在严格相位序列

\[
+\;|\;-\;-\;|\;+,
\]

两条边

\[
(1,2),\qquad(3,4)
\]

承担了传统连续理论中两条 horizon 的边界角色。

这直接否定了 P019 第一阶段里潜在的过强假设：**离散视界不一定必须是一个零半径状态。**

## 6. P019-RN-T04 —— 顶点—边界复形统一 exact / non-exact horizon

状态：`PROVED ON THE RADIAL LINE GRAPH`

把非负整数径向状态看成 primitive line graph：

\[
0-1-2-3-\cdots
\]

定义 horizon boundary complex：

1. **零顶点**：所有正整数 `n` 满足 `P(n)=0`；
2. **变号边**：相邻状态 `(n,n+1)` 满足

\[
P(n)P(n+1)<0.
\]

`0` 从不提升为 horizon vertex；它继续作为中心/除数边界单独处理。

对 `a>0,b>0`：

- `Delta<0`：0 个 boundary component；
- `Delta=0`：1 个零顶点；
- `Delta>0` 且 `Delta` 为完全平方：2 个零顶点；
- `Delta>0` 且 `Delta` 非完全平方：0 个零顶点 + 2 条变号边。

于是 subextremal 两边界结构在整数模型中始终保留为**两个 boundary components**；改变的只是它们落在 primal vertices 还是 dual edges。

这比强迫格点对齐更适合作为后续 coordinate-free causal graph 定义的原型。

## 7. P019-RN-T05 —— 带电 finite-precision observation 与 Schwarzschild 严格退化

状态：`PROVED`

对 `lambda>0,n>0` 定义

\[
\boxed{
g_\lambda(n;a,b)
=Q_{n^2}\!\left(\lambda|P(n)|\right)
=\left\lfloor\frac{\lambda|P(n)|}{n^2}\right\rfloor.}
\]

若

\[
\lambda\mid\mu,
\qquad r=\mu/\lambda,
\]

则与第一阶段完全同型：

\[
\boxed{g_\mu//r=g_\lambda.}
\]

所以它继续是 P018 divisibility precision chain 上的合法 observation system。

更重要的是，当

\[
b=0,\qquad a=h,
\]

有

\[
P(n)=n(n-h),
\]

从而

\[
\boxed{
g_\lambda(n;h,0)
=
\left\lfloor\frac{\lambda|n-h|}{n}\right\rfloor
=q_\lambda(n;h).}
\]

所以 Schwarzschild P019 第一阶段是本模型的严格 `b=0` 特例。

## 8. P019-RN-T06 —— 零 observation 的 persistence 精确判据

状态：`PROVED`

若

\[
P(n)\ne0,
\]

则

\[
g_\lambda(n)=0
\iff
\lambda|P(n)|<n^2.
\]

因此该非根状态能够继续伪装成零 observation 的最大整数 precision 恰为

\[
\boxed{
\Lambda_0(n)
=
(n^2-1)//|P(n)|.
}
\]

而若

\[
P(n)=0,
\]

则对所有正 `lambda`：

\[
\boxed{g_\lambda(n)=0.}
\]

所以得到一个完全有限、无需极限的判据：

> **零 observation 能穿过任意 precision refinement 持续存在，当且仅当该 primal vertex 是一个精确代数根。**

同时对 `a>=1,b>=0`，存在一个统一但不追求最紧的有限 terminal precision：

\[
\boxed{
\lambda_*(a)=\max\{2,(2a-1)^2\}.}
\]

在该 precision 上，对所有正整数 `n`：

\[
\boxed{
g_{\lambda_*}(n)=0\iff P(n)=0.}
\]

### 证明要点

当 `n>=2a` 时，因 `b>=0`：

\[
P(n)\ge n^2-an\ge n^2/2,
\]

所以 `lambda>=2` 已保证非根大半径状态不可能为零 observation。

剩余候选只有有限集合

\[
1\le n<2a.
\]

对其中任一非根状态，`|P(n)|>=1`，故其零 persistence 上界小于 `n^2`，而

\[
(2a-1)^2
\]

统一超过所有这些非根状态的最大容许 precision。

这给 P018 一个真正的 finite predicate-completeness horizon。

## 9. P019-RN-T07 —— 整数尺度变换保持 horizon regime，不能“细化救回”非平方判别式

状态：`PROVED`

做统一整数径向尺度变换

\[
n' = sn,
\qquad
a'=sa,
\qquad
b'=s^2b,
\qquad s>0.
\]

则

\[
\boxed{
\Delta'=a'^2-4b'=s^2\Delta.}
\]

因此：

- `Delta<0` 的符号保持；
- `Delta=0` 保持；
- `Delta>0` 保持；
- `Delta` 是否为完全平方也保持，因为 `s^2Delta` 是完全平方 iff `Delta` 是完全平方。

所以一个 non-square discriminant 不能仅靠普通整数尺度细化变成 square discriminant。

更强地：

\[
P'(sn)=s^2P(n),
\]

于是

\[
\boxed{
g_\lambda(sn;sa,s^2b)=g_\lambda(n;a,b).}
\]

dimensionless horizon observation 在统一整数尺度嵌入上严格不变。

这不是坏事，但它迫使我们接受 T04 的结论：**不对齐格点的 horizon 应当作为 edge/dual boundary 表示，而不能期待无限细化最终把它变成一个 primal zero vertex。**

## 10. P019-RN-T08 —— 判别式的 parity-constrained square cell

状态：`PROVED`

由于所有可达平方状态

\[
(2n-a)^2
\]

的平方根都与 `a` 同奇偶，普通 `R_2(Delta)` 还不是最精确的 horizon cell coordinate。

令

\[
u=\max\{x\ge0:x\equiv a\pmod2,\ x^2\le\Delta\}.
\]

可直接从普通整数根得到：

\[
\boxed{
u=R_2(\Delta)
\text{ 若奇偶匹配；否则 }u=R_2(\Delta)-1.}
\]

则对称内部候选状态

\[
n_-=(a-u)//2,
\qquad
n_+=(a+u)//2
\]

满足

\[
\boxed{
P(n_-)=P(n_+)
=-\frac{\Delta-u^2}{4}.}
\]

下一个同奇偶平方 `u+2` 对应外侧 residual

\[
\boxed{
\frac{(u+2)^2-\Delta}{4}>0
}
\]

（除 exact case 中 `u^2=Delta` 时当前候选已经为零根）。

因此每条 horizon 都被一个纯整数、带 parity 的 square cell 包住：

\[
\text{positive phase}
\;|\;
\text{boundary cell}
\;|\;
\text{negative phase}.
\]

这与 P001/P002 的 basin gap/carry 语言形成直接接口，后续应研究该 defect 是否能统一成一般“几何边界 carry”。

## 11. 一个重要的理论修正：horizon 更像 cut，而不是必须像 point

Schwarzschild 第一阶段容易让我们把

\[
q_\lambda=0
\]

理解成 horizon 本体。

RN 压力测试说明更稳健的层级应是：

1. **因果相位**：primitive states 上的整数符号/可达性结构；
2. **边界复形**：零顶点 + 变号边；
3. **precision observation**：对边界附近状态的可分辨程度；
4. 只有当 boundary 恰与 primal vertex 对齐时，才出现“零状态 = horizon vertex”。

这将 P019 从“离散化一个半径公式”推进到一个更接近 P012 图几何的定义：

> **离散 horizon 首先是因果相位之间的 boundary/cut；它可以由 primal vertex 表示，也可以由 dual edge 表示。**

下一阶段应把这一点从一维 radial line graph 推广到一般 primitive causal graph。

## 12. 物理压力点

这一补充没有消除物理风险，反而把风险暴露得更清楚：

- 外部 RN 参数是连续模型中的质量/电荷参数；P019 尚未证明任意物理参数如何进入整数 `a,b`；
- uniform integer refinement 保持 square/nonsquare 类别，因此不能用“精度再高一点”逃避 arithmetic class；
- vertex/edge boundary 虽然解决格点不对齐，却必须进一步证明其 coordinate independence；
- extremal `Delta=0` 是零顶点但不变号，说明 horizon 不能只定义成 sign-change cut；
- inner horizon/Cauchy-horizon 的稳定性是外部 GR 中独立且困难的问题，当前纯静态多项式没有处理 perturbation stability。

因此当前最小统一定义必须同时容纳：

\[
\boxed{
\text{zero-expansion vertices}
+
\text{opposite-phase crossing edges}.}
\]

## 13. 本阶段 ledger

- `P019-RN-T01`：completed-square identity —— `PROVED`
- `P019-RN-T02`：integer roots iff square-collapse fixed discriminant —— `PROVED`
- `P019-RN-T03`：integer causal phase from square/discriminant comparison —— `PROVED`
- `P019-RN-C01`：trapped band without integer zero horizon —— `COUNTEREXAMPLE`
- `P019-RN-T04`：vertex-edge boundary complex and component classification —— `PROVED`
- `P019-RN-T05`：charged precision observation, divisible projection, Schwarzschild reduction —— `PROVED`
- `P019-RN-T06`：zero-persistence limit and finite terminal zero precision —— `PROVED`
- `P019-RN-T07`：uniform integer scale invariance / no square-class rescue —— `PROVED`
- `P019-RN-T08`：parity-constrained discriminant horizon cell —— `PROVED`

Executable checks：

- `src/enterprise_math/charged_black_hole.py`
- `tests/test_charged_black_hole.py`
- `tests/test_charged_horizon_boundary.py`

## 14. 下一步

1. 把 boundary complex 抽象到一般有向/因果图，定义 coordinate-free outgoing phase boundary；
2. 把 P018 observation fiber 放到 boundary vertices/edges 上，而不只放在 radial coordinate 上；
3. 检验 extremal boundary 的“零但不变号”如何用图上的 local expansion 表示；
4. 在完成 source-registry 后加入稳定 RN primary/context citations；
5. 之后才进入 Kerr，检验旋转是否要求 face/cell 级边界而不只是 vertex/edge。

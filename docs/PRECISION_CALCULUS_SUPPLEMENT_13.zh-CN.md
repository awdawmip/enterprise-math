# P018 —— 有限精度证明演算：补充 13

状态：`ACTIVE RESEARCH NOTE`  
范围：2×2 typed critical grid、端点对严格拼接、有限 signed holonomy 矩形恒等式、局部缺陷抵消与底层 interchange 边界  
依赖：P003、P005、P009、P010、P018-T99—T118、P020  
纪律：本阶段只证明有限状态与端点恒等式。rewriting critical pairs、finite differences、kernel pairs、double-category/interchange 等成熟语言均属于前人工作；本文不因出现相似公式就宣称已构造新的 2-category 或新型微积分。

---

## 1. 为什么现在攻 2×2 grid

P018 Supplement 11 已经得到 exact finite response

\[
\mathscr R_F(x,h)=F(x+h)-F(x),
\]

以及严格复合律

\[
\mathscr R_{G\circ F}(x,h)
=
\mathscr R_G(F(x),\mathscr R_F(x,h)).
\]

Supplement 12 又进一步发现：signed difference 并不是最弱结构。对任意状态集合 `X`，最先存在的是 State Pair

\[
(x,y)\in X\times X,
\]

确定性映射 `F:X→Y` 自动作用为

\[
(x,y)\mapsto(F(x),F(y)).
\]

因此 P018-Q97 的正确下一步不是先引入抽象 2-category，而是构造最小的 2×2 typed rectangle，检查：

1. 端点对层的两种分解是否严格一致；
2. 加入整数 Difference 坐标后，一致性如何写成 exact finite identity；
3. outer holonomy 为零是否迫使局部 defect 都为零；
4. P003 的 collapse commutation、P009 的 nonconfluence、P010 的 confluence 应落在哪一层。

---

## 2. 2×2 typed rectangle

设

\[
F_0,F_1:X\to Y,
\qquad
G_0,G_1:Y\to Z.
\]

对固定状态 `x∈X`，记

\[
a=G_0(F_0(x)),
\quad
b=G_0(F_1(x)),
\quad
c=G_1(F_0(x)),
\quad
d=G_1(F_1(x)).
\]

得到一个纯确定性的 2×2 rectangle：

\[
\begin{array}{ccc}
F_0(x)&\xrightarrow{G_0}&a\\
\downarrow&&\downarrow\\
F_1(x)&\xrightarrow{G_1}&d
\end{array}
\]

为了避免图形符号误导，本文真正使用的是四个明确端点 `a,b,c,d`：

- 左上到右上：`(a,b)`；
- 右上到右下：`(b,d)`；
- 左上到左下：`(a,c)`；
- 左下到右下：`(c,d)`。

---

## 3. P018-T119 —— 相邻 State Pair 的严格拼接

状态：`PROVED / LEAN-CHECKED TARGET`

若有两个相邻端点对

\[
(a,b),\qquad(b,c),
\]

定义拼接

\[
(a,b)\star(b,c):=(a,c).
\]

这里没有减法、加法、序、距离或精度。

它只是说：两段路径共享同一个中间端点时，比较整个复合路径只需要保留最外两个端点。

这一操作已经在

`EnterpriseMath/State/CriticalGrid.lean`

中以 `composeAdjacent` 表达。

---

## 4. P018-T120 —— 端点对层的严格 rectangle interchange

状态：`PROVED / LEAN-CHECKED TARGET`

对任意集合/类型 `X,Y,Z`，任意函数

\[
F_0,F_1:X\to Y,
\qquad
G_0,G_1:Y\to Z,
\]

以及任意 `x∈X`，严格有

\[
\boxed{
(a,b)\star(b,d)
=
(a,d)
=
(a,c)\star(c,d).
}
\]

即

\[
\boxed{
(G_0F_0x,G_0F_1x)\star(G_0F_1x,G_1F_1x)
=
(G_0F_0x,G_1F_1x)
}
\]

并且

\[
\boxed{
(G_0F_0x,G_1F_0x)\star(G_1F_0x,G_1F_1x)
=
(G_0F_0x,G_1F_1x).
}
\]

### 证明

两边按定义都只保留共同的左外端点 `a` 与右外端点 `d`。∎

### 结构意义

这是当前最弱意义上的 interchange：

- 不要求任一局部 square commute；
- 不要求 `b=c`；
- 不要求 Difference object；
- 不要求 Abelian group；
- 不要求 order/metric/topology；
- 不要求 state space 是数。

因此，**端点对的路径拼接比数值 holonomy 更底层。**

但这仍然不足以宣布某个完整 double category，因为我们尚未定义一般 2-cell 对象、所有水平/垂直组合、单位与全局 interchange 公理。这里证明的是一个最小 rectangle endpoint theorem。

---

## 5. 加入整数坐标

现在特化到自然状态，并允许 signed difference 作为比较坐标。

设

\[
h=F_1(x)-F_0(x).
\]

再定义第二层操作族的点态差

\[
\delta_G(y):=G_1(y)-G_0(y).
\]

outer signed holonomy 为

\[
\Omega(x)
:=
G_1(F_1(x))-G_0(F_0(x)).
\]

此时 State Pair `(a,d)` 只是被坐标化为

\[
(a,d-a).
\]

所以 numeric holonomy 不是新的底层对象，而是 endpoint pair 的一个整数坐标。

---

## 6. P018-T121 —— outer holonomy 的两种精确有限分解

状态：`PROVED / EXECUTABLE`

严格有

\[
\boxed{
\Omega(x)
=
\mathscr R_{G_0}(F_0(x),h)
+
\delta_G(F_1(x)).
}
\]

同时也有

\[
\boxed{
\Omega(x)
=
\delta_G(F_0(x))
+
\mathscr R_{G_1}(F_0(x),h).
}
\]

### 第一条证明

由定义，

\[
\mathscr R_{G_0}(F_0x,h)
=G_0(F_1x)-G_0(F_0x).
\]

而

\[
\delta_G(F_1x)
=G_1(F_1x)-G_0(F_1x).
\]

相加后中间项 `G_0(F_1x)` 消去，得到

\[
G_1(F_1x)-G_0(F_0x)=\Omega(x).
\]

第二条完全同理。∎

### 解释

第一种分解对应：

1. 先沿 `F_0→F_1` 移动，并用 `G_0` response 运输；
2. 再在 `F_1(x)` 处切换 `G_0→G_1`。

第二种分解对应：

1. 先在 `F_0(x)` 处切换 `G_0→G_1`；
2. 再用 `G_1` response 运输同一个 first-stage displacement。

两种调度得到同一个 outer endpoint difference。

---

## 7. P018-T122 —— 精确 finite rectangle-variation identity

状态：`PROVED / EXECUTABLE`

由 T121 两式相减，得到

\[
\boxed{
\delta_G(F_1x)-\delta_G(F_0x)
=
\mathscr R_{G_1}(F_0x,h)
-
\mathscr R_{G_0}(F_0x,h).
}
\]

其中

\[
h=F_1x-F_0x.
\]

左边描述：**操作族 `G_0/G_1` 之间的 pointwise defect 沿 first-stage displacement 改变了多少。**

右边描述：**同一个 displacement 经过 `G_1` 与 `G_0` 后，response 相差多少。**

二者严格相等。

这可以看作一个完全有限、无极限的 rectangle variation law。

目前不把它命名为“曲率定理”，因为那会暗示额外几何结构。它只是一个精确整数恒等式。

---

## 8. P018-T123 —— T102 common-suffix propagation 是 rectangle 的退化情形

状态：`PROVED / EXECUTABLE`

若

\[
G_0=G_1=G,
\]

则

\[
\delta_G\equiv0.
\]

T121 退化为

\[
\boxed{
\Omega(x)
=
\mathscr R_G(F_0x,F_1x-F_0x).
}
\]

这正是 Supplement 11 的 T102 common-suffix holonomy propagation。

所以 T102 不是孤立公式，而是完整 2×2 rectangle 的一条退化边界。

---

## 9. P018-T124 —— common-prefix 退化

状态：`PROVED / EXECUTABLE`

若

\[
F_0=F_1=F,
\]

则

\[
h=0,
\]

因此

\[
\mathscr R_{G_0}(F(x),0)
=
\mathscr R_{G_1}(F(x),0)
=0.
\]

outer holonomy 退化为

\[
\boxed{
\Omega(x)=\delta_G(F(x)).
}
\]

即纯粹是在同一个 intermediate state 上比较两个后续操作。

---

## 10. P018-C10 —— outer flatness 不推出 local flatness

状态：`COUNTEREXAMPLE / DESIGN WARNING`

取自然状态 `x≥1`，令

\[
F_0(x)=x,
\qquad
F_1(x)=x+1,
\]

\[
G_0(y)=y,
\qquad
G_1(y)=\max(y-1,0).
\]

则

\[
G_0(F_0(x))=x,
\]

而

\[
G_1(F_1(x))=x.
\]

所以

\[
\boxed{\Omega(x)=0.}
\]

但 first-stage displacement 为

\[
F_1(x)-F_0(x)=1\ne0,
\]

且

\[
\delta_G(F_1(x))=-1\ne0.
\]

两个局部非零 defect 精确抵消。

因此：

\[
\boxed{
\text{outer confluence / zero holonomy}
\not\Rightarrow
\text{every local square is flat}.
}
\]

这是后续所有 confluence 解释必须保留的硬边界。

---

## 11. P018-T125 —— P003 collapse commutation 是 outer holonomy 的零分类

状态：`DERIVED FROM P003`

固定正指数 `p,q`，取

\[
F_0=C_q,
\qquad
F_1=C_p,
\]

\[
G_0=C_p,
\qquad
G_1=C_q.
\]

则 outer holonomy 为

\[
\Omega_{p,q}(n)
=
C_q(C_p(n))-C_p(C_q(n)).
\]

P003 已证明：

\[
\boxed{
\Omega_{p,q}(n)=0\ \forall n
\iff
p\mid q\ \text{或}\ q\mid p.
}
\]

所以 P003 可以被严格重述为：

> 完全幂 collapse family 的 2×2 operation rectangle 全局 outer-flat，当且仅当指数在整除序下可比。

这里没有改变 P003 本身，只是把它嵌入更一般的 critical-grid 语言。

---

## 12. P018-T126 —— P009 nonconfluence 属于 nonzero outer pair，而不是 Pair 拼接失败

状态：`STRUCTURAL REINTERPRETATION`

P009 已证明 mixed collapse/project scheduling 一般不合流。

Supplement 12/13 说明：

- State Pair 的拼接本身始终严格；
- nonconfluence 表现为 outer endpoint pair 不在 diagonal：

\[
(a,d)\notin\Delta;
\]

- 在整数坐标下等价于

\[
\Omega=d-a\ne0.
\]

因此 P009 的“不合流”并不是底层路径拼接失效，而是**不同调度得到不同 endpoint**。

这是很重要的分层：

\[
\text{path composition can be strict}
\quad\text{while}\quad
\text{path endpoints fail to coincide}.
\]

---

## 13. P018-T127 —— P010 confluence 是 outer pair 落入 diagonal

状态：`DERIVED FROM T110—T118 / P010`

设两条历史路径经过当前累计动力学后得到两个 endpoint。

它们合流当且仅当 endpoint pair 落入 diagonal：

\[
\boxed{(a,d)\in\Delta\iff a=d.}
\]

一旦再施加共同确定性 suffix，diagonal 仍然被映到 diagonal。

所以 P010 的“历史一旦合流就不能由确定性后续重新分叉”在 rectangle 语言中变成：

> outer pair 一旦进入 diagonal，所有共同 suffix 下的 outer pair 仍在 diagonal。

结合 C10，必须区分：

- outer diagonal：最终两路径当前不可区分；
- local flatness：每个局部 defect 都为零。

前者不推出后者。

---

## 14. P018-T128 —— P020 stabilization 提供 canonical diagonal sink，但不抹掉前史

状态：`DERIVED CONNECTION / NOT A NEW P020 THEOREM`

P020 对良基偏序上的单调向下映射 `F` 构造有限稳定化

\[
\operatorname{stabilize}_F.
\]

对 State Pair `(x,y)` 施加同一个 stabilization suffix 得到

\[
(\operatorname{stabilize}_F(x),
 \operatorname{stabilize}_F(y)).
\]

若两者拥有同一个最大不动点，则 pair 落入 diagonal。

这给出一个 canonical deterministic merging mechanism。

但 C10 告诉我们：即使最终 pair 落入 diagonal，也不能据此反推中间每一步都交换或每个局部 defect 为零。

因此 P020 提供的是 canonical sink/normal-form 结构，不是 local path-flatness 定理。

---

## 15. 当前底层结构被进一步压缩

到 T128 为止，可以更明确地区分四层：

### 第一层：Path / Pair

只需要类型和确定性函数：

\[
\boxed{
\text{typed State}
+\text{parallel endpoint Pair}
+\text{adjacent-pair composition}.
}
\]

这一层已经足以表达：

- path comparison；
- kernel/diagonal；
- deterministic merging；
- 2×2 outer endpoint interchange。

### 第二层：Difference coordinate

当状态允许整数坐标化时：

\[
(a,d)\leftrightarrow(a,d-a).
\]

得到：

- signed holonomy；
- finite response；
- rectangle variation identity；
- carry/borrow transport。

### 第三层：Precision / operation structure

加入：

- P005 typed scale；
- P008 adjunction/projection；
- operation families；
- carry cocycle；
- atlas / representation obstruction。

### 第四层：global certificates / time

加入：

- P010 history merging；
- P011 irreversibility spectra；
- P017 global certificates；
- P019/P020 stabilization。

因此当前更稳的候选顺序是

\[
\boxed{
\text{typed State}
\to
\text{Path Pair / kernel}
\to
\text{optional Difference coordinate}
\to
\text{response/holonomy}
\to
\text{precision/operation atlas}
\to
\text{global irreversibility/certificate/stabilization}.
}
\]

---

## 16. 为什么仍不宣布 2-category

T120 确实给出了一个严格的 rectangle endpoint interchange。

但完整 categorical 宣称仍需额外回答：

1. 2-cell 的对象究竟是 endpoint pair、path pair、rewrite witness 还是 defect class；
2. 水平/垂直组合是否对所有 typed arrows 封闭；
3. 单位 2-cell 应取什么；
4. 若 quotient 掉中间路径信息，哪些信息被不可逆丢失；
5. numeric defect 在 representation change 下是否为自然对象；
6. nondeterministic relation/spans 加入后是否仍保留相同 interchange。

因此当前最合适的表述是：

> **我们已经证明了一个 subtraction-free endpoint-pair rectangle interchange，以及它在整数 Difference 坐标下的 exact finite shadow。**

这比直接贴上 2-category 标签更强，因为它明确知道哪些公理真的用到了、哪些还没有。

---

## 17. 可执行与形式化验证

新增：

- `src/enterprise_math/critical_grid.py`
- `tests/test_critical_grid.py`
- `EnterpriseMath/State/CriticalGrid.lean`

验证目标包括：

1. generic State Pair 两条 rectangle 分解得到同一个 outer pair；
2. numeric outer holonomy 两种分解严格一致；
3. finite rectangle-variation identity；
4. common-prefix / common-suffix 退化；
5. outer zero + local nonzero 的抵消反例；
6. P003 可比指数给出 zero outer holonomy；
7. P003 不可比指数给出显式 nonzero outer holonomy。

Lean 优先验证 T119/T120 的完全无代数版本，以及整数坐标下的 telescoping rectangle identity。

---

## 18. 下一步开放问题

### P018-Q100 —— grid 是否能从 rectangle 推广到有限 cell complex？

不是先引入拓扑，而是先研究有限 path network 中 endpoint-pair 拼接是否给出规范的 outer comparison，以及不同 cell decomposition 是否保留相同 pair/kernel 信息。

### P018-Q101 —— kernel partition 与 grid refinement

把一条 coarse rectangle 细分成多个小 rectangle 时，哪些 kernel/diagonal 信息严格保持，哪些 numeric local defect 会重分配？

### P018-Q102 —— local defect cancellation 的 certificate

C10 说明 local defect 可抵消。寻找完全整数化的 cancellation certificate，区分：

- genuine local flatness；
- nonzero defects 的精确抵消；
- 经过 coarse projection 后才变得不可见的 defect。

### P018-Q103 —— Pair 层上的 P011 高阶不可逆性谱

P011 collision polynomial 统计的不只是 pair collision。下一步应从 kernel pair 出发恢复 higher-order fiber combinatorics，证明 Pair/kernel 是底层 substrate，而 P011 spectrum 是其高阶组合统计。

### P018-Q104 —— P020 coalescence time

对共同 deterministic dynamics，定义两个初态首次进入 diagonal 的有限时间。研究在 P020 良基向下系统中，coalescence time 是否有 canonical bound，以及它和 stabilizationSteps 的关系。

---

## 19. 当前结论

本阶段最重要的不是得到一个新术语，而是把“interchange”压到了一个几乎不可再削弱的有限事实：

\[
\boxed{
(a,b)\star(b,d)
=
(a,d)
=
(a,c)\star(c,d).
}
\]

只要两条复合路径拥有明确 endpoint，2×2 rectangle 的 outer pair 与内部选择哪条分解无关。

整数结构加入后，它变成两条精确的 finite holonomy decomposition，以及 rectangle-variation identity。

因此目前可以更有把握地说：

\[
\boxed{
\text{Pair/kernel 是路径逻辑；}
\quad
\text{Difference/holonomy 是它的数值坐标；}
\quad
\text{nonconfluence 是 outer pair 不在 diagonal。}
}
\]

这一分层同时容纳 P003、P009、P010、P020，而没有删除它们各自更具体的结构。

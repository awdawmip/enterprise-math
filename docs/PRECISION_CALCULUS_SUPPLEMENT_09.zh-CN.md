# P018 —— 有限精度证明演算：补充 09

状态：`ACTIVE RESEARCH NOTE`  
范围：operation-scheduling holonomy、defect transport、跨尺度组合律与严格恢复阈值  
依赖：P018-T11、T12、T72、T73、T75、T87  
纪律：本文不把“holonomy”一词本身当作新发现。真正需要检验的是：已有 collapse/refinement noncommutation 是否满足一个精确、有限、可组合且不依赖隐藏连续体的路径差演算。

## 1. T87 以后真正应寻找什么

Supplement 08 的 T87 已证明：如果路径上只有 canonical precision projections，而且这些投影只依赖起终点，那么所谓 endpoint-defect path curvature 自动为零。

因此，非零 path effect 必须来自真正改变运算顺序的路径。

P018 第一阶段其实已经给出了最小实例。对 `d|e`，定义

\[
S_{p,d}(n)=R_p(nd^p),
\qquad
C_{p,d}(n)=S_{p,d}(n)^p,
\]

并定义“在细层 collapse 后再投到粗层”

\[
\mathcal R_{p;e\to d}(n)
=
C_{p,e}(n)//(e/d)^p.
\]

T11 已定义

\[
\chi_{p;e:d}(n)
=
\mathcal R_{p;e\to d}(n)-C_{p,d}(n)
\ge0.
\]

现在把它重新放回路径语言：

\[
\boxed{
\chi_{p;e:d}(n)
=
(\text{refine to }e\to\text{collapse}\to\text{project to }d)
-
(\text{collapse at }d).
}
\]

这不是纯 projection path 的坐标差，而是 **collapse 与 precision projection 的 operation-scheduling holonomy**。

本文不改变 T11 的定理内容，只补上它在新 atlas/defect 框架中的正确位置。

---

## 2. P018-T88 —— 一般非负 defect transport

状态：`PROVED`

固定 `m>=1`。对一个显式整数基态 `a>=0` 与非负 defect `h>=0`，定义

\[
\boxed{
\mathcal T_m(a,h)
=Q_m(a+h)-Q_m(a)
=
(a+h)//m-a//m.
}
\]

它表示：在投影前给 fine state 增加 `h`，这个差异投到 coarse layer 后还能留下多少。

写

\[
a=mA+u,
\qquad
h=mH+v,
\qquad
0\le u,v<m.
\]

由 T72 的加法 carry 立刻得到

\[
\boxed{
\mathcal T_m(a,h)
=
H+\kappa_m(u,v)
=
Q_m(h)+\kappa_m(a\bmod m,h\bmod m).
}
\]

因此 defect transport 分成两部分：

\[
\boxed{
\text{transported defect bulk}
+
\text{boundary-crossing carry}.
}
\]

这第一次把 T72 的 carry 从“普通加法”直接接到真正的 operation path defect。

---

## 3. P018-T89 —— defect transport 满足严格跨尺度 coherence

状态：`PROVED`

对 `m,n>=1`，有

\[
\boxed{
\mathcal T_{mn}(a,h)
=
\mathcal T_m\bigl(Q_n(a),\mathcal T_n(a,h)\bigr).
}
\]

### 证明

由整数商的复合律

\[
Q_m(Q_n(x))=Q_{mn}(x),
\]

并且

\[
Q_n(a+h)
=Q_n(a)+\mathcal T_n(a,h).
\]

于是

\[
\begin{aligned}
\mathcal T_m(Q_n(a),\mathcal T_n(a,h))
&=Q_m(Q_n(a)+\mathcal T_n(a,h))-Q_m(Q_n(a))\\
&=Q_m(Q_n(a+h))-Q_m(Q_n(a))\\
&=Q_{mn}(a+h)-Q_{mn}(a)\\
&=\mathcal T_{mn}(a,h).
\end{aligned}
\]

∎

所以 defect transport 本身虽然包含 carry，却沿 canonical precision chain 严格可组合。

这给出一个重要结构：

> **原 operation 可以与 projection 不交换，但它产生的 path defect 仍可以拥有自己的 coherent transport law。**

这比要求原运算强行严格自然更弱，也更符合有限精度算术。

---

## 4. P018-T90 —— collapse holonomy 的精确跨层组合律

状态：`PROVED`

设

\[
d\mid e\mid f,
\qquad
r=e/d,
\qquad
m=r^p.
\]

简写

\[
\chi_{e:d}=\chi_{p;e:d}(n),
\qquad
\chi_{f:e}=\chi_{p;f:e}(n),
\qquad
\chi_{f:d}=\chi_{p;f:d}(n).
\]

则

\[
\boxed{
\chi_{f:d}
=
\chi_{e:d}
+
\mathcal T_{r^p}\bigl(C_{p,e}(n),\chi_{f:e}\bigr).
}
\]

再代入 T88，得到完全展开式：

\[
\boxed{
\chi_{f:d}
=
\chi_{e:d}
+
Q_{r^p}(\chi_{f:e})
+
\kappa_{r^p}
\bigl(
C_{p,e}(n)\bmod r^p,
\chi_{f:e}\bmod r^p
\bigr).
}
\]

### 证明

首先，整数投影路径严格相容：

\[
\mathcal R_{p;f\to d}(n)
=
Q_{r^p}(\mathcal R_{p;f\to e}(n)).
\]

又由定义

\[
\mathcal R_{p;f\to e}(n)
=C_{p,e}(n)+\chi_{f:e}.
\]

因此

\[
\begin{aligned}
\chi_{f:d}
&=Q_{r^p}(C_{p,e}+\chi_{f:e})-C_{p,d}\\
&=[Q_{r^p}(C_{p,e})-C_{p,d}]\\
&\quad+[Q_{r^p}(C_{p,e}+\chi_{f:e})-Q_{r^p}(C_{p,e})]\\
&=\chi_{e:d}
+\mathcal T_{r^p}(C_{p,e},\chi_{f:e}).
\end{aligned}
\]

再用 T88 即得第二式。∎

### 关键含义

collapse holonomy **不是简单相加**。

上层 path defect 向下传递时：

1. 整块跨过 `r^p` 的部分直接成为 coarse defect；
2. 剩余 detail 只有在与当前 coarse-boundary residue 合起来越界时，才额外产生一个 carry。

所以新得到的统一链是：

\[
\boxed{
\text{operation noncommutation}
\to
\text{local holonomy}
\to
\text{precision transport}
\to
\text{carry cocycle}.
}
\]

这把早期 T11 与新 T72/T73 真正接成同一套演算。

---

## 5. P018-T91 —— coarse layer 何时完全看不见一个 fine holonomy

状态：`PROVED`

对 `m>=1`、`a,h>=0`，写

\[
u=a\bmod m.
\]

则

\[
\boxed{
\mathcal T_m(a,h)=0
\iff
u+h<m.
}
\]

等价地，

\[
\boxed{
\mathcal T_m(a,h)=0
\iff
h<m-(a\bmod m).
}
\]

### 证明

`Q_m(a+h)=Q_m(a)` 当且仅当 `a+h` 仍留在 `a` 所在的同一个 quotient fiber；该 fiber 从余数 `u` 到下一边界只剩 `m-u` 个整数单位。∎

因此有限精度不是把所有 fine difference 按比例“缩小”成一个实数误差。

一个 fine path defect 要么：

- 完全留在同一个 coarse fiber，粗层严格看不见；
- 要么跨过有限边界，粗状态发生一个或多个离散跳变。

这就是一种真正的**有限分辨率可见性阈值**。

---

## 6. P018-T92 —— 精化恢复何时严格增加的充要条件

状态：`PROVED`

仍设

\[
d\mid e\mid f,
\qquad
m=(e/d)^p.
\]

T12 已证明

\[
\mathcal R_{p;e\to d}(n)
\le
\mathcal R_{p;f\to d}(n).
\]

现在可以精确刻画什么时候严格：

\[
\boxed{
\mathcal R_{p;f\to d}(n)
>
\mathcal R_{p;e\to d}(n)
}
\]

当且仅当

\[
\boxed{
\chi_{p;f:e}(n)
\ge
m-igl(C_{p,e}(n)\bmod m\bigr).
}
\]

### 证明

两恢复状态之差正好是

\[
\mathcal T_m(C_{p,e},\chi_{f:e}).
\]

由 T91，它严格大于零当且仅当

\[
(C_{p,e}\bmod m)+\chi_{f:e}\ge m.
\]

整理即得。∎

所以 T12 的“单调恢复”现在从一个弱单调性升级成了一个**严格事件判据**：

> 更高精度只有在新增 operation holonomy 真正撞穿下一条 coarse fiber boundary 时，才会改变已经观察到的粗恢复状态。

这与 P010 的严格历史合流判据在形式上出现值得继续研究的共同模式：

- 时间侧：只有新碰撞发生时，历史 multiplicity 才严格增加；
- 精度侧：只有新 boundary crossing 发生时，恢复状态才严格增加。

这里仅记录共同的“event-triggered monotonicity”骨架；目前**不宣称二者已经构成 categorical duality**。

---

## 7. 一个最小非零 holonomy 例子

沿用 T11 的例子：

\[
n=3,
\quad p=2,
\quad d=1,
\quad e=10.
\]

粗路径：

\[
C_{2,1}(3)=1.
\]

细路径：

\[
S_{2,10}(3)=17,
\qquad
C_{2,10}(3)=289,
\qquad
289//100=2.
\]

因此

\[
\boxed{
\chi_{2;10:1}(3)=1.
}
\]

这现在可以明确解释为：

\[
\boxed{
\text{collapse 与 projection 的最小 operation-scheduling holonomy}=1.
}
\]

它不是两条 scale-only paths 的 chart disagreement，而是同一起点、同一最终粗类型下，不同 operation ordering 的真实状态差。

---

## 8. 对底层逻辑的进一步反哺

Supplement 08 的候选底层为：

\[
\text{typed finite states}
+\text{projection/adjunction}
+\text{defect}
+\text{obstruction}
+\text{atlas/coherence}.
\]

本阶段补上一个此前缺失的动作层：

### Layer 4a —— Operation-labelled paths

一条路径不只记录尺度箭头，还记录何时执行 operation。

### Layer 4b —— Path holonomy

同起终点的两条 typed operation paths 可以有非零有限差：

\[
H(\gamma_1,\gamma_2)
=\operatorname{out}(\gamma_1)-\operatorname{out}(\gamma_2).
\]

### Layer 4c —— Defect transport

path defect 不是裸值；当观察精度继续变化时，它通过

\[
\mathcal T_m(a,h)
\]

被运输，而且 transport 满足 T89 coherence。

所以目前更完整的候选基础是：

\[
\boxed{
\text{states/types}
\to
\text{projections/adjunctions}
\to
\text{operations}
\to
\text{exact defects}
\to
\text{representation obstruction}
\to
\text{atlas}
\to
\text{operation paths + coherent defect transport}.
}
\]

这比“所有图都应交换”更自然：某些图可以不交换，但**不交换量本身必须是有限、显式、可运输、可组合的数学对象**。

---

## 9. 可执行压力测试

新增 `src/enterprise_math/precision_holonomy.py` 与 `tests/test_precision_holonomy.py`，对小有限域验证：

1. T88 defect transport = quotient difference；
2. T88 bulk + carry 展开式；
3. T89 两级 transport coherence；
4. T90 collapse holonomy composition；
5. T91 zero-visibility threshold；
6. T92 strict recovery criterion。

计算只用于反例搜索与实现核验，不替代理论证明。

---

## 10. 下一阶段开放问题

### P018-Q86 —— multiplication/power defect 是否共享同一 transport law？

transport 本身只依赖 coarse projection 与一个非负 state difference，因此可能比 carry cocycle 更普适。应检查 P018 已有乘法/幂 naturality defect 是否都可嵌入同一个 `T_m(a,h)` 框架。

### P018-Q87 —— signed defect transport

把 `h` 扩展为可正可负的 path difference 时，单一非负 `T_m` 不再足够；需要 carry/borrow 统一的 signed transport，并明确其 composition law。

### P018-Q88 —— operation-path 2-cell

为“project / collapse / add / multiply”等 typed arrows 建立最小 2-cell 语言，使 noncommuting square 的 defect 与 T89 transport 成为可证明结构，而不是图示比喻。

### P018-Q89 —— 多菱形 holonomy 组合

串联多个 operation-scheduling diamonds，研究总 holonomy 是否完全由局部 holonomy + canonical transport 递归决定；若否，最小缺失数据是什么？

### P018-Q90 —— 与 P017 global certificate 接轨

检验 P017 中 carry/shell/factor-precision 的局部 defect 是否也能先形成 path holonomy，再由 transported defect budget 汇总成全局 certificate。

---

## 11. 当前结论

本阶段把 T87 后“真正的非零路径效应从哪里来”回答到了第一个严格实例：

\[
\boxed{
\chi_{p;e:d}
=\text{collapse/refinement operation-scheduling holonomy}.
}
\]

它沿精度继续粗化时遵守

\[
\boxed{
\chi_{f:d}
=
\chi_{e:d}
+
\mathcal T_{(e/d)^p}(C_{p,e},\chi_{f:e}),
}
\]

而

\[
\boxed{
\mathcal T_m(a,h)
=Q_m(h)+\kappa_m(a\bmod m,h\bmod m).
}
\]

所以 carry 不再只是独立的算术现象，而成为**真实 operation holonomy 跨精度传播时的边界修正项**。

这使目前最值得继续推进的底层原则变得更具体：

> **允许非交换，但要求非交换量有限化；允许 defect，但要求 defect 有 canonical transport；允许多路线，但要求路线差能够在同一 typed atlas 中比较与组合。**
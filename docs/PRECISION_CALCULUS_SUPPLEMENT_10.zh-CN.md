# P018 —— 有限精度证明演算：补充 10

状态：`ACTIVE RESEARCH NOTE`  
范围：signed operation holonomy、signed defect transport、状态层与差分层分离  
依赖：P006、P009-C02、P018-T76—T81、T88—T92  
纪律：整数作为自然数加法幺半群的 Grothendieck group completion、Euclidean division、group completion 都是成熟数学。本文研究它们如何避免把“负的路径差”误写成“底层状态必须为负”。

## 1. 为什么 T88 的非负 defect 还不够一般

Supplement 09 研究的 collapse/refinement holonomy

\[
\chi_{p;e:d}(n)\ge0
\]

天然非负，因此可以先用

\[
\mathcal T_m(a,h),
\qquad h\in\mathbb N
\]

描述其向粗层传播。

但 P009-C02 已经证明，一般的 collapse/project 混合调度不合流。对同一起点的两条路径，终点差并没有固定符号。

因此一般 path holonomy 不应被定义成“非负损失”，而应是**有方向的状态差**。

这迫使我们区分两个问题：

1. 底层状态是否允许负数；
2. 两个非负状态之间的有向差是否允许为负。

第二个问题显然需要 `Z`，但它并不自动回答第一个问题。

---

## 2. P018-T93 —— collapse/project scheduling holonomy 对每个 `p>=2` 都可正可负

状态：`PROVED`

固定 `p>=2`、`r>=2`，对自然数状态定义有向调度差

\[
\boxed{
H_{p,r}(m)
=
C_p(Q_r(m))-Q_r(C_p(m))
\in\mathbb Z.
}
\]

其中第一项对应

\[
\text{project}\to\text{collapse},
\]

第二项对应

\[
\text{collapse}\to\text{project}.
\]

即使固定 `r=2`，对每个 `p>=2`，`H_(p,2)` 都同时取正值和负值。

### 正值例子

取

\[
m=2.
\]

因为对任意 `p>=2`，

\[
C_p(2)=1,
\qquad
Q_2(2)=1,
\qquad
C_p(1)=1,
\]

所以

\[
\boxed{
H_{p,2}(2)
=1-0
=1.
}
\]

### 负值例子

取

\[
m=2^p.
\]

则

\[
C_p(2^p)=2^p,
\qquad
Q_2(C_p(2^p))=2^{p-1}.
\]

另一方面，

\[
Q_2(2^p)=2^{p-1}<2^p,
\]

所以其整数 `p` 次根仍为 `1`，从而

\[
C_p(2^{p-1})=1.
\]

于是

\[
\boxed{
H_{p,2}(2^p)
=1-2^{p-1}<0.
}
\]

∎

### 含义

一般 operation scheduling 的非合流不能被编码成一个只取自然数的“损失量”。

如果要保留路径方向，就必须允许 defect 本身带符号。

---

## 3. P018-T94 —— signed defect transport 仍由同一个 carry 公式控制

状态：`PROVED`

固定 `m>=1`。对任意

\[
a,h\in\mathbb Z,
\]

采用 Supplement 08 的 Euclidean decomposition：

\[
a=mA+u,
\qquad
h=mH+v,
\qquad
0\le u,v<m.
\]

定义 signed defect transport：

\[
\boxed{
\mathcal T_m^{\mathbb Z}(a,h)
=q_m(a+h)-q_m(a),
}
\]

其中 `q_m` 是带非负余数的 Euclidean/floor quotient。

则

\[
\boxed{
\mathcal T_m^{\mathbb Z}(a,h)
=q_m(h)+\kappa_m(\rho_m(a),\rho_m(h)).
}
\]

### 证明

由

\[
a+h=m(A+H)+(u+v),
\]

并且 `u,v` 都是 canonical residues，进一步把 `u+v` 分成

\[
u+v=m\kappa_m(u,v)+(u\oplus v).
\]

所以

\[
q_m(a+h)
=A+H+\kappa_m(u,v).
\]

减去 `q_m(a)=A` 即得。∎

### carry 与 borrow 的统一

当 `h<0` 时，`q_m(h)` 可以为负，而 `rho_m(h)` 仍是 `0,...,m-1` 的 canonical residue。

例如 `h=-1`：

\[
-1=m(-1)+(m-1).
\]

因此

\[
\mathcal T_m^{\mathbb Z}(a,-1)
=-1+\kappa_m(\rho_m(a),m-1).
\]

若 `rho_m(a)>0`，carry 项为 `1`，总 transport 为 `0`；若 `rho_m(a)=0`，carry 为 `0`，总 transport 为 `-1`。

传统上分别叫作“不借位”和“借位”的两种情况，在这里由**同一个 signed Euclidean carry 公式**统一产生。

所以：

\[
\boxed{
\text{carry / borrow}
=\text{同一个 signed defect transport 的正反方向现象}.
}
\]

---

## 4. P018-T95 —— signed defect transport 保持跨尺度 coherence

状态：`PROVED`

对任意 `m,n>=1` 与 `a,h in Z`，

\[
\boxed{
\mathcal T_{mn}^{\mathbb Z}(a,h)
=
\mathcal T_m^{\mathbb Z}
\bigl(
q_n(a),
\mathcal T_n^{\mathbb Z}(a,h)
\bigr).
}
\]

### 证明

Euclidean floor quotient 对正整数模数满足

\[
q_m(q_n(x))=q_{mn}(x).
\]

又有

\[
q_n(a+h)
=q_n(a)+\mathcal T_n^{\mathbb Z}(a,h).
\]

完全重复 T89 的计算即可。∎

因此 signed transport 并不会破坏 canonical precision chain 的组合一致性。

---

## 5. P018-T96 —— signed defect 的精确不可见窗口

状态：`PROVED`

固定 `m>=1` 与 `a,h in Z`。令

\[
u=\rho_m(a)\in\{0,\ldots,m-1\}.
\]

则

\[
\boxed{
\mathcal T_m^{\mathbb Z}(a,h)=0
\iff
-u\le h<m-u.
}
\]

### 证明

`T=0` 当且仅当

\[
q_m(a+h)=q_m(a).
\]

写 `a=mA+u`，这当且仅当

\[
mA\le mA+u+h<m(A+1),
\]

也即

\[
0\le u+h<m.
\]

整理得到

\[
-u\le h<m-u.
\]

∎

因此一个 coarse fiber 对 signed difference 的“不可见范围”不是以 `0` 为中心的对称误差条，而是由当前 residue 决定的有限整数窗口：

\[
\boxed{[-u,\ m-u)}.
\]

向上越过右边界产生正 coarse change；向下越过左边界产生负 coarse change/borrow。

---

## 6. P018-T97 —— 自然数状态不需要因为 signed holonomy 而扩成整数状态

状态：`PROVED COORDINATE FACT / ESTABLISHED ALGEBRAIC INTERPRETATION`

对任意两个自然数终点

\[
x,y\in\mathbb N,
\]

通过标准嵌入

\[
\iota:\mathbb N\hookrightarrow\mathbb Z
\]

定义有向路径差

\[
\boxed{
H(x,y)=\iota(y)-\iota(x)\in\mathbb Z.
}
\]

它满足：

\[
H(x,y)=0\iff x=y,
\]

以及

\[
\boxed{H(y,x)=-H(x,y).}
\]

所以即使 base state space 继续严格保持

\[
\mathbb N,
\]

路径比较层也天然可以使用

\[
\mathbb Z.
\]

### 成熟代数解释

`(Z,+)` 是 `(N,+)` 的标准 Grothendieck group completion。这里使用这一成熟结构只为表达一个基础分型：

\[
\boxed{
\text{state type}
\ne
\text{oriented difference type}.
}
\]

因此“我们需要负的 path defect”**不能**被当成“物理底层状态必须包含负数”的论据。

P006 的 signed physical-state extension 继续是独立问题；P018 的 signed defect layer 不替它作决定。

---

## 7. P018-T98 —— P009 非合流 holonomy 的进一步粗化由 signed transport 精确给出

状态：`PROVED`

固定 `p>=2`、`r,s>=1` 与自然状态 `m`。

定义两条 P009 调度路径在第一次共同尺度上的结果：

\[
A=Q_r(C_p(m)),
\qquad
B=C_p(Q_r(m)).
\]

有向 holonomy 为

\[
H=B-A\in\mathbb Z.
\]

如果随后只对两条结果共同执行同一个进一步 quotient `q_s`，那么新终点差满足

\[
\boxed{
q_s(B)-q_s(A)
=
\mathcal T_s^{\mathbb Z}(A,H).
}
\]

### 证明

因为 `B=A+H`，直接代入 signed transport 定义：

\[
q_s(A+H)-q_s(A).
\]

∎

所以 P009 的一般 signed nonconfluence 与 Supplement 09 的非负 collapse holonomy 现在共享同一个 transport 框架。

差别只在于：

- T11/T90 的特殊 holonomy 已知非负；
- P009 的一般 scheduling holonomy 可以任意取正负。

---

## 8. 对 P006 的直接反哺：把“signed state”与“signed defect”彻底拆开

P006 研究的问题是：自然状态本身是否需要带符号，以及负数根应采用 usual order 还是 magnitude semantics。

本阶段研究的是另一件事：即使所有状态始终是非负整数，两条合法路径的有向差仍然自然落在 `Z`。

因此底层不应写成：

> “因为 defect 可能为负，所以 state 必须为整数。”

更干净的分层是：

### State layer

\[
X_d\subseteq\mathbb N
\]

或项目最终选定的有限状态对象。

### Difference / defect layer

当状态对象拥有可取消的加法坐标时，把有向差放入其 group completion；当前自然数坐标的完成就是

\[
\mathbb Z.
\]

### Signed physical-state layer

只有物理/代数问题本身要求负状态时，才由 P006 决定是否扩展 base state ontology。

这避免把“比较工具”反向污染“状态本体”。

---

## 9. 对候选底层逻辑的第五层反馈

Supplement 08–09 已经形成：

1. typed states；
2. adjoint projections；
3. exact operation defects；
4. representation obstruction；
5. precision atlas；
6. operation-labelled paths；
7. coherent defect transport。

现在还应再明确一个类型区分：

### State object vs difference object

不再假设 defect 与 state 必须住在同一个集合。

在当前整数原型中：

\[
\boxed{
\text{state coordinate}:\mathbb N,
\qquad
\text{oriented defect coordinate}:\mathbb Z.
}
\]

更抽象地，如果未来某个 state coordinate 是 cancellative commutative monoid，可以考虑它的 group completion 作为 difference object；若不满足这些条件，则必须另找正确的比较对象，不能机械套用 `Z`。

这使底层框架更像：

\[
\boxed{
\text{State}
\xrightarrow{\text{paths}}
\text{State},
\qquad
\text{parallel-path comparison}
\to
\text{Defect group/object}.
}
\]

而不是把所有信息挤在一个万能数集里。

---

## 10. 可执行压力测试

新增 `src/enterprise_math/precision_signed_holonomy.py` 与 `tests/test_precision_signed_holonomy.py`，验证：

1. T93 对多个 `p` 的正负 scheduling holonomy 见证；
2. T94 signed bulk + carry 公式，包括负 `h`；
3. T95 signed transport coherence；
4. T96 signed invisibility window；
5. T98 P009 holonomy 的进一步 quotient transport。

---

## 11. 下一阶段开放问题

### P018-Q91 —— group completion 到底应属于基础还是只属于 defect 层？

当前证据支持“只放 defect/comparison 层”。继续寻找反例：是否存在核心 operation 本身迫使 base state 使用 group structure？

### P018-Q92 —— 非可取消状态对象的 defect 应落在哪里？

collapse 本身是多对一的，未来若状态坐标不再是自然数加法幺半群，Grothendieck completion 可能不适用。需要为一般 ordered/noncancellative state 寻找 comparison object。

### P018-Q93 —— signed holonomy 的 obstruction class

局部 signed difference 会随 chart/section 改变。研究哪些 signed path holonomies 只有 coordinate value，哪些具有跨 representation 的不可消除 class。

### P018-Q94 —— 2-cell / rewrite critical-pair 统一

P009 的 nonconfluence 本来就是 rewrite critical-pair 现象。研究是否可以把“critical pair + signed holonomy + transport”写成同一个 typed 2-cell 结构。

---

## 12. 当前结论

本阶段得到的关键不是“把自然数换成整数”，恰恰相反：

\[
\boxed{
\text{自然数状态可以保持不动，
而有向 defect 独立进入整数差分层。}
}
\]

一般 P009 operation scheduling holonomy 确实可正可负；但 signed Euclidean transport 仍由与无符号情形相同的 carry cocycle 控制，并保持跨尺度 coherence。

因此现在的底层候选进一步变成：

\[
\boxed{
\text{typed finite State objects}
+\text{separate Defect objects}
+\text{projection/adjunction}
+\text{operation paths}
+\text{exact holonomy}
+\text{coherent signed transport}
+\text{representation obstruction}
+\text{atlas/certificates/time}.
}
\]

这给 P006 一个重要保护边界，也给 P009 的一般非合流一个统一的定量语言：

> **负的路线差属于“路径比较”并不自动意味着负数必须属于“自然状态”。**
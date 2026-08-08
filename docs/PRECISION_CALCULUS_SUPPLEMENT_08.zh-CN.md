# P018 —— 有限精度证明演算：补充 08

状态：`ACTIVE RESEARCH NOTE`  
范围：P006/P018 带符号精度扩张、section-dependent carry、coboundary 变换与不可 strictify 的结构障碍  
依赖：P006、P008、P018-T63—T67  
纪律：群扩张、短正合列、2-cocycle、coboundary 与 extension class 都是成熟数学。本文的研究目标是判断这些成熟对象如何精确进入进取数论的有限精度底层，而不是重新命名后主张原创。

## 1. 为什么必须从 `N` 进一步检查 `Z`

Supplement 07 在自然数状态上证明：

\[
\Phi_m(n)=(n//m,n\bmod m)
\]

把自然数加法重写成“粗状态 + detail + carry”的 twisted monoid。

但标准群上同调所说的 carry cocycle 自然生活在带符号整数与循环商群之间。若不区分这两层，容易把以下两个陈述混为一谈：

1. `N` 上的 coarse/detail 分解形成带 carry 的交换幺半群；
2. `Z` 上的 residue quotient 形成真正的群扩张，并由 2-cocycle 分类其 section defect。

P006 已经证明：带符号扩展不是简单给自然数根“加一个负号”；通常整数序根与带符号模长根是不同结构。因此，这里同样必须显式说明采用哪一种带符号 quotient 语义。

本补充只研究**整数欧几里得分解 / residue quotient**，不修改 P006 已经区分开的两类根。

---

## 2. P018-T68 —— 带符号欧几里得精度分解

状态：`PROVED / ESTABLISHED`

固定整数 `m>=1`。对每个

\[
z\in\mathbb Z,
\]

存在唯一

\[
q_m(z)\in\mathbb Z,
\qquad
\rho_m(z)\in\{0,1,\ldots,m-1\}
\]

使得

\[
\boxed{z=mq_m(z)+\rho_m(z).}
\]

这里 `q_m` 采用与非负余数配套的 Euclidean/floor quotient，而不是向零截断 quotient。

因此，有限精度的 coarse/detail 坐标可以无缝覆盖负状态，只要 quotient convention 被固定为状态定义的一部分。

这与 P006 的设计纪律一致：**带符号状态必须显式选择序与商的语义，不能让编程语言默认除法替我们决定数学。**

---

## 3. P018-T69 —— 同一个 carry 精确控制带符号加法 defect

状态：`PROVED`

对 `x,y in Z`，写

\[
x=mq_x+r_x,
\qquad
y=mq_y+r_y,
\qquad0\le r_x,r_y<m.
\]

仍定义标准 carry

\[
\kappa_m(r_x,r_y)
=\left\lfloor\frac{r_x+r_y}{m}\right\rfloor
\in\{0,1\}.
\]

则

\[
\boxed{
q_m(x+y)
=q_m(x)+q_m(y)+\kappa_m(r_x,r_y).
}
\]

并且

\[
\boxed{
\rho_m(x+y)
=(r_x+r_y)\bmod m.
}
\]

### 证明

直接相加：

\[
x+y=m(q_x+q_y)+(r_x+r_y).
\]

再对 `r_x+r_y` 做唯一欧几里得分解即可。∎

所以 Supplement 07 的 carry defect 不是自然数边界效应；在正确的带符号 Euclidean quotient 下，它原样延伸到 `Z`。

---

## 4. P018-T70 —— `Z` 的 coarse/detail/carry 是一个真正的 twisted group

状态：`PROVED`

令

\[
D_m=\{0,1,\ldots,m-1\}
\]

并把它按模 `m` 加法识别为循环群 `Z/mZ` 的标准代表。

定义

\[
\Phi_m^{\mathbb Z}(z)
=(q_m(z),\rho_m(z)).
\]

在 `Z x D_m` 上定义

\[
(a,u)\boxplus(b,v)
=
\bigl(a+b+\kappa_m(u,v),(u+v)\bmod m\bigr).
\]

则

\[
\boxed{
(\mathbb Z,+)
\cong
(\mathbb Z\times D_m,\boxplus)
}
\]

作为群成立。

单位元为 `(0,0)`。逆元可以显式写出：

\[
\boxed{
-(a,0)=(-a,0),
}
\]

而当 `0<u<m` 时，

\[
\boxed{
-(a,u)=(-a-1,m-u).
}
\]

因为

\[
u+(m-u)=m
\]

恰好产生一个 carry，抵消粗坐标中的额外 `-1`。

这给出 carry/borrow 的一个带符号统一解释：**跨零或跨 digit boundary 的负向修正，不需要另造隐藏连续余量；它是同一个 extension algebra 中的逆元结构。**

---

## 5. P018-T71 —— carry 来自标准 residue extension 的 section defect

状态：`PROVED / ESTABLISHED EXTENSION THEORY INSTANCE`

考虑短正合列

\[
\boxed{
0
\longrightarrow\mathbb Z
\xrightarrow{\times m}
\mathbb Z
\xrightarrow{\rho}
\mathbb Z/m\mathbb Z
\longrightarrow0.
}
\]

取标准 section

\[
s:\mathbb Z/m\mathbb Z\to\mathbb Z,
\qquad
s([u])=u,
\qquad0\le u<m.
\]

section 一般不是群同态。它偏离同态的量为

\[
s(u)+s(v)-s(u+v)
=m\kappa_m(u,v).
\]

因此

\[
\boxed{
\kappa_m(u,v)
=
\frac{s(u)+s(v)-s(u+v)}{m}.
}
\]

这里右侧是精确整数，因为分子属于 kernel `mZ`。

所以 carry 的 cohomological 含义不是“把一个普通进位重新取名字”，而是：

> 选择 detail representative section 后，该 section 无法严格保持群运算；carry 是它落入 kernel 的精确 defect 坐标。

Daniel C. Isaksen, *A Cohomological Viewpoint on Elementary School Arithmetic* (American Mathematical Monthly, 2002, DOI `10.1080/00029890.2002.11919915`) 直接讨论 carrying、group extensions 与 cocycles。该成熟联系不属于进取数论原创。

---

## 6. P018-T72 —— 换 section 只会把 carry 改变一个 coboundary

状态：`PROVED / PRIOR-ART COHOMOLOGY PATTERN`

保留同一个 residue quotient，但把标准 section `s` 换成另一个 section `s'`。

任何这样的 section 都可写为

\[
s'(u)=s(u)+m h(u),
\]

其中

\[
h:\mathbb Z/m\mathbb Z\to\mathbb Z.
\]

令对应 defect 为

\[
\kappa'_m(u,v)
=
\frac{s'(u)+s'(v)-s'(u+v)}{m}.
\]

代入即得

\[
\boxed{
\kappa'_m(u,v)
=
\kappa_m(u,v)
+h(u)+h(v)-h(u+v).
}
\]

所以换 representative system 会改变局部 carry 数值，但变化项严格是一个 coboundary。

### 对 representation switch 的直接意义

这给 Supplement 07 的“换证明表示空间”纪律增加了更强版本：

> **局部 defect 可以依赖表示；真正值得提升到底层的不一定是某个具体 defect 表，而可能是所有表示变换下保持的 equivalence / cohomology class。**

因此未来研究 precision defect 时必须区分：

1. coordinate-dependent defect；
2. change-of-section law；
3. representation-invariant obstruction。

这可能成为判断“哪些量能反哺底层逻辑”的通用筛选器。

---

## 7. P018-T73 —— `m>1` 时 carry obstruction 不能被全局 strictify 掉

状态：`PROVED / ESTABLISHED GROUP-THEORETIC CONSEQUENCE`

当 `m>1` 时，短正合列

\[
0\to\mathbb Z\xrightarrow{\times m}\mathbb Z\to\mathbb Z/m\mathbb Z\to0
\]

**不分裂**。

### 初等证明

若该扩张分裂，则存在群同态 section

\[
s:\mathbb Z/m\mathbb Z\to\mathbb Z
\]

满足 quotient 后为恒等。

于是 `s(1)` 在 `Z` 中应具有阶 `m`。但加法群 `Z` 是 torsion-free：除 `0` 外没有有限阶元素。

矛盾。∎

因此不存在任何 section 能让其 cocycle 在所有输入上恒为零。

换言之：

\[
\boxed{
\text{carry 可以换坐标，
但当 }m>1\text{ 时不能被全局消灭。}
}
\]

这比“projection 不是同态”更强。后者可能只是坐标选择不佳；T73 说明在 signed group extension 中，**不存在某个更聪明的 representative choice 可以把整个 defect strictify 掉。**

这给出当前最强的候选底层原则：

> 某些有限精度 defect 应被理解为结构障碍，而不是计算误差；只有证明相应 extension/class 可平凡化时，才有资格把 defect 从底层删掉。

---

## 8. P006 与 P018 的边界现在更清楚

P006 已经区分：

- odd-power `orderRootOdd`；
- `magnitudeRoot`；
- `signedMagnitudeCollapse`。

本补充增加的 `q_m / rho_m` 是**另一条独立的 signed scale decomposition**，它不选择哪一种根，也不修正 P006 的已有结论。

所以带符号层至少有两个互不应混淆的问题：

1. **root semantics**：负数根到底跟随通常序，还是跟随模长；
2. **precision quotient semantics**：负状态如何分解成 coarse integer + canonical nonnegative residue。

二者可以组合，但不能互相替代。

这保持住 P006 路线，同时让 P018 得到真正的 group-extension 宿主。

---

## 9. 对底层逻辑的第三层候选反馈

Supplement 07 给出：

- Layer 0：order-adjoint core；
- Layer 1：defect-enriched operation core。

本补充提示再增加一个尚未封板的 Layer 2：

### Layer 2 —— Defect equivalence / obstruction layer

不把某个坐标下的 `D_f` 直接当成最终不变量，而记录：

\[
\boxed{
\text{defect}
+\text{change-of-representation law}
+\text{obstruction class}.
}
\]

其核心问题变成：

- 哪些 defect 能通过合法的表示变换消掉？
- 哪些只能改变代表而不能消灭？
- 哪些 extension/class 的非平凡性是有限精度结构本身的不可约信息？

对加法 carry，T72–T73 已经给出一个完整原型。

这可能比单独把“cocycle”作为新原语更稳健，因为它保留了**表示依赖量与结构不变量的区分**。

---

## 10. 从 carry obstruction 推向一般 precision obstruction

现在可以给一般 operation defect 提出一套更严格的研究流程。

给定某个 precision system 与 operation `f`：

### Step A —— 定义 defect

\[
D_f=\pi f-f\pi.
\]

### Step B —— 找合法表示变换

明确哪些 coordinate/section/representative change 不改变原问题语义。

### Step C —— 推导 defect transformation law

检查

\[
D_f\mapsto D'_f
\]

是否具有 coboundary、conjugacy、gauge transform 或其他成熟结构。

### Step D —— 找 obstruction

问是否存在合法表示使

\[
D'_f=0.
\]

如果存在，原 defect 更接近坐标伪影；如果不存在，则应寻找阻止 strictification 的不变量。

### Step E —— 才决定是否提升到底层

只有跨表示稳定、或能精确控制所有表示变化的结构，才有资格成为底层逻辑候选。

这是一条比“看到一个漂亮公式就加入基础”更强的防漂移规则。

---

## 11. 与 P017 global certificate 的新联系

P017 的 signed shell / carry / Möbius 项经常依赖具体分解方式。

T72 提醒我们：局部项本身发生变化不一定意味着证明结构发生变化。更好的问题可能是：

> P017 的不同分解、不同 anchor、不同 precision axis 之间，是否存在类似 change-of-section 的变换律，使总 certificate 落在同一个等价类？

如果能找到，则“global certificate”不必要求所有局部 decomposition 相同，只需证明：

1. 合法重表示只增加可控的 boundary/coboundary 项；
2. 最终 obstruction / total certificate 不变；
3. Legendre existence target 对这一不变量有确定符号或非消失条件。

这条路线目前是 `OPEN`，但它比单纯追求逐项正性更有结构性。

---

## 12. 与 P012 geometry 的新联系

P012 的 geometry 也应该应用同样筛选标准。

若某个 lattice lift、coset coordinate 或 embedding 改变以后，局部距离表达发生变化，则需要区分：

- 是几何本身改变；
- 还是只有坐标表达改变；
- 是否存在类似 gauge/coboundary 的等价关系；
- 哪些 shortest-path / quotient-fiber quantities 是表示不变量。

因此 P012 保留 primitive graph metric 作为最稳固基线，同时允许 derived geometry 通过“表示变换不变量”测试后逐步上升。

---

## 13. 下一阶段开放问题

### P018-Q69 —— signed carry 的 Lean 形式化

在 `Int.ediv / emod` 或 mathlib 当前规范整数除法上形式化 T68–T70，并核对负数 convention。

### P018-Q70 —— section-change/coboundary 的有限形式化

不必一开始引入完整 group-cohomology 库；先对有限 residue representatives 直接证明 T72。

### P018-Q71 —— non-splitting obstruction 形式化

形式化 `m>1` 时不存在 `Z/mZ -> Z` 的 additive section，并把它与“carry 不可全零化”连接起来。

### P018-Q72 —— 多精度 extension tower

对 `d|e|f`，研究嵌套 subgroup

\[
f\mathbb Z\subseteq e\mathbb Z\subseteq d\mathbb Z\subseteq\mathbb Z
\]

对应的 extension classes 如何组合，并与 T67 的 staged carry coherence 对接。

### P018-Q73 —— precision obstruction 的抽象定义

寻找一个弱到足以覆盖整数精度、强到足以谈 strictification obstruction 的抽象结构。不要预设必须使用完整 abelian category 或 derived functor。

---

## 14. 当前结论

Supplement 07 说明 carry 是 operation defect 与 cocycle data。

Supplement 08 再向下一层推进：

\[
\boxed{
\text{具体 carry table}
\quad\text{不是最终对象；}
}
\]

真正更稳定的层次是

\[
\boxed{
\text{section defect}
\longrightarrow
\text{coboundary change law}
\longrightarrow
\text{non-splitting obstruction / extension class}.
}
\]

所以目前底层逻辑的候选演进变成：

\[
\boxed{
\text{order adjunction}
\to
\text{typed precision projection}
\to
\text{exact defect}
\to
\text{coherence}
\to
\text{defect-equivalence / obstruction}
\to
\text{proof certificate and time dynamics}.
}
\]

其中最重要的新原则是：

> **先问 defect 能否被合法重表示 strictify，再决定它是不是底层结构。**

对 `m>1` 的 signed additive carry，答案已经是否定的：它可以换代表，但不能被全局消灭。
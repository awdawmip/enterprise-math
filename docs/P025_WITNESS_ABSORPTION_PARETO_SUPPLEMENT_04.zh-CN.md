# P025 补充 04 —— 吸收感知的 Pareto Witness Precision

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 01–03；Pasten arithmetic derivatives；P023 task-relative repair；A4 Pareto-antichain 语义  
创新状态：`MATHEMATICS MOSTLY STANDARD / PROJECT INTEGRATION NOVELTY_UNVERIFIED`

## 1. 为什么标量 witness 半径仍然过粗

补充 01 定义了第一可用 witness 半径

\[
\mu(a,b,c)=\min\{\|x\|_\infty:x\in T(a,b)\setminus T^\circ(a,b)\}.
\]

它回答的是一个未来问题：

> 为了让任意一个非退化 relation-adapted certificate 出现，整数 witness 搜索至少要打开到多大半径？

但它并不衡量 witness 对 radical collapse 所遗忘 multiplicity 信息吸收得有多紧。

经典 Mason–Stothers 证明和 Pasten 的 arithmetic-derivative 构造都不仅使用“非退化”这一事实：重复因子 residual 会被一个公共 Wronskian 吸收。因此同一个 witness 上天然还存在第二个精确整数成本。

本补充的目的，就是在把 witness precision 过早压成标量之前，先压力测试这个更丰富的未来语言。

## 2. Arithmetic derivative 与具有规范尺度的 Wronskian

固定 primitive 正整数三元组

\[
a+b=c,\qquad \gcd(a,b)=1,
\]

并令 prime-coordinate 集合

\[
S=\operatorname{supp}(abc).
\]

对整数坐标向量

\[
x=(x_p)_{p\in S},
\]

Pasten 的有限 support arithmetic derivative 为

\[
d_x(n)
=
 n\sum_{p\mid n}\frac{v_p(n)}p x_p.
\]

relation-adapted witness 格为

\[
T(a,b)=\{x:d_x(a)+d_x(b)=d_x(c)\}.
\]

定义实际 arithmetic Wronskian

\[
\boxed{
W_x(a,b)=a\,d_x(b)-b\,d_x(a).
}
\]

与仅用于恢复退化超平面的 primitive normal 不同，这个 Wronskian 带有**规范算术尺度**。一旦未来语言观察 `|W|`，这个尺度就不能再被约掉。

令

\[
M(a,b,c)
=
 m(a)m(b)m(c),
\qquad
m(n)=\frac{n}{\operatorname{rad}(n)}.
\]

## 3. P025-T11 —— 每个非退化 Wronskian 都吸收完整 multiplicity residual

对每个 additive witness `x in T(a,b)`，都有

\[
\boxed{
M(a,b,c)\mid W_x(a,b).
}
\]

因此对每个非退化 witness，

\[
\boxed{
\eta(x)
=
\frac{|W_x(a,b)|}{M(a,b,c)}
\in\mathbb N_{>0}.
}
\]

我们把 `eta(x)` 称为 witness 的**吸收冗余（absorption redundancy）**。

### 证明

对任意正整数 `n`，

\[
m(n)\mid d_x(n).
\]

原因是每一项

\[
\frac{n}{p}v_p(n)x_p
\]

都包含 `m(n)=prod p^(v_p(n)-1)` 的全部素数幂。

同时 `m(n)|n`。因此 `m(a)` 与 `m(b)` 都整除

\[
W_x(a,b)=a d_x(b)-b d_x(a).
\]

又因为 `x` 对 `a+b=c` 满足 additivity，

\[
d_x(c)=d_x(a)+d_x(b).
\]

于是

\[
W_x(a,c)
=a d_x(c)-c d_x(a)
=a d_x(b)-b d_x(a)
=W_x(a,b),
\]

所以 `m(c)` 也整除同一个 Wronskian。

primitive abc 条件使 `a,b,c` 两两互素，因此 `m(a),m(b),m(c)` 也两两互素，它们的乘积必整除 `W_x(a,b)`。∎

### 含义

`eta=1` 表示 Wronskian 恰好只携带一份被强制要求吸收的 residual 尺度；更大的 `eta` 表示 certificate 在 compulsory residual 之外还携带额外算术尺度。

它不是误差项，也不是浮点 quality score，而是一个精确正整数商。

## 4. P025-T12 —— 不可避免的吸收下界是 determinantal divisor

令

\[
\widehat\alpha\in\mathbb Z^S
\]

为补充 01 的 primitive additive normal，因此

\[
T=\ker_{\mathbb Z}\widehat\alpha.
\]

令

\[
\beta_{\rm raw}\in\mathbb Z^S
\]

为**未经 primitive 归一化**的 Wronskian 行，使得

\[
W_x(a,b)=\beta_{\rm raw}\cdot x.
\]

定义带尺度的 exterior signature

\[
\boxed{
\Omega
=
\widehat\alpha\wedge\beta_{\rm raw}
\in\bigwedge^2\mathbb Z^S.
}
\]

用 `cont(Omega)` 表示 `Omega` 全部 Plücker 坐标绝对值的 gcd。

则

\[
\boxed{
\beta_{\rm raw}(T)
=\operatorname{cont}(\Omega)\,\mathbb Z.
}
\]

特别地，所有 witness 能达到的最小正吸收冗余为

\[
\boxed{
\eta_{\min}(a,b,c)
=
\frac{\operatorname{cont}(\Omega)}{M(a,b,c)}.
}
\]

### 证明

由于 `alpha_hat` primitive，存在整数 unimodular 坐标变换把它送到第一坐标行 `e_1`。在该坐标下，

\[
T\cong\{(0,y_2,\ldots,y_s):y_i\in\mathbb Z\}.
\]

于是 Wronskian 在 `T` 上的像就是变换后 `beta_raw` 剩余坐标生成的整数子群，即 `d Z`，其中 `d` 是这些坐标的 gcd。

二行矩阵 `[alpha_hat; beta_raw]` 的全部 `2x2` minors 的 gcd 在 unimodular 列变换下不变。把 `alpha_hat` 送到 `e_1` 后，这些 minors（差一个符号）正好就是剩余的 Wronskian 系数。因此同一个 gcd 就是

\[
d=\operatorname{cont}(\widehat\alpha\wedge\beta_{\rm raw}).
\]

由 P025-T11，像中的所有值都被 `M` 整除；而 `d` 是该像的生成元，所以 `M|d`。除以 `M` 即得最小正 `eta`。∎

### 前人工作边界

这属于标准 Smith normal form / determinantal divisor / exterior algebra 数学在 Pasten witness 格上的应用。P025 不主张这些代数事实本身是新发现。

本项目真正需要记录的是：补充 02 中只按 projective 方向使用的同一个 exterior 对象，一旦未来语言开始询问 Wronskian 大小，其**content** 就变成了可观测信息。

## 5. N03 —— projective witness geometry 与 absorption-aware geometry 是不同精度任务

补充 02 使用

\[
\left(S,\widehat\alpha,
[\widehat\alpha\wedge\beta]
\right)
\]

恢复饱和格旗标

\[
T^\circ\subset T.
\]

对该任务而言，第二行的尺度无关紧要，因为它不改变 `T` 内部的退化超平面。

但 absorption observable 更丰富。把 Wronskian 行替换为

\[
\beta\mapsto\lambda\beta+\mu\widehat\alpha
\]

仍保持 `T` 内同一个超平面；可是限制在 `T` 上以后，Wronskian 的绝对值会被 `|lambda|` 缩放。

因此：

\[
\boxed{
\text{projective flag precision 足以恢复 witness geometry，但一般不足以恢复 Wronskian-scale cost。}
}
\]

若未来语言需要 absorption 信息，就必须保留 Wronskian functional 在 `T` 上的**带尺度限制**；等价地，需要保留带 content 的 exterior signature `Omega`（整体符号可忽略），以及足以恢复 `M` 的状态。

这再次直接体现 P023 规则：

> 对一个 future language 精确的 representation，在 future language 变丰富以后可能立刻变得过粗。

## 6. P025-D02 —— 二轴 witness cost

对每个非退化 witness 定义

\[
\boxed{
C(x)=
\left(
\|x\|_\infty,
\eta(x)
\right)
\in\mathbb N_{>0}^2.
}
\]

第一坐标是 prime-coordinate 格中的几何/搜索成本；第二坐标是算术吸收冗余。

按分量序定义

\[
(r,e)\preceq(r',e')
\iff
r\le r'\text{ and }e\le e'.
\]

令

\[
\boxed{
\mathcal P(a,b,c)
=
\operatorname{Min}_{\preceq}
\{C(x):x\in T\setminus T^\circ\}
}
\]

称为**吸收感知 Pareto witness frontier**。

这里不主张 Pareto order 是新数学。A3/A4 已经把 Pareto antichain 用于更弱的 future languages，有限 antichain 压缩也是标准序理论。P025 在这里消费该结构，而不是再造一个平行母理论。

## 7. P025-T13 —— 完整 Pareto frontier 有限，并且完备刻画二成本有界 certificate queries

考虑 future query language

\[
H_{K,E}(a,b,c)
=
1_{\exists x\in T\setminus T^\circ:
\|x\|_\infty\le K,\ \eta(x)\le E}.
\]

则：

1. `P(a,b,c)` 有限；
2. 对任意 `K,E`，
   \[
   \boxed{
   H_{K,E}=1
   \iff
   \exists(r,e)\in\mathcal P
   \text{ with }r\le K,e\le E;
   }
   \]
3. 全部 rectangle queries `H_(K,E)` 的真假值可以唯一恢复 Pareto frontier。

### 证明

全部成本对落在 `N_{>0}^2`。把 Pareto-minimal 点按第一坐标递增排列，则第二坐标必须严格递减；正整数不存在无限严格递减序列，所以 frontier 有限。这正是 Dickson lemma 的二维情形。

任意可行 witness 的成本都支配某个 Pareto-minimal 成本，因此 rectangle feasibility 完全由 frontier 决定。反过来，使 query 为真的阈值对 `(K,E)` 构成 witness cost set 的 upward closure，而该 upward closure 的最小元恰好就是 `P`。∎

### 架构含义

因此，一个无限的 candidate derivation 格，对这个声明过的 bounded-cost future language 可以存在一个有限且精确的 semantic summary。

这个 summary 既不是整个 witness 集，也不是单个标量，而是一组有限 task-relevant cost tradeoffs 组成的 antichain。

## 8. P025-N04 —— 标量 `mu` 会丢失真实 witness tradeoff

### 例 A：`2+3=5`

在 prime coordinates `(2,3,5)` 上，加法关系为

\[
x_2+x_3-x_5=0,
\]

并且

\[
W_x=2x_3-3x_2.
\]

这里 `M=1`，`eta_min=1`。

存在 radius-one witness，例如

\[
x=(0,1,1),
\qquad
(\|x\|_\infty,\eta)=(1,2).
\]

但第一组 perfect-absorption witness 可以取

\[
x=(1,1,2),
\qquad
(\|x\|_\infty,\eta)=(2,1).
\]

因此

\[
\boxed{
\mathcal P(2,3,5)=\{(1,2),(2,1)\}.
}
\]

标量半径只能告诉我们 `mu=1`，却无法回答是否能同时要求 `eta<=1`。

### 例 B：`2+7=9`

精确枚举配合 determinantal absorption floor 得到

\[
\boxed{
\mathcal P(2,7,9)
=
\{(1,3),(4,2),(5,1)\}.
}
\]

因此 cost tradeoff 可以有超过两个层级。

### 例 C：`5+7=12`

这里

\[
M=2,
\qquad
\eta_{\min}=2,
\]

且

\[
\boxed{
\mathcal P(5,7,12)
=
\{(1,6),(2,2)\}.
}
\]

所以即使无限扩大搜索，也不可能达到 `eta=1`：relation lattice 自身施加了不可消除的 absorption overhead。

这把标量 witness radius 混在一起的两个现象分开了：

- **search hardness** —— 在格上至少要走多远；
- **absorption obstruction** —— arithmetic functional 最紧能贴近 compulsory multiplicity residual 到什么程度。

## 9. 对无限 frontier 的构造性有限认证

可执行参考层并不枚举无限 witness 格。

它先从 scaled exterior signature 精确计算

\[
\eta_{\min}
=
\frac{\operatorname{cont}(\Omega)}M.
\]

然后逐步扩大有限 `L_infinity` ball，直到找到一个达到 `eta_min` 的 witness。

到这一刻 Pareto frontier 已经完整：所有尚未出现的 witness 都有更大的 norm，并且 `eta>=eta_min`，因此它要么被已经找到的 absorption-optimal 点支配，要么不可能再制造新的左下角极小点。

所以小 support reference oracle 获得了一个有限终止证书。

## 10. P025-T14 —— Mason 的 polynomial margin 精确分裂成 absorption slack 与 capacity slack

同样的二阶段结构，在经典 polynomial proof 中可以精确看见。

令

\[
D
=
\deg a+\deg b+\deg c
-
\deg\operatorname{rad}(abc)
\]

为 multiplicity residual `abc/rad(abc)` 的次数，令

\[
w=\deg W(a,b),
\]

以及

\[
C=\deg a+\deg b-1.
\]

经典证明给出

\[
D\le w\le C.
\]

针对 `c` 的 theorem margin 为

\[
\deg\operatorname{rad}(abc)-\deg c-1
=C-D.
\]

把实际 witness degree `w` 插入中间，得到

\[
\boxed{
\deg\operatorname{rad}(abc)-\deg c-1
=
\underbrace{(w-D)}_{\text{absorption slack}}
+
\underbrace{(C-w)}_{\text{capacity slack}}.
}
\]

两项都非负。

这只是从经典 Wronskian proof 中抽出的初等代数恒等式，并不主张它是新的 Mason–Stothers refinement。

### 为什么这个分裂对 P025 有价值

它把 proof bottleneck 分成两段：

1. **residual -> witness：** witness 比 compulsory repeated-factor residual 多装了多少；
2. **witness -> capacity：** 可用 Wronskian capacity 实际用了多少。

在整数路线中，`eta=|W|/M` 是第一个问题的乘法对应物，而 lattice norm / Geometry-of-Numbers bound 控制第二侧。Pasten 已经证明 sufficiently strong 的 witness-size 改进与 abc 紧密等价；P025 不把这一桥梁当成新发现。

## 11. 对进取数论 precision architecture 的反哺

P025 目前的推进链变成：

\[
\text{radical support}
\to
\text{multiplicity residual}
\to
\text{relation-conditioned witness flag}
\to
\text{scalar witness radius}\ \mu
\to
\boxed{\text{multi-cost Pareto witness precision}}.
\]

关键纠偏是：

\[
\boxed{
\text{certificate precision 没有理由天然是一维标量。}
}
\]

哪些 witness 差异必须保留，由声明的 certificate language 决定：

- 只问 non-degenerate existence -> flag geometry 可能足够；
- 只问 radius thresholds -> `tau_K(mu)` 可能足够；
- 同时问 radius + absorption thresholds -> Pareto antichain 是精确 semantic shadow；
- 询问实际 Wronskian values -> 还必须更完整地保留 scaled functional。

这正是 task-relative precision 原则，但这一次不是从架构偏好出发强加，而是从经典数论证明机制自身逼出来的。

## 12. 与 A2/P023 和 A4 的关系

### A2/P023

补充 03 的 `tau_K` 定理不应另行晋升为独立母定理。P023 Supplement 09 已经拥有更一般的 query-language equivalence-relation 与 minimum-repair calculus；`tau_K` 只是一个 nested threshold language 的闭式坐标。

新的二成本 rectangle language 同样属于 generic P023 query semantics 的特化。

### A4 / A3-A4 bridge

Pareto frontier 应复用 A3/A4 bridge 已经发展出的 antichain semantics。P025 不自动继承任何 A4 composition theorem：当前并没有证明 arithmetic-derivative witnesses 的 composition law。

真正可复用的只是：

\[
\text{infinite/multivalued witness family}
\to
\text{finite Pareto semantic shadow for a declared monotone query language}.
\]

## 13. 可执行资产

本阶段新增：

- `src/enterprise_math/abc_witness_absorption.py`
  - 带规范尺度的 arithmetic Wronskian row；
  - 精确 arithmetic derivative / Wronskian evaluation；
  - multiplicity-residual product；
  - 精确 absorption redundancy `eta`；
  - scaled exterior signature；
  - determinantal-divisor absorption floor；
  - 完整二成本 Pareto frontier 的 certified finite computation；
  - 显式 tradeoff 反例；
  - Mason degree-slack decomposition helper。
- `tests/test_abc_witness_absorption.py`
  - residual divisibility 样例；
  - `eta_min>1` 样例；
  - scaled exterior content 检查；
  - 二级和三级 Pareto frontiers；
  - Mason slack 分裂为独立 absorption/capacity channels。

有限枚举只属于 regression 与 exact-oracle evidence。一般命题由上面的证明支撑，而不是由枚举支撑。

## 14. 前人工作与创新纪律

本阶段消费的外部成熟数学包括：

- Mason–Stothers 与 Snyder 的 Wronskian proof，并由 Baek–Lee formalization 清晰暴露 [SRC-BAEK-LEE-2024-MASON-LEAN]；
- Pasten 的 relation-adapted arithmetic derivatives、Wronskians 与 Geometry-of-Numbers size program [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]；
- Smith normal form、determinantal divisors 与 exterior/Plücker coordinates；
- Dickson lemma 与 Pareto-antichain compression。

内部已经存在的母结构包括 P023 task-generated precision relations，以及 A3/A4 Pareto-antichain semantics。

精确 invariant `eta_min=cont(Omega)/M`、二成本 witness frontier 以及把它们作为进取数论 precision diagnostics 的用法，当前仍标记 `NOVELTY_UNVERIFIED`。在完成专项文献审计前，不作任何历史优先权声明。

## 15. 下一前沿

不存在 hard block。当前最强下一问题是：

1. 直接从 prime supports 与 valuation exponents 推出 `eta_min` 的闭式算术公式，完全消除 witness-lattice 枚举；
2. 分类 `eta_min=1` 的充要条件，并识别 unavoidable `eta_min>1` 的族；
3. 比较 high-abc-quality triples 的 absorption floor 与 Pareto frontier，但绝不把有限数据当成证明；
4. 测试 Pasten 的 Geometry-of-Numbers witness bounds 能否表述成对 Pareto front 的界，而不是只界一个 scalar norm；
5. 判断其中哪些内容其实已经隐含在 Pasten 的格证明中，并在适当处降格为 `ADOPT/REINTERPRET`；
6. 只有完成上述审计以后，才判断 generic multi-cost certificate structure 是否值得从 P025 回流到更高母层。

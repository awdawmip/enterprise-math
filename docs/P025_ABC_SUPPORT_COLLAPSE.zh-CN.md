# P025 —— ABC Radical-Support 坍缩压力测试

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
范围：普通数学 + 进取数论架构压力测试  
硬阻断：`NONE`

> 本文不声称证明 ABC 猜想。任何有限计算、经验排序、架构类比或 witness 试验均不得升级为 ABC 证明。

## 1. 研究入口

对正整数 `n` 定义

\[
\operatorname{rad}(n)=\prod_{p\mid n}p.
\]

若把整数写成素因子指数向量

\[
V(n)=(v_p(n))_p,
\]

则 `rad` 只保留 support：

\[
(v_p(n))_p\longmapsto (1_{v_p(n)>0})_p.
\]

因此在进取数论语言里，`rad` 是一个极强的 multiplicative-support collapse：它忘掉全部重复指数，只保留哪些素数出现。

为把被忘掉的信息显式化，定义

\[
m(n)=\frac{n}{\operatorname{rad}(n)}.
\]

于是始终有精确分解

\[
\boxed{n=\operatorname{rad}(n)m(n).}
\]

这里 `m(n)` 称为 **multiplicity residual / 重数残差**。这个分解本身是普通算术，不是项目新定理。

## 2. P025-T01 —— primitive abc 三元组的 support 两两不交

设

\[
a+b=c,\qquad \gcd(a,b)=1.
\]

则

\[
\gcd(a,c)=\gcd(a,a+b)=1,
\qquad
\gcd(b,c)=\gcd(b,a+b)=1.
\]

所以 `a,b,c` 两两互素，它们的素因子 support 两两不交。因此

\[
\boxed{
\operatorname{rad}(abc)
=\operatorname{rad}(a)\operatorname{rad}(b)\operatorname{rad}(c).
}
\]

同时

\[
\boxed{
abc=\operatorname{rad}(abc)m(a)m(b)m(c).
}
\]

### 架构含义

ABC 的困难不是三个输入的 prime support 相互碰撞；primitive 条件已经把这种碰撞消掉。真正留下的是：

> **在 support 完全分离的情况下，加法关系 `a+b=c` 能否限制每个数内部被 radical collapse 遗忘的重复指数？**

这把 P025 从 P017 的 support-overlap 计数问题区分出来。

## 3. P025-N01 —— radical 不是加法的精确安全商

考虑两组输入：

\[
(4,1),\qquad (8,1).
\]

它们在 radical 粗状态中完全相同：

\[
(\operatorname{rad}(4),\operatorname{rad}(1))
=(2,1)
=(\operatorname{rad}(8),\operatorname{rad}(1)).
\]

但加法后的 radical 不同：

\[
\operatorname{rad}(4+1)=5,
\qquad
\operatorname{rad}(8+1)=\operatorname{rad}(9)=3.
\]

因此 radical collapse 对二元加法不满足 P023 的 fiber-constant / operation-congruence 判据。

\[
\boxed{\text{radical support alone cannot make addition descend exactly.}}
\]

所以若 ABC 能由“坍缩语言”解释，它必须使用比 exact safe quotient 更弱但仍可控制的结构。

## 4. P025-T02 —— rational exponent 的完全整数 defect 坐标

ABC 通常写成实指数形式。为了避免把对数或浮点数当成底层状态，固定正整数

\[
u>v\ge1
\]

并定义

\[
\boxed{
Q_{u,v}(a,b,c)
=\left\lceil
\frac{c^v}{\operatorname{rad}(abc)^u}
\right\rceil.
}
\]

则对任意正整数 `B`，

\[
\boxed{
Q_{u,v}(a,b,c)\le B
\iff
c^v\le B\operatorname{rad}(abc)^u.
}
\]

证明只是正整数 ceiling-division 的定义。

因此，对固定 rational exponent `u/v>1`，`Q_{u,v}` 的一致有界性与对应的 ABC 型界完全等价，只使用整数乘方、比较和整除。

这不是对 ABC 的加强，只是把一个实数 quality 观察量换成了等价的有限整数 defect 坐标。

## 5. P025-T03 —— 高质量状态必然产生 multiplicity pressure

令

\[
R=\operatorname{rad}(abc),
\qquad
M=m(a)m(b)m(c)=\frac{abc}{R}.
\]

固定 `u>v>=1`。若

\[
\boxed{c^v>R^u,}
\]

则

\[
R^u<c^v.
\]

由 `M=abc/R`，

\[
M^u
=\frac{(abc)^u}{R^u}
>\frac{(abc)^u}{c^v}
=(ab)^u c^{u-v}.
\]

又因为正整数 `a+b=c`，有紧的初等下界

\[
ab\ge c-1,
\]

等号在 `{a,b}={1,c-1}` 时达到，所以

\[
\boxed{
M^u>c^{u-v}(c-1)^u.
}
\]

也就是说：若一个三元组的 support weight 相对于 `c` 太小，缺掉的规模必定以重复素因子重数的形式储存在 `m(a)m(b)m(c)` 中。

## 6. P025-T04 —— residual pressure 必局域到至少一个输入

记

\[
m_{\max}=\max\{m(a),m(b),m(c)\}.
\]

因为

\[
M=m(a)m(b)m(c)\le m_{\max}^3,
\]

P025-T03 立即推出

\[
\boxed{
m_{\max}^{3u}>c^{u-v}(c-1)^u.}
\]

令项目已有整数根为

\[
R_r(N)=\max\{k\in\mathbb N:k^r\le N\}.
\]

则等价地得到精确有限阈值：

\[
\boxed{
 m_{\max}>
 R_{3u}\!\left(c^{u-v}(c-1)^u\right).
}
\]

这是 P025 第一个直接回接现有 integer-root 基础工具的桥：ABC 型高质量事件强制至少一个 multiplicity residual 越过一个显式整数 root horizon。

### 小型工作样本

\[
1+4374=4375
\]

中

\[
\operatorname{rad}(abc)=210,
\]

而三项 residual 为

\[
1,\ 729,\ 125.
\]

这个样本只用于观察结构，不作为渐近或猜想证据。

## 7. Mason–Stothers 路线：真正的桥不是“导数”一个词

函数域中的 Mason–Stothers 定理是 ABC 的经典多项式对应物。Baek–Lee 的 Lean 4 工作把一个短的 Wronskian 证明完整形式化，并明确了以下链条 [SRC-BAEK-LEE-2024-MASON-LEAN]：

1. 对多项式 `f`，
   \[
   f/\operatorname{rad}(f)\mid f';
   \]
2. 对 `a+b+c=0`，三个 Wronskian
   \[
   W(a,b),\ W(b,c),\ W(c,a)
   \]
   相等；
3. 因而三个 multiplicity residual
   \[
   a/\operatorname{rad}(a),\quad
   b/\operatorname{rad}(b),\quad
   c/\operatorname{rad}(c)
   \]
   都进入同一个公共 witness `W`；
4. 两两互素使 residual product 整体整除 `W`；
5. `deg W < deg a + deg b` 给出 witness capacity；
6. 消元后得到
   \[
   \deg c+1\le\deg\operatorname{rad}(abc).
   \]

所以在当前架构下，更精确的抽象不是“导数连接加法和乘法”，而是：

\[
\boxed{
\text{hidden multiplicity residual}
\to
\text{relation-conditioned common witness}
\to
\text{witness capacity}
\to
\text{support bound}.
}
\]

`src/enterprise_math/abc_support.py::witness_capacity_elimination` 只实现最后的整数消元骨架；Wronskian witness 的存在属于经典 Mason–Stothers 数学，不归 P025 所有。

## 8. 关键 prior-art 碰撞：Pasten 已经把这条桥搬到整数上

Hector Pasten 的 arithmetic-derivative 工作已经构造了某类整数上的 derivations：它们满足 Leibniz 规则，并且**针对给定的关系 `a+b=c` 强制满足相应加法约束**；其 Geometry-of-Numbers 论证给出受控大小的 derivations，并证明“足够小的 arithmetic derivatives”与 ABC 猜想在精确指数关系上等价 [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。

Pasten 还在整数版 Wronskian 中得到与函数域证明同型的关键吸收结构：multiplicity residual 被公共 witness 吸收，然后 `abc` 由 witness 大小与 `rad(abc)` 控制。

因此：

\[
\boxed{
\text{“寻找整数版 Mason 导数”不是 P025 的新方向。}
}
\]

这次 prior-art 碰撞不是失败，而是把项目可研究的新层压缩得更准确。

## 9. P025-H01 —— relation-conditioned witness space

P023 当前主要问：一个 quotient 是否让指定未来观测/运算精确下沉。

Pasten 的结构提示另一种中间层：不是要求存在一个全局确定 witness，也不是立即把 quotient 修复到 exact-safe，而是对每个任务/关系状态 `x` 考虑一个允许的 witness 集合

\[
\mathcal W_R(x).
\]

这里：

- `R` 是当前关系语言，例如 `a+b=c`；
- 每个 `w in W_R(x)` 满足一组结构约束；
- `w` 能吸收 quotient 忘掉的一部分 residual；
- witness 有整数或离散成本 `cost(w)`；
- 真正的问题变成是否存在足够低成本的 witness：

\[
\boxed{
\min_{w\in\mathcal W_R(x)}\operatorname{cost}(w)
\le \text{required horizon}(x).
}
\]

在 ABC 上，这不是新猜想的重新命名：Pasten 已经证明特定 arithmetic-derivative 版本的“小 witness”问题与 ABC 紧密等价。P025 的研究内容是考察**这种 relation-conditioned witness-space 语义能否成为比具体导数更一般的进取数论接口**。

当前状态：`CONJECTURAL ARCHITECTURE / NOVELTY_UNVERIFIED`。

## 10. 与 A2 / A4 的潜在桥，而不是合并

这个对象同时触碰两个现有层，但不能把它们混成一个 ontology：

- A2 / P023：任务相对的 future-safe quotient、minimal repair、operation descent；
- A4：一个输入允许多个 admissible support / correspondence witness。

P025 提示的可能桥是：

\[
\text{coarse state}
\to
\text{relation-conditioned admissible witness family}
\to
\text{minimum witness precision/cost}
\to
\text{future bound/certificate}.
\]

这与 Foundation Issue `FQ-20260809-004` 的边界要求一致：functional kernel、relation-state 和 multivalued support 仍需保持显式区分。P025 只提供压力测试，不直接修改 Foundation。

## 11. P025-H02 —— 从二值安全推广到“失败强度 × 失败稀疏度”

radical 对加法并不 exact-safe，因此仅用 `safe/unsafe` 二值标签会过早丢失结构。

现代 ABC exceptional-set 工作提供了另一类成熟参照。Bernert–Browning–Lichtman–Teräväinen 研究满足

\[
\operatorname{rad}(abc)<c^{1-\varepsilon}
\]

的异常三元组并给出 power-saving 型计数界 [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2024-ABC-EXCEPTIONAL]。Runbo Li 随后给出更强的指数界

\[
O\!\left(X^{56/85+\varepsilon}\right)
\]

[SRC-LI-2025-ABC-EXCEPTIONAL]。

对 rational `epsilon=r/s`，异常判据本身可完全整数化为

\[
\boxed{
\operatorname{rad}(abc)^s<c^{s-r}.
}
\]

因此 P025 暂时把粗化行为分成至少三档：

1. **exact descent**：未来观测在 quotient fiber 上完全一致；
2. **witness-mediated bounded defect**：不精确下沉，但存在受控 witness 吸收遗忘信息；
3. **sparse-exception descent**：坏状态存在，但其 incidence 随尺度有定量稀疏界。

第三档是对外部 exceptional-set 思想的架构重解释，不声称异常集方法本身由项目发明。

## 12. Derivation generalization 的创新边界

Mason–Stothers 的导数/Wronskian 机制已经有广泛推广；例如 Kikteva 研究 locally nilpotent derivations 上的 ABC-type generalization [SRC-KIKTEVA-2023-ABC-DERIVATION]。因此 P025 不把“用 derivation 抽象 ABC”声称为新发现。

若以后形成一般 mother theorem，必须证明它的项目新增部分来自：

- quotient residual 的显式 finite-state 语义；
- relation-conditioned multivalued witness family；
- witness precision/cost 与 future-safe precision 的关系；
- exact / bounded-defect / sparse-exception 三层之间的严格迁移判据；

而不是简单重述已有 derivation、Wronskian 或 Geometry-of-Numbers 结果。

## 13. 第一阶段可执行资产

当前 owner 已建立：

- `src/enterprise_math/abc_support.py`
  - exact prime support / radical / multiplicity residual；
  - primitive abc support partition；
  - rational-exponent integer defect；
  - exact rational exceptional predicate；
  - residual-pressure theorem 的 executable check；
  - radical-addition negative boundary；
  - Mason witness-capacity 的纯整数消元骨架。
- `src/enterprise_math/abc_precision_bridge.py`
  - 把 residual pressure 搬运到已有 `integer_nth_root` horizon。
- `tests/test_abc_support.py`
- `tests/test_abc_precision_bridge.py`

独立原型回归已覆盖：

- 经典高质量三元组 `2 + 3^10*109 = 23^5`；
- `Q_{3,2}=13` 的精确整数 defect；
- radical-addition 反例；
- `c<120`、`(u,v) in {(2,1),(3,2),(4,3)}` 的 primitive triples 穷举 residual-pressure 回归；
- integer-root horizon bridge。

穷举只验证实现与已证明初等不等式，不提供 ABC 的无限范围证据。

## 14. 下一前沿

当前最佳前沿已经从“找一个整数版导数”改成：

1. **重建 Pasten witness space 的有限 support 坐标**：把每个 prime-support 坐标、关系约束、自由度、non-degeneracy 与 norm 分开；
2. **witness precision**：研究同一 abc 状态允许的 witness family 在逐步精度限制下如何收缩，是否存在单调/稳定/最小充分层；
3. **P023 bridge**：精确区分 `repair state until operation descends` 与 `retain coarse state but attach bounded witness` 两种成本；
4. **A4 bridge**：检查 admissible-support relation 是否足以表达一个状态的多 witness family，以及哪些 witness 组合律是真实的；
5. **exceptional-set bridge**：把 `bad-state count` 从单一 ABC 应用抽出为有限/尺度化的 quotient failure statistic；
6. **function-field calibration**：先在 Mason–Stothers 已证明世界验证整套 witness-precision 语言，再返回整数世界。

若这些步骤只重新得到 Pasten/Mason 的既有结构，就如实记为 `ADOPT/REINTERPRET`；只有出现严格更一般、可复用且经过 prior-art 审计的接口，才考虑回流 A2/P018 或 Foundation。

## 15. 当前结论

第一阶段已经得到三个可靠方向判断：

\[
\boxed{
\text{radical 是 support collapse，但绝不是加法 congruence；}
}
\]

\[
\boxed{
\text{ABC 型高质量状态必把大量信息压进 multiplicity residual；}
}
\]

\[
\boxed{
\text{前人已证明成功桥的核心形态是“关系条件化 witness + witness 大小”。}
}
\]

因此 P025 后续不再追求一个脱离关系的万能运算，而研究**任务/关系决定 witness 空间，witness 精度决定遗忘信息是否仍可控**。这与进取数论现有精度架构形成了真正可检验的新接口候选。

# E002 — 有限预测商编译器，补充 06

状态：`ACTIVE ENGINEERING RESEARCH NOTE`  
范围：通用有限预测 partition 编译，以及对 E002 闭式的自动重建  
父文档：`docs/E002_TASK_RELATIVE_OBSERVABLE_SUPPLEMENT_05.zh-CN.md`  
依赖：P023 future-compatible quotient 理论  
前人工作：`docs/PRIOR_ART_E002_PREDICTIVE_QUOTIENT.zh-CN.md`

## 1. 动机

第一至第五阶段已经推导出越来越多针对特定物理动作与未来查询的整数精度闭式。真正的风险是：这些公式只是人工挑选出的若干巧合，而不是同一个操作性状态原则的特例。

因此第六阶段不再先猜下一条特殊公式，而是先构造一个通用有限编译器：

\[
\boxed{
(\text{fine states},\text{actions},\text{observation},\text{horizon})
\longmapsto
\text{最粗 predictive partition}.
}
\]

编译器完全不知道 E002 的 gcd、余数、向量乘积、二项式或 Boolean 闭式。只有当通用编译器仅从底层有限系统重新得到同样 partition/基数时，才认为这些闭式得到了独立重建。

有限状态行为等价与自动机最小化都是成熟前人工作。 [SRC-MOORE-1956-SEQUENTIAL-MACHINES] [SRC-HOPCROFT-1971-AUTOMATON-MINIMIZATION] E002 不声称新的最小化算法。

## 2. 有限系统

令

\[
X
\]

为有限非空状态集。令

\[
\mathcal A=\{T_a:X\to X\}
\]

为有限非空的全定义确定性动作族，并令

\[
O:X\to Y
\]

为有限值观测映射。

对动作 word

\[
v=a_1\cdots a_k,
\]

记

\[
T_v=T_{a_k}\circ\cdots\circ T_{a_1},
\]

空 word 为恒等映射。

整个构造不需要概率、实值 metric、embedding 或无限精度 completion。

## 3. horizon-indexed 预测等价

递归定义等价关系。

horizon 0 时，

\[
\boxed{x\sim_0y\iff O(x)=O(y).}
\]

对 `h>=0`，定义

\[
\boxed{
x\sim_{h+1}y
\iff
O(x)=O(y)
\ \text{且}\ 
T_a(x)\sim_hT_a(y)
\text{ 对每个 }a\in\mathcal A.}
\]

这正是实现中的 partition-refinement 递推：

- `observation_partition`；
- `refine_predictive_partition`；
- `finite_horizon_partition`。

## 4. E002-T33 — 精确有限 horizon 语义

对任意 `h>=0`，

\[
\boxed{
x\sim_hy
\iff
O(T_v(x))=O(T_v(y))
\text{ 对所有 }|v|\le h\text{ 的动作 word }v.}
\]

因此 `~_h` 正是保留 horizon `h` 内完整已声明观测未来的最粗 partition。

### 证明

对 `h` 归纳。

当 `h=0` 时，唯一 word 是空 word，结论就是 `~_0` 的定义。

假设结论对 `h` 成立。按定义，

\[
x\sim_{h+1}y
\]

要求当前观测相同，并且对每个第一步动作 `a` 有

\[
T_a(x)\sim_hT_a(y).
\]

由归纳假设，后者等价于：从这些 successor 出发，所有长度不超过 `h` 的 suffix word 后观测都相同。这恰好覆盖从 `x,y` 出发所有长度不超过 `h+1` 的非空动作 word；再加上空 word/当前观测，就得到所述完整语言。∎

### 推论

被 `~_h` 合并的状态，对于已声明有限未来语言完全可互换。任何更粗 partition 都会合并至少一对被某个允许 word/观测区分的状态，从而失去 predictive sufficiency。

这使 horizon 成为明确的精度义务，而不是模糊的规划参数。

## 5. E002-T34 — 单调有限稳定与稳定 congruence

预测关系单调细化：

\[
\boxed{
\sim_{h+1}\ \subseteq\ \sim_h.
}
\]

等价地，block 数随 horizon 不减。

由于 `X` 有限，序列经过有限次严格细化后必然稳定。若 `b_0` 为当前观测 partition 的 block 数，则严格细化轮数至多

\[
\boxed{|X|-b_0}.
\]

记稳定关系为

\[
\sim_*.
\]

则：

1. `~_*` 细化当前观测等价；
2. `~_*` 是动作 congruence：
   \[
   x\sim_*y\implies T_a(x)\sim_*T_a(y)
   \quad\forall a\in\mathcal A;
   \]
3. `~_*` 保留**所有有限动作 word**后的观测；
4. `~_*` 是满足 1–2 的最粗等价关系。

### 证明

T33 立即给出单调性，因为 horizon `h+1` 的未来语言包含 horizon `h` 的语言。

每次严格细化至少新增一个非空 block，而 `|X|` 个状态最多有 `|X|` 个 block，于是得到有限上界。

在固定点，`~_(h+1)` 与 `~_h` 的递归定义相同，因此等价状态在每个动作后的 successor 仍等价，即得到 congruence。congruence 沿任意有限动作 word 传播，而当前观测相同保证每个传播后的输出相同。

最后设 `R` 为任意细化观测等价的动作 congruence。对 `h` 归纳可得 `x R y` 蕴含 `x~_h y`：`h=0` 显然；若对 `h` 成立，则 congruence 给出 `T_a(x) R T_a(y)`，再由归纳假设得到 successor 的 `~_h` 等价，从而得到 `~_(h+1)`。因此 `R` 包含于每个 `~_h`，也包含于 `~_*`。所以 `~_*` 比任意其他安全 congruence 合并不少状态，即为最粗者。∎

## 6. 编译器输出

可执行编译器提供三类结果。

### 有限 horizon partition

`finite_horizon_partition` 返回 `~_h` 的 block label。

### 稳定 quotient

`stable_predictive_partition` 返回：

- 稳定 partition；
- 首次稳定深度；
- 稳定 block 数。

### 可执行 quotient machine

对一个安全稳定 partition：

- `quotient_transition_table` 构造诱导出的确定性动作表；
- `quotient_observation_table` 为每个 quotient state 构造唯一观测。

如果 proposed partition 合并了未来 transition/output 行为并不良定义的状态，两者都会拒绝。

所以编译结果不只是一个类别数，而是一个可执行有限世界状态机。

## 7. 受限初始 fiber

E002 闭式通常统计某一个已声明粗精度胞元内部的 fine phase，而不是一个全局闭合测试系统的全部状态。

因此编译器区分：

- 动作真正闭合运行的有限 state set；
- 要统计 predictive block 的已声明初始 subset/fiber。

`restricted_block_count` 统计编译后有多少 predictive block 与该初始 fiber 相交。

这样可以用有限闭合 harness 模拟局部精度胞元，而不假装物理动作在胞元边界停止。

## 8. E002-T35 — 通用编译器自动重建此前闭式

对对角单位动作实验构造有限 countdown system：

\[
X=\{0,1,\ldots,w\}^n,
\]

动作

\[
T(x_1,\ldots,x_n)
=(\max(0,x_1-1),\ldots,\max(0,x_n-1)).
\]

将每个坐标的 `1..w` 解释为原 fine phase，将状态 `0` 解释为“已经跨越”。

编译器只获得这个 transition 和所选观测映射，**不获得任何手工类别闭式**。

有界重建得到：

### 完整向量观测

对

\[
O_{\rm full}(x)=(\mathbf1_{x_1=0},\ldots,\mathbf1_{x_n=0}),
\]

自动恢复

\[
\boxed{(h+1)^n}
\]

个初始 fiber 类别（`h<w`）。

### 对称和

对

\[
O_{\rm sum}(x)=\sum_i\mathbf1_{x_i=0},
\]

自动恢复

\[
\boxed{\binom{h+n}{n}}.
\]

### Boolean ANY / ALL

对

\[
O_{\rm ANY}=\mathbf1_{\exists i:x_i=0},
\qquad
O_{\rm ALL}=\mathbf1_{\forall i:x_i=0},
\]

自动恢复与维数无关的

\[
\boxed{h+1}.
\]

### 二维线性观测

对

\[
O_{\alpha,\beta}
=\alpha\mathbf1_{x_1=0}+\beta\mathbf1_{x_2=0},
\]

自动恢复 T29 的完整系数分类：

\[
1,\ B,\ B(B+1)/2,\ B(B-1)+1,\ B^2
\]

分别对应其系数情形。

### Boolean equality

对

\[
O_=(x)=
\mathbf1_{(x_1=0)=(x_2=0)},
\]

自动恢复

\[
\boxed{1+h(h+1)/2}.
\]

这些重建表明，此前 E002 闭式在这些有限系统上确实是同一个通用 predictive equivalence compiler 的特殊闭式。

这并不意味着今后每个 Enterprise Math 问题都一定存在简短闭式。

## 9. 概念上发生了什么变化

工程线现在可以脱离具体控制器术语表述为：

\[
\boxed{
\text{fine finite world state}
+\text{allowed actions}
+\text{declared observation}
+\text{future horizon}
\longrightarrow
\text{minimal predictive quotient}.
}
\]

得到的 quotient 可能恰好是：

- 一个粗精度胞元；
- gcd 细化；
- 有限 horizon residue rank；
- 多坐标 rank 的乘积；
- multiset summary；
- Boolean crossing bucket；
- 或者根本没有短算术闭式的不规则有限 partition。

第一至第五阶段的算术闭式真正有价值，是因为它们让通用 quotient 在无需枚举全部 fine state 的情况下被直接表示出来。

## 10. 与 P023 的关系

P023 拥有通用原则：未来操作必须在保留状态上因子化，最粗安全修复也依赖具体语言。

第六阶段只是一个可执行有限确定性特化：

- T33 给出精确 finite-word 语义；
- T34 用经典有限 partition refinement 计算稳定 common-compatible congruence；
- T35 用这个通用 oracle 证伪或重建 E002 闭式。

因此 E002 不把编译器算法提升为新的 Foundations 母定理族。它的角色是工程验证与自动状态综合。

## 11. 前人工作边界

Moore 的序贯机器工作是有限状态/输出行为区分的前人工作。 [SRC-MOORE-1956-SEQUENTIAL-MACHINES]

Hopcroft 的自动机最小化工作是状态最小化与 partition refinement 的前人工作。 [SRC-HOPCROFT-1971-AUTOMATON-MINIMIZATION]

E002 不声称递归细分、稳定最小化或有限状态 quotient compiler 具有历史新颖性。

项目特定实验是：把这类编译器解释并用作受显式物理/控制 action 与 observation language 约束的有限精度世界状态综合器。

历史新颖性继续保持 `NOVELTY_UNVERIFIED`。

## 12. 可执行审计

实现：

- `src/enterprise_math/predictive_quotient.py`

测试：

- `tests/test_predictive_quotient.py`

测试覆盖通用有限稳定、distinguishing horizon、quotient transition/output table、不安全 partition 拒绝，以及在有界有限域自动重建 E002 第四/第五阶段闭式。

独立重建还单独实现了同一 recurrence，并在不把闭式写入 refinement 算法的情况下重现了完整向量、对称和与 ANY 公式。

## 13. 证伪条件

若出现以下任一情况，第六阶段必须否定或缩窄：

1. 递归 partition 与相同 horizon 的直接观测未来枚举不一致；
2. 稳定 partition 不能定义确定性的 quotient actions/observations；
3. 存在比 claimed stable partition 更粗、却仍保持观测的动作 congruence；
4. 通用编译器不能在某个声称闭式精确的域上重建该 E002 公式；
5. 项目把有限状态最小化/partition refinement 描述成 Enterprise Math 的发明。

## 14. 下一批压力测试

编译器让下一步变成可直接执行的问题：

1. 允许状态相关/partial action availability，编译 controller-policy language 而不是所有 total action；
2. 比较枚举 quotient 的大小/运行时间与闭式算术特化，量化数学什么时候真正带来工程速度；
3. 把 E001 向量碰撞状态与 Boolean collision observation 输入编译器，自动寻找更小的 future-safe collision state；
4. 把 controller memory 与 delayed queue 作为显式有限状态加入 product system；
5. 先让通用 oracle 暴露 partition 规律，再搜索其算术/几何闭式并证明，而不是先猜结构。

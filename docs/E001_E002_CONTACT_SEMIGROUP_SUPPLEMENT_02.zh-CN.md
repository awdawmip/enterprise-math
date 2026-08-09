# E001/E002 — 接触动作 Semigroup 边界，补充 02

状态：`ACTIVE CROSS-ROUTE ENGINEERING NOTE`  
范围：单向 numerical-semigroup 接触精度与双向 gcd 接触精度的分界  
父文档：`docs/E001_E002_CONTACT_ACTION_FAMILY_SUPPLEMENT_01.zh-CN.md`

## 1. 对“动作对称性必要”的纠正

上一份动作族补充证明了：若每个幅度都成对提供 `+a_j/-a_j`，则 gcd contact 坐标成立。这个条件是充分的，但比真正需要的更强。

真正的代数分界是：**有符号动作 monoid 是单向还是双向**。

- 只有 separating（或只有 closing）时，未来累计运动形成单向加法 semigroup，在 gcd 之上可能存在有限不可达孔洞；
- 只要至少存在一个正 gap 动作和一个负 gap 动作，非负 word 生成的加法 monoid 就等于这些动作生成的完整 subgroup，即 `g Z`。

这会直接改变 Boolean contact 的最粗精度。

## 2. 单向 separating language

令

\[
A=\{a_1,\ldots,a_m\}\subset\mathbb N_{>0}
\]

且只允许

\[
x\mapsto x+a_j.
\]

对 horizon `h`，令 `M_h` 为长度不超过 `h` 的动作 word 的不同累计和集合，并包含 0；令

\[
M=\bigcup_hM_h
\]

为生成的 numerical semigroup。

对当前 contact gap `0<=x<d`，定义到边界的剩余距离

\[
r=d-x\in\{1,\ldots,d\}.
\]

一个累计位移为 `s` 的 word 之后仍 contact，当且仅当

\[
s<r.
\]

## 3. E001/E002-T40 — 精确单向 semigroup partition

两个当前 contact gap 在 horizon `h` 内 future-equivalent，当且仅当

\[
M_h\cap\{1,\ldots,d-1\}
\]

中没有任何值落在二者的剩余距离之间。

等价地，

\[
\boxed{
\rho_h(x)=\#\{s\in M_h:0<s<d-x\}
}
\]

就是 contact fiber 内最粗的 horizon-`h` predictive state。

精确类别数为

\[
\boxed{
C_h=1+|M_h\cap\{1,\ldots,d-1\}|.
}
\]

对任意有限未来 word，

\[
\boxed{
C_\infty=1+|M\cap\{1,\ldots,d-1\}|.
}
\]

### 证明

每一个可达累计位移 `s` 只读取嵌套阈值 `s<r`。每个不同的正可达 `s<d` 都恰好新增一条 `r=s` 与 `r=s+1` 之间的边界；不可达位移永远不会产生未来观测，因此不能拆分 fiber。所有这些有序阈值完全由“有多少可达阈值小于 r”决定，得到上述 rank 与类别数。∎

## 4. 仅 closing 的 separated shell

对 separated shell

\[
x=d+j,\qquad0\le j<R,
\]

若只允许 closing 幅度 `a_j`，累计 closing 位移 `s` 进入 contact 当且仅当

\[
s>j.
\]

同样的阈值论证给出

\[
\boxed{
C^{\rm close}_h=1+|M_h\cap\{1,\ldots,R-1\}|,
}
\]

任意未来时把 `M_h` 换成 `M`。

因此 Boolean 边界两侧的单向运动都由**实际可达 semigroup 阈值**控制，而不是只由 group completion 控制。

## 5. E001/E002-T41 — gcd 何时已经最小的精确判据

令

\[
g=\gcd(a_1,\ldots,a_m).
\]

充分的 gcd 坐标会在 contact fiber 中保留

\[
\left\lceil\frac dg\right\rceil
\]

类。

它对单向 separating language 同时也是**最小**的，当且仅当每个小于 `d` 的正 gcd 倍数都实际可达：

\[
\boxed{
kg\in M
\quad\text{对所有 }1\le kg<d.
}
\]

也就是 contact 边界以下相关 gcd 倍数中不存在 numerical-semigroup hole。

### 反例

取

\[
d=7,
\qquad A=\{4,6\}.
\]

此时 `g=2`，gcd refinement 会保留

\[
\left\lceil\frac72\right\rceil=4
\]

类。

但小于 `d` 的正可达累计位移只有

\[
4,6;
\]

`2` 是 semigroup hole。因此

\[
\boxed{C_\infty=1+2=3.}
\]

所以 gcd 坐标安全，但严格过细。

## 6. 双向有符号动作 language

现在令

\[
D=\{\delta_1,\ldots,\delta_m\}\subset\mathbb Z\setminus\{0\}
\]

至少包含一个正动作和一个负动作。物理运动为

\[
x\mapsto\max(0,x+\delta_j).
\]

定义

\[
\boxed{g=\gcd(|\delta_1|,\ldots,|\delta_m|).}
\]

## 7. E001/E002-T42 — 双向性恢复 gcd-minimal quotient

`D` 的非负 word 加法 monoid 恰好等于

\[
\boxed{g\mathbb Z.}
\]

因此任意未来 Boolean contact 的精确最粗坐标重新变为

\[
\boxed{
K_{d,D}(x)=\left\lceil\frac{d-x}{g}\right\rceil.
}
\]

正动作 `delta>0` 给出

\[
K\mapsto K-\delta/g,
\]

负动作 `delta<0` 给出

\[
K\mapsto
\min\left(K+|\delta|/g,\left\lceil d/g\right\rceil\right),
\]

并且

\[
x<d\iff K\ge1.
\]

### 为什么 action monoid 等于 `g Z`

整数 group 由 Bezout 定理生成 `g Z`。还需证明：一旦动作集合同时具有正负号，负系数可以消掉。

固定一个正生成元 `p` 与一个负生成元 `-q`。若某个正生成元在 Bezout 表示中的系数为负，就加入足够多次正系数零关系

\[
\frac{\operatorname{lcm}(a,q)}a\,a
+
\frac{\operatorname{lcm}(a,q)}q\,(-q)=0
\]

使该系数非负。对负生成元的负系数，用固定正生成元构造同类零关系。反复处理即可把任意 `g` 倍数的整数表示变成全部非负 word count，因此 monoid 就是完整 `g Z`。

### 最粗性

精确 quotient transport 说明相同 K 的状态任意未来行为相同。由于每个整数 K 位移都能由有限 signed-action word 实现，不同 K 可以被平移到一边 `K=1`、另一边 `K<=0`。把所有 separating move 排在 closing move 之前，中间 K 先下降再上升到最终边界，不会非预期撞到 ground clipping cap，因此不同 K 必有限可区分。∎

## 8. 修正后的分界

上一阶段的成对动作定理仍然成立，但其最强解释应修正为：

\[
\boxed{
\text{逐幅度成对对称是充分条件，不是必要条件；}
\quad
\text{真正恢复 gcd-minimal 的是双向 signed reachability。}
}
\]

单向 action language 会保留 numerical-semigroup hole，因此可能允许比 gcd refinement 更粗的状态。

该结论应覆盖任何此前把“成对 `+a_j/-a_j` 对称本身”表述成必要条件的 Relay 文字。

## 9. 编译器交叉验证

通用预测商编译器独立验证分类两侧：

- separating-only 有限世界自动重建 `1+|M_h cap [1,d-1]|` 个 contact-fiber 类；
- `{+6,-10}`、`{+9,-15}` 这类不成对但双向的动作，stable compiler partition 仍逐状态等于 gcd 坐标 K。

编译器并不知道 numerical-semigroup 或 gcd 闭式。

## 10. 解释

该结果为 semigroup 与 group completion 的区别提供了直接工程含义：

- **单向未来操作**留下不可达阈值孔洞，因此这些差异不属于最小 predictive state；
- **双向未来操作**行为上填满整个 gcd subgroup，凡是能影响 Boolean 边界的 gcd phase 都被迫保持可区分。

因此所需精度不仅依赖数值步长，还依赖未来世界允许的操作方向语言。

## 11. 可执行资产

- `src/enterprise_math/predictive_contact_semigroup.py`
- `tests/test_predictive_contact_semigroup.py`

## 12. 下一批压力测试

1. 不枚举全部 word，直接刻画任意 one-sided action semigroup 的 finite-horizon 类别增长；
2. 如需引入 conductor/Frobenius 结构，必须显式登记 numerical-semigroup 前人工作，不能换名包装；
3. 让 action availability 依赖当前状态；
4. 加入 rebound/material observation，重新编译 Boolean contact 之外的状态；
5. 把 semigroup/group-completion 分界提升到向量 collision action。

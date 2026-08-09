# P023 —— 任务精度细化与最小 repair 计量，补充 09

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023 future-compatible quotient  
依赖：P023 composition-safe repair formal core、P023-S8 actual-image separation、E002 predictive quotient  
纪律：等价关系格、kernel 交、闭包系统与有限分区计数属于成熟数学；本补充不主张这些一般结构的历史原创性。项目价值在于把它们固定为有限精度研究的统一计量接口。

## 1. 问题

P023 已经证明：若旧粗状态是

\[
q:X\to Q,
\]

而新增 observable 是

\[
h:X\to R,
\]

则 pair state

\[
(q,h):X\to Q\times R
\]

是同时保留二者的最粗精确 repair。

但这个 existence / coarsest theorem 尚未回答三个有限精度问题：

1. 多个任务组合后到底实现多少 quotient classes？
2. 从旧 task quotient 升级到新 task quotient，最少需要多少 repair symbols？
3. 多次升级时 repair 成本怎样组合？

本补充给出精确有限答案。

---

## 2. 任务 query 与精度关系

令 `X` 为有限非空状态集。每个声明 query 是一个确定性映射

\[
f_\alpha:X\to Y_\alpha.
\]

对 query language

\[
\mathcal L
\]

定义未来可区分关系

\[
\boxed{
x\sim_{\mathcal L}y
\iff
f_\alpha(x)=f_\alpha(y)
\quad\text{对所有 }\alpha\in\mathcal L.
}
\]

记对应等价关系为

\[
E_{\mathcal L}.
\]

当 query 来自 future dynamics 时，可以取

\[
f_\alpha=O_j\circ T_w,
\]

所以有限 horizon、动作语言、observable language 都只是这个统一定义的特例。

---

## 3. P023-S9-T01 —— task language 反单调，任务并集对应共同细化

状态：`PROVED`。

若

\[
\mathcal L_1\subseteq\mathcal L_2,
\]

则

\[
\boxed{
E_{\mathcal L_2}\subseteq E_{\mathcal L_1}.
}
\]

也就是说，声明更多未来问题时，安全 quotient 只能保持或变细，不能凭空变粗。

对任意 task family \(\{\mathcal L_i\}\)，

\[
\boxed{
E_{\bigcup_i\mathcal L_i}
=
\bigcap_i E_{\mathcal L_i}.
}
\]

### 证明

`x,y` 在左侧等价，当且仅当它们对并集中的每一个 query 给出相同答案；这等价于对每个 `i` 中的所有 query 都相同，也就是同时属于每个 \(E_{\mathcal L_i}\)。∎

### 含义

这给出 task-relative precision 的第一个结构律：

\[
\boxed{
\text{任务组合}
\longleftrightarrow
\text{quotient 共同细化}.
}
\]

因此 horizon 增大、动作生成元增加、observable 增加，都统一表现为等价关系向细方向移动。

---

## 4. P023-S9-T02 —— 组合 quotient 数的是 realized tuples，不是形式笛卡尔积

设两个任务 quotient 为

\[
\pi_1:X\to X/E_1,
\qquad
\pi_2:X\to X/E_2.
\]

组合任务由

\[
\Pi(x)=(\pi_1(x),\pi_2(x))
\]

表示。

则

\[
\ker\Pi=E_1\cap E_2.
\]

因此组合 quotient 的 class 数恰好是

\[
\boxed{
C_{12}
=
\left|
\operatorname{im}\Pi
\right|.
}
\]

若

\[
C_i=|X/E_i|,
\]

则

\[
\boxed{
\max(C_1,C_2)
\le
C_{12}
\le
C_1C_2.
}
\]

### 关键点

右侧乘积只是完整候选笛卡尔积

\[
(X/E_1)\times(X/E_2).
\]

真正组合状态只占其中实际被 `X` 命中的 tuples。

因此

\[
\boxed{
\text{formal product candidates}
\neq
\text{realized combined states}.
}
\]

这与 P023-S8/P017 L055 的 actual-image discipline 是同一个数学现象：先把实际像扩大成形式 superset，会制造不存在的“状态组合”或“碰撞”。

### 多任务版本

对任意有限任务族 \(\pi_1,\ldots,\pi_m\)，

\[
\boxed{
\left|X/\bigcap_iE_i\right|
=
\left|
\operatorname{im}
\left(
X\to\prod_i X/E_i
\right)
\right|.
}
\]

不能在没有 independence/surjectivity 证明时把 class 数直接乘起来。

---

## 5. refinement chain 与局部 split multiplicity

现在设目标精度关系 `F` 比旧关系 `E` 更细：

\[
F\subseteq E.
\]

对每个旧 `E`-block

\[
B\in X/E,
\]

定义它被 `F` 切成的子块数

\[
\boxed{
m_{E\to F}(B)
=
\#\{C\in X/F:C\subseteq B\}.
}
\]

定义最大局部 split multiplicity

\[
\boxed{
R(E\to F)
=
\max_{B\in X/E}m_{E\to F}(B).
}
\]

注意这是**局部**量，不是全局 class 数之比。

如果不同 coarse blocks 的 split 程度不同，则

\[
|X/F|/|X/E|
\]

既可能不是整数，也不是最小 repair alphabet 的正确答案。

---

## 6. P023-S9-T03 —— 最小 repair alphabet 定理

状态：`PROVED`。

设 repair coordinate 是

\[
\rho:X\to A.
\]

要求旧 coarse state 与 repair 一起恰好实现目标 relation：

\[
\boxed{
F
=
E\cap\ker\rho.
}
\]

那么所有可行 repair alphabet `A` 中的最小基数为

\[
\boxed{
\min |A|
=
R(E\to F)
=
\max_{B\in X/E}
m_{E\to F}(B).
}
\]

### 必要性

固定一个 `E`-block `B`。若它包含 `m` 个不同 `F`-blocks，而 repair alphabet 少于 `m` 个符号，那么鸽巢原理迫使两个不同 `F`-blocks 在 `B` 内得到同一个 repair symbol。

它们于是旧 coarse label 相同、repair symbol 也相同，却不属于同一个 `F`-block，违反

\[
F=E\cap\ker\rho.
\]

所以

\[
|A|\ge m
\]

对每个 `B` 成立，故

\[
|A|\ge R(E\to F).
\]

### 充分性

令

\[
R=R(E\to F).
\]

在每个 coarse block `B` 内，把其 `F`-subblocks 任意编号为

\[
0,1,\ldots,m_B-1.
\]

不同 coarse blocks 之间可以**重复使用同一组 repair symbols**。

取统一 alphabet

\[
A=\{0,\ldots,R-1\}.
\]

令 \(\rho(x)\) 为 `x` 所属 `F`-subblock 在其当前 `E`-block 内的局部编号。

那么同一 `E`-block 内：

\[
\rho(x)=\rho(y)
\iff
xFy.
\]

而不同 `E`-blocks 本来已由 coarse label 区分，所以

\[
E\cap\ker\rho=F.
\]

因此大小 `R` 的 alphabet 足够，定理成立。∎

---

## 7. 一比特 repair 的真正一般判据

P023-S9-T03 立刻给出：

\[
\boxed{
\text{binary repair 足够}
\iff
R(E\to F)\le2.
}
\]

若某个 coarse block 确实被目标任务切成两个子块，则二值 alphabet 同时也是最小的。

所以此前反复出现的 one-bit 结果统一为：

- P023 crossing bit；
- E002 one-step carry repair；
- P017 L057 的 lower-band root-shell repair；

它们并不是因为“bit”本身特殊，而是因为对应 coarse fiber 的最大 target split multiplicity 恰好为 2。

---

## 8. P023-S9-T04 —— repair chain 的次乘法

状态：`PROVED`。

若有 refinement chain

\[
G\subseteq F\subseteq E,
\]

则

\[
\boxed{
R(E\to G)
\le
R(E\to F)\,R(F\to G).
}
\]

### 证明

一个 `E`-block 最多包含

\[
R(E\to F)
\]

个 `F`-blocks。

每个这样的 `F`-block 又最多包含

\[
R(F\to G)
\]

个 `G`-blocks。

因此一个 `E`-block 内的 `G`-blocks 总数最多为二者乘积。对所有 `E`-blocks 取最大即得。∎

### 严格不等号可以发生

如果最坏的 `E->F` split 与最坏的 `F->G` split 不发生在同一条局部路径上，则直接 repair 可以严格小于逐级最坏成本之积。

因此研究中不能把每一级的 worst-case 机械相乘后当成真实状态数。

---

## 9. P023-S9-T05 —— query-generated precision closure lattice

状态：`PROVED / STANDARD STRUCTURE`。

固定可用 query family `Q`，考虑所有子语言

\[
\mathcal L\subseteq Q
\]

产生的关系集合

\[
\mathfrak P_Q
=
\{E_{\mathcal L}:\mathcal L\subseteq Q\}.
\]

由 T01：空语言给出最大粗关系 `X×X`；任意族 \(E_{\mathcal L_i}\) 的交仍然等于

\[
E_{\cup_i\mathcal L_i}.
\]

因此 \(\mathfrak P_Q\) 是等价关系格中的一个 closure system，因而自身形成完备格。

在“越细 relation 越小”的 refinement order 中：

\[
\boxed{
\bigwedge_i E_{\mathcal L_i}
=
E_{\cup_i\mathcal L_i}.
}
\]

join 则是所有仍属于 \(\mathfrak P_Q\)、且同时粗于给定 relations 的 query-generated relations 的交。

### 项目含义

这给出一个比“precision scalar”更基础的对象：

\[
\boxed{
\text{precision state}
=
\text{query-generated equivalence relation}.
}
\]

不同任务不是在同一条数轴上简单加减“精度位数”，而是在一个 refinement lattice 中移动。

均匀尺度、root level、boundary rank、repair bit 等都只是这个格中的结构化坐标系。

这仍然首先是**证明/预测充分性结构**，不自动声称物理本体随任务改变。

---

## 10. 与 P023 formal core 的精确关系

本补充不重新发明 pair repair。

`EnterpriseMath/Precision/CompositionSafeCollapse.lean` 已证明：

\[
(q,h)
\]

是同时保留 `q` 与 `h` 的 coarsest repair。

本补充新增的是其有限计量层：

\[
\boxed{
\text{coarsest repair relation}
\quad+\quad
\text{exact minimum repair alphabet cardinality}.
}
\]

二者分别回答：“必须细化到哪个 relation？”以及“最少要增加多少离散 repair states？”

---

## 11. 与 P017 的新反哺

P017 lower-band exact cofactor shell 经 integer root 后，可以把 coarse state 取为 root index。

目标 task 是同时保留 root 与 least-prime shell identity。

因此每个 root fiber 的 split multiplicity，就是该 root 实际由多少不同 prime shells 命中。

P017 补充 20 将证明：

\[
\boxed{
R_{\min}(k)
=
\begin{cases}
2,&k\in\{5,6,8\},\\
1,&k\ge4,\ k\notin\{5,6,8\}.
\end{cases}
}
\]

并给出统一最小 repair bit。

这构成第二次完整反哺闭环：

\[
\text{P017 collision data}
\to
\text{P023 finite repair calculus}
\to
\text{P017 exact minimal repair theorem}.
\]

---

## 12. Executable specification

- `src/enterprise_math/task_precision_refinement.py`
- `tests/test_task_precision_refinement.py`

回归验证：task union 与 partition common refinement 完全一致；realized tuple count 可以严格小于形式笛卡尔积；最小 repair alphabet 等于最大局部 split multiplicity；小于该 alphabet 的所有 repair 编码在小模型上均失败；refinement chain 满足 repair 次乘法，且严格不等号可发生。

有限穷举用于 reconstruction / regression；定理证明本身如上为普通有限数学证明。

# P024 —— 伴随边界回拉演算，补充 02

状态：`ACTIVE RESEARCH NOTE`  
母文：`docs/P024_ACTION_LANGUAGE_PRECISION.zh-CN.md`  
范围：离散有序链、阈值观测，以及相关阈值逆像仍保持 principal 的前向动作  
依赖：P008 序伴随核心、P023 未来兼容 quotient 纪律与 P024 可达边界精度

## 1. 动机

P024 第一阶段把整数平移的未来安全 cuts 写成

\[
C_h=B-M_h.
\]

这个公式利用了一个特殊事实：平移 `a` 会把未来阈值 `b` 精确回拉成 `b-a`。

更底层的问题是：

> 什么性质保证一个前向动作把“一条阈值边界”逆向传播后仍然是一条精确阈值边界？

答案不是度量性质，而是序理论性质：

> 一个前向动作对**所有 principal 阈值**都保持精确回拉结构，当且仅当它在相关有序状态空间上是一个**右伴随**。

对某个声明的有限任务，动作也可能只在实际出现的 boundary orbit 上满足这一性质；全局右伴随只是对**全部** principal 阈值成立的干净统一条件。

本补充由此建立反变的边界演算。

## 2. Principal 阈值观测

设 `X` 为偏序状态空间。对 `b in X`，记

\[
\uparrow b=\{x\in X:b\le x\}.
\]

对应阈值 bit 为

\[
O_b(x)=\mathbf1_{b\le x}.
\]

设

\[
F:X\to X
\]

为前向动作。

若存在边界映射

\[
\lambda_F:X\to X
\]

满足

\[
\boxed{
F^{-1}(\uparrow b)=\uparrow\lambda_F(b)
}
\]

则称 `lambda_F` 为精确 principal boundary pullback。

等价地，

\[
\boxed{
\lambda_F(b)\le x
\iff
b\le F(x).
}
\]

## 3. P024-S2-T01 —— Principal 阈值回拉当且仅当左右伴随

状态：`PROVED`。

对映射 `F:X->X`，存在总边界映射 `lambda_F:X->X` 使

\[
F^{-1}(\uparrow b)=\uparrow\lambda_F(b)
\quad\text{对每个 }b
\]

当且仅当

\[
\boxed{\lambda_F\dashv F.}
\]

### 证明

由定义，

\[
x\in F^{-1}(\uparrow b)
\iff
b\le F(x).
\]

逆像恰为 `uparrow lambda_F(b)`，等价于

\[
b\le F(x)
\iff
\lambda_F(b)\le x,
\]

这正是 Galois/伴随关系。∎

因此，**全部** principal 阈值在精确回拉下闭合，并不是额外数值近似性质，而恰好就是前向动作的右伴随结构。

这是成熟序理论在 P024 未来边界语义下的重新解释；P024 不主张发明伴随定理本身。

## 4. P024-S2-T02 —— 前向复合变成反向边界复合

状态：`PROVED`。

若

\[
\lambda_F\dashv F,
\qquad
\lambda_G\dashv G,
\]

则

\[
\boxed{
\lambda_F\circ\lambda_G
\dashv
G\circ F.
}
\]

因此在状态偏序上选定 equality-faithful 伴随映射后，

\[
\boxed{
\lambda_{G\circ F}
=
\lambda_F\circ\lambda_G.
}
\]

### 证明

\[
(\lambda_F\circ\lambda_G)(b)\le x
\iff
\lambda_G(b)\le F(x)
\iff
b\le G(F(x)).
\]

∎

所以前向状态动力学与反向边界动力学按相反的函数复合顺序运行。

这才是 P024 平移公式出现 `B-M` 的结构原因：加法平移只是一般反变 boundary pullback calculus 的一个坐标实现。

## 5. P024-S2-T03 —— 链上的有限 horizon 伴随边界轨道定理

状态：`PROVED`。

现在令状态空间为离散全序 `Z` 或 `N_0`，并令

\[
F_1,\ldots,F_m
\]

为显式带左伴随

\[
\lambda_i\dashv F_i
\]

的前向动作。

当前观测完整报告有限阈值向量

\[
B=\{b_1,\ldots,b_q\}.
\]

对前向动作词

\[
w=(i_1,\ldots,i_k),
\]

约定 `F_(i_1)` 最先执行、`F_(i_k)` 最后执行，并定义回拉边界映射

\[
\lambda_w
=
\lambda_{i_1}\circ\cdots\circ\lambda_{i_k}.
\]

对 horizon `h` 定义

\[
\boxed{
C_h
=
\{\lambda_w(b):b\in B,\ |w|\le h\}.
}
\]

则对 `x<y`，

\[
\boxed{
\text{所有长度不超过 }h\text{ 的动作词之后阈值输出都相同}
\iff
(x,y]\cap C_h=\varnothing.
}
\]

因此最粗有限 horizon 未来安全商仍然是相对于回拉 cut 的整数 rank：

\[
\boxed{
\rho_h(x)=\#\{c\in C_h:c\le x\}.
}
\]

### 证明

对任意 boundary `b` 与动作词 `w`，反复使用 T02 得到

\[
b\le F_w(x)
\iff
\lambda_w(b)\le x.
\]

因此完整未来阈值语言，恰好等于当前状态对 `C_h` 中所有 cut 的比较集合。两个状态对全部这些比较一致，当且仅当两者之间没有 cut。∎

这样就能在无限有序状态空间上直接得到 P023 的闭式安全 quotient，而无需枚举所有细状态。

## 6. P024-S2-T04 —— 递归有限编译器与精确稳定判据

状态：`PROVED`。

定义

\[
C_0=B
\]

并递归令

\[
\boxed{
C_{h+1}
=
C_h
\cup
\bigcup_{i=1}^{m}\lambda_i(C_h).
}
\]

则该递归精确产生所有长度不超过 `h+1` 的动作词所能得到的边界回拉。

最朴素的动作词数量上界为

\[
\boxed{
|C_h|
\le
|B|\sum_{k=0}^{h}m^k.
}
\]

当 `m=1` 时即 `|B|(h+1)`；当 `m>1` 时，

\[
|C_h|
\le
|B|\frac{m^{h+1}-1}{m-1}.
\]

真实边界碰撞会使 cut 数远小于这个最坏界。

更重要的是，如果某个有限 `h` 满足

\[
\boxed{C_{h+1}=C_h},
\]

则 `C_h` 已经对所有生成元 `lambda_i` 闭合，因此

\[
\boxed{C_{h+k}=C_h\quad\text{对所有 }k\ge0.}
\]

所以只要 boundary orbit 本身有限并达到闭包，任意未来精度就能通过有限计算得到，不需要对无限状态空间做 partition refinement。

## 7. P024-S2-T05 —— 平移恰为加法特例

状态：`PROVED`。

对整数平移

\[
F_a(x)=x+a,
\]

定义

\[
\lambda_a(b)=b-a.
\]

则

\[
\lambda_a(b)\le x
\iff
b-a\le x
\iff
b\le x+a=F_a(x),
\]

故

\[
\lambda_a\dashv F_a.
\]

动作词累计平移为 `s` 时，

\[
\lambda_w(b)=b-s.
\]

于是 T03 给出

\[
\boxed{C_h=B-M_h,}
\]

正好恢复 canonical P024 第一阶段。

因此 `B-M` 不是母定律，而只是伴随边界回拉在加法坐标中的形式。

## 8. P024-S2-T06 —— P008 的根、商与 collapse 都是边界伴随动作

状态：`PROVED`，定义域为 `N_0`。

这一阶段把 P024 直接接回早期 P008 序核心。

### 整数根

P008 已有

\[
k^p\le n
\iff
k\le R_p(n).
\]

因此前向动作

\[
F=R_p
\]

的精确边界回拉为

\[
\boxed{
\lambda_{R_p}(b)=b^p.
}
\]

所以未来 root 状态上的阈值，会在当前状态上变成完全幂阈值。

### 整数商

对

\[
Q_d(n)=n//d,
\qquad d\ge1,
\]

有

\[
db\le n
\iff
b\le Q_d(n),
\]

故

\[
\boxed{
\lambda_{Q_d}(b)=db.
}
\]

### 完全幂 collapse

令

\[
C_p(n)=R_p(n)^p.
\]

定义不小于 `b` 的最小完全 `p` 次幂

\[
N_p(b)=\min\{k^p:k^p\ge b\}.
\]

则

\[
\boxed{
N_p(b)\le n
\iff
b\le C_p(n),
}
\]

所以

\[
\boxed{\lambda_{C_p}=N_p.}
\]

由于 `N_p` 幂等，

\[
N_p(N_p(b))=N_p(b),
\]

单个 `p`-collapse 动作的 boundary orbit 在一次回拉后就稳定，这恰好与 collapse 幂等性构成对偶。

这给出了 P008 伴随语义到 P024 未来安全精度语义的一条真正结构桥。

## 9. P024-S2-T07 —— 前向粗/细直觉可以被未来精度反转

状态：由精确例子 `PROVED`。

前向动作看起来是“粗化”还是“扩张”，并不能直接决定未来安全的**初始**精度是增长还是收缩。

### Floor division：前向 many-to-one 收缩，却产生扩张的边界层级

对

\[
F_d(x)=x//d,
\qquad d\ge2,
\]

在 `Z` 上有

\[
\lambda_d(b)=db.
\]

单边界 `B={1}` 且反复执行同一动作时，

\[
\boxed{
C_h=\{1,d,d^2,\ldots,d^h\}.
}
\]

所以

\[
|C_h|=h+1,
\]

整条链在 horizon `h` 下共有 `h+2` 个未来安全区间。

任意 horizon 的 cut orbit 是无限的。

因此，一个 many-to-one 的前向粗化映射，完全可能随着未来语言变长，要求初始状态保留越来越多区别。

反复整数根更极端：当 `b>=2` 时，回拉边界为

\[
b,b^p,b^{p^2},\ldots.
\]

### Dilation：前向扩张，却产生收缩边界层级

对

\[
G_d(x)=dx,
\qquad d\ge2,
\]

有

\[
\lambda_d(b)=\left\lceil\frac bd\right\rceil.
\]

任意有限整数边界集合都会在有限步后达到固定 orbit：大于 `1` 的正数幅度严格下降到 `1`，负数向 `0` 上升，而 `0,1` 都是不动点。

所以前向扩张反而可以产生有限的任意未来 boundary precision。

### 后果

不存在普遍成立的动力学口号，例如：

- “前向越粗化，初始精度需求一定越粗”；
- “前向越扩张，初始精度需求一定越细”。

真正精确的量始终是声明未来边界的 pullback orbit。

## 10. P024-S2-T08 —— 动作词可以按边界变换取商

状态：对完整带标签阈值向量 `PROVED`。

对动作词 `w`，定义其在声明 boundary 集上的 signature

\[
\boxed{
\Sigma_B(w)
=
(\lambda_w(b_1),\ldots,\lambda_w(b_q)).
}
\]

则两个动作词 `u,v` 满足

\[
\boxed{
\Sigma_B(u)=\Sigma_B(v)
}
\]

当且仅当它们在**每个**当前状态上都产生同样的完整阈值向量输出：

\[
O_B(F_u(x))=O_B(F_v(x))
\quad\text{对所有 }x.
\]

因此未来动作词语言本身，也可以按其对声明 boundary 集的作用取商。

平移情况下，所有累计位移相同的动作词都会合并；非线性伴随动作下，这个 quotient 可以非交换，并且当多个不同动作词诱导同一 boundary transformation 时，远小于原始动作词树。

这里不主张发明 automata minimization；它只是声明 P024 链语言在边界侧的精确形式。

## 11. P024-S2-T09 —— 全局右伴随比任务相对边界闭合更强

状态：`PROVED BY COUNTEREXAMPLE`。

T01 刻画的是**所有** principal 阈值都闭合的情况；某个声明的有限未来任务可能只需要更弱条件。

定义非单调整数映射

\[
F(-2)=-1,
\qquad
F(-1)=-2,
\qquad
F(x)=x\text{ otherwise}.
\]

它不是右伴随，因为 `uparrow(-1)` 的逆像不是 upper set：

- `-2` 映到 `-1`，被接受；
- `-1` 映到 `-2`，被拒绝；
- `0` 又被接受。

但对声明阈值 `B={0}`，

\[
F^{-1}(\uparrow0)=\uparrow0.
\]

而且任意次迭代仍保持，因为非单调交换完全发生在零以下。

所以任务相对 P024 compiler 可以在完整动作没有全局伴随时仍然工作。

正确层级应写成：

1. **全局右伴随**：全部 principal 阈值在回拉下闭合；
2. **orbit-relative principal closure**：只要求声明任务实际生成的 boundary 闭合；
3. 如果连这一点也失败，则单 cut 演算失效，必须使用更丰富的 P023 状态关系。

## 12. P024-S2-T10 —— 非单调回拉可以把一条边界裂成多个分量

状态：`PROVED BY COUNTEREXAMPLE`。

取

\[
F(x)=|x|
\]

作用于 `Z`，阈值 `b=1`。

则

\[
F^{-1}(\uparrow1)
=
(-\infty,-1]\cup[1,\infty),
\]

它不是 principal upper set。

显式地，

\[
F(-1)\ge1,
\qquad
F(0)<1,
\qquad
F(1)\ge1.
\]

任何单一整数 cut 都无法表示这个逆像。

因此，任意 state-dependent / 非单调动力学不能仅仅把 `B-M` 换成某个猜测位移集合，就强行塞回标量 P024 boundary-rank 公式。

正确未来状态可能需要多个 boundary 分量、更高维关系，或者回退到一般 P023 partition refinement。

## 13. 与 P008、P023、P024 补充 01 的关系

### P008

P008 拥有最小序伴随语义。补充 02 不重新主张 Galois connection 或伴随复合。它只给成熟结构增加项目侧新角色：**左伴随恰好是未来阈值边界的反向搬运律**。

### P023

P023 继续拥有一般未来安全 quotient / 最小修复。补充 02 在声明阈值语言始终保持 principal boundary 时，给出一个闭合的有限编译器。

### P024 补充 01

补充 01 处理高维晶格平移与完整仿射 guard 向量；补充 02 处理一维/链上非平移动作的伴随边界回拉。

目前不能把二者直接写成一个万能非线性晶格定理。下一条桥必须先说明：每个高维 guard score 是否自身按伴随链动作演化，以及公共 score-lattice 可行性如何与这些非线性 pullback 相互作用。

## 14. 可执行审计

实现：

- `src/enterprise_math/adjoint_boundary_precision.py`

测试：

- `tests/test_p024_adjoint_boundary_precision.py`

可执行层包括：

- 同时携带前向映射与 boundary pullback 的显式动作 witness；
- 平移、整数 dilation、floor division、自然数整数根、自然数 quotient 与完全幂 collapse；
- direct future threshold signature；
- 动作词的反变 boundary pullback；
- 有限 boundary-orbit 编译；
- 稳定化检测；
- 明确只作为回归审计、**不被当成全局证明**的有限 box adjunction 检查。

提交测试覆盖：

1. 精确恢复 canonical `B-M` 平移 cuts；
2. 混合平移/dilation/division/分段单调动作下 direct future signature 与 boundary rank 等价；
3. boundary pullback 的反向复合；
4. 根/商/collapse 伴随关系；
5. floor-division 的无限边界层级；
6. dilation 的有限稳定；
7. 相同 boundary transformation 下动作词合并；
8. 任务相对非单调例外；
9. absolute-value split-preimage no-go；
10. 有限动作词数量给出的 cut 上界。

独立重实现还对数百个带 plateau 与 jump 的随机单调 cofinal 整数映射做了 future-signature/rank 等价压力测试，未发现不一致。有限审计只支撑实现与陈述；T01–T10 由上面的证明/反例支撑。

## 15. 前人工作边界

Galois connection、左右伴随、伴随复合、floor/ceiling division 伴随，以及 principal upset 都是成熟序理论。P008 已登记相关结构邻域，包括 [SRC-MATHLIB-FLOORDIV] 与 [SRC-MATHLIB-CLOSURE]。

P024 不把这些数学工具本身声明为发明。

项目当前测试的综合，是把它们精确组织成：

\[
\boxed{
\text{前向右伴随动作语言}
\longleftrightarrow
\text{反变 principal-boundary pullback 语言}
\longrightarrow
\text{有限未来安全精度 cuts}.
}
\]

这一综合精度解释的历史新颖性继续保持 `NOVELTY_UNVERIFIED`。

## 16. 下一批压力测试

1. 桥接补充 01 与补充 02：多个 guard-score 方向上的非线性右伴随演化 + 公共 score-lattice 可行性；
2. 使用成熟 Galois-connection API 把 T01–T04 推入 Lean，而不是重新发明序理论；
3. 把 collapse-word 家族搬到边界侧，与 P019/P020 的不动点稳定化比较其 stable boundary map；
4. 在彻底回退 arbitrary P023 partition 前，研究非单调动作的 orbit-relative principal closure；
5. 把 boundary-orbit collision 作为精确动作语言压缩量研究，但不得与历史不可逆性或 entropy 混为一谈。

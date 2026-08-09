# P024 — 动作语言精度与可达边界轨道

状态：`ACTIVE CORE RESEARCH`  
范围：整数平移、有序阈值观测、可达动作幺半群、数值半群缺口、群完备化与循环周期化  
依赖：P023 未来兼容商/最小修复、P020 有限稳定化  
工程见证：E001 Boolean-contact bridge 与 E002 precision-locked actuation

## 1. 为什么需要 P024

P023 回答抽象问题：

> 给定一个表示关系以及声明的未来操作/观测语言，什么是足以支撑该未来的最粗关系？

E001 与 E002 又暴露出一个更具体的算术问题，而 P023 有意没有替它回答：

> 当状态是整数、未来操作是平移时，这个最粗关系究竟长什么样？

答案并不只由动作幅度的 gcd 决定。首先决定结构的是**实际可达的未来动作语言**。

单向平移语言能够保留数值半群缺口；真正双向的语言会完成为加法群；有限循环相位空间即使只允许正向重复生成，也会自动完成为子群。

P024 单独抽取这一算术层。

它不替代 P023。P023 负责一般商定理；P024 负责整数平移特化下的精确边界几何。

---

## 2. 有序阈值观测

令细状态为

\[
x\in\mathbb Z.
\]

令

\[
B=\{b_1<\cdots<b_r\}\subset\mathbb Z
\]

为有限观测边界集。整数边界 `b` 位于状态 `b-1` 与 `b` 之间。

定义有序区间观测

\[
\boxed{
O_B(x)=\#\{b\in B:b\le x\}.
}
\]

它只记录 `x` 落在由 `B` 切出的哪个区间。

令动作字母表为有限集合

\[
A\subset\mathbb Z.
\]

每个动作以其整数标签平移状态。对 horizon `h`，令

\[
M_h
=
\left\{
\sum_{j=1}^{k}a_j:
0\le k\le h,
\ a_j\in A
\right\}
\]

为长度不超过 `h` 的动作 word 所能实现的累计平移集合。

对任意有限未来 word，记

\[
M=\langle A\rangle_{\mathbb N}
\]

为 `A` 生成的加法子幺半群。

---

## 3. P024-T01 — 可达边界轨道定理

**状态：已证明。**

定义 horizon-`h` 的边界轨道

\[
\boxed{
\mathcal C_h=B-M_h
=\{b-m:b\in B,\ m\in M_h\}.
}
\]

对两个状态 `x<y`，下列条件等价：

1. 任意长度不超过 `h` 的动作 word 后，`x` 与 `y` 的 `O_B` 观测都相同；
2. 对所有 `m in M_h`，
   \[
   O_B(x+m)=O_B(y+m);
   \]
3. 二者之间不存在任何未来可见边界：
   \[
   \boxed{
   (x,y]\cap\mathcal C_h=\varnothing.
   }
   \]

因此，horizon-`h` 下最粗预测精度胞元，恰好就是由 `C_h` 切出的极大整数区间。

### 证明

对某个累计平移 `m`，有

\[
O_B(y+m)-O_B(x+m)
=
\#\{b\in B:x+m<b\le y+m\}.
\]

右侧为非负计数，因此两个观测相同，当且仅当该集合为空。

而

\[
x+m<b\le y+m
\]

等价于

\[
x<b-m\le y.
\]

所以对每一个可达 `m` 都相同，恰好等价于 `(x,y]` 中不存在任何平移后的边界 `b-m`。∎

### 解释

这里的精度不是事后人为加入的 tolerance。观测边界与允许的未来动作一旦给定，未来动作语言就会把那些边界**反向拉回当前状态空间**。这个边界轨道就是未来仍有能力读取的全部区别。

---

## 4. P024-T02 — 未来视野增长就是边界轨道增长

**状态：已证明。**

长度不超过 `h` 的 word 必然也是长度不超过 `h+1` 的 word，因此

\[
M_h\subseteq M_{h+1},
\]

从而

\[
\boxed{
\mathcal C_h\subseteq\mathcal C_{h+1}.
}
\]

所以扩大未来视野只能增加切分、细化精度胞元，不能重新合并已经被更短未来区分的状态。

这是 P023 “未来语言越丰富，安全关系只能更细”在整数边界上的具体形式。

---

## 5. P024-T03 — 单向阈值精度就是数值半群分割

**状态：已证明。**

只取一个阈值 `theta` 与正动作

\[
A=\{a_1,\ldots,a_m\}\subset\mathbb N_{>0}.
\]

此时

\[
M=\langle A\rangle\subset\mathbb N
\]

是包含零的有限生成加法半群。

考察阈值正下方连续 `L` 个整数状态：

\[
I_{\theta,L}
=
\{\theta-L,\ldots,\theta-1\}.
\]

在 horizon `h` 内，每一个真正可达的正位移

\[
s\in M_h\cap\{1,\ldots,L-1\}
\]

恰好在该窗口内产生一个边界 `theta-s`。

因此精确预测类别数为

\[
\boxed{
C_h(L)
=
1+
\left|M_h\cap\{1,\ldots,L-1\}\right|.
}
\]

对任意有限未来 word：

\[
\boxed{
C_\infty(L)
=
1+
\left|M\cap\{1,\ldots,L-1\}\right|.
}
\]

若状态到阈值的正整数距离为

\[
t=\theta-x,
\]

则一个规范的窗口内 rank 为

\[
\boxed{
\rho_h(t)
=
\#\{s\in M_h:0<s<t\}.
}
\]

因此单向未来下的预测精度由**真正可达的累计位移**决定，而不是由 gcd 单独决定。

---

## 6. P024-T04 — 群完备化过细缺陷的精确公式

**状态：已证明。**

令

\[
g=\gcd(a_1,\ldots,a_m).
\]

`A` 生成的加法群为 `g Z`。若把真实的单向幺半群 `M` 替换成其群完备化，那么宽 `L` 的阈值侧窗口会被所有小于 `L` 的正 `g` 倍数切开，因此得到

\[
\boxed{
C_{\rm grp}(L)
=
\left\lceil\frac{L}{g}\right\rceil
}
\]

个均匀 gcd 胞元。

定义与当前窗口相关的半群缺口

\[
\boxed{
H_{A,L}
=
\{kg:1\le kg<L,\ kg\notin M\}.
}
\]

则有精确恒等式

\[
\boxed{
C_{\rm grp}(L)-C_\infty(L)
=|H_{A,L}|.
}
\]

### 证明

小于 `L` 的正 `g` 倍数共有

\[
\left\lfloor\frac{L-1}{g}\right\rfloor
\]

个。`M` 中小于 `L` 的每一个正元素必然属于这些倍数。完整 gcd 切分与真实可达切分之差，恰好就是缺失的倍数 `H_{A,L}`。两边再加共同的初始胞元即可。∎

### 精确最小性判据

宽 `L` 窗口上的均匀 gcd refinement 已经最小时，当且仅当

\[
\boxed{H_{A,L}=\varnothing.}
\]

因此 gcd 可以是安全的，却仍然保留未来单向语言永远无法重新读取的多余区别。

### 最小见证

取

\[
L=7,
\qquad
A=\{4,6\}.
\]

则 `g=2`，但小于 `7` 的可达正位移只有

\[
\{4,6\}.
\]

位移 `2` 是半群缺口，所以

\[
C_\infty(7)=3,
\qquad
C_{\rm grp}(7)=4.
\]

---

## 7. P024-T05 — conductor 局域化的非均匀精度边界层

**状态：由标准数值半群 conductor 理论证明。**

按 gcd 归一化正生成元：

\[
S
=
\left\langle
\frac{a_1}{g},\ldots,\frac{a_m}{g}
\right\rangle.
\]

归一化生成元 gcd 为一，因此 `S` 是数值半群。令 `c(S)` 为 conductor，即最小的非负整数，使得任意 `n>=c(S)` 都属于 `S`。

于是任何缺失的群完备化边界，其位移都严格小于

\[
\boxed{g\,c(S).}
\]

等价地，当状态到阈值的距离至少达到 `g c(S)` 后，每一个 gcd 间隔边界都已经实际可达。

因此单向动作语言自然生成

\[
\boxed{
\text{有限非均匀边界层}
+
\text{渐近均匀 gcd 胞元}.
}
\]

非均匀边界层不是人工 patch，其中缺失的切分恰好就是数值半群 gaps。

这给出了 P023 “regular scale + localized bounded detail” 的一个精确整数实现。

---

## 8. P024-T06 — 真正双向的动作语言等于其群完备化

**状态：已证明。**

令

\[
D=\{\delta_1,\ldots,\delta_m\}\subset\mathbb Z\setminus\{0\}
\]

至少包含一个正动作和一个负动作，并令

\[
g=\gcd(|\delta_1|,\ldots,|\delta_m|).
\]

定义由非负 word 次数生成的动作幺半群

\[
M_D
=
\left\{
\sum_i n_i\delta_i:n_i\in\mathbb N
\right\}.
\]

则

\[
\boxed{M_D=g\mathbb Z.}
\]

### 证明

所有生成和都被 `g` 整除，所以 `M_D subseteq g Z`。

Bézout 恒等式给出 `g` 的整数系数表示。由于 `D` 同时包含正、负生成元，还存在一个所有系数都严格为正的零关系

\[
\sum_i z_i\delta_i=0.
\]

构造方法是：对每一对正/负生成元写出显然的两项正系数零关系，然后把这些关系求和。

对任意目标 `kg`，先取其整数系数 Bézout 表示，再加足够大的正零关系倍数，使所有系数都变成非负，而和值不变。于是每个 `kg` 都属于 `M_D`。∎

### 单阈值均匀坐标

对阈值 `theta` 定义

\[
\boxed{
K_{\theta,g}(x)
=
\left\lceil\frac{\theta-x}{g}\right\rceil.
}
\]

则

\[
\boxed{x<\theta\iff K_{\theta,g}(x)\ge1}
\]

且任意声明动作 `delta` 都满足精确传输

\[
\boxed{
K(x+\delta)
=
K(x)-\frac{\delta}{g}.
}
\]

因为未来动作幺半群已经是完整的 `g Z`，不同 `K` 值总能通过有限平移把其中一个送到阈值边界而区分。因此 `K` 是该单阈值平移语言任意未来的最粗状态。

逐幅度成对的 `+a/-a` 只是充分条件，不是必要条件。真正条件是未来可达性具有两个方向。

---

## 9. P024-T07 — 有限周期化会自动把幺半群完成为群

**状态：已证明。**

令 `G` 为有限群，`S` 为包含单位元的子幺半群，则

\[
\boxed{S\text{ 自动是 }G\text{ 的子群}.}
\]

### 证明

任取 `s in S`。由于 `G` 有限，`s` 具有有限阶 `n`。用加法记号：

\[
-s=(n-1)s.
\]

右侧只是对 `s` 的非负重复幺半群求和，所以 `-s in S`。因此 `S` 对逆元封闭。∎

### 循环群推论

在

\[
\mathbb Z/w\mathbb Z
\]

中，用整数 `a_1,...,a_m` 的 residue 生成动作，即使动作 word 只允许非负重复次数，可达 residue 幺半群也会自动成为

\[
\boxed{
\{0,g,2g,\ldots,w-g\}\pmod w,
\qquad
g=\gcd(w,a_1,\ldots,a_m),
}
\]

这个子群，共有

\[
\boxed{w/g}
\]

个 residue。

这正是 E002 Stage 2 背后缺失的结构解释：一旦胞元内部相位按宽度 `w` 周期化，反复执行“正向”动作本身就能够模 `w` 实现逆元。整数无限链上能够永久存在的数值半群 holes，在有限循环相位群中不能继续存在。

---

## 10. P024-T08 — 整数链与循环相位的精度二分

**状态：在上述加法整数/循环范围内已证明。**

相同的整数动作幅度，在不同状态拓扑下会产生不同的未来精度结构。

### 无界有序整数链

在 `Z` 上只允许单向正平移时，未来语言是数值半群：

- gcd 的某些正倍数可以永久不可达；
- 这些 holes 会删除对应的未来可见阈值切分；
- 所以观测边界附近的最粗预测胞元可以不均匀。

### 有限循环相位

一旦把相位模 `w` 周期化，同样的非负动作 word 生活在有限群中：

- 生成幺半群自动对逆元封闭；
- 可达性变成 gcd 子群；
- semigroup holes 通过周期回绕消失。

因此

\[
\boxed{\text{动作幅度本身不足以决定精度。}}
\]

精度几何共同取决于

\[
\boxed{
\text{状态拓扑}
+
\text{未来动作幺半群}
+
\text{观测边界}.
}
\]

这就是 E001 与 E002 工程结果在底层上的统一解释。

---

## 11. 与 P023 的职责边界

P024 是 P023 的精确算术特化。

P023 给出

\[
\text{未来语言}
\longrightarrow
\text{最粗未来安全等价关系}.
\]

P024 则说明：对于整数平移与有序阈值观测，这个关系能够直接由

\[
\boxed{B-M}
\]

——观测边界在可达平移幺半群下的轨道——算出来。

P023 继续负责：

- 任意有限状态空间；
- 任意确定性操作；
- 一般未来兼容商；
- 最小修复；
- safe-selector 的组合与稳定化。

P024 负责：

- 一维整数平移可达性；
- 精确边界轨道胞元；
- 数值半群 holes 作为缺失的精度切分；
- gcd 过细缺陷的精确计数；
- conductor 局域非均匀精度；
- 真正双向平移语言的群完备化；
- 有限循环周期化下的自动群完备化。

---

## 12. 工程推论，但不倒置理论归属

### E001 Boolean contact

候选观测

\[
Contact_d(g)\iff g<d
\]

正是单阈值 `B={d}`。因此，一旦 E001 声明该物理观测，contact bridge 的整数闭式都成为 P024 阈值窗口定理的推论。

但 Boolean contact quotient 不是完整碰撞状态。若 rebound law 读取精确 gap/penetration、速度、动量、冲击相位、形变或材料状态，就会引入新的状态变量/观测边界，必须按 P023/P024 重新编译。

### E002 precision-locked actuation

E002 的中心胞元内部相位是模胞元宽度 `w` 的有限状态。P024-T07 解释了为什么“只正向”的平移动作族也会生成完整循环 gcd 子群。E002 的精确稳定宽度

\[
\gcd(w,|a_1|,\ldots,|a_m|)
\]

因此与周期相位中不存在单向 semigroup holes 完全一致。

E002 仍拥有中心 quotient 的精确特化定理；P024 只提供更底层的可达性解释。

---

## 13. 可执行审计

实现：

- `src/enterprise_math/action_language_precision.py`

测试：

- `tests/test_p024_action_language_precision.py`

探针：

- `experiments/p024_action_language_precision_probe.py`

测试独立覆盖：

- 多个阈值集合与 signed action alphabet 下，边界轨道定理与直接 future signature 完全一致；
- 单向有限 horizon 与任意未来类别计数；
- gcd 过细量恰等于相关 semigroup holes 数；
- conductor 能局域全部 holes；
- mixed-sign gcd 坐标的精确传输；
- 小规模循环动作族穷举，验证仅正向生成的 residue monoid 恰等于预期 gcd 子群。

提交前的独立重建未发现反例。

---

## 14. 前人工作与新颖性边界

数值半群、gaps、Apéry 集、Frobenius 数与 conductor 都是成熟数学；Bézout 恒等式、加法子群生成、有限群逆元与循环群 gcd 子群公式也都是成熟数学。有限状态行为最小化与一般未来等价已经在 E002/P023 中登记为前人工作。

P024 不把这些工具本身声明为发明。

Enterprise Math 当前真正测试的研究贡献是把它们精确组织成一套精度演算：

\[
\boxed{
\text{可达未来动作语言}
\to
\text{观测边界轨道}
\to
\text{当前最小精度胞元},
}
\]

并明确得到链/循环二分，以及“数值半群 hole = 相对于群完备化精度网格被删除的切分”这一解释。

历史新颖性继续标记为 `NOVELTY_UNVERIFIED`。

---

## 15. 下一轮压力测试

1. 多阈值 + 群完备化：研究多个 boundary coset 的周期并集，而不是默认单一均匀 gcd 网格；
2. state-dependent actions：可达对象不再是与状态无关的加法幺半群；
3. 高维边界 arrangement 与 lattice actions；
4. 非平移操作下是否仍存在简单的边界 pullback orbit；
5. API 稳定后，把 T01、T06、T07 推入 Lean；
6. 继续寻找新的工程域，测试 boundary-orbit compilation 是否能替代人为 epsilon/deadband/tolerance。

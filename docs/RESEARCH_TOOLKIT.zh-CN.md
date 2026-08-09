# Enterprise Math / 进取数论研究工具箱 v1

状态：`ACTIVE METHODOLOGY / THEOREM-LIFTING GUIDE`  
日期：2026-08-09  
范围：从 P007/P008/P018/P019/P023/P024 与 E001/E002/P017 已验证路线中提炼可重复使用的数学研究工具  
纪律：本文组织的是研究接口与使用顺序。Galois connection、partition refinement、Euclidean division、集合像分离、Möbius inversion 等成熟数学不属于项目原创。

## 1. 为什么需要工具箱

当前项目已经反复出现同一种现象：

- 一个应用路线先发现具体整数结构；
- 随后另一路线用不同术语重新发现相同 obstruction；
- 最后才意识到它们都属于同一个 quotient、adjunction、boundary、defect 或 stabilization 问题。

这说明下一阶段的瓶颈已经不只是“多证明定理”，而是：

> **把已经证明有效的研究动作压成少数母工具，使新的数论问题先经过统一编译，再进入领域特化。**

工具箱的目标不是让所有问题长得一样，而是让研究者优先问对以下问题：

1. 真正声明的状态是什么？
2. 允许哪些后续操作？
3. 最终要区分什么 observable/query？
4. 哪些当前区别对这些未来任务永远不可见？
5. 如果粗状态不够，最小 repair 是什么？
6. 是否存在结构化 fast path，避免枚举整个状态空间？
7. transient complexity 与 stable normal form 是否应该分开？
8. 有限性到底需要全局成立，还是只需要任务相关轨道局部闭合？

---

## 2. 工具一：Future-context quotient compiler

### 2.1 输入

声明：

- 状态空间 `X`；
- 动作/运算生成元 `T_a:X->X`；
- observable `O:X->Y`；
- horizon `h`，或任意有限未来语言。

对动作词 `w` 记复合为 `T_w`。

定义 horizon-`h` future signature：

\[
\boxed{
\Sigma_h(x)
=
\bigl(O(T_w(x))\bigr)_{|w|\le h}.
}
\]

于是最粗精确未来商就是 signature 的 kernel：

\[
\boxed{
x\sim_h y\iff\Sigma_h(x)=\Sigma_h(y).}
\]

### 2.2 已有实现

- P023：operation-family recursive refinement；
- E002：generic finite predictive quotient compiler；
- A2：长期 mother owner。

有限 `X` 上可以 partition refinement；无限 `X` 上不能因此默认枚举，必须继续寻找下面的结构化工具。

### 2.3 使用原则

先声明 future language，再谈“需要多少精度”。

因此研究中禁止把一个预先选择的尺度 `d` 自动等同于数学上必要的 precision。真正对象是：

\[
\boxed{
\text{RequiredPrecision}
=
F(\text{representation},\text{actions},\text{observations},\text{horizon}).
}
\]

这首先是预测充分性定理，不自动成为物理本体主张。

---

## 3. 工具二：Boundary pullback compiler

当 observable 由少量阈值/guard 生成，而且 forward map 有序结构良好时，不要枚举 states；编译**边界**。

### 3.1 伴随 fast path

若

\[
\lambda_F\dashv F,
\]

即

\[
\boxed{
\lambda_F(b)\le x
\iff
b\le F(x),
}
\]

则 future threshold `b` 在当前状态上的精确义务就是 `lambda_F(b)`。

状态向前复合，边界反向复合：

\[
\boxed{
\lambda_{G\circ F}
=
\lambda_F\circ\lambda_G.
}
\]

### 3.2 canonical arithmetic 实例

- translation `x->x+a`：`b->b-a`；
- integer quotient `Q_d`：`b->db`；
- integer root `R_p`：`b->b^p`；
- power collapse `C_p`：`b->N_p(b)`，即向上最近完全 `p` 次幂。

### 3.3 有限编译

有限 boundary set `B` 在生成元左伴随下递归闭包：

\[
C_0=B,
\qquad
C_{h+1}=C_h\cup\bigcup_a\lambda_a(C_h).
\]

如果某一步

\[
C_{h+1}=C_h,
\]

则任意更远未来已经稳定。

这说明：**无限状态空间仍可能拥有有限的精确 future quotient**，只要相关 boundary orbit 有限闭合。

---

## 4. 工具三：Defect / minimal-repair compiler

当 coarse representation `q:X->Q` 与未来操作 `F` 不交换时，不要把失败写成“近似误差”。

先检查 factorization：是否存在 `F_bar` 使

\[
q\circ F=\bar F\circ q.
\]

若失败，则在每个 coarse fiber 内只按 `q(F(x))` 真正产生的不同结果继续分裂。

因此一步最小 repair 的抽象形式就是：

\[
\boxed{
(q(x),\operatorname{class}_{q(x)}(q(F(x))))
}
\]

而不是默认补回完整 fine state。

### 4.1 已出现的具体 defect

- P018：carry / borrow；
- P018：collapse/refinement commutation defect；
- P023：crossing bit；
- E002：carry threshold rank；
- P024：pulled-back boundary rank。

### 4.2 核心理念

\[
\boxed{
\text{noncommutation defect}
\neq
\text{numerical error}.
}
\]

它通常是一个**精确、有限、有界、可组合的 repair coordinate**。

研究中应优先寻找 defect 的最小状态空间，而不是恢复全部 remainder/detail。

---

## 5. 工具四：Image-separation / label-erasure test

如果当前状态写成 shell label 加内部坐标

\[
(i,x),
\qquad x\in W_i,
\]

先问 label 是否已经冗余。

### 5.1 当前删除

删除映射 `(i,x)->x` 可逆到完整 tagged state，当且仅当 `W_i` 两两不交。

### 5.2 经过未来映射后仍恢复 label

对 `G:X->Y`，shell label 能从 `G(x)` 恢复，当且仅当

\[
\boxed{
G(W_i)\cap G(W_j)=\varnothing
\quad(i\ne j).
}
\]

完整原状态可恢复还额外要求每个 `G|W_i` 单射。

### 5.3 为什么这是重要研究工具

很多“资源碰撞”其实来自先把真实集合扩大成 candidate superset，再在扩大集合上数 overlap。

P017 给出目前最清楚的反例：

- exact cofactor windows 从 `k>=4` 起不交；
- 扩大后的 root candidate pairs 要到 `k>=15` 才不交；
- actual root images 实际从 `k>=9` 起已经不交。

所以：

\[
\boxed{
\text{over-approximation can manufacture false collisions.}
}
\]

除非上界证明明确需要，否则研究中应先计算 actual image，再决定是否扩张。

---

## 6. 工具五：Fixed-skeleton / stable-normal-form compiler

一个非交换、路径敏感的 transient system，长期语义可能远比瞬态简单。

### 6.1 先求 fixed skeleton

对 reductive monotone map `F`，稳定点由

\[
\operatorname{Fix}(F)
\]

控制。

在适当终止条件下，反复作用 `F` 计算初态下方的最大 fixed point。

P019 的 collapse-word 实例：

\[
W=C_{p_m}\cdots C_{p_1},
\qquad
L=\operatorname{lcm}(p_1,\ldots,p_m),
\]

虽然 transient word 可以非交换，稳定函数却是

\[
\boxed{
\operatorname{Stab}(W)=C_L.
}
\]

稳定等价商因此变成 lcm join-semilattice。

### 6.2 研究纪律

必须分开：

- transient path information；
- fixed-point skeleton；
- stable input-output normal form。

不要因为 stable quotient 交换，就倒推原动态交换；也不要因为 transient 很复杂，就假设稳定语义同样复杂。

---

## 7. 工具六：Local-finiteness / trapped-orbit principle

项目早期很容易把“有限数学”误解成“全宇宙必须是有限集合”。当前研究已经显示这太强。

真正经常使用的是：

> 声明任务相关的 state orbit、boundary orbit、quotient window、guard lattice slice 或 fixed interval 被困在一个有限集合里。

例如 P019 在 `N_0` 上并不需要整个自然数集有限；每条 collapse orbit 被困在

\[
[C_L(n_0),n_0]
\]

这个有限整数区间。

P024 也不需要整个 ordered state space 有限；只要 relevant boundary orbit 达到有限闭包即可。

因此优先证明：

\[
\boxed{
\text{task-local finite closure}
}
\]

而不是无谓地加强为 global finiteness。

这条原则正在继续形式化为“显式 fixed bound + locally finite interval”的稳定化母定理；在形式化完成前保持 research-only。

---

## 8. 六个工具之间的统一流程

一个新的数论/工程问题优先经过以下编译链：

### Step 1 — 声明语义

写清：

\[
(X,\mathcal A,O,h).
\]

不要先选 precision scalar。

### Step 2 — 编译 exact future quotient

原则上使用 context signature/kernel。

### Step 3 — 寻找结构化 fast path

依次检查：

- quotient/remainder coordinate；
- order adjunction；
- boundary pullback；
- residue lattice / CRT；
- shell image separation；
- monotone interval geometry。

### Step 4 — 隔离 obstruction

若不能直接下沉，求最小 defect/repair，而不是恢复全部 fine state。

### Step 5 — 找 task-local finite closure

证明相关 orbit/window/guard slice 有限，给出有限算法或 exact recurrence。

### Step 6 — 分离 transient 与 stable semantics

求 fixed skeleton、stable normal form、asymptotic quotient。

### Step 7 — theorem lifting

把领域假设逐项删掉，送回 A0–A5 唯一 mother owner；应用路线只保留 corollary、sharp threshold、counterexample 与 provenance。

---

## 9. 强制反例轴

任何“看起来已经统一”的工具至少沿下面几条轴压力测试：

1. **actual set vs candidate superset**：是否制造假 collision？
2. **finite vs arbitrary horizon**：短期安全是否会在更远未来破裂？
3. **one-sided semigroup vs two-sided action language**：holes 是否被 group completion 填平？
4. **full vector vs aggregated observable**：坐标乘积公式是否仍成立？
5. **monotone/right-adjoint vs nonmonotone map**：principal boundary 是否 split？
6. **global finite vs local bounded**：是不是偷偷用了过强有限性？
7. **transient vs stable**：路径非交换是否真的传到稳定层？
8. **label recovery vs full-state recovery**：是否把“知道来自哪个 shell”误当成“知道原状态”？

这些不是测试清单附件，而是 theorem-generalization 的组成部分。

---

## 10. 提炼出的基础理念

### 理念 A —— 精度首先是“最小充分区分”，不是数字位数

一个 precision object 应回答：

> 为了声明的未来运算与查询，现在至少必须区分哪些状态？

均匀网格、十进制位数、固定半径只是可能的实现，不是基础定义。

### 理念 B —— 状态向前，证明义务/边界向后

forward dynamics 作用在 state；未来 query 的边界通过 pullback 反向传播。

\[
\boxed{
\text{state evolution: covariant}
\qquad
\text{query obligation: contravariant}.
}
\]

P008 的 adjunction 因而同时控制“前向算术”与“反向证明边界”。

### 理念 C —— 缺陷是信息，不是误差

carry、borrow、commutation defect、boundary crossing 都是 exact finite witnesses。

研究目标不是把 defect “估计小”，而是确定：

- 它取多少状态；
- 如何组合；
- 什么时候为零；
- 最少需要保留多少。

### 理念 D —— 粗化可以制造假结构

coarsening 不只会“丢信息”。当它用 supersets、bucket 或 coarse basin 代替 actual states 时，还可能制造原系统不存在的 collision、multiplicity 与 apparent coupling。

P017 `15 -> 9` 是目前最清楚的数论实例。

### 理念 E —— 稳定骨架与瞬态历史是不同对象

长期 normal form 可以丢掉大量 word order，而不意味着这些信息在 transient 中不存在。

### 理念 F —— 有限性应优先是任务局部的

不需要先假定整个数学宇宙有限。只要本次证明真正能访问的 orbit/closure 有限，就能得到完全有限、精确的演算。

---

## 11. 对 A0–A5 的直接反哺

### A0 — Primitive discrete algebra

新增研究默认：每个除法/factor-stripping 问题先编译 exact quotient window；每个 root/quotient/collapse 先检查 adjoint boundary law。

P017 L054 已回灌为 P007 quotient-window theorem。

### A1 — Functional dynamics / stabilization

把“存在稳定语义”与“有限迭代如何计算”分开。下一母层应优先研究 extremal fixed selector，再单独给 global well-founded / local bounded termination 条件。

### A2 — Future-compatible quotient

P023 继续拥有 context-kernel、minimal repair 与新 image-separation zero-repair test。P024 是阈值/伴随可闭式化时的 structured fast path。

### A3/A4 — Relation/support

未来应把“image separation”“minimal repair”“future context”推广到 structured relation state 与 multivalued support，但禁止直接从 function 公式机械搬运；split-completeness 与 MAY/MUST 必须重新证明。

### A5 — Intrinsic geometry

先声明 primitive guard/query，再由 A2 编译需要保留的 geometry precision；不能反过来先选 Euclidean-like resolution 再宣布它天然充分。

---

## 12. 对数论主线的立即反哺

### 12.1 Factor stripping 先删维度

P007 T09–T12 先决定 `(factor,cofactor)` 中 factor label 是否已经被 exact cofactor window 编码。

### 12.2 Root/quotient 后检查 actual images

不用 candidate superset 代替 realized image，除非证明只需要上界。

P017 L055 因此把 actual lower-band root-channel stable threshold 从 `15` 推进到 `9`。

### 12.3 递归前先求 zero-repair 区域

如果一个 scale/channel 已经由 image separation 证明无跨 shell collision，就不再把 shell multiplicity 带进下一层递归。

### 12.4 计数应晚于结构压缩

先做：

\[
\text{exact transport}
\to
\text{label erasure}
\to
\text{minimal repair}
\to
\text{local closure}
\]

再做 cardinality / analytic estimate。

否则很容易用一个人为扩大的状态空间证明一个本来不存在的“容量困难”。

---

## 13. 什么还不能提升为基础定理

以下内容继续保持 research-only：

1. 任何“自然本体会自动选择 future-safe quotient”的物理解释；
2. 尚未完成 Lean 的 local-bounded stabilization 一般母定理；
3. 将 function-level image separation 直接推广到 multivalued correspondence；
4. 把所有数论困难都归结为 boundary arrangement；
5. 任何从有限计算直接推断无限一般性的结论。

工具箱的用途恰恰是把这些边界写清楚，而不是制造新的万能理论。

---

## 14. 成功判据

以后一个新结果只有满足下面至少一项，才算真正反哺底层：

- 删除了应用特有假设，形成更一般 mother theorem；
- 给已有 mother theorem 找到新的 sharp arithmetic specialization；
- 找到 counterexample，迫使基础定理缩小假设；
- 把 state enumeration 压成 boundary/residue/window closed form；
- 把完整 detail 压成 minimal repair；
- 把 global finiteness 压成 task-local closure；
- 把 transient monoid 压成 stable normal form；
- 证明一个辅助 label 可以被安全删除。

如果只是给已有公式换名字、增加术语或增加一个领域例子，而没有改变 theorem ownership、假设强度、状态复杂度或证明能力，就不算底层推进。

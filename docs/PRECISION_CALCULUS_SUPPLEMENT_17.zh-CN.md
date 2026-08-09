# P018 —— 有限精度证明演算：补充 17

状态：`ACTIVE RESEARCH NOTE`  
范围：observation kernel、precision state 的动态闭包、semiconjugacy、merger-time contraction、quotient-operation descent，以及 carry 作为精确 closure data  
依赖：P005、P008、P009、P010、P011、P018-T71—T149  
纪律：quotient factorization、congruence relation、semiconjugacy 与 operation descent 都属于成熟数学。本文研究它们在进取数论有限精度语义中的精确作用，不主张这些一般结构为项目发明。

---

## 1. 真正的 state merging 与 observed equality 不是同一件事

设 fine deterministic dynamics 为

\[
F:X\to X,
\]

observation / precision projection 为

\[
O:X\to Y.
\]

在时间 `n`，定义 observed equality：

\[
\boxed{
O(F^{[n]}x)=O(F^{[n]}y).
}
\]

这弱于真正的 state equality：

\[
F^{[n]}x=F^{[n]}y.
\]

真正 equality 一旦发生，在之后任何共同 deterministic suffix 下都永久保持；但 observed equality **不一定**永久保持，因为隐藏的 fine detail 可能在后续 observation 中重新显现。

在把 P010 irreversibility language 用到 coarse precision level 之前，必须先区分这两件事。

---

## 2. P018-T150 —— 固定时间下，postprocessing 只能使 observation kernel 变粗

状态：`PROVED / EXECUTABLE`

设

\[
O_1:X\to Y,
\qquad
H:Y\to Z,
\qquad
O_2=H\circ O_1.
\]

对任意固定时间 `n`：

\[
\boxed{
\ker(O_1\circ F^{[n]})
\subseteq
\ker(O_2\circ F^{[n]}).
}
\]

### 证明

如果

\[
O_1(F^{[n]}x)=O_1(F^{[n]}y),
\]

对两边施加 `H` 即得

\[
H(O_1(F^{[n]}x))=H(O_1(F^{[n]}y)).
\]

∎

因此，**在同一时间切片上，precision coarsening 永远只能让 kernel 更粗。**这一轴不需要 dynamic closure 假设。

---

## 3. P018-C14 —— coarse observational equality 可以在以后重新分开

状态：`COUNTEREXAMPLE / FOUNDATIONAL WARNING`

取自然坐标：

\[
F(n)=2n,
\qquad
O(n)=n//2.
\]

时间零时：

\[
O(0)=O(1)=0.
\]

所以 histories `0` 与 `1` 在 observation 上不可区分。

一步 fine dynamics 后：

\[
F(0)=0,
\qquad
F(1)=2,
\]

从而

\[
O(F(0))=0,
\qquad
O(F(1))=1.
\]

observed pair 离开了 diagonal。

因此：

\[
\boxed{
\text{某一 precision 下的 observed equality}
\not\Rightarrow
\text{未来 observed equality 永久保持}.
}
\]

这不违反 P010。两个 fine histories 从未真正成为同一个 fine state，只是 coarse readout 暂时重合。

---

## 4. P018-T151 —— Dynamic closure 精确等价于 observation kernel 被 dynamics 保持

状态：`PROVED`

定义 observation kernel congruence 条件：

\[
\boxed{
O(x)=O(y)
\Longrightarrow
O(Fx)=O(Fy).
}
\]

以下三条等价：

1. 上述条件成立；
2. time-zero observed kernel 包含于 time-one observed kernel；
3. 对所有 `n`：
   \[
   \ker(O\circ F^{[n]})
   \subseteq
   \ker(O\circ F^{[n+1]}).
   \]

### 证明

`3 -> 2` 显然；`2 -> 1` 正好就是时间零与时间一的定义展开。

对 `1 -> 3`，若

\[
O(F^{[n]}x)=O(F^{[n]}y),
\]

把 kernel-congruence 条件应用到中间 fine states `F^[n]x`、`F^[n]y`，即可得到再走一步后的 observation equality。∎

所以 coarse observation 具有 P010 式不可逆 kernel filtration，**当且仅当它的 fibers 对 fine dynamics 前向闭合。**

---

## 5. P018-T152 —— 对 surjective observation，dynamic closure 等价于存在自治 coarse dynamics

状态：`PROVED / ESTABLISHED QUOTIENT-FACTORIZATION THEOREM`

假设

\[
O:X\twoheadrightarrow Y
\]

为 surjective。

则 kernel-congruence 条件

\[
O(x)=O(y)
\Rightarrow
O(Fx)=O(Fy)
\]

成立，当且仅当存在唯一 deterministic map

\[
G:Y\to Y
\]

使

\[
\boxed{
O\circ F=G\circ O.
}
\]

### 证明概要

若 `G` 已存在，则相同的 `O`-image 经过同一个 `G` 后仍相同，因此 kernel compatibility 成立。

反过来，对任意 `y in Y` 选择一个 `O(x)=y` 的 representative，定义

\[
G(y):=O(Fx).
\]

kernel compatibility 保证该定义与 representative 的选择无关。surjectivity 保证每个 `y` 都有定义，也保证 `G` 唯一。∎

### 对 precision 的意义

一个 precision coordinate 在 operation `F` 下是否动态自足，精确取决于 `F` 是否能下降穿过 precision quotient。

如果不能下降，则 coarse coordinate 本身不足以做 exact evolution；hidden detail 对未来 coarse state 仍然重要。

---

## 6. P018-T153 —— Semiconjugacy 在同一时间搬运 finite coalescence

状态：`PROVED / LEAN TARGET`

若

\[
O\circ F=G\circ O,
\]

则有限迭代严格满足

\[
O\circ F^{[n]}=G^{[n]}\circ O.
\]

因此

\[
F^{[n]}x=F^{[n]}y
\Longrightarrow
G^{[n]}(O x)=G^{[n]}(O y).
\]

在 `CoalescedBy` language 中：

\[
\boxed{
\operatorname{CoalescedBy}_F(n;x,y)
\Longrightarrow
\operatorname{CoalescedBy}_G(n;Ox,Oy).
}
\]

新的 Lean theorem `coalescedBy_semiconj` 使用 mathlib 已有的 `Semiconj.iterate_right` 形式化该 relation-level 结论。

---

## 7. P018-T154 —— coarse semiconjugacy 使 merger time 收缩；injective chart change 保持 merger time

状态：`PROVED / LEAN RELATION-LEVEL SUPPORT`

当 finite merger time 存在时，T153 给出

\[
\boxed{
\bar\tau_G(Ox,Oy)
\le
\bar\tau_F(x,y).
}
\]

noninjective coarse representation 可以让 histories 更早被识别为同一状态。

若 `O` injective，则 observed iterates equality 反推 fine iterates equality，所以每个 finite coalescence level 都严格等价：

\[
\boxed{
F^{[n]}x=F^{[n]}y
\iff
G^{[n]}(Ox)=G^{[n]}(Oy).
}
\]

因此：

\[
\boxed{
\bar\tau_G(Ox,Oy)=\bar\tau_F(x,y).
}
\]

特别地，bijective precision-chart change 配合 conjugated dynamics 时，完整 labelled merger-time geometry 严格不变。

这在正确假设下解决了 P018-Q112：**合法 invertible chart transition + conjugated dynamics**。

---

## 8. P018-T155 —— compatible precision chain 产生真正的 precision-time bifiltration

状态：`PROVED STRUCTURAL CONSEQUENCE`

假设 precision observations 构成 coarsening chain

\[
O_c=H\circ O_f,
\]

并且每个 level 都 dynamically closed，因此存在自治 coarse dynamics，且 observation maps 与 dynamics commute。

对同一组带标签 fine histories 定义 precision-time kernel：

\[
K_{O,n}
=
\{(x,y):O(F^{[n]}x)=O(F^{[n]}y)\}.
\]

则有两个 monotonic axes。

### Precision axis

固定 `n`：

\[
\boxed{
K_{O_f,n}\subseteq K_{O_c,n}.
}
\]

即 T150。

### Time axis

固定 dynamically closed `O`：

\[
\boxed{
K_{O,n}\subseteq K_{O,n+1}.
}
\]

即 T151。

因此 compatible precision 与 deterministic time 共同生成一个递增的 two-parameter kernel family。

如果 dynamic closure 不成立，则只能保证 precision axis；time axis 可以像 C14 那样反向。

这是一个有限 bifiltration 结论，不宣称 precision 与 time 存在 categorical duality。

---

## 9. P018-T156 —— 固定时间下 P011 spectrum 随 precision coarsening 单调增加

状态：`DERIVED FROM P011 / PROVED`

固定有限 labelled history set `H` 与时间 `n`。

coarser observation 是 finer observation 的 postcomposition，因此它的 kernel partition 是 finer partition 的 coarsening。由 P011-S02，系数逐项有

\[
\boxed{
K_{O_f,n}(t)
\preceq_{\rm coeff}
K_{O_c,n}(t).
}
\]

所以**在同一个时间切片上**，precision coarsening 只能增加或保持各阶 observed collision count。

但沿 time axis，只有 dynamically closed observation 才拥有同样的 monotonicity。

C14 已给出显式失败：对 histories `{0,1}`、`F(n)=2n`、`O(n)=n//2`，observed quadratic collision count 从 time zero 的 `1` 降到 time one 的 `0`。

所以 observed collision-spectrum 的时间单调性并不是 coarse readout 的自动规律，而是 dynamically closed quotient evolution 的规律。

---

## 10. P018-C15 —— Quotient coordinate 单独无法承载 exact addition

状态：`COUNTEREXAMPLE / DESCENT OBSTRUCTION`

令

\[
Q_r(n)=n//r,
\qquad r>1.
\]

假设 coarse coordinates 上存在 binary operation `boxplus`，满足对所有 `x,y`：

\[
Q_r(x+y)=Q_r(x)\boxplus Q_r(y).
\]

比较 fine input pairs

\[
(0,0)
\]

和

\[
(r-1,1).
\]

两者 coarse coordinate pair 完全相同：

\[
(Q_r(0),Q_r(0))=(0,0),
\]

以及

\[
(Q_r(r-1),Q_r(1))=(0,0).
\]

但 coarse sum 不同：

\[
Q_r(0+0)=0,
\qquad
Q_r((r-1)+1)=Q_r(r)=1.
\]

所以只依赖 quotient coordinates 的 coarse binary operation 不可能精确重建 fine addition。

这比“floor projection 不是 additive homomorphism”更强：它说明 coarse quotient coordinate 本身**不是 exact addition 的 sufficient state**。

---

## 11. P018-T157 —— Detail + carry 是恢复 additive closure 的精确 extension data

状态：`DERIVED FROM T72–T75 / PROVED`

写成

\[
x=ra+u,
\qquad
y=rb+v,
\qquad 0\le u,v<r.
\]

则

\[
\boxed{
Q_r(x+y)
=a+b+\kappa_r(u,v),
}
\]

且

\[
\boxed{
(x+y)\bmod r
=(u+v)\bmod r.
}
\]

因此 enriched state

\[
(a,u)
\]

具有 exact closed twisted addition，而只有 coarse coordinate `a` 时做不到。

所以 carry 不只是 arithmetic correction term。在 descent language 下，它是**非 congruent quotient 后恢复 exact operation closure 所需 extension data 的组成部分**。

carry extension 形成 cocycle 属于成熟前人工作；本文的新关注点是它对 precision-state sufficiency 的作用。

---

## 12. P018-T158 —— Critical-square defect 衡量某个 proposed coarse operation 是否确实为 descent

状态：`PROVED / REINTERPRETATION`

给定

\[
\pi:X_e\to X_d,
\qquad
F_e:X_e\to X_e,
\qquad
F_d:X_d\to X_d,
\]

Supplement 12/13 比较两个 endpoints：

\[
\pi(F_e(x))
\quad\text{与}\quad
F_d(\pi(x)).
\]

proposed coarse operation 成为 exact descent，当且仅当所有 critical-square pair 都在 diagonal：

\[
\boxed{
\pi\circ F_e=F_d\circ\pi.
}
\]

因此 nonzero critical-square defect 证明**这个 proposed** `F_d` 不是 fine dynamics 的精确下降。

必须严格区分：

- 一个 proposed `F_d` 失败，不代表绝对不存在其他 coarse descent；
- “任何 descent 都不存在”的绝对 obstruction，要由 T151/T152 的 kernel-congruence failure 证明。

这样可以区分 representation choice 的失败与真正 state-sufficiency obstruction。

---

## 13. P018-T159 —— Precision state 的 dynamic-closure criterion

状态：`FOUNDATIONAL SYNTHESIS / NOT FROZEN`

对 surjective precision map

\[
\pi:X_e\twoheadrightarrow X_d,
\]

以及 fine deterministic operation `F_e`，coarse state `X_d` 对该 operation 精确自治，当且仅当

\[
\boxed{
\pi(x)=\pi(y)
\Longrightarrow
\pi(F_e x)=\pi(F_e y).
}
\]

即 precision kernel 必须是 operation congruence。

若成立，则存在唯一 descended operation `F_d`，coarse history 获得真正 monotone kernel / merger-time calculus。

若失败，则至少必须选择以下之一：

1. 保留 additional detail state；
2. 保留 carry 等 exact defect / extension datum；
3. 承认 coarse representation 只是 observation，而不是 autonomous dynamical state。

这给出一个更尖锐的 candidate foundational rule：

> **Finite precision 不只是 value partition。一个 precision state 对某 operation 是否动态完备，精确等价于该 partition 是否 operation-congruent。**

本文仍把它保留为 research synthesis，不直接写入 `FOUNDATIONS`。

---

## 14. 可执行与形式化压力测试

新增 executable checks：

- `src/enterprise_math/observation_kernel.py`
- `tests/test_observation_kernel.py`

测试：

1. fixed-time postprocessing 只会使 observation kernel 变粗；
2. `F(n)=2n`、`O(n)=n//2` 下 observed equality 会重新分开；
3. semiconjugate coarse evolution 具有 dynamic closure；
4. coarse equality 可以严格早于 true state coalescence；
5. closure 失败时 observed P011 collision count 可以随时间下降；
6. compatible observed kernel 沿时间单调；
7. 对所有测试的 `r>1`，quotient coordinate 都无法单独支持 exact binary addition。

`EnterpriseMath/State/Coalescence.lean` 中的 Lean 支持现在包括：

- `Function.Semiconj` 下 finite coalescence 同时间传递；
- injective semiconjugacy 下每个 finite coalescence level 严格不变；
- eventual-coalescence 的传递与 injective invariance。

---

## 15. 对底层逻辑的反哺

当前 deterministic precision/time hierarchy 不能被默认理解成两个天然 monotone axes。

正确结构首先是：

\[
\boxed{
\text{fine State}
\xrightarrow{\text{precision quotient}}
\text{coarse representation}
}
\]

然后必须单独问：

\[
\boxed{
\text{operation 是否能下降穿过 quotient？}
}
\]

若能，coarse representation 才成为 autonomous state space，并继承 monotone merger-time geometry。

若不能，observational equality 可以重新分开，missing detail / defect 继续具有动态意义。

这个框架同时解释了：

- P005 为什么坚持 typed precision states；
- P009 为什么警惕 erased-type fake dynamics；
- carry 为什么作为 exact detail-dependent operation data 保留下来；
- critical-square holonomy 为什么有意义；
- P010 irreversibility 为什么适用于 true deterministic state merging，而不是任意 coarse equality；
- P011 spectrum 沿 observed time axis 的单调性为什么需要 dynamic closure。

---

## 16. 下一步开放问题

### P018-Q116 —— 恢复 congruence 的最小 extension

给定 noncongruent precision quotient 与 operation，刻画使 operation 能精确下降所需的最小 finite detail object。carry 已解决一个 additive prototype；寻找一般 finite-state analogue。

### P018-Q117 —— Binary / multi-ary operation congruence

把 T152 从 unary dynamics 推广到 binary / multi-ary operations。研究 extension data 什么时候自然形成 cocycle / higher coherence，什么时候完全不需要这些语言。

### P018-Q118 —— Precision-time bifiltration invariants

对 dynamically closed precision chains，研究 two-parameter kernel filtration 的有限不变量，同时禁止把 continuous persistence machinery 直接当作 ontology。

### P018-Q119 —— Approximate closure 尚未定义

不要把 exact congruence failure 换成浮点 tolerance。如果未来确需 approximate closure，先用 explicit finite states、fibers 与 certificates 定义。

---

## 17. 当前结论

本阶段最强的新 foundational criterion 是精确的：

\[
\boxed{
\text{coarse state dynamically autonomous}
\iff
\text{其 precision kernel 是 operation congruence}.
}
\]

semiconjugacy 于是能够无延迟搬运 finite coalescence；injective chart change 精确保留 merger time；noninjective coarsening 可以让 histories 更早不可区分。

congruence 失败时，observed equality 不具不可逆性，未来可以重新分开。对 additive quotient，coarse coordinates 之所以不闭合，正因为 hidden residues 控制 carry；加入 detail + carry 后才能恢复 exact closed operation。

这把 precision、defect、time 与 irreversibility 接到同一有限结构里，不需要 hidden continuum，也不需要 error-bar ontology。

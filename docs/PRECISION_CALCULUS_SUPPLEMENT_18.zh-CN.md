# P018 —— 有限精度证明演算：补充 18

状态：`ACTIVE RESEARCH NOTE`  
范围：有限 future-observation refinement、canonical predictive closure、有限稳定化界、最小 dynamically autonomous quotient refinement，以及 P018-Q116 的 unary 解  
依赖：P005、P009、P010、P011、P018-T150—T159  
前人工作边界：有限确定性状态可区分性、behavioral equivalence、automata congruence 与 minimal quotient machine 都属于成熟数学/计算机科学。见 `docs/PRIOR_ART_P018_PREDICTIVE_CLOSURE.zh-CN.md`。[SRC-MOORE-1956-SEQUENTIAL] [SRC-NERODE-1958-AUTOMATON]

---

## 1. Supplement 17 留下的精确问题

Supplement 17 已证明：observation

\[
O:X\to Y
\]

对 deterministic endomap

\[
F:X\to X
\]

是否 dynamically autonomous，精确取决于 observation kernel 是否 forward compatible：

\[
O(x)=O(y)\Longrightarrow O(Fx)=O(Fy).
\]

如果失败，则 coarse state 对 exact future evolution 不够充分。

P018-Q116 问：究竟需要补回什么信息？

对**有限 unary deterministic system**，存在一个规范答案：只把 observation refinement 到“具有不同 future observable behavior 的 states 已被分开”为止。

---

## 2. P018-T160 —— 有限 horizon future-observation equivalence

状态：`PROVED / EXECUTABLE`

对每个 horizon `n>=0`，定义

\[
\boxed{
x\equiv_n y
\iff
O(F^{[i]}x)=O(F^{[i]}y)
\quad\text{对所有 }0\le i\le n.
}
\]

等价地，为每个 state 定义有限 observable signature：

\[
\boxed{
\Sigma_n(x)
=
\bigl(O(x),O(Fx),\ldots,O(F^{[n]}x)\bigr).
}
\]

则

\[
x\equiv_n y\iff \Sigma_n(x)=\Sigma_n(y).
\]

所以每个 `equiv_n` 都是普通有限 equivalence relation，可直接表示成显式 finite partition。

---

## 3. P018-T161 —— Predictive partitions 单调细化

状态：`PROVED / EXECUTABLE`

多看一个未来 observation，只可能把已有 block 再切开：

\[
\boxed{
\equiv_{n+1}\ \subseteq\ \equiv_n.
}
\]

更精确地：

\[
\boxed{
x\equiv_{n+1}y
\iff
O(x)=O(y)
\ \text{且}\
Fx\equiv_n Fy.
}
\]

第二个公式就是 recursive refinement law。

这一方向与 P010 的 time-kernel growth 相反：这里是在**向 representation 增加 predictive information**，所以 indistinguishability 变细。

---

## 4. P018-T162 —— Predictive refinement 一旦停止，以后永久停止

状态：`PROVED`

如果对某个 `n`

\[
\boxed{
\equiv_{n+1}=\equiv_n,
}
\]

那么

\[
\boxed{
\equiv_{n+k}=\equiv_n
\quad\forall k\ge0.
}
\]

### 证明

recursive law 给出

\[
\equiv_{n+1}
=
\ker(O)\cap F^{-1}(\equiv_n).
\]

若 `equiv_{n+1}=equiv_n`，说明 `equiv_n` 已是该 refinement operator 的 fixed point。再次施加同一个 operator 仍得到相同 relation，归纳即可。∎

在同一时刻，stable relation 也已经 forward compatible：

\[
x\equiv_n y\Longrightarrow Fx\equiv_n Fy.
\]

---

## 5. P018-T163 —— 有限 predictive closure 存在显式有限上界

状态：`PROVED / EXECUTABLE`

假设 `X` 有

\[
N=|X|
\]

个 states，而原 observation partition 有

\[
c_0
\]

个 nonempty blocks。

每一次 strict refinement 至少增加一个 block；任何 `X` 上的 partition 最多只有 `N` 个 blocks。

因此 first stable horizon `h_*` 满足

\[
\boxed{
h_*\le N-c_0.}
\]

完全不需要 infinite limit。

即便 `N-c_0` 次可能的 strict refinements 全部发生，最终也已经到 equality partition；而 equality 自动 forward compatible，所以最迟在该 horizon 必然稳定。

---

## 6. P018-T164 —— Stable relation 精确等于 all-future observational equivalence

状态：`PROVED`

记 first stable predictive partition 为 `equiv_*`。

则

\[
\boxed{
x\equiv_* y
\iff
O(F^{[n]}x)=O(F^{[n]}y)
\quad\forall n\in\mathbb N.
}
\]

### 证明

正向：stable relation forward compatible 且包含在 `ker(O)` 内。不断施加 `F` 后，每个 future pair 仍在 stable relation 中，因此 observation 永远相同。

反向：若所有 future observations 都相同，则尤其 stable horizon 的有限 signature 相同，所以 `x equiv_* y`。∎

因此 stable partition 不是对 infinite behavior 的近似。有限 state space 上，它在 T163 的有限界内就已经真正达到，并从此精确证书化所有后续 observation equality。

---

## 7. P018-T165 —— Predictive closure 是 observation kernel 内最大的 compatible equivalence

状态：`PROVED / EXECUTABLE`

设 `R` 是任意 equivalence relation，并满足

\[
R\subseteq\ker(O)
\]

以及

\[
xRy\Longrightarrow F(x)\,R\,F(y).
\]

则

\[
\boxed{
R\subseteq\equiv_*.
}
\]

### 证明

若 `xRy`，compatibility 推出对任意有限 `n`：

\[
F^{[n]}x\ R\ F^{[n]}y.
\]

又因为 `R` 包含于 `ker(O)`，这些 future states 的 observation 全部相同。由 T164 得 `x equiv_* y`。∎

所以 `equiv_*` 是同时满足以下条件的**最大 relation / 最粗 partition**：

1. refine 原 observation partition；
2. 对 `F` dynamically closed。

---

## 8. P018-T166 —— Predictive closure quotient 是最小 exact autonomous refinement

状态：`PROVED STRUCTURAL CONSEQUENCE / EXECUTABLE`

由于 `equiv_*` forward compatible，`F` 可以下降成 quotient deterministic map：

\[
F_*:X/\!\equiv_*\to X/\!\equiv_*.
\]

又因为 `equiv_*` 包含在 `ker(O)` 内，原 observation 也可以下降为

\[
O_*:X/\!\equiv_*\to Y.
\]

该 quotient 因而可以自治演化，并且精确重现原 observation sequence。

现在设 `R` 是另一个包含在 `ker(O)` 内且 dynamically compatible 的 equivalence。T165 给出

\[
R\subseteq\equiv_*.
\]

所以 `R` 的 quotient blocks/states 数量至少和 `equiv_*` quotient 一样多。

因此

\[
\boxed{
X/\!\equiv_*
}
\]

是在这类 quotient-state models 中，保持原 observations 的最粗 / state 数最少的 exact autonomous refinement。

这属于 classical finite-state minimization 邻域；Enterprise Math 的研究点是把它作为 exact precision-state sufficiency criterion。

---

## 9. P018-T167 —— 原 precision 已 dynamically closed 当且仅当 horizon zero 就稳定

状态：`PROVED / EXECUTABLE`

以下等价：

1. 原 observation kernel forward compatible；
2. `equiv_1 = equiv_0`；
3. first stable horizon 为 `0`；
4. predictive closure 没有增加任何 state distinction。

因此 Supplement 17 的 dynamic-closure test，正是 canonical predictive-refinement construction 的 zero-step 情形。

---

## 10. P018-C16 —— 有时 exact future closure 必须保留完整 fine state

状态：`COUNTEREXAMPLE / INFORMATION BOUNDARY`

取有限状态集

\[
X=\{0,1,2,3\}
\]

以及 deterministic transition

\[
F(0)=0,
\quad F(1)=0,
\quad F(2)=1,
\quad F(3)=2,
\]

observation 为

\[
O(0)=O(2)=O(3)=0,
\qquad O(1)=1.
\]

其 horizon partitions 依次为

\[
\{\{0,2,3\},\{1\}\},
\]

然后

\[
\{\{0,3\},\{1\},\{2\}\},
\]

最后变成 equality：

\[
\{\{0\},\{1\},\{2\},\{3\}\}.
\]

所以 `h_*=2=N-c_0`，达到 T163 的上界。

由 T165，如果 predictive closure 就是 equality，那么**不存在任何包含在原 observation kernel 内的 nontrivial equivalence quotient，可以同时 exact 且 dynamically autonomous。**

这类系统要精确预测未来 observation，确实必须保留完整 fine-state distinction。

---

## 11. P018-T168 —— Unary P018-Q116 得到 canonical finite answer

状态：`RESOLVED FOR FINITE UNARY DETERMINISTIC SYSTEMS`

对有限 deterministic endomap + observation，恢复 dynamic closure 所需的 minimal exact state refinement 不是任意设计：

\[
\boxed{
\text{按照 finite future-observation signatures 细化，直到 partition 稳定。}
}
\]

该构造：

- 完全有限；
- 具有显式停止界 `N-c0`；
- 产生 forward-compatible equivalence；
- 是原 observation kernel 内最大的 compatible equivalence；
- 给出保持原 observations 的最小 quotient-state autonomous refinement。

所以 P018-Q116 在 finite unary setting 下已经解决。

---

## 12. P018-C17 —— Unary closure theorem 不能偷换成 binary operation descent

状态：`DESIGN BOUNDARY`

Supplement 17 C15 已证明 quotient coordinates `Q_r(x)` 单独不能支持 exact binary addition。Supplement 18 不改变这一事实。

unary future-observation refinement 研究的是同一个 endomap 的反复作用：

\[
F:X\to X.
\]

而 binary operation

\[
\mu:X\times X\to X
\]

要求 equivalence 在**两个输入坐标**上都 compatible；更一般地，还必须对全部允许 operation contexts 保持。

所以这里的 finite predictive closure 不会被静默升级成 P018-Q117 的答案。multi-ary congruence 与 minimal extension data 仍是下一独立问题。

---

## 13. 回接 precision、time 与 irreversibility

Supplement 18 把 Supplement 17 的 hierarchy 进一步锐化为

\[
\boxed{
\text{raw observation}
\to
\text{finite predictive refinement}
\to
\text{dynamically closed quotient state}
\to
\text{monotone time kernel / merger geometry}.
}
\]

如果 raw precision 本来已经 closed，第一箭头就是 identity。

如果没有 closed，predictive refinement 只恢复 autonomous future observation 真正需要的 distinctions，并且在 quotient refinements 中不多保留额外区分。

closure 恢复后，P010/P011/P018 merger-time machinery 才真正作用在 quotient state 本身，而不是一个可能未来重新分叉的 observational readout 上。

---

## 14. 可执行压力测试

新增：

- `src/enterprise_math/predictive_closure.py`
- `tests/test_predictive_closure.py`

测试包括：

1. finite-horizon partitions 单调 refinement；
2. 一个达到 bound 的 four-state example；
3. 对 `N<=4` 的 deterministic endomaps + binary observations 穷举验证 `N-c0` bound；
4. stable partition 的 forward compatibility 与 observation refinement；
5. 已 compatible observation 在 horizon zero 稳定；
6. 小有限例中枚举全部 candidate partitions 验证 maximality；
7. quotient dynamics 与 quotient observation 的 exactness；
8. equality-closure 情形下不存在 nontrivial exact quotient。

---

## 15. 当前底层反哺

finite-precision state 问题现在可以被拆成两个 exact tests：

### Static precision

当前 observation 把哪些 fine states 识别为同一个 state？

### Dynamic sufficiency

在它应该 autonomously 支持的 operations 下，这些 identifications 中哪些能对**所有未来**继续成立？

对一个 finite deterministic endomap，predictive closure 在有限次 refinement 后给出 canonical answer。

这提示一个更强但仍未封板的 design rule：

> **有限精度状态不能只按“此刻可区分性”判断。对它需要自治支持的 operations，其 equivalence relation 必须是 congruence；如果不是，规范修复应是最粗 operation-compatible refinement，而不是任意 floating error margin。**

unary theorem 已经明确；multi-operation 版本仍开放，下一步应从 algebraic congruence 而不是 continuous approximation 进攻。

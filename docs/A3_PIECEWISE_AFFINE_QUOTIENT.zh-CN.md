# A3 Piecewise Affine Quotient —— Hidden Guard 擦除与非单调 Refinement

状态：`RESEARCH WIP / EXACT BINARY THRESHOLD CRITERION PROVED + EXECUTABLE REFERENCE`

## 1. 问题

A3 已经解决 integer linear/affine dynamics

\[
c'=Bc+u
\]

以及 exact linear observations 下的 minimum exact partition。

下一步考虑一个真正会读取 hidden relation 的二元 piecewise map：

\[
T(c)=
\begin{cases}
B_+c+u_+,&w^Tc+b\ge0,\\
B_-c+u_-,&w^Tc+b<0.
\end{cases}
\]

状态空间是完整整数格 `Z^k`。partition matrix `A:k->ell` 只观察 block sums `Ac`。

核心问题：

> guard identity 本身不可从 coarse state 读取时，是否仍可能安全删除它？

答案是：可以，但只有不同 branch 在 coarse quotient 上具有完全相同效果时。

## 2. Guard 是否 descend

令 partition kernel：

\[
K_A=\ker_{\mathbb Z}A.
\]

线性 guard score `w^Tc+b` 能从 `Ac` 精确读取，当且仅当：

\[
w^T\eta=0\quad\forall\eta\in K_A.
\]

对 coordinate partition，这等价于 `w` 在每个 coarse block 内常数。

若该条件失败，则存在 `eta in K_A` 使 `w^T eta != 0`。因为 `t eta` 对任意整数 `t` 仍在 kernel 内，同一 coarse fiber：

\[
c+K_A
\]

中的 guard score 沿 `t` 向正负两个方向无界。因此：

\[
\boxed{\text{每一个 coarse fiber 都同时包含 true/false 两种 branch state。}}
\]

这是完整整数格假设带来的关键强化。

## 3. A3-PW01 —— guard 可见时的 exact criterion

若 guard descend 到 coarse weights `w_bar`：

\[
w^T=w_{bar}^TA,
\]

则 branch choice 是 coarse-state function。

### 非常数 guard

若 `w_bar != 0`，在整个 `Z^ell` 上 true/false 两区都非空。此时 `T` 精确 descend 当且仅当两个 active affine branches 都各自 descend：

\[
AB_+=\bar B_+A,
\qquad
AB_-=\bar B_-A.
\]

任意 offsets 只需普通聚合：

\[
\bar u_+=Au_+,
\qquad
\bar u_-=Au_-.
\]

coarse map 保留同一个 threshold guard。

### 常数 guard

若 `w_bar=0`，guard 由常数 `b` 决定。只有实际 active branch 必须 descend；inactive branch 可以完全读取 hidden detail，因为它永远不会执行。

## 4. A3-PW02 —— Hidden-Guard Erasure Theorem

若 guard **不 descend**，则每个 coarse fiber 同时看到两种 branch。

因此 exact quotient 必须满足：

1. 两个 branches 各自对 kernel 不敏感，即都 descend；
2. 两个 descended affine maps 完全相同：

\[
\boxed{
\bar B_+=\bar B_-=ar B,
\qquad
Au_+=Au_-=\bar u.
}
\]

于是无论 hidden guard 选择哪一支：

\[
AT(c)=\bar B(Ac)+\bar u.
\]

反过来，若两个 coarse branch effects 不同，由于同一 coarse fiber 中两种 branch 都实际出现，必然产生同一 `Ac` 对应两个不同 coarse outputs，故 quotient 不 exact。

所以在完整 `Z^k` 上：

\[
\boxed{
\text{hidden guard exact}
\iff
\text{both branches descend and have identical coarse affine effect}.
}
\]

这给出 Supplement 26 留下的 “hidden branch different but coarse output same” 情形的必要充分条件。

## 5. Guard identity 不是必须保存的信息

该定理说明：

> future language 是否需要保存 branch identity，取决于 branch identity 是否改变 coarse output，而不是取决于 fine program 内部是否真的走了不同 branch。

所以：

\[
\boxed{
\text{different fine histories}
\not\Rightarrow
\text{different required coarse states}.
}
\]

这与 A3 的 future-safe collapse 原则完全一致：只保存未来程序真正能区分的 relation detail。

## 6. A3-PW03 —— Exactness 对 refinement 非单调

线性 dynamics 的 stable partition solver 可以通过单调 refinement 工作。

piecewise map 不再自动拥有这个性质。

存在 3-coordinate 例子：

- coarse partition `{{0,1,2}}`：guard hidden，但两个 branch 的总 coarse effect 都是 0，因此 exact；
- intermediate partition `{{0},{1,2}}`：guard 仍 hidden，但 branch effect 已被 coarse observation 区分，因此 **不 exact**；
- singleton partition：guard 本身可见，因此又 exact。

所以：

\[
\boxed{
P_0\text{ exact},\quad P_1\succ P_0\text{ not exact},\quad P_2\succ P_1\text{ exact}.
}

即：

\[
\boxed{\text{piecewise quotient exactness need not be monotone under refinement}.}
\]

因此不能把 Supplement 25 的 signature-splitting algorithm 原样推广成 general piecewise minimum solver。

## 7. 与 A2/P023 的关系

一般的 future-compatible quotient / behavioral equivalence 母定理仍归 A2/P023。

本文属于 A3 `SPECIALIZATION`：利用 coordinate partition kernel 与完整整数格，得到 linear-threshold affine program 的 closed-form exact criterion。

可复用的新信息包括：

- hidden guard 在每个 fiber 中两侧都出现；
- coarse-output equality 可以完全擦除 branch identity；
- exact partitions 在 piecewise 情形可能不构成 refinement-monotone family。

这些结果应通过 Research Relay #82 回流 A2/P023，不能在两边各维护一套一般理论。

## 8. 实现

新增：

- `src/enterprise_math/piecewise_relation_quotient.py`；
- `tests/test_piecewise_relation_quotient.py`。

测试覆盖：

- hidden guard + identical coarse branch effect；
- hidden guard + different coarse effect 失败；
- coarse-readable guard 允许不同 coarse branches；
- globally constant guard 只要求 active branch；
- exact → non-exact → exact 的 refinement 非单调反例。

## 9. 下一步

不直接暴力推广到任意非线性程序。下一步优先：

1. 分类 binary threshold piecewise map 的 exact partitions 是否存在多个 incomparable maximal/coarsest candidates；
2. 对小 `k` 建立 partition-lattice oracle，验证 general synthesis 的边界；
3. 找出比 exhaustive partition search 更强的 structural decomposition；
4. 将 output-equivalence 结论 Relay 到 P023/A2；
5. 对 A3 weighted relation queries 构造一个实际 hidden-feedback piecewise 示例，测 minimum relation precision 是否低于 branch-identity-sensitive solver。

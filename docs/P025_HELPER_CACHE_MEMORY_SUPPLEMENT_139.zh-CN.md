# P025 补充 139 —— Auxiliary helper state 在 endpoint 是 cache，在 runtime 是 memory

状态：`PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-helper-cache-stage139`

## 1. 合法饱和 section

沿用 Stage 138 的合法 raw initialization contract。设 `C_raw` 为 pure k-way conjunction law 下已经 closed 的 raw states；从每个 raw closed state 出发，所有 helpers 初始 absent，并让 sequential helper compiler 运行到 saturation。

定义

\[
H:C_{raw}\to X_{ext}^{sat}
\]

为这一合法饱和映射。

对每个 raw closed state `X`，

\[
\boxed{\pi(H(X))=X.}
\]

因此 `H` injective，从而

\[
\boxed{
|\operatorname{im}H|=|C_{raw}|.
}
\]

在合法 saturated endpoint state space 上，helper coordinates 相比 raw closed state **没有增加新的 semantic state distinctions**。它们只是确定性 derived cache coordinates。

这比“raw projection 正确”更强：合法饱和 internal state 实际上构成 raw semantic state 上的一个 section。

## 2. Raw projection 下的 transient collision

现在把 future language 从 saturated endpoint 改成 stepwise execution。

对四元 sequential compiler

\[
a_1a_2\Rightarrow e_2,
\qquad e_2a_3\Rightarrow e_3,
\qquad e_3a_4\Rightarrow z,
\]

从

\[
S=\{a_1,a_2,a_3\}
\]

出发，并让 `a_4` absent。raw projection 始终不变，但 internal trace 包含

\[
T_1=\{a_1,a_2,a_3,e_2\}
\]

与

\[
T_2=\{a_1,a_2,a_3,e_2,e_3\}.
\]

它们满足

\[
\boxed{\pi(T_1)=\pi(T_2)=S,}
\]

但 runtime futures 不同：

- 从 `T_1` 出发，下一轮会加入 `e_3`；
- `T_2` 因 `a_4` absent 已经稳定。

所以 raw projection 对 stepwise internal language 并不是 future-safe quotient。

## 3. Cache/memory phase boundary

同一个 helper coordinate 会随着 declared future 改变身份。

### Saturated endpoint future

`H(X)` 被 raw closed `X` 函数性确定。helper state 是 cache，可以在不损失 endpoint semantics 的前提下 quotient 掉。

### Stepwise/runtime future

transient helper progress 会改变下一步 enabled update、剩余 derivation depth 与 internal trace。此时 helper state 是真正 runtime memory，不能只靠 raw projection collapse。

因此

\[
\boxed{
\text{cache 还是 memory 是 future-language-relative，而不是 coordinate-intrinsic。}
}
\]

## 4. Precision 后果

auxiliary-state dimension 本身并不等于它贡献的 **semantic precision**。必须继续问这些 coordinates 是：

- 在 declared endpoint 上由 visible state 确定的函数；
- 还是 declared runtime future 需要的独立 progress/history coordinates。

这里给出一个 exact finite 例子：同一 coordinate 对 endpoint-state refinement 的贡献为零，但对 runtime-state refinement 的贡献非零。

## 5. 前人工作边界

derived caches、sufficient state、hidden execution progress 与 refinement maps 都是标准计算机科学/控制思想。P025 不主张 generic novelty。项目侧结果是把 Stage138 legality 与 state-precision accounting 接起来的 exact future-relative phase boundary。

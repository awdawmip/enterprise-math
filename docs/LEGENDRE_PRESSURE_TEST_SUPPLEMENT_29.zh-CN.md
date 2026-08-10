# Legendre 压力测试 — 补充 29

状态：`PROVED RESEARCH NOTE`  
范围：真实 factor-to-root split 的 branch-local Bonferroni proof precision  
依赖：P017 L069 exact Möbius rough counts 与 finite inclusion–exclusion  
纪律：Bonferroni inequalities 属于经典数学。本补充不替代 exact Möbius semantics；它度量的是多少 truncated factor-overlap information 足以证明需要的 positivity。

## 1. Exact occupancy 不一定需要完整 inclusion–exclusion

L069 把每个 root-branch occupancy 写成 exact p-rough count：

\[
R_p[a,b]
=
N-S_1+S_2-S_3+\cdots,
\]

其中

\[
N=b-a+1,
\]

而 `S_j` 是：对小于 `p` 的 primes 的每个 `j` 元 subset，统计同时被该 subset 全部整除的 states，再求和。

要证明

\[
R_p[a,b]>0,
\]

并不总要算完整 alternating sum。

## 2. Odd Bonferroni lower bounds

对 odd depth

\[
d=2m-1,
\]

定义

\[
\boxed{
B_d
=N-S_1+S_2-\cdots-S_d.
}
\]

对小素数 divisibility events 的 union 使用标准 Bonferroni inequalities，可得

\[
\boxed{
B_d\le R_p[a,b]
\qquad(d\text{ odd}).
}
\]

因此

\[
\boxed{
B_d>0
\Longrightarrow
R_p[a,b]>0.
}
\]

这就是一个严格 early-stop certificate。

## 3. P017-L070-A —— Branch-local proof depth

状态：`PROVED`。

对一个实际 occupied 的 p-rough interval `I=[a,b]`，定义

\[
\boxed{
h_B(I,p)
=
\min\{d\ge1:d\text{ odd 且 }B_d(I,p)>0\},
}
\]

若存在这样的 odd truncation。

对 `p=2`，没有更小 primes，所以 occupancy 在 depth zero 就已经 exact：

\[
\boxed{h_B(I,2)=0.}
\]

若有限 small-prime family 用完以前没有任何 odd truncation 变成正值，则记

\[
h_B(I,p)=\mathrm{FULL},
\]

表示应该回退到 exact Möbius count。

关键是：

\[
\boxed{h_B=\mathrm{FULL}}
\]

**不**表示 interval 为空，只表示当前 lower-bound proof language 没有提前证明 positivity。

## 4. P017-L070-B —— Split-shell proof precision

令

\[
W_p^-,W_p^+
\]

为某条实际 split shell 的两个 L068 subwindows。

定义

\[
\boxed{
h_p^-(k)=h_B(W_p^-,p),
\qquad
h_p^+(k)=h_B(W_p^+,p).
}
\]

若两者都有 finite odd depth，则整条 shell split 在

\[
\boxed{
h_p^{\rm split}(k)=\max(h_p^-(k),h_p^+(k))}
\]

处得到证明。

必须取 maximum，因为 theorem 同时要求两个 root branches 都 positivity。

若任一侧为 `FULL`，shallow Bonferroni language 自身不足以闭合 split proof，必须使用 exact inclusion–exclusion 或其他 certificate。

## 5. P017-L070-C —— Proof precision 会真实跳跃

状态：`PROVED BY EXACT FINITE CERTIFICATES`。

以下真实 split shells 需要不同 minimum Bonferroni depths。

### k=8, p=3

两个 branches 在 first order 就都被证明：

\[
\boxed{
(h_p^-,h_p^+)=(1,1),
\qquad
h_p^{\rm split}=1.
}
\]

### k=18, p=7

两边的 first-order inclusion–exclusion 都不够，而 depth three 成功：

\[
\boxed{
(h_p^-,h_p^+)=(3,3),
\qquad
h_p^{\rm split}=3.
}
\]

### k=104, p=13

两个 branches 的 proof burden 已经不同：

\[
\boxed{
(h_p^-,h_p^+)=(5,3),
\qquad
h_p^{\rm split}=5.
}
\]

所以 proof precision 既不对 `p` 恒定，也不必在同一个 root boundary 两侧对称。

## 6. P017-L070-D —— Exact semantic state 与 proof state 必须分开

represented shell split bit 只是

\[
\mathbf1[R_p^->0]\mathbf1[R_p^+>0].
\]

它的 truth value 与最终用什么 proof method 建立 positivity 无关。

Bonferroni depth 记录的是另一个对象：

\[
\boxed{
\text{多少 small-prime intersection information 足以证明这个 truth}.
}
\]

因此

\[
\boxed{
\text{semantic precision}
\neq
\text{proof precision}.
}
\]

两个 branches 可以表示完全相同的 Boolean truth，却需要不同 proof horizons。

## 7. 与 P018/P023 task precision 的关系

exact branch truth 是 observable。截断 inclusion–exclusion depth 则是一套关于局部 divisibility configurations 的 proof-state refinement hierarchy。

随着 depth 增长，proof state 越来越细。一旦某个 positive lower bound 出现，该 occupancy certificate 在更细的 exact refinement 下永久保持。

这正是 P018 adaptive precision 已经出现的结构：

\[
\boxed{
\text{refine observations until a predicate certificate becomes permanent}.
}
\]

L070 给出一个直接连接 L067 repair spectrum 的 sieve-theoretic 实例。

## 8. 潜在算法用途

证明或计算 `S(k)` 时，可以逐 branch 执行：

1. 用 L068 overshoot test 删除 raw nonsplits；
2. 两侧先尝试低 odd Bonferroni depth；
3. 一旦两个 lower bounds 都为正立即停止；
4. 只有困难 branches 才升级到更深 inclusion–exclusion、exact Möbius、rough recursion、CRT 或 Jacobsthal 工具。

这是 exact adaptive proof precision，不是 approximate counting。

## 9. 可执行规范

- `src/enterprise_math/rough_bonferroni.py`
- `src/enterprise_math/p017_root_split_proof_precision.py`
- `tests/test_p017_root_split_proof_precision.py`

测试验证每个 odd truncation 都不超过 exact rough count，并固定 `1 -> 3 -> 5` 的 proof-depth 跃迁。

## 10. 基础反哺

新的链条是

\[
\boxed{
\text{exact state truth}
\to
\text{finite proof-language hierarchy}
\to
\text{minimum certificate depth}.
}
\]

这提示 Enterprise Math 应该在 theorem discovery / finite verification cost 真正相关时，把 **proof precision** 保持为区别于 represented state precision 的一等对象。

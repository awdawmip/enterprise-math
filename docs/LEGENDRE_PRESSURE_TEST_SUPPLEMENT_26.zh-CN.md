# Legendre 压力测试 — 补充 26

状态：`PROVED RESEARCH NOTE`  
范围：least-prime precision 被 cofactor-root precision 细化后的完整相对 repair spectrum  
依赖：P017 L064、P023-S11 relative repair spectrum、P018 exact root threshold  
纪律：这是有限 square-basin representation theorem，不证明 Legendre 猜想。

## 1. 从 one-bit 上界推进到完整 repair spectrum

L064 已证明，每个 least-prime shell 最多只会碰到两个 cofactor-root classes。

S11 又说明，一次 finite precision refinement 不能只由最坏 repair alphabet 描述；它还有完整 relative repair spectrum。

在当前 P017 特化中，L064 的 binary 上界会把整个 spectrum 强制截断在二阶。

## 2. Split-shell count

令

\[
N_P(k)=|X/P|
\]

表示当前 square basin 中非空 realized least-prime shells 的数量。

对每个这样的 prime `p`，令

\[
r_p\in\{1,2\}
\]

为该 shell 内实际实现的 cofactor-root values 数量。

定义

\[
\boxed{
S(k)=\#\{p:r_p=2\}.
}
\]

因此 `S(k)` 精确统计：哪些 least-prime shells 真正需要 nontrivial root-repair bit。

## 3. L067-A —— 精确 joint class count

状态：`PROVED`。

joint `(factor,root)` precision 的 classes 数为

\[
\sum_p r_p.
\]

由于每个 `r_p` 只能是 1 或 2，得到

\[
\boxed{
|X/(P\cap R)|
=N_P(k)+S(k).
}
\]

每个 unsplit shell 贡献一个 joint class；每个 split shell 额外多贡献一个 class。

这是 L064 binary bound 的精确全局 class-count refinement。

## 4. L067-B —— 完整 relative repair spectrum 是二次的

状态：`PROVED`。

对 canonical quotient projection

\[
X/(P\cap R)
\longrightarrow
X/P
\]

应用 S11。

它的 fiber sizes 正好就是 `r_p`。

因此

\[
\mathcal R_1
=
\sum_p r_p
=N_P+S,
\]

而

\[
\mathcal R_2
=
\sum_p\binom{r_p}{2}
=S.
\]

对所有更高阶都有

\[
\boxed{
\mathcal R_j=0
\qquad(j\ge3).
}
\]

所以

\[
\boxed{
\mathcal R(P\leftarrow P\cap R)
=(N_P+S,\ S).
}
\]

整个 higher-order repair structure 只比 factor-shell 数量多需要一个整数 `S(k)`。

## 5. L067-C —— Repair generating polynomial

状态：`PROVED`。

S11 generating polynomial 为

\[
K(t)
=
\sum_p\big((1+t)^{r_p}-1\big).
\]

其中有 `N_P-S` 个 unsplit shells 和 `S` 个 split shells，因此

\[
\begin{aligned}
K(t)
&=(N_P-S)t+S(2t+t^2)\\
&=(N_P+S)t+St^2.
\end{aligned}
\]

所以

\[
\boxed{
K_{P\leftarrow P\cap R}(t)
=(N_P(k)+S(k))t+S(k)t^2.
}
\]

这里 `t^2` 的系数不再只是抽象 collision statistic；它精确等于需要第二个 root state 的 factor shells 数量。

## 6. L067-D —— Split shell 的精确 threshold / p-rough occupancy 判据

状态：`PROVED`。

固定 prime `p`，写

\[
j_p
=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right).
\]

P018 upper-root threshold 为

\[
\boxed{
q=(j_p+1)^2.
}
\]

设 open exact cofactor window 为

\[
W_p(k)=[A_p,B_p].
\]

lower root `j_p` 被真实 least-prime shell 实现，当且仅当存在一个 `p`-rough integer

\[
q\in[A_p,\min(B_p,(j_p+1)^2-1)].
\]

upper root `j_p+1` 被真实实现，当且仅当存在一个 `p`-rough integer

\[
q\in[\max(A_p,(j_p+1)^2),B_p].
\]

因此

\[
\boxed{r_p=2}
\]

当且仅当这两个相邻 threshold subwindows **都**含有 `p`-rough quotient。

这是 P018 raw two-basin split condition 经过 realizability filter 后的精确版本。

## 7. L067-E —— Uniform binary product slots 与 unused-code count

假设 `S(k)>0`，因此全局 factor-to-root repair alphabet 必须包含两个 symbols。

统一 factor-first product code 会分配

\[
2N_P
\]

个形式 `(factor,bit)` slots。

真正 joint precision 只使用

\[
N_P+S
\]

个。

所以 unused slots 精确为

\[
\boxed{
2N_P-(N_P+S)
=N_P-S.
}
\]

也就是说：**没有被使用的统一 binary code slots 数量，恰好就是 unsplit least-prime shells 数。**

这给 S18 的 unrealized-support defect 一个逐 shell 的纯数论解释。

若 `S(k)=0`，task-minimal alphabet 只有一个 symbol，自然不存在 unused slots。

## 8. 例子

### k=11

\[
N_P=5,
\qquad
S=1,
\qquad
|X/(P\cap R)|=6.
\]

因此

\[
\boxed{\mathcal R=(6,1).}
\]

### k=18

split shells 为

\[
\boxed{p=2,7}.
\]

所以

\[
N_P=5,
\qquad
S=2,
\qquad
|X/(P\cap R)|=7,
\]

并且

\[
\boxed{\mathcal R=(7,2).}
\]

### k=1737

真实 basin 中

\[
N_P=157,
\qquad
S=7,
\qquad
|X/(P\cap R)|=164.
\]

统一 binary factor-first product 有 `314` 个形式 slots，其中

\[
\boxed{150=157-7}
\]

个从未实现，因为对应 factor shells 根本不需要 upper repair digit。

## 9. P011 第二 collision coordinate 的新解释

P011 的第二 spectrum coordinate 通常统计一个 coarse map 合并了多少 pairs of fine classes。

这里 canonical precision-forgetting projection 的 fibers 只能是 1 或 2，因此

\[
\boxed{
J_2(\pi_{P\cap R,P})=S(k).
}
\]

所以一个 P011 irreversibility-spectrum coordinate 直接变成 P017 shell geometry 的精确算术 observable。

这是一条 theorem-level bridge，而不是符号类比。

## 10. 对 state design 的影响

给每条 factor shell 都机械携带一个 uniform one-bit field，虽然充分，但会浪费大量状态。

更精确的 represented state 应该是：

- unsplit shells 不携带额外 root repair；
- 只有 `S(k)` 条 split shells 携带一个 binary branch。

若工程上必须使用固定 rectangular storage format，可以按 S18 先保留 uniform product，再对 realized support 做 rank compression。但 theorem 层面应优先保留 local split profile。

## 11. 可执行规范

- `src/enterprise_math/p017_factor_root_spectrum.py`
- `tests/test_p017_factor_root_spectrum.py`

可执行层把 p-rough threshold criterion 与 direct realized root sets 逐 shell 对照，固定上面的三个例子，验证 quadratic spectrum truncation，并检查 unused uniform binary codes 恰好等于 unsplit shells。

## 12. 工具反哺

抽象闭环现在成为

\[
\boxed{
\text{P011 collision spectrum}
\to
\text{P023 relative repair spectrum}
\to
\text{P017 exact split-shell observable}.
}
\]

这正是我们希望的研究模式：general tool 返回数论以后，不只是换一个术语，而是生成新的精确整数统计量。

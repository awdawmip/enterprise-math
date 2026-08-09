# Causal Uniform Residual Generator —— 任意维 Future Quotient、Bulk/Structure 分离与最小生成状态

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT ABSTRACT THEOREM + FINITE EXECUTABLE PRESSURE TESTS`

归属：一般 future-equivalence 母理论与经典 automata 对应应由 A2/P023 消费；本文件是 LEGO repeated-slot / arbitrary-dimension specialization。

## 1. 为什么固定 horizon 不够

固定总长度 `N` 时，总可以把足够多 prefix history 塞进中间 state，因此“某个 N 能被二体递归生成”并不能说明存在真正 dimension-uniform 的低维 law。

任意维问题必须比较**所有未来 suffix 长度**。

设 finite alphabet `A` 表示每次新加入一个 LEGO slot 的局部 symbol，给任意 finite word：

\[
O:A^*\to V
\]

一个 declared discrete observation。

## 2. UR-01 —— horizon-independent future residual equivalence

对两个 prefixes `p,q` 定义：

\[
\boxed{
p\equiv_\infty q
\iff
O(ps)=O(qs)
\quad\forall s\in A^*.
}
\]

也就是：无论未来再加入多少 slots，任何允许 suffix 都不能区分 `p,q`。

这是 repeated-LEGO system 的真正 future-equivalence；不是固定 `N` 下的临时压缩。

## 3. UR-02 —— append operation 自动下降

若：

\[
p\equiv_\infty q,
\]

则对任意新 symbol `a`：

\[
\boxed{
pa\equiv_\infty qa.
}
\]

因为对任意 suffix `s`：

\[
O((pa)s)=O(p(as))=O(q(as))=O((qa)s).
\]

因此 continuation class 上自动存在统一 update：

\[
\boxed{
[p]\xrightarrow{a}[pa].
}
\]

不是先定义 automaton state，再要求它工作；而是 future equivalence 自己生成 state transition。

## 4. UR-03 —— observation 自动下降

取 empty suffix：

\[
p\equiv_\infty q\Rightarrow O(p)=O(q).
\]

所以：

\[
\boxed{
\bar O([p])=O(p)
}
\]

well-defined。

从初始 class `[empty]` 出发按 input word `w` 逐 symbol update，最终 state 正是 `[w]`，读出的 observation 精确等于 `O(w)`。

## 5. UR-04 —— 最粗 exact dimension-uniform state

设另一个 deterministic state summary：

\[
h:A^*\to S
\]

满足：

1. `h(pa)` 只由 `h(p)` 与新 symbol `a` 决定；
2. `O(p)` 可由 `h(p)` 精确读取。

若：

\[
h(p)=h(q),
\]

则对任意 suffix `s`，deterministic update 给：

\[
h(ps)=h(qs),
\]

再由 observation readability：

\[
O(ps)=O(qs).
\]

故：

\[
\boxed{
h(p)=h(q)\Rightarrow p\equiv_\infty q.}
\]

因此任何 exact uniform generator 都必须细化 `A*/equiv_infty`。

所以：

\[
\boxed{
A^*/\equiv_\infty
\text{ 是该任意维任务的最粗 deterministic causal state}.}
\]

若 quotient 有有限多个 classes，则得到真正 finite-type dimension-uniform law；任何 exact finite-state realization 至少需要同样多 states。

在 Boolean observation 特例中，这与经典 Myhill–Nerode residual-language construction 同形。传统 DFA / right-congruence 是这里的 `SHADOW_FORMULA / COORDINATE_TOOL`，不作为进取数论 primitive 或原创主张。

## 6. Class count 是 representation-independent capacity

若在某个有限 horizon/depth 下最少需要 `C` 个 continuation classes，则任意 exact encoding 至少必须提供 `C` 个不同 code states。

即使只使用一个非负整数 register，最紧凑 injective code 也需要：

\[
\boxed{
\max code\ge C-1.
}
\]

所以：

```text
s <- 2*s + x
```

虽然只写一个整数变量和一行更新公式，仍可以携带指数级历史容量。不能用变量个数或代码长度冒充 causal simplicity。

## 7. Raw residual complexity 与 structural complexity 必须分开

整数 observation 经常包含已经确定的 bulk value。

若：

\[
O:A^*\to\mathbb Z,
\]

定义 normalized residual：

\[
\boxed{
\widehat\Sigma_p(s)=O(ps)-O(p).
}
\]

它只问：

> 在扣除 prefix 已经确定的当前整数值以后，未来 suffix 还会怎样响应？

定义 structural equivalence：

\[
\boxed{
p\approx q
\iff
\widehat\Sigma_p(s)=\widehat\Sigma_q(s)
\quad\forall s.}
\]

于是 runtime state 可以自然分成：

\[
\boxed{
(\text{current bulk value},\ \text{structural continuation type}).
}
\]

这与项目长期坚持的 `value != relation structure` 完全一致。

## 8. 三个关键例子

### 8.1 Binary sum

\[
O(w)=\sum_iw_i.
\]

虽然 raw prefix future classes 随 prefix sum 增长，但：

\[
\widehat\Sigma_p(s)=\sum_i s_i
\]

与 `p` 完全无关。

所以：

- bulk：当前 integer sum；
- structural continuation type：只有 1 个。

这是真正简单的 integer accumulator。

### 8.2 Finite-range local grade

若 total grade 是连续 `q`-slot windows 的整数和，已积累 grade 是 bulk；future increment 只依赖 prefix 最后至多 `q-1` 个 symbols。

因此 raw suffix memory 提供：

\[
|A|^{q-1}
\]

steady-state structural type 上界；future-equivalence 还可能进一步压缩。

所以 `q`-layer local interaction 不要求 `q`-ary composition primitive。

### 8.3 Full history integer code

令 binary word 编码：

\[
O(wx)=2O(w)+x.
\]

未来 suffix 长度 `m` 会把旧 prefix code 乘 `2^m`。因此即使扣除当前 `O(p)`，normalized residual 仍依赖完整 prefix code。

不同 histories 不会因为“只用一个整数变量”而变成同一个 structural continuation type。

## 9. Fixed-horizon continuation complexity 与 P011 collapse spectrum

对 horizon `N`、depth `d`，prefix-to-future-class map：

\[
q_{N,d}:A^d\to T_{N,d}
\]

本身是一场 finite causal collapse。

因此：

\[
\boxed{
|A|^d-|T_{N,d}|
}
\]

是当前任务可以安全遗忘的第一阶历史 distinction 数。

更完整地：

\[
\boxed{
J_k(q_{N,d})
=
\sum_{\tau\in T_{N,d}}
\binom{|q_{N,d}^{-1}(\tau)|}{k}.
}
\]

它精确统计有多少 `k` 元不同过去已经对所有剩余未来完全等价。

所以 P011 collision spectrum 同时成为：

- history merge spectrum；
- measurement collapse spectrum；
- coupling forgetting spectrum；
- **future-safe memory forgetting spectrum**。

## 10. Complexity examples

### parity

binary parity task 对任意 horizon：

\[
C_N\le2.
\]

这是 global-looking 但真正 bounded causal-memory 的规则。

### copy constraint

对长度 `2n` binary word 要求后半等于前半。到 midpoint：

\[
\boxed{
C_{2n,n}=2^n.
}
\]

每个前半 prefix 只接受唯一不同 suffix，所以它们的 future signatures 全部不同。

这是真正 exponential continuation-state capacity；一个整数 register 也只能通过指数增大的 code range 把它隐藏起来。

### full word identity

终态直接读取完整 word 时没有可合法遗忘 history；P011 higher collision coordinates 均为零。

## 11. 当前因果复杂度报告格式

以后不再只报“几体 interaction”或“用了几个变量”。至少应区分：

\[
\boxed{
(\text{exposed coupling order},
\ \text{continuation class growth},
\ \text{structural normalized class growth},
\ \text{join coherence defect}).
}
\]

这比 traditional degree / tensor order / state-variable count 更接近任意维 LEGO law 的真实复杂度。

## 12. 前人工作纪律

Boolean language 情形与经典 Myhill–Nerode theorem / residual languages 直接相邻。Mathlib 已有 `Mathlib.Computability.MyhillNerode`，通过 language left quotients 构造最小 residual-state DFA，并证明 regularity 与有限 quotient 的对应。

进取数论不主张该一般 automata theorem 是原创。这里的项目工作是把它放回更大的 causal LEGO composition 路线，并与 graded fiber、P011 collapse spectrum、bulk/structure separation 和 dimension-uniformity 联通。

## 13. 可执行资产

- `causal_prefix_complexity.py`
- `causal_state_capacity.py`
- `causal_normalized_residual.py`
- corresponding tests

## 14. 下一步

1. 把 normalized residual 从 `Z`-valued translation observations 推到一般明确给定的 output-composition law；
2. 给 finite-range close-packing grade 编译最小 normalized continuation state，而不是只保存 raw `q-1` suffix；
3. 比较 FCC/HCP/polytype grade law 的 continuation complexity，而不是只比较周期标签；
4. 在 clean integration 后用 mathlib Myhill–Nerode 形式化 Boolean special case，不重造 automata 基础库。

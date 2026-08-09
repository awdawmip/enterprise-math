# Causal Dimension–Collapse Core —— Hidden Motion、增长阶与 P008 Basin 的统一桥

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT INTEGER BRIDGE THEOREMS + EXECUTABLE REFERENCES`

归属：A3/A5/P008/P012/P019 跨线桥。一般 order-adjoint 母理论仍归 P008；几何模型仍归 P012/P022。本文不把“多项式次数=物理维度”作为定义，只给出何时多个独立整数维数见证被同一 causal structure 强迫一致。

## 1. 自由 fixed-total LEGO fiber

对 `m` 个 integer slots：

\[
T(x)=\sum_{i=1}^{m}x_i.
\]

固定 coarse total `c` 的 nonnegative fine fiber：

\[
\mathcal F_m(c)=\{x\in\mathbb N^m:T(x)=c\}.
\]

任意两个 same-total fine states 的差落在：

\[
\boxed{
K_m=\{\eta\in\mathbb Z^m:\sum_i\eta_i=0\}.
}
\]

显式整数基：

\[
e_1-e_m,\ldots,e_{m-1}-e_m.
\]

所以：

\[
\boxed{\operatorname{rank}K_m=m-1.}
\]

这个 rank 是 coarse total 隐藏掉的 fine redistribution freedom 数。

## 2. DC-01 —— hidden-motion rank = fiber-growth difference degree

fiber multiplicity：

\[
H_m(c)=|\mathcal F_m(c)|=\binom{c+m-1}{m-1}.
\]

但 closed form 不是本体；LEGO composition 已经给出递推。

exact finite difference：

\[
\boxed{
\Delta H_m(c)=H_{m-1}(c+1).
}
\]

反复：

\[
\boxed{
\Delta^r H_m(c)=H_{m-r}(c+r).
}
\]

最终：

\[
\Delta^{m-1}H_m=1,
\qquad
\Delta^mH_m=0.
\]

因此：

\[
\boxed{
\operatorname{rank}K_m
=
\deg_\Delta H_m
=m-1.
}
\]

这里不是借 Ehrhart 定义 dimension，而是同一个 coarse-total fiber 一边产生 hidden motion lattice，一边产生 finite fiber growth；二者直接给同一个整数。

## 3. DC-02 —— block decomposition 的维数守恒

把 `m=sum_i m_i` 个 fine slots 分成 `k` 个 coarse blocks。

若每个 block total 都保留，则各块内部 hidden rank：

\[
\boxed{
\sum_i(m_i-1)=m-k.
}
\]

若再只保留 grand total，block totals 自身允许 zero-sum redistribution：

\[
\{\delta\in\mathbb Z^k:\sum_i\delta_i=0\},
\]

新增 rank：

\[
\boxed{k-1.}
\]

所以：

\[
\boxed{
(m-k)+(k-1)=m-1.
}
\]

解释：

> 内部 relation freedom + cross-block redistribution freedom = grand-total fiber 的全部 hidden freedom。

二块合并时，只保留总量会精确新增一个 cross-block relation freedom。

这条 rank decomposition 与 set-level LEGO fiber decomposition 同源：

\[
\boxed{
\mathcal F_m(c)
\cong
\bigsqcup_{c_1+\cdots+c_k=c}
\prod_i\mathcal F_{m_i}(c_i).
}
\]

外层 block-total allocation set 本身就是：

\[
\mathcal F_k(c),
\]

携带 `k-1` 个 coarse redistribution freedoms。

## 4. DC-03 —— free A_p regime 的三重维数一致

`A_p` zero-sum integer representation 使用：

\[
p+1
\]

个 slots。

因此 hidden motion rank：

\[
\boxed{p.}
\]

同一个 `p+1`-slot free allocation multiplicity：

\[
H_{p+1}(c)
\]

finite-difference degree也是：

\[
\boxed{p.}
\]

现有 `A_p` primitive-root graph ball count：

\[
V_p(r)
\]

由项目 closed integer formula 可直接验证并证明是 degree `p` 的整数值多项式。

所以 free `A_p` working regime 中：

\[
\boxed{
\text{hidden relation rank}
=
\text{fiber-growth degree}
=
\text{graph-ball growth degree}
=p.
}
\]

这叫 **dimension agreement certificate**；不把三者预先定义成同一个对象。

## 5. Task continuation dimension 可以不同

future task 的 minimal continuation-state capacity：

\[
C(d)
\]

是另一种 causal observable。

若它是 degree `q` 的 integer-valued polynomial，则可定义 task/state-growth order `q`。

但它不自动等于 substrate relation dimension。

### parity

\[
C(d)=2,
\]

所以 task growth order = 0，即使底层 relation substrate 可更高维。

### binary sum

\[
C(d)=d+1,
\]

order = 1。

### copy/history task

\[
C(d)=2^d,
\]

不存在固定 finite polynomial difference order。

因此：

\[
\boxed{
\text{physical/geometric/relation dimension}
\neq
\text{task continuation complexity by definition}.
}
\]

两者只有在具体 bridge theorem 下才可等同。

## 6. DC-04 —— independent task growth degree 可加

若两个 independent causal tasks 的 exact continuation capacities 分别是非零 leading coefficient 的 integer polynomials：

\[
C_A(d),\quad C_B(d),
\]

独立 signature product 给：

\[
\boxed{C_{A\boxtimes B}(d)=C_A(d)C_B(d).}
\]

所以 ordinary polynomial degree 给：

\[
\boxed{
\deg_\Delta C_{A\boxtimes B}
=
\deg_\Delta C_A+\deg_\Delta C_B.
}
\]

这里 degree additivity 是 independent future-state multiplication 的 shadow，不是 dimension 的先验 Cartesian axiom。

## 7. DC-05 —— causally generated complete growth 接入 P008

让 causal/LEGO construction 生成严格递增 integer complete-growth law：

\[
V(k).
\]

P008 order-adjoint 直接给：

\[
\boxed{
R_V(n)=\max\{k:V(k)\le n\},
}
\]

\[
\boxed{
C_V(n)=V(R_V(n)).
}
\]

因此 causal composition 不形成第二套理论，而回到项目原始主轴：

\[
\boxed{
\text{one-slot causal law}
\to
\text{complete integer growth }V
\to
\text{P008 root}
\to
\text{idempotent collapse}.
}
\]

## 8. DC-06 —— P008 basin width = first dimension-lowering difference

第 `k` 个 root basin：

\[
V(k)\le n<V(k+1).
\]

其精确 integer width：

\[
\boxed{|B_k|=V(k+1)-V(k)=\Delta V(k).}
\]

若 `V` 的 exact growth degree 是 `p`，则 basin-width growth degree 是：

\[
\boxed{p-1.}
\]

所以 P008 collapse basin 本身携带一次 exact dimension-lowering operation。

### free LEGO special strengthening

取：

\[
V(c)=H_m(c).
\]

则不只是“次数少一”：

\[
\boxed{
|B_c|
=H_m(c+1)-H_m(c)
=H_{m-1}(c+1).
}
\]

整个 basin width **严格就是少一个 hidden slot freedom 的完整 LEGO fiber cardinality**。

### A_p graph-ball special case

取：

\[
V(r)=|B_r^{A_p}|.
\]

则：

\[
\boxed{
V(r)-V(r-1)=|S_r^{A_p}|.
}
\]

球的 P008 basin boundary 就是 exact graph shell，growth degree从 `p` 降到 `p-1`。

## 9. 重要负边界：degree lowering 不等于 family lowering

自由 allocation family 有特殊 closure：

\[
\Delta H_m=\text{shifted }H_{m-1}.
\]

但一般几何 complete-growth family 只保证**次数**降一，不保证差分后的 shell 等于同半径的低一维 ball。

例如 `A_p` shell 与 `A_(p-1)` ball 一般不是同一个对象，也不只是固定 scalar 倍数。

因此不得把：

\[
\deg_\Delta V=p
\]

机械解释成“每次边界都 literally 变成低一维空间”。

exact same-family lowering 需要额外 combinatorial bijection / recurrence theorem。

## 10. DC-07 —— plateau 先做 causal level quotient，再做 root

若 complete observable 只 monotone：

\[
V(k)=V(k+1)
\]

出现 plateau，则它已经把多个 raw complete levels 映成同一个 observation。

正确做法：

1. 若 future language 还能区分 plateau members：补 future/continuation state，说明 `V` 不充分；
2. 若 future 也无法区分：先把 plateau levels quotient 成一个 causal level。

monotone plateau quotient 的 induced capacity sequence严格递增，才能作为 P008 order embedding。

所以：

\[
\boxed{
\text{causally distinguishable complete levels}
\to
\text{P008 root/collapse}.
}
\]

root 不能偷偷恢复 observable 已经擦掉的 level identity。

### 最小例子

free one-slot configuration count：

\[
H_1(c)=1
\quad\forall c.
\]

它完全不能恢复不同 value totals `c`。

这不是数值 root 算法太弱，而是再次证明：

\[
\boxed{\text{value}\neq\text{structure count}.}
\]

## 11. 与“反弹层 / 厚度”的关系

P008 basin width：

\[
\Delta V(k)
\]

现在可被解释成“从完整 level `k` 到下一个完整 level `k+1` 之间，所有会坍缩回同一个 complete state 的 integer thickness”。

在 free LEGO family 中，这个 thickness 本身严格是低一 relation-rank fiber。

这为早期“坍缩范围自然形成厚度/反弹层”提供了一个纯数学母结构，但**不自动推出任何具体材料反弹物理**。物理力学还需要 declared dynamics/grade/energy/causal transition law。

## 12. 可执行资产

- `causal_hidden_motion.py`
- `causal_block_redistribution.py`
- `causal_dimension_agreement.py`
- `causal_completion_collapse.py`
- `causal_basin_dimension.py`
- `lego_partition_fiber.py`
- corresponding tests

## 13. 前人工作边界

lattice-point counting / Ehrhart polynomial 的“次数与多面体维数”是成熟传统数学。本文不主张该事实原创。

项目性内容是：从 coarse-total LEGO fiber 直接同时导出 hidden motion rank 与 exact growth degree，并把 causally generated complete-growth law 接入已有 P008 order-adjoint collapse，再区分 exact same-family lowering 与仅 growth-degree lowering。

## 14. 下一步

1. 把 relation-rank / ball-growth / P008-basin 三重 agreement formalize 成 Lean 可复用定理；
2. 检验 close-packed / coupled graded fibers 的 complete-growth law 是否仍有 finite polynomial dimension，还是出现 quasi-polynomial / exponential causal complexity；
3. 建立 `DECLARED_RESOLUTION` 与 `CAUSAL_DERIVED_PRECISION` 的桥条件；
4. 继续寻找 physical geometry 中 exact same-family dimension lowering 的非自由例子。

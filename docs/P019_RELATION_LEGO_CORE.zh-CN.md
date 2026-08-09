# P019 —— Relation LEGO Core / 关系乐高核心

状态：`RESEARCH WIP / DISTILLED CORE`

用途：把 P019 大量 proof supplements 中已经反复稳定出现的共同骨架抽出来。本文不是最终 foundation，也不声称自然空间已经证明采用 `A_p/FCC`。它只是当前最小工作核心；详细证明、反例、实现与 prior-art 边界见各 Supplements。

---

## 1. 最小单位原则

数值 `1` 不携带维度标签。

对 collision-power fiber minimum：

\[
\Psi_{m,s}(c)
=
\min_{a_1+\cdots+a_m=c}
\sum_{u=1}^m|a_u|^s.
\]

对任意有限 `m>=1,s>=1`：

\[
\boxed{\Psi_{m,s}(1)=1.}
\]

所以提高/压低维度槽位数不会把一个 unit 的数值身份改掉。

---

## 2. Current block state

当前 coarse state 有 `k` 个可区分 blocks。

每个 block 只需要两类基本整数：

\[
\boxed{m_i>0}
\]

表示其中已经合并的原始 unit-slot capacity，以及

\[
\boxed{c_i\in\mathbb Z}
\]

表示 block total。

固定 grand total：

\[
C=\sum_i c_i.
\]

当前 relation dimension：

\[
\boxed{dim_{relation}=k-1.}
\]

---

## 3. Canonical weighted relation field

定义：

\[
\boxed{Z_{ij}=m_jc_i-m_ic_j.}
\]

矩阵式：

\[
\boxed{Z=cm^T-mc^T.}
\]

unit blocks `m_i=1` 时：

\[
Z_{ij}=c_i-c_j.
\]

基本闭合：

\[
Z_{ii}=0,
\qquad
Z_{ij}=-Z_{ji},
\]

\[
\boxed{
m_kZ_{ij}+m_iZ_{jk}+m_jZ_{ki}=0.}
\]

给定 capacities、grand total 与合法 `Z`：

\[
\boxed{
c_i=(m_iC+\sum_jZ_{ij})//M,
\qquad M=\sum_i m_i.}
\]

所以 `(m,C,Z)` 是 tree-independent present-state relation representation。

---

## 4. Dimension contraction = partition quotient

任意 coarse partition 由 0-1 incidence matrix：

\[
A:k\to\ell
\]

表示。

coarse state：

\[
\boxed{m'=Am,}
\qquad
\boxed{c'=Ac,}
\]

\[
\boxed{Z'=AZA^T.}
\]

若继续 coarse-grain：

\[
A_2(A_1ZA_1^T)A_2^T
=(A_2A_1)Z(A_2A_1)^T.
\]

所以：

\[
\boxed{Q_{A_2}\circ Q_{A_1}=Q_{A_2A_1}.}
\]

binary contraction tree 只是 partition quotient 的一种执行/坐标顺序，不是 current coarse state 的必要本体。

---

## 5. Dimension-loss kernel

定义：

\[
\boxed{K_A=\ker_{\mathbb Z}A.}
\]

则：

\[
\boxed{rank K_A=k-\ell.}
\]

同一 coarse state 的 fine totals：

\[
\boxed{c+K_A.}
\]

coarse world 看不见的 additive updates：

\[
\boxed{K_A.}
\]

因此：

\[
\boxed{
\text{state fiber}
=
\text{invisible motion lattice}
=
\text{dimension-loss kernel}.
}
\]

一次 binary merge：`k->k-1`，恰删除一个 independent internal relation：

\[
\boxed{z=Z_{ij}.}
\]

保留它即可精确反解 two-child totals。

---

## 6. Dynamics on relations

任意保持总量的整数 update：

\[
\delta\in\mathbb Z^k,
\qquad
\sum_i\delta_i=0
\]

作用：

\[
c\to c+\delta.
\]

relation update：

\[
\boxed{
Z\to Z+\delta m^T-m\delta^T.
}
\]

与 partition quotient 严格交换：

\[
\boxed{
Q_A\circ T_\delta
=T_{A\delta}\circ Q_A.
}
\]

fine primitive transfer `e_i-e_j`：

- 同 coarse block：映到 `0`；
- 不同 coarse blocks：映到 coarse primitive transfer。

所以降维同时 quotient state 与 motion。

---

## 7. Collision observation family

定义：

\[
\boxed{
E_{\mathbf m}^{(s)}(c)
=\sum_i\Psi_{m_i,s}(c_i),
\qquad s=1,2,3,\ldots
}
\]

`Psi` 的 exact closed form：若

\[
c=mq+r,
\qquad0\le r<m,
\]

则：

\[
\boxed{
\Psi_{m,s}(c)
=(m-r)|q|^s+r|q+1|^s.
}
\]

一步 slope：

\[
\boxed{
\Psi(c+1)-\Psi(c)
=|q+1|^s-|q|^s.
}
\]

所以 fiber optimization 可以只用 finite integer exchange，不需要微积分。

---

## 8. Ball as relation-state sublevel set

定义 fixed-total tagged ball：

\[
\boxed{
B_{\mathbf m}^{(s)}(T)
=\{c:\sum c_i=C,\ E_{\mathbf m}^{(s)}(c)\le T\}.
}
\]

由于 `(m,C,Z)` 唯一恢复 `c`，该 ball 可以视作 weighted relation-state 的 sublevel set。

特殊观察：

### `s=1`

zero-total 时：

\[
\boxed{
M E^{(1)}
=2\max_S Z(S,S^c).
}
\]

unit `A_p` 中：

\[
N d_G=\max cut(Z).
\]

### `s=2`

unit zero-sum 中：

\[
\boxed{
\sum_{i<j}Z_{ij}^2=2Nq.
}
\]

coarse tagged square energy可由 weighted `Z` + bounded block residues 精确重建。

所以 graph/radial 更适合解释成同一 relation state 的不同 observation channels。

---

## 9. Arbitrary-dimension ball quotient theorem

对任意 partition `A`：

\[
\boxed{
\min_{Ac=y}E_{\mathbf m}^{(s)}(c)
=E_{A\mathbf m}^{(s)}(y).
}
\]

因此：

\[
\boxed{
Q_A(B_{\mathbf m}^{(s)}(T))
=B_{A\mathbf m}^{(s)}(T).
}
\]

即：

> 任意高维 tagged ball 降到任意 coarse partition，得到的严格是同一 family 的低维 tagged ball。

没有极限、积分或连续投影。

---

## 10. Directional excavation / boundary section

一次 oriented binary merge `j->i` 的 coarse fiber 是一条 internal relation arithmetic line。

在 finite energy ball 中，fiber feasible states 是有限整数 interval；该方向唯一的穿界 state 是 interval right endpoint。

所以：

\[
\boxed{
C_{\mathbf m,j\to i}^{(s)}(T)
\cong
B_{\mathbf m'}^{(s)}(T).
}
\]

任意 oriented contraction flag `F` 复合这些 endpoint lifts，得到：

\[
\boxed{
L_F:B_{A\mathbf m}^{(s)}(T)
\hookrightarrow B_{\mathbf m}^{(s)}(T),
\qquad
Q_A\circ L_F=id.
}
\]

coarse quotient tree-independent，但 selected boundary witness 一般 flag-dependent。

---

## 11. Exact refinement memory

若未来只允许 quotient-compatible coarse operations，deleted internal relations 可以永久删除。

若未来允许 exact refinement，则一个 coarse block 内含 `r` 个 fine blocks 时：

- 保存任意 spanning tree 的 `r-1` 条 internal weighted relations；
- 加 coarse total 与 capacities；
- 即可唯一恢复所有 child totals。

整个 partition 的 Refinement Forest 只需：

\[
\boxed{k-\ell}
\]

条 independent relation witnesses，恰等于被 quotient 删除的 relation rank。

真实 merge chronology 属于 process provenance，不是 present-state exact refinement 的必要条件。

---

## 12. Relation precision scale

令：

\[
\boxed{g=\gcd(m_i).}
\]

则：

\[
\boxed{m=g\hat m,}
\qquad
\boxed{Z=g\hat Z,}
\qquad
\gcd(\hat m)=1.
\]

定义：

- relation quantum：`g`；
- field-preserving translation period：
  \[
  \tau=M/g.
  \]

有：

\[
\boxed{g\tau=M.}
\]

partition coarsening 只能使：

\[
\boxed{g_{fine}\mid g_{coarse}.}
\]

primitive relation state coarsening产生整数 scale carry：

\[
\boxed{
g'=gh.}
\]

因此 precision scale 可以从 capacities 的整数结构中内生出来。

---

## 13. Dimension 的三种内部读法

在当前 `A_p` 工作模型：

1. ball-growth finite-difference depth：
   \[
   dim_{growth}=p;
   \]
2. repeated relation contraction depth：
   \[
   dim_{contract}=p;
   \]
3. independent relation degrees：
   \[
   dim_{relation}=p.
   \]

所以：

\[
\boxed{
\dim_{growth}
=
\dim_{contract}
=
\dim_{relation}
=p.
}
\]

维数不再只能由外部写下的坐标数声明。

---

## 14. Minimum relation geometry for all `s>=2`

写：

\[
C=Mq+r,
\qquad0\le r<M.
\]

所有 `s>=2` 的 global minimizer unit slots 都取 `q/q+1`。

block `i` 若含 `h_i` 个 `q+1` slots：

\[
c_i=m_iq+h_i,
\qquad
\sum h_i=r.
\]

则：

\[
\boxed{
Z_{ij}=m_jh_i-m_ih_j,
}
\]

bulk `q` 完全消失，并有：

\[
\boxed{|Z_{ij}|\le m_im_j.}
\]

所以 power order `s>=2` 改变 minimum value，但不改变 minimum relation geometry。

---

## 15. Future-safe collapse rule

抽象安全门：给 quotient `Q` 与 future operation `T`，只有当：

\[
\boxed{
Q(x)=Q(y)
\Rightarrow
Q(Tx)=Q(Ty)
}
\]

等价于存在：

\[
\boxed{Q\circ T=\bar T\circ Q}
\]

时，`T` 才不会把 hidden detail 重新反馈到 coarse layer。

若所有 future generators 与 observations 都 factor through `Q`，被 Q 删除的 distinctions 可以永久忘记。

所以：

\[
\boxed{
\text{safe collapse}
=
\text{quotient by future operational indistinguishability}.
}
\]

---

## 16. 当前工具层级

### Canonical / tree-independent

- `(m,C,Z)` weighted relation state；
- partition quotient `Q_A`；
- kernel `K_A`；
- collision observation `E^(s)`；
- relation scale `g`。

### Chart / computational convenience

- unit pair field；
- spanning-tree flow chart；
- Contraction Atlas `z` chart；
- Refinement Forest。

### Witness / provenance

- directional boundary sections；
- contraction flags；
- actual history / P021 witness relations。

这些层不能混同。

---

## 17. 前人工作纪律

当前核心大量复用成熟数学：

- `A_n` root lattices；
- integer incidence/cut/flow spaces；
- spanning-tree bases；
- Smith normal form / integer lattices；
- separable/discrete convex minimization；
- quotient congruence / bisimulation 类思想；
- exterior/wedge matrix representation。

P019 不把这些成熟工具改名为原创。

当前可能值得研究原创性的，是它们在“finite precision + dimension contraction + collision observations + relation erasure/future safety”中的具体整体组合；正式 novelty claim 前必须完成 lineage audit。

---

## 18. 下一阶段单一主问题

不再继续横向制造 primitive。

下一阶段只攻：

\[
\boxed{
\text{给定 future operation language，
求最小 exact relation state。}
}
\]

具体包括：

1. 自动计算哪些 internal relations 可以永久 quotient；
2. 哪些只需 demand-driven refinement 时恢复；
3. 哪些 P021 witness identity 必须作为 provenance 保留；
4. 将 P018 precision selection 重写成 relation-state refinement cost；
5. 在可控范围内 Lean 形式化 partition quotient、kernel 与 directional ball theorem。

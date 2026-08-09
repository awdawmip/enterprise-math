# A3 Guard-Image Lattice 补充 12 —— Guard Quotient Module、Smith Torsion 与 Predicate Precision Exact Sequence

状态：`RESEARCH WIP / EXACT FINITELY-GENERATED ABELIAN QUOTIENT PROFILE`

## 1. 从 two-guard quotient 推广

Supplement 11 对两个 guards、rank-one hidden image 证明：

\[
\mathbb Z^2/\mathbb Z h
\cong
\mathbb Z\oplus\mathbb Z/d\mathbb Z.
\]

一般 finite guard family 有：

\[
W:\mathbb Z^k\to\mathbb Z^r,
\]

partition hidden kernel：

\[
K_A\le\mathbb Z^k,
\]

hidden guard image：

\[
\boxed{L_A=W(K_A)\le\mathbb Z^r.}
\]

真正的 coarse predicate-information object 是：

\[
\boxed{
\mathcal Q_A
:=
\mathbb Z^r/L_A.
}
\]

它不是一个 scalar precision level，而是一个 finitely generated abelian group。

## 2. A3-G42 —— free rank 与 hidden rank 对偶

设：

\[
\operatorname{rank}_{\mathbb Q}L_A=d.
\]

则：

\[
\boxed{
\operatorname{rank}_{free}\mathcal Q_A
=r-d.
}
\]

因此：

- hidden rank越高，coarse predicate quotient 的 free rank越低；
- refinement 让 hidden lattice 缩小时，predicate quotient 的 free rank只能保持或增加。

这与“更多 relation detail 被暴露”一致。

## 3. Smith invariant factors

取 `L_A` 任意整数 generator matrix：

\[
G\in\mathbb Z^{m\times r}.
\]

令：

\[
\Delta_j
=
\gcd\{\text{所有 }j\times j\text{ minors of }G\},
\]

并约定：

\[
\Delta_0=1.
\]

若 hidden rank 为 `d`，Smith nonzero invariant factors：

\[
\boxed{
s_j=\Delta_j/\Delta_{j-1},
\qquad j=1,\ldots,d.
}
\]

满足：

\[
\boxed{s_1\mid s_2\mid\cdots\mid s_d.}
\]

于是：

\[
\boxed{
\mathcal Q_A
\cong
\mathbb Z^{r-d}
\oplus
\bigoplus_{j:s_j>1}\mathbb Z/s_j\mathbb Z.
}
\]

所以 predicate precision 自然含：

- free integer coordinates；
- finite torsion coordinates。

## 4. A3-G43 —— torsion order 与 lattice saturation

finite torsion subgroup 的 order：

\[
\boxed{
|\operatorname{Tor}(\mathcal Q_A)|
=
\prod_{j:s_j>1}s_j
=
\Delta_d.
}
\]

当全部 `s_j=1`，hidden lattice 在其 rational span 内是 primitive/saturated，对应 quotient 没有 finite torsion，只留下 free coordinates。

当某个 `s_j>1`，coarse predicate state 必须额外保存 finite residue 类，才能完整标记 hidden coset。

Supplement 11 的 two-guard rank-one：

\[
G=(h_1,h_2),
\]

只有：

\[
\Delta_1=\gcd(|h_1|,|h_2|)=d,
\]

所以：

\[
\mathcal Q
\cong
\mathbb Z\oplus\mathbb Z/d\mathbb Z.
\]

正好恢复 `(free integer, torsion residue)`。

## 5. A3-G44 —— Refinement Exact Sequence

设 `R` refine `P`：

\[
R\preceq P.
\]

则：

\[
K_R\subseteq K_P.
\]

施加 `W`：

\[
\boxed{L_R\subseteq L_P.}
\]

因此有自然 quotient map：

\[
\pi:
\mathbb Z^r/L_R
\to
\mathbb Z^r/L_P.
\]

它是 surjective，kernel：

\[
\ker\pi
=
L_P/L_R.
\]

所以得到 exact sequence：

\[
\boxed{
0
\to
L_P/L_R
\to
\mathcal Q_R
\to
\mathcal Q_P
\to
0.
}
\]

这给 refinement 一个非常直接的 precision 解释：

> **child predicate state 比 parent 多暴露的完整 guard detail，恰好是 hidden-image quotient `L_P/L_R`。**

rank-one modulus refinement：

\[
L_P=\mathbb Z h,
\qquad
L_R=q\mathbb Z h,
\]

因此新增 detail kernel：

\[
\boxed{
L_P/L_R
\cong
\mathbb Z/q\mathbb Z.
}
\]

这就是 Supplement 05/06 的 residue refinement 为何自然产生 mod-`q` precision。

## 6. 不能把不同 gcd 混成一个 scale

A3 当前已经有多个不同 arithmetic scale：

1. weighted relation capacities 的 structural relation quantum：
   \[
   g_m=\gcd(m_i);
   \]
2. guard hidden lattice quotient 的 Smith torsion factors：
   \[
   s_1,\ldots,s_d;
   \]
3. rank-one child subgroup index：
   \[
   q=[L_P:L_R].
   \]

它们可能在具体 observable 下有 theorem 关系，但不能因都出现 gcd/index 就自动认同。

因此 precision state 应 typed：

\[
\boxed{
\text{relation scale}
\quad\text{vs}\quad
\text{predicate quotient torsion}
\quad\text{vs}\quad
\text{refinement subgroup index}.
}
\]

## 7. A3-G45 —— predicate quotient state 是 branch geometry 的 complete base object

固定 partition `A`。

两个 fine score vectors：

\[
x,x'\in\mathbb Z^r
\]

位于同一 coarse fiber 的 hidden score coset，当且仅当：

\[
\boxed{x-x'\in L_A.}
\]

也就是：

\[
\boxed{[x]=[x']\in\mathcal Q_A.}
\]

所以任何只依赖该 coarse fiber 内 threshold reachability / branch geometry 的 future query，其 base state 应是：

\[
\boxed{
[x]\in\mathcal Q_A,
}
\]

而不是任意选择一个 fine score representative。

具体计算可以：

- 低维用 Supplement 11 的 explicit free/torsion coordinates；
- 一般情况用成熟 Smith/Hermite transform 生成 quotient coordinates。

A3 reference implementation当前只计算 invariant factors，不复制 production SNF coordinate engine。

## 8. 实现

新增：

- `src/enterprise_math/guard_quotient_module.py`；
- `tests/test_guard_quotient_module.py`。

接口：

- `determinantal_divisor`；
- `guard_quotient_module_profile`；
- `guard_partition_quotient_profile`；
- `GuardQuotientModuleProfile`。

profile 输出：

- guard count；
- hidden rank；
- free rank；
- Smith invariant factors；
- torsion factors；
- torsion order。

测试包括：

- rank-one `(6,-4)` 恢复 `Z ⊕ Z/2Z`；
- primitive rank-one 无 torsion；
- `< (2,0),(0,3) >` 得 Smith `(1,6)`；
- redundant generators 不改变 quotient invariants；
- zero hidden lattice 产生全 free quotient；
- full primitive hidden lattice 产生 trivial quotient；
- known 3D diagonal lattice 得 `(2,4,8)`。

## 9. 前人工作边界

Smith normal form、determinantal divisors、finitely generated abelian groups、exact sequences 都是成熟 algebra。

A3 不主张这些基础工具原创。

当前项目特化是把：

\[
\boxed{
\text{partition hidden motion}
\to
W(K_A)
\to
\mathbb Z^r/W(K_A)
\to
\text{future predicate precision state}
}
\]

变成一个统一接口，并与 relation quotient / task precision / branch reachability联结。

## 10. 下一步

1. 建立一个 typed `A3PrecisionCertificate`，同时记录 relation rank/quantum 与 guard quotient free/torsion profile；
2. refinement certificate 中显式记录 `L_P/L_R` 的新增 predicate detail，而不是只给 rank gain；
3. 用 production-grade HNF/SNF 工具替换 combinatorial minors 参考实现之前先保持 dependency-light；
4. 将 quotient module 作为 global symbolic branch program 的 state space；
5. 与 P018 typed scale / P023 minimal state 做 theorem-level bridge，不重复母理论。

# Causal Event Grammar Core —— 从守恒事件生成 Primitive Geometry

状态：`ACTIVE CROSS-ROUTE RESEARCH CORE / INTERNAL THEOREMS + PHYSICAL BRIDGE OPEN`

## 1. 核心纠偏

后续不再以 root lattice、packing、vector space 或 precision scale 作为 primitive geometry 的起点。

当前统一顺序为：

\[
\boxed{
\text{local LEGO state}
\to
\text{admissible causal events}
\to
\text{irreducible events}
\to
\text{integer grade}
\to
\text{primitive shell}
\to
\text{relation geometry}.
}
\]

传统 root/code/lattice/design 对象只在某些 regime 下作为这一结构的 shadow 出现。

## 2. Admissibility

给 raw event \(\Delta\)。conservation / support / residue law 决定其是否允许：

\[
\Delta\in\mathcal E_L.
\]

典型例子：

- 无守恒；
- exact total conservation；
- total mod \(m\) conservation；
- 一般 residue conservation map \(\Phi\) 的 kernel；
- local alphabet + residue code glue。

## 3. Irreducibility

允许事件不自动等于 primitive event。

若：

\[
\Delta=a+b
\]

其中 \(a,b\) 都是非零允许事件，并且 decomposition 不在任何 slot 上发生符号抵消，则 \(\Delta\) 是 conformally decomposable。

不能这样拆的事件称为 causal irreducible event。

传统 integer-kernel / Graver-basis / circuit 工具与这一层有成熟邻域；本项目不对一般算法工具作原创声明。

## 4. Grade

给 irreducible event 一个非负整数 grade：

\[
g:\mathcal E_{irr}\to\mathbb N_0.
\]

grade 的来源必须显式标记。候选包括：

- support size；
- primitive-operation cost；
- local-cell integer quadratic grade；
- future-distinguishability 反推出的 semantic loss grade；
- 经物理实验 bridge 验证的其他有限整数 grade。

不能把传统 Euclidean norm 或人为 precision label 默认提升成 primitive grade。

## 5. Primitive shell

定义：

\[
g_*=\min_{e\in\mathcal E_{irr},e\ne0}g(e),
\]

\[
\boxed{
\Phi_*=
\{e\in\mathcal E_{irr}:g(e)=g_*\}.
}
\]

`irreducible` 与 `primitive` 必须分开。

- mod 4 unit-amplitude grammar：support-2 transfer 与 support-4 creation 都 irreducible；若 grade=support，则 primitive shell 只有 support 2。
- binary E8 Construction-A grammar：axis event support 1 与 glue event support 4，但 local square-grade都为 4，因此共同进入 primitive shell。

## 6. Primitive relation geometry

在 additive event language 中，一个自然 first-link relation 是：

\[
e\sim f
\iff
e-f\in\Phi_*.
\]

它生成：

- primitive direction link；
- edge common-neighbor context；
- shell/ball growth；
- relation boundary；
- automorphism/future-context quotient。

这些是 primitive event grammar 的 derived observables，而不是先验连续空间结构。

## 7. Z/A/D 的守恒生成

若 grade 取 support size，unit amplitude \(\Delta_i\in\{-1,0,1\}\)：

- no conservation：minimum support 1，\(\pm e_i\) -> Z grammar；
- exact total conservation：minimum support 2，\(e_i-e_j\) -> A grammar；
- parity conservation：minimum support 2，\(\pm e_i\pm e_j\) -> D grammar。

所以：

\[
\boxed{
\text{conservation law}+
\text{primitive grade}
\to
\text{root-geometry shadow}.
}
\]

## 8. Modular higher irreducibles

对 total mod \(m\) conservation：

- \(m=1\)：irreducibles 是 single-slot events；
- \(m=2\)：irreducibles 正好是 D-type support-2 sign pairs；
- \(m\ge3\)：irreducibles 包括 A-type support-2 transfers，以及 support-\(m\) 的全同号 creation/annihilation events。

因此 mod \(m\ge3\) 与 exact conservation 在 primitive support-2 geometry 上相同，但在第 \(m\) 阶 causal event grammar 分裂。

这定义 support-order tomography，而不是把 primitive geometry误当完整 ontology。

## 9. Local alphabet + residue code

code 不是 primitive。更底层是：

\[
\text{residue conservation checks}
\to
C=\ker\Phi
\to
\text{local alphabet lift}.
\]

每个 local residue symbol有最低 grade与最低 representative multiplicity。

codeword \(c=(c_i)\) 的最低 lift：

\[
G(c)=\sum_i g(c_i),
\qquad
M(c)=\prod_i\mu(c_i).
\]

比较 minimum nonzero code lift grade \(d_C\) 与 local zero-sector primitive grade \(g_0\)：

- \(d_C<g_0\)：code/glue dominated；
- \(d_C>g_0\)：local dominated；
- \(d_C=g_0\)：primitive-grade resonance。

E6/E7/E8 的已研究 code constructions 都位于 resonance regime；binary parity/D 位于 code-dominated regime。

## 10. Primitive-shell phase transition

放松 conservation constraint、扩大 code 时：

\[
C\subset C'.
\]

minimum code grade只能不变或下降。

- 若 primitive grade不变，旧 primitive shell 可包含于新 shell；
- 若更低 grade事件出现，旧 primitive events 会退到 higher shell，minimum-precision geometry 可以整体重排。

因此：

\[
\boxed{
\text{weaker conservation}
\not\Rightarrow
\text{higher primitive coordination}.
}
\]

已构造的 binary length-8 chain 给出 grade-4 shell `48 -> 112 -> 240`，再放松到 even parity 后 grade降到 2，primitive shell 回到 112-event D8 profile。

## 11. Geometry 不能唯一反推 causal ontology

已知严格反例：

1. \(A_3\cong D_3\cong FCC\)：
   - 4 rank-1 slots + exact total conservation；
   - 3 rank-1 slots + parity conservation；
   可给相同 3D primitive geometry shadow。
2. E8：
   - 8 rank-1 integer cells + binary extended-Hamming code；
   - 4 rank-2 hex/A2 cells + ternary Hamming code；
   给相同 rank/root-count geometry shadow。

所以 factorization/provenance 是否属于 current state，必须由 future/context quotient 判断。

## 12. 物理边界

`exact conservation + unit amplitude + support-minimality + slot symmetry -> A_p` 是**已声明 causal slot model 内的定理**。

它不是“物理空间必为 A_p/FCC”的证明。

要把它升级成自然本体，需要 P016 风格 bridge：

- 自然最小 event 是否真是 unit amplitude；
- 自然 primitive grade 是否真由 support/minimum semantic cost决定；
- slots 是否物理等价；
- exact conservation 还是 modular/code conservation；
- 哪些 continuation/material contexts 属于几何，哪些只是材料状态。

## 13. 当前恢复入口

主要可执行资产：

- `causal_unit_transfer_minimality.py`
- `causal_conservation_geometry.py`
- `causal_modular_conservation.py`
- `causal_irreducible_modular_events.py`
- `causal_conservation_tomography.py`
- `causal_residue_conservation.py`
- `causal_local_alphabet_code.py`
- `causal_code_lattice.py`
- `causal_e6_hex_code_geometry.py`
- `causal_code_event_context.py`
- `causal_code_relaxation.py`
- `causal_lattice_direction_link.py`
- `causal_close_packed_contact.py`

完整仓库 CI 仍属于 integration gate；研究结论当前以 exact integer derivation、small exhaustive oracle 与 executable reference 为主。

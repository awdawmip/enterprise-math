# Causal Kernel–Grade Geometry —— 从守恒 Kernel 与 Local LEGO Grade 生成 Primitive Geometry

状态：`ACTIVE CROSS-ROUTE CORE / EXACT SPECIALIZATIONS + GENERAL CAUSAL PRINCIPLE`

## 1. 母式

给一个事件空间。事件写成 local LEGO cells 的变化：

\[
\Delta=(\Delta_1,\ldots,\Delta_N).
\]

给 conservation / residue map：

\[
\boxed{\Phi(\Delta)=0.}
\]

它决定什么事件可以发生。

再给每个 local cell 的非负整数 grade：

\[
g_i(0)=0,
\qquad
g_i(a)>0\ (a\ne0).
\]

joint grade 只做 LEGO additive composition：

\[
\boxed{
G(\Delta)=\sum_i g_i(\Delta_i).
}
\]

定义 minimum nonzero causal grade：

\[
\boxed{
G_*=\min_{\Delta\ne0,\Phi(\Delta)=0}G(\Delta).
}
\]

primitive shell：

\[
\boxed{
\mathcal P(\Phi,g)
=\{\Delta\ne0:\Phi(\Delta)=0,\ G(\Delta)=G_*\}.
}
\]

这就是当前 primitive geometry 的母对象。

## 2. 因果顺序

传统路径常写成：

`lattice + norm -> shortest vectors -> geometry`。

当前项目顺序改为：

\[
\boxed{
\text{causal conservation law}
+\text{local unit grade}
\to
\text{minimum causal events}
\to
\text{root/lattice/norm shadow}.
}
\]

传统 shortest-vector / code-lattice / root-system 工具仍可以用于计算与验证，但不再自动占据 ontology 起点。

## 3. Local grade 不是统一固定的 support

`support size` 只是 local grade 的一个特例：

\[
g_i(a)=\mathbf1[a\ne0].
\]

另一个重要特例是 scalar integer square grade：

\[
g_i(a)=a^2.
\]

hex/A2 local cell 则可使用：

\[
\boxed{g_{hex}(u,v)=u^2+uv+v^2.}
\]

所以 primitive event 的“最小”不能未经 bridge 就等同最小 support、欧氏长度或人为 precision。

## 4. Z / A / D specializations

### Z

无 conservation，unit-support grade：

\[
\mathcal P=\{\pm e_i\}.
\]

### A

exact total conservation：

\[
\Phi(\Delta)=\sum_i\Delta_i=0,
\]

unit-amplitude/support grade 下：

\[
\mathcal P=\{e_i-e_j:i\ne j\}.
\]

这生成 A_(N-1) primitive grammar。

### D

parity conservation：

\[
\sum_i\Delta_i\equiv0\pmod2.
\]

unit-amplitude/square grade最低层：

\[
\mathcal P=\{\pm e_i\pm e_j:i\ne j\}.
\]

这生成 D_N shadow。

## 5. Binary code specializations

对 local scalar integer cell modulo 2：

- zero-sector event \(\pm2e_i\) local grade 4；
- nonzero residue representative \(\pm1\) grade 1。

给 binary residue conservation code \(C\)：

\[
x\bmod2\in C.
\]

codeword weight \(w\) 的最低 lift grade为 \(w\)，multiplicity 为 \(2^w\)。

所以：

- single parity check: minimum code grade 2 < local grade 4 -> D_N code-dominated shell；
- [7,3,4] simplex: minimum code grade 4 = local grade 4 -> E7 resonance；
- [8,4,4] extended Hamming: grade 4 resonance -> E8。

## 6. Ternary hex specializations

hex local cell用 integer weight coordinates：

\[
(u,v)\in\mathbb Z^2,
\quad
r=u-v\pmod3,
\]

\[
g_{hex}=u^2+uv+v^2.
\]

zero residue sector：minimum nonzero grade 3，共 6 states。

两个 nonzero residue sectors：minimum grade 1，各 3 个 representatives。

因此：

### E6

三个 hex cells + ternary repetition constraint：

\[
r_1=r_2=r_3.
\]

base primitive count：

\[
3\times6=18.
\]

两个 nonzero codewords各有：

\[
3^3=27
\]

个 grade-3 lifts。

所以：

\[
18+2\times27=72.
\]

### E8 ternary construction

四个 hex cells + [4,2,3]_3 Hamming code。

8 个 nonzero weight-3 codewords，各给 \(3^3=27\) lifts：

\[
4\times6+8\times27=240.
\]

与 binary E8 construction 有不同 factorization grammar，但相同 E8 geometry shadow。

## 7. Primitive-grade resonance

定义 minimum nonzero code lift grade：

\[
d_C.
\]

local zero-sector primitive grade：

\[
g_0.
\]

三种 regime：

\[
d_C<g_0:\ \text{code dominated};
\]

\[
d_C>g_0:\ \text{local dominated};
\]

\[
\boxed{d_C=g_0:\ \text{primitive-grade resonance}.}
\]

E6/E7/E8 的已研究 code constructions 都是 resonance；D-family binary parity construction 是 code-dominated。

这提供一个 causal 解释：exceptional local relation richness 可以来自多个 primitive event channels 在最低 grade 同层共存，而不是先把 exceptional root system 当作 primitive object。

## 8. Constraint relaxation 与 shell phase transition

扩大 residue code：

\[
C\subset C'.
\]

会增加允许 event sectors，但 minimum grade 可能下降。

- grade 不变：primitive shell 可扩张；
- grade 下降：新更小事件重定义 primitive shell，旧 events 退到 higher shell。

所以：

\[
\boxed{
\text{weaker conservation}
\not\Rightarrow
\text{primitive coordination monotone increase}.
}
\]

binary length-8 已有 explicit chain：

`48 -> 112 -> 240` at grade 4，随后放松到 even-parity 后 grade降到2，primitive count回到112。

## 9. Geometry 与因果 factorization 非单射

已知：

- A3 与 D3 都可 shadow FCC；
- E8 同时有 binary rank-1-cell factorization 与 ternary rank-2-hex-cell factorization。

因此：

\[
\boxed{
\text{geometry}
\not\Rightarrow
\text{unique causal law/factorization}.
}
\]

factorization provenance 只有在 future operation / observation 会读取它时才属于 current state；否则必须经过 future-safe quotient 后才能决定是否删除。

## 10. 与传统数学的边界

以下均有成熟前人工作：

- lattice shortest vectors；
- Construction A；
- linear codes / parity checks；
- Lee/Euclidean code weight；
- ADE root systems；
- Coxeter numbers；
- block designs；
- Graver/circuit-like integer kernel primitives。

本项目不声称发明这些工具。

当前研究命题是把它们重新排序为：

\[
\boxed{
\text{local causal alphabet}
+\text{conservation kernel}
+\text{grade}
\to
\text{traditional structures as shadows}.
}
\]

## 11. 开放问题

1. 哪些物理实验能确定自然 local grade，而不是只确定 geometry shadow？
2. conservation map + local grade 在什么条件下唯一决定 all-context future quotient？
3. 是否可以按 causal support/grade tomography 识别多个不同 factorization origins？
4. 哪些 homogeneous code support systems会生成 connected + edge-context-uniform primitive geometry？
5. A/D/E 是否能在某个明确的 causal minimality/factorization 条件下得到分类，而不是调用传统 ADE 分类作为起点？

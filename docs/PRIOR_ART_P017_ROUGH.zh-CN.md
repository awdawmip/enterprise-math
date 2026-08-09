# P017 Rough Number / Buchstab 前人工作附录

状态：`PRIOR-ART APPENDIX`  
范围：P017 cofactor-window 路线使用的 rough-number 计数、最小素因子递归与经典素数估计

## Rough numbers

现代筛法文献使用 `Phi(x,y)` 一类函数计数不含小素因子的整数，并通过 Buchstab / de Bruijn 理论研究它们。Steve Fan 关于 rough number 的显式估计工作是这一成熟框架的当前参考。[SRC-FAN-2023-ROUGH-NUMBERS]

## Buchstab 递归

按下一最小素因子分解 sifted set，以及 Buchstab identity，本身都是成熟筛法工具。Runbo Li 关于 Buchstab identity 变体的工作提供了近期明确参考，说明这种递归不是进取数论新构造。[SRC-LI-2025-BUCHSTAB]

## 素数倒数和与素数计数估计

在精确 L049 hit-state union 之后使用的渐近步骤，来自经典素数分布估计，而不是项目新数学。Rosser 与 Schoenfeld 给出了标准的素数计数函数以及素数倒数和显式估计，属于经典 Mertens 理论邻域。[SRC-ROSSER-SCHOENFELD-1962-PRIME-ESTIMATES]

特别地，P017 将以下事实视为前人工作：

\[
\sum_{p\le x}\frac1p
=
\log\log x+B_1+o(1)
\]

以及不超过 `x` 的素数数量为 `o(x)`（经典结果实际上远强于此）。项目只在已经得到有限精确资源素数区间和精确 hit-count 包络之后才调用这些事实。

因此 P017 **不**声称以下内容属于项目发明：

- p-rough 数；
- `Phi(x,y)` 型 rough-number 计数；
- 按下一最小素因子分割筛后集合；
- Buchstab identity 或其迭代变体；
- 素数倒数和的 Mertens 定理；
- 素数定理、Rosser–Schoenfeld 不等式或经典素数计数估计。

## 当前项目专门检验的内容

P017 真正进行压力测试的内容更窄：相邻平方几何使每个 least-factor shell 获得一个由同一截断 `k` 和最小素数 `p` 决定的**精确移动 cofactor interval**；这个 interval 的 raw 长度本身又是精确 quotient-response / boundary-carry 量。把成熟 least-factor recursion 应用到这些特殊窗口，会产生额外有限约束，其中包括高带阈值 `p^2 >= 2k`：此时每个第二因子分支至多一个 raw candidate，而且整个 shell 的状态按重数计至多含三个素因子。

后续高带路线先在完全有限整数层得到 pairwise resource separation、multiplicative capacity 与 cross-shell hit-state unions，然后才调用任何解析素数分布定理。经典素数倒数估计只用于把项目已经推导出的有限资源区间

\[
\sqrt{2k}\le r\le\frac{k+2}{2}
\]

转化为渐近包络。因此解析推论中的 `log(2)` 常数，只是经典 Mertens 行为在项目特定端点上的专门化，并不是新的素数分布常数。

这一平方盆地专门化的历史创新状态仍为 `NOVELTY_UNVERIFIED`。它的价值取决于这些特殊移动窗口和精确资源碰撞能否产生普通平均筛密度无法给出的 survivor 上界。

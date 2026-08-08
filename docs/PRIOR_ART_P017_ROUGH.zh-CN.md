# P017 Rough Number / Buchstab 前人工作附录

状态：`PRIOR-ART APPENDIX`  
范围：P017 cofactor-window 路线使用的 rough-number 计数与最小素因子递归

## Rough numbers

现代筛法文献使用 `Phi(x,y)` 一类函数计数不含小素因子的整数，并通过 Buchstab / de Bruijn 理论研究它们。Steve Fan 关于 rough number 的显式估计工作是这一成熟框架的当前参考。[SRC-FAN-2023-ROUGH-NUMBERS]

## Buchstab 递归

按下一最小素因子分解 sifted set，以及 Buchstab identity，本身都是成熟筛法工具。Runbo Li 关于 Buchstab identity 变体的工作提供了近期明确参考，说明这种递归不是进取数论新构造。[SRC-LI-2025-BUCHSTAB]

因此 P017 **不**声称以下内容属于项目发明：

- p-rough 数；
- `Phi(x,y)` 型 rough-number 计数；
- 按下一最小素因子分割筛后集合；
- Buchstab identity 或其迭代变体。

## 当前项目专门检验的内容

P017 真正进行压力测试的内容更窄：相邻平方几何使每个 least-factor shell 获得一个由同一截断 `k` 和最小素数 `p` 决定的**精确移动 cofactor interval**；这个 interval 的 raw 长度本身又是精确 quotient-response / boundary-carry 量。把成熟 least-factor recursion 应用到这些特殊窗口，会产生额外有限约束，其中包括高带阈值 `p^2 >= 2k`：此时每个第二因子分支至多一个 raw candidate，而且整个 shell 的状态按重数计至多含三个素因子。

这一专门化的历史创新状态仍为 `NOVELTY_UNVERIFIED`。它的价值取决于这些特殊移动窗口能否产生普通平均筛密度无法给出的 survivor 上界。

# P025 补充 69 —— Projective Activation 的点态 Squarefree 安全盆地

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 47、66–67  
Hard block：`NONE`

## 1. 在任何 exceptional-set 计数之前就存在点态安全区

考虑 primitive 非 unit triple

\[
a+b=c,\qquad a,b>1.
\]

Stage 67 把

\[
\sigma_{\rm proj}\ge1
\]

称为 projective **activation**。

在导入 de Bruijn 后，activation layer 是稀疏的；本补充进一步识别出一个完全点态、永远不可能激活的大型结构区域。

## 2. P025-T137 —— `c` squarefree 强迫进入 subunit basin

若 `c` squarefree，则

\[
m(c)=1,
\]

因此 c-oriented term 因分母为大于 1 的正整数而严格小于 1。

对 a-oriented term，

\[
\rho_a=\frac{m(a)}{K_{bc}}.
\]

因为 `b>1`，其 block capacity 为正，而 denominator 中包含

\[
R_cC(b)=cC(b)\ge c.
\]

但

\[
m(a)\le a<c.
\]

故

\[
\rho_a<1.
\]

b-oriented term 同理。因此

\[
\boxed{c\text{ squarefree}\Longrightarrow\sigma_{\rm proj}<1.}
\]

所以任何 activated 非 unit state 的输出 component `c` 必须 nonsquarefree。

## 3. P025-T138 —— 两个 input sides 都 squarefree 也强迫进入 subunit basin

若 `a,b` 都 squarefree，则

\[
m(a)=m(b)=1,
\]

两个 side-oriented terms 都不可能达到 1。

对 c-oriented term，exact block capacity 变成

\[
K_{ab}=R_bC(a)+R_aC(b)=b\,a'+a\,b'=(ab)',
\]

因为 `a,b` squarefree 且互素。

对任意 squarefree `n>1`，

\[
\frac{n'}n=\sum_{p\mid n}\frac1p\ge\frac1n,
\]

故 `n'>=1`。于是

\[
(ab)'=ba'+ab'\ge b+a=c.
\]

如果 `c` nonsquarefree，则

\[
m(c)<c;
\]

如果 `c` squarefree，则 P025-T137 已处理。因此

\[
\boxed{a,b\text{ both squarefree}\Longrightarrow\sigma_{\rm proj}<1.}
\]

## 4. P025-C14 —— activation 至少需要两个 components 含 repeated-prime structure

合并 P025-T137–T138：

\[
\boxed{
\sigma_{\rm proj}\ge1
\Longrightarrow
\begin{cases}
c\text{ nonsquarefree},\\
\text{a,b 中至少一个 nonsquarefree}.
\end{cases}}
\]

等价地，

\[
\boxed{
\text{至多一个 nonsquarefree component}
\Longrightarrow
\sigma_{\rm proj}<1.
}
\]

所以非 unit activation 至少需要两个不同 components 携带 repeated-prime information，并且其中一个永远是 `c`。

这个结论是点态、初等的，不使用 density theorem。

## 5. 精确样本

### `c` squarefree 的安全样本

\[
9+2=11.
\]

虽然 `9` nonsquarefree，但 `c=11` squarefree，因此该 triple 被强制落入 subunit basin。

### 两个 sides squarefree 的安全样本

\[
3+5=8.
\]

这里 `c` nonsquarefree，但两个 inputs 都 squarefree，所以仍不可能 activation。

### Activated 样本

\[
2+25=27,
\quad
3+125=128,
\quad
7+162=169,
\quad
49+576=625
\]

都满足 `c` nonsquarefree 且至少一个 side nonsquarefree，符合必要条件。

该条件是必要而非充分。

## 6. 与 Stage 61 的关系

Stage 61 证明高 projective threshold 会强迫一个大的 paired residual product。P025-C14 可以看作 threshold-one 的结构 shadow，但它比“product 大于某个常数”更具体：它直接识别出哪些 components 必须已经含有 repeated-prime information。

特别地，activation layer 不可能由一个孤立 squareful component 加上其它全 squarefree 数据产生。

## 7. 精度架构后果

Boolean squarefreeness pattern

\[
(\operatorname{sqfree}(a),\operatorname{sqfree}(b),\operatorname{sqfree}(c))
\]

远粗于完整 projective state，却能认证一个大型 exact safe basin：

\[
\boxed{
[c\text{ squarefree}]
\lor
[a,b\text{ squarefree}]
\Longrightarrow
A_{\rm proj}=0.
}
\]

只有离开这个 basin，进一步 projective precision 才可能有用。

于是形成新的 adaptive decision pipeline：

\[
\text{three squarefree bits}
\to
\text{projective activation bit}
\to
\text{dyadic projective levels}
\to
\text{full value if needed}.
\]

## 8. Prior-art discipline

Squarefree numbers 与 standard arithmetic derivative identities 都属于 prior mathematics。证明只使用初等不等式和 Stage-66 的 prior-art identity `U(n)=n'`。

项目侧结果只是 P025 projective activation query 的 exact squarefree-safe basin；历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_projective_squarefree_basin.py`；
- `tests/test_abc_projective_squarefree_basin.py`。

## 10. 下一前沿

Hard block 不存在。继续：

1. 当恰有两个 components nonsquarefree 时，分类下一层最粗 structural basin；
2. 检查 exponent-two / higher-power flags 在进入 full factor data 前还能消掉多少 activation states；
3. 将 pointwise safe basin 与 Stage-68 aggregate precision budget 合并；
4. 把 `cheap structural guard -> sparse expensive refinement` 模式回流 A2/P023。

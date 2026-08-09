# P025 补充 29 —— Shared-Prime Coupling 之后的 Certificate Rank Gain

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 27–28  
Hard block：`NONE`

## 1. Stage 27 必须先经过 prime-to-block map

补充 27 在 independent pairwise-coprime blocks 下给出 certificate precision-rank gain

\[
\operatorname{rank}[L;H]-\operatorname{rank}L.
\]

补充 28 已证明，shared primes 下 block values 先受 `B`——block-by-prime derivative coefficient matrix——约束。因此 relations 与 certificates 都必须先拉回 fine prime-coordinate domain。

Declared relations 变成

\[
LBx=0,
\]

block-linear certificates 变成

\[
HBx.
\]

## 2. P025-T82 —— exact shared-prime certificate rank gain

令

\[
K=\ker_{\mathbb Q}(LB).
\]

Certificate family 在 relation-adapted fine coordinates 上为

\[
HB|_K.
\]

与补充 27 同理，

\[
\boxed{
\Delta_H^{(B)}
=
\operatorname{rank}_{\mathbb Q}
\begin{pmatrix}
LB\\HB
\end{pmatrix}
-
\operatorname{rank}_{\mathbb Q}(LB).
}
\]

这就是 shared-prime coupling 与 declared relations 都已经施加以后，certificate family 真正可见的独立维数。

## 3. P025-T83 —— residual certificate-fiber rank

补充 28 给出 compressed relation-state rank

\[
\boxed{
r_{\rm comp}
=
\operatorname{rank}B-\operatorname{rank}(LB).}
\]

因此 exact certificate vector 尚未看见的 residual rank 为

\[
\boxed{
r_{\rm residual}
=
r_{\rm comp}-\Delta_H^{(B)}.}
\]

所以

\[
\boxed{0\le\Delta_H^{(B)}\le r_{\rm comp}.}
\]

无论 certificate 输出多少，都不可能恢复 prime coordinates 映入 `B` 时已经消失的 directions。

## 4. 恢复 Stage 27

当 non-unit blocks 两两互素时，`B` 的 active rows 有互不重叠 support 且 full row rank。对该 active row space，乘 `B` 保持相关 row-rank increments，因此

\[
\Delta_H^{(B)}
=
\operatorname{rank}[L;H]-\operatorname{rank}L,
\]

精确恢复补充 27。

所以 Stage 29 是严格推广，不是竞争公式。

## 5. Shared-prime example `2+4=6`

补充 28 给出

\[
B=
\begin{pmatrix}
1&0\\
4&0\\
3&2
\end{pmatrix},
\qquad
L=(1,1,-1),
\qquad
LB=(2,-2).
\]

Compressed relation-state rank 为

\[
2-1=1.
\]

取 certificate `t_2`，block row 为

\[
H=(1,0,0).
\]

则

\[
HB=(1,0),
\]

augmented derivative matrix rank 为 2，所以

\[
\boxed{\Delta_H^{(B)}=1.}
\]

这一个 certificate 已经 complete rank-one compressed state。

继续添加 `t_4`、`t_6` 或很多其他线性 outputs，都不能把 gain 提升到 1 以上。

## 6. P025-N11 —— Certificate outputs 无法逆转 shared-prime collapse

取 blocks `(4,8)`，不声明 relation。虽然 block outputs 有两个，但

\[
B=
\begin{pmatrix}4\\12\end{pmatrix}
\]

rank 只有 1，因为二者都依赖同一个 fine coordinate `x_2`。

即使 certificate family 报告**两个 exact block values**，

\[
H=I_2,
\]

仍有

\[
HB=B
\]

并因此

\[
\boxed{\Delta_H^{(B)}=1,}
\]

而不是 2。

关系

\[
t_8=3t_4
\]

是在 certificate language 出现之前，就由 shared prime-coordinate coupling 产生的。Exact outputs 可以暴露剩下的一个 direction，但不能重新创造一个从未存在于 `im B` 中的第二独立方向。

## 7. 在 derivative image 上恒零的 certificates

仍看 `(4,8)`。Block-linear certificate

\[
\ell(t_4,t_8)=-3t_4+t_8
\]

作为 formal block-space row 并不为零，但满足

\[
HB=0.
\]

所以

\[
\boxed{\Delta_H^{(B)}=0.}
\]

这是比“检查 `H` 是否属于 declared relations 的 row span”更强的 redundancy test：certificate 也可能因为在 prime-to-block image 上恒零而完全无信息。

## 8. 架构后果

完整 precision-rank accounting 顺序现在是

\[
\boxed{
\text{fine prime coordinates}
\xrightarrow{B}
\text{derivative image}
\xrightarrow{L}
\text{relation state}
\xrightarrow{H}
\text{certificate state}.
}
\]

Ranks 也按同样顺序扣减：

\[
\boxed{
\begin{aligned}
r_{\rm block}&=\operatorname{rank}B,\\
r_{\rm relation}&=\operatorname{rank}B-\operatorname{rank}(LB),\\
\Delta_H&=\operatorname{rank}[LB;HB]-\operatorname{rank}(LB),\\
r_{\rm residual}&=r_{\rm relation}-\Delta_H.
\end{aligned}}
\]

这防止一种常见架构错误：在 formal block space 中数 certificate rows，却忽略其中某些 directions 早已被 shared prime-coordinate structure 禁止。

## 9. Prior-art / ownership 边界

Restricted-map rank、stacked-matrix rank gain 与 image-kernel linear algebra 都是标准数学，P025 不主张创新。

项目侧新增候选是 overlapping arithmetic-derivative blocks 下的 corrected precision-accounting interface。它应 Relay 给 A3/P023，而不是保留成 abc 私有术语。

## 10. 可执行资产

新增：

- `src/enterprise_math/shared_prime_certificate_rank.py`
  - `HB` certificate pullback；
  - exact shared-prime rank gain；
  - residual rank 与 completeness flags。
- `tests/test_shared_prime_certificate_rank.py`
  - pairwise-coprime recovery；
  - `2+4=6` rank-one certificate completion；
  - relation-row redundancy；
  - `(4,8)` identity-output gain collapse；
  - certificate vanishing on `im B`。

## 11. 下一前沿

没有 hard block。继续：

1. 定义 shared-prime matrix image 的 exact joint preimage access costs；
2. 为这些成本寻找 finite HNF/SNF response summaries；
3. 把 rank-accounting stack 正式连接到 A3 relation-state precision；
4. 检验 rank gain + access cost 的 adaptive certificate-selection 价值，但保持 rank 与 proof cost 分离；
5. 在开启下一代数学前，冻结 Stage 18–29 generation 做 validation/Relay。

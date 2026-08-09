# P025 补充 28 —— Relation Rank 之前的 Shared-Prime Coupling

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 26–27  
Hard block：`NONE`

## 1. 为什么 pairwise coprimality 很重要

补充 26 假设 blocks 两两互素。在该假设下，不同 block 的 prime-coordinate supports 互不重叠，所以在施加 declared relation rows 之前，每个 block derivative value 可以独立选择。

若 blocks 共享 primes，这个 product structure 在 relation 之前就已经失效。同一个 prime-coordinate variable 会同时贡献给多个 block derivative values。

因此一般正确状态应由一张 block-by-prime coefficient matrix 控制。

## 2. P025-D16 —— derivative coefficient matrix

令正整数 blocks 为

\[
n_1,\ldots,n_m,
\]

不再假设互素。令

\[
p_1,\ldots,p_s
\]

为全部 prime supports 的并集。

定义

\[
\boxed{
B_{i,p}
=
\begin{cases}
\dfrac{n_i v_p(n_i)}p,&p\mid n_i,\\
0,&p\nmid n_i.
\end{cases}}
\]

对 fine prime-coordinate vector

\[
x\in\mathbb Z^s,
\]

block derivative-value vector 精确为

\[
\boxed{t=Bx.}
\]

所以即使还没有 relation constraint，joint block-value image 也只是

\[
\boxed{\Gamma_B=\operatorname{im}_{\mathbb Z}B,}
\]

而一般不是各 separate row ideals 的 Cartesian product。

## 3. P025-T80 —— exact shared-prime relation state

令 declared integer block relations 为

\[
Ln=0.
\]

Derivative linearity 要求

\[
Lt=LBx=0.
\]

所以 relation-adapted fine coordinates 为

\[
\ker_{\mathbb Z}(LB),
\]

而其 exact compressed derivative-value image 为

\[
\boxed{
\Lambda_{B,L}
=
B(\ker_{\mathbb Z}(LB)).
}
\]

等价地，

\[
\boxed{
\Lambda_{B,L}
=
\operatorname{im}_{\mathbb Z}B
\cap
\ker_{\mathbb Z}L.
}
\]

### 交集恒等式证明

任意 `Bx` 若满足 `LBx=0`，显然同时落在两个集合中。

反之，若 `t` 属于 `im_Z B` 且 `Lt=0`，取整数 `x` 使 `Bx=t`。则

\[
LBx=Lt=0,
\]

故 `x` 是 relation-adapted，`t` 落在 `B(ker_Z LB)` 中。∎

## 4. P025-T81 —— 一般 rational rank formula

考虑 restricted map

\[
B:\ker_{\mathbb Q}(LB)\to\mathbb Q^m.
\]

其 kernel 恰好为

\[
\ker_{\mathbb Q}B,
\]

因为 `ker B` 自动包含在 `ker LB` 中。

所以 rank-nullity 给出

\[
\begin{aligned}
\operatorname{rank}_{\mathbb Q}\Lambda_{B,L}
&=
\dim\ker(LB)-\dim\ker B\\
&=
(s-\operatorname{rank}LB)-(s-\operatorname{rank}B).
\end{aligned}
\]

因此

\[
\boxed{
\operatorname{rank}_{\mathbb Q}\Lambda_{B,L}
=
\operatorname{rank}_{\mathbb Q}B
-
\operatorname{rank}_{\mathbb Q}(LB).
}
\]

这就是 shared-prime 情形对补充 26

\[
\text{active block count}-\text{relation rank}
\]

的正确替代。

## 5. 恢复 pairwise-coprime 秩律

若 non-unit blocks 两两互素，则 `B` 的非零 rows 有互不重叠的 prime-coordinate supports，因此这些 rows rationally independent，

\[
\operatorname{rank}B=s_{\rm blocks},
\]

即 active block count。

而且 disjoint-support matrix 在 active rows 上拥有 rational right inverse，所以乘 `B` 不改变 restricted relation matrix 的 row rank：

\[
\operatorname{rank}(LB)=\operatorname{rank}L_I.
\]

因此 P025-T81 精确退化为

\[
\boxed{
\operatorname{rank}\Lambda
=s_{\rm blocks}-\operatorname{rank}L_I,
}
\]

恢复补充 26。

## 6. P025-N10 —— Separate block image ideals 会制造假状态

考虑

\[
\boxed{2+4=6.}
\]

union prime coordinates 为 `(2,3)`，derivative matrix 是

\[
\boxed{
B=
\begin{pmatrix}
1&0\\
4&0\\
3&2
\end{pmatrix}.
}
\]

Declared relation row 为

\[
L=(1,1,-1),
\]

所以

\[
\boxed{LB=(2,-2).}
\]

Fine relation condition 因而是

\[
x_2=x_3,
\]

compressed states 为

\[
\boxed{(t_2,t_4,t_6)=t(1,4,5).}
\]

Ranks 为

\[
\operatorname{rank}B=2,
\qquad
\operatorname{rank}(LB)=1,
\]

所以 compressed relation state rank 为 1。

现在只看 separate block ideals：

\[
A(2)=1,
\qquad
A(4)=4,
\qquad
A(6)=1.
\]

向量

\[
\boxed{(0,4,4)}
\]

通过了 naive tests：

- 每个 component 都落在自己的 separate block image ideal；
- 同时满足 `0+4=4`。

但它 joint-impossible。第一 derivative value 就是 `x_2`，所以 `t_2=0` 强迫 `x_2=0`；于是 `t_4=4x_2=0`，与 `t_4=4` 矛盾。

因此 shared-prime 情形可以严格有

\[
\boxed{
\left(\prod_i A_i\mathbb Z\right)\cap\ker L
\supsetneq
\operatorname{im}_{\mathbb Z}B\cap\ker L.
}
\]

这给出任何试图把 independent-block access calculus 无条件推广出 coprime scope 的精确 negative boundary。

## 7. 即使没有 declared relation，共享 prime 也可先降 rank

取 blocks

\[
(4,8).
\]

只有一个 prime coordinate `2`，并且

\[
B=
\begin{pmatrix}4\\12\end{pmatrix}.
\]

因此

\[
\boxed{\operatorname{rank}B=1}
\]

尽管有两个 non-unit blocks。

所以 shared-prime coupling 本身就在 external relation language 之前形成了 block-values 之间的隐藏约束。

## 8. 架构后果

一般 dimension pipeline 现在是

\[
\boxed{
\text{fine prime coordinates }x
\xrightarrow{B}
\operatorname{im}B
\xrightarrow{L}
\operatorname{im}B\cap\ker L.
}
\]

两种独立 collapse 来源为：

1. **shared-coordinate coupling：**`rank B` 可能已经小于 block count；
2. **declared relations：**`rank(LB)` 继续删除方向。

所以 exact global relation-state rank 为

\[
\boxed{
\text{prime-to-block image rank}
-
\text{relation rank visible on that image}.
}
\]

这比补充 26 更一般，也明确指出其 pairwise-coprime product assumption 的真实位置。

## 9. Access-cost 边界

Supports 互不重叠时，固定 block-value state 的 exact fine cost 为

\[
\max_i\kappa_{n_i}(t_i)
\]

因为可以独立选择每个 block 的 optimal preimage。

Shared primes 下这一公式一般失败：separate optimal preimages 可能对同一个 prime coordinate 给出互不兼容的值。此时正确的 preimage-cost problem 是 joint：

\[
\boxed{\min\{\|x\|_\infty:Bx=t\}.}
\]

所以补充 20–24 在其 pairwise-coprime abc scope 内仍然 exact；Stage 28 给出超出该 scope 时的正确 replacement object，而不是偷偷扩大旧公式。

## 10. Prior-art 边界

Integer matrix images、restricted linear-map rank、kernel/image intersection identities 与 coupled linear preimage problems 都属于标准 linear algebra/module theory。

P025 不对这些一般数学作创新主张。项目侧新增的是：当 block supports 重叠时，对 relation-conditioned precision architecture 的精确修正。

这天然应 Relay 给 A3/P023，而不是静默升级为 P025 私有术语。

## 11. 可执行资产

新增：

- `src/enterprise_math/relation_shared_prime_rank.py`
  - union-prime derivative coefficient matrix；
  - relation-derivative matrix `LB`；
  - exact rank formula；
  - fine coordinate evaluation/relation check；
  - naive separate-ideal test 与显式 false-state counterexample。
- `tests/test_relation_shared_prime_rank.py`
  - `2+4=6` rank-one shared-prime state；
  - pairwise-coprime recovery of Stage 26；
  - no-relation shared-prime rank loss；
  - false separate-ideal state `(0,4,4)`；
  - mixed-exponent calibration。

## 12. 下一前沿

没有 hard block。继续：

1. 定义 shared-prime system 的 exact joint access function `kappa_B(t)=min{||x||∞:Bx=t}`；
2. 为该 matrix-preimage cost 寻找类似 disjoint-block Apéry/capacity profile 的有限 precision summaries；
3. 把 certificate rank gain 从 `L` 推广到一般 `im B` restricted form；
4. 检验 Smith/HNF normal forms 是否给 practical exact shared-prime access solvers；
5. 把 corrected rank law 与 false-product counterexample Relay 给 A3/P023。

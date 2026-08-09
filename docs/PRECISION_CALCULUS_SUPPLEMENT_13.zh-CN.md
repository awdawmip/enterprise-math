# 精度演算 — 补充 13

状态：`ACTIVE RESEARCH NOTE`  
范围：P018-T110 之后的 quotient-path 平坦性与严格平方根尺度下降  
依赖：P018-T110、P007 离散除法，以及自然数 quotient 的规范恒等式 `Nat.div_div_eq_div_mul`  
纪律：floor division 的复合恒等式属于成熟算术，**不**声称为项目新数学。项目专门内容，是把该恒等式与 T110 结合以消除多步 root 分支的表面爆炸，并进一步得到平方盆地上的严格下降结论。

## 1. 为什么 T110 不会产生二叉树式爆炸

T110 说明，一个平方盆地经过一次非平凡 quotient 后，最多只会碰到两个相邻 square-root indices。

如果机械递归理解，似乎经过 `h` 次连续因子提取后，最终可能出现 `2^h` 个 root-index 候选。

这个判断在 quotient state 层面已经是错的。

自然数 floor division 满足

\[
\boxed{
\left\lfloor
\frac{\left\lfloor n/a\right\rfloor}{b}
\right\rfloor
=
\left\lfloor\frac{n}{ab}\right\rfloor.
}
\]

这是标准 Euclidean quotient 恒等式，在 mathlib 中形式化为 `Nat.div_div_eq_div_mul`，属于成熟数学。

它在这里的意义是结构性的：一串 quotient 操作有一个精确的一步代表，即除以所有 divisor 的乘积。

---

## 2. P018-T111 — Quotient-path 平坦性

状态：`PROVED / CLASSICAL QUOTIENT IDENTITY + PROJECT CONSEQUENCE`。

对任意自然数 `n,a,b`，

\[
\boxed{
Q_b(Q_a(n))=Q_{ab}(n),
}
\]

其中 `Q_d(n)=floor(n/d)`。

通过归纳，对任意有限非零 divisor 序列

\[
d_1,\ldots,d_h,
\]

都有

\[
\boxed{
Q_{d_h}\circ\cdots\circ Q_{d_1}
=
Q_{d_1\cdots d_h}.
}
\]

这个恒等式本身属于前人算术；P018 的新增后果来自把它与 T110 结合。

设

\[
k^2\le n<(k+1)^2,
\qquad a,b\ge2,
\]

并令

\[
D=ab,
\qquad
j=R_2\!\left(\left\lfloor\frac{k^2}{D}\right\rfloor\right).
\]

则

\[
\boxed{
R_2\!\left(
\left\lfloor
\frac{\left\lfloor n/a\right\rfloor}{b}
\right\rfloor
\right)
\in\{j,j+1\}.
}
\]

因此两步 quotient **不会**产生四个最终 root-index 分支。两步先精确压平为一次除以 `ab`，再只需对总除数应用一次 T110。

同理，任意有限 quotient path 的最终 quotient state 只取决于总乘积 divisor，所以最终 square-root image 仍然只由一次 T110 的二盆地界控制。

这里并不声称不同因式分解下的中间状态都相同；结论只是在总除数固定时，最终 quotient projection 对 divisor 的因式分解是平坦的。

---

## 3. P018-T112 — k >= 3 时实际 quotient root 严格下降

状态：`PROVED`。

T110 给出 base root `j<k`，但形式上仍允许实际 quotient root 为 `j+1`；理论上存在 `j+1=k` 的边缘可能。

从 `k>=3` 开始，这种边缘情况实际上不会发生。

设

\[
k\ge3,
\qquad d\ge2,
\qquad n<(k+1)^2.
\]

则

\[
(k+1)^2\le2k^2\le dk^2.
\]

所以

\[
n<dk^2,
\]

由精确 floor division 得到

\[
\left\lfloor\frac nd\right\rfloor<k^2.
\]

因此

\[
\boxed{
R_2\!\left(\left\lfloor\frac nd\right\rfloor\right)<k.
}
\]

这是**实际运输后状态**的严格下降，而不只是 T110 的 base index 严格下降。

`k=1,2` 只是有限基例，不需要渐近或递归处理。

---

## 4. 合并后的良基 quotient 骨架

T110–T112 现在给出一个很紧凑的 operation-level 图景。

对任意 `k>=3` 的平方盆地，以及任意非平凡 divisor `d>=2`：

1. quotient transport 完全精确且只用整数；
2. 整个盆地最多碰到两个相邻目标 root indices；
3. 实际目标 root index 严格小于 `k`；
4. 把 `d` 拆成多步 quotient 不会放大最终 root-index 候选数，因为多步可以精确压平成一次总乘积 quotient。

符号上：

\[
\boxed{
B_k
\xrightarrow{Q_{d_1}}
\cdots
\xrightarrow{Q_{d_h}}
Q_D(B_k),
\qquad
D=\prod_i d_i,
}
\]

并且对 `k>=3` 的实际最终状态，

\[
\boxed{
Q_D(B_k)
\text{最多碰到两个相邻 root indices，且实际最终 root 小于 }k.
}
\]

重点不是“除法让数变小”这么粗糙，而是：square-root precision coordinate 形成了**良基下降**，同时 quotient factorization 在最终状态上又是平坦的。

---

## 5. 对 P017 lower band 的含义

回到平方盆地中的 composite state

\[
n=pq,
\]

其中 `p` 是最小素因子。

T110 给出

\[
j=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right),
\qquad
R_2(q)\in\{j,j+1\}.
\]

若 `k>=3`，T112 进一步给出

\[
\boxed{R_2(q)<k.}
\]

如果 `q` 仍是 composite，记它的最小素因子为 `ell`，则在下降后的状态上应用普通 root-factor horizon：

\[
\ell\le R_2(q).
\]

又因为 `p` 是原状态 `n` 的最小素因子，必有 `p<=ell`。因此

\[
\boxed{
p\le\ell\le R_2(q)<k.
}
\]

于是 least-factor extraction 会同时降低 root scale，并缩窄下一最小素因子的可用区间。

这就是回到 P017 lower band 的预定桥梁。但它仍然不是 Legendre 证明：下一步必须从这个缩小的状态空间中推导有用的递归**质量上界**，而不是简单枚举递归分支。

---

## 6. 什么不是新数学，什么是项目专门内容

不声称为新数学：

- Euclidean floor division；
- `floor(floor(n/a)/b)=floor(n/(ab))`；
- `Nat.div_div_eq_div_mul` 及其形式化；
- 一般自然数良基归纳。

项目正在检验的专门内容：

- 用 quotient-path 平坦性证明反复 T110 transport 不会造成指数级最终 root-scale 分支；
- T112 的精确平方盆地严格 root descent；
- 把这种下降与 P017 lower band 的 least-factor horizon 耦合。

历史创新状态仍为 `NOVELTY_UNVERIFIED`。

---

## 7. 可执行与形式化核验

Python 层在 `src/enterprise_math/quotient_basin.py` 中新增：

- `iterated_quotient_flatness`；
- `square_basin_iterated_quotient_transport`；
- `strict_square_root_descent`。

测试验证有限范围内的多步路径、与因式分解无关的最终 quotient、保留的二 root 界，以及 `k>=3` 的严格下降。

Lean 模块 `EnterpriseMath.Precision.QuotientBasin` 新增：

- `quotient_path_flat_two`；
- `square_basin_two_step_div_root_pair`；
- `square_basin_div_root_strict`。

形式化层有意只证明最小的两步路径恒等式及其 T110 后果。更长路径由普通归纳得到，除非后续应用确实需要，否则不扩成冗余 theorem family。

---

## 8. 下一目标

下一步真正有意义的问题已经不是证明 lower-band factor extraction 会下降；T110–T112 已经提供了这个骨架。

剩余问题是定量的：

> 能否把不断缩小的 root scale 和不断缩小的可用 least-factor 区间，转化为一个关于 lower-band composite mass 的递归上界，而且这个上界必须真正强于标准 Buchstab / least-factor bookkeeping？

任何候选递归都必须与成熟 sieve theory 压力测试。若最终只是在 square-root 坐标中重写普通 least-factor recursion，就应降级，而不是继续膨胀路线。

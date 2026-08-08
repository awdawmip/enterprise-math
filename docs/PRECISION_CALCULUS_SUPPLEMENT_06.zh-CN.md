# P018 —— 有限精度证明演算：补充 06

状态：`ACTIVE RESEARCH NOTE`  
范围：P017 factor precision 的 proof-relevant compression，以及平方盆地最小 survivor-prime horizon  
依赖：P017 Root-Factor Horizon 与 P018 第四至第六阶段  
纪律：素数筛、最小素因子、半素数分解都是经典数学；本文不证明 Legendre 猜想。

## 1. 完整 factor information 多于 primality 真正需要的信息

第四阶段使用 factor-precision state：

\[
D_y(n)=\{p\le y:p\text{ 为素数},\ p\mid n\}.
\]

它构成合法的相容 precision system：增大 `y` 会增加可能出现的 factor witness；投影回较低 cutoff，只需遗忘高于 cutoff 的 witness。

但对 Boolean predicate“`n` 是否为素数”来说，一旦已经发现合数 witness，就没有必要继续保留所有 visible factors 的身份。

所以第七阶段首先问：

> factor precision 可以压缩到什么程度而不损失 primality proof power？哪些压缩还能在不同 cutoff 之间保持合法的 precision-system projection？

## 2. P018-T55 —— Least-witness factor precision 保持 projective compatibility

状态：`PROVED`

定义

\[
\ell_y(n)=
\begin{cases}
0,&D_y(n)=\varnothing,\\
\min D_y(n),&D_y(n)\ne\varnothing.
\end{cases}
\]

即 `ell_y(n)` 只记录当前已发现的最小 tested factor。

对 `a<=b`，定义投影

\[
q_{b\to a}(s)=
\begin{cases}
s,&0<s\le a,\\
0,&s=0\text{ 或 }s>a.
\end{cases}
\]

则

\[
\boxed{
\ell_a(n)=q_{b\to a}(\ell_b(n)).
}
\]

证明：若 `n` 的最小素因子不超过 `a`，两个 level 都看到同一个最小 factor；若最小素因子位于 `(a,b]`，fine level 记录它、projection 把它抹去；若 cutoff `b` 内仍没有 factor，则两个 level 都为 0。∎

因此 least-witness state 本身形成一条相容有限 precision chain。

## 3. P018-T56 —— Least-witness compression 不损失任何 primality proof power

状态：`PROVED`

固定平方盆地 `I_k` 与 cutoff `y<=k`。

完整 observation `D_y` refine least-witness observation `ell_y`，因为 `ell_y` 是 `D_y` 的确定性函数。

然而对 primality predicate，两者在每个状态上的 conflict multiplicity 完全一致：

\[
\boxed{
C_{D_y,\mathrm{prime}}(n)
=
C_{\ell_y,\mathrm{prime}}(n).
}
\]

分两种情况：

- 若 cutoff `y` 内没有 factor，`D_y(n)=empty` 且 `ell_y(n)=0`，两个 fiber 完全相同，都是 survivor set `S_y(k)`；
- 若已经出现 factor，则 full-factor fiber 与 least-witness fiber 都只包含合数，因此 primality-conflict multiplicity 都为 0。

所以额外 visible factor 的精确身份可以继续降低 **state ambiguity**，却不会继续降低 **primality conflict**。

最小 visible witness 是 full factor precision 针对 primality 的 proof-sufficient compression。

## 4. P018-T57 —— One-bit factor compression 单层 proof-sufficient，但通常不能组成 precision chain

状态：`PROVED + COUNTEREXAMPLE`。

定义单 bit：

\[
b_y(n)=\mathbf1_{D_y(n)\ne\varnothing}.
\]

在一个固定 cutoff 上，这一 bit 与 `D_y`、`ell_y` 拥有完全相同的 primality conflict multiplicity：

- `b_y=1` 的 fiber 全部是 composite；
- `b_y=0` 的 fiber 正好就是 survivor fiber `S_y(k)`。

所以该 bit 在**单个 precision level** 上对 primality 已经 proof sufficient。

但不同 cutoff 的 bit observation 一般不能组成相容 precision chain。

取 terminal states `2` 与 `3`，cutoff 为 `2<3`。

在 cutoff `3`，两个状态的 bit 都是 `1`；而在 cutoff `2`，对应 bit 分别为 `1` 与 `0`。

因此不存在从 high-cutoff bit 到 low-cutoff bit 的确定性 projection。

所以

\[
\boxed{
\text{每一层都 proof-sufficient 的 compression}
\not\Rightarrow
\text{跨层仍是 precision-system-compatible compression}.
}
\]

这给出 P018 一个重要设计约束：可用的 precision coordinate 不仅要保留目标 proof information，还要保留 calculus 所需的 inter-level forgetting maps。

## 5. 最小 survivor-prime horizon

对开放平方盆地

\[
I_k=\{k^2+1,\ldots,(k+1)^2-1\},
\]

定义

\[
\boxed{
H(k)=
\max\{\operatorname{spf}(n):n\in I_k,\ n\text{ 为合数}\},
}
\]

如果盆地没有合数，则约定 `H(k)=0`。

它与 universal Root-Factor Horizon `k` 不是同一个对象。

`k` 是已经通过定理知道的 universal cutoff；`H(k)` 则是这个具体盆地中，恰好足以排除所有合数的最小 cutoff。

## 6. P018-T58 —— Survivor-prime horizon 的精确最小性

状态：`PROVED`

令 `S_y(k)` 表示 `I_k` 中没有任何素因子不超过 `y` 的状态。

则

\[
\boxed{
S_y(k)\subseteq\{\text{primes}\}
\iff
y\ge H(k).
}
\]

证明：

- 若 `y>=H(k)`，每个合数的最小素因子都不超过 `H(k)<=y`，所以所有合数都已被排除；
- 若 `y<H(k)`，取最小素因子等于 `H(k)` 的合数，它在 cutoff `y` 下仍然 survive，因此 survivor set 不可能全为素数。∎

所以 `H(k)` 正是如下性质成立的最小 factor precision：**对盆地中任何 remaining state，“没有 visible factor”已经是 sound prime certificate。**

## 7. P018-T59 —— Root horizon 上界与 last-shell 刻画

状态：`PROVED`

P017 Root-Factor Horizon 保证每个 `n in I_k` 的合数都有一个不超过 `k` 的素因子，因此

\[
\boxed{H(k)\le k.}
\]

令 `L_p(k)` 为第四阶段 first-factor shell，即盆地中最小素因子为 `p` 的状态。

则

\[
\boxed{
H(k)=\max\{p\le k:L_p(k)\ne\varnothing\},
}
\]

若没有任何 composite shell，则值取 0。

因此最小 primality-certifying factor horizon，恰好就是最后一个非空 composite first-decision shell 的 index。

定义 **factor proof slack**：

\[
\boxed{
\sigma(k)=k-H(k)\ge0.
}
\]

universal root horizon 中可能有 `sigma(k)` 单位的 factor precision，对这个具体盆地实际上并不需要。

## 8. P018-T60 —— 最小 horizon 上的 prime survivor identity

状态：`PROVED`

在 `y=H(k)` 时，所有 composite 都已经退出；prime 因为在任何不超过 `k` 的 cutoff 上都没有 factor，所以全部仍然 survive。

因此

\[
\boxed{
S_{H(k)}(k)
=
\{n\in I_k:n\text{ 为素数}\}.
}
\]

从而

\[
\boxed{
\Pi(k)=|S_{H(k)}(k)|.
}
\]

更一般地，任何 `B>=H(k)` 的 cutoff，在到达 universal terminal cutoff `k` 之前，都拥有相同的 prime-only survivor set。

### 非循环边界

`H(k)` 是通过“哪些盆地状态为 composite”定义出来的。因此上式只是结构定理，**不能单独作为 Legendre 猜想的证明捷径**。

若要真正产生证明杠杆，必须在没有预先分类盆地 primes/composites 的情况下，独立证明显式上界

\[
H(k)\le B(k).
\]

这样 Legendre 在 `k` 处才会被降成只需证明

\[
S_{B(k)}(k)\ne\varnothing.
\]

现有 universal 选择是 `B(k)=k`。若能独立证明真正更小的 `B(k)`，才构成新的 factor-precision 杠杆。

## 9. P018-T61 —— 固定平方盆地内，square-root observation 对 primality 本身是 inert 的

状态：`PROVED`。

对所有 `n in I_k`：

\[
R_2(n)=k.
\]

所以 observation

\[
n\mapsto R_2(n)
\]

在整个 P017 terminal set `I_k` 上是常值。

它诱导的 precision partition 就是单 block partition，与完全无信息的 observation 相同。

因此，单独看 square-root coordinate，它在固定盆地内部拥有

\[
\boxed{
\text{zero ambiguity gain and zero primality-conflict gain}.
}
\]

P017 中 root coordinate 的价值并不是区分盆地内部状态；它的价值是**结构性的**：给出有限 factor-completeness horizon `p<=k`，并组织其他 precision axes 之间的关系。

这明确区分了“coordinate information”与“由该 coordinate 启用的 theorem”。

## 10. P018-T62 —— 高 first-factor shell 是 semiprime shell

状态：`PROVED`。

令

\[
U=(k+1)^2-1
\]

为开放盆地最大状态，取素数 `p<=k` 满足

\[
\boxed{p>R_3(U).}
\]

等价于 `p^3>U`。

若 `n in L_p(k)`，则 `spf(n)=p`。若 `n` 至少含三个按重数计的素因子，那么每个都至少为 `p`，于是

\[
n\ge p^3>U,
\]

矛盾。

因此 `n` 恰好只有两个按重数计的素因子。又因为 `p<=k` 给出 `p^2<=k^2<n`，第二个因子不可能等于 `p`。

所以 shell 中每个状态都具有

\[
\boxed{
n=pq,
\qquad q\text{ 为素数},
\qquad q>p.
}
\]

因此在 cube-root threshold 以上，factor-precision shell 不再是一般 rough-composite shell，而是精确的 semiprime-pair shell。

特别地，若 horizon 自身满足

\[
H(k)>R_3(U),
\]

则最后一个非空 composite precision shell 完全由 `H(k)q` 形式的 semiprime 构成，其中 `q>H(k)` 为素数。

这把 proof-horizon 问题连接到平方边界附近一个狭窄的 prime-pair geometry。

## 11. 第七阶段在概念上改变了什么

factor axis 现在出现三种不同状态表示：

1. full witness set `D_y` —— state information 最丰富；
2. least witness `ell_y` —— state information 更少，但 primality proof power 完全相同，并且保持 compatible projection；
3. one-bit witness `b_y` —— 单层 primality proof power 仍相同，但一般破坏跨 precision level 的 compatibility。

由此得到 P018 的一般教训：

> 最好的 precision representation 既不一定是信息最丰富的，也不一定是每层最小的 certificate。它必须同时保留真正 proof-relevant 的信息，和 calculus 所需要的 inter-level transition structure。

horizon `H(k)` 还给出第二个教训：

> universal precision bound 与某一个有限问题实际所需的 minimal precision，是两个不同数学对象。

这正是第六阶段 adaptive precision selection 的直接基础。

## 12. 前人工作与创新边界

trial division、smallest-prime-factor sieve、rough number 与 semiprime factorization 都是经典数学。把 divisibility record 压缩成 least witness 也不被声称为历史创新。

当前真正要检验的是这些基本事实与 P018 proof calculus 的组合：

\[
\boxed{
\text{proof-sufficient factor compression}
+
\text{projection compatibility}
+
\text{minimal survivor-prime horizon}
+
\text{first-decision shells}
+
\text{adaptive proof precision}.
}
\]

历史创新状态仍为 `NOVELTY_UNVERIFIED`。

本文没有证明 `S_(H(k))(k)` 对所有 `k` 都非空；这正是 Legendre existence issue 在 minimal semantic factor horizon 上的表达。

## 13. 第七阶段状态

- P018-T55 least-witness projective compatibility：`PROVED`
- P018-T56 least-witness 与 full factor state 的 primality-proof equivalence：`PROVED`
- P018-T57 one-bit proof sufficiency / projective incompatibility：`PROVED + COUNTEREXAMPLE`
- P018-T58 minimal survivor-prime horizon criterion：`PROVED`
- P018-T59 `H(k)<=k` 与 last-shell characterization：`PROVED`
- P018-T60 `H(k)` 上的 prime survivor identity 与 non-circularity boundary：`PROVED`
- P018-T61 固定平方盆地内 square-root observation 对 state/proof inert：`PROVED`
- P018-T62 high factor shell semiprime theorem：`PROVED`
- 独立非平凡上界 `H(k)<=B(k)<k`：`OPEN / HIGH PRIORITY`
- 证明 `S_(H(k))(k)` 永远非空：`OPEN / EQUIVALENT EXISTENCE TARGET`
- factor precision 之外的 adaptive multi-axis P017 proof cost：`OPEN`

可执行检查位于 `src/enterprise_math/p017_precision_horizon.py` 与 `tests/test_p017_precision_horizon.py`。

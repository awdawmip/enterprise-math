# 精度演算 — 补充 14

状态：`ACTIVE RESEARCH NOTE`  
范围：T110 二盆地像内部的精确单阈值响应，以及多个 quotient divisor 之间的共享 offset coherence  
依赖：P018-T110–T112、T007 整数根、P007 离散除法  
纪律：阈值比较和 floor division 序关系属于成熟初等算术。项目专门内容，是平方盆地上的精确响应律，以及把它作为后续跨尺度论证中的共同 offset coherence 层。

## 1. 二盆地陈述还缺少什么

T110 已证明：若

\[
k^2\le n<(k+1)^2,
\qquad d\ge2,
\]

并定义

\[
j_d=R_2\!\left(\left\lfloor\frac{k^2}{d}\right\rfloor\right),
\]

则 quotient root 只能是

\[
j_d\quad\text{或}\quad j_d+1.
\]

这已经是很强的有限像定理，但还没有说明两个值究竟在什么位置切换。

这个切换实际上是精确的，而且只发生一次。

---

## 2. P018-T113 — 精确 quotient-root 切换阈值

状态：`PROVED`，并已进入 Lean 形式化。

在 T110 的条件下，

\[
\boxed{
R_2\!\left(\left\lfloor\frac nd\right\rfloor\right)=j_d+1
\iff
d(j_d+1)^2\le n.
}
\]

等价地说，在到达这个 state threshold 之前，root 恰好处于下侧分支。

### 证明

T110 已经把 quotient root 限定在 `j_d` 或 `j_d+1`。

达到上侧值，当且仅当

\[
(j_d+1)^2
\le
\left\lfloor\frac nd\right\rfloor.
\]

利用自然数 floor division 的精确序伴随关系，这又等价于

\[
d(j_d+1)^2\le n.
\]

没有使用任何近似。∎

Lean 定理为

`EnterpriseMath.Precision.square_basin_div_upper_root_iff`。

---

## 3. Offset 形式

把盆地状态写成

\[
n=k^2+s,
\qquad 0\le s\le2k.
\]

定义正的 offset threshold

\[
\boxed{
\tau_d
=d(j_d+1)^2-k^2.
}
\]

其正性来自 `j_d` 定义中的严格上界

\[
\left\lfloor\frac{k^2}{d}\right\rfloor<(j_d+1)^2.
\]

于是 T113 变成

\[
\boxed{
R_2\!\left(\left\lfloor\frac{k^2+s}{d}\right\rfloor\right)
=j_d+\mathbf1[s\ge\tau_d].
}
\]

如果 `tau_d>2k`，那么整个盆地内都永远不会进入上侧分支。

因此 quotient-root response 在有限 basin offset 上就是一个真正的单跳变阶跃函数。

---

## 4. 多个 divisor 的共享 offset coherence

固定

\[
d_1,\ldots,d_h\ge2.
\]

对每个 `d_i` 定义 T113 上侧 bit

\[
\varepsilon_i(s)
=
\mathbf1[s\ge\tau_{d_i}].
\]

所有坐标都由**同一个** offset `s` 驱动。

所以向量

\[
\boxed{
\varepsilon(s)
=(\varepsilon_1(s),\ldots,\varepsilon_h(s))
}
\]

并不是 `{0,1}^h` 中任意独立的 bit 组合。

随着 `s` 在有限盆地中增加，一个坐标只可能在跨过自己的 threshold 时翻转一次。把不同 thresholds 排序以后，相邻 threshold 之间向量保持不变。因此

\[
\boxed{
\#\{\varepsilon(s):0\le s\le2k\}
\le h+1.
}
\]

而朴素独立 bit 计数会给出 `2^h`。

它与 T111 从不同方向加强结构：

- T111 说明固定总除数时，**最终 quotient state** 与因式分解路径无关；
- T113 说明即使同时观察不同 divisor 的多个 quotient-root 分支 bit，它们也被一个共同 state coordinate 约束。

Python 参考实现会直接检验这个有限模式数上界。

---

## 5. 整除条件与大模数相变

如果 divisor `D` 还实际整除盆地状态

\[
n=k^2+s,
\]

则

\[
\boxed{s\equiv-k^2\pmod D.}
\]

当

\[
D>2k
\]

时，允许的 offset 区间长度只有 `2k+1`，因此满足该同余的正 interior offset 至多一个。

这只是 P017 已使用的大模数唯一命中现象在下平方边界坐标中的表达。T113 并不另起竞争性 large-hit 机制；它只是给同一个有限状态增加 quotient-root response 坐标。

---

## 6. Mirror 坐标

对中心平方盆地 mirror decomposition，

\[
M=k(k+1),
\qquad
M-r,\ M+r,
\qquad 1\le r<k,
\]

相对于 `k^2` 的 offsets 恰好为

\[
\boxed{s_-=k-r,\qquad s_+=k+r.}
\]

若 divisor `p` 作用于下侧 mirror state，它的 T113 上侧 root bit 为

\[
\boxed{
\varepsilon_p^-(r)
=\mathbf1[k-r\ge\tau_p]
=\mathbf1[r\le k-\tau_p].
}
\]

上侧 divisor `q` 则满足

\[
\boxed{
\varepsilon_q^+(r)
=\mathbf1[k+r\ge\tau_q]
=\mathbf1[r\ge\tau_q-k].
}
\]

所以 quotient-root branch selection 被转化成一个**有界 radius 半区间条件**，可以直接与现有 mirror CRT progression 求交。

这正是与 P017 mirror-certificate 路线连接的接口：least-factor / second-factor 约束以后可以同时使用

1. radius 的 CRT residue class；
2. 精确 quotient-root threshold interval。

二者都不是概率条件。

---

## 7. 对 P017 lower band 的解释

若

\[
n=pq
\]

是平方盆地中的 composite，且 `p` 是最小素因子，T110–T112 已说明 cofactor root 会下降；T113 再给出精确 branch selector：

\[
R_2(q)
=j_p+\mathbf1[n\ge p(j_p+1)^2].
\]

如果 `q` 仍是 composite，它的下一最小素因子就被这个精确下降 root 截断。

因此下一因子 cutoff 不必总取粗糙的 `j_p+1`，而是可以根据单次整数阈值比较逐状态确定为 `j_p` 或 `j_p+1`。

这可能用于 least-factor-gated mirror capacity，因为 mirror radius 已经精确决定了 basin offset。

---

## 8. 可执行核验

Python 层在 `src/enterprise_math/quotient_basin.py` 新增：

- `quotient_root_threshold`；
- `square_basin_offset_root_response`；
- `quotient_root_threshold_pattern`。

测试检查：

- threshold 始终位于下平方边界之上；
- 有限完整盆地中 root response 恰等于 `base_root + 1[offset>=tau]`；
- 有些 threshold 落在盆地内，有些超过整个盆地；
- 对固定 `h` 个 divisors，观察到的 bit-vector family 大小至多为 `h+1`。

Lean 层形式化 exact upper-branch equivalence；有限 bit-vector pattern 结论只是 threshold 排序的初等推论，除非后续证明确实需要 typed finite-set theorem，否则暂保留在文档/参考测试层。

---

## 9. 下一目标

T110–T113 已经把当前 lower-band 路线需要的 quotient transport operation-level 几何压得足够紧：

- 严格下降；
- 无因式分解路径爆炸；
- 精确单阈值 branch response；
- 共享 offset coherence。

所以下一个真正有用的定理应当是**跨 shell**，而不是继续增加 quotient identity。

当前最强的 P017 候选，是 lower-band root-target overlap bound：在满足 `p^2<2k` 的 least primes 中，每个下降后的 root index 最多只会出现在两个不同 least-prime shells 的 T110 candidate pair 中。

如果能证明，那么每个 lower square-root scale 只接收常数个 shell channels，这正是递归 composite-mass 论证所需要的结构类型。

# Legendre 压力测试 — 补充 20

状态：`PROVED RESEARCH NOTE`  
范围：完整 lower-band actual-root collision 分类，以及最小 shell-repair alphabet  
依赖：P017 L054–L055、P023-S8 image separation、P023-S9 task-refinement repair calculus  
纪律：本补充证明的是 square-basin lower-band shell structure，不声称证明 Legendre 猜想。

## 1. 从“最终不碰撞”继续追问

L055 已证明 `k>=9` 时，不同 lower-band least-prime shells 的实际 root images 两两不交；它还给出 bounded audit：较小 `k` 中只看见 `k=5,6,8` 三次真实碰撞，全部来自 `p=2,r=3`。

重新检查 L055 的普通证明可见：对 `r>=5` 的排除没有使用 `k>=9`；对 `(p,r)=(2,3)` 排除 `s>=8` 也没有使用 `k>=9`；`k>=9` 只在最后把剩余小范围截成 `9,10,11` 时使用。

因此 L055 的证明实际上已经几乎包含一个更强的完整碰撞分类定理。

## 2. 记号

仍令

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right]
\]

为 prime `p` 的 exact cofactor window，且

\[
G_p(k)=\{R_2(q):q\in W_p(k)\}.
\]

lower-band 条件为 `p^2<2k`。若 `s in G_p(k) cap G_r(k)` 且 `p<r`，称 `(k,p,r,s)` 为 realized lower-band cross-shell root collision。

## 3. L056 —— 全部 lower-band actual-root collisions 精确分类

状态：`PROVED`。

对所有正整数 `k` 与不同 lower-band primes `p<r`，

\[
G_p(k)\cap G_r(k)\ne\varnothing
\]

当且仅当四元组为以下三种之一：

\[
\boxed{
(k,p,r,s)
=
(5,2,3,3),
(6,2,3,4),
(8,2,3,5).
}
\]

整个 lower-band actual-root collision set 因而恰好只有三点。

### 3.1 `r>=5` 全部不可能

L055 Sections 5–8 已证明：若 `r>=5` 且存在共同 root，则从

\[
k^2<p\,s(s+2),
\qquad
rs^2\le k^2+2k,
\qquad
k^2<r(s+1)^2
\]

可推出

\[
2s^2<(3r-3)s+r+1.
\]

随后 `r>=11` 与 lower-band 条件矛盾；`r=7` 导致 `k<=22` 而 lower-band 要求 `k>=25`；`r=5` 导致 `k<=11` 而 lower-band 要求 `k>=13`。这些论证都没有使用 `k>=9`。

所以任何 realized collision 必须满足

\[
\boxed{r=3,\quad p=2.}
\]

### 3.2 `(2,3)` collision 强迫 `s<=7`

L055 对 `(2,3)` 得到

\[
k^2<2s(s+2),
\tag{I}
\]

\[
3s^2\le k^2+2k.
\tag{J}
\]

其 Section 9.1 仅用 (I)、(J) 与整数平方比较证明 `s<=7`，同样没有使用 `k>=9`。

于是

\[
k^2<2\cdot7\cdot9=126,
\]

故 `k<=11`。而 prime `3` 进入 lower band 必须满足 `9<2k`，所以 `k>=5`。

所有剩余可能性只有

\[
\boxed{k=5,6,7,8,9,10,11.}
\]

### 3.3 七个精确有限 case

由 exact quotient-window 公式：

- `k=5`: `W_2=[13,17]`, `G_2={3,4}`；`W_3=[9,11]`, `G_3={3}`，碰撞 root `s=3`；
- `k=6`: `W_2=[19,24]`, `G_2={4}`；`W_3=[13,16]`, `G_3={3,4}`，碰撞 root `s=4`；
- `k=7`: `G_2={5}`, `G_3={4}`，无碰撞；
- `k=8`: `W_2=[33,40]`, `G_2={5,6}`；`W_3=[22,26]`, `G_3={4,5}`，碰撞 root `s=5`；
- `k=9`: `G_2={6,7}`, `G_3={5}`，无碰撞；
- `k=10`: `G_2={7}`, `G_3={5,6}`，无碰撞；
- `k=11`: `G_2={7,8}`, `G_3={6}`，无碰撞。

因此恰好只剩 `(5,2,3,3)`, `(6,2,3,4)`, `(8,2,3,5)`。L056 得证。∎

## 4. L055 的地位因此加强

L055 的 `k>=9` sharp eventual threshold 仍然正确，但 L056 说明得更彻底：

\[
\boxed{\text{所有真实 lower-band 跨 shell root collision 总共只有三次。}}
\]

并且

\[
\boxed{r\ge5\Longrightarrow\text{永远不发生 actual lower-band root collision}.}
\]

全部真实跨 shell 冲突都集中在最小 prime pair `(2,3)` 的三个小盆地。

## 5. 从碰撞分类转向最小 repair

L056 告诉我们 unrepaired root coordinate 的局部 shell split multiplicity：`k=5,6,8` 时某个 root fiber 同时命中 `p=2,p=3`，最大 multiplicity 为 2；其他 `k>=4` 时每个 actual root fiber 至多命中一个 lower-band shell，最大 multiplicity 为 1。

由 P023-S9-T03，若目标状态同时保留 root index 与 least-prime shell identity，那么最小 repair alphabet 大小已经被完全确定。

## 6. L057 —— lower-band root-shell 最小 repair alphabet

状态：`PROVED`。

对每个 `k>=4`，设 `E_root` 是仅保留 actual root index 的 partition，`E_root+shell` 是同时保留 root 与 least-prime shell label 的细 partition。则

\[
\boxed{
R_{\min}(k)
=
R(E_{\rm root}\to E_{\rm root+shell})
=
\begin{cases}
2,&k\in\{5,6,8\},\\
1,&k\ge4,\ k\notin\{5,6,8\}.
\end{cases}
}
\]

证明直接来自 L056 的 root-fiber shell multiplicity 与 P023-S9-T03 的最大局部 split multiplicity 定理。∎

## 7. 一个统一、规范的一比特 repair

定义

\[
\boxed{
\beta_k(q)
=
\mathbf 1
\left[
q>
\left\lfloor\frac{k(k+2)}3\right\rfloor
\right].
}
\]

### L057-A —— `beta_k` 在 actual lower-band states 上恰好是 `p=2` 指示器

设 `q in W_p(k)`，`p` 为 lower-band prime，`k>=4`。

若 `p>=3`，则

\[
q\le\left\lfloor\frac{k(k+2)}p\right\rfloor
\le\left\lfloor\frac{k(k+2)}3\right\rfloor,
\]

故 `beta_k(q)=0`。

若 `p=2`，则

\[
q\ge\left\lfloor\frac{k^2}{2}\right\rfloor+1.
\]

而 `k>=4` 给出

\[
\frac{k(k+2)}3\le\frac{k^2}{2},
\]

等价于 `2(k+2)<=3k`。因此

\[
\left\lfloor\frac{k(k+2)}3\right\rfloor
\le\left\lfloor\frac{k^2}{2}\right\rfloor<q,
\]

故 `beta_k(q)=1`。

于是

\[
\boxed{\beta_k(q)=1\iff p=2}
\]

在所有 actual lower-band shell states 上成立。∎

## 8. L057-B —— repaired root 从 k=4 起统一恢复 shell

定义

\[
\boxed{\widetilde R_k(q)=(R_2(q),\beta_k(q)).}
\]

则对所有 `k>=4`，不同 lower-band prime shells 的实际 repaired images 两两不交。

由 L056，root 单独发生跨 shell collision 时只能是 `p=2` 与 `p=3`；由 L057-A，`p=2` bit 恒为 1，而 `p>=3` bit 恒为 0。所以所有原有 `(2,3)` root collisions 被第二坐标分开，其他 shell 对本来就无 actual root collision。∎

由 P023-S8-T02，least-prime shell label 因而是 repaired root state 的函数。

## 9. 为什么这个 bit 是最小而不是任意补丁

在 `k=5,6,8` 的碰撞 root fiber 内，确实存在两个不同 shell labels。任何只取一个值的 repair coordinate 都无法区分它们；而 `beta_k` 只使用 `{0,1}` 两值，因此恰好达到 P023-S9-T03 下界。

所以 one bit 是该 task quotient 的精确最小局部状态空间，不是工程习惯。

## 10. 四种精度现在可以严格区分

- exact cofactor precision，L054：`k>=4`；
- root + minimal repair，L057：`k>=4`；
- actual root alone，L055/L056：eventual threshold `k>=9`，且仅有三次小 collision；
- enlarged candidate-pair precision，L052：统一分离阈值 `k>=15`。

即

\[
\boxed{
\begin{array}{c}
\text{exact cofactor: }4\\
\text{root + minimal repair: }4\\
\text{actual root alone: }9\\
\text{candidate superset: }15.
\end{array}}
\]

这再次证明更粗的 over-approximation 会制造额外虚假资源竞争，而最小 repair 只补回任务真正能重新读取的 detail。

## 11. 对基础数论路线的反哺

L056/L057 把 lower-band shell 问题从“碰撞计数”进一步改写成

\[
\boxed{\text{actual root channel}+\text{一个只在三个小盆地真正必要的二值 repair}.}
\]

从 `k>=9` 起 repair 恒退化为平凡值；即使把统一公式保留到 `k>=4`，它也只是 `p=2` 指示 bit。

因此后续 P017 递归不应继续为 lower-band 跨 shell competition 支付统一 multiplicity-two 成本。真正剩余复杂度继续收缩到 shell 内 root many-to-one、p-rough cofactor capacity、high-band large-prime tail 与 mirror/CRT 状态的任务相关压缩。

## 12. Executable specification

- `src/enterprise_math/p017_root_shell_repair.py`
- `tests/test_p017_root_shell_repair.py`

回归固定 `k=5,6,8` 三个且仅三个小 collision witnesses；验证 `beta_k` 与 `p=2` shell indicator；验证 repaired root images 从 `k=4` 起的大范围无 overlap；并固定最小 repair alphabet profile。大范围回归只用于防止实现退化，不替代 L056/L057 的普通证明。

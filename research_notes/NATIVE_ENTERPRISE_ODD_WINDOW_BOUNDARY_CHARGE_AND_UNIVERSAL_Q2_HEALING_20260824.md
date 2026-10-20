# 进取原生 filament：奇窗口边界电荷阶梯与统一二层修复

Status: `FREE_RESEARCH_EXACT_CHARGE_STAIRCASE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 一、偶长度严格平衡

对任意偶长度 \(k\)，坐标反射
\[
j\mapsto k-1-j
\]
把两个手性仿射码互相交换，差异只是一项可吸收到自由参数中的 affine function。

所以对每个奇模数、每个有限域扩张和每个允许的 residue-ring 精度：
\[
\boxed{
N_k^+=N_k^-
\qquad(k\text{ even})
}.
\]

因此手性边界电荷只可能出现在奇长度窗口。

## 二、已实现奇长度的 slope-distinct 电荷阶梯

对全局 prime-incidence 岛谱中出现的长窗口 \(k=5,7,9\)，在
\(q>k-1\) 的斜率分离范围内，非零手性电荷精确为：

| \(k\) | 特征 \(q\) | \(N_+(\mathbb F_q)\) | \(N_-(\mathbb F_q)\) | 电荷 \(N_+-N_-\) |
|---:|---:|---:|---:|---:|
| 5 | 5 | 8 | 7 | \(+1\) |
| 7 | 13 | 98 | 99 | \(-1\) |
| 9 | 13 | 84 | 85 | \(-1\) |
| 9 | 23 | 354 | 353 | \(+1\) |

其余 slope-distinct exceptional channels 虽可能有三重、四重共点，但左右边界的 distinct-collision 数相同，所以总 survivor 数仍手性平衡。

## 三、有限域扩张永久保留绝对电荷

若特征 \(q\) 上的排列常数差为
\[
b_+-b_-=e\in\{-1,+1\},
\]
则对任意 \(s\ge1\)：
\[
\boxed{
N_+(\mathbb F_{q^s})-N_-(\mathbb F_{q^s})=e
}.
\]

具体第二层：

| \(k\) | \(q\) | \(N_+(\mathbb F_{q^2})\) | \(N_-(\mathbb F_{q^2})\) |
|---:|---:|---:|---:|
| 5 | 5 | 508 | 507 |
| 7 | 13 | 27398 | 27399 |
| 9 | 13 | 27072 | 27073 |
| 9 | 23 | 275112 | 275111 |

绝对差保持一个点；相对密度差则按 \(q^{-2s}\) 衰减。

## 四、整个 \(k=5,\dots,9\) 异常谱都在第二层修复

mixed-parity 三线共点由整数
\[
3(w-u)(w-v)\pm\chi
\]
控制。

对所有实际允许的窗口长度 \(k=5,\dots,9\)，逐一分解所有 slope-distinct exceptional obstruction，得到：

| \(k\) | slope-distinct exceptional primes |
|---:|:---|
| 5 | \(5\) |
| 6 | \(7,11,23\) |
| 7 | \(7,11,13,23\) |
| 8 | \(11,13,23,31,53\) |
| 9 | \(11,13,23,31,53\) |

对表中每一个 \(q\)、每一种实际出现该 \(q\) 的手性：
\[
\boxed{
\max v_q\!\left(3(w-u)(w-v)\pm\chi\right)=1
}.
\]

因此：
\[
\boxed{
\delta_{k,q}^\chi(1)\text{ 可以非零},
\qquad
\delta_{k,q}^\chi(a)=0\quad(a\ge2)
}
\]
对整个 \(k=5,\dots,9\) slope-distinct exceptional spectrum 成立。

也就是说：
\[
\boxed{
q^2\text{ 是全部已实现 filament arrangement 的统一去奇异化精度}
}.
\]

## 五、奇窗口第二层直接计数

| \(k\) | \(q\) | \(N_+(\mathbb Z/q^2\mathbb Z)\) | \(N_-(\mathbb Z/q^2\mathbb Z)\) |
|---:|---:|---:|---:|
| 5 | 5 | 510 | 510 |
| 7 | 13 | 27399 | 27399 |
| 9 | 13 | 27076 | 27076 |
| 9 | 23 | 275116 | 275116 |

所以奇窗口电荷具备非常明确的算术性格：

- 在 residue characteristic 的 special fiber 上出现；
- 沿 unramified field degree 永久保留；
- 沿 ramified precision 在第二层统一消失。

## 六、与原生岛长上限的关系

全局进取 prime-incidence 几何已证明
\[
k\le9.
\]

正因为窗口长度有这个 sharp cap，异常 obstruction 的大小和 prime support 都是有限的；其最后通道为 \(53\)，而全部 \(q\)-进深度又在 1 截断。

因此产生完整链条：
\[
\boxed{
5\text{ 打断全局连通}
\to
9\text{ 限制最大窗口}
\to
53\text{ 截止局部异常}
\to
q^2\text{ 统一修复全部异常}
}.
\]

这是目前最完整的一条“原生几何—有限异常—算术提升”闭环。它仍然描述局部 sieve carrier 的精确结构，不据此主张实际素数事件率偏离 Hardy–Littlewood 型零模型。

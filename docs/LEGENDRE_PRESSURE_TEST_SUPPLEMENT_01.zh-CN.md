# Legendre 压力测试——补充 01

状态：`ACTIVE RESEARCH NOTE`  
范围：对 `LEGENDRE_PRESSURE_TEST.zh-CN.md` 中工具的精确细化。  
结论纪律：**本文不声称证明了 Legendre 猜想。**

## 1. 目的

第一份压力测试笔记已经把相邻平方之间的素数个数压缩为有符号平方进位，再进一步压成二进制进位事件。本补充继续消除两个黑箱：

1. 给出三值进位 \(\kappa_d(k)\) 的中心余数直接判据；
2. 把锚点转移 \(\Lambda_b(k)\) 改写成普通的中心差异量，并证明所有负转移都被限制在 \(b\le k\) 的小模数层。

以下都是精确整数命题，不是密度启发式。

## 2. L007 —— 中心平方进位判据

状态：`PROVED`

写成

\[
k=qd+t,\qquad 0\le t<d,
\]

并定义中心锚点余数

\[
a_d(t)=t(t+1)\bmod d.
\]

局部平方盆地可以围绕 \(t(t+1)\) 写成

\[
(t^2,(t+1)^2)
=
 t(t+1)+\{1-t,\ldots,t\}.
\]

因此 \(\kappa_d(k)=H_d(t)\) 恰好等于同余类

\[
s\equiv-a_d(t)\pmod d
\]

在

\[
\{1-t,\ldots,t\}
\]

中的代表元数量。

因为局部区间长度为 \(2t<2d\)，最多只有两个代表。对 \(t>0\)，它们分别是负代表 \(-a_d(t)\) 与正代表 \(d-a_d(t)\)。所以

\[
\boxed{
\kappa_d(k)
=
\mathbf 1_{a_d(t)<t}
+
\mathbf 1_{a_d(t)\ge d-t}
}
\]

而当 \(t=0\) 时 \(\kappa_d(k)=0\)。

这不仅重新得到 \(\kappa_d(k)\in\{0,1,2\}\)，还把三个取值解释为：**同一个中心余数类是否穿过局部窗口的左边界与右边界。**

## 3. L008 —— 显式二进制进位事件

状态：`PROVED`

令 \(d\) 为奇数，并写

\[
k=qd+t,
\qquad
0\le t<d.
\]

定义

\[
a=t(t+1)\bmod d,
\qquad
h=\left\lfloor\frac{t(t+1)}{d}\right\rfloor.
\]

第一份笔记已经证明

\[
\kappa_d(k)-\kappa_{2d}(k)
=(-1)^q\varepsilon_d(k),
\qquad
\varepsilon_d(k)\in\{0,1\}.
\]

现在可以把 \(\varepsilon_d(k)\) 完全展开：

\[
\boxed{
\varepsilon_d(k)=
\begin{cases}
\mathbf 1_{a\ge d-t}, & q\equiv0\pmod2,\ h\equiv0\pmod2,\\
\mathbf 1_{a<t},       & q\equiv0\pmod2,\ h\equiv1\pmod2,\\
\mathbf 1_{a\ge t},    & q\equiv1\pmod2,\ h\equiv0\pmod2,\\
\mathbf 1_{a<d-t},      & q\equiv1\pmod2,\ h\equiv1\pmod2.
\end{cases}
}
\]

证明要点：从模 \(d\) 提升到模 \(2d\) 时，提升后的余数由 \(h\) 的奇偶决定，因为

\[
t(t+1)=hd+a.
\]

若 \(h\) 为偶数，模 \(2d\) 的提升余数为 \(a\)；若 \(h\) 为奇数，则为 \(a+d\)。而 \(q\) 的奇偶决定 \(k\bmod2d\) 是 \(t\) 还是 \(d+t\)。分别代入 L007 即得到上述四种情况。

当 \(d\) 为奇数时，局部商奇偶还具有全局中心解释：

\[
\left\lfloor\frac{k(k+1)}{d}\right\rfloor
\equiv h\pmod2.
\]

因为代入 \(k=qd+t\) 后

\[
\left\lfloor\frac{k(k+1)}d\right\rfloor
=q^2d+q(2t+1)+h,
\]

而 \(d\) 为奇数时前两项奇偶相同，在模二意义下相消。

所以二进制进位事件已经完全由以下三项决定：

- 欧几里得商层 \(q=\lfloor k/d\rfloor\)；
- 局部中心商的奇偶 \(h\bmod2\)；
- 关于 \(a=t(t+1)\bmod d\) 的一个边界比较。

开放问题因此不再是理解一个未知的 `0/1` 变量，而是控制这些**显式边界穿越事件**在平方自由除数层上的有符号分布。

## 4. L009 —— 横向锚点差异恒等式

状态：`PROVED`

令

\[
M=k(k+1),
\]

并令 \(A_k\) 为所有满足 \(p\le k\) 且 \(p\mid M\) 的素数的平方自由乘积。取任意正整数 \(b\)，满足

\[
\gcd(b,A_k)=1.
\]

回忆锚点 Möbius 转移

\[
\Lambda_b(k)
=
\sum_{a\mid A_k}\mu(a)\kappa_{ab}(k).
\]

定义

\[
R_A(x)=\#\{1\le m\le x:\gcd(m,A)=1\}
\]

以及中心存活计数

\[
S_b(k)=
\#\left\{
1-k\le s\le k:
 b\mid M+s,
 \gcd(s,A_k)=1
\right\}.
\]

则

\[
\boxed{
\Lambda_b(k)
=
S_b(k)-2R_{A_k}\!\left(\left\lfloor\frac{k}{b}\right\rfloor\right)
}.
\]

证明：由平方进位分解

\[
\kappa_{ab}(k)=H_{ab}(k)-2\left\lfloor\frac{k}{ab}\right\rfloor.
\]

对 \(a\mid A_k\) 做 Möbius 反演，第一部分恰好数出盆地内部那些被 \(b\) 整除、且 \(n/b\) 与 \(A_k\) 互素的状态。由于 \(\gcd(b,A_k)=1\)，这等价于 \(\gcd(n,A_k)=1\)。写成 \(n=M+s\)，再利用 \(A_k\mid M\)，就等价于 \(\gcd(s,A_k)=1\)，因此得到 \(S_b(k)\)。

粗主体则满足

\[
\sum_{a\mid A_k}\mu(a)
\left\lfloor\frac{k}{ab}\right\rfloor
=
R_{A_k}\!\left(\left\lfloor\frac{k}{b}\right\rfloor\right).
\]

两者相减即得结论。

## 5. 立即得到的局部化推论

### 5.1 负转移只可能发生在小模数层

若

\[
b>k,
\]

则 \(\lfloor k/b\rfloor=0\)，因此

\[
\boxed{\Lambda_b(k)=S_b(k)\ge0.}
\]

所以一切负锚点转移都必须满足

\[
\boxed{b\le k.}
\]

此前找到的反例

\[
\Lambda_5(456)=-4
\]

因此被严格限制在真正的小横向模数层；负异常不可能任意漂移到很大的除数乘积上。

### 5.2 超过两倍根以后，转移再次二值化

若

\[
b>2k,
\]

中心区间连续整数的数量小于 \(b\)，所以其中至多存在一个 \(b\) 的倍数。结合基准项为零，可得

\[
\boxed{\Lambda_b(k)\in\{0,1\}.}
\]

因此在**大横向除数侧**，锚点变换又进入一个二进制区域。

### 5.3 有限支撑

若

\[
b>(k+1)^2-1,
\]

平方盆地内部不存在正的 \(b\) 倍数，同时基准项为零，于是

\[
\boxed{\Lambda_b(k)=0.}
\]

所以锚点变换以后只有

\[
1<b\le(k+1)^2-1
\]

可能产生贡献。

## 6. P017 的新结构

当前有符号问题自然分成三个区域：

1. **小横向模数 \(b\le k\)**：唯一可能出现 \(\Lambda_b(k)<0\) 的区域；根—截断耦合的强相互作用集中在这里。
2. **中间区域 \(k<b\le2k\)**：转移非负，而且中心命中最多两个。
3. **大模数 \(2k<b\le(k+1)^2-1\)**：转移已经二值化为 `0/1`，因此成为截断除数格上的 Boolean 边界问题。

这提示更聚焦的符号反转策略：不要试图在全部除数乘积上寻找一个统一 involution。先隔离小模数差异，再尝试沿除数格中“跨越 cutoff”的边，对非负二值大模数项进行配对。

这是否足以穿过经典筛法 parity barrier，目前仍是开放问题。

## 7. 验证状态

`tests/test_legendre_pressure.py` 在有限范围内执行检查：

- 中心进位判据与原始命中数定义完全一致；
- 显式二进制事件准确重构 \(\kappa_d-\kappa_{2d}\)；
- 锚点差异恒等式与原始 Möbius 转移完全一致；
- \(b>k\Rightarrow\Lambda_b\ge0\)；
- \(b>2k\Rightarrow\Lambda_b\in\{0,1\}\)；
- 有限支撑截断。

上述数学结论的依据是本文证明，而不是有限计算本身。

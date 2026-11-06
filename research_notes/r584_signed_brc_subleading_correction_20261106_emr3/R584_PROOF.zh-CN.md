# R584｜倒谱矩修正项的次主阶全参数正性与精确双尺度展开

日期：2026-11-06。状态：AUTHOR_SIDE_ANALYTIC_PROOF / EXACT_FINITE_CROSSCHECK；独立数学 Driver 审阅待完成。

## 科学来源与范围

冻结 signed BRC 科学输入为 R462 @ 18783e01e3646c72b7aab3b16d3f565e83e6446f；沿用 R582 @ 832b1bb9a094f91454b46170150332727c79fff6 的辅助标量倒谱观察者，并直接接续 R583 @ 1622f5fd51e6359a5cd39de5185e5165db2e74b7 的修正系数问题。这里仅证明一个代数函数的全部 Taylor 系数性质；无需接受 R582 的端点积分证明即可独立核验本轮定理。原生 signed BRC 联合十二支路、P000 和 ACTIVE 世界观保持原定义。

定义 t=0 处的形式幂级数芽
$$
s(t)=\sqrt{1-2t},\quad \alpha(t)=\frac{1+s(t)}2,\quad
B(t)=\frac{\alpha(t)\sqrt{s(t)}}{(2s(t)-1)^{3/2}},
\qquad b_m=-m[t^m]\log B(t)\quad(m\ge1).
$$
所有解析分支在 t=0 归一化为正值，B(0)=1。

## 定理 R584-A：全阶显式分解与正余项

对每个整数 m≥1，精确成立
$$
\boxed{b_m=-\frac32\left(\frac83\right)^m+2^{m-2}+E_m},
$$
其中
$$
\boxed{
E_m=[t^{m-1}]\frac1{s(t)}
\left(\frac1{1+s(t)}+\frac3{1+2s(t)}\right)
\ \ge\ \frac32\,\frac{\binom{2m-2}{m-1}}{2^{m-1}}\ >0.
}
$$
下界在 m=1 取等。

**证明。** 恒等式 $(2s-1)(2s+1)=3-8t$ 给出
$$
\log B(t)=\log\alpha(t)+\frac14\log(1-2t)
+\frac32\log\frac{1+2s(t)}3
-\frac32\log\left(1-\frac83t\right).
$$
系数提取后，第一、第三项的贡献为
$$
E_m=-m[t^m]\left(\log\alpha(t)+\frac32\log\frac{1+2s(t)}3\right).
$$
因为 $s'(t)=-1/s(t)$，逐项求导即得所示 E_m 系数表达。

令 $w(t)=1-s(t)$。对每个 j≥1，
$$
[t^j]w(t)=\frac{\binom{2j}{j}}{2^j(2j-1)}>0.
$$
又有 $s=1-w$，于是
$$
\frac1{s}\left(\frac1{1+s}+\frac3{1+2s}\right)
=\frac1{1-w}\left[
\frac12\sum_{j\ge0}\left(\frac w2\right)^j+
\sum_{j\ge0}\left(\frac{2w}3\right)^j\right].
$$
右端各个 Taylor 系数均非负，并且只取两个求和的 j=0 项便得到 $(3/2)(1-2t)^{-1/2}$。故 E_m 的系数级下界成立；后者每阶严格为正，证毕。

## 定理 R584-B：次主阶及首个非平凡修正项

在 m→∞ 时，有
$$
\boxed{
E_m=\frac{2^m}{\sqrt{\pi m}}
\left(2-\frac5{2m}+O(m^{-2})\right).
}
$$
从而
$$
\boxed{
b_m=-\frac32\left(\frac83\right)^m+
2^{m-2}+
\frac{2^m}{\sqrt{\pi m}}
\left(2-\frac5{2m}+O(m^{-2})\right).
}
$$
这里的 $O(m^{-2})$ 常数与 m 无关，定理是对单个阶数参数 m 的极限，且与有限 k 的谱零点问题相区别。

**证明。** 令 $A(t)$ 为定理 A 中的 E_m 生成函数。当 $s\to0$，代数展开为
$$
A(t)=\frac1{s(1+s)}+\frac3{s(1+2s)}
=\frac4s-7+13s-25s^2+49s^3+O(s^4).
$$
作为 $s=\sqrt{1-2t}$ 的函数，$A(t)$ 在从原点延拓的割平面 $\mathbb C\setminus[1/2,\infty)$ 上解析，分母 $s,1+s,1+2s$ 在该分支内均不为零；它在 $t=1/2$ 具有允许代数奇性转移的凹角邻域。奇点分析的标准系数转移（或等价的 Hankel 轮廓论证）因此适用；局部整数幂项只影响解析部分，下一非整数幂项 $s^3$ 给出 $O(2^n n^{-5/2})$ 尾阶，其中 $n=m-1$。

取前两项非整数幂并使用
$$
[t^n](1-2t)^{-1/2}=\frac{2^n}{\sqrt{\pi n}}
\left(1-\frac1{8n}+O(n^{-2})\right),
$$
$$
[t^n](1-2t)^{1/2}=-\frac{2^n}{2\sqrt{\pi}\,n^{3/2}}
\left(1+O(n^{-1})\right),
$$
便得到
$$
E_m=\frac{2^m}{\sqrt{\pi m}}
\left(2+\frac{3}{4m}-\frac{13}{4m}+O(m^{-2})\right),
$$
即所需结果。证毕。

## 精确证书与观测边界

源码 R584_VERIFY.py 用 Python 3.13.5 标准库整数及 Fraction 验证 m=1..96；一条路径以 R583 的有限有理二项式和计算 b_m，另一条路径用 w 的原始 Taylor 系数、形式幂级数求逆和卷积计算 E_m。全部 96 阶逐项有理数恒等式、严格正性及系数级下界通过。浮点输出只展示渐近收敛，不参与任何数学验收条件。原始输出见 R584_EVIDENCE.txt。

BRC 复用类别：REUSE_APPLIED。冻结 R462 signed 分支 → R580/R582 辅助标量 Catalan 读出 → R583 的 b_m → 本轮精确校正；不作新 native BRC 实验。

## 下一研究单元

本轮分清了 b_m 的 $8/3$ 主导奇点与 $2$ 次主导奇点，却仍需要研究有限 k 的 $P_k(t)$ 在 $t\in(3/8,1/2)$ 及邻近复环域的真实零点。优先寻求同时控制 k 和 m 的余项或固定复域上的零点计数证书，并检验辅助标量观察者对原生 signed BRC 联合操作的保真条件。

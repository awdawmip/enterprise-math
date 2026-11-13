# 三端口共同损耗族的固定纠缠见证

**命题。** 对候选模型的共同损耗幅度参数 $0\le t\le1$，从 $|100\rangle$ 出发，迹去环境与第三端口。任意正整数 $n$ 次独立新鲜环境作用后，两端口态 $\rho_{AB}^{(n)}$ 对一个固定单位向量 $w=(1,0,0,2)/\sqrt5$ 满足

$$
\langle w|(\rho_{AB}^{(n)})^{T_B}|w\rangle
=-\frac{2(1-t^n)(2+t^n)}{45}.
$$

因此 $t<1$ 时每个有限正步数都得到纠缠的 $AB$ 态。$t=1$ 时输出保持可分输入。

**通道。** 以三个 qubit 的单激发基 $|100\rangle,|010\rangle,|001\rangle$ 定义 $|b\rangle=(1,1,1)/\sqrt3$、$P=|b\rangle\langle b|$、$D=I-P$。保留算子 $K_t=D+tP$。真空记为 $|v\rangle=|000\rangle$。取 $A_0$ 在单激发扇区上为 $K_t$，在真空和多激发扇区上为恒等；取 $A_1=\sqrt{1-t^2}|v\rangle\langle b|$。于是 $A_0^*A_0+A_1^*A_1=I$，吸收出口 $L_t=\sqrt{1-t^2}\langle b|$ 满足 $L_t^*L_t=(1-t^2)P$。每一步按 $\rho\mapsto A_0\rho A_0^*+A_1\rho A_1^*$ 无条件求和。真空为吸收态。

**证明。** 正交投影给出 $K_t^n=D+t^nP$。由于每次吸收进入真空并留下独立环境记录，无条件态为 $|u_z\rangle\langle u_z|+(1-z^2)|v\rangle\langle v|/3$，其中 $z=t^n$，$u_z=(a,c,c)$，$a=(2+z)/3$，$c=(z-1)/3$。迹去第三端口后，在 $00,01,10,11$ 基下作 $B$ 偏转置，得到

$$
(\rho_{AB}^{(n)})^{T_B}=
\begin{pmatrix}
1-a^2-c^2&0&0&ac\\
0&c^2&0&0\\
0&0&a^2&0\\
ac&0&0&0
\end{pmatrix}.
$$

代入 $w$，其二次型为 $(1-a^2-c^2+4ac)/5$，展开即得命题。可分态的偏转置为正半定，因此负二次型证明该分割上的纠缠。一步取 $t=1/2$ 恢复 $-1/18$；$t=0$ 给 $-4/45$。当 $t=1$ 时，$A_0=I,A_1=0$。

[原 v0.4 第 3、6 节](https://github.com/awdawmip/enterprise-math/blob/79107cf112b77c9890458c30bbf066fdb7d81dee/research_notes/BRC_CELL_RESIDUAL_ENTANGLEMENT_CCBF9335_20260928.md)给出 $t=1/2$ 和完全损耗端点的见证。[v0.5 第 1、4 节](https://github.com/awdawmip/enterprise-math/blob/4bb4cbebb0369513a310c8ba1c250529f4bd99f8/research_notes/BRC_CELL_SCATTERING_GRAM_CCBF9335_20260928.md)给出投影幂公式和偏转置主子式。本附注确定同一个 $w$ 在整个闭区间的期望。结论限定在带共同出口、张量分割和新鲜环境的端口模型。P000 原生结点是否实现这些条件仍待独立推导。[Peres 偏转置判据](https://doi.org/10.1103/PhysRevLett.77.1413)

**精确核验。** 同目录运行 `python -B verify.py`。脚本用标准库有理数直接作用在八维系统上，独立执行偏迹与偏转置。单步期望是至多二次多项式：$A_0$ 的条目对 $t$ 为仿射函数，已迹去环境的吸收项对 $t$ 为二次函数。因此在三个不同有理点检验等式也构成整个多项式的恒等证书。多步恒等式由投影幂和真空吸收的证明覆盖所有正整数。

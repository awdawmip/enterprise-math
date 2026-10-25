# R281 — BRC 清洁重置完整效果的 Edgeworth 校正与最终唯一峰值

日期：2026-10-25。作者侧解析证明（AUTHOR_PROVED，DRIVER_UNREVIEWED，NOT_ADMITTED）。

## 0. 固定范围、原始输入和证据

Global Knowledge 原生 main 快照：8ce5de60e43a0ff3123f44d79c2d6424b0a44c06。同一快照已读取两个规范入口、P000_STARTUP.json（原 P000 blob=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc）、ACTIVE 世界观以及数学、代码、BRC 研究政策。项目 Source 快照：enterprise-math main@9da3be970df5a28268b54d246594b2896bcff468；按 portable research 规则处理。数学依赖是 R279（commit 24f2d7515ac6bb8201d74c5dcdc1d61b6a11b159）和 R280（commit 66be646553b1b7e8f989bd60dc91124dedfdb5f8），均为作者侧成果、未获独立 Driver 数学接纳。

研究对象仅为**正权、有序来源词**的仿射 BRC 辅助自动机，不是 P000 六维 Cell 原生动力学，路径长度不等于物理心跳时间。状态 q=0,1,2；六边转移 q0: 0→(q2,-1,-1),1→(q2,+1,-1)；q1: 0→(q0,-1,-1),1→(q0,+1,-1)；q2: 0→(q1,+1,+1),1→(q2,+1,-1)。右复合规则为 $(\epsilon,k)\star(\eta,b)=(\eta\epsilon,\eta k+b)$。clean 意为来源词不含相邻 00。$P_n(\epsilon,k)$ 是从 q0 出发、返回 q0、完整效果恰为 $(\epsilon,k)$ 的 clean 原始来源词数量，保留正整数重数与路径区别。

## 1. 两项新定理

设
\[
\varphi=(1+\sqrt5)/2,\quad \rho=\varphi^{-1},\quad
\sigma^2=(15+7\sqrt5)/10,
\]
\[
\mu_+=-(2+\sqrt5),\quad
\mu_-=-(5+\sqrt5)/2,\quad
C=1+\frac{3\sqrt5}{8}.
\]

**定理 A：固定宽度窗口的显式一阶 Edgeworth 展开。**
对每个固定 $M>0$，存在 $N_M,C_M>0$，对全部 $n\ge N_M$、$\epsilon\in\{\pm1\}$、$|k|\le M$ 且 $k\equiv n\pmod2$ 一致成立
\[
\boxed{P_n(\epsilon,k)=
\frac{\varphi^n}{5\sqrt{2\pi\sigma^2 n}}\left[
1+\frac1n\left(C-\frac{(k-\mu_\epsilon)^2}{2\sigma^2}\right)
+O_M(n^{-2})\right].}
\]
对错误奇偶格点，$P_n(\epsilon,k)=0$ 严格成立。上述相对余项只对固定宽度窗口声明；不是对全部随 n 任意增长的 k 的相对误差界。

**定理 B：最大 clean 效果纤维的最终唯一位置。**
存在整数 $N$，使全部 $n\ge N$ 的全局最大效果恰有一个：
\[
\boxed{
\operatorname*{argmax}_{(\epsilon,k)}P_n(\epsilon,k)
=\begin{cases}
\{(+1,-4)\},&n\text{ 偶数},\\
\{(-1,-3)\},&n\text{ 奇数}.
\end{cases}}
\]
这是存在性结论，目前未给出有效最小整数阈值 N。有限范围 n=81..400 具有这一性质，不构成 $N=81$ 的无限范围证明。

## 2. 可审查的解析骨架

R279 的精确 Laurent 生成函数为
\[
G_+(x,z)=\frac{1+x^2+x^4-xz^{-1}-x(1+x^2)z}{H(x,z)},\qquad
G_-(x,z)=\frac{x^4z^{-2}-x^5z^{-1}}{H(x,z)}
\]
其中
\[
H(x,z)=(1+x^2)D(x,z),\qquad
D(x,z)=1+2x^4-x^6-x(z+z^{-1}).
\]
写 $z=e^s$，则 $D(x,s)=1+2x^4-x^6-2x\cosh s$，且
\[
D(\rho,0)=0,\qquad D_x(\rho,0)=15-7\sqrt5\ne0.
\]
故隐函数定理给出唯一解析偶函数 $r(s)$ 满足 $r(0)=\rho$、$D(r(s),s)=0$。记
\[
\lambda(s)=\log\frac{\rho}{r(s)},\quad
A_\epsilon(s)=-\frac{N_\epsilon(r(s),e^s)}
{r(s)(1+r(s)^2)D_x(r(s),s)}.
\]
在足够小的纯虚 s 区间，R280 已论证的单位圆谱间隙和解析极点分离允许一致提取唯一主留数：
\[
[x^n]G_\epsilon(x,e^s)
=\varphi^n A_\epsilon(s)e^{n\lambda(s)}
+O((\rho+\delta)^{-n}).
\]
这里在 $s=i\pi$ 对应的另一主峰需要单独计入奇偶格点；远离两峰，R280 的严格正矩阵谱间隙提供指数抑制。全结论的审查依赖包含该先前作者侧引理，不能把有限矩检验当成谱证明。

## 3. 精确四阶累积量与两种符号共享的振幅曲率

对 $D(r(s),s)=0$ 求导得到
\[
r'(0)=0,\qquad r''(0)=\frac{2\rho}{D_x(\rho,0)}
=-1-\frac{2\sqrt5}{5},
\quad \lambda''(0)=\sigma^2.
\]
展开 $r(s)=\rho+\alpha s^2+\beta s^4+O(s^6)$，
直接比较 D 的 $s^2,s^4$ 系数可得
\[
\alpha=-\frac12-\frac{\sqrt5}{5},
\qquad \beta=\frac73+\frac{313\sqrt5}{300},
\]
进而
\[
\boxed{\kappa_4=\lambda^{(4)}(0)
=-\frac{153}{2}-\frac{1711\sqrt5}{50}.}
\]
对留数因子直接取对数求导，使用 $r'(0)=0$：
\[
A_+(0)=A_-(0)=1/10,\qquad
(\log A_\epsilon)'(0)=\mu_\epsilon,
\]
\[
\boxed{(\log A_+)''(0)=(\log A_-)''(0)
=-\frac{119+53\sqrt5}{10}=:v.}
\]
证明中的重要新现象是两个完整效果符号的**二阶留数振幅完全相同**，虽然一阶中心不同。符号计算以独立精确有理式核验以上等式，而不改变来源计数定义。

由代数化简，
\[
\boxed{\frac{\kappa_4}{8\sigma^4}-\frac{v}{2\sigma^2}
=1+\frac{3\sqrt5}{8}=C.}
\]

## 4. 局部 Fourier 反演的误差控制

在 $s=i\theta$ 附近，
\[
\lambda(i\theta)=-\frac{\sigma^2\theta^2}{2}
+\frac{\kappa_4\theta^4}{24}+O(\theta^6),
\]
\[
\log A_\epsilon(i\theta)
=-\log10+i\mu_\epsilon\theta-\frac{v\theta^2}{2}
+O(\theta^3).
\]
将固定 $|k|\le M$ 的相位 $e^{-ik\theta}$ 合并，设高斯尺度 $\theta=y/\sqrt n$。对 $e^{i(\mu_\epsilon-k)\theta}$ 和其他因子展开至相对 $1/n$，利用 $\mathbb E(y^2)=1/\sigma^2$、$\mathbb E(y^4)=3/\sigma^4$，得相对修正项
\[
\frac{\kappa_4}{8\sigma^4}
-\frac{v}{2\sigma^2}
-\frac{(k-\mu_\epsilon)^2}{2\sigma^2}.
\]

解析余项可以取 $|\theta|\le n^{-2/5}$ 后用受控 Taylor 展开与高斯积分处理：$n\theta^6,\theta^4,n^2\theta^8$ 的积分相对为 $O(n^{-2})$；奇次幂因实系数共轭对称在对称积分区间抵消，与其他奇次幂相乘才贡献相对 $O(n^{-2})$。中间弧因实部二次衰减而超多项式小，远弧继承 R280 的谱间隙而指数小。常数对固定 M 及两个符号统一。每个来源步的 k 奇偶性翻转，因此反演在 $0,\pi$ 两处的主峰在正确奇偶格点相加，产生 lattice factor 2，得到定理 A 的系数 $1/5$；错误格点严格相消。

## 5. 从 Edgeworth 展开严格定位最终峰值

R280 已建立作者侧有限宽度定位引理：足够大 n 的全局最大位置满足 $|k-\mu_\epsilon|\le C_0$，$C_0$ 与 n 无关。因此取固定足够大的 M，定理 A 一次覆盖所有峰值候选（固定有限集）。由于符号共享同一修正常数 C，比较各候选只须比较 $(k-\mu_\epsilon)^2$；不同候选的严格正差在 $1/n$ 项中压过 $O_M(n^{-2})$。

按偶奇类，各符号最近整数为：

| 长度奇偶 | ε=+1 的最近 k | ε=-1 的最近 k |
|:--|:--:|:--:|
| 偶数 | -4 | -4 |
| 奇数 | -5 | -3 |

同一符号的最近奇偶整数均唯一。不同符号的最小距离平方差为
\[
\text{偶数： }(-4-\mu_-)^2-(-4-\mu_+)^2
=\frac{5\sqrt5-11}{2}>0,
\]
\[
\text{奇数： }(-5-\mu_+)^2-(-3-\mu_-)^2
=\frac{25-11\sqrt5}{2}>0.
\]
因此最终唯一峰值交替出现，证明定理 B。注意比较不为零但偶数间隙很小，这解释了有限长度存在较晚的符号翻转。不能因为数值 n=81 后持续稳定就宣称已严格证明最小阈值。

## 6. 实际精确证据、权限与未解问题

实际执行 Python+SymPy 精确断言：$\sigma^2,\kappa_4,v,C$ 两个根式距离差；原始六边自动机整数 DP 到 n=400，保留 q、上一个 bit、ε、k、原始来源重数；独立 Laurent 有理分式整数递推到 n=150，逐完整效果核对 21,463 个非零系数；全部非零结果服从 k≡n mod2。观测 n=81..400 的唯一最大效果与定理 B 一致，在 n=9..400 中共 69 个偏离层，最后一个偏离 n=80。这些仅是有限准确核对。实际运行的程序与输出分别为 R281_verify_edgeworth.py 和 EXACT_EVIDENCE.json。

本轮原生控制查询为 CONTROL_QUOTA；原生 session_start 为 STATIC_READONLY_SCOPE_DENIED(operation_sent=false)。作者侧 Research-Activity-ID: RA-EMR3-20261025-1022-R281EDGEWORTH。既无已验证活跃 Owner、正式 CLAIM 或 Source Result，也未获得独立 Driver 审查；不更改 P000/ACTIVE 世界观，不提升 Working Truth。

**下一最小研究单元**：为两条竞争峰值建立显式余项常数或有限正锥证书，从而将存在性 N 变成有效整数阈值；然后只在峰值 $(+1,-4)$ 与 $(-1,-3)$ 上比较三个 dirty 通道，尝试证明或反驳 $B_n=\Lambda_n$ 的最终全长等式。R276 的无限边缘反例排除了对所有效果采用 dirty 全域逐点支配的简单路线。

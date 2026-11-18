# 用低阶 Legendre 值计算 CM 点的第二数位

设 $p>3$ 为素数，$p\equiv13,19\bmod24$，$n=(p-1)/3$，在 $\mathbf Z_{(p)}[t]/(2t^2-1)$ 取冻结的交换端口。用 $P_j(1)=1$ 归一化普通 Legendre 多项式。已知 $P_n(t)\equiv0\bmod p$ 且 $P_n'(t)\not\equiv0\bmod p$。以下给出只用低阶多项式模 $p$ 的计算式，再用普通三项递推模 $p^2$ 独立检查。全素数结论使用两条项目分支经核对的同余。[任务](https://github.com/awdawmip/enterprise-math/blob/3a8cee80e6707deb8601fb2d53bf2dc85d16fcba/research_tasks/EMW59A_JT2_UR_NORM_JET_GEN3_20260920.md) · [分支衔接及来源](legendre.md)

## 平方多项式的原函数

对任何非负整数 $n$，令 $f=P_n$，$I_n(x)=\int_0^x f(v)^2\,dv$。用低于 $n$ 且与 $n$ 同奇偶的 Legendre 多项式组成
$$
S_n(x)=\sum_{\substack{0\le j<n\\j\equiv n\ (2)}}\frac{2j+1}{(n-j)(n+j+1)}P_j(x).
$$
则在 $\mathbf Q[x]$ 有恒等式
$$
(2n+1)I_n(x)=xP_n(x)^2+
2(1-x^2)\big(P'_n(x)S_n(x)-P_n(x)S'_n(x)\big).
$$

设 $L_n g=((1-x^2)g')'+n(n+1)g$。由 Legendre 方程，$L_nP_j=(n-j)(n+j+1)P_j$。两个标准导数恒等式 $xP'_n-nP_n=P'_{n-1}$（$n\ge1$）与 $P'_{j+1}-P'_{j-1}=(2j+1)P_j$ 给出 $L_nS_n=xf'-nf$；展开至 $P'_1=P_0$ 或 $P'_0=0$ 即可。$n=0$ 时两侧都为零。于是
$$
\big[(1-x^2)(fS_n'-f'S_n)\big]'=
fL_nS_n-S_nL_nf=xff'-nf^2.
$$
原公式两侧的导数相同，在零处也相同，因为 $f,S_n$ 同奇偶。[Legendre 导数与递推](https://dlmf.nist.gov/14.10)

## 无需先求模 $p^2$ 的除值

在本任务中 $2n+1<p$。$S_n$ 的全部系数分母为 $p$ 单位。在 $x=t$ 处利用 CM 零值与 $1-t^2=1/2$，平方原函数的公式变为
$$
(2n+1) I_n(t)\equiv P'_n(t)S_n(t)\pmod p .
$$
结合经两条记录衔接所得的 $9P_n(t)P'_n(t)=p(2I_n(t)+3t)\pmod{p^2}$，并在使用 CM0 后写 $u=P_n(t)/p$，得到
$$
u\equiv \frac23 S_n(t)+\frac{t}{3P'_n(t)}\pmod p .
$$
这里只在 $P'_n(t)$ 已知为单位后才除以它。为在基域中计算，记 $V_j=P_j(t)/t^{j\bmod2}$。由 $(1-t^2)P_n'(t)=n(P_{n-1}(t)-tP_n(t))$ 得 $P_n'(t)/t\equiv2nV_{n-1}$。又有
$$
\frac{2j+1}{(n-j)(n+j+1)}=\frac1{n-j}-\frac1{n+j+1}.
$$
将 $n\equiv-1/3\bmod p$ 代入即得可直接复算的第一位公式
$$
\boxed{\ 
\frac{P_n(t)}p\equiv
-2\sum_{\substack{0\le j<n\\ j\ {\rm even}}}V_j
   \left(\frac1{3j+1}+\frac1{3j+2}\right)
-\frac1{2V_{n-1}}\pmod p .\ }
$$
这里 $3j+2\le 3(n-2)+2=p-5$，所以求和中的逆元都存在。初值 $V_0=V_1=1$，在 $\mathbf F_p$ 用
$$
(j+1)V_{j+1}=(2j+1)c_j V_j-jV_{j-1},\qquad
c_j=\begin{cases}1,&j\ {\rm even},\\1/2,&j\ {\rm odd}\end{cases}
$$
即可随递推逐项求和。若把一次域求逆计为一次域运算，时间为 $O(n)$，只需固定数量的域元素作工作空间。直接模 $p^2$ 递推同样是线性步数；这条推论的增量在于所有输入计算均只需模 $p$，并去掉平方多项式的系数卷积。

| $p$ | $n$ | $V_{n-1}$ | 公式中不含 $-2$ 系数的和 | 预测及直接求得的 $P_n(t)/p\bmod p$ |
|---:|---:|---:|---:|---:|
| 21157 | 7052 | 13330 | 15425 | 2729 |
| 21139 | 7046 | 14525 | 12443 | 3791 |

程序另对 $0\le n\le24$ 在有理数域逐系数核验完整的原函数公式。大素数例分别取自两个指定剩余类。验证用的模 $p^2$ 路线和上表的预测路线从同一规范化初值出发，只在最后比较除值。更高精度须重新保留上面按模 $p$ 消失的项。[标准库复算程序](legendre_primitive_check.py)


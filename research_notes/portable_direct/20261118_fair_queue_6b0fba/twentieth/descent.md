# 固定 P11 点的三等分域与素数密度

取原始核 $(r,s)=(11,8)$，其勾股三边为 $(57,176,185)$，$P=233,\ Q=119$。原返回把严格解 $(D,U,V)=(105,208,56)$ 送到
$$
 E:\ y^2=f(x)=x(x-P^2)(x-Q^2),\qquad H=(194089,69872040).
$$
它已证 $H$ 非挠，原有理点族为 $[n]H$。后续均匀挠点稿还确定了原始曲线族的有理挠子群。本稿计算九个三等分点组成的集合 $S=[3]^{-1}(H)$ 在伽罗瓦与约化下的行为。固定曲线的认证二下降另有已用尽预算的返回，记录科学执行次数为零。本计算与该证书、秩及二主 Tate–Shafarevich 群的判定相互独立。[原始点和有理点族，§§3–5](https://github.com/awdawmip/enterprise-math/blob/0b7b96e5d63e22c9937c5c7ae5833c8d48a5bcfb/research_artifacts/mcp/RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC/MCP-b4bf84ccfffc4affacc0f551cb1fa0ad/e486dcbc06d80c035317/RETURN.md) · [均匀挠点稿](https://github.com/awdawmip/enterprise-math/blob/a68132d8f8155e94723533417e04fa45f7ea3d81/research_notes/owner_goal_20261016/p11_uniform_torsion/P11_UNIFORM_TORSION_AND_EMPTY_OR_INFINITE_STRICT_FIBER_PAPER.md) · [固定二下降题书](https://github.com/awdawmip/enterprise-math/blob/5f21d0f7623ace4d0cacfec16988296adda46e27/research_tasks/P11_FIXED_233_119_CERTIFIED_2_DESCENT_RANK_BUDGET_V2_20261016.md) · [原执行边界](https://github.com/awdawmip/enterprise-math/blob/a4bc616941ea24b468321a9a9fef2abff73d047b/research_artifacts/mcp/RS-P11-FIXED-233-119-CERTIFIED-2-DESCENT-RANK/MCP-387e35a6a7d24e8cb2c44e361b9ce5b9/e61b5751d0e8fd837a98/P11_RESOURCE_BOUNDARY_RETURN.json)

**定理。** $E[3]$ 的线性伽罗瓦像为 $\mathrm{GL}_2(\mathbf F_3)$。选一个三等分点作原点，$S$ 的仿射伽罗瓦像为 $\mathbf F_3^2\rtimes\mathrm{GL}_2(\mathbf F_3)$，阶 $432$。每个三等分点单独生成九次数域。有理数域的有限扩张若含任意一个三等分点，其次数必为 $9$ 的倍数。

写 $N_p=\#\{R\in E(\mathbf F_p):[3]R=\bar H\}$。对 $p\nmid 6PQ(P^2-Q^2)$，$N_p$ 取 $0,1,3,9$。各列是素数的自然密度，最后两列以相应同余类内全部素数为分母。

| $N_p$ | 所有素数 | $p\equiv1\bmod3$ | $p\equiv2\bmod3$ |
|---:|---:|---:|---:|
| 0 | $8/27$ | $56/216$ | $72/216$ |
| 1 | $9/16$ | $135/216$ | $108/216$ |
| 3 | $5/36$ | $24/216$ | $36/216$ |
| 9 | $1/432$ | $1/216$ | $0$ |

### 三个好素数确定全局像

令 $a=-(P^2+Q^2)$，$b=P^2Q^2$，于是 $f=X^3+aX^2+bX$。原返回已有的三除多项式
$$
 \psi_3=3X^4+4aX^3+6bX^2-b^2
$$
给出四条三挠直线的四个不同横坐标。每条线恰有一对互负的非零点。两处首一化的约化为
$$
\begin{aligned}
p=13:\quad &(X-6)(X^3-5X^2+4X-2),\\
p=41:\quad &g=X^4+13X^3-4X^2-15 .
\end{aligned}
$$
前一三次式在 $\mathbf F_{13}$ 无根。模 $g$ 有 $X^{41^2}\equiv-16X^3+9X^2+6X+5$，且 $\gcd(g,X^{41^2}-X)=1$，从而 $g$ 无一次、二次因子，必不可约。射影像含三循环和四循环，阶被 $12$ 整除。$S_4$ 唯一指数二子群 $A_4$ 不含四循环，于是射影像为 $S_4$。

四循环的任一线性提升 $M$ 没有 $\mathbf F_3$ 特征线，特征值为 $\lambda,\lambda^3\in\mathbf F_9^\times$。$M^4$ 是标量。若为 $I$，则 $\lambda^4=1$，特征值之比 $\lambda^{-2}$ 的阶至多 $2$，与射影阶 $4$ 矛盾。因此 $M^4=-I$，线性像含全部标量，其阶为 $48$。

在 $p=23$ 用群律得到
$$
\#E(\mathbf F_{23})=24,\qquad \bar H=(15,18),\qquad [8]\bar H=(2,9)\ne O .
$$
若 $H=[3]R$ 且 $R$ 有理，好约化会给 $[8]\bar H=[24]\bar R=O$，故 $S$ 没有有理点。设仿射像为 $G$，平移核 $W\subseteq E[3]$ 受完整线性像稳定，因此 $W=0$ 或 $E[3]$。若 $W=0$，$G$ 中 $-I$ 的唯一提升是中心元，在 $S$ 上形如 $v\mapsto-v+t$，仅固定 $t/2$。中心性迫使全群固定此点，与模 $23$ 证据矛盾。于是 $W=E[3]$，得到所述全仿射像。平移子群的传递性给出次数 $9$。这个平移核论证同样适用于奇素数 $\ell$、完整模 $\ell$ 线性像且 $H\notin\ell E(\mathbf Q)$ 的曲线与标记点。

### 一条可直接约化的九次不可约式

设 $h=x(H)$ 及
$$
r=X^6+2aX^5+5bX^4-5b^2X^2-2ab^2X-b^3,\qquad
F_H=(X-h)\psi_3^2-8f r .
$$
由倍乘公式 $\psi_2=2y,\ \psi_4=4yr$ 和 $x([3]R)=x(R)-\psi_2(R)\psi_4(R)/\psi_3(R)^2$，$F_H$ 是以 $S$ 的横坐标为根的首一九次式。$H\ne-H$ 保证 $S$ 中两点不能共用横坐标。横坐标和点的稳定子相同，因此此式在 $\mathbf Q$ 上不可约，分裂域的次数恰为 $432$。在上述好素再满足 $p\nmid y(H)$ 时，同一公式逐个匹配有理横坐标与有理三等分点。对 $\bar H=-\bar H$ 的好素，密度定理的对象仍是点的纤维，此时横坐标可能合并。

### 素数密度及向原始点族传递

好约化处 $[3]$ 有限 étale，纤维的有理点数等于 Frobenius 在九个几何点上的不动点数。令仿射元素为 $v\mapsto Mv+t$，$k=\#\ker(M-I)$。九个平移中恰有 $9/k$ 个可解 $(I-M)v=t$，每个可解情形有 $k$ 个解。线性群内 $k=1,3,9$ 分别有 $27,20,1$ 个矩阵。计数可按非零向量计算。每个非零向量的稳定子阶为 $6$，固定非零向量的关联对共有 $8\cdot6$ 个，其中恒等贡献 $8$，每个 $k=3$ 的矩阵贡献 $2$。行列式一的子群传递地作用在同样八个向量上，稳定子阶 $3$，相应三个计数为 $15,8,1$。行列式由 Weil 配对给出 $p\bmod3$。逐项乘以平移数并用切博塔廖夫密度定理，即得表中三列。

对任意 $n\in\mathbf Z$ 与 $T\in E[2](\mathbf Q)$，若 $3\nmid n$，则 $R\mapsto[n]R+T$ 把 $S$ 伽罗瓦等变地双射到 $[3]^{-1}([n]H+T)$，因为 $[3]T=T$ 且 $[n]$ 在 $E[3]$ 上可逆。因此这批点有相同分裂域，且**逐个好素**有同样数目的三等分点。若 $3\mid n$，则 $[n/3]H+T$ 已是有理三等分点，该纤维等变同构于 $E[3]$。这时 $N_p=1,3,9$ 的密度分别为 $9/16,5/12,1/48$。这些结论作用于原返回保留符号的椭圆点。去符号并作整数原始归一化后的元组需要通过原映射解释。

### 复算

同目录以 Python 3.8+ 执行下列命令，标准输出对应 descent_checked.json。

    python descent_check.py

程序只用标准库，验证上述多项式分解与最大公因式、模 $23$ 群律见证和 $432$ 个仿射元素的不动点数。另用两条计算路径逐点核对有限域中的横坐标根与有序对三倍映射。在 $p=23,13,89,2833$ 依次得到 $0,1,3,9$ 个原像，其中 $p=2833$ 的九个横坐标为 $139,358,703,1037,1823,1972,1983,2414,2576$。四个素数给出四种取值的实例。表内密度来自全局像与切博塔廖夫定理。

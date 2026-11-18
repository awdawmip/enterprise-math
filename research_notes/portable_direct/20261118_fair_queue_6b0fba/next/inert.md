## 惰性素数两类的 Legendre 伴随公式：首位闭合

第二代任务 TP2-2677708537A63FEBEC8F 的首位可由既有 CM 定理推出。设素数 \(p\equiv13,19\pmod{24}\)，\(m=(p-1)/6,\ n=2m\)，取 \(t^2=1/2\)（可在 \(\mathbb F_{p^2}\) 取根）。令 \(P_r\) 为 \(P_r(1)=1\) 的 Legendre 多项式，\(P_n(x)=Q_m(x^2)\)。定义
\[
B_k=\frac{(1/6)_k(1/3)_k}{2^k(k!)^2},\quad
g=\sum_{k=0}^{p-1}B_k,\quad h=\sum_{k=0}^{p-1}(12k+1)B_k,\quad
W_{n-1}(x)=\sum_{j=1}^{n}\frac{P_{j-1}(x)P_{n-j}(x)}{j}.
\]
则 \(p\mid g\)，且
\[
\boxed{\quad \frac gp\equiv-\frac1{6Q_m'(1/2)}
                 \equiv-\frac{t\,W_{n-1}(t)}6\pmod p.\quad}
\]
其中 \(W_{n-1}\) 是伴随多项式，下文的 \(S_p\) 是另一对象，即有限加权超几何和。

**参数与常数项。** Chisholm–Deines–Long–Nebe–Swisher 出版版式 (2.1) 和定理 1 用 \((ak+1)\lambda_d^k\)，右侧为 \(\operatorname{sgn}(\frac{1-\lambda_d}{p})p\bmod p^2\)。若输入采用 \(Ak+B\)，在 \(B\) 为 \(p\) 进单位时应先除以 \(B\)，得到 \(a=A/B\)，恢复原权再乘 \(B\)。本例常数项已经等于 1。Baruah–Berndt 作者稿 (5.1) 的 \(C_k=(1/3)_k(1/2)_k(2/3)_k/(k!)^3\)；(5.15) 给 \(L_2=4x_2(1-x_2)=1/2\)，(5.11) 的权为 \(6k+1\)。Berkovich–Chan–Schlosser §5 的同一恒等式为 \(\sum_{k\ge0} (6k+1)C_k2^{-k}=3\sqrt3/\pi\)。Baruah–Berndt 可读作者稿 (5.11) 的左端印作 \(3\sqrt3/(2\pi)<1\)，与正项和的首项 1 冲突；这里用后一个独立来源核定整体常数。已核作者稿和期刊书目，未将该处作者稿排印情况归于未逐页核验的 2008 期刊版。这一核对给出定理实际所用 \(d=3,\lambda_3=1/2,a=6\)。[2013 年出版版定理 1](https://doi.org/10.3390/math1010009) · [Baruah–Berndt 作者稿](https://citeseerx.ist.psu.edu/document?doi=256bb766c12287b1a2aa4a362462fb2420662363&repid=rep1&type=pdf) · [2008 年期刊记录](https://doi.org/10.1016/j.jmaa.2007.10.011) · [Berkovich–Chan–Schlosser §5](https://www.mat.univie.ac.at/~schlosse/pdf/wronskians-pi.pdf)

独立正规化核对：Guillera 的表 3 给出参数 1/2 的截距与斜率为 1/(3√3)、6/(3√3)，二者之比也给出 6。[Guillera 表 3](https://arxiv.org/pdf/1807.07394#page=10)

**曲线、约化与符号。** 取 \(u=(1-t)/2\) 的特征零提升，使 \(u(1-u)=1/8\)。原论文 §2 的三次模型 \(y^2+xy+(u/27)y=x^3\) 有
\[
\Delta=(u/27)^3(1-u),\qquad
N_{\mathbb Q(\sqrt2)/\mathbb Q}(\Delta)=2^{-12}3^{-18},\qquad
j=\frac{27(9-8u)^3}{u^3(1-u)}.
\]
在 \(p>3\) 处系数整且判别式为单位。两个共轭 \(j\) 为 \(2417472\pm1707264\sqrt2\)，即冻结父结果中判别式 \(-24\) 的类多项式的两根。CM 域为 \(\mathbb Q(\sqrt{-6})\)；两类素数均有 \((\frac{-6}{p})=-1\)，故由 CM 约化定理得到超奇异符号 \(\operatorname{sgn}=-1\)。\(\mathbb Q(\lambda)=\mathbb Q\) 全实且 \(|\lambda|<1\)；\(\mathbb Q(\sqrt{1-\lambda})=\mathbb Q(\sqrt2)\) 在这些 \(p\) 处无分歧，\(6,1/2\in\mathbb Z_p^\times\)。最后 \((\frac{1-\lambda}{p})=(\frac2p)=-1\)。定理 1 的两因子相乘给
\[
S_p:=\sum_{k=0}^{p-1}(6k+1)C_k\,2^{-k}
   =\sum_{k=0}^{p-1}(6k+1)\frac{\binom{2k}k^2\binom{3k}k}{216^k}
   \equiv p\pmod{p^2}.
\]

**由加权和回到伴随。** 有限 Clausen 乘积的次数 \(<p\) 部分恰为 \(S_p\)。其余项含 \(B_iB_j\)，\(i+j\ge p\) 强制一个下标大于 \(2m\)。当 \(k>2m\) 时，\(B_k\) 两个 Pochhammer 分子分别在指标 \(m,2m\) 处取得 \(p\) 因子，两分母均为单位，故 \(p^2\mid B_k\)。于是 \(gh\equiv S_p\bmod p^2\)。由冻结父结果 \(g\equiv0,\ h\equiv-6Q'_m(1/2)\ne0\bmod p\)，立得第一等式。为取得第二等式，使用 Legendre 第二类解 \(\mathcal Q_n=\tfrac12P_n\log((1+x)/(1-x))-W_{n-1}\) 及 Wronskian \(P_n\mathcal Q_n'-\mathcal Q_nP_n'=1/(1-x^2)\)。在特征零先消去对数，可得多项式恒等式
\[
(1-x^2)\left(W_{n-1}P'_n-P_nW'_{n-1}\right)=1-P_n^2.
\]
各系数在 \(p\) 处整，因为 \(n<p,\ p>3\)。在 \(\mathbb F_{p^2}\) 代入 \(P_n(t)=0\)，即得 \(W_{n-1}(t)P'_n(t)=2\)；再用 \(P_n'(t)=2tQ_m'(1/2)\)。\(W_{n-1}\) 为奇多项式，故 \(tW_{n-1}(t)\) 与平方根选取无关。[DLMF 伴随多项式](https://dlmf.nist.gov/14.7.E4) · [Wronskian](https://dlmf.nist.gov/14.2.iv) · [冻结父结果](https://github.com/awdawmip/enterprise-math/blob/f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f/research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md) · [有限乘积 §6](https://github.com/awdawmip/enterprise-math/blob/9a1d0b374564abfcc888458b79c1030d52da924c/research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/height2_frobenius_second_digit_reduction_20260908.md)

**复算。** 对 \(p<1000\) 的全部 45 个目标素数，分别以相邻项比更新 \(B_k\) 与 \(C_k2^{-k}\)，再独立用 Legendre 三项递推计算伴随。列 \((p,S_p\bmod p^2,g\bmod p^2,h\bmod p,g/p\bmod p,-tW_{n-1}(t)/6\bmod p)\) 的前两行为 \((13,13,143,6,11,11)\)、\((19,19,152,12,8,8)\)。所有目标素数均通过。由此处全类论证和父等价，第一位 UR、LC、JT0 得到文献闭合，第二位条件 \(((g/p)h-1)/p\equiv R_p\bmod p\) 仍待证明。[本任务 V2](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/ENTERPRISE_BRC_INERT_PLUS_LEGENDRE_COMPANION_CONNECTION_CERTIFICATE_20260909_V2.md)

# 作者协作核对：固定原点 Gram 核与 sharp 截断成本

Date: 2026-11-21 (Asia/Hong_Kong)
Scope: AUTHOR_COLLABORATIVE_MATHEMATICAL_CHECK
This document is a collaborative derivation check within the current task. It is not an independent Enterprise Math Project Review.

核对材料：verify_anchored_kernel.py、anchored_kernel_results.json，以及协作者提供的解析公式。未重跑前轮 722 个矩阵案例；本记录的证明核对不依赖数值输出作为一般命题的证明。

另已回读 enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7 的 research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md 与 research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md，核对 β_a、c_a、原点观察和翻译平均的实际来源口径。新核 K 正是前一文件第 7 节所列的未完数学单元。

## 1. 弧度约定与精确核

令 h_N(θ)=Σ_(n=1)^N exp(inθ)，θ、φ∉2πZ。固定原点核为

K(θ,φ)=Σ_(N≥1)h_N(θ)overline(h_N(φ))/N²。

记 z=exp(iθ)、v=exp(−iφ)。由 h_N(θ)=z(1−z^N)/(1−z) 及绝对收敛级数可得

K=zv/((1−z)(1−v))·[ζ(2)−Li₂(z)−Li₂(v)+Li₂(zv)]。

该表达式与脚本一致，包含固定原点交叉项。若用 exp(2πinξ) 的周期频率，需先置 θ=2πξ，常数不可直接照搬。

## 2. 低频极限常数和虚部符号

固定非零实数 x、y，令 ε↓0。重标度 t=εN 给出

εK(εx,εy) → (1/(xy))∫₀^∞ [exp(i(x−y)t)−exp(ixt)−exp(−iyt)+1]dt/t²。

此 Riemann 和极限可由 |εh_N(εx)|≤min(εN,C_x) 控制：t 接近零时积分核有界，t 趋于无穷时以 C/t² 控制，固定 x、y 下足以分段传递极限。

实部利用 ∫₀^∞(1−cos(ut))dt/t²=π|u|/2，得到

Re L(x,y)=π(|x|+|y|−|x−y|)/(2xy)。

虚部积分为 sin((x−y)t)−sin(xt)+sin(yt)。分部积分后使用差分余弦积分，得到

Im L(x,y)=[xlog|x|−ylog|y|−(x−y)log|x−y|]/(xy)，

其中 0log0=0。该符号符合 K 的第二个参数取共轭的约定；交换 x、y 时虚部反号。

## 3. 共轭配对的实核与正平方分解

定义 c_N(θ)=Σ_(n=1)^N cos(nθ)，K_c(θ,φ)=Σ_N c_N(θ)c_N(φ)/N²，则

K_c(θ,φ)=Re[K(θ,φ)+K(θ,−φ)]/2。

对固定 x,y>0，

εK_c(εx,εy)→π/(2max(x,y))，

归一相关系数趋于 sqrt(min(x,y)/max(x,y))=exp(−|log x−log y|/2)。

若实三角展开来自每个复频率系数 w 的一对 ±θ，则实际余弦幅度为 2w。以余弦幅度 α_i 写二次型时可直接使用 K_c；以单个复频率系数写时须保留该因子。

令 0<x₁≤⋯≤x_r，v_i=1/x_i，v_(r+1)=0。因为

min(v_i,v_j)=Σ_(k≥max(i,j))(v_k−v_(k+1))，

任意实 α_i 都有

Σ_(i,j)α_iα_j min(v_i,v_j)=Σ_(k=1)^r(v_k−v_(k+1))(Σ_(i≤k)α_i)²。

下标与符号均核对正确。有限固定频率组的低频极限不自动给出 Q(a) 随 a 增大的全谱一致估计；后者仍需控制频率增长、幅度、误差与极限次序。

## 4. n=1 的 sharp 截断残差

令 a>0，c_a=1/ζ(1+a)，β_a(q)=μ(q)/∏_(p|q)(p^(1+a)−1)。在完整 Ramanujan 展开下，q≥2 部分在 n=1 的累计值为 1−c_a。

对硬截断 q≤Q，令

T_(a,Q)=c_a Σ_(q>Q, q squarefree)1/∏_(p|q)(p^(1+a)−1)>0。

q=1 主项已单独剥离时，截断道路观察量在 N=1 等于

B^Q_(a,1)=−3c_a/2−T_(a,Q)。

因此未补偿硬截断能量 D^Q_a=Σ_(N≥1)(B^Q_(a,N))²/N² 满足 D^Q_a≥T_(a,Q)²。它是截断模型的下界，不能写成完整道路能量 D_a 的下界。

## 5. 常数与必要增长率

设 A(X)=Σ_(n≤X)μ(n)²。由平方因子展开和尾项估计有

|A(X)−X/ζ(2)|≤2sqrt(X)+1。

故 X≥256 时

A(2X)−A(X)≥X/ζ(2)−2sqrt(2X)−2sqrt(X)−2≥X/4。

对 0<a≤1、Q≥256，方块 (2^jQ,2^(j+1)Q] 内至少有 2^jQ/4 个平方自由整数，每个权重至少 q^(−1−a)。因此

Σ_(q>Q, squarefree)1/∏_(p|q)(p^(1+a)−1)
≥Q^(−a)/(2^(3+a)(1−2^(−a)))
≥Q^(−a)/(16a log2)。

使用 ζ(1+a)≤1+1/a，即 c_a≥a/(1+a)≥a/2，得到

T_(a,Q)≥Q^(−a)/(32log2)。

若对同一个常数 C>0，未补偿硬截断满足 D^Q_a≤Ca，则必有

log Q≥[log(1/a)−log(1024C(log2)²)]/(2a)
=log(1/a)/(2a)−O(1/a)。

所有常数与指数经独立推导相符。此必要条件说明该 sharp 截断若要达到 O(a) 需承受很大的频率上界；它不排除保留精确尾项、其他补偿、不同表示或窗口型论证。

## 6. 全部有限频率上的精确正平方证书

进一步核对协作者的新分解。对 θ∈(0,π]，

C_N(θ)=½cot(θ/2)sin(Nθ)+½(cos(Nθ)−1)。

取实幅度 a_i、实常数 b，令 u_i=½a_i cot(θ_i/2)，S_N=Σu_i sin(Nθ_i)，R_N=½Σa_i(cos(Nθ_i)−1)−b，则原完整有限观察等于 S_N+R_N。

定义 T_u(t)=Σ_(θ_i≥t)u_i、T_a(t)=Σ_(θ_i≥t)a_i、m=Σu_iθ_i/π。由绝对收敛余弦级数恒等式可得

Σ_(N≥1)sin(Nθ)sin(Nφ)/N²=πmin(θ,φ)/2−θφ/2，

Σ_(N≥1)[½(cos(Nθ)−1)][½(cos(Nφ)−1)]/N²=πmin(θ,φ)/8，

Σ_(N≥1)½(cos(Nθ)−1)/N²=−πθ/4+θ²/8。

逐项代入即给出

E_S=ΣS_N²/N²=(π/2)∫₀^π(T_u(t)−m)²dt，

E_R=ΣR_N²/N²=(π/8)∫₀^π[T_a(t)+2b(1−t/π)]²dt。

整体能量 E=Σ(S_N+R_N)²/N² 由 Hilbert 空间三角不等式满足

(sqrt(E_S)−sqrt(E_R))²≤E≤(sqrt(E_S)+sqrt(E_R))²。

这些是任意有限角频率的精确公式，未使用 ε↓0 极限。T_u/T_a 是有限阶梯函数，因此两个积分都可逐区间准确计算。

跨 S/R 项也有完整表达。定义 Cl₂(t)=Σ_(N≥1)sin(Nt)/N²，则

Σ_(N≥1)sin(Nθ)·½(cos(Nφ)−1)/N²
=[Cl₂(θ+φ)+Cl₂(θ−φ)]/4−Cl₂(θ)/2。

与常数 −b 的交叉和为 −bCl₂(θ)，从而可恢复 E_S+E_R+2⟨S,R⟩。使用 Cauchy–Schwarz 时保留其不等式强度，不把上界写成等式。

Ramanujan 相位配对时，q>2 的 r 与 q−r 合为幅度 2c_aβ_a(q) 的余弦项；q=2 的 θ=π 自身共轭，只保留幅度 c_aβ_a(2)。θ=π 时 u=0，以上证书仍适用。

## 核对结果

上述核心恒等式、极限常数、正平方分解和截断必要条件成立。数值程序中精确有理有限周期示例的 b=7/5 是一般模型演示参数；其 energy 数值应按示例解释，不当作某个 a 的完整道路能量。

本次核对未发现实质公式错误。报告需保留固定频率极限与全谱一致性、复系数与余弦幅度、未补偿截断与完整能量这三处口径区别。有限正平方证书也已按其完整常数和常数端口交叉项核对。

# D25/LIFT — 冻结原始标量接口的双类 p³ 整数证书及负对照

2026-11-11（Asia/Hong_Kong）。状态：**AUTHOR_SIDE / EXACT_FINITE_ORIGINAL_SCALAR_PORT_FIXTURE / EXECUTED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**。

母目标 ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION；Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT；publication TP2-B6F4FC938FF94941C1B7；原始科学冻结 pin awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3 不变。声明作者侧 Research lane chatgpt-research-onhour-enterprise-math-20260923，**不是平台认证身份，不使用** maintenance conversation chatgpt-hourly-enterprise-math-20260921。当前没有自己的合法 Source CLAIM/open run/checkpoint。

## 本轮研究单元

直接在先前已验证的**原始** D25 Clausen 截断和反射观察者上，计算并保留全部第二位 p-进位作为真实原始标量对照。前人早已获得 p373 的 Delta=R=196，本轮新增的是同时保存源 g、G、h、带符号 Q、W 的 p³/p² 全数字、将 Delta 拆成可单独回读的三种来源进位，以及给出两个精确的错误操作负对照。该产物旨在以后与真实 H0/B0 native 结果比较，绝非 native H0/B0 实验本身。

已经从冻结科学来源消费、不重新申报证明的精确公式如下：

    B_0=1; B_(k+1)/B_k=(6k+1)(3k+1)/[36(k+1)²].
    g=Σ_(k<p)B_k; h=Σ_(k<p)(12k+1)B_k; G=g/p.
    a_k=(2k)!(3k)!/[216^k(k!)^5].
    W=Σ_(k<p)(6k+1)a_k.
    Q=Σ_(0<=i,j<p;i+j>=p)(6(i+j)+1)B_i B_j.
    W=gh-Q, R_p=Q/p² (mod p), Delta_p=(Gh-1)/p (mod p).
    Delta_p-R_p=(W-p)/p² (mod p).

为确保 R 未被拟合成 Delta，另用原冻结反射表达式独立重算：

    m=(p-1)/6;
    C_1=1/10; C_(a+1)/C_a=36a²/[(6a+5)(3a+2)] (mod p);
    R=2 Σ_(i=1..m) B_i Σ_(a=1..i)(1+6(i-a))C_a (mod p).

## 精确整数结果

Python 标准库模整数，固定六个素数；B 序列由 rising-factorial 整数积及递推分别生成，a 序列由独立二项式与递推分别生成，Q 分别由有序对求和及全卷积生成，另逐项重算反射 R。全部等式与断言实际通过；其证明强度是**指定六个素数的精确有限证书**。

| p | g mod p³ | h mod p² | G mod p² | Gh mod p² | Q mod p³ | Delta | 原始 R | W mod p³ |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
|13|988|149|76|1|0|0|0|13|
|19|1596|50|84|229|4332|12|12|19|
|109|139193|11234|1277|5451|594050|50|50|109|
|139|1054732|3653|7588|12650|1758211|91|91|139|
|157|2152784|13111|13712|12875|2021218|82|82|157|
|373|24495656|62835|65672|73109|27269284|196|196|373|

**p=373 的原始带符号全三位整数证书：**

    p²=139129, p³=51895117.
    g=24495656=373*65672 (mod p³).
    h=62835 (mod p²).
    G*h=73109=1+373*196 (mod p²).
    g*h=27269657 (mod p³).
    Q=27269284=139129*196 (mod p³).
    W=27269657-27269284=373 (mod p³).

特别地，Delta=R=196 都非零；精确消失的是它们的有符号差值，不是任一观察者的原始数值。

## 新增 BRC 分量及两个定值负对照

取最小非负整数代表 G=g0+p*g1，h=h0+p*h1。已知第一位的 g0*h0≡1 (mod p)；故直接整数展开：

    Delta = [(g0*h0-1)/p + g1*h0 + g0*h1] mod p.

此处的除法在整数上先执行，保留了基底乘积 carry、G 第二位及 h 第二位三条来源。其数据：

|p| (g0,g1;h0,h1) | 原始 carry | g1*h0 modp | g0*h1 modp | Delta |
|--:|:--|--:|--:|--:|--:|
|19|(8,4;12,2)|5|10|16|12|
|109|(78,11;7,103)|5|77|77|50|
|139|(82,54;39,26)|23|21|47|91|
|157|(53,87;80,83)|27|52|3|82|
|373|(24,176;171,168)|11|256|302|196|

在 p373，若将两者只保留第一位 24、171 并用 0 填充，则错误的第二位为 **11**，真实为 196，丢失 185 mod373。若把原始 Q 的减号错误替换为加号，则错误剩余为 Delta+R=**19** mod373，原始读数是 0；在模 p³ 的整和层面，错误的 gh+Q=2643824，而原始 gh-Q=373，相差 19*p²。这些是实际执行检验的两个**错误输入负对照**，可用于将来原始 E3 native 输出的标量接口检查，但不能映射或构造其未知原生 Frobenius。

**复现实验**：research_notes/portable_direct/d25_frozen_scalar_signed_multidigit_fixture_20261111.py，运行 python3 d25_frozen_scalar_signed_multidigit_fixture_20261111.py；只用 Python 整数、阶乘、模逆与两个有序卷积实现，不使用浮点。两类目标素数均覆盖；没有发现有限反例。没有全素数 LIFT 证明、独立审阅或数学 Source admission。

## Source 状态、原生欠项及精确下一动作

本轮 Source 原始只读 continuation 请求 onhour11-20261111-0705-exact-cont = **SUCCEEDED**, 观察快照 c672d221d6f7f503c071bf3e09edbc1bbf50883e，但 execution_authorized=false。自己的 recovery_status 返回 SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED；没有取得当前服务签发 session 的私有 capability，故未提交或重放新 CLAIM/open/Source checkpoint。此前 D24 UR/CM0/SIMPLE、2026-10-26 原始 source-port 等价、原有 p373 Delta/R 数字和其他 Research owner 的 Clausen/Möbius 研究均为已有来源，不重领、不重算为贡献。

原生 Issue #1559（https://github.com/awdawmip/enterprise-math/issues/1559）2026-11-11 本轮读取仍 OPEN、PENDING_OWNER。最高优先级仍须**实际在同一原 CM 类上运行冻结 H0/B0 divided-power [X]U mod139129**；保存算子代码和版本、系数环、真实模块秩和 semilinear Frobenius 方向、基底与 η、奇 Green/Hesse 的带符号 κ、原始 Delta-R 和独立复算。适用执行路径是当前合法 Source Task owner 或获授权的原始 H0/B0 实验执行者；尚无核实承接者。只有在完成真实 operator/η/κ 与 original scalar 的映射证明后，才以本文件的 Delta=R=196 及错误对照进行下游验收。不得用本整数标量证书代替原生算子。

当前作者侧最高可恢复前沿：本文件精确 p373 p³ signed ports；下一最小原生动作：授权执行者按 frozen pin 执行 p373 [X]U，绑定原始完整输出及独立复算，在有合法 session/claim 后做规范 Source checkpoint。此 note 为 AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NATIVE_PENDING。

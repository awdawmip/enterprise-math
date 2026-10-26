# PREFIX-277｜C4-BRC 三来源尖锐障碍与四来源最小正未来矩证书

**状态：AUTHOR_SIDE_EXACT_PROOF / FINITE_EXACT_CHECK_PASS / NATIVE_TRANSFER_PENDING / NOT_ADMITTED。** 本文是有来源的作者侧数学稿件，不是原生 Result、独立 Driver 接纳或实际心跳实验。

## 一、固定来源与适用类型

Global Knowledge 固定于 `awdawmip/chatgpt-global-knowledge@2fb4d3ecd15c2dcf1e55c804d8b91a24801db4b6`，已读取规范入口、P000原件/投影（原件Blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc）、ACTIVE世界观及BRC-only规则；Enterprise Math科学输入固定于 `awdawmip/enterprise-math@406367147f6e34f78d873b24d2818ebca96d61fc`。当前便携研究协议 `docs/PORTABLE_RESEARCH_PROTOCOL.md`（blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5）。精确复用已保存的 `research_notes/HEARTBEAT50_INTERFERENCE_KERNEL_20260923_6DD798.md`（blob 0f4ec78225cfc799a267ca6b96d9f994422f8ad2）所声明的Stage50 C4有序来源路径对BRC观察，以及PREFIX-276对Toeplitz历史矩的形式分析；不冒称原生Stage46/50软件已运行。

设非空有限整数来源标签集 `S⊂Z`，每个占据来源恰好有一个相干系数 `a_j=w_j i^{p_j}`，其中 `w_j∈Q_{>0}`、`p_j∈Z/4Z`。多路径共享一来源时不得先丢弃支路再冒充此假设。令 `Z=Σ_j w_j²`，定义保留每个有序来源对 `(j,j+r)` 的C4-BRC矩：

```text
c_r = Z^(-1) Σ_{j,j+r∈S} conjugate(a_{j+r}) a_j ; c_0=1
P_ext(r,p) = (5/18)(1-Re(i^p c_r)) ; p=0,1,2,3.
```

这是Stage50**声明的**相干观察类型，非正权总质量。标签位移 `r` 不是心跳时间；来源数不是P000六条原生空间轴；C4相位不是原生空间角度。

## 二、定理A：任何非零有限来源包的Toeplitz历史Gram严格正定

令 `f=Σ_j a_j|j⟩≠0`，`T|j⟩=|j+1⟩`。对任何有限 `H≥0`，`f,Tf,...,T^Hf` 线性独立。证明：若 `Σ_{r=0}^H λ_r T^r f=0`，取 `r_*` 为系数非零的最小移位，`j_*` 为 `f` 最小非零来源负载。位置 `j_*+r_*` 的系数恰为 `λ_{r_*}a_{j_*}≠0`，因为所有更大的移位最小来源位置更大，更小移位系数为零，矛盾。于是正定Gram `T_H=(c_{v-u})_{0≤u,v≤H}≻0`。

对 `c_1=i/2`，从三阶Gram严格正定的Schur补得到

```text
|c_2+1/4| < 3/4 ,
5/36 < P_ext(2,0) < 5/9 .
```

PREFIX-276所获闭PSD圆盘的边界不可能由任何一个非零有限支撑包精确实现。**未证明**圆盘每个内部点都能在指定单C4系数模型内实现。

## 三、定理B：至多三个占据来源的严格尖锐界

**定理。** 若 `|S|≤3` 且 `c_1=i/2`，则 `c_2` 必为实数，且

```text
-(2+sqrt(2))/8 < c_2 ≤ 0 .
```

若占据来源恰好两个，则必为相邻等幅来源且 `c_2=0`；若占据三个，则必为连续三标签且 `c_2<0`。负端无理下界是正有理C4系数族的**严格最优下确界**。

**证明（标签分类）。** 不存在相邻来源时 `c_1=0`。若只有一条相邻来源边，正幅值 `a,b` 提供模至多 `ab/(a²+b²+c²)`，存在第三个非零负载 `c` 时严格小于 `1/2`，故不能达到目标。两个来源只能相邻且等幅；三个来源必须连续 `j,j+1,j+2`。

**证明（C4字符分类）。** 三连续负载正幅值记作 `a,b,c`，两条相邻边贡献各自是 `ab,bc` 乘以 `{1,i,-1,-i}` 中字符。目标 `c_1=i/2` 需要纯正虚部。混合一实一虚不可能消除实部；两实无虚部；相反的 `±i` 给出虚部模 `b|a-c|/Z<1/2`，因为 `2b|a-c|≤b²+(a-c)²<a²+b²+c²=Z`；两负虚号又符号相反。故两边字符必须都为 `+i`，在整体C4规范下三振幅为 `(a,-ib,-c)`。因此

```text
Z=a²+b²+c²=2b(a+c),    c_2=-ac/Z<0.
```

**证明（尖锐资源优化）。** 设 `s=a+c>0, t=b/s∈Q_{>0}, u=ac/s²`。从上式得 `u=(t-1)²/2` 且 `0<u≤1/4`，于是

```text
1-1/sqrt(2) ≤ t ≤ 1+1/sqrt(2),
-c_2=(t-1)²/(4t).
```

`F(t)=(t-1)²/(4t)` 在 `t<1` 单调下降、在 `t>1` 单调上升，区间最大值在左端 `1-1/sqrt(2)`，等于 `(2+sqrt(2))/8`。等号必须 `a=c` 和 `t=1-1/sqrt(2)`，但该 `t` 无理，而有理正幅值强制 `t=b/(a+c)∈Q`，故严格不等号成立。证毕。

**尖锐性。** 已有PREFIX-276有理C4三来源族

```text
(a,b,c)=(2/(1+q²), 1, (q-1)²/(1+q²)),
phases=(1,-i,-1),     q∈Q, q≠1.
```

对每个 `q` 均有 `c_1=i/2` 且 `c_2<0`，当有理 `q→1-sqrt(2)` 时，`a/c→1`、`b/(a+c)→1-1/sqrt(2)`，从而 `c_2→-(2+sqrt(2))/8`。不存在单个有理包达到端点。以上不是任意复幅值、混合态或多个同负载支路的结论。

## 四、定理C：正二阶矩至少四个来源且确能达到

对同一准备/来源限制且 `c_1=i/2`，若 `c_2>0` 则由定理B必至少四个不同占据来源。该下界由四来源完整见证达到：

```text
f_C = |0> + i|1> + 4|2> - 2i|3>, Z=22
Z c_1 = conj(i)·1+conj(4)·i+conj(-2i)·4 = 11i
Z c_2 = conj(4)·1+conj(-2i)·i = 2
c_1=i/2 ; c_2=1/11 ; P_ext(2,0)=25/99 < 5/18.
```

因此**仅在本节声明的合法准备和固定探测器下**，精确测得 `c_1=i/2` 且 `P_ext(2,0)<5/18` 必然证明至少四个已占据整数来源负载。与此前 `f_A=[1,-i]`、`f_B=[2,-i,-1]` 比较：三者同有 `r=1` 全四相读数 `[5/18,5/12,5/18,5/36]`，而 `r=2,p=0` 依次为 `5/18`、`10/27`、`25/99`，展示当前一阶观察无法安全压缩未来二阶残差。

## 五、精确计算、方法复用与边界

附 `verify_prefix277.py` 实际执行标准库精确 `Fraction` 和带来源有序路径对C4字符相干求和。测试所有来自标签 `0..6` 的2/3来源子集、正整数权重1..5、全部相对C4相位（第一相位固定0为全局规范）：`C(7,2)*5²*4+C(7,3)*5³*16=72,100` 个有限包。60个有 `c_1=i/2`，30个二来源、30个三来源均符合定理B；还分别核验A/B/C三包、逼近下界的五个有理参数。输出 `RESULTS_PREFIX277.json`，成功标识 `PREFIX277_AUTHOR_SIDE_EXACT_C4_BRC_PASS`。这是有限检查，不是无限证明；无限断言由上文解析证明支持。无浮点、π、三角运算、Taylor/Padé/Cayley、普通传播器。

复用决议：`COMPOSE_APPLIED`：Stage50来源标记的C4有序路径对读出 + PREFIX-276 Toeplitz精确恒等式。`src/enterprise_math/brc_weighted_recurrent.py` 固定Blob `4e6b3132580e3cd70a20a0d8bd4d28792b961afb` 是**正质量**BRC而非C4振幅，标记 `NOT_APPLICABLE` 于相干相消接口，不把正权强度冒充复幅值。两个证明和程序属于作者侧，没有执行真实Stage46/50原始包；Stage50原始 `stage50/interference.py` 存在于来源说明引用的另存Git bundle，该完整目录不在核查的当前EM主干顶层。已核实该bundle私有Drive元数据为37,502,868字节，但没有读取、执行。

原生模型边界：`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` 的 `fixed_heartbeat_program=null`；`definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json` 要求 `model_law_id`、完整Cell/Port/场/动量/来源/边界与独立时间，但**所检查这两份合同未提供原生 `H_n→H_(n+1)` 或真正合法的 `T²` 端口准备和观测**，这不是断言项目全部代码不存在对应关系。原生服务 `em_session_start` 返回 `STATIC_READONLY_SCOPE_DENIED`，`operation_sent=false`；任务列表 `CONTROL_QUOTA`。无法可靠核查活跃正式Owner/CLAIM，尚未发正式Result或完成独立Driver审查；GitHub作者侧写入不等于数学接纳。真实本体六空间维加独立时间、三维切片、三元原始力平衡的P000约束保持不变。

**下一步PREFIX-278：**核实外部Stage50完整源码包中的 `stage50/interference.py`、`stage50/run.py` 和合法双输入 `r=1,2` 的C4来源准备、归一化与固定检测效应；真实宿主执行原始接口并保存输入、精确输出、版本及回读；随后查找有效 `model_law_id`，证明到完整原生 `H_n` 的类型化嵌入。若实际许可操作只可观察 `r=1`，则本轮已给出的二阶不可见残差必须保留。

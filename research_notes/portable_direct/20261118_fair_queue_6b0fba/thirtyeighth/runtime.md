# 三面地址的十进制往返域、路径容量与字节计数

固定注册切片有四个带方向的单位步。若每个输出字段最多使用 $D$ 位十进制数字，令 $T=10^D-1$，则可按规范 JSON 写出并由同一设置读回的地址恰有 $3T^2$ 个。对一条给定的指令字，只需记录三个整数投影在所有前缀上的最小值和最大值，即可算出**沿途每个地址均可往返的起点数**与**允许至少一个起点的最小容量**。若只知道三个前缀跨度的最大值为 $d$，最坏路径需要的单字段数值上界恰为 $\lceil(2d+2)/3\rceil$。

固定实现为 `three_region_slice_v1`、version 1、frame `X6_FIXED_E1_E2_CHART`。2026 年 9 月的既有结果已经证明抽象编解码互逆、原生四步与地址转移及其完整有序词迹相容。本轮将这些结果接到有十进制预算的实际文本边界。第 35 轮研究的三帧旧调用与缓存迁移是另一个任务。[任务书](https://github.com/awdawmip/enterprise-math/blob/b4dbf92417211d7286cad72629080bbdf310f1b4/research_tasks/RS-COORD-RUNTIME-REFINEMENT-20260916.md) · [固定契约](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/coordinate_address_contract.json) · [既有验证及范围](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/research_notes/CELL_SLICE_LEAN_VALIDATION_20260913_A8D47F21.md)

## 一、规范字符串与有类型值

本文的文本输入取普通 JSON 字符串。对象必有且仅有 `schema,codec,version,frame,coordinates` 五个键，各出现一次。三个字符串标签为契约中的 schema、codec、frame，版本的数学值为 1。坐标数组长 6，每个整数词法为 `-?(0|[1-9][0-9]*)`，取值后恰两个正整数、一个零占前三栏，后三栏为零。对象字段次序、合法 JSON 空白和等价字符串转义由 JSON 语法处理。规范输出由原实现的排序键和紧凑分隔符唯一确定。原输入中的 `-0` 在零栏可以通过，重写为 `0`。负的非零坐标被拒绝。原代码禁止小数、指数记法、非常规浮点常量和重复键。精确类型检查还排除布尔值。未知 codec、frame、version、额外键、不合零型、切片外方向均有独立拒绝分支。[实际文本接口](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/src/enterprise_math/cell_address.py) · [JSON Schema](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/schemas/cell_address.schema.json)

三种接口的差别可以直接观察。JSON Schema 对已解析值按数学整数判定，合法位置的 `1.0`、`1e0` 通过该数据模型检验，两种文本均被实际入口拒绝。普通 JSON 解析若先合并相同键，后置 schema 看不见原重复键。注册入口的键值对钩子在该处拒绝。Python 内存对象用 exact `int`，故对大整数直接 `to_wire/from_wire` 可以成功，即使对应十进制输入超过所设位数而不能读回。原测试的原始坐标绝对值最大为 $2^{512}$，不足以触及本机默认的十进制边界。[原有 16 项回归](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/tests/test_cell_address_contract.py)

在有整数十进制转换限制的 CPython 上，原 `from_json` 使用默认整数解析器。本次 CPython 3.12.14 的通常默认值为 4300，允许的最小非零设置是 640，显式设置为 0 表示关闭该位数限制。符号不计入位数。地址的合法正数没有前导零。下文将双向预算具体施加于接口。对已通过类型及零型检查的值，以整数比较逐字段验证 $q_i\le 10^D-1$，写出后经同一设置的注册入口读回。若另设应用预算与解释器输入上限，则取有效上限中较小者。单次格式化成功不能充当双向预算检查。关闭该设置且无应用预算时，每个有限切片地址均有规范文本，实际执行仍以可用内存等通常资源条件为前提。[CPython 文档](https://docs.python.org/3.12/library/stdtypes.html#integer-string-conversion-length-limitation)

## 二、构造、直接步进与十进制六边形

记三种地址为 $A(b,c),B(a,c),C(a,b)$，参数是实际正字段，零位依次为第一、二、三栏。Lean 构造参数为相应正数减一。实际解码依次给 $(1-c,b-c),(a+1-c,1-c),(a,b)$。反向编码按 $m\le 0, n\ge m$ 进入 A，按 $n\le 0, m\ge n+1$ 进入 B，其余为 $m,n\ge 1$ 的 C。三个分支互不重叠、覆盖整平面。以下列出原码的非对称分支。各行条件从左至右取第一个成立者，未给条件的项总是成立。符号 $1\pm,2\pm$ 对应 `E1_FORWARD/REVERSE,E2_FORWARD/REVERSE`。[冻结编码与直接表](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/src/enterprise_math/_cell_slice_codec.py) · [三面定义](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/EnterpriseMath/CellAddress/ThreeRegionSlice.lean) · [已有公开字段与步进结论](https://github.com/awdawmip/enterprise-math/blob/d2984d1a0c5c8221ee103084dd3da68dd039dfaa/EnterpriseMath/CellAddress/Contract.lean)

|输入| $1+$ | $1-$ | $2+$ | $2-$ |
|---|---|---|---|---|
| $A(b,c)$ | $b=1:B(1,c)$。$c=1:C(1,b-1)$。$A(b-1,c-1)$ | $A(b+1,c+1)$ | $A(b+1,c)$ | $b=1:B(1,c+1)$。$A(b-1,c)$ |
| $B(a,c)$ | $B(a+1,c)$ | $a=1:A(1,c)$。$B(a-1,c)$ | $c=1:C(a,1)$。$a=1:A(1,c-1)$。$B(a-1,c-1)$ | $B(a+1,c+1)$ |
| $C(a,b)$ | $C(a+1,b)$ | $a=1:A(b+1,1)$。$C(a-1,b)$ | $C(a,b+1)$ | $b=1:B(a,1)$。$C(a,b-1)$ |

每个活跃字段按 $=1$ 或 $\ge 2$ 分开，三面乘四方向共有 48 个分格。在每格内目标构造固定，正参数的减一只发生在原数至少为二处。代入三个解码式，目标点是原点加对应单位向量。也可逐格查一个基点，并对每个自由字段查该基点加一的差分。两边均为仿射式，以上恰好 96 次取值确定全部系数。这给出实际整数算术下四个直接转移的逐分支推导，JSON/解释器和硬件的全执行语义仍是可信边界。未新作形式化。

**定理 1。** 对任意正整数数值上界 $T$，容许的原始整数点恰为
$$
H_T=\{(m,n):1-T\le m,n,m-n\le T\}.
$$
由三条编码式逐面比较两个正坐标与 $T$ 即得。另一写法是所需容量
$$
h(m,n)=\max(m,n,m-n,1-m,1-n,1-m+n).
$$
三面各有 $T^2$ 种地址，故 $|H_T|=3T^2$。负侧的平面截距是 $1-T$，来自正字段偏移。起点 $(T,1)$ 的 $1+$ 步和 $(1-T,1-T)$ 的 $1-$ 步均碰到容量 $T+1$。两步在内存中都有精确目标，且逆步能返回。只有把该中间点也经有限预算往返时才形成障碍。

每个水平方向在 $2T$ 条非空水平格线各有一个出界起点。竖直同理。因此四个具名方向各有 $2T$ 条有向出边。任意不超过 $r$ 步的一切前缀都安全，等价于三带各向内缩 $r$。每个投影两种极向位移 $\pm r$ 都可由重复同一指令达到。这样得到
$$
 \#\{\text{全部长度}\le r\text{的词均安全}\}=3\max(T-r,0)^2.
$$
初态均匀抽自 $H_T$ 时，走到第一个超界点的**最短**步数恰为 $j$ 的起点有 $6(T-j)+3$ 个，$1\le j\le T$。其均值为 $(T+1)(2T+1)/(6T)$。

## 三、指定有序词的起点数和最小容量

令 $(x_j,y_j)$ 为词的前缀位移，包括空前缀。取三个序列 $x_j,y_j,x_j-y_j$，其最小、最大和跨度依次记 $p_i,P_i,d_i=P_i-p_i$。每个前缀都需用于保存和重新读取时，所有允许起点由
$$
 L_i\le (m,n,m-n)_i\le U_i,\qquad L_i=1-T-p_i,\quad U_i=T-P_i
$$
刻画。设 $A=U_1-L_1+1,B=U_2-L_2+1$，若有空带，计数为零。令 $G(s)=\binom{s+2}{2}$（$s\ge 0$），其余取零，并置
$$
 F(s)=G(s)-G(s-A)-G(s-B)+G(s-A-B).
$$
则精确起点数为
$$
 N_T=F(U_3-L_1+U_2)-F(L_3-1-L_1+U_2).
$$
因为 $i=m-L_1, j=U_2-n$ 在 $A\times B$ 整矩形内，$m-n=L_1-U_2+i+j$，对两边界作容斥即得。固定词在足够大的 $T$ 下还有显式二次式。写 $\alpha=-1-P_1+p_2+P_3, \beta=p_1-P_2-p_3$。当第三带非空，且 $0\le T+\alpha,T+\beta\le \min(A,B)$ 时，从矩形减去两个角的三角数即得
$$
 N_T=3T^2-(d_1+d_2+d_3)T+
 d_1d_2-\frac{\alpha(\alpha+1)+\beta(\beta+1)}2 .
$$

**定理 2。** 可容纳至少一个起点的最小正整数上界为
$$
 T_{\min}=\max\left\{
 \max_i\left\lceil\frac{1+d_i}{2}\right\rceil, \left\lceil\frac{2+P_1-p_2-p_3}{3}\right\rceil, \left\lceil\frac{1-p_1+P_2+P_3}{3}\right\rceil
 \right\}.
$$
矩形上 $m-n$ 的取值遍历整区间 $[L_1-U_2,U_1-L_2]$。三带非空外，充要条件只剩该区间与 $[L_3,U_3]$ 相交。解这五个整数不等式即得。故最小十进制字段预算就是令 $10^D-1\ge T_{\min}$ 的最小正整数 $D$。

令 $d=\max d_i$。因 $x=y+(x-y)$，必有 $P_1\le P_2+P_3$ 及 $p_1\ge p_2+p_3$，两个交叉项中的跨度组合至多 $d_2+d_3\le 2d$。所以所有这种词都有 $T_{\min}\le \lceil(2d+2)/3\rceil$。逐单位步走 $(0,0)\to(d,0)\to(0,0)\to(0,-d)$，三跨度皆 $d$，且 $P_1-p_2-p_3=2d$，达到上界。

两个各含两前两后的水平词 $++--$ 和 $+-+-$ 长度相同、净位移均零。取 $T\ge 2$，每条非空水平格线有 $2T-|n|\ge T$ 个点，故全前缀允许的起点数分别是 $3T^2-4T$ 和 $3T^2-2T$。若只存初态和终态，两词都允许全部 $3T^2$ 个点。这给出同一实际转移表里可逐步验证的严格区别。

## 四、规范文本的总字节与复算

原 `to_json` 的规范 ASCII 文本含 132 个固定字节。其余恰是两个正字段的十进制位数之和。定义 $S(j)=0$ 对 $j<2$，对 $j\ge 2$ 取 $S(j)=1+(9j-10)10^{j-1}$。每一面中，位数和恰为 $j\ge 2$ 的正数对有 $81(j-1)10^{j-2}$ 个，累加给 $S$。于是每字段最多 $D$ 位且规范文本至多 $132+B$ 字节时，地址数为
$$
 3\{S(B)-2\cdot10^D S(B-D)+10^{2D}S(B-2D)\}.
$$
减去一栏位数超过 $D$ 的情形时，长度平移 $D$ 使拼法总数恰乘 $10^D$。预算 $B\ge 2D$ 即回到 $3(10^D-1)^2$。非规范输入可以增加空白或采用等价转义，这个字节公式针对规范输出。

复算环境为 CPython 3.12.14 和 jsonschema 4.26.0。独立运行冻结源的 16 个原回归均通过。配套脚本对两个 Python 模块、schema、原测试、两份已有 Lean 源先核 SHA-256，随后调用真实编码、解码、步进及 JSON 接口。它核了 48 个分格的 96 个仿射取值。在 $T=1,2,3,4,5,9$ 各自核了所有长度至五的 1,365 个指令词，另以实际编码检验 $d=0,\ldots,8$ 的尖锐容量见证。字段位数 $D=1,2$ 的 29,646 个合法地址全部用规范输出实际计字节。小 $T$ 由整数预检实施，解释器的实际十进制往返在常规 640、4300 位及文档所述关闭设置上检验。所有统计仅属固定两生成元切片。[复算程序](runtime_check.py) · [核验数值](runtime_checked.json)

在冻结项目根目录或持有相同源文件的检出中，执行 `python runtime_check.py --repo /path/to/enterprise-math`。标准输出可与配套 JSON 逐字比较。

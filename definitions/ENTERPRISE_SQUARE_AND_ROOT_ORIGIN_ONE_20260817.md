# 进取平方与平方根：原点一 / 零不存在重推

Status: `ACTIVE / CANONICAL_FOUNDATIONAL_REBUILD`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Supersedes: `definitions/ENTERPRISE_SQUARE_AND_ROOT_20260816.md`
Depends on: `definitions/ENTERPRISE_COORDINATE_ORIGIN_ONE_NO_ZERO_20260817.md`

## 1. 为什么旧公式必须重推

旧平方定义以坐标原点 `0` 为几何端点，使用

`T_n=((0,0,0),(n,0,0),(0,-n,0))`

从而默认“坐标标签 `n` 与从原点出发的 primitive interval 数同为 `n`”。

用户现已冻结：

`ENTERPRISE_COORDINATE_ORIGIN = 1`

且 `0` 不属于进取坐标系。

因此从原点 `1` 到原生点态 `n`，primitive interval 数不再是 `n`，而是外部计数

`m = n-1`。

这里 `m` 是环境数学中的步数/区间数，不是进取坐标。

所以旧的 `n^2` 胞元面积推导不能直接平移到新坐标本体。

## 2. 原点一几何中的半平方

取两条进取垂直的有向原生轴 `u,v`，共享原点 `O_E=1`。

取同一原生坐标态 `n>=1` 作为两轴端点标签：

`U_n=(u,n)`，`V_n=(v,n)`。

从 `O_E` 到任一端点共有外部 primitive interval 数

`m=n-1`。

由与旧 triangular-cell 计数相同的局部拼接结构、但把边长 interval 数改为 `m`，半平方中的两类 elementary triangle 数分别为：

`N_+(n)=m(m+1)/2 = n(n-1)/2`

`N_-(n)=m(m-1)/2 = (n-1)(n-2)/2`

其总 elementary half-square cell 数为：

`N_T(n)=N_+(n)+N_-(n)=m^2=(n-1)^2`。

注意：当 `n=1` 时没有非退化 primitive interval，因此这里只是原点基态；不把任何坐标 `0` 引入进取坐标系。

## 3. 完整进取平方的原始几何面积

将上述半平方与其关于对应原生轴的镜像拼接，得到完整进取平方。

它包含：

`2m^2 = 2(n-1)^2`

个 elementary triangular cells。

沿用“一对镜像 elementary half-square triangles = 一个完整进取面积单位”的归一化，则完整平方的原始几何面积 magnitude 为：

`ENTERPRISE_SQUARE_RAW_AREA(n)=(n-1)^2`。

该量是外部面积胞元计数/几何 magnitude，不是原生坐标状态。

因此：

- `n=1`：原点基态，非退化面积不存在；外部 cell count 为空；
- `n=2`：一条 primitive interval 的单位边长，raw area = `1`；
- `n=3`：两条 primitive intervals，raw area = `4`；
- `n=4`：三条 primitive intervals，raw area = `9`。

这说明旧 `n^2` 在 origin-one 语义下若继续出现，首先应解释为某种点态/索引计数，而不能再自动解释为由端点 `1 -> n` 张成的二维胞元面积。

## 4. 原生标量状态编码

进取坐标/进取标量状态自身只允许：

`1,2,3,...`

因此把外部非负 magnitude `q` 送回原生标量状态时，采用唯一的保序一阶编码：

`ENC_E(q)=q+1`。

其意义是：

- 外部“无扩张 / 空步数 / 零 magnitude”对应原生基态 `1`；
- 外部 magnitude `1` 对应原生状态 `2`；
- 外部 magnitude `2` 对应原生状态 `3`；
- 依次类推。

这里 `0` 只存在于外部计数语言中，不是进取坐标值。

## 5. 新的进取平方定义

定义 **进取平方** 为“原生边端点状态 -> 原生面积状态”的映射：

`ENTERPRISE_SQUARE(n)=ENC_E(ENTERPRISE_SQUARE_RAW_AREA(n))`。

因此：

`ENTERPRISE_SQUARE(n)=1+(n-1)^2`, `n>=1`。

正式冻结：

`ENTERPRISE_SQUARE_ORIGIN_ONE(n)=1+(n-1)^2`。

首项为：

`1 -> 1`

`2 -> 2`

`3 -> 5`

`4 -> 10`

`5 -> 17`

`6 -> 26`

即平方态序列：

`1,2,5,10,17,26,...`。

这是 origin-one / no-zero 坐标语义下的原生平方态序列。

## 6. 壳层递推

新平方定义可以完全不用坐标 `0` 地递推生成：

`S_E(1)=1`

`S_E(n+1)=S_E(n)+(2n-1)`, `n>=1`。

证明：从坐标态 `n` 扩到 `n+1`，primitive interval 边长从 `m=n-1` 扩到 `m+1=n`，新增 raw area 为：

`(m+1)^2-m^2=2m+1=2n-1`。

所以新平方每次加入连续奇数壳层：

`+1,+3,+5,+7,...`。

该递推给出同一闭式：

`S_E(n)=1+(n-1)^2`。

## 7. 新的进取平方根定义

进取平方根定义为上述原生平方映射在其像上的逆：

若

`y=1+(n-1)^2`

则

`ENTERPRISE_ROOT(y)=n`。

等价地，在外部证明语言中：

`ENTERPRISE_ROOT(y)=1+sqrt(y-1)`，

前提是 `y-1` 为普通整数完全平方。

正式 exact-square domain 为：

`SQ_E={1,2,5,10,17,26,...}`

或

`SQ_E={1+k^2 : k is an external nonnegative integer}`。

首项：

`ROOT_E(1)=1`

`ROOT_E(2)=2`

`ROOT_E(5)=3`

`ROOT_E(10)=4`

`ROOT_E(17)=5`。

对不属于 `SQ_E` 的原生状态，本阶段不强制定义 exact Enterprise root；近似根、上下根、BRC 根读出另行研究。

## 8. 原始面积根与原生状态根必须区分

若输入的是外部 raw area magnitude `A=m^2`，则对应原生边端点状态为：

`ENTERPRISE_ROOT_FROM_RAW_AREA(A)=1+sqrt(A)`。

因此：

- raw area `1` -> endpoint state `2`；
- raw area `4` -> endpoint state `3`；
- raw area `9` -> endpoint state `4`。

而若输入已经是原生 square state `y=ENC_E(A)=A+1`，则使用：

`ENTERPRISE_ROOT(y)=1+sqrt(y-1)`。

二者不得混写。

## 9. 与普通代数的关系重新定型

本定义不宣布普通代数恒等式 `m*m=m^2` 错误。

普通 `m^2` 继续是外部 magnitude / step-count arithmetic。

被 supersede 的是旧命题：

> “原生坐标标签 `n` 的几何进取平方直接等于普通标签乘法 `n*n`。”

在 origin-one 坐标系中，原生坐标标签 `n` 与几何边长 interval magnitude 相差一个基态：

`m=n-1`。

因此原生平方态是：

`ENC_E(m^2)=1+m^2=1+(n-1)^2`。

若以后要建立完整的 origin-one 原生加法/乘法，应从同一编码原则独立推导，不在本文件中越权冻结。

## 10. 对旧进取半平方/平方结果的处置

旧文件：

`definitions/ENTERPRISE_SQUARE_AND_ROOT_20260816.md`

从本定义起状态为 `SUPERSEDED_BY_ORIGIN_ONE_REBUILD`。

其中仍可保留为历史事实的是：

- 给定 primitive interval 边长 `m` 时，三角胞元总数为 `m^2`；
- 完整镜像平方含 `2m^2` elementary triangular cells；
- 普通 magnitude square 为 `m^2`。

被撤销的是把原生坐标标签直接等同于 `m` 的零原点语义。

## 11. 最高冻结

正式冻结：

`ENTERPRISE_COORDINATE_ORIGIN = 1`

`ZERO_IS_NOT_AN_ENTERPRISE_COORDINATE`

`ENTERPRISE_SQUARE_RAW_AREA(n)=(n-1)^2`

`ENTERPRISE_SQUARE(n)=1+(n-1)^2`

`ENTERPRISE_ROOT(1+(n-1)^2)=n`

以及递推：

`S_E(1)=1`

`S_E(n+1)=S_E(n)+2n-1`。

若后续 checker、几何构造或更基础公理给出精确反例，则按用户指令推倒重来；在被 supersede 前，本文件是当前 canonical square/root definition。

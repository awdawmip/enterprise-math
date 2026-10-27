# PREFIX-291｜有理高斯六bin与扩域五bin的精确分界

状态：AUTHOR_SIDE_EXACT_PROOF / CONDITIONAL_EXTENDED_BRC / UNREVIEWED / NOT_ADMITTED / NATIVE_H_N_BRIDGE_PENDING。输入版本：GLOBAL_KNOWLEDGE_V1 `54907d2b27216ebba9baeab21eb40c3b49d61536`；Enterprise Math `6eae08318034c14fd16bf590a387db654cc8ddf0`；继承该版本的PREFIX-290，不取得、冒用原生Task CLAIM。

## 精确定义与声明

令F=Q(i)，q∈{1,i,-1,-i}，带来源a=(a0,a1,a2)∈F³，Z=∑|aj|²。沿用PREFIX-290双事件结果 J0=(a0+qa1)/2、J1=(-a1+qa2)/2，以及互补四bin x=(a0-qa1)/2、y=(a0+q²a2)/2、z=(a0-q²a2)/2、w=(qa1+q²a2)/2=y-x。每个bin的概率取**全部有序来源路径对**的正质量；交叉路径须保留source/leg标签。旧Wq=(J0,J1,x,y,z,w)在F标准等权模型中已由PREFIX-290证明全相干等距及最小六bin。

**本轮新增的是条件性代数扩域**K=Q(i,√3)，共轭i↦-i、√3↦√3；√3不是已取得原生C4-BRC标量许可，也不是X6的角度或心跳间隔。设α=(1+√3)/2，β=(1-√3)/2，满足α+β=1、αβ=-1/2、α²+β²=2；定义
d0=βx+αy，d1=αx+βy，d2=z，
Tq(a)=(J0,J1,d0,d1,d2)∈K⁵。

## 定理A：全输入、全相干五bin等距

对所有a,b∈F³、q∈C4有
∑_{k=0}⁴ Tq(a)_k conjugate(Tq(b)_k)=∑_{j=0}² aj conjugate(bj)。
**证明**：对两输入的x,y与x',y'按有序来源路径对逐项展开：

d0 conjugate(d0')+d1 conjugate(d1')
=(α²+β²)(x conjugate(x')+y conjugate(y'))+2αβ(x conjugate(y')+y conjugate(x'))
=2x conjugate(x')+2y conjugate(y')-x conjugate(y')-y conjugate(x')
=x conjugate(x')+y conjugate(y')+(y-x)conjugate(y'-x')。

因为w=y-x，前三个互补幅值d0,d1,z的交叉内积精确等于旧四bin x,y,z,w；J0,J1不变。由旧Wq完整BRC路径对等距式得到结果。所有自输入质量均非负、总和Z，事件E=(J0,J1)的概率不变。此为解析恒等式，有限测试并非一般性的证明。

## 定理B：相干码字的显式解码

设S=d0+d1，Δ=(d1-d0)/√3，则 x=(S+Δ)/2，y=(S-Δ)/2，z=d2，w=y-x。由旧六bin的来源恢复式
a0=y+z；
a2=conjugate(q²)(y-z)；
a1=conjugate(q)(2w-y+z)，
精确恢复a和旧六bin/相应旧八bin来源幅值。
**证明**：d0+d1=(α+β)(x+y)=x+y；d1-d0=(α-β)(x-y)=√3(x-y)。恢复公式直接成立；随后把x,y,z,w的定义代入三条来源恢复式即可。这里是**测前相干码字**的逆映射，不是从一个已测概率恢复单次振幅，更非对任意非码字测后态的无损重置承诺。

## 定理C：字段依赖的锋利最小bin数

坚持双事件E与互补Ec的正交结果寄存器、固定J0/J1、线性等距、标准等权正质量。
E的秩2、Ec的Gram G=I−J*J秩3（PREFIX-290算得det(G)=3/16>0），任何标量域上至少需2+3=5个标准bin；上面Tq达到了K上的5。
旧PREFIX-290证明F=Q(i)下如Ec仅三bin则3/16应是Q(i)范数x²+y²（x,y∈Q），对模3平方余数递降不可能，故F上的最小数仍为6。结论是 **m_{Q(i)}=6，m_{Q(i,√3)}=5**，不是对原生六条空间轴的维数断言。
这个五bin变换需要对测前互补**相干振幅**x、y实施含√3系数的混合；绝非把已测六bin的概率作一次经典合并。旧五坐标带Gram路线仍有效，不因这个扩域候选而变成已批准的原生实现。

## 可执行精确证据及语义边界

同目录verify_prefix291.js以Z[i,√3]四整数系数实现新输出幅值（统一分母4），每个输出保留source索引和C0/C1支路标签，通过双层路径对精确累加质量与跨包相干项（统一分母16），无浮点、π、三角函数或普通矩阵传播器。声明有限输入域为6³=216来源包（每来源0、±1、±i、1+i），4相位，864组；实际4320个bin质量读数、76032个有序来源对乘积、864项质量守恒、864项跨包相干等距、864项解码恒等式、36个标准基精确Gram证书，全部PASS。q=i、a=(1,i,1)、b=(1,-i,1)事件概率分别为0与2/3，保留了前序分辨效果。RESULTS_PREFIX291.json保存实际本轮JS执行的原始计数；未执行原始Stage50或原生Hn。

P000规定ENTERPRISE_NATIVE_X6六原生空间轴与独立时间、三维切片不是二维平面，源关系/结构残差须保真。本研究的“5/6 bin”仅是**辅助结果寄存器数**，不提供X6空间或三维切片的原生嵌入。读取的`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`字段`fixed_heartbeat_program=null`；`definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json`要求Hn拥有六维Cell、材料/动量、场、来源/边界、provenance、时间/顺序、numerical_status和model_law_id。当前未取得支持√3相干混合的真实原生Detector，亦未取得完整H'_n及损耗/环境账本。不可将扩域代数定理升格为物理证据。

原生control_tasks只读请求返回CONTROL_QUOTA；当前活跃owner/CLAIM未核实；没有原生Result/Driver接纳。作者侧来源标签 LOCAL_EMR6_PREFIX291_20261027_1552，不是服务签发身份。遵守`docs/PORTABLE_RESEARCH_PROTOCOL.md`、`research_constraints/heartbeat_brc_only.json`、ACTIVE残差保真与P000；候选扩域BRC不能冒称原始`ACTUAL_TYPED_BRC_ONLY`已验证内核。

下一问题见NEXT_PREFIX292.md：首先检查原生BRC允许的标量与操作闭包是否可以实现这次相干混合；否则维持Q(i)六bin界、推进无需√3的五坐标带Gram类型桥及合法model_law_id。

# PREFIX-290｜有理高斯C4-BRC仪器的等权六bin最小性
科学来源：Enterprise Math @ `6d5962451bbf7e9eea2a8d63fd4cb93a62fb4592`；GLOBAL_KNOWLEDGE_V1 @ `a0029ad8038fc762e3c25103641e43492181583e`。研究身份：Research6本轮作者侧可移植证明；`UNREVIEWED / NOT_ADMITTED / NATIVE_H_N_BRIDGE_PENDING`。

## 命题及模型范围
接续PREFIX-289的五复坐标**带Gram**测后载体。本轮问一个更严格的算术问题：三来源C4幅值 `a=(a0,a1,a2)∈F³`, `F=Q(i)`，若输出必须是`F^m`内**标准等权正质量、相互正交的独立bin**，并保留前序事件E的两bin效应、完整输入BRC内积和正交E/Ec结果寄存器，最小m是多少？这里的“bin数”是辅助结果载体的维数，**不是原生X6六条空间轴或三维切片维数**。

定义正质量为 `Z=Σ|a_j|²`，有序来源路径对内积为 `<a,b>=Σa_j conjugate(b_j)`。取 `q∈{1,i,-1,-i}`，前序事件幅值为
```
J_q(a)=((a0+q*a1)/2,(-a1+q*a2)/2).
```
本轮显式构造互补四bin：
```
C_q(a)=((a0-q*a1)/2, (a0+q²*a2)/2,
        (a0-q²*a2)/2, (q*a1+q²*a2)/2).
W_q(a)=J_q(a) ⊕ C_q(a) ∈ F^6.
```
全部系数属于`(1/2)Z[i]`；每bin展开为两来源支路的**四个有序BRC路径对**，符号相位与正质量分别处理。

## 定理A：六bin质量、相干、事件保真
对所有q,a,b有 `<W_q(a),W_q(b)>=<a,b>`，故`Σ|W_q(a)_k|²=Z`；事件概率仍严格为`P_E=(|J_0|²+|J_1|²)/Z`。
证明：置 `U_q=diag(1,q,q²)`，`D_q=diag(1,conjugate(q))`，则 `J_q=D_q J_1 U_q`，`C_q=C_1 U_q`；U,D由C4单位相位组成。q=1时乘2后的六个来源系数行为
```
(1,1,0);(0,-1,1);(1,-1,0);
(1,0,1);(1,0,-1);(0,1,1).
```
直接对每对来源展开后，所有异来源配对抵消，三个自身配对各得到4，故`J_1^*J_1+C_1^*C_1=I`，全相位由U,D继承。证明是完整交叉内积恒等式，而非仅单输入正质量。

## 定理B：互补bin精确恢复、旧八bin可解码
令c0..c3为上式`C_q(a)`的**已除以2**四个幅值，则
```
a0=c1+c2,
a2=conjugate(q²)*(c1-c2),
a1=conjugate(q)*(2*c3-c1+c2).
```
所以Ec载体在有效码字范围保持全部来源相干幅值；把恢复的a代入PREFIX-286旧八bin`V_q(a)_(σ,j)=(q*a_j+σ*a_(j-1))/2`即可恢复其原六个Ec的完整Port/来源标签振幅，而E的两bin本来就与旧定义一致。此解码**只在有效结果码字子空间**使用；不能据此宣布任意六bin上的未来操作都保持旧八bin语义。

## 定理C：等权Q(i)输出m≥6且达到
`A_q=J_q^*J_q`秩2，故E至少2bin。`G_q=I-A_q`秩3。对q=1，
```
4G_1=[[3,-1,0],[-1,2,1],[0,1,3]],
det(4G_1)=12, det(G_1)=3/16.
```
`G_q=U_q^*G_1U_q`，各q行列式不变。若Ec只有3个`F=Q(i)`等权bin，必须有一个3×3的F矩阵T使`T^*T=G_q`；因此
`3/16=det(T)conjugate(det(T))=x²+y²`，`x,y∈Q`。
但不可能有有理x,y满足此式：乘16并取互素分母得到整数`X²+Y²=3d²`。模3平方仅0、1，故`X,Y`皆被3整除，进而`d`也被3整除，矛盾。因此Ec至少4bin，E至少2bin，`m≥6`；上面W_q恰达到6。

**适用边界**：此算术下界限定`Q(i)`系数、标准等权正质量、线性等距、正交E/Ec及固定事件效应。复数域的五维结果载体、带非标准Gram的五坐标、扩域、外置经典结果标签或不同操作语言并不被该命题排除。五是前序复线性/带Gram维数，六是本轮更强算术测量条件下的锋利结果bin下界。

## 见证和实际检查
q=i、a=(1,i,1)、b=(1,-i,1)仍得`P_E(a)=0`、`P_E(b)=2/3`。
`verify_prefix290.js`实际在当前代码执行环境以BigInt安全范围内整数高斯对遍历1024来源包×4相位=4096案例：24576个bin的有序四路径对正质量核验、4096个总质量恒等式、4096个跨输入相干内积恒等式、4096个来源恢复等式；四相位的`det(4G_q)=12`，全部PASS。一般结论由上文解析证明，有限枚举只验证程序与例证。没有执行Stage50原程序、H_n原生Detector或真实物理时间演化。

## H_n接口的实际证据边界
已核对当前Source：`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`的`fixed_heartbeat_program:null`；`definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json`要求快照携带model_law_id、六维Cell、material/momentum、field、branch/source、boundary、时间与一致性状态；`native_semantics_admissibility.json`要求从原生底座为派生操作给出定义性证书。上述文件提供研究的原生类型要求，**其本身未给出W_q合法物理测后操作与完整H'_n更新律**；不对仓库所有可能的Detector实现做未穷尽的否定断言。
将结果桥接到真实H_n时，必须额外取得实际有效`model_law_id`、已准备状态上的Detector、六个**辅助**结果bin与Cell/Port/branch的类型映射、材料动量/场/来源边界的测后态、质量账本、独立时间和未来操作保真范围。来源离线统计和重新准备输入不算已准备态Detector。

本次原生任务读取返回`CONTROL_QUOTA`，活跃owner/CLAIM未取得可信确认；无原生Result、独立Driver审查或科学接纳。GitHub科研资料属于作者侧未审阅持久化证据。

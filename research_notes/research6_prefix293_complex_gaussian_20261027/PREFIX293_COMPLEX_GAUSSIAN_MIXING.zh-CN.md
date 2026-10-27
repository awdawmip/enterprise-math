# PREFIX-293｜复有理 Gaussian BRC 混合的分母资源反例与精确泄漏定理

研究等级：AUTHOR_SIDE_EXACT_MODEL_PROOF / UNREVIEWED / NOT_ADMITTED / NATIVE_HN_PENDING。
日期：2026-10-27。
本轮规范快照：GLOBAL_KNOWLEDGE_V1 main@e9025994caa6e7be3e6ac0268c5158b50fe99075。
本轮科学输入：Enterprise Math main@5ea862c0dcb1c1ab62de89a1d3c392b4000d213c。
规范入口：00_BOOTSTRAP、OPERATING_MANUAL、P000、ACTIVE 世界观、Portable Research、HEARTBEAT_BRC_ONLY_ARITHMETIC。沿用 PREFIX-290 至 PREFIX-292 的有来源 C4-BRC 形式证明，不替换其原件。

## 输入与定理A（复相干等距）

在声明的辅助BRC模型中，a=(a0,a1,a2) 属于 Q(i)^3；u 属于 C4={1,i,-1,-i}；每个Port保留完整有序来源 (j,k) 项。定义
J0=(a0+u*a1)/2，J1=(-a1+u*a2)/2，
x=(a0-u*a1)/2，y=(a0+u²*a2)/2，z=(a0-u²*a2)/2，
w=y-x=(u*a1+u²*a2)/2，s=x+y。
沿用已证明的六结果 (J0,J1,x,y,z,w) 对所有输入保持全复内积。

本轮取任意 t,c 属于 Q(i)，定义
d0=(s+t*w)/2，d1=(s-t*w)/2，d2=z，leak=c*w，
T(a)=(J0,J1,d0,d1,d2,leak)。

定理A：此固定对称六结果结构对所有双输入 a,b 保持全相干内积，当且仅当
|t|²+2|c|²=3。

证明：对任意a,b，直接保持有序路径对展开，
d0(a)conj(d0(b))+d1(a)conj(d1(b))
 =[s(a)conj(s(b))+|t|²w(a)conj(w(b))]/2。
旧三结果(x,y,w)的贡献为 [s(a)conj(s(b))+3w(a)conj(w(b))]/2。两者加leak后的Gram差为
[(|t|²-3)/2+|c|²]*w(a)conj(w(b))。
w非零，故上述条件充要。质量与跨输入相干同时守恒，事件E={J0,J1}保持旧读数。

取正整数p,r以及非负整数h，若 p²+h²+2=3r²，则 t=(p+ih)/r、c=1/r 给出Q(i)的全相干六结果等距。舍去第六结果时的精确Gram残差是 -w(a)conj(w(b))/r²，秩一，核维数2；对所有非零a，
0≤L(a)=|w(a)|²/(r² Z)≤1/(2r²)，Z=Σ|aj|²。
上界由 a=(0,1,conj(u)) 达到，故锋利。

## 定理B（固定结构下的分母下界）

任取 t=(p+ih)/r，c=(s+ik)/r 属于Q(i)，p,h,s,k为整数，r≥1。在该结构中完整等距当且仅当
p²+h²+2(s²+k²)=3r²。

当c=0，上式成为 p²+h²=3r²。模3平方余数仅0、1，迫使p,h均被3整除，再迫使r被3整除；无限递降排除非零有理解。因此有限Q(i)对称结构必有非零leak。

若公共整数分母限制为r≤R，因s²+k²≥1，最坏输入泄漏满足
sup_(a≠0)L(a)=|c|²/2=(s²+k²)/(2r²)≥1/(2R²)。
等号要求r=R且s²+k²=1，还要同时满足上述整数方程。此是对固定对称参数化、固定事件E和保留z的条件性预算定理；不是对任意六bin或全部原生Detector的全局最优宣称。按直接来源leg系数，所有输出可采用共同分母D=4r。

## 严格反例：实Pell参数族并非扩大Q(i)族后的分母预算最优

PREFIX-292的实混合取h=0，Pell p²−3r²=−2，r依次为1、3、11、41等。允许复有理高斯相干混合：
(1) (p,h,r)=(3,1,2)，因为9+1+2=12，t=(3+i)/2，c=1/2。最坏L=1/8，直接输出分母D=8。预算r≤2内，实Pell只有r=1，最坏L=1/2；因此此反例减少四倍。
(2) (12,1,7)，因为144+1+2=147，最坏L=1/98；同一预算r≤7内实Pell最大r=3，最坏L=1/18。
(3) (8,3,5)还给出最坏L=1/50。

另有无限非实族。固定h=1，以(p,r)=(3,2)启动，递推
p'=2p+3r，r'=p+2r，
保持p²−3r²=−3，故始终p²+1+2=3r²。所得r=2、7、26、97等，渐趋无穷。所有有限项仍保留精确有来源的第六结果；五bin泄漏界仅趋于0而不等于0。

在u=i时，旧C4相位伙伴a=(1,i,1)、b=(1,-i,1)的未条件化事件E概率仍为0与2/3。

## 精确证据与适用边界

实际运行verify_prefix293.js：BigInt Gaussian整数、共同分母4r；每bin遍历完整9个有序来源对。不调用浮点、经典三角、π、普通矩阵传播。参数：(1,0,1)、(3,1,2)、(5,0,3)、(8,3,5)、(12,1,7)；216个来源包(每项0,1,-1,i,-i,1+i)，4种C4相位，共4320组合。通过25920次直接BRC质量、466740项有序来源对乘积、180项精确Gram比较、各4320项总质量/跨输入/泄漏/事件保持/解码代数检查、20项锋利见证检查。结果保存在RESULTS_PREFIX293.json。整数分母r≤30的穷举仅是有限枚举，不代替无限证明。相干解码检查针对测前复载荷，而非测量后读出全部相位。

原生来源审计：固定版本 definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json 中fixed_heartbeat_program=null。现有该合同没有提供可用于上述仪器的model_law_id，也没有实际完成Cell、三维切片、Port、全场、材料动量、来源、边界、测后态及独立时间的全态操作验证。2026-10-27本轮原生服务可读em_status，但em_control_tasks返回CONTROL_QUOTA；Owner/CLAIM未核实，未建立原生Result或独立Driver接纳。上述证明仅在声明的Q(i) C4来源相干BRC模型内成立。

NEXT：扩大至非对称及可复合的Q(i)门集以检验是否还有更优分母/Port方案；取得Source允许的H_n Detector操作模型、model_law_id和测后环境账本后进行原生实验。
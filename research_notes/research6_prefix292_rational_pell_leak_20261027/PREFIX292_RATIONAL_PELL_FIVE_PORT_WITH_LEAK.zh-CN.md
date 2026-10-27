# PREFIX-292｜有理 Pell 系数下的五可观测 BRC Port 与单支路泄漏

研究等级：**AUTHOR_SIDE_EXACT_PROOF / FINITE_BRC_CHECK_PASS / UNREVIEWED / NOT_ADMITTED / NATIVE_HN_PENDING**。
本轮规范读入 GLOBAL_KNOWLEDGE_V1 主干 524c9845bfb3090b00fc5be1b962bef3b39ddbdd；数学输入固定 Enterprise Math 50b3784c6be63849c8b8d72221c44cdf9ada6f32。P000 启动投影与原件 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 一致。ACTIVE 世界观与 portable research、BRC-only 协议不变。前序精确定理参照 PREFIX-290 和 PREFIX-291。

## 问题与类型

PREFIX-290 在标准等权 Q(i) 上证明完整 C4-BRC 仪器至少六 bin；PREFIX-291 在扩域 Q(i,√3) 中构造条件性五bin等距映射。本轮问：**不引入 √3，能否让五个有理 Gaussian Port 的缺陷得到准确量化，并由一个来源支路保真修复？** 本轮的 Port/bin 是辅助来源寄存器，不是 P000 的六个原生空间轴，不是完整三维切片或一次物理心跳。

输入 a=(a₀,a₁,a₂) ∈ Q(i)³，C4 相位 u∈{1,i,−1,−i}，Z=Σ|aⱼ|²。继承已有带来源 leg 标签的有序路径对 BRC：
J₀=(a₀+u a₁)/2，J₁=(−a₁+u a₂)/2，
x=(a₀−u a₁)/2，y=(a₀+u²a₂)/2，z=(a₀−u²a₂)/2，
w=y−x=(u a₁+u²a₂)/2。
PREFIX-290 在本形式模型内的完整交叉内积恒等式是六bin (J₀,J₁,x,y,z,w) 精确保相干。

## 定理 A：Pell 六bin 的完整 BRC 等距

取任意正整数 p,r 满足 p²−3r²=−2；令 t=p/r、α=(1+t)/2、β=(1−t)/2，全部系数都在 Q(i)。设置
d₀=βx+αy，d₁=αx+βy，d₂=z，ℓ=w/r。
新六输出 T=(J₀,J₁,d₀,d₁,d₂,ℓ)。

**对所有 a,b∈Q(i)³ 有** Σ₆ Tₖ(a)conj(Tₖ(b))=Σⱼaⱼconj(bⱼ)。
且仅保留前五Port时，严格产生**秩一**交叉内积缺陷
Σ₅ Tₖ(a)conj(Tₖ(b))=⟨a,b⟩−w(a)conj(w(b))/r²。

证明：α+β=1，α²+β²=(1+t²)/2，2αβ=(1−t²)/2。沿有序来源 path/leg 对展开，相对于原互补 (x,y,w) 的交叉内积，(d₀,d₁) 增量恰为 ((t²−3)/2) w(a)conj(w(b))；Pell 条件令它等于 −w(a)conj(w(b))/r²。最后一条 ℓ=w/r 的交叉项完全抵消。J、z 及旧 PREFIX-290 等距恒等式保持不变。这里展开的是带标签的全部有序来源对，不以相位抵消冒充正 BRC 质量。

缺陷算子的秩为1，零空间是 w=0，即 u a₁+u² a₂=0，维数2。在此子空间前五bin严格无损；一般状态不能把第六支路省略后仍称无损。

## 定理 B：锋利界、原事件与相干解码

对所有非零输入，泄漏占比 L=|ℓ|²/Z 满足
**0≤L≤1/(2r²)**。
理由为 |u a₁+u² a₂|²≤2(|a₁|²+|a₂|²)≤2Z。取 a=(0,1,conj(u)) 达界。因此 p/r=1/1、5/3、19/11、71/41、265/153 的最坏 L 分别严格为 1/2、1/18、1/242、1/3362、1/46818。这里 L 是形式探测结果账本，并非已测物理耗散。

事件 E=(J₀,J₁) 的**未条件化**概率保持原值。丢弃泄漏分支再归一化会将概率改成 P_E/(1−L)，其相对原值的绝对差最多 L≤1/(2r²)（因为 P_E≤1−L）。对于 u=i 的既有相位伙伴 (1,i,1)、(1,−i,1)，原事件仍为 0 与 2/3。

形式相干码字的显式左逆：s=d₀+d₁，δ=(d₁−d₀)/t，x=(s+δ)/2，y=(s−δ)/2，z=d₂；a₀=y+z，a₂=conj(u²)(y−z)，a₁=conj(u)(2(y−x)−y+z)。该解码需要测前完整复振幅，不声称一次正概率测量能恢复相位，更不主张任意测后态可压回三来源类型。

## 定理 C：纯有理 Pell 路径与闭包界限

p₀=r₀=1；pₙ₊₁=2pₙ+3rₙ，rₙ₊₁=pₙ+2rₙ。每项保持 p²−3r²=−2，rₙ趋于无穷，五Port缺陷界收敛至0。起点 t=1 的六bin只是旧 (J₀,J₁,x,y,z,w) 的重排；有限任何一级仍保留有来源 leg 的泄漏支路。

对于**声明的**加、乘、非零除、C4相位、线性有理来源合成及有限次Port分支操作字母表，Q(i) 系数封闭；√3不在Q(i)，因为互素整数 p²=3r² 不可能。此结论只是条件性运算闭包证明，不是对原生全部BRC操作集合的穷尽式权限审计；若Source确有额外代数扩域或归一化原生门，应按具体 model_law_id 重检。

## 实际执行及证据

随附自包含 Node BigInt 高斯整数验证程序 verify_prefix292.js。直接按分母 D=4r 明列每个来源及 leg 的系数，逐个bin用全部有序来源对求质量和跨输入内积。源域为 a_j∈{0,1,−1,i,−i,1+i} 的216包，4种C4相位，5对Pell整数，共4320组合；直接bin质量 25920次，含跨输入核验的有序来源对乘积 293760项，标准基Gram 180项，以及各4320项完整质量、跨输入相干、恢复、秩一缺陷与E事件检验，全部PASS。解析推导给出一般定理，有限测试只复核实现。results见 RESULTS_PREFIX292.json。

复用前序来源路径和算术：REUSE_APPLIED；Pell参数化属现有 C4 BRC 形式仪器的 EXTEND_EXISTING_TOOL。Native backend 本轮 em_status 返回 BACKEND_IDENTITY_CHECK_UNAVAILABLE / operation_sent=false；owner/CLAIM未核实，Research Activity register pending，未进行原生H_n探测、Result发布或独立Driver接纳。当前 Source 的 HEARTBEAT_WORLD_NATIVE_X6_TIME.json 中 fixed_heartbeat_program=null。所需下一桥为Cell、三维切片、Port、来源、场、材料动量、边界、环境结果、独立时间和实际合法 model_law_id 的整体对应。

后续问题见 NEXT_PREFIX293.md：确认原生 Q(i) 相干组合的操作许可；独立研究固定电路门集/分母资源下的全局最小泄漏。**本轮的 1/(2r²) 是给定 Pell 构造族内的锋利界，不是所有有理电路的全局下界。**

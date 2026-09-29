# 触发记录商与返回干涉：任务发布所用的固定前沿

Progress-Event-ID: hbw-return-task-publication-9f026e-20260929
Status: SOURCE_CANDIDATE_PRESERVED / NOT_ADMITTED
原研究事件：hbw-record-quotient-9f026e-20260928。
原作者：EM-DIRECT-9F026E；原活动：RA-DEF97E433B003C96F9B921F8。
本文件是2026-09-29的来源归档与任务入口，不修改原始报告，不宣称本轮重跑科学实验或完成独立审查。

## 完整原始材料

https://drive.google.com/file/d/1KIe8jzjNyf73yVqBDvtpL1nWBuEP43E3/view?usp=drivesdk
ZIP SHA256: 261177ad99b11cb5bdd23dd37669db8426efc2148db170e9af715c1441af0506
ZIP bytes: 36200091。
完整包包含原报告、THEOREMS.md、冻结计划、源码及依赖、原始账本、验证器和保存记录自检。
主要文件的精确字节绑定见同目录SOURCE_MANIFEST.json。原包内LOCAL_ONLY/待发布措辞是历史状态，保留不改写。
原ZIP已通过连接器上传，文件ID、父目录、MIME及字节数已回读；没有声称二次下载全字节比对。

## 固定模型与类型

使用原signed-CWM候选桥接。六轴Cell坐标及独立时间保留，仅前三轴正向移动。
整数接点D=2J-3I，每拍幅值共同分母3；平方读出是声明假设，不是从P000导出的原生本构。
初态为原点/端口0/工作1。第t拍仅输出端口1乘以a^(2^t) mod N，端口0/2不乘。
记V=SD，P1选端口1，P0同时选端口0/2，B_e=P_e V。
记录beta的可见幅值v_beta=B_beta(T-1)...B_beta(0)|origin,0>，指数q(beta)=sum_t 2^t beta_t，Q=9^T。
原联合态Psi=sum_beta v_beta tensor |a^q(beta) mod N>。

## 候选结论及未解决点

记录分开基线P0(b)=sum_beta |v_beta(b)|^2/Q可由条件纯态轨迹精确采样。
每拍两组整数质量n0+n1=9m，按质量选一组，并保留该组内部0/2相干；路径概率望远镜消去证明全分布。
单轨迹选择后活跃幅值至多2(t+1)，抽象标量操作O(T^2)，完整审计存储及大整数/随机数成本另计。
已保存的64拍四条轨迹峰值为82/62/62/84；它们实际采样的是P0，不自动是任意模数的原模型。
若q->a^q modN在0<=q<2^T单射，则P0等于原模型最终可见分布。易素数幂族N=3^(T+1),a=2满足此条件；这不是困难分解成果。
固定末端同基读出可用更弱的等位重前缀无碰撞条件；其小实例检查目前枚举8或32个指数，不是通用廉价证书。

令G_(b,w)={beta:a^q(beta)=w}。确切返回修正为：
Delta(b)=sum_w sum_(beta!=gamma in G_(b,w)) v_beta(b)v_gamma(b)。
P_N(b)=P0(b)+Delta(b)/Q；sum_b Delta(b)=0，Delta局部可正可负，不能作为正概率混合分量。
现有TV上界为[sum_(b,w)((sum_beta |v_beta(b)|)^2-sum_beta v_beta(b)^2)]/(2Q)。
该界当前用已付成本的六拍穷举树构造，尚未有非枚举、廉价的一般算法。

## 必保回归

a=2,T4时N21/35/77最终分布一致。
T6,Q=531441：N21真实TV=80576/Q、绝对界122112/Q；N35真实TV=33280/Q、界39296/Q；N77两者为0。
模21下指数2与8返回工作4；模35下4与16返回工作16。工作碰撞还需可见匹配，存在碰撞本身不推出非零误差。
同触发记录000中，T3位置(2,0,1)、端口0的-4/-4两路径须相干给64，不得独立平方为32。
前序80对16、可达当前Gram压缩误差下界32/243继续作为安全合并回归，不将旧执行算作新实验。

## 正式任务链与来源诚实性

原直接聊天研究没有伪造为已获接受的正式父任务。先发布一个REPLAY类型的独立接口核验任务，
只核验尚未独立确认的候选证明与有限关键回归，不要求重跑64拍整批科学记录。
其后两个CONTINUATION任务依次处理非枚举Delta证书和修正采样；依赖须取得适用结果后才能进入后续执行。
共同绑定现有OPEN母目标OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS，代次OG-7AE66316D7566C519AE0。
这是其观察相对最小记忆/残差载体/安全合并范围内的候选接口核验与扩展，不更改既有目标内容或其他分支。
本次不授予CLAIM、Working Truth、数学准入或Shor输出等价。

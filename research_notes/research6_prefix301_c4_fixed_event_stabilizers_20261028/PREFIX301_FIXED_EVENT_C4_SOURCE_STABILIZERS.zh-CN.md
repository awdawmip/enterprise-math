# PREFIX-301｜固定 E/Ec 标签的 C4-BRC 来源稳定群及相干参考残差

日期：2026-10-28。状态：AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED / NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION。作者侧本地身份 EM-R006-P301-20261028-LOCAL（非 Source 签发 ID）。本研究继承 PREFIX-300 的 T 相位共轭等变及固定事件标签反例，未重做 PREFIX-298/299 的 Port 轨道穷举。

**固定输入：** GLOBAL_KNOWLEDGE_V1 main@ecd9a62fddac9d34492c57cf902c9c119f4e58c1；Enterprise Math main@34b47b6cc01bfebcfaa61aaaefd1e41f5ee3d92a；P000 原件 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc，与同一全球快照的 P000_STARTUP.json 投影一致。规范入口、ACTIVE 世界观、TASK_RESEARCH 路由、当前 portable research 协议与 BRC-only 规则已读取。当前原生任务查询 em_control_tasks 返回 CONTROL_QUOTA，不能确认活跃 owner/CLAIM。GitHub 作者侧写入不等于正式 Source Result 或独立数学接纳。

## 1. 问题与精确定理

在辅助 Q(i) 来源空间令 q,q'∈C4={1,i,-1,-i}，a=(a0,a1,a2)。两条带固定语义标签的事件振幅为

  e_q(a)=(a0+q*a1)/2，
  c_q(a)=(-a1+q*a2)/2。

来源单项门 A 的语义为 (Aa)_j=d_j*a_{sigma(j)}，其中 sigma∈S3、d_j∈C4，允许比较 q 与目标相位 q'。研究两条**单独事件**正质量保持的充要条件：
  |e_q(Aa)|²=|e_q'(a)|²，|c_q(Aa)|²=|c_q'(a)|²，对所有 a∈Q(i)^3。
绝不将 E/Ec 互换或仅要求二者之和相同。

**定理 A（完整分类）：** 对任意 q,q'，条件成立当且仅当
  A = u*diag(1,r,r²)，u∈C4，r=q'/q=q'*conj(q)。
恰有四种，且 sigma 必须是恒等置换。逐来源振幅等式是
  e_q(Aa)=u*e_q'(a)，c_q(Aa)=u*r*c_q'(a)。
固定相位 q'=q 的稳定群是 {I,iI,-I,-iI}≅C4。允许 q'=conj(q) 时四个代表为 u*diag(1,q²,1)，q=±i 的代表仅翻转中间来源符号而不交换 E/Ec。变换在相位参数上满足 A(u;q→q')A(v;q'→q'')=A(uv;q→q'')；这是一种辅助来源群胚，不是已认证的原生 Detector 门。

**完整证明：** 去掉共同 1/2，写 f_q=(1,q,0)，g_q=(0,-1,q)。对所有复有理输入正质量相等，经 Hermitian 极化分别推出 (f_q A)* (f_q A)=f_q'*f_q' 以及 (g_q A)* (g_q A)=g_q'*g_q'。非零秩一行向量的 Gram 相同，则两者相差单位模数，尤其来源支集相同。因 f 的支集为 {0,1}、g 为 {1,2}，单项置换强制 {sigma(0),sigma(1)}={0,1} 和 {sigma(1),sigma(2)}={1,2}。两集合交集只有 {1}，所以 sigma(1)=1，进一步 sigma(0)=0、sigma(2)=2。故 A=diag(d0,d1,d2)。比较 f 行两系数得到 d0=u、q*d1=u*q'，因此 d1=u*r；比较 g 行得到 d2=d1*r=u*r²。逆向代入立得全部两个振幅等式，所以充分必要且无遗漏。证毕。

## 2. 九来源输入是完整判别证书

定义 W={e0,e1,e2,e0+e1,e0+e2,e1+e2,e0+i*e1,e0+i*e2,e1+i*e2}，ej 是三来源标准基。

**定理 B：** 对任一候选 A，如果两条事件读数在 W 的全部九输入各自相等，则上述等式对全部 Q(i)^3 输入相等。证明：每条事件的 Hermitian Gram 差记 H。ej 得 Hjj=0；ej+ek 得 2Re Hjk=0；ej+i*ek 得 -2Im Hjk=0。三种 j<k 和三个对角已穷尽 Hermitian 3×3 矩阵的九个实参数。因此 H=0。两事件各自应用。证毕。九探针都包含在 V³，V={0,1,-1,i,-i,1+i}，所以本次有限穷尽并非样本拟合的外推。

## 3. 未来门的精确残差边界

对固定 q，所有全局相位 uI 使辅助**齐次 Q(i)-线性**输出链 F、K 满足 K(F(u*a))=u*K(F(a))。因此若声明未来观测只取得这些链的正质量，各输出都无法区分该 C4 整体相位。

**定理 C（未同步参考的反例）：** 如果未来门允许一条来源标签 R 的固定相干参考振幅 1 与 E 事件同 bin 相加，固定 q=1,a=(1,0,0) 时 e=1/2，观测 J=|e+1|²。由完整四路径标签的 16 项有序来源对直接得到
  J(I)=9/4；J(iI)=5/4；J(-I)=1/4；J(-iI)=5/4。
所以三个 u≠1 均与恒等相位可区分，该特定未来参考门集下稳定子缩成 {I}。**这只证明指定参考观察器下的不可安全商去，不证明该参考门在真实原生 H_n 可达。** 没有该门时，固定相位整体因子的质量等价仍按其明确范围成立。联合路径与来源若未来仍有作用，不得因当前正质量相等而直接消去。

## 4. 精确 BRC 校验证据与声明范围

完整检查程序为 verify_prefix301.js；全量结果经过 gzip(mtime=0) + base64 无损保存为 RESULTS_PREFIX301.json.gz.base64，解码后 SHA-256 为 a5febe6e53fa55854a5732cf2d57baf15beb6001290d9288f4926d3fe09cf2c7。可读摘要是 SUMMARY_PREFIX301.json。

程序对全部 6×4³=384 个来源单项门、16 个 (q,q') 相位对用九探针检验；每个不合法候选立即保留一个九探针范围内的 BRC 读数反例。6080 个不合法候选均有反例，每相位对恰四个接受，16×4=64 个接受门精确匹配 A 的公式。筛选实际做 11,360 个候选-探针组合、22,720 次事件 bin 读数与 204,480 个九项有序来源乘积。对全部 64 个接受门，再穷尽 V³ 的 216 个输入，得 13,824 组、55,296 次两侧直接 bin 读数、497,664 个有序来源对贡献，全部通过；384 个逐来源系数等式通过。独立固定参考分支反例采用四项路径和全部 16 项有序来源对。一般定理由解析证明建立；穷尽只覆盖声明的 C4 单项门与有限验证输入。

代码的整数高斯二元组保留来源路径及相位干涉，不借助浮点、π、三角函数、普通矩阵指数、Taylor/Padé/Cayley，也不以正质量替代相干振幅。结果严格为辅助三来源、二事件 BRC 数学。没有经 Source 验证的合法 model_law_id、完整 H_n 的 Cell/场/路径/环境/边界/测后状态、未来原生门闭包、X6 三维切片实际嵌入或独立时间账本。P000 固定六原生空间轴 + 独立时间及无原生二维平面并未改变。

**后继**：NEXT_PREFIX302.md 将九探针扩展到逐 Port / 联合参考 / 未来合成观测，以观察器与门集严格定型的最小充分来源商为目标。成果 UNREVIEWED / NOT_ADMITTED；Research Activity 正式注册 REGISTER_PENDING。
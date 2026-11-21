# 带符号 Green 上界研究包

研究说明见 [SIGNED_GREEN_TRANSPORT_AND_ELIMINATION.md](SIGNED_GREEN_TRANSPORT_AND_ELIMINATION.md)。本包属于原 `EM-DIRECT-B5750A / TASK_RESEARCH` 与原 Activity `RA-60C6D083A81B19084A74C5BA`，没有新登记、领取或远端写入。

## 已完成的增量

1. **正负运输包络**：任意可行部分运输给出 \(Gm\le V_t\le Gm_+\)。邻位差核按距离付费，保留已配负源的抵消。
2. **二矩多层消元**：把节点质量按重心转给相邻保留节点；局部源包的总质量与第一矩为零，Green 像为紧支撑三角势。负包在传递之后免费去除，得到 \(Gm\le U\le Gm_+\)。
3. **临界充分条件**：完整带符号前缀的间距加权均方，或所有合并尺度的三角矩平方和，连同真实端点、dyadic 骨架质量及局部余项，可条件性达到 \(\theta=1/2\)。这些统一算术条件尚未证明。
4. **同一严格窗口的证书**：[1024,32768] 上原 q 与 \(Q=q+P_{256}\)，全部结果使用原严格有理节点道路。六种道路/分区组合中，多层消元总平方预算约 0.0056–0.0067，相比逐点正化预算改善约 116–30,828 倍。

定理直接控制内部能量 \(S^\circ\)。闭窗口还须加入真实两端的直接贡献

\[
e_\partial=(q_A)_+^2/A^{2\theta+1}+(q_B)_+^2/B^{2\theta+1}.
\]

任何闭窗口次幂结论必须保留 \(e_\partial=A^{o(1)}\) 的条件，或改用包含两端的范数。

## 文件与复算

|文件|用途|
|---|---|
|`SIGNED_GREEN_TRANSPORT_AND_ELIMINATION.md`|完整定义、证明、条件性临界命题、有限结果和剩余算术问题|
|`certify_signed_transport.py`|可行运输与完整前缀诊断的严格区间程序|
|`signed_transport_certificate.json`|每个运输计划、每个带符号前缀、严格区间与输入哈希|
|`certify_multiscale_elimination.py`|固定二叉消元与非正节点优先候选的严格区间程序|
|`multiscale_elimination_certificate.json`|全部层、全部消元包、真实端点预算与严格区间|

程序依赖同层目录中的 `rh_joint_certificate/joint_energy_certificate.json`、`rh_joint_certificate/certify_joint_energy.py`，以及后者引用的原严格有理区间工具。仅从已有粗源证书读取数据，不重新构造道路；两个输出 JSON 均包含输入证书的 SHA-256。

```bash
python rh_joint_signed/certify_signed_transport.py
python rh_joint_signed/certify_multiscale_elimination.py
```

本次分别约 9 秒与 19–21 秒。证书采用紧凑 JSON，完整保留字段。逐点支配由正文的代数定理证明；程序中的区间相容性核对不冒称分离式不等式证明。

## 范围与下一步

这不是黎曼猜想证明，也未证明本项目要求的无界窗口统一算术条件。一般方法不主张数学新颖性。完整整数/合数人口、背景、单位项、原前缀及真实端点均保留；辅助 Green 与层次基只用于观察与预算。

同作者分支已核对核心证明与量词，不等同于独立 Project Review。接下来最有价值的是控制大尺度合并三角矩的联合平方和，并保留平滑主项与大除数尾项之间的带符号相关；有限证书中已标出支配层和具体帽函数。

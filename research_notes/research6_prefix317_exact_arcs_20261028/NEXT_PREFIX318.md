# PREFIX-318：冻结报告两形状五条相位弧的连续最小球风险

前沿：PREFIX-317 author-side verified, not Source Result and not independently admitted. Preserve all original proofs/certificates and no redoing PREFIX-316. Scientific input pin: awdawmip/enterprise-math/main@dedcf9f123adbc065324ee57fb8676acafcf4f8a; GLOBAL_KNOWLEDGE_V1 pin: main@c4b076402410ac7a87c9f9875625ac4836b6bf13.

模型：辅助静态S7-3，q=1，U=A/8，b0=(-2,-2i,1)，b2=(2i,2,-i)，共同尺度r=25/54。五项完全准确Q0、十项相干参考Q1/Qi每项容差≤1，报告固定为PREFIX-316同一确切有理报告；逐项保留source:1/2/3与独立reference标签、有序BRC全部路径对。无原生 X6/Detector/model_law_id/时间及测后对应证明，禁止物理外推。

不可重做：PREFIX-317已精确穷尽每形状20条带边界、28个真实圆交点；b0四个可行端点、两条闭弧，b2六个可行端点、三条闭弧。完整代数端点、有理开弧证书保存于RESULTS_PREFIX317.json.gz.b64（gzip+base64，解码原JSON SHA256=aabcd1c45895e3f77d68d59e997e6f79c59a8d3ebb3a57c5191ec9d8d89735b4），代码可原样重新生成RESULTS_PREFIX317.json。八态同一观测的严格MEB²=184807873005625/118075452616116；严格高于PREFIX-316的333788125/213477444，但仍低于全模型已知双态下界1062562/458329。

新一般定理：对等范数状态集S，MEB²(S)=c²-dist(0,conv(S))²。两个形状所在辅助实张成恰为4维；故完整连续圆弧族的接触证明最多需5个态，若凸包最近点h≠0最多只需4个。这是选题的数学缩减。

**下一最小可执行问题**：令S_arcs为五条完整闭相位弧通过r z b0、r z b2映射得到的紧致连续状态集，求出 dist(0,conv S_arcs)² 的精确值或上下匹配证书；给出支撑超平面、四维凸包投影、各弧端点和带内一阶驻点的严格代数验证。先证实或否定h≠0，再使用≤4接触的缩减；若h=0按≤5处理。区分代数实相位最优与仅高斯有理相位可逼近的极值。禁止用有限采样宣称连续极值。

交付：完整数学证明或精确范围、可复核源码和机器证据、未决问题及来源；走GitHub持久化和回读，再按当前独立Source合同决定是否接纳。没有有效session/claim不得提交正式Result或独立审查。

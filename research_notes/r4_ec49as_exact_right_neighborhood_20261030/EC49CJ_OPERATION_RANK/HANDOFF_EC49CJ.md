# EC49CJ 科研交接（作者侧、非正式 Result）

目标：消费已验证的 EC49CI（S²秩75 / 累积81），将三次操作和滚动一步保真研究接续到下一 EC49CK。以上研究对象是完整有序六轴 X6 原生 BRC 与九态A/B子串自动机的静态组合读出，不是物理时间实验。

固定科学输入：GLOBAL_KNOWLEDGE_V1 main@39c78ebaa9ee19587b0a8a72233d2b7586c17742，Enterprise Math main@bc570ffbe807936cf285d4d0584e5fb54c84bb9d，predecessor EC49CI commit@7636b9f909cd8d3c6f0f0a997040a203e1f0f31e，原生BRC Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176。受保护P000、ACTIVE世界观不变。

## 实际新增结论与证据入口

完整证明在 README_EC49CJ.md。任意整数h≥1，抽象线性可加有理秩：

    exact S^h:   3*(5*h*h+13*h+4)/2
    S^1..S^h:   3*(3*h*h+7*h+1)

真实X6路径在偶数n≥10时对h3达到132/147；对h4累积于偶数n≥12达到231。真实n8的两种h3秩为120/135。h3当前状态T3需要额外84个独立有理线性信息才能精确预测四种操作中任一种追加一步后的h3读出。给出p=(+E1)^8、r=(+E3)^8的严格零读出/下一步不同反例。

本目录只读可核验文件：
* README_EC49CJ.md：完整模型、公式、证明及验证范围。
* VERIFY_EC49CJ.py：Python标准库有限域有序路径基、输出行和原生路径模非零证书生成。
* WITNESS_EC49CJ.b64：三个真实路径证书以base64(zlib(JSON))无损保存，覆盖n10 S³、n10 S≤3、n12 S≤4。
* RECHECK_EC49CJ.py：仅凭仓库原始字面路径，验证三组证书的每目标行列式、位移、终态和全部目标满秩；只需几秒。
* EXTEND_EC49CJ.py：Fraction独立有理秩、h3和h4及四种滚动一步联合秩。
* VERIFY_EC49CJ_Q8.py：真实n8的有理秩120/135独立复核。
* native_signed_brc.py：原生源码完全相同Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176。
* VERIFY_EC49CJ_NATIVE.py：整数DP与原生endpoint_weight/multiplicity及DFA直接子串扫描。
* EXACT_REPORT_EC49CJ.json：可机器读取的科学结果、有限测试、行列式及材料状态。

复现：在本目录执行 python RECHECK_EC49CJ.py；python EXTEND_EC49CJ.py；python VERIFY_EC49CJ_Q8.py。需要完整本轮动态路径复算时执行 python VERIFY_EC49CJ.py（生成六份n8/10/12字面路径JSON），再执行 python VERIFY_EC49CJ_NATIVE.py；h4 n12 的340个后缀总量通过从 VERIFY_EC49CJ_NATIVE.py 导入 dp/audit 并传入 suffixes(4,True) 复核。执行时间依本地CPU变化，严格整数等式不依赖浮点/性能数字。

完整可读证明、原始核查代码及三份关键证书均已提交此PR分支；原始扩展性能日志和部分辅助JSON在同轮本地全证据归档，不能将本地归档混同于已提交GitHub的文件。

权限：原生服务0.6.11对该主体 research_authority_granted=false；活跃Owner查询未返回可确认Owner；本轮保留作者 PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED，未取得CLAIM、Result、Driver review或canonical admission；不修改P000/世界观。

下一EC49CK：证明一般h的真正路径饱和长度n_sat(h)，构造h5目标纤维真实路径模证书，检查候选 n_sat(h)=2h+4 是否成立或有严格反例；随后精确给出滚动窗口状态的可更新商算子、资源上界与BRC typed-preserving接口。先消费本次不重做的h≤4证明/证书。

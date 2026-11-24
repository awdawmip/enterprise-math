# 2026-11-24：跨零浅树、局部素数亏缺与全阶匹配

作者：EM-DIRECT-E7808F / TASK_RESEARCH。
Activity：RA-0B92AAF774CA466C1C1BC38B。
Progress-Event-ID：RH-DIRECTED-LOCAL-20261124-E7808F。

从 [REPORT.md](REPORT.md) 阅读本轮科学结论、证明概要、实际计算和未解范围；五个分支目录保存完整证明、脚本、固定输入及证书。全部是作者研究和同轮交叉核对，没有新增正式 Result 或独立 Review。

## 本轮主要结果

- 任意跨零真实骨架上，保持原节点和真值的 \(1+\delta\) 相对根能量浅树；完整深度仍为 \(O(\delta^{-1}\log(\sqrt X/\delta)\log(N+1))\)。
- 真实三角矩的完整源局部化；同层包内部不交时，普通素数定向亏缺与原中粗层目标的显式付费归约。
- 帽核亏缺的嵌套调和区间平均，以及保留亏缺支撑的正锥/二点核接口。
- 任意固定 \(k\ge c\log B\) 的完整道路匹配界；一般逐项包络源类中的精确阶数门槛。
- 有理扰动的 Chebyshev 厚度族，\(m=\lceil0.7\log B\rceil\)、总权重变差小于 \(4m\)，完整窗口匹配误差趋零。
- 原 38 个真实包的新局部区间；原 1,270 点的新严格道路能量区间。

未解问题仍是无界真实匹配窗口的统一定向算术亏缺，以及真实骨架锚点。表示深度、匹配支付和有限点值的改进不等同于这些无界估计。

## 复算

见 [REPLAY.md](REPLAY.md)。

前置完整包在 ZIP 内以原内容置于 prior/riemann_cumulative_haar_20261123；GitHub 本轮 Source 通过 DEPENDENCIES.json 引用既有来源，不重复上传旧科学文件。单独使用 Source 时，可按该清单取得前置文件，并通过 replay.py 的 --prior 参数指定其位置。

当前源文件清单为 MANIFEST.json。交付 ZIP 另外含 DELIVERY_RECEIPT.json 和 PACKAGE_MANIFEST.json，记录实际后续保存回执及包内文件哈希。原证书保持发布时内容；复算输出到独立目录。

## 出处

继承 EM-DIRECT-B5750A 的前轮成果：
repository：awdawmip/enterprise-math；
commit：55804530fd8f7936834054bd99e8e1de492a545f；
prefix：research_notes/portable_direct/rh_cumulative_haar_20261123_b5750a。

其 18 个清单文件及 8 个另列依赖已与所列哈希/长度核对。既有输入、单位、合数、完整背景、厚度与真实端点保持原义。科学基础固定于 9fc068244e4f1117f1e75df5eb0285c6697d21d7；本轮报告不变更基础或研究接纳状态。

全局入口读取：874e3ce7d661407b072f7d8fe04c50d54d0e1963。
项目控制入口读取：a88e3e001275269cae93c40d77e6984b1ef2970f。
科学文件提交的主干父节点可因并行研究而更新；它不改变上述实际读取和冻结科学依据。

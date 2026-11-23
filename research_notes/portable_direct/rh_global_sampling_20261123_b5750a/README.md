# 全窗口采样与端点认证复算包

研究日期：2026-11-23。主报告为 `REPORT.md`。这是 `EM-DIRECT-B5750A` 同一科研接续的作者证明与有限证书包，不是独立审查或正式数学晋升。

## 文件

- `arithmetic/`：全窗口采样网格定理、精确整数步长检查及证书。
- `skeleton/`：精确整数预算、贪心分配、一般源信息下界及穷举证书。
- `shallow_tree/`：一般加法近似、平方样本族、点态相对障碍、真实 44 节点树及能量证书。
- `harmonic_evaluation/`：有限谐和区间、二分支持和端点矩能量计算；附定向作者交叉核对。
- `inputs/`：四份只读历史输入及其出处。下载包内包含原字节；项目 Source 只提交 `PROVENANCE.json` 与说明，历史输入仍以其原提交为权威来源。
- `MANIFEST.json`：下载包内容的准确大小和 SHA256（不包含 manifest 自身）。

## 运行

仅使用 Python 3 标准库，无第三方安装、联网或 API 密钥。从包根目录执行：

```bash
python3 arithmetic/verify_mesh.py
python3 skeleton/verify_global_allocation.py
python3 shallow_tree/certify_shallow_trees.py --source-root inputs
python3 harmonic_evaluation/certify_fast_harmonic_energy.py --input inputs/rh_partial_frontier_20261122/sparse_sample_observations.json --old-certificate inputs/rh_partial_frontier_20261122/sparse_curvature_envelope_certificate.json --scan-check
```

最后一条可去掉 `--scan-check`，运行端点路径而不生成逐点扫描基线。脚本严格拒绝未能被区间分离的符号判断；本包报告的有限实例均已完成并通过。复算会覆盖对应 JSON 证书，保留原证书副本后再运行有利于比对。计时随环境变化。

## 数学边界

全窗口定理控制真实正能量的观察损失，未证明真实道路本身的无界正能量目标。总样本下界属于更广的一般双侧源类；浅树反例属于点态乘法保证。十亿内点算例是已知势合成单元。六个谐和矩及原 1,270 点值来自已保存的前置成果，本轮新增的是全局分配、近似树及实际端点认证算法。

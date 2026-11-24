# 完整支付、真实累计残差与正能量指数：复算包

主报告：[REPORT.md](REPORT.md)。本轮继续沿用 `EM-DIRECT-E7559A / TASK_RESEARCH`、Activity `RA-D2F111EA1C0D4B1DBEFBC1B4`。

## 内容

- `parametric/`：准确穿越残差的同分裂点子帽最大值、完整漂移支付、范围反例及精确验证。
- `compensation/`：真实κ累计背景、ψ/θ/原生E的比较、原匹配半径稳定性和原38包证书。
- `matching/`：单厚度首阶偏差、尖锐加权渐近、算术校正及四个完整有限输入的区间证书。
- `anchors/`：完整正能量与RH/最右零点增长指数的关系，正Green链ℓ²接续及宏观素数平方常数。

本包为作者证明和作者核验。无界结论由解析证明承担；所有探索数据有单独状态。共同作者交叉核对不构成独立Review。

## 统一复算

使用Python3.12及标准库。完整下载包已包含科学前驱；在解压目录执行：

```bash
python replay.py
```

Source目录只保存新增文件时，可指定前驱包：

```bash
python replay.py --previous /path/to/riemann_matching_isotonic_anchors_20261124
```

统一入口核对新文件清单与关键输入散列，运行五个严格验证器，将临时生成证书与已保存证书作结构比较，不覆盖已保存内容。最后复算一次旧探索数据的支付比较；这一步仅验证复用过程，不把浮点数据升级为严格证书。

可另行重做扩大探索：

```bash
python compensation/explore_native_compensation.py --max-power 20 --output /tmp/native_compensation_exploration.json
```

该数据使用双精度。原38包和单厚度四个输入的严格端点使用80位向外整数区间。

## 固定输入和对象范围

38包来自原5个块、17层，实际道路仍使用原11厚度。其新界通过真实参考累计场和原局部匹配半径取得，无需重新查询D或q。

单厚度首阶核验采用B=256,1024,4096,16384，a=1/B，A=floor√B，是新的随窗族。原1270点的能量证书继续沿用前驱。

完整正能量的等价与增长指数使用原道路的背景和线性归一化。稀疏锚点帽、有限数值及单调回归过程各有自身范围，详见完整证明。

# 残差联络复验包

运行 `python check_holonomy.py` 生成 `results.json` 和 `summary.json`。Python 3.10及以上，使用标准库；科学系数运算实际调用所附固定正权BRC源码。

`NOTE.md` 给出证明与范围；`SOURCES.json` 固定原规则及审查来源。所附 `sources/brc_weighted.py` 已按原Git blob核验。原V18整套检查器没有运行，也没有把载体通道等同于原生空间坐标。

Source保存完整执行输出的gzip/base64版本 `results.json.gz.b64`；解码并解压后应与CHECKPOINT中的results.json哈希完全一致。会话包另含未压缩结果、summary和两次运行日志。CHECKPOINT的artifacts清单覆盖分发包及可再生结果，不表示每个未压缩副本均在Source单独保存。

字节完整性不等于数学审查。活动登记仍因此前平台拒绝而未完成，本轮未重提该请求，没有借用旧身份。参见NOTE末节。

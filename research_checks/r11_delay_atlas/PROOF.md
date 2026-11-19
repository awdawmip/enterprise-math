# R11 单拍延迟证书

在原 5,832 地址闭合系统的六个具名相位中，每次只改变一个已占用 pending 槽的一单位剩余时间。对应端口原来还需 \(r\) 拍时，该单位只改变自己在源与目标之间交付的时刻。A 至 B 的开门拍只可能短一份端口 1；当拍原门前等待为 \((2,2,1)\)，仍够释放一组。其余短缺均发生在闭门拍。第 \(r+1\) 拍实交后与基准完整场及累计具名流量全部相同。初次回复前持续可见源节点的 pending 变更，第 \(r\) 拍还可见目标等待变化。源运行核对 144 例每一拍至 256，紧凑证书专门保存首次恢复以前的每个字段替换及恢复端点，同相六周期重建其余 36,480 拍。[完整数学、分配计数与实测资源](../../research_notes/portable_direct/20261118_fair_queue_6b0fba/fiftyeighth/delay.md)

先运行标准库 `verify.py --manifest INPUT_MANIFEST.json --require-cases 144 --max-ticks 256 --strict`，可选 `--source-zip ORIGINAL.zip` 核对原始归档。其余两个入口为 `test_mutations.py` 和 `cost.py --include-certification --include-output`。目录中存放派生证书和原件指纹；机器计时应以本机输出为准。

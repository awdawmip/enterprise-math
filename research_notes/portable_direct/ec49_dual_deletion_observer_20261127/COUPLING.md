# EC49 两次删除何时首次耦合 Port 因子

2026-11-27 · 作者证明与精确复算 · 待项目评审

沿用[具名删除的对偶秩](REPORT.md)。固定一个当前可加的 Port 分区 \(P=C_1\sqcup\cdots\sqcup C_k\)，并固定当前活动标签与容量。以下判定在这一步开始、仅作删除时，该分区第一次失效是否发生在第一或第二次删除。可在任意插入后重新应用。只读取 \(\varnothing,C_1,\ldots,C_k\) 的对偶单点和两点秩，扫描各标签一次即可得到见证。

## 缺口公式

记删除集合为 \(D\)，观察函数为 \(g_D(S)=\Phi_{A\setminus D}(S)-\Phi_{A\setminus D}(\varnothing)\)。迹缺口
\[
\Delta(D)=\sum_i g_D(C_i)-g_D(P)
\]
非负。它为零当且仅当分区在所有查询上可加。确实，对任意 \(S\)，相应缺口 \(\sum_i g_D(S\cap C_i)-g_D(S)\) 随 \(S\) 增长非减，因为每增一个 Port，所在部分的边际至少为全体边际。当前分区可加，且去掉全部 Port 后原匹配秩为零，故 \(\rho_P(D)=|D|\)。直接相减得到
\[
\Delta(D)=\sum_i \rho_{C_i}(D)-|D|-(k-1)\rho_{\varnothing}(D).
\]

若单个标签 \(x\) 是 \(\rho_\varnothing\) 的非环元，则各 \(\rho_{C_i}(\{x\})=1\)，删除它不产生新耦合。若它是环元，记 \(u\) 为它在多少个 \(\rho_{C_i}\) 中为非环元，则 \(\Delta(\{x\})=u-1\)。所以第一次删除产生耦合恰当且仅当某个整体环元在至少两个部分的表中成为非环元。

## 两次才耦合的判据

假定所有可删除单标签都不产生耦合。设 \(I_S(x,y)=1\) 当且仅当 \(x,y\) 在 \(\rho_S\) 下是非环元且平行。将二点秩写为两单点秩之和减 \(I_S\)，单点缺口相消，得
\[
\Delta(\{x,y\})=(k-1)I_{\varnothing}(x,y)-\sum_i I_{C_i}(x,y).
\]
若整体表中两者不平行，非负性迫使缺口为零。若整体平行，它们在每个部分表都为非环元。此时缺口等于它们在多少个部分中被分开减一。因此两次删除第一次产生耦合，当且仅当同一整体平行类中有一对标签，在至少两个部分的类号不同。

每个整体平行类任选一个锚标签。先寻找与锚至少有两处类号不同的标签。若都只差至多一处，则只需寻找两个相对锚各差一处而且差在不同部分的标签。这两个标签彼此至少差两处。若两种寻找均失败，就不存在见证。对 \(N\) 个可删除标签和 \(k\) 个部分，总计扫描 \(O(kN)\) 个类号。

最小见证为两个单位容量 Port 和三个标签，掩码分别为 \(\{1\},\{2\},\{1,2\}\)。初态及每次单删除后两 Port 仍可满配，观察函数为零。删去两个专用标签，只剩联合掩码，两个单 Port 查询各为 1，全 Port 查询为 1，缺口为 1。少于两个 Port 没有非平凡分区。少于三个标签做两次删除后已没有目标，剩余观察是容量的可加函数。

## 精确复算

下方代码枚举两个 Port、各容量 0 至 2、至多四个目标的掩码多重集。以直接 Hall 最小值构造每个反事实状态，逐对对比独立的缺口和类号判据。程序还确认最小见证的全部三个单删除。

~~~python
from collections import Counter
from itertools import combinations, combinations_with_replacement, product

def phi(cap, masks, query):
    return min(
        sum(c for i,c in enumerate(cap) if w & (1<<i))
        - sum(e & w == e for e in masks)
        for w in range(4) if w & query == query
    )

def table(cap, masks, removed=()):
    live = [e for i,e in enumerate(masks) if i not in removed]
    return tuple(phi(cap, live, s) for s in range(4))

def gap(a):
    return a[1] + a[2] - a[0] - a[3]

counts = Counter()
for cap in product(range(3), repeat=2):
    for n in range(5):
        for masks in combinations_with_replacement(range(4), n):
            initial = table(cap, masks)
            if gap(initial):
                continue
            counts['initial_additive'] += 1
            singles = [table(cap, masks, (x,)) for x in range(n)]
            for one in singles:
                r = [x-y for x,y in zip(one, initial)]
                assert (gap(one)>0) == (r[0]==0 and r[1]+r[2]>=2)
                counts['single_checks'] += 1
            if any(map(gap,singles)):
                continue
            counts['all_singles_additive'] += 1
            for x,y in combinations(range(n), 2):
                two = table(cap, masks, (x,y))
                parallel = [
                    singles[x][s] == singles[y][s] == two[s] == initial[s]+1
                    for s in range(3)
                ]
                assert gap(two) == int(parallel[0])-int(parallel[1])-int(parallel[2])
                assert (gap(two)>0) == (parallel[0] and not parallel[1] and not parallel[2])
                counts['pair_checks'] += 1
                counts['first_coupling_pairs'] += gap(two)>0
                if gap(two):
                    assert n>=3

example = (1,2,3)
assert gap(table((1,1), example)) == 0
assert all(gap(table((1,1), example, (x,))) == 0 for x in range(3))
assert gap(table((1,1), example, (0,1))) == 1
print(dict(counts))
~~~

固定输出

~~~text
{'initial_additive': 585, 'all_singles_additive': 538, 'single_checks': 1885, 'pair_checks': 2168, 'first_coupling_pairs': 90}
~~~

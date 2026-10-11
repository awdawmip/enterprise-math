# 素数残差续接：BRC组合剖面、模数迁移与冠军起点检验

Progress-Event-ID: `prime-residual-brc-successor-20261011-a1`
Scope: `enterprise-math / formal arithmetic BRC interface experiment`
Status: `SELF_CHECKED_UNREVIEWED; NO_NATIVE_RESIDUAL_ATTRIBUTION; NO_SPEEDUP_OR_NOVEL_PRIMALITY_CLAIM`
Global-read: `46de0b0d4865d9e7410df30d96b07ee4167d1fbe`
EM-source-read: `670859d463cca9cd4d8f5e9f1d36f47792f8faa5`
Research-Activity-ID: `NONE_ALLOCATED; REGISTRATION_PENDING`

## 1. 续接边界

用户在“每个素数带残差，下一素数是否与较小冠军合数的残差累积有关”之后要求继续尝试。

已消费而不重做的前沿：EM@8592e86179396bf3090d97fd0d951e2ec5bea5dc:research_notes/divisor_extrema/20261011T001340Z-prime-residual-champions.md，blob 9752ddd6c726c9f63a0306f8d1eebf360eba5d08；本轮用固定提交的GitHub.fetch_file核对blob，并与已挂载复算包的原文一致。前轮可加约数累积恒等式、局部筛法计数及原生对应缺口保留。

本轮选择一个独立、明确的代数候选载体：二选择组合的BRC直方图。它不是晶胞力学，不给原生r_p虚构数值，不把模余数说成物理残差，也不把二选择支路当作P000的二力平衡。原生对应仍未建立；本轮没有运行经典物理参考、三角函数或平方根壳模型。

## 2. 实际BRC载体与观察许可

源码：src/enterprise_math/brc_histogram.py；固定EM-source-read；Git blob 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1。
全文件8138字节经Git blob重算与远端返回完全一致。执行原始weight_histogram、WeightHistogram和histogram_serial定义，仅以AST去掉未调用的相对import rational_prime_valuations。未冒称完整项目安装或全项目测试。

定理接口：definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md，WBRC-T36。

令T=[1]+[2]属于N[Q_{>0}^x]。每步两条正权支路，权重仅为形式标签1、2。串联n次：

H_n=T^(tensor n)=sum_{j=0}^n b(n,j)[2^j], b(n,j)=binom(n,j).

支路身份是二进制选择串；在本轮只观察选择1的总次数j、其精确多重数，以及继续追加相同选择。对这些观察，按j合并由卷积定理保证；支路次序敏感、原生位置/场/力观察不在该压缩许可中。2^j作为权重的数值不是物理能量。全过程正计数没有符号质量抵消。

BRC给出b(n+1,j)=b(n,j-1)+b(n,j)，和H_(ab)=H_a^(tensor b)。因此同一候选状态同时有乘法分组与n->n+1的精确更新。

## 3. 每个素数携带的非零除整剖面

用X作权重2的形式标记，F_n(X)=(1+X)^n。对素数p，定义：

Q_p(X)=sum_{j=1}^{p-1} [binom(p,j)/p] X^j,
F_p(X)=1+X^p+p Q_p(X).

Q_2=X；Q_3=X+X^2；Q_5=X+2X^2+2X^3+X^4。
这些Q_p是明确的非零整数多项式，不因模p的余数为零而消失。

合数pq的组合可由：
F_(pq)(X)=(1+X^p+pQ_p(X))^q
精确计算；所有交互项由串联展开决定，而不是任意拟合K。交换p与q得到同一完整结果。它是本轮代数模型的组合律，不是原生素数残差的既有定义。

## 4. 全剖面判据与最早失败因子

对n>=2、1<=j<n，定义r(n,j)=binom(n,j) mod n，取0..n-1。

经典判据：n为素数，当且仅当所有内部r(n,j)=0。AKS原文Lemma 2.1给出更一般的多项式表述；本轮没有重新发现该判据，也没有执行完整AKS算法。

本轮明确重证的细化：n合成，ell为最小质因子，则

min{j:1<=j<n,r(n,j)!=0}=ell；r(n,ell)=n/ell。

证明：j<ell时gcd(j,n)=1，利用j*binom(n,j)=n*binom(n-1,j-1)得n整除该系数。j=ell时，binom(n-1,ell-1) mod ell=1，因为分子逐项为-1,...,-(ell-1)，分母可逆；ell=2亦成立。故binom(n,ell)=(n/ell)*binom(n-1,ell-1) mod n=n/ell，严格非零。

这是任意合数的代数结论，不依赖有限表拟合；不宣称文献首创。证明使用最小因子，但执行分类器只消费BRC系数，不接收n的因子、未来素数表或标签。

## 5. 模数迁移必须保留整数商

对全部系数（含两端）记b(n,j)=n q(n,j)+r(n,j)。越界坐标为零。令Q=q(n,j-1)+q(n,j)，R=r(n,j-1)+r(n,j)。

r(n+1,j)=(R-Q) mod(n+1)；
q(n+1,j)=floor((n Q+R)/(n+1))。

此式由n=-1 mod(n+1)直接推出。只把当前模n余数带到下一步并套Pascal加法是不正确的；整数商重新进入下一模数读数。模余数为零不等于完整状态为零。

本轮另做一般直方图的压缩反例：A=(1+X)^11，A'=A+11 X(X-1)(X-2)。A'的所有系数仍非负。A、A'有相同CWM=(2048,177147,2048)、相同全部系数模11余数；但同样乘(1+X)后，X^2系数模12分别为6、7。此反例只说明一般直方图的上述压缩不是模数迁移安全的；A'不冒称第11个标准二选择剖面，也不声称已知n时不能从头重算标准剖面。

## 6. 实际精确验证结果

使用原始BRC直方图串联生成n=1..1000，先分类，再调用独立试除核验；后者不进入状态或预测规则。

- 分类范围2..1000，共999个整数；168个素数、831个合数；不一致0。
- 系数与独立组合数公式逐项对比501500次。
- 商/余数迁移关系逐项核对501495次。
- n=1..10完整二进制支路族与直方图一致，共10项。
- a,b=1..8的乘法分组一致64项。
- p,q取2,3,5,7的除整剖面重建/串联一致16项。
- n行完整系数按ASCII `n:c0,c1,...,cn\n` 顺次散列的SHA256：91f1b084f9e8a0c921176eb71bfb6c6988990d896b3c6ea7b81b64e317217059。

|n|最早非零j|r(n,j)|结论|
|---:|---:|---:|---|
|120|2|60|合数|
|121|11|11|合数|
|122|2|61|合数|
|123|3|41|合数|
|124|2|62|合数|
|125|5|25|合数|
|126|2|63|合数|
|127|无|内部全部0|素数|
|341|11|31|合数|
|561|3|187|合数|
|645|3|215|合数|

因此本轮从H=120逐步计算，完整判据的第一个后继素数为127；并非预先给出127再拟合。

## 7. 总量和有限折叠的失败

把内部分布压成一个合计，得到E(n)=(2^n-2) mod n。它不是充分的素性判据。

2..1000内，完整模型抓住而总量漏掉的合数恰为341、561、645。其中341=11*31，在j=11处余数31，尽管合计余数0。这里是取模后的合计遮蔽了分布，不是正质量彼此抵消。

另将完整剖面按j mod r折叠，对r=1..30实算：341在r=1,2,3仍误过；561在r=1,2,4误过；645在r=1,2误过；121均未误过。仅为4个固定合数的有限测试，不把r=5等小值宣称为普遍充分。AKS的多项式压缩有其额外条件，不能用单一r或单一基底冒充完整AKS。

## 8. 冠军是否特殊：本模型没有证明

H_n=H_H tensor T^(tensor(n-H))对每个0<=H<n成立，不要求H是冠军。实际分别从30、60、90、120、125续推到127，所有逐步完整状态相同。30/60/120是前轮同质因子支持、不同幂次的对照；90、125只是非严格约数纪录者对照。

各起点之后的首个素数分别是31、61、97、127、127，但到同一候选127时状态完全一致。起点依赖与目标位置必须分开；不能用不同起点后首素数不同当成模型不一致。

结论限定：在此模型，冠军不是独立的数学信息来源；它可以是缓存或分组起点。尚未证明或排除某种实现上的计算效率优势，不将本模型的结论扩张成所有原生残差模型不可能。

## 9. 计算成本与真正未决项

标准行有n+1个系数，最大系数有O(n)比特，完整行总存储O(n^2)比特量级。顺序扫描至N有O(N^2)次系数操作；大整数位运算成本还需另计。这不是关于输入位长log n的多项式时间实现，不是跳跃预测公式，不比试除更快的证据。

本轮完成的是：正式BRC载体、无需未来标签的素数/合数判别、非零Q_p和后继更新关系，以及总量压缩反例。未完成的是心跳原生构型到此载体的对应、冠军的额外判别/效率优势，以及无需完整剖面的低成本后继规则。

具体下一单元：在事先固定的观察范围和未来步数下，寻找能保留首个失败通道及模数迁移所需商信息的较小BRC商载体；把由冠军因数结构决定的分组与等成本非冠军分组作对照。先证明该压缩的观察许可，再测试；原生对应作为独立待证接口，不用代数试验自行升级。

## 10. 复算文件和来源

当前对话复算包包含完整源码、reproduce.py、observer_checks.py、results.json、all_results.json、selected_exact_profiles.json、observer_results.json及散列清单。源笔记保全本轮定义、证明、精确输入、算法和验证范围；附件路径不是跨对话来源。

主循环复写关系：从原始BRC weight_histogram([1])开始，每步histogram_serial(H,weight_histogram([1,2]))；按权重2^j取精确整数多重数，检查1<=j<n的首个系数模n非零。所有行与comb(n,j)独立逐项比较；前行逐系数divmod(n-1)后用第5节关系预测本行。完整脚本未将试除结果作为分类输入。

文件SHA256：
- brc_histogram_source.py: 256ef167e2aee651c042195522a0013ba619f265f9e4d8fa24f07d3399695a67
- reproduce.py: 87f5d382468d2f9d55bad9bdc39f3be65d119d4a6a98377b8ee89fc43436cc47
- results.json: eae173c147de34d158f0a44831d36de1fd46b24994e85e461bf5a90a9520973d
- all_results.json: 9e8511fb3a112d130a00348af1a33d5b4a729a40104b89fcbebcb2f8eaeb3d80
- selected_exact_profiles.json: f4067d9a612ecfbd9fd38a0b5e3c2e2b648a92c45866202cc8b47035ebf67bca

外部原始来源：M. Agrawal, N. Kayal, N. Saxena, PRIMES is in P，作者机构PDF https://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf 。本轮实际核读第2节、Lemma 2.1及其页面截图。只把基本多项式判据和压缩边界归于该文，不把本轮完整系数遍历称为AKS实现。

本轮原生登记实调em_session_start(request_id=prime-residual-champion-continuation-20261011-s1)返回STATIC_READONLY_SCOPE_DENIED，operation_sent=false。没有已分配研究员、activity、CLAIM或准入。本次独立研究笔记的GitHub保全不冒称原生登记修复；没有改定时任务或其他owner。

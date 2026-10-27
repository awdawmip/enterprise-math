# PREFIX-284｜真正可实施的来源Detector与X6模型桥接

**不要重做：**PREFIX-282已在原始Stage50执行40次local，确认f=(1,4,4)、g=(2,5,2)在所有自相关外Port观察下相同，但软件packet_variance可从完整输入包作来源对角诊断。PREFIX-283已经用精确BRC有序路径对证明：

$$\Delta(E)=(-3E_{00}-9E_{11}+12E_{22}-12\operatorname{Re}E_{01}+12\operatorname{Re}E_{12})/33.$$

所有Toeplitz效应都失辨；若有真正来源对角二元效应，最大单次概率差为4/11，等先验来源样本最佳判别率15/22。PREFIX-283本轮精确代码PASS（19,683个Hermitian系数、243个Toeplitz系数、8个binary masks、32个C4检查），**不是本轮执行原始Stage50或原生物理心跳实验**。

**首要未决点：**Source是否提供对单个完整、已准备好的X6心跳后态实行的合法、来源敏感Detector/Port效应（不是重新构造输入包计算packet_variance）？如果有，将Source定义的效应映射到上述E，检验实际E是否落在失辨超平面之外；实际运行合法原生输入/输出，并保存精确范围与读回证据。

如果真实接口未发现/无法核实，不推断整个世界没有此类仪器；在明确已证合法的外Port与操作代数内证明观察闭包及不可辨识条件。必须定位六维Cell、Port、材料动量、完整场、来源、边界、C4相位、独立时间及model_law_id，并区分来源历史差与心跳步数。

固定上一轮输入GLOBAL c2658a2945f4decaf267d7f75f70eda63e6740ea / EM bf16665ae130258a99c8516298361152e618c308；下一轮必须读取届时真正最新规范与权限。当前GitHub认证awdawmip/admin；原生task query CONTROL_QUOTA、session start STATIC_READONLY_SCOPE_DENIED，owner/CLAIM不详，不得擅自接管。

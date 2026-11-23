# EC49FYJ — Exact all-column-count adaptive observer law (frozen support atlas)

Date 2026-11-24. Parent EC49FYI@658fa6821eb7a37c1d794ffe474b344be2dc0660, research_notes/portable_direct/EC49FYI_DEPTH14_VERIFY.js and EC49FYI_EXACT_ADAPTIVE_DEPTH14_THEOREM.md. Frozen BRC16943 support atlas (50 nonempty ten-bit masks) copied exactly from parent. This extends the auxiliary one-hole Boolean product model, not arithmetic realizability for new moduli or native X6 attribution. AUTHOR_PROVED / EXACT_FINITE_CONSTRUCTIVE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.

## Statement
For integer m>=1 let states be (U,z) with U in F and z=-1,0,...,m-1. A probe (t,j) returns bit_t(U) times 1[z!=j]. All m columns labeled, no free information, noiseless single-site adaptive queries, exact recovery of both labels. Let Q(m) be optimal worst-case query cost. Then Q(1)=infinity (all 50 hole states identical); Q(2)=Q(3)=8; Q(4)=Q(5)=9; Q(m)=m+3 for every integer m>=6.

## Lower bounds
For m>=2 all states distinguishable by full array: the nonzero columns give U (nonempty), and the unique all-zero column, if any, identifies the hole. A binary tree with 50(m+1) leaves requires at least ceil(log2(50(m+1))) reads. This gives 8 for m=2,3 and 9 for m=5. For m=4, 250 leaves at depth 8 would require each root branch <=128. For row t with c_t supports containing t, the two root sizes are 250-4c_t and 4c_t for every physical column j, since exactly four of five z values give a positive reading on such a support. The ten c_t and branch sizes in the output below have min of the larger branch = 134 >128. Thus Q(4)>=9, by exact root obstruction independent of any solver.

For all m>=2 the full state U=833 forces m positive observations to distinguish the m same-support single-hole variants, and at least three negative observations to distinguish its full supersets 857,867,965 with pairwise disjoint extra masks 24,34,132. Thus Q(m)>=m+3. All masks checked against the frozen list.

## Extension lemma (all nonempty support families)
For any m>=2 with an exact decision tree, Q(m+1)<=Q(m)+1. Run the m-column tree restricted to the first m columns. A hole in the added column is indistinguishable from the full state on those columns, so the tree returns (U,-1) in both cases. If the tree instead returns a hole in the original block, then that is the true hole and the support is already decoded. If it returns full, use any row t in U to read the added column exactly once: 1 means full, 0 means hole in the added column. No support or hole label is lost. More generally Q(m+r)<=Q(m)+r by inspecting added columns on that same known positive row until a hole is found, or all are certified present. This is a construction, not a claim that unseen columns were erased or have no residual. It holds for the declared future probe and label-recovery language only. For every m>=6 the m=6 base tree of depth 9 extends with m-6 probes, meeting m+3. For m=4 the m=3 depth-8 tree gives depth at most 9.

## Finite base constructions
Reuse FYI's full A and sorted hole-fibre H_j exact quotient, parameterized by m. Candidate branches are Boolean supports; multiplicities of equal fibres and physical column decoder retained. Search is only a constructor; the raw labeled decision tree replay, without any quotient or pruning assumptions, checks every state. Four base trees at m=2,3,5,6 suffice. Exact counts use BigInt bitsets and ordinary exact small integer counts. No numerical approximation, no new Farey enumeration. The prior m=11 conclusion is recovered as a corollary, not rerun. In the attached code q=m*t+j, branches 0 then 1, leaf -1-((m+1)*i+z+1). The full trees are embedded below as compact JSON, so a separate checker can replay them without running search.

## Executed verification summary
```json
{
  "rows": [
    37,
    26,
    29,
    25,
    28,
    23,
    29,
    26,
    27,
    22
  ],
  "m4splits": [
    [
      102,
      148
    ],
    [
      146,
      104
    ],
    [
      134,
      116
    ],
    [
      150,
      100
    ],
    [
      138,
      112
    ],
    [
      158,
      92
    ],
    [
      134,
      116
    ],
    [
      146,
      104
    ],
    [
      142,
      108
    ],
    [
      162,
      88
    ]
  ],
  "m4best": 134,
  "bases": [
    {
      "m": 2,
      "d": 8,
      "calls": 420,
      "memo": 134,
      "states": 150,
      "nodes": 149,
      "max": 8,
      "sum": 1094
    },
    {
      "m": 3,
      "d": 8,
      "calls": 543,
      "memo": 173,
      "states": 200,
      "nodes": 199,
      "max": 8,
      "sum": 1544
    },
    {
      "m": 5,
      "d": 9,
      "calls": 844,
      "memo": 268,
      "states": 300,
      "nodes": 299,
      "max": 9,
      "sum": 2503
    },
    {
      "m": 6,
      "d": 9,
      "calls": 2206,
      "memo": 879,
      "states": 350,
      "nodes": 349,
      "max": 9,
      "sum": 2992
    }
  ]
}
```

## Reproducible constructor and raw-label audit (Node.js)
```javascript
function verify(){
const F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005];
const ck=(b,s)=>{if(!b)throw Error(s)};
const bit=i=>1n<<BigInt(i), ALL=bit(50)-1n, cmp=(a,b)=>a<b?-1:a>b?1:0;
function pc32(x){x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24}
const pc=x=>pc32(Number(x&0xffffffffn))+pc32(Number(x>>32n));
const mask=p=>F.reduce((v,u,i)=>p(u,i)?v|bit(i):v,0n);
const row=Array.from({length:10},(_,t)=>mask(u=>u>>t&1));
const sup=F.map(u=>mask(v=>u!==v&&(u&v)===u));
const neg=F.map(u=>{const out=Array.from({length:11},()=>[]);for(let m=0;m<1024;m++)if(!(m&u))out[pc(BigInt(m))].push(mask(v=>m&v));return out});
function run(m,d){
const canon=(a,h)=>[a,...h.slice().sort(cmp)];
const count=s=>s.reduce((n,v)=>n+pc(v),0);
function child(s,t,j,b){const g=b?row[t]:ALL^row[t];return canon(s[0]&g,s.slice(1).map((h,k)=>k===j?(b?0n:h):h&g))}
function lower(s,n,d){let l=0;while(2**l<n)l++;if(l>d)return l;for(let i=0;i<50;i++)if(s[0]&bit(i)){let p=0;for(let j=1;j<=m;j++)if(s[j]&bit(i))p++;const target=s[0]&sup[i];let q=0;while(q<=d-p&&q<=10&&!neg[i][q].some(v=>(v&target)===target))q++;l=Math.max(l,p+q);if(l>d)return l}return l}
const memo=new Map();let calls=0;
function solve(s,d){calls++;const n=count(s);if(n<=1)return true;if(d<=0||n>2**d)return false;const k=s.join(','),v=memo.get(k)||{lo:0,hi:999};if(v.lo>d)return false;if(v.hi<=d)return true;const l=lower(s,n,d);if(l>d){v.lo=Math.max(v.lo,l);memo.set(k,v);return false}
const opts=[];for(let j=0;j<m;j++){if(j&&s[j+1]===s[j])continue;for(let t=0;t<10;t++){let n1=pc(s[0]&row[t]);for(let z=0;z<m;z++)if(z!==j)n1+=pc(s[z+1]&row[t]);let n0=n-n1;if(n0&&n1&&Math.max(n0,n1)<=2**(d-1))opts.push([Math.max(n0,n1),t,j,n0,n1])}}
opts.sort((x,y)=>x[0]-y[0]||x[1]-y[1]||x[2]-y[2]);for(const [,t,j,n0,n1] of opts){let a=child(s,t,j,0),b=child(s,t,j,1);if(lower(a,n0,d-1)>d-1||lower(b,n1,d-1)>d-1)continue;if(n0<n1)[a,b]=[b,a];if(solve(a,d-1)&&solve(b,d-1)){v.hi=d;v.t=t;v.j=j;memo.set(k,v);return true}}v.lo=Math.max(v.lo,d+1);memo.set(k,v);return false}
ck(solve(Array(m+1).fill(ALL),d),"base construction");
const states=F.flatMap((u,i)=>Array.from({length:m+1},(_,z)=>({id:(m+1)*i+z,u,i,z:z-1})));
const read=(s,t,j)=>Number(Boolean((s.u>>t&1)&&s.z!==j));
function residual(ss){let a=0n,h=Array(m).fill(0n);for(const s of ss){if(s.z<0)a|=bit(s.i);else h[s.z]|=bit(s.i)}const perm=Array.from({length:m},(_,j)=>j).sort((i,j)=>cmp(h[i],h[j])||i-j);return {key:canon(a,h),perm}}
function build(ss,d){if(ss.length===1)return -1-ss[0].id;const {key,perm}=residual(ss);ck(solve(key,d),"subtree");const v=memo.get(key.join(',')),t=v.t,j=perm[v.j];const a=ss.filter(s=>!read(s,t,j)),b=ss.filter(s=>read(s,t,j));ck(a.length&&b.length,"nonconstant");return [m*t+j,build(a,d-1),build(b,d-1)]}
const tree=build(states,d);let max=0,sum=0,nodes=0;const leaves=new Set();
function audit(n){if(typeof n==="number"){ck(n<0,"leaf");return;}ck(n.length===3&&n[0]>=0&&n[0]<10*m,"probe");nodes++;audit(n[1]);audit(n[2]);}
audit(tree);
for(const s of states){let n=tree,k=0;while(Array.isArray(n)){n=n[1+read(s,Math.floor(n[0]/m),n[0]%m)];k++}ck(n===-1-s.id&&k<=d,"raw replay");leaves.add(n);max=Math.max(max,k);sum+=k}
ck(nodes===states.length-1&&leaves.size===states.length&&max===d,"tree coverage");
return {m,d,calls,memo:memo.size,states:states.length,nodes,max,sum,tree};
}
const rows=row.map(pc),m4splits=rows.map(x=>[250-4*x,4*x]);
ck(m4splits.every(([a,b])=>Math.max(a,b)>128),"m4 root obstruction");
const U=833,V=[857,867,965],diff=V.map(v=>v^U);
ck(F.includes(U)&&V.every(v=>F.includes(v)&&(v&U)===U)&&diff.every(x=>x)&&!(diff[0]&diff[1])&&!(diff[0]&diff[2])&&!(diff[1]&diff[2]),"lower witness");
return {F,rows,m4splits,m4best:Math.min(...m4splits.map(x=>Math.max(...x))),bases:[[2,8],[3,8],[5,9],[6,9]].map(([m,d])=>run(m,d))};
}
console.log(JSON.stringify(verify(),null,2));
```

## Explicit constructive certificates
```json
[{"m":2,"d":8,"tree":[0,[5,[1,[8,[2,[9,[3,-78,-62],[13,-65,[17,-92,-50]]],[4,[3,-63,-61],[6,[10,-102,-81],-114]]],[4,[3,[12,-66,[16,-93,-51]],[12,-64,[16,-91,-49]]],[6,[2,[12,-123,-147],-6],[10,-69,-129]]]],[3,[7,[9,[11,-131,-104],[11,-116,-119]],[13,[11,-35,-107],[9,-74,-134]]],[7,[15,[9,-137,-56],[11,-26,-29]],[9,[11,-23,[13,-41,-83]],[11,-8,-14]]]]],[13,[7,[1,[3,[4,-122,-121],[2,-101,-100]],[3,[9,-59,[11,-125,-140]],[11,-2,-86]]],[1,[4,[11,-68,-128],[10,-67,-127]],[3,[9,-44,[11,-17,-110]],[9,-20,[11,-38,-71]]]]],[1,[4,[3,[7,-146,-77],[7,[9,-80,-5],-113]],[2,[6,-145,-76],[6,[8,-79,-4],-112]]],[3,[15,[19,-11,-95],[7,[9,-143,-32],-149]],[11,[9,-47,-89],[7,-98,-53]]]]]],[1,[2,[8,[10,[4,[6,-132,-75],[12,-60,-144]],[6,[4,-105,[18,-12,-96]],[12,-45,-150]]],[4,[6,[10,-117,-120],[10,[12,-36,-135],-108]],[6,[10,-126,[12,-141,-33]],[10,-18,-111]]]],[4,[6,[14,[8,-138,-57],[10,-27,-30]],[8,[10,-24,[12,-42,-84]],[10,-9,-15]]],[6,[8,[10,-48,-99],[10,[12,-3,-90],-87]],[8,[12,-21,-54],[10,-39,-72]]]]],[2,[8,[10,[4,[6,-130,-73],[12,-58,-142]],[6,[4,-103,[18,-10,-94]],[12,-43,-148]]],[4,[6,[10,-115,-118],[10,[12,-34,-133],-106]],[6,[10,-124,[12,-139,-31]],[10,-16,-109]]]],[4,[6,[14,[8,-136,-55],[10,-25,-28]],[8,[10,-22,[12,-40,-82]],[10,-7,-13]]],[6,[8,[10,-46,-97],[10,[12,-1,-88],-85]],[8,[12,-19,-52],[10,-37,-70]]]]]]]},{"m":3,"d":8,"tree":[0,[13,[7,[20,[5,[8,[1,-84,-138],[9,-163,[15,-91,-171]]],[4,[6,[12,-83,-87],-135],[1,[3,-82,-81],-54]]],[2,[9,[3,-195,[12,-107,-7]],[6,[24,-123,-67],[3,-103,-151]]],[4,[10,-174,-98],[10,-182,[16,-30,-110]]]]],[1,[3,[4,[6,-102,[8,-104,-101]],[10,[16,-134,-106],-150]],[5,[9,[15,-136,-108],-152],[9,[15,-133,-105],-149]]],[4,[22,[10,[28,-14,-126],-58],[10,[19,-78,-190],-198]],[10,[16,-62,-130],[19,-26,-70]]]]],[4,[10,[1,[19,[6,-162,[8,-164,-161]],[6,-194,[8,-196,-193]]],[7,[16,-154,-158],[16,-166,[19,-186,-42]]]],[1,[16,[6,-90,[8,-92,-89]],[6,-170,[8,-172,-169]]],[7,[16,[19,-46,-178],-142],[16,-22,-146]]]],[1,[9,[7,[19,-86,[25,-122,-66]],[3,-6,[5,-8,-5]]],[5,[18,-88,[24,-124,-68]],[18,-85,[24,-121,-65]]]],[7,[10,[16,-34,[22,-74,-38]],[16,-10,-18]],[10,[16,[19,-2,-118],-114],[16,-50,-94]]]]]],[3,[12,[7,[15,[1,[6,[9,-175,-99],[18,-79,-191]],[2,[9,-176,-100],[9,-173,-97]]],[6,[1,-139,[2,-140,-137]],[9,[27,-15,-127],[18,-59,-199]]]],[2,[21,[9,[27,-16,-128],-60],[9,[18,-80,-192],-200]],[21,[9,[27,-13,-125],-57],[9,[18,-77,-189],-197]]]],[6,[28,[11,[2,-48,[15,-155,-159]],[27,[1,-47,-45],[15,-179,-143]]],[2,[9,[15,-156,-160],[15,-180,-144]],[9,[15,-153,-157],[15,-177,-141]]]],[22,[15,[1,[9,-167,-23],[2,-168,-165]],[9,[18,-187,-43],-147]],[2,[9,[18,-188,-44],[15,-24,-148]],[9,[18,-185,-41],[15,-21,-145]]]]]],[6,[9,[13,[12,[1,-183,[2,-184,-181]],[15,-35,[21,-75,-39]]],[2,[15,-36,[21,-76,-40]],[15,-33,[21,-73,-37]]]],[19,[17,[1,[12,-31,-11],-56],[18,[1,-55,-53],[12,-111,-19]]],[2,[12,[15,-32,-112],[15,-12,-20]],[12,[15,-29,-109],[15,-9,-17]]]]],[18,[13,[11,[2,-28,[15,-3,-115]],[12,[1,-27,-25],[15,-51,-95]]],[2,[9,[15,-4,-116],[15,-52,-96]],[9,[15,-1,-113],[15,-49,-93]]]],[15,[12,[1,-63,[2,-64,-61]],[1,-119,[2,-120,-117]]],[9,[1,-131,[2,-132,-129]],[1,-71,[2,-72,-69]]]]]]]]},{"m":5,"d":9,"tree":[10,[6,[42,[21,[1,[15,[5,[20,-207,[25,-231,-237]],[25,-51,-57]],[25,[0,-183,[20,-45,-15]],[5,-213,-27]]],[25,[0,[11,-206,[46,-20,-188]],[15,-262,-148]],[2,-208,[3,-209,[4,-210,-205]]]]],[28,[33,[3,[15,[25,-233,-239],-215],[0,-32,-70]],[2,[15,-232,-268],[0,-230,[4,-234,-229]]]],[16,[0,[11,-236,-62],[2,-238,[4,-240,-235]]],[0,[11,-212,-218],[2,-214,[4,-216,-211]]]]]],[22,[18,[46,[1,[5,-261,-273],[0,-116,-149]],[0,[11,-260,-284],[3,-263,[4,-264,-259]]]],[1,[2,[7,-152,-123],[5,-147,[30,-81,-165]]],[0,[11,-146,[31,-86,-296]],[4,-150,-145]]]],[1,[12,[0,[30,-129,-99],[5,[30,-69,-267],-111]],[16,[31,-242,-290],[26,-134,-254]]],[48,[3,[30,-71,-269],[0,-68,[4,-72,-67]]],[0,[11,-266,[26,-248,-278]],[4,-270,-265]]]]]],[22,[2,[30,[17,[7,[0,[20,-124,-130],-82],[26,-200,-158]],[5,[11,-122,-224],[8,-125,[9,-126,-121]]]],[25,[0,[40,-184,-100],[15,-52,[20,-46,-16]]],[15,[20,-274,[35,-112,-58]],[20,-166,-28]]]],[18,[3,[35,[15,-275,-83],[25,-47,-167]],[0,[11,-272,[26,-92,-194]],[4,-276,-271]]],[0,[11,[26,-44,[31,-80,-164]],[31,-38,-104]],[4,[25,-48,[30,-84,-168]],[25,-43,[30,-79,-163]]]]]],[3,[18,[1,[30,[5,-8,-131],[40,-185,-101]],[15,[25,-53,[35,-113,-59]],[25,-17,-29]]],[30,[5,[31,-128,[41,-182,-98]],[9,-132,-127]],[9,[40,-186,-102],[40,-181,-97]]]],[0,[11,[16,[26,-50,[36,-110,-56]],[26,-14,-26]],[16,[26,[31,-2,-176],-170],[26,-74,-140]]],[4,[15,[25,-54,[35,-114,-60]],[25,-18,-30]],[15,[25,-49,[35,-109,-55]],[25,-13,-25]]]]]]],[20,[5,[26,[1,[17,[25,[0,-154,[30,-117,-285]],[45,-21,-189]],[11,[0,-153,[30,-87,-297]],[13,-155,[14,-156,-151]]]],[30,[2,-118,[3,-119,[4,-120,-115]]],[2,-286,[3,-287,[4,-288,-283]]]]],[15,[45,[2,-22,[3,-23,[4,-24,-19]]],[2,-190,[3,-191,[4,-192,-187]]]],[30,[2,-88,[3,-89,[4,-90,-85]]],[2,-298,[3,-299,[4,-300,-295]]]]]],[1,[47,[31,[0,[6,-159,-202],[15,-93,[30,-39,-105]]],[7,[15,-160,-226],[8,-161,[9,-162,-157]]]],[15,[6,[0,-201,-195],[8,-203,[9,-204,-199]]],[6,-225,[8,-227,[9,-228,-223]]]]],[15,[25,[2,-94,[3,-95,[4,-96,-91]]],[2,-196,[3,-197,[4,-198,-193]]]],[30,[2,-40,[3,-41,[4,-42,-37]]],[2,-106,[3,-107,[4,-108,-103]]]]]]],[1,[47,[15,[8,[12,[30,-244,-292],[0,-11,-63]],[6,[0,-9,-3],[7,-10,[9,-12,-7]]]],[11,[5,[0,-135,-33],[25,-75,-141]],[12,[25,-136,-256],[13,-137,[14,-138,-133]]]]],[11,[25,[0,[30,-243,-291],[5,-249,-177]],[15,[5,-279,-171],[0,-255,-219]]],[13,[15,[30,-245,-293],-257],[14,[15,[30,-246,-294],-258],[15,[30,-241,-289],-253]]]]],[5,[27,[2,[15,[25,-250,[30,-280,-64]],[25,-34,-220]],[15,[3,-251,[4,-252,-247]],[3,-35,[4,-36,-31]]]],[48,[3,[15,[30,-281,-65],-221],[4,-66,-61]],[4,[15,-282,-222],[15,-277,-217]]]],[15,[47,[2,[25,[30,-4,-178],-172],[3,-5,[4,-6,-1]]],[25,[3,-179,[4,-180,-175]],[3,-173,[4,-174,-169]]]],[25,[2,-76,[3,-77,[4,-78,-73]]],[2,-142,[3,-143,[4,-144,-139]]]]]]]]]},{"m":6,"d":9,"tree":[12,[36,[19,[32,[9,[15,[0,[25,-303,-268],[1,-80,-242]],[1,[37,-282,-338],[25,[37,-135,-331],-289]]],[2,[7,[24,-143,-150],[25,-233,-9]],[13,-58,[25,-107,[37,-2,-205]]]]],[43,[8,[0,[55,-23,-219],[18,-241,-248]],[14,[1,-94,[25,-317,-128]],[25,-226,-198]]],[0,[13,[7,[25,-240,-275],-65],[1,-184,[37,-324,-72]]],[3,-243,[4,-244,[5,-245,-239]]]]]],[48,[32,[1,[13,[37,[25,-142,-149],[49,-212,-114]],[7,[25,-177,-156],-261]],[37,[13,[0,-79,-249],[7,-37,-86]],[7,[25,-170,-310],[25,-51,-16]]]],[57,[13,[25,[37,-93,-191],[0,-30,-250]],[43,[7,-100,-121],[25,-44,-163]]],[0,[49,[13,-247,-254],[1,-296,-345]],[4,-251,[5,-252,-246]]]]],[8,[2,[0,[24,-144,-151],[6,-81,-95]],[3,-82,[4,-83,[5,-84,-78]]]],[45,[4,[0,[24,-145,-152],-97],[3,-96,[5,-98,-92]]],[24,[10,-146,[11,-147,-141]],[10,-153,[11,-154,-148]]]]]]],[7,[55,[44,[20,[6,[2,-172,-304],[24,-318,-129]],[0,[48,-213,-115],[6,-311,[30,-17,-31]]]],[21,[6,[3,-173,[30,-269,-276]],[30,-59,-66]],[1,[6,-171,[30,-52,-192]],[4,-174,[5,-175,-169]]]]],[26,[2,[42,[18,-305,-312],[30,-270,-277]],[3,-306,[4,-307,[5,-308,-302]]]],[45,[3,[18,[30,-271,-278],-313],[4,-314,[5,-315,-309]]],[30,[4,-272,[5,-273,-267]],[4,-279,[5,-280,-274]]]]]],[20,[26,[51,[30,[42,[0,-214,-18],[18,-60,-53]],[2,[18,-67,-32],-320]],[2,[18,[24,-319,-130],[0,-116,-193]],[4,-321,[5,-322,-316]]]],[33,[3,[30,-61,[42,-131,-68]],[4,-62,[5,-63,-57]]],[42,[4,-132,[5,-133,-127]],[4,-69,[5,-70,-64]]]]],[3,[9,[0,[48,-215,-117],[24,[30,-54,-194],[30,-19,-33]]],[48,[10,-216,[11,-217,-211]],[10,-118,[11,-119,-113]]]],[24,[30,[4,-55,[5,-56,-50]],[4,-195,[5,-196,-190]]],[30,[4,-20,[5,-21,-15]],[4,-34,[5,-35,-29]]]]]]]],[49,[1,[38,[56,[20,[0,[18,[24,-235,-11],-263],[6,-136,-3]],[6,[0,-157,[24,-101,-38]],[24,-45,[30,-87,-164]]]],[9,[0,[6,[18,-283,-297],-236],[18,[30,-290,-325],-255]],[7,[0,-234,-199],[10,-237,[11,-238,-232]]]]],[42,[27,[9,[0,-12,[54,-24,-220]],[18,[30,-108,-227],-122]],[7,[0,-10,-206],[10,-13,[11,-14,-8]]]],[9,[0,[6,[18,-339,-178],-264],[18,[24,-332,-73],-346]],[7,[18,-185,-262],[10,-265,[11,-266,-260]]]]]],[26,[39,[9,[18,[6,[54,-26,-222],-229],[3,-47,[30,-39,-256]]],[2,[18,[30,-4,-200],-46],[4,-48,[5,-49,-43]]]],[58,[4,[6,[54,-27,-223],-230],[2,[24,-25,-74],[5,-28,-22]]],[2,[6,-221,[24,-228,-207]],[5,[6,-224,-231],[6,-218,-225]]]]],[6,[21,[3,[18,-75,[30,-40,-257]],[4,-76,[5,-77,-71]]],[30,[4,-41,[5,-42,-36]],[4,-258,[5,-259,-253]]]],[57,[3,[30,[36,-5,-208],-201],[4,-6,[5,-7,-1]]],[30,[4,-209,[5,-210,-204]],[4,-202,[5,-203,-197]]]]]]],[2,[18,[27,[10,[0,[6,[36,-285,-341],-188],[36,-137,-333]],[8,[0,-186,-109],[9,-187,[11,-189,-183]]]],[42,[14,[0,-284,-291],[16,-286,[17,-287,-281]]],[14,[0,-340,-326],[16,-342,[17,-343,-337]]]]],[27,[45,[0,[24,-180,[30,-159,-299]],[6,-102,-123]],[14,[0,-179,-347],[16,-181,[17,-182,-176]]]],[30,[14,[0,-158,-88],[16,-160,[17,-161,-155]]],[14,[0,-298,-165],[16,-300,[17,-301,-295]]]]]],[18,[45,[3,[24,[6,[36,-138,-334],-110],[30,-292,-327]],[6,[4,-293,[5,-294,-288]],[4,-111,[5,-112,-106]]]],[58,[4,[24,[36,-139,-335],-328],[5,-140,-134]],[5,[24,-336,-329],[24,-330,-323]]]],[9,[3,[6,[36,-103,-348],[24,-124,[30,-89,-166]]],[36,[4,-104,[5,-105,-99]],[4,-349,[5,-350,-344]]]],[28,[4,[24,-125,[30,-90,-167]],[5,-126,-120]],[5,[30,-91,-168],[30,-85,-162]]]]]]]]}]
```

## Continuation
The all-m worst-case law is closed within the fixed atlas. Next distinct direction: determine nonadaptive cost for all m or the expected-cost optimum under depth Q(m). Arithmetic realizability of this 50-mask atlas at changed moduli, finite height or native X6 requires a separate bridge. Current task exact receipt r4-20261124-0425-ec49as-current-read-v1 returned absence of canonical RS-EC49AS publication directory at adf001b4d1f6ab2e9311c790af75a13fafae54aa. No formal shared CLAIM/Result/Review. Historical own registration EM-DIRECT-23537B / RA-2D7B4AD1AA5CD3F5D9EF1C76 original receipt verified; activity association separately tracked.


const fixedPrimes = ["5","7","11","13","17","19","31","37","41","61","71","73","97","109","113","127","151","181","241","257","281","331","337","433","577","631","641","673","1321","14449","23311","29191","38737","54001","65537","87211","246241","262657","279073","6700417","18837001","29247661","487824887233","29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);
const B=[0,3,5,8,10,15,21,23,26,28,30,31,33];
const gcd=(a,b)=>b?gcd(b,a%b):a;
const lcm=(a,b)=>a/gcd(a,b)*b;
const weight=n=>{let w=0;for(let p=2;p<=n;p++)for(;n%p===0;n/=p)w+=p-1;return w;};
const h0=Array.from({length:4480},(_,i)=>i+1).filter(h=>weight(h/gcd(h,35))<=7);
const eligible=h0.filter(h=>h>=9&&h!==10);
const fixed=[[2,1],[3,1],[4,2]];
const rows=[0,1,2,3,5];
const bits=(mask,arr)=>arr.filter((_,i)=>(mask>>i)&1);
const assert=(test,message)=>{if(!test)throw Error(message);};
const surviving=new Map;
const branches=[];
for(let f=0;f<8;f++)for(let r=0;r<32;r++){
  const F=bits(f,fixed), R=bits(r,rows);
  const k=8-F.length-R.length;
  if(k<1)continue;
  const L=F.reduce((n,[m])=>lcm(n,m),35);
  const D=Array.from({length:L},(_,i)=>i).filter(x=>B.includes(x%35)&&!R.includes(x%7)&&!F.some(([m,b])=>x%m===b));
  if(D.length===0)continue;
  const candidate=new Map;
  for(const h of eligible){
    const g=gcd(h,L),m=h/g;
    if(weight(m)>k-1)continue;
    const incidence=Array(g).fill(0);
    for(const x of D)incidence[x%g]++;
    assert(1814400%m===0,'mass scale');
    const mass=Math.max(...incidence)*(1814400/m);
    if(mass)candidate.set(h,mass);
  }
  const best=Math.max(0,...candidate.values()), survivors=[];
  for(const [h,mass] of candidate){
    
    let m=h/gcd(h,L), cap=mass+(k-1-weight(m))*best;
    for(let p=2;p<=m;p++){
      for(let power=p;m%p===0;power*=p,m/=p){
        const constrained=Math.max(0,...Array.from(candidate).filter(([v])=>v/gcd(v,L)%power===0).map(([,value])=>value));
        cap+=(p-1)*constrained;
      }
    }
    if(cap<D.length*1814400)continue;
    survivors.push(h);
    if(!surviving.has(h))surviving.set(h,[]);
    surviving.get(h).push({F,R,k,L});
  }
  branches.push({F,R,k,L,remain:D.length,survivors});
}


function enumerate(reverse){
const all=[];
let branchCount=0, visited=0, shapesCount=0, maxL=0;
for(const {F,R,k,L,survivors} of (reverse ? branches.slice().reverse() : branches)){
  if(!survivors.length)continue;
  if(branchIndex!==null&&branches.findIndex(x=>x.F===F&&x.R===R)!==branchIndex)continue;
  branchCount++;
  const P=survivors.reduce(lcm,L);
  maxL=Math.max(maxL,P);
  const D=Array.from({length:P},(_,x)=>x).filter(x=>B.includes(x%35)&&!R.includes(x%7)&&!F.some(([m,b])=>x%m===b));
  const n=D.length, full=(1n<<BigInt(n))-1n;
  const bit=Array.from({length:n},(_,i)=>1n<<BigInt(i));
  const options=(reverse ? survivors.slice().reverse() : survivors).flatMap(h=>{
    const set=Array(h).fill(0n);
    for(let i=0;i<n;i++)set[D[i]%h]|=bit[i];
    return set.flatMap((mask,b)=>mask?[{h,b,mask}]:[]);
  });
  const keys=new Map(options.map(({h,b},i)=>[h+':'+b,i]));
  const at=D.map(x=>(reverse?survivors.slice().reverse():survivors).map(h=>keys.get(h+':'+(x%h))));
  const priority=bit.map((b,i)=>i).sort((i,j)=>at[i].length-at[j].length || (reverse ? j-i : i-j));
  const chosen=[], blocked=new Uint8Array(options.length);
  const dfs=now=>{
    visited++;
    if(now===full){
      if(chosen.some(i=>{let covered=0n;for(const j of chosen)if(j!==i)covered|=options[j].mask;return (options[i].mask&~covered)===0n;}))return;
      all.push({F,R,classes:chosen.map(j=>[options[j].h,options[j].b])}); shapesCount++; return;
    }
    if(chosen.length===k)return;
    const pivot=priority.find(i=>!(now&bit[i]));
    const used=[];
    for(const j of at[pivot]){
      if(blocked[j])continue;
      chosen.push(j);
      dfs(now|options[j].mask);
      chosen.pop();
      blocked[j]=1;
      used.push(j);
    }
    for(const j of used)blocked[j]=0;
  };
  dfs(0n);
  if(branchCount%24===0)console.error({reverse,branchCount,visited,shapesCount,P});
}
if(branchIndex===null)all.push({F:[],R:rows,classes:[]});
const assignments=new Map;
for(const {F,R,classes} of all){
 const a=[...R.map(b=>[7,b]),...classes].sort(([h,b],[j,c])=>h-j||b-c).map(([h,b])=>h+":"+b);
 assignments.set(a.join(","),a);
}
const order=[...assignments.values()].sort((a,b)=>a.length-b.length);
const minimal=[];
for(const a of order)if(!minimal.some(b=>b.every(x=>a.includes(x)))) minimal.push(a);

return {branchCount,visited,shapesCount,maxL, unique: order.length, minimal};
}
const one=typeof process!=="undefined"&&process.argv[2];
const branchIndex=one===false||one===undefined?null:Number(one);
if (branchIndex!==null) assert(Number.isInteger(branchIndex)&&branchIndex>=0&&branchIndex<branches.length,"branch number (0.."+(branches.length-1)+")");
const normal=enumerate(false), reverse=enumerate(true);
const canonical=sets=>JSON.stringify(sets.map(s=>s.join(',')).sort());
assert(canonical(normal.minimal)===canonical(reverse.minimal),'search orders disagree');



const output={forward:{...normal,minimal:undefined},reverse:{...reverse,minimal:undefined},templates:normal.minimal,groups:[...new Set(normal.minimal.flat().map(s=>+s.split(':')[0]))].sort((a,b)=>a-b)}; console.log(JSON.stringify(output));

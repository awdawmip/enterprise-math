
const fixedPrimes = ["5","7","11","13","17","19","31","37","41","61","71","73","97","109","113","127","151","181","241","257","281","331","337","433","577","631","641","673","1321","14449","23311","29191","38737","54001","65537","87211","246241","262657","279073","6700417","18837001","29247661","487824887233","29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);
const B=[0,3,5,8,10,15,21,23,26,28,30,31,33];
const gcd=(a,b)=>b?gcd(b,a%b):a;
const lcm=(a,b)=>a/gcd(a,b)*b;
const weight=n=>{let w=0;for(let p=2;p<=n;p++)for(;n%p===0;n/=p)w+=p-1;return w;};
const h0=Array.from({length:2240},(_,i)=>i+1).filter(h=>weight(h/gcd(h,35))<=6);
const eligible=h0.filter(h=>h>=9&&h!==10);
const fixed=[[2,1],[3,1],[4,2]];
const rows=[0,1,2,3,5];
const bits=(mask,arr)=>arr.filter((_,i)=>(mask>>i)&1);
const assert=(test,message)=>{if(!test)throw Error(message);};
const surviving=new Map;
const branches=[];
for(let f=0;f<8;f++)for(let r=0;r<32;r++){
  const F=bits(f,fixed), R=bits(r,rows);
  const k=7-F.length-R.length;
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
    assert(60480%m===0,'mass scale');
    const mass=Math.max(...incidence)*(60480/m);
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
    if(cap<D.length*60480)continue;
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
  const at=bit.map(b=>options.flatMap((o,i)=>(o.mask&b)?[i]:[]));
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
}
all.push({F:[],R:rows,classes:[]});
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
const normal=enumerate(false), reverse=enumerate(true);
const canonical=sets=>JSON.stringify(sets.map(s=>s.join(',')).sort());
assert(canonical(normal.minimal)===canonical(reverse.minimal),'search orders disagree');


const groups=[7,9,12,14,15,16,18,20,21,24,28,30,32,35,36,40,48,60,70,80,140];
const expectedOrders={"7":[63,126,252],"9":[81,162,324],"12":[432],"14":[504],"15":[135,270,540],"16":[192,576],"18":[648],"20":[80,240,720],"21":[189,378,756],"24":[864],"28":[112,336,1008],"30":[1080],"32":[128,384,1152],"35":[315,630,1260],"36":[1296],"40":[160,480,1440],"48":[1728],"60":[2160],"70":[280,840,2520],"80":[320,960,2880],"140":[560,1680,5040]};
const lowerCaps={"7":5,"9":3,"12":3,"14":5,"15":3,"16":5,"18":1,"20":5,"21":3,"24":2,"28":3,"30":1,"32":3,"35":10,"36":1,"40":8,"48":1,"60":1,"70":3,"80":3,"140":3};
const knownRealization={"7":["7:0","14:10","14:12","20:0","20:8"],"9":["9:0","12:8","18:12","36:24"],"12":["12:0","12:8"],"14":["14:0","14:10","14:12","20:0","20:8"],"15":["12:0","15:11","20:0","20:8"],"16":["12:0","16:0","16:8","24:20"],"18":["9:0","12:8","18:12","36:24"],"20":["20:0","20:8","20:16"],"21":["7:0","7:1","7:2","7:3","21:5","21:12"],"24":["12:0","24:8","24:20"],"28":["14:0","14:10","14:12","28:8","28:16"],"30":["12:0","15:11","20:0","30:8"],"32":["16:0","16:4","16:12","32:8","32:24"],"35":["14:0","14:10","20:0","20:8","35:26"],"36":["9:0","12:8","18:12","36:24"],"40":["20:0","20:16","40:8","40:28"],"48":["12:0","16:0","24:20","48:8"],"60":["12:0","15:11","20:0","60:8"],"70":["14:0","14:10","20:0","20:8","70:26"],"80":["16:0","20:0","20:16","40:28","80:8"],"140":["14:0","14:10","20:0","20:8","140:96"]};
const A4=427862534250255874142059986311712045208460862156242374709749146714880029585009065541265479726658295808843521086362454718047435496681465110551998259577542161622793500228931578210883591253490428068977896911616949921393222257268332228484808322449966505904395308464777304242195893590213416972267332840402564470159978966396652296385533697227114107008635433673n,S4=555913265364989619697873741372709588670986629522837781333836453228687923187421391074561543226863273773190894562567333918792362053445593573850052370953876739565216134323755512367030826851461448887445240358521194430339039575739758436657254293728498346839912662754165409451691836095700927934351172974265672180517614278948584699085275521666505271546605819230n;
const bigGcd=(a,b)=>b?bigGcd(b,a%b):a;
function remove(n, bad){
 let common;
 while((common=bigGcd(n,bad))>1n)n/=common;
 return n;
}
function divisors(n){
 return Array.from({length:n},(_,i)=>i+1).filter(p=>n%p===0);
}
function trialPrime(n){
 if(n<2)return false;
 for(let p=2;p*p<=n;p++)if(n%p===0)return false;
 return true;
}
function primitive(d){
 let value=(1n<<BigInt(d))-1n;
 for(const p of divisors(d).filter(trialPrime))value=remove(value,(1n<<BigInt(d/p))-1n);
 for(const q of fixedPrimes)value=remove(value,q);
 return value;
}
function powmod(a,e,q){
 let m=BigInt(e),v=1n;
 for(;m;m>>=1n,a=a*a%q)if(m&1n)v=v*a%q;
 return v;
}

function inverse(a,m){
 let x=1n,y=0n,u=(a%m+m)%m,v=m;
 while(v){const d=u/v;[u,v]=[v,u-d*v];[x,y]=[y,x-d*y];}
 assert(u===1n,'inverse');return (x%m+m)%m;
}
function crt(a,m,b,n){
 if(n===1n)return [a,m];
 return [a+m*((((b-a)%n+n)%n)*inverse(m,n)%n),m*n];
}
function rootCat(w,n){return powmod(inverse(2n,n),16+18*w,n)}

const lines=Object.fromEntries(groups.map(h=>[h,divisors(36).map(g=>h*g).filter(d=>d/gcd(d,36)===h).map(d=>[d,primitive(d)]).filter(([,n])=>n>1n)]));
assert(JSON.stringify(Object.fromEntries(groups.map(h=>[h,lines[h].map(([d])=>d)])))===JSON.stringify(expectedOrders),'order group');
const C=Object.fromEntries(groups.map(h=>[h,lines[h].reduce((z,[d,m])=>z*m,1n)]));
for(const [h,picks] of Object.entries(knownRealization)){
 assert(normal.minimal.some(t=>t.join(',')===picks.join(',')),'necessary period has term');
 assert(picks.some(s=>s.startsWith(h+':')),'term includes claimed period');
 for(const k of groups)assert(picks.filter(s=>s.startsWith(k+':')).length<=lowerCaps[k],'realizable inventory');
}
const C5040=lines[140].find(([d])=>d===5040)[1];
const C1120=primitive(1120),C3360=primitive(3360);
assert(C1120>1n&&C3360>1n&&bigGcd(C1120,C3360)===1n,'higher carriers nonempty disjoint');
const picked=[[14,0,1009n],[14,10,21169n],[20,0,4278255361n],[20,8,394783681n],[140,96,C5040]];
const Csum=Object.values(C).reduce((a,b)=>a*b,1n);
const mask=picked.reduce((n,[h,b,q])=>remove(n,q),Csum);
let [a,z]=crt(A4,S4,0n,mask);
for(const [h,b,q] of picked.slice(0,-1))[a,z]=crt(a,z,rootCat(b,q),q);
for(const [w,n] of [[96,C1120],[236,C3360]])[a,z]=crt(a,z,rootCat(w,n),n);
const [on,common]=crt(a,z,rootCat(96,C5040),C5040);
const [off]=crt(a,z,0n,C5040);
const ao=on+common, af=off+common;
assert(ao%S4===A4&&af%S4===A4&&(ao-af)%z===0n,'exact R4 CRT common coordinates');
function slot(a,h,b){const n=C[h];return bigGcd(n,(a%n)**2n*powmod(2n,32+36*b,n)-1n)>1n}
function le11(a){return normal.minimal.some(t=>t.every(x=>slot(a,...x.split(':').map(Number))))}
const e10=[["12:0","12:8"],["20:0","20:8","20:16"],["12:0","24:8","24:20"],["12:8","24:0","24:12"],["16:0","16:4","16:8","16:12"],["20:0","20:8","40:16","40:36"],["20:0","20:16","40:8","40:28"],["20:8","20:16","40:0","40:20"],["14:0","14:2","14:8","14:10","14:12"],["7:0","14:2","14:8","14:10","14:12"],["7:1","14:0","14:2","14:10","14:12"],["7:0","7:1","14:2","14:10","14:12"],["7:2","14:0","14:8","14:10","14:12"],["7:0","7:2","14:8","14:10","14:12"],["7:1","7:2","14:0","14:10","14:12"],["7:0","7:1","7:2","14:10","14:12"],["7:3","14:0","14:2","14:8","14:12"],["7:0","7:3","14:2","14:8","14:12"],["7:1","7:3","14:0","14:2","14:12"],["7:0","7:1","7:3","14:2","14:12"],["7:2","7:3","14:0","14:8","14:12"],["7:0","7:2","7:3","14:8","14:12"],["7:1","7:2","7:3","14:0","14:12"],["7:0","7:1","7:2","7:3","14:12"],["7:5","14:0","14:2","14:8","14:10"],["7:0","7:5","14:2","14:8","14:10"],["7:1","7:5","14:0","14:2","14:10"],["7:0","7:1","7:5","14:2","14:10"],["7:2","7:5","14:0","14:8","14:10"],["7:0","7:2","7:5","14:8","14:10"],["7:1","7:2","7:5","14:0","14:10"],["7:0","7:1","7:2","7:5","14:10"],["7:3","7:5","14:0","14:2","14:8"],["7:0","7:3","7:5","14:2","14:8"],["7:1","7:3","7:5","14:0","14:2"],["7:0","7:1","7:3","7:5","14:2"],["7:2","7:3","7:5","14:0","14:8"],["7:0","7:2","7:3","7:5","14:8"],["7:1","7:2","7:3","7:5","14:0"],["7:0","7:1","7:2","7:3","7:5"],["7:0","7:1","7:3","7:5","35:23","35:30"],["7:0","7:2","7:3","7:5","35:8","35:15"]];
function le10(a){return e10.some(t=>t.every(x=>slot(a,...x.split(':').map(Number))))}
assert(le11(ao)&&!le10(ao)&&!le11(af),'root exact budget bounds');
function missing(ch){
  const L=ch.reduce((x,[h])=>lcm(x,h),35);
  return Array.from({length:L},(_,i)=>i).filter(w=>B.includes(w%35)&&!ch.some(([h,b])=>w%h===b));
}
const base=[[2,1],[4,2],...picked.slice(0,-1).map(([h,b])=>[h,b])];
assert(missing([...base,[140,96]]).length===0&&missing([...base,[280,96],[280,236]]).length===0,'two complete local covers');
const result={forward:{...normal,minimal:undefined},reverse:{...reverse,minimal:undefined},templates:normal.minimal,orderGroups:expectedOrders,
  minimumSupportCarrier:groups.map(h=>[h,String(C[h])]),availabilityWitnesses:knownRealization,
  roots:{on:ao.toString(16),off:af.toString(16),sharedModulus:z.toString(16),topCarrier:C5040.toString(16),higherRepairCarriers:[C1120,C3360].map(String),onCost:11,offCost:12}};
if(typeof text==='function')text(result);else console.log(JSON.stringify(result,null,2));


const fixedPrimes = ["5","7","11","13","17","19","31","37","41","61","71","73","97","109","113","127","151","181","241","257","281","331","337","433","577","631","641","673","1321","14449","23311","29191","38737","54001","65537","87211","246241","262657","279073","6700417","18837001","29247661","487824887233","29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);
const B=[0,3,5,8,10,15,21,23,26,28,30,31,33];
const gcd=(a,b)=>b?gcd(b,a%b):a;
const lcm=(a,b)=>a/gcd(a,b)*b;
const weight=n=>{let w=0;for(let p=2;p<=n;p++)for(;n%p===0;n/=p)w+=p-1;return w;};
const h0=Array.from({length:1120},(_,i)=>i+1).filter(h=>weight(h/gcd(h,35))<=5);
const eligible=h0.filter(h=>h>=9&&h!==10);
const fixed=[[2,1],[3,1],[4,2]];
const rows=[0,1,2,3,5];
const bits=(mask,arr)=>arr.filter((_,i)=>(mask>>i)&1);
const assert=(test,message)=>{if(!test)throw Error(message);};
const surviving=new Map;
const branches=[];
for(let f=0;f<8;f++)for(let r=0;r<32;r++){
  const F=bits(f,fixed), R=bits(r,rows);
  const k=6-F.length-R.length;
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
    assert(1440%m===0,'mass scale');
    const mass=Math.max(...incidence)*(1440/m);
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
    if(cap<D.length*1440)continue;
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
const compact=[
 ['12:0','12:8'],
 ['20:0','20:8','20:16'],
 ['12:0','24:8','24:20'],
 ['12:8','24:0','24:12'],
 ['16:0','16:4','16:8','16:12'],
 ['20:0','20:8','40:16','40:36'],
 ['20:0','20:16','40:8','40:28'],
 ['20:8','20:16','40:0','40:20'],
 ['7:0','7:1','7:3','7:5','35:23','35:30'],
 ['7:0','7:2','7:3','7:5','35:8','35:15']
];
for(let mask=0;mask<32;mask++){
 const assignment=rows.map((b,i)=>mask>>i&1?'14:'+(b+(b%2)*7):'7:'+b);
 compact.push(assignment.sort((a,b)=>{
   const [h,x]=a.split(':').map(Number),[j,y]=b.split(':').map(Number);
   return h-j||x-y;
 }));
}
assert(canonical(normal.minimal)===canonical(compact),'compact formula disagrees');
assert(normal.minimal.length===42,'template count');
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
const periods=[7,12,14,16,20,24,35,40];
const inventory=Object.fromEntries(periods.map(h=>[h,divisors(36).map(g=>h*g).filter(d=>d/gcd(d,36)===h).map(d=>[d,primitive(d)]).filter(([,n])=>n>1n)]));
assert(new Set(fixedPrimes).size===74,'fixed fiber');
const order1440=inventory[40].find(([d])=>d===1440)[1];
for(const q of [37441,170251201]){
 assert(trialPrime(q),'order 1440 prime');
 assert(order1440%BigInt(q)===0n,'order 1440 carrier');
 assert(powmod(2n,1440,BigInt(q))===1n&&[2,3,5].every(p=>powmod(2n,1440/p,BigInt(q))!==1n),'order 1440 check');
}
const c576=primitive(576), c192=primitive(192);
const first=3457n,second=816769n;
assert(trialPrime(Number(first))&&trialPrime(Number(second))&&c576%(first*second)===0n,'order 576 primes');
assert(remove(remove(c576,first),second)>1n&&c192>1n,'four distinct period 16 primes');
const witness=[[20,0],[20,8],[40,36],[40,16]];
const higher=[[80,16],[80,56]];
function missing(cover){
 const all=[...fixed,...cover];
 const period=all.reduce((acc,[h])=>lcm(acc,h),35);
 return Array.from({length:period},(_,w)=>w).filter(w=>B.includes(w%35)&&!all.some(([h,b])=>w%h===b));
}
assert(missing(witness).length===0,'true witness');
assert(missing(witness.slice(0,-1)).length>0,'false witness');
assert(missing(witness.slice(0,-1).concat(higher)).length===0,'finite 11-cover');
const chosen=witness.slice(0,-1).map(([h,b])=>h+':'+b);
assert(!normal.minimal.some(a=>a.every(x=>chosen.includes(x))),'false exact cost');
const result={
 forward:{...normal,minimal:undefined},
 reverse:{...reverse,minimal:undefined},
 templates:normal.minimal,
 orders:Object.fromEntries(periods.map(h=>[h,inventory[h].map(([d])=>d)])),
 carrierDecimalDigits:Object.fromEntries(periods.map(h=>[h,(''+inventory[h].reduce((n,[,c])=>n*c,1n)).length])),
 lowerWitness:{period40Primes:[37441,170251201],period20Primes:[4278255361,394783681],falseMissingCount:missing(witness.slice(0,-1)).length}
};

const A4=427862534250255874142059986311712045208460862156242374709749146714880029585009065541265479726658295808843521086362454718047435496681465110551998259577542161622793500228931578210883591253490428068977896911616949921393222257268332228484808322449966505904395308464777304242195893590213416972267332840402564470159978966396652296385533697227114107008635433673n,S4=555913265364989619697873741372709588670986629522837781333836453228687923187421391074561543226863273773190894562567333918792362053445593573850052370953876739565216134323755512367030826851461448887445240358521194430339039575739758436657254293728498346839912662754165409451691836095700927934351172974265672180517614278948584699085275521666505271546605819230n;
assert(fixedPrimes.every(q=>S4%q===0n),'fixed modulus');
const C=Object.fromEntries(periods.map(h=>[h,inventory[h].reduce((v,[,n])=>v*n,1n)]));
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
const Lhi=[320,2880].map(primitive);
assert(Lhi.every(n=>n>1n),'nonempty high repair carriers');
const cut=[4278255361n,394783681n,170251201n,37441n];
const slots=[0,8,36,16];
const allC=Object.values(C).reduce((a,b)=>a*b,1n);
const inactive=cut.reduce((n,q)=>remove(n,q),allC);
let [v,m]=crt(A4,S4,0n,inactive);
for(let j=0;j<3;j++)[v,m]=crt(v,m,rootCat(slots[j],cut[j]),cut[j]);
for(let j=0;j<2;j++)[v,m]=crt(v,m,rootCat([16,56][j],Lhi[j]),Lhi[j]);
const [on,fullM]=crt(v,m,rootCat(16,cut[3]),cut[3]);const [off]=crt(v,m,0n,cut[3]);
const rOn=on+fullM,rOff=off+fullM;
assert((rOn-rOff)%m===0n&&rOn%S4===A4&&rOff%S4===A4,'same underlying coordinates except target');
function slot(a,h,w){let n=C[h];return bigGcd(n,(a%n)**2n*powmod(2n,32+36*w,n)-1n)>1n}
function le10(a){return compact.some(t=>t.every(x=>slot(a,...x.split(':').map(Number))))}
assert(le10(rOn)&&!le10(rOff),'explicit root toggle');
assert(![ [7,[0,1,2,3,5]],[12,[0,8]],[20,[0,8,16]] ].some(([h,bs])=>bs.every(w=>slot(rOn,h,w))),'on misses ninth budget');
const A9=[...fixed,...witness.slice(0,-1),...higher];
assert(missing(A9.slice(fixed.length)).length===0,'off repair');
result.explicitPair={onHex:rOn.toString(16),offHex:rOff.toString(16),sharedModulusHex:m.toString(16),fullModulusHex:fullM.toString(16),higherRepairCarrierHex:Lhi.map(a=>a.toString(16)),verified:{onCost:10,offCost:11}};

if(typeof text==='function')text(result);else console.log(JSON.stringify(result,null,2));

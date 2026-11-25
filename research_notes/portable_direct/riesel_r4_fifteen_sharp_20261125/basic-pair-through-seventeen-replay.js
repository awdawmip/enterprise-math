
const fixedPrimes = ["5","7","11","13","17","19","31","37","41","61","71","73","97","109","113","127","151","181","241","257","281","331","337","433","577","631","641","673","1321","14449","23311","29191","38737","54001","65537","87211","246241","262657","279073","6700417","18837001","29247661","487824887233","29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);

const B=[0,3,5,8,10,15,21,23,26,28,30,31,33];
const gcd=(a,b)=>b?gcd(b,a%b):a;
const lcm=(a,b)=>a/gcd(a,b)*b;
const assert=(test,key)=>{if(!test)throw Error(key);};
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



const P=[7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417].map(BigInt);
const fixedExtra=[5,13,19,73,38737,246241,487824887233].map(BigInt);
assert(fixedPrimes.every(q=>P.includes(q)||fixedExtra.includes(q)||A4%q===0n),'all other fixed coordinates inactive');


const H=[0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100];
const extras=[[4,9,19],[1,9,73],[34,36,38737],[34,54,246241],[52,72,487824887233]];
const origin=BigInt(A4);
for(const [b,d,q] of extras)assert(powmod(2n,2*b,BigInt(q))*(origin%BigInt(q))**2n%BigInt(q)===1n,'fixed phase');
const small={11:[23,89],13:[8191],17:[131071],22:[683],25:[601,1801],26:[2731],33:[599479],34:[43691],39:[79,121369],44:[397,2113],50:[251,4051],52:[53,157,1613],66:[67,20857],78:[22366891],80:[4278255361],88:[353,2931542417],132:[312709,4327489]};
for(const [d,arr] of Object.entries(small))assert(primitive(+d)===arr.reduce((p,q)=>p*BigInt(q),1n)&&arr.every(trialPrime),'counted order '+d);
function rows(h,s){return divisors(s).map(g=>g*h).filter(d=>d/gcd(d,s)===h);}
function checkSpecial(h,s,count){
 assert(rows(h,s).every(d=>small[d])&&rows(h,s).flatMap(d=>small[d]).length===count,'inventory of '+s+','+h);
}
for(const [step,inventory] of [[2,[[11,3],[13,2],[33,3],[17,2],[25,4],[39,3]]],[4,[[11,5],[13,5],[20,1],[33,5],[22,2]]]])for(const [h,n] of inventory)checkSpecial(h,step,n);
const periodScale=Array.from({length:31},(_,i)=>BigInt(i+1)).reduce((a,b)=>a*b/bigGcd(a,b),1n);
const cache=new Map;
function hasFree(h,step){
 if(h>150)return true;
 const k=h+','+step;
 if(!cache.has(k))cache.set(k,rows(h,step).some(d=>remove(primitive(d),3n)>1n));
 return cache.get(k);
}
function flags(h){return Number(h%11===0)+2*Number(h%13===0);}
function capacity(D,L,step,omit){
 const generic=Array(4).fill(BigInt(D.length)*periodScale/31n),special=new Map(), low33=[0n,0n,0n];
 for(const g of divisors(L)){
  const K=new Int32Array(g);for(const x of D)K[x%g]++;
  const biggest=Math.max(...K);
  for(let m=1;m<=30;m++){
   const h=g*m;
   if(gcd(h,L)!==g||h===11||h===13||!hasFree(h,step))continue;
   const value=BigInt(biggest)*periodScale/BigInt(m);
   if(omit.has(h))special.set(h,value);
   else if(generic[flags(h)]<value)generic[flags(h)]=value;
  }
 }
 return {generic,special};
}
const frac=(n,d)=>{const a=bigGcd(n,d);return [n/a,d/a];};
const bigger=(a,b)=>a[0]*b[1]>b[0]*a[1];
const mulFlags=(j,k)=>[BigInt((11-j)*(13-k)),BigInt(11*(13-k)),BigInt(13*(11-j)),143n];
const minimum=cap=>cap.reduce((a,b)=>a>b?a:b,0n);
function runBudget(budget,step,parity){
 const u=z=>step===2?z:parity+2*z;
 const fixed=extras.filter(([a,d])=>step===2||d%2||a%2===parity).map(([a,d,q])=>{
  if(step===2)return [a,d,q];
  const m=d/gcd(d,2);
  const b=Array.from({length:m},(_,z)=>z).find(z=>u(z)%d===a);
  return [b,m,q];
 });
 const extrasForStep=step===2?[[33,3],[17,2],[25,4],[39,3]]:[[20,1],[33,5],[22,2]];
 const omit=new Set(extrasForStep.map(([h])=>h));
 let worst=[0n,1n],witness,leaves=0;
 const trouble=[];
 for(let s=0;s<1<<fixed.length;s++){
  const selected=fixed.filter((_,i)=>s>>i&1);
  const L=selected.reduce((l,[b,d])=>lcm(l,d),105);
  const D=Array.from({length:L},(_,z)=>z).filter(z=>H.includes(u(z)%105)&&!selected.some(([b,d])=>z%d===b));
  const {generic,special}=capacity(D,L,step,omit);
  for(let j=0;j<=(step===2?3:5);j++)for(let k=0;k<=(step===2?2:5);k++){
   const factors=mulFlags(j,k);
   const max=minimum(generic.map((c,i)=>c*factors[i]));
   const total=BigInt(D.length)*periodScale*factors[0];
   function branches(i,left,used,mass){
    if(i<extrasForStep.length){
      const [h,maxN]=extrasForStep[i],c=(special.get(h)??0n)*factors[flags(h)];
      for(let q=0;q<=maxN&&q<=left;q++)branches(i+1,left-q,used.concat(q),mass+BigInt(q)*c);
      return;
    }
    const cap=mass+BigInt(left)*max, result=frac(cap,total);
    leaves++;
    if(bigger(result,worst)){worst=result;witness={selected:selected.map(t=>t[2]),j,k,used};}
    if(cap<total)return;
    assert(budget===17&&step===4,'only 17 single-missing branches withstand main test');
    const idx33=extrasForStep.findIndex(r=>r[0]===33), num33=used[idx33];
    assert(num33>0,'33 is selected');
    const central=D.filter(z=>u(z)%3===0), side=D.filter(z=>u(z)%3!==0);
    const g=gcd(33,L),m=33/g;
    const classMass=Array(g).fill(0);
    for(const x of D)classMass[x%g]++;
    const sideClass=Math.max(...classMass.filter((_,b)=>u(b)%3!==0));
    const alternative=BigInt(sideClass)*periodScale/BigInt(m);
    const drop=(special.get(33)-alternative)*factors[flags(33)];
    assert(cap-drop<total,'all period-33 choices must be central');
    const rest=capacity(side,L,step,omit);
    const need=BigInt(side.length)*periodScale*factors[0];
    const other=extrasForStep.reduce((acc,[h],a)=>h===33?acc:acc+BigInt(used[a])*(rest.special.get(h)??0n)*factors[flags(h)],0n);
    const bound=other+BigInt(left)*minimum(rest.generic.map((x,g)=>x*factors[g]));
    assert(bound<need,'peripheral residue impossible even if central full');
    trouble.push({selected:selected.map(x=>x[2]),j,k,used,left,global:frac(cap,total).map(String),sideMass:frac(bound,need).map(String)});
   }
   branches(0,budget-Number(step===4)-selected.length-j-k,[],0n);
  }
 }
 return {budget,step,parity,worst:worst.map(String),witness,leaves,trouble};
}
const proof=[15,16,17].flatMap(b=>[runBudget(b,2,0),runBudget(b,4,0),runBudget(b,4,1)]);

console.log(JSON.stringify(proof,null,2));

const assert=(v,m)=>{if(!v)throw Error(m);};
const fixedPrimes = ["5","7","11","13","17","19","31","37","41","61","71","73","97","109","113","127","151","181","241","257","281","331","337","433","577","631","641","673","1321","14449","23311","29191","38737","54001","65537","87211","246241","262657","279073","6700417","18837001","29247661","487824887233","29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);

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



const fs=require('node:fs'),data=require('./enumeration-cpp.json'), prior=require('./known-factors.json');
const known={};
for(const [d,factors] of Object.entries(prior))known[d]=factors.map(BigInt);
for(const [d,q] of [[1120,16824641n],[6720,16141441n],[10080,20161n]])(known[d]??=[]).push(q);
const orders={},availability={},witnesses={},maxima={};
for(const h of data.groups){
 const layers=data.orders[h].map(d=>[d,primitive(d)]).filter(x=>x[1]>1n);
 const lower=layers.reduce((a,[d,m])=>{
  let q=(known[d]??[]).filter(z=>m%z===0n);
  return a+q.length+Number(q.reduce((n,p)=>remove(n,p),m)>1n);
 },0);
 orders[h]=layers.map(([d,n])=>[d,n.toString()]);
 availability[h]=lower;
}
for(const h of data.groups){
 const f=data.templates.filter(t=>t.some(s=>s.startsWith(h+':')));
 maxima[h]=Math.max(...f.map(t=>t.filter(s=>s.startsWith(h+':')).length));
 const w=f.find(t=>data.groups.every(g=>t.filter(s=>s.startsWith(g+':')).length<=availability[g]));
 assert(w,'no proved realizable template for '+h);
 witnesses[h]=w;
}
const max=Math.max(...Object.values(orders).flat().map(a=>a[0]));
assert(max===10080,'top order');
const {templates,...shape}=data;
const summary={...shape,orderCount:Object.values(orders).flat().length, max, orders,availability,maxima,witnesses};
fs.writeFileSync('observer.json',JSON.stringify(summary,null,2)+'\n');
for(let i=0;i<templates.length;i+=800)fs.writeFileSync('templates-'+String(i/800).padStart(2,'0')+'.json',JSON.stringify(templates.slice(i,i+800))+'\n');
console.log({max,availability,maxima,orderCount:summary.orderCount});

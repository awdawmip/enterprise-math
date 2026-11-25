
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

const shared=[
 [9,44,397n],[4,33,599479n],
 [1,11,23n],[2,11,89n],[3,22,683n],[5,44,2113n],
 [6,66,67n],[7,66,20857n],[8,132,312709n],[10,132,4327489n],
 [0,88,353n],[11,88,2931542417n]
];
const cat=(b,q)=>powmod(inverse(2n,q),4+6*b,q);
const vPeriod=d=>d/gcd(d,12);
for(const [b,d,q] of shared){
 assert(trialPrime(Number(q))&&primitive(d)%q===0n,'prime exact order '+q);
 assert(vPeriod(d)===(b%11===0?22:11),'effective period');
}
assert(new Set(shared.map(x=>x[2])).size===12,'twelve distinct free primes');
const bank=shared.map(([b,d,q])=>({q,d,b:(8+12*b)%d}));
function exactOrder(q){
 let r=2n,d=1;
 while(r!==1n){r=r*2n%q;d++;}
 return d;
}
const original=[...P,...fixedExtra].map(q=>{
 const d=exactOrder(q);
 let r=(A4%q)**2n%q, b=-1;
 for(let n=0;n<d;n++,r=r*2n%q)if(r===1n){b=n;break;}
 return {q,d,b};
});
const entirety=[...original,...bank];
for(const [q,n] of [[5n,6],[13n,12]]){
 const hits=entirety.filter(x=>n%x.d===x.b).map(x=>x.q);
 assert(hits.length===1&&hits[0]===q,'private basic prime at '+n);
}
const cover=[...original.filter(x=>P.includes(x.q)||[5n,13n].includes(x.q)),...bank];
const period=cover.map(x=>x.d).reduce(lcm);
for(let n=1;n<=period;n++)assert(cover.some(x=>n%x.d===x.b),'global cover at '+n);
const A=[1,2,10,11,12,16,17,22,25,26,30,31,32];
const fixedV=[[5,6,38737n],[5,9,246241n],[8,12,487824887233n]];
const L=Array.from({length:lcm(lcm(35,22),36)},(_,v)=>v).filter(v=>A.includes(v%35));
const witnesses=[];
for(const z of [0,1]){
 for(const [b,d,q] of shared){
  const hit=v=>v%vPeriod(d)===b;
  const v=L.find(v=>v%3===z&&hit(v)&&!shared.some(([bb,dd,qq])=>qq!==q&&v%vPeriod(dd)===bb)&&!fixedV.some(([r,h])=>v%h===r));
  assert(v!==undefined,'each shared class private in free phase '+z);
  witnesses.push([z,String(q),v]);
 }
}
const third=[];
for(const [b,d,q] of shared.filter(([b,d])=>vPeriod(d)===11||b%2===0)){
 const v=L.find(v=>v%3===2&&v%vPeriod(d)===b&&!fixedV.some(([r,h])=>v%h===r));
 assert(v!==undefined,'third phase mandatory '+q);
 third.push([String(q),v]);
}
assert(third.length===11,'third phase needs eleven named shared channels');
const odd=L.find(v=>v%3===2&&v%22===11&&v%9!==5&&v%12!==8);
assert(odd!==undefined&&odd%6===5,'last third phase requires either 38737 or odd period-22 class');

const sharedPool=[...shared.slice(0,10),...[[353,88],[2931542417,88],[7393,264],[1761345169,264],[98618273953,264]].map(([q,d])=>[0,d,BigInt(q)])];
const tests=[];
for(const [phase,d,q] of sharedPool){
 let set, target, spares;
 if(vPeriod(d)===11){
   set=shared;
   target=set.find(x=>x[2]===q);
   spares=[[phase,264,7393n],[phase+11,264,1761345169n]];
 } else {
   const alt=q===353n?2931542417n:353n;
   target=[0,d,q];
   set=[...shared.slice(0,10),target,[11,88,alt]];
   spares=[[0,176,229153n],[22,176,119782433n]];
 }
 for(const [b,d,p] of spares)assert(trialPrime(Number(p))&&primitive(d)%p===0n,'spare exact order');
 const groups=set.filter(x=>x!==target).concat(spares);
 assert(groups.length===13&&new Set(groups.map(x=>x[2])).size===13,'refined active carriers');
 for(const [basic,n] of [[5n,6],[13n,12]]){
   const fixedHits=original.filter(x=>n%x.d===x.b);
   assert(fixedHits.length===1&&fixedHits[0].q===basic,'fixed basic private');
   assert(!set.concat(spares).some(([b,d])=>n%d===(8+12*b)%d),'all free classes miss basic private position');
 }
 const matches=(v,[b,d])=>v%vPeriod(d)===b;
 const V=Array.from({length:27720},(_,v)=>v).filter(v=>A.includes(v%35));
 assert(V.every(v=>groups.filter(x=>matches(v,x)).length===1),'refinement partitions shared residual');
 const side=new Set(V.filter(v=>v%3===0).flatMap(v=>groups.filter(q=>matches(v,q)).map(x=>x[2])));
 const other=new Set(V.filter(v=>v%3===1).flatMap(v=>groups.filter(q=>matches(v,q)).map(x=>x[2])));
 assert(side.size===13&&other.size===13,'each W-free side needs all thirteen refined classes');
 const anchorFree=V.filter(v=>v%3===2&&!fixedV.some(([r,h])=>v%h===r));
 const third=new Set(anchorFree.flatMap(v=>groups.filter(q=>matches(v,q)).map(x=>x[2])));
 assert(third.size>=11,'even third phase alone rules out fourteen with both W');
 tests.push({q:String(q),d,spares:spares.map(([b,d,q])=>[b,d,String(q)]),privateThird:third.size});
}
const result={targets:tests,costPair:[14,15],period:27720};

console.log(JSON.stringify(result,null,2));

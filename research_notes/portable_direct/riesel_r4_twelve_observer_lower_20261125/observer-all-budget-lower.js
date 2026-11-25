
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
const low=[[1009n,0,504],[21169n,10,504],[4278255361n,0,80],[394783681n,8,240]];
function exactOrder(q){let x=2n,d=1;while(x!==1n){x=x*2n%q;d++;}return d;}
const descriptors=[...P,...fixedExtra].map(q=>{
 const d=exactOrder(q),a=A4%q;
 let s=a*a%q,b=-1;
 for(let n=0;n<d;n++){if(s===1n){b=n;break;}s=s*2n%q;}
 return {q,d,b};
});
for(const [q,w,d] of low){assert(exactOrder(q)===d,'exact low order');descriptors.push({q,d,b:(32+36*w)%d});}
const anchorPrimes=[5,13,19,73,38737,487824887233,1009,21169,4278255361,394783681].map(BigInt);
const period=descriptors.map(x=>x.d).reduce(lcm,560);
const privateWitness={};let residual=0;const highPrivate=[];
for(let n=1;n<=period;n++){
 const hits=descriptors.filter(x=>n%x.d===x.b);
 if(hits.length===1&&n%560!==3488%560&&!privateWitness[hits[0].q])privateWitness[hits[0].q]=n;
 if(!hits.length)residual++;
 if(!hits.length&&n%36===32&&((n-32)/36)%140===96)highPrivate.push(n);
}
assert(anchorPrimes.every(q=>privateWitness[q]),'all anchors private with the parent high progression as a possible competitor');
const anchors=Object.fromEntries(anchorPrimes.map(q=>[String(q),privateWitness[q]]));

const withoutR=descriptors.filter(x=>x.q!==246241n);
for(let n=1;n<=period;n++){
 const uncovered=!withoutR.some(({d,b})=>n%d===b);
 const anchorHole=n>=32&&n%36===32&&((n-32)/36)%140===96;
 assert(uncovered===anchorHole,'complete anchor hole progression at '+n);
}
for(let depth=0;depth<=12;depth++){
 const r=1<<depth;
 const leafPartition=[];
 for(let j=1;j<=depth;j++)leafPartition.push([1<<j,1<<(j-1)]);
 leafPartition.push([r,0]);
 for(let x=0;x<r;x++)assert(leafPartition.filter(([h,b])=>x%h===b).length===1,'dyadic partition');
 for(const [h,b] of leafPartition){
   const d=(b===0?36:4)*140*h;
   assert(d/gcd(d,36)===140*h&&d%560===0,'order and global anchor');
 }
 const off=leafPartition.filter(([,b])=>b!==0).concat([[2*r,0],[2*r,r]]);
 for(let x=0;x<2*r;x++)assert(off.filter(([h,b])=>x%h===b).length===1,'refined dyadic partition');
 for(const g of [4,12]){
  const d=g*280*r;
  assert(d/gcd(d,36)===280*r&&d%560===0,'common refinement orders');
 }
}
const report={checks:13,period,oldDictionaryPeriod:P.map(exactOrder).reduce(lcm),anchors,residual,highPrivate};

console.log(JSON.stringify(report,null,2));

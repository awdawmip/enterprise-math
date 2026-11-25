
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

const H=[0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100];
const old=descriptors.filter(s=>P.includes(s.q));
const oldPeriod=old.map(s=>s.d).reduce(lcm);
assert(oldPeriod===6720&&oldPeriod%210===0,'period divisibility');
for(let n=1;n<=oldPeriod;n++)assert(!old.some(({d,b})=>n%d===b)===(n%2===0&&H.includes((n/2)%105)),'period 210 of union complement at '+n);
const bound=64;
const states=Array.from({length:bound},()=>0n);states[0]=1n;
for(let p=2;p<=bound;p++)if(trialPrime(p)) for(let s=p-1;s<bound;s++)states[s]+=states[s-p+1];
const rows=[1,5,8,9,10,11,12,16,32,64].map(b=>({b,distinctM:states.slice(0,b).reduce((a,z)=>a+z).toString(),absoluteOrderUpper:(210n<<BigInt(b-1)).toString()}));
console.log(JSON.stringify({band:rows, oldPeriod, holePeriod:210,checks:oldPeriod}));

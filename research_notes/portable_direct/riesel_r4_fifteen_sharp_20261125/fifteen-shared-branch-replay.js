
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


const A=[1,2,10,11,12,16,17,22,25,26,30,31,32];
const columns=Array.from({length:5},(_,b)=>A.filter(x=>x%5===b));
assert(JSON.stringify(columns.map(c=>c.length).sort((a,b)=>a-b))==='[0,0,3,5,5]','three occupied unequal columns');
const free=f=>divisors(12).map(g=>g*f).filter(d=>d/gcd(d,12)===f).map(d=>[d,remove(primitive(d),3n)]).filter(([,m])=>m>1n);
const dead=[1,2,4,5,7,8,10,14,35];
assert(dead.every(f=>free(f).length===0),'unavailable shared periods');
const inventory={
 11:[23,89],13:[8191],22:[683],26:[2731],33:[599479],39:[79,121369],44:[397,2113],52:[53,157,1613],
 66:[67,20857],78:[22366891],80:[4278255361],88:[353,2931542417],132:[312709,4327489],156:[313,1249,3121,21841],
 176:[229153,119782433,43872038849],240:[394783681,46908728641],264:[7393,1761345169,98618273953],55:[881,3191,201961]
};
for(const [d,qs] of Object.entries(inventory)){
 const p=qs.reduce((m,q)=>m*BigInt(q),1n);
 assert(qs.every(trialPrime)&&p===primitive(+d),'primitive inventory '+d);
}
function groupCount(f){return free(f).flatMap(([d])=>{
 assert(inventory[d],'fully known period '+f+': '+d);
 return inventory[d];
}).length;}
assert(groupCount(11)===10&&groupCount(13)===12&&groupCount(20)===3&&groupCount(22)===5,'closed low inventory');
const factor=11*572;
const inherited=[];
for(let j=0;j<=10;j++)for(let z=0;z<=3&&j+z<=13;z++){
 const D=11-j, p=j*(factor/11)+z*D*5*(factor/(11*52))+(13-j-z)*Math.max(D*(factor/(11*13)),factor/22);
 if(p>=factor)inherited.push({j,z,num:p,den:factor});
}
assert(inherited.every(x=>x.j===0||x.j===9&&x.z===0||x.j===10),'all branches reduce to 0,9,10');
const eq=inherited.find(x=>x.j===9);
assert(eq.num===eq.den,'nine period-eleven classes need all four quotient half-mass slots');
let weighted=0;
let weightedCase=[];
const scale=13*780;
for(let k=0;k<=12;k++)for(let z=0;z<=3&&k+z<=13;z++){
 const D=13-k, p=k*(scale/13)+z*D*(scale/(13*12))+(13-k-z)*Math.max(D*(scale/(13*15)),scale/26);
 assert(p<scale,'equal-column weights exclude every zero-eleven case');
 if(p>weighted){weighted=p;weightedCase=[k,z];}
}
function cap(e){
 const g=gcd(e,35),counter=Array(g).fill(0);
 for(const a of A)counter[a%g]++;
 return [Math.max(...counter)*g,13*e];
}
for(let e=3;e<=280;e++){
 const [p,q]=cap(e);assert(2*p<q,'strict below half when period at least three');
 if(e%3!==0&&e!==5){assert(4*p<=q,'maximum quarter when outside two and five');}
}
const maxOrders=Object.fromEntries([11,22,44,55].map(f=>[f,Math.max(...free(f).map(([d])=>d))]));
assert(Math.max(...Object.values(maxOrders))===660,'maximum all-common order');
const res={inherited,weighted:[weighted,scale],weightedCase,sharedOrders:maxOrders,
 shapes:['j=9 with four period-22 classes','j=10 with a period-22 pair','j=10 with one period-22 class and two period-44 classes','j=10 with three period-55 classes']};

console.log(JSON.stringify(res,null,2));

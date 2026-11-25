
const gcd=(a,b)=>b?gcd(b,a%b):a;
const lcm=(a,b)=>a/gcd(a,b)*b;
const primes=[2,5,7,11,13];
const weights=[];
function gen(i,m,left,charges){
 if(i===primes.length){weights.push({m,charges,weight:13-left});return;}
 const p=primes[i];let power=1,terms=charges.slice();
 for(let w=left;w>=0;w-=p-1){
  gen(i+1,m*power,w,terms);
  power*=p;terms=terms.concat([[power,p-1]]);
 }
}
gen(0,1,13,[]);
const scale=weights.map(r=>r.m).reduce(lcm,1);
if(!Number.isSafeInteger(14*13*scale))throw Error('unsafe');
const maxima={1:13,5:5,7:3,35:1};
const h=[];
for(const a of weights)for(const g of [1,5,7,35]){
 const f=a.m*g;
 if(gcd(f,35)!==g||f<11||f===14||f===35)continue;
 h.push({...a,f,g,cap:maxima[g]*(scale/a.m)});
}
const biggest=Math.max(...h.map(x=>x.cap)),out=[];
for(const x of h){
 const c=x.cap+(13-x.weight)*biggest+x.charges.reduce((r,[v,n])=>r+n*Math.max(0,...h.filter(y=>y.m%v===0).map(y=>y.cap)),0);
 if(c>=13*scale)out.push({f:x.f,m:x.m,cap:c});
}
const greatest=Math.max(...out.map(x=>x.f));
const result={candidates:h.length,survived:out.length,greatest,maxOrder:greatest*12,list:out.map(x=>x.f).sort((a,b)=>a-b)};

console.log(JSON.stringify(result,null,2));

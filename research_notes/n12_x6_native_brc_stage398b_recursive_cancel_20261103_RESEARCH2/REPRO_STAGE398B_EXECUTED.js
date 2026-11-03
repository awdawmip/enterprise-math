// node compatible: node REPRO_STAGE398B_EXECUTED.js
const main = () => {
// Stage398-B independently executable exact JavaScript verifier.
const A=[1,-1,2,-2,3,-3,4,-4,5,-5,6,-6],B=[1,-1,2,-2];
function step(z,d){z=z.slice();z[Math.abs(d)-1]+=Math.sign(d);return z}
const cache=new Map();
function brc(n,z,weighted){let k=n+':'+z.join(',')+':'+weighted;if(cache.has(k))return cache.get(k);if(n===0)return z.every(x=>x===0)?1n:0n;let a=0n;for(let d of A){let p=(weighted?(d===1?2n:d===-1?3n:1n):1n);a+=p*brc(n-1,step(z,-d),weighted)}cache.set(k,a);return a}
function sig(c,w){if(c===0)return JSON.stringify(w.length?w[w.length-1]:0);let n=w.length,inv=n>=2&&w[n-1]===-w[n-2];return JSON.stringify([sig(c-1,w),n?sig(c-1,w.slice(0,-1)):null,inv?sig(c-1,w.slice(0,-2)):null])}
function obs(w){let z=[0,0,0,0,0,0],j=new Array(144).fill(0),omega=1n;for(let i=0;i<w.length;i++){let d=w[i];z=step(z,d);omega*=d===1?-2n:d===-1?3n:1n;if(i)j[A.indexOf(w[i-1])*12+A.indexOf(d)]++}return JSON.stringify([w.length,z,j,String(omega)])}
function op(w,a,c){if(a==='C')return c>0&&w.length>=2&&w.at(-1)===-w.at(-2)?[w.slice(0,-2),c-1]:null;return [w.concat([a]),c]}
function witness(c,x,y){if(c===0){if(x.at(-1)===y.at(-1))throw Error('bad base');return [1]}if(sig(c-1,x)!==sig(c-1,y))return witness(c-1,x,y);if(x.at(-1)!==y.at(-1))throw Error('last mismatch');if(sig(c-1,x.slice(0,-1))!==sig(c-1,y.slice(0,-1)))return [-x.at(-1),'C',...witness(c-1,x.slice(0,-1),y.slice(0,-1))];if(x.length<2||x.at(-1)!==-x.at(-2))throw Error('missing inverse');return ['C',...witness(c-1,x.slice(0,-2),y.slice(0,-2))]}
function distinguish(x,y,c,seq){for(let a of seq){let xx=op(x,a,c), yy=op(y,a,c);if(!!xx!==!!yy)return true;if(!xx)return false;x=xx[0];y=yy[0];c=xx[1];if(obs(x)!==obs(y))return true}return false}
const n=8,wrs=[];for(let r=2;r<8;r++){let w=Array.from({length:n},(_,i)=>i+1===r?-1:1);wrs.push([r,w])}
if(new Set(wrs.map(x=>obs(x[1]))).size!==1)throw Error('fiber mismatch');
const U=new Map(),S=new Map();for(let [r,w] of wrs){let u=w.slice(-5).join(','),s=sig(2,w);if(!U.has(u))U.set(u,[]);if(!S.has(s))S.set(s,[]);U.get(u).push(r);S.get(s).push(r)}
const groups=Array.from(S.values()).sort((a,b)=>a[0]-b[0]);
if(U.size!==5||S.size!==3||JSON.stringify(groups)!==JSON.stringify([[2,3,4,5],[6],[7]]))throw Error('quotient mismatch');
const N=brc(8,[6,0,0,0,0,0],false), W=brc(8,[6,0,0,0,0,0],true);
if(N!==288n||W!==20992n)throw Error('native BRC mismatch');
let pairs=0,eq=0,neq=0,checks=0,maxWitness=0,groupsScanned=0;
for(let m=0;m<=6;m++){let table=new Map();function walk(w){if(w.length===m){let k=obs(w);if(!table.has(k))table.set(k,[]);table.get(k).push(w);return}for(let d of B)walk(w.concat([d]))}walk([]);groupsScanned+=table.size;
for(let words of table.values())for(let i=0;i<words.length;i++)for(let j=i+1;j<words.length;j++){let x=words[i],y=words[j];pairs++;for(let c=0;c<=2;c++){if(sig(c,x)===sig(c,y)){eq++;for(let d of A){if(obs(x.concat([d]))!==obs(y.concat([d]))||sig(c,x.concat([d]))!==sig(c,y.concat([d])))throw Error('append congruence');checks++}if(c){let xx=op(x,'C',c),yy=op(y,'C',c);if(!!xx!==!!yy)throw Error('cancel enabled');if(xx){if(obs(xx[0])!==obs(yy[0])||sig(c-1,xx[0])!==sig(c-1,yy[0]))throw Error('cancel congruence');checks++}}}else{neq++;let seq=witness(c,x,y);maxWitness=Math.max(maxWitness,seq.length);if(!distinguish(x,y,c,seq))throw Error('nonwitness');checks++}}}}
return {result:'STAGE398B_RECURSIVE_SIGNATURE_PASS',BRC_count:String(N),BRC_weight:String(W),uniform_classes:U.size,minimal_classes:S.size,uniform_bits:3,minimal_bits:2,complete_fiber_groups:groups,observer_groups:groupsScanned,pairs,eq,neq,checks,maxWitness};
};
const result=main();console.log(JSON.stringify(result,null,2));

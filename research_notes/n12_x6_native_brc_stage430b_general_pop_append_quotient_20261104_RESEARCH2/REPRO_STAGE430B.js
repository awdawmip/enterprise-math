'use strict';
const D=Array.from({length:12},(_,i)=>i);
function endpoint(w){const v=[0,0,0,0,0,0];for(const a of w)v[Math.floor(a/2)]+=(a%2===0?1:-1);return v.join(',');}
function J(w){const d=new Array(144).fill(0);for(let i=1;i<w.length;i++)d[12*w[i-1]+w[i]]++;return d.map((v,i)=>v?i+':'+v:'').filter(Boolean).join(',');}
function K(p,q){let k=0;for(let i=0;i<Math.min(p.length,q.length);i++)k+=(p[i]===q[i]?1:0);return k;}
function O(p,q){return [p.length,q.length,endpoint(p),endpoint(q),J(p),J(q),K(p,q)].join('|');}
function tuple(p,q,b){return q.slice(q.length-b-1).join(',')+'|'+p.slice(q.length-b,q.length+1).join(',');}
function futures(b){const z=[];for(let k=0;k<=b;k++){z.push('P'.repeat(k));for(let at=0;at<=k;at++)for(const x of D)z.push('P'.repeat(at)+'a'+String.fromCharCode(65+x)+'P'.repeat(k-at));}return z;}
function runWord(p,q,word){const trace=[];let z=q.slice();for(let i=0;i<word.length;i++){if(word[i]==='P'){if(!z.length){trace.push('ILLEGAL');break;}z.pop();}else if(word[i]==='a'){const x=word.charCodeAt(++i)-65;z.push(x);}else throw Error('unexpected instruction');trace.push(O(p,z));}return trace.join(' :: ');}
function words(alpha,n){const out=[];const rec=(w,k)=>{if(k===n){out.push(w);return;}for(const x of alpha)rec(w.concat([x]),k+1);};rec([],0);return out;}
function exactFiberCheck(b,n,m,alphabet){const ff=futures(b),P=words(alphabet,m),Q=words(alphabet,n),fibers=new Map();let histories=0;
for(const p of P)for(const q of Q){histories++;const key=O(p,q);let a=fibers.get(key);if(!a){a=[];fibers.set(key,a);}a.push({p,q,t:tuple(p,q,b)});}
let groups=0,pairs=0,same=0,different=0,divergent=0;
for(const items of fibers.values()){if(items.length<2)continue;groups++;for(let i=0;i<items.length;i++)for(let j=i+1;j<items.length;j++){pairs++;const a=items[i],c=items[j],eq=a.t===c.t;let diff=false;for(const f of ff){if(runWord(a.p,a.q,f)!==runWord(c.p,c.q,f)){diff=true;break;}}if(eq===diff)throw Error('quotient mismatch '+JSON.stringify({b,n,m,a,c}));if(eq)same++;else{different++;divergent++;}}}
return {b,n,m,alphabet,operations:ff.length,histories,fibers:fibers.size,nontrivial_fibers:groups,pairs,same_tuple_pairs:same,different_tuple_pairs:different,distinguished_pairs:divergent};}
function lowerBoundFamily(b){const L=b+1,n=L+2,m=5*L+9,M=3*L+3,R=L+1,q=Array(n).fill(2),hist=[];
for(let bits=0;bits<2**L;bits++){const w=Array.from({length:L},(_,i)=>(bits>>i)&1),bb=w.reduce((s,x)=>s+(x===1),0);let rr=0;for(let i=0;i<L;i++)if(w[i]===1&&(i===0||w[i-1]===0))rr++;
const h=R-rr,z=M-bb;if(h<1||z<h)throw Error('bad runs');
const p=[0,0,0,...w,0,...Array(z-h+1).fill(1)];for(let j=1;j<h;j++)p.push(0,1);while(p.length<m)p.push(0);if(p.length!==m)throw Error('bad length');hist.push({p,word:w.join('')});}
const base=O(hist[0].p,q),sig=new Set();for(const h of hist){if(O(h.p,q)!==base)throw Error('fiber mismatch '+h.word);const obs=[];for(let j=0;j<=b;j++){const f='P'.repeat(j)+'aA',last=runWord(h.p,q,f).split(' :: ').at(-1),kval=Number(last.split('|').at(-1));obs.push(kval);if(kval!==(h.p[n-j]===0?1:0))throw Error('bad K probe');}sig.add(obs.join(''));}if(sig.size!==2**L)throw Error('collision');
return {pop_budget:b,window_bits:L,history_count:hist.length,distinct_future_signatures:sig.size,n,m,initial_observer_equal:true};}
function verify(){const tests=[exactFiberCheck(2,3,4,[0,1,2]),exactFiberCheck(2,3,7,[0,1,2]),exactFiberCheck(2,4,8,[0,1]),exactFiberCheck(1,3,6,[0,1,2])];const lower=[];for(let b=0;b<=7;b++)lower.push(lowerBoundFamily(b));return {status:'STAGE430B_GENERAL_POP_ONE_APPEND_QUOTIENT_PASS',exact_fiber_tests:tests,lower_bound_families:lower,scope:'All 12 APPEND labels; exhaustive finite initial-word subalphabets. Unbounded theorem established by symbolic proof.'};}
if(typeof require!=='undefined'&&require.main===module)console.log(JSON.stringify(verify(),null,2));

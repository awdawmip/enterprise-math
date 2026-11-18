'use strict';
// EC49EXE independently implementable V8 check, run: node VERIFY_EC49EXE_PORTABLE.js
const O={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const H=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]];
const B=['N','A','B','AB','BA'], PRIME=1000003;
const check=(v,s)=>{if(!v)throw Error(s)};
function steps(w){return [...w].flatMap(t=>O[t])}
function disp(w){const s=steps(w);return Array.from({length:6},(_,i)=>s.filter(x=>x===i+1).length-s.filter(x=>x===-i-1).length)}
function key(w){const s=steps(w);return Array.from({length:6},(_,i)=>s.filter(x=>x===i+1).length).join(',')}
function sig(w){let out=[];for(const [e0,p0] of H){let e=e0,p=p0;for(const t of steps(w)){if(p===1&&t===2){if(e==='N')e='A';else if(e==='B')e='BA'}else if(p===2&&t===1){if(e==='N')e='B';else if(e==='A')e='AB'}p=t}out.push(B.indexOf(e))}return out}
function power(a,n){let x=1;for(;n;n=Math.floor(n/2),a=a*a%PRIME)if(n%2)x=x*a%PRIME;return x}
function rank(ss){const cs=ss.flatMap(s=>B.map((_,b)=>s.map(v=>v===b?1:0)));const a=Array.from({length:9},(_,i)=>cs.map(c=>c[i]));let r=0;for(let j=0;j<cs.length&&r<9;j++){let k=r;while(k<9&&!a[k][j])k++;if(k===9)continue;[a[r],a[k]]=[a[k],a[r]];const v=power(a[r][j],PRIME-2);for(let t=j;t<cs.length;t++)a[r][t]=a[r][t]*v%PRIME;for(let i=r+1;i<9;i++){const z=a[i][j];for(let t=j;t<cs.length;t++)a[i][t]=(a[i][t]-z*a[r][t]%PRIME+PRIME)%PRIME}r++}return r}
function resources(w){const pre=new Set(),ks=new Set(),ss=new Set();for(const [hh,words] of Object.entries(w)){let h=+hh;check(new Set(words.map(key)).size===1,'key h'+h);let ts=[...new Map(words.map(s=>[sig(s).join(','),sig(s)])).values()];check(rank(ts)===9,'rank h'+h);ks.add(key(words[0]));for(let s of words){check(s.length===h&&disp(s).join(',')==='2,0,0,0,0,0','native return '+s);const t=steps(s);for(let i=1;i<=t.length;i++)pre.add(t.slice(0,i).join(','));ss.add(sig(s).join(','))}}return[pre.size,ks.size,ss.size]}
const base=['ce','de','ec','ed'],S=base.map(sig);
const ranks={};for(let k=1;k<=4;k++){const arr=new Set();for(let m=1;m<16;m++)if(m.toString(2).replaceAll('0','').length===k)arr.add(rank(S.filter((_,i)=>m&(1<<i))));ranks[k]=[...arr].sort((a,b)=>a-b)}
check(JSON.stringify(ranks)==='{"1":[3],"2":[5],"3":[7],"4":[9]}','signature ranks');
check(new Set(Object.values(O).map(v=>v.slice(0,2).join(','))).size===7,'prefix');
let classes=new Map();for(let [op,s] of Object.entries(O)){let p=Array.from({length:6},(_,i)=>s.filter(x=>x===i+1).length).join(',');if(!classes.has(p))classes.set(p,[]);classes.get(p).push(op)}for(const ks of classes.values())check(new Set(ks.map(k=>O[k][0])).size===ks.length,'terminal 2-step distinct');
const sample={};for(let h=2;h<=40;h++){let W={};for(let i=2;i<=h;i++)W[i]=base.map(w=>w+'g'.repeat(i-2));const r=resources(W);check(r.join(',')===[8*h+12,h-1,4].join(','),'family H'+h);if([2,3,4,5,6,7,8,16,32,40].includes(h))sample[h]=r}
const h7={2:base,3:['feg','gef'],4:['cecc','dedd','eccc','eddd'],5:['cecfg','dedgf','eccfg','eddgf'],6:['fegfgc','fegfgd','geffgc','geffgd'],7:['fegfggf','geffgfg']};
check(resources(h7).join(',')==='116,2,6','prior h7');
const h8={...h7,8:h7[7].map(w=>w+'f')};
check(resources(h8).join(',')==='120,3,6','H8');
const front=[[58,5,6],[68,6,4],[72,4,6],[80,5,4],[86,3,6],[92,4,4],[116,2,6],[116,3,4]];
front.forEach((p,i)=>check(!front.some((q,j)=>i!==j&&q.every((v,k)=>v<=p[k])&&q.some((v,k)=>v<p[k])),'dominance'));
const result={status:'PASS',research_unit:'EC49EXE',T4_subset_ranks:ranks,all_H_checked_through:40,family_samples:sample,H7:[68,6,4],H8:[120,3,6],H8_minimum_M_exact:3,H7_Pareto:front};
console.log(JSON.stringify(result,null,2));
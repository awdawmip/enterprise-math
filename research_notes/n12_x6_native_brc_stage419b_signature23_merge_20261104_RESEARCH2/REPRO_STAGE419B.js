'use strict';
// Stage419-B | full-observer exact categorical checks of signature 2/3 under bounded futures.
// Typed native X6 D={+-E1,...,+-E6}; all arithmetic exact integer/categorical.
const D=[1,-1,2,-2,3,-3,4,-4,5,-5,6,-6],A=1,B=-1;
const assert=(b,msg)=>{if(!b)throw Error(msg)};
function fiber(n){const f=[];for(let r=2;r<n-2;r++)for(let s=r+2;s<n;s++)for(const i of [r,s]){
const P=Array(i-1).fill(A).concat([B],Array(n-i).fill(A));
const Q=Array(r-1).fill(A).concat([B],Array(s-r-1).fill(A),[B],Array(n-s).fill(A));
f.push({r,s,i,P,Q});}return f;}
function obs(P,Q){const one=W=>{const z=Array(6).fill(0),J={};for(let j=0;j<W.length;j++){z[Math.abs(W[j])-1]+=Math.sign(W[j]);if(j){const k=W[j-1]+','+W[j];J[k]=(J[k]||0)+1;}}return [W.length,z,Object.entries(J).sort((a,b)=>a[0].localeCompare(b[0]))]};return JSON.stringify([one(P),one(Q),P.reduce((k,x,i)=>k+(i<Q.length&&x===Q[i]?1:0),0)])}
function key(x){return JSON.stringify([x.P.slice(-6),x.Q.slice(-7)])}
function step(x,act){let {P,Q,p,c}=x;if(act[0]==='APP'){P.push(act[1]);Q.push(act[2]);return true;}if(act[0]==='POP'){if(!p||!Q.length)return false;Q.pop();x.p--;return true;}if(act[0]==='CANCEL'){if(!c||P.length<2||Q.length<2||P.at(-1)!==-P.at(-2)||Q.at(-1)!==-Q.at(-2))return false;P.splice(-2);Q.splice(-2);x.c--;return true;}throw Error('bad act')}
function init(x){return {P:x.P.slice(),Q:x.Q.slice(),p:2,c:2}}
function run(x,trace){const st=init(x),history=[obs(st.P,st.Q)];for(const act of trace){const ok=step(st,act);history.push(ok?obs(st.P,st.Q):'DENIED_'+act[0]);if(!ok)break;}return JSON.stringify(history)}
function uniq(x){return [...new Map(x.map(y=>[key(y),y])).values()]}
function patterns(a,p,c,pre=[],out=[]){if(!a&&!p&&!c){out.push(pre);return out;}if(a)patterns(a-1,p,c,pre.concat('APP'),out);if(p)patterns(a,p-1,c,pre.concat('POP'),out);if(c)patterns(a,p,c-1,pre.concat('CANCEL'),out);return out;}
let traceCount=0,checks=0;
function auditClass(group,options){const reps=uniq(group);assert(reps.length===3,'three keys');const goal=JSON.stringify(obs(reps[0].P,reps[0].Q));assert(reps.every(x=>obs(x.P,x.Q)===JSON.parse(goal)),'initial observation');
for(const setting of options){const {maxa,maxp,maxc,letters}=setting;for(let a=0;a<=maxa;a++)for(let p=0;p<=maxp;p++)for(let c=0;c<=maxc;c++)for(let pattern of patterns(a,p,c)){
function visit(j,t){if(j===pattern.length){traceCount++;const hs=reps.map(x=>run(x,t));checks++;if(!hs.every(s=>s===hs[0]))throw Error('counterexample '+JSON.stringify({group:group[0].i===group[0].r?'2':'3',t,items:reps.map(x=>({r:x.r,s:x.s,i:x.i,raw_key:key(x)})),outputs:hs}));return;}if(pattern[j]==='APP'){for(let u of letters)for(let v of letters){t.push(['APP',u,v]);visit(j+1,t);t.pop();}}else{t.push([pattern[j]]);visit(j+1,t);t.pop();}}
visit(0,[]);
}}
return reps.map(x=>({r:x.r,s:x.s,i:x.i,P_suffix:x.P.slice(-6),Q_suffix:x.Q.slice(-7)}))}
function main(){let minObs=0,maxObs=0;for(let n=11;n<=40;n++){let f=fiber(n);assert(f.length===(n-3)*(n-4),'fiber size');for(const c of [2,3]){let g=f.filter(x=>x.s===n-3&&(c===2?x.i===x.r:x.i===x.s));assert(g.length===n-6,'target size '+n+','+c);assert(uniq(g).length===3,'three target suffix keys '+n+','+c);assert(new Set(g.map(x=>obs(x.P,x.Q))).size===1,'common obs '+n+','+c);minObs+=g.length;}}const f11=fiber(11),opts=[{maxa:1,maxp:2,maxc:2,letters:D},{maxa:2,maxp:1,maxc:1,letters:D},{maxa:2,maxp:2,maxc:2,letters:[1,-1,2,-2]},{maxa:3,maxp:2,maxc:2,letters:[1,-1]}];let r2=auditClass(f11.filter(x=>x.s===8&&x.i===x.r),opts);let r3=auditClass(f11.filter(x=>x.s===8&&x.i===x.s),opts);return {marker:'STAGE419B_SIGNATURE_2_3_MERGE_PASS',setup:'P_i=A^(i-1) B A^(n-i), Q_rs=A^(r-1) B A^(s-r-1) B A^(n-s), s=n-3, groups i=r and i=s',native_dimensions:6,directions:12,operations:'APP arbitrary signed directions, Q-only POP up to 2, inverse-pair two-source CANCEL up to 2',observable:'full lengths; six signed endpoint entries per source; each complete directed J; absolute aligned K; attempted enabledness',n11_representatives:{class2:r2,class3:r3},n11_exact_trace_count:traceCount,comparisons:checks,other_exact_coverage:'Each n=11..40; both groups exactly n-6 histories and three safe suffix keys; same full initial observation',new_minimal_state_bound_candidate:[16,22],evidence_strength:'Bounded exhaustive computational check; all-horizon conclusion requires separate symbolic proof',scientific_pins:{global:'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',em:'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',p000_blob:'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'}}}
const ans=main();console.log(JSON.stringify(ans,null,2));

// Stage418-B reproducible exact integer/categorical finite checks.
// Native X6, D={±E1,...,±E6}, two Q-only POP, two paired inverse CANCEL.
'use strict';
const A=1,B=-1,D=[1,-1,2,-2,3,-3,4,-4,5,-5,6,-6];
function need(x,m){if(!x)throw Error(m)}
function fiber(n){let out=[];for(let r=2;r<n-2;r++)for(let s=r+2;s<n;s++)for(let i of [r,s]){
let P=Array(i-1).fill(A).concat([B],Array(n-i).fill(A));
let Q=Array(r-1).fill(A).concat([B],Array(s-r-1).fill(A),[B],Array(n-s).fill(A));out.push({n,r,s,i,P,Q});}
return out;}
function repkey(x){return JSON.stringify([x.P.slice(-6),x.Q.slice(-7)])}
function rawobs(P,Q){
  function one(W){let z=Array(6).fill(0),J=new Map();for(let x of W)z[Math.abs(x)-1]+=Math.sign(x);for(let i=1;i<W.length;i++){
  let k=W[i-1]+','+W[i];J.set(k,(J.get(k)||0)+1);}return [W.length,z,[...J.entries()].sort((a,b)=>a[0].localeCompare(b[0]))];}
  let K=0;for(let k=0;k<Math.min(P.length,Q.length);k++)if(P[k]===Q[k])K++;return [one(P),one(Q),K];
}
function state(x){return {P:x.P.slice(),Q:x.Q.slice(),p:2,c:2}}
function move(s,op){
 if(op[0]==='APP'){s.P.push(op[1]);s.Q.push(op[2]);return true;}
 if(op[0]==='POP'){if(s.p===0||s.Q.length===0)return false;s.Q.pop();s.p--;return true;}
 if(op[0]==='CANCEL'){if(s.c===0||s.P.length<2||s.Q.length<2||s.P.at(-1)!==-s.P.at(-2)||s.Q.at(-1)!==-s.Q.at(-2))return false;
 s.P.splice(-2);s.Q.splice(-2);s.c--;return true;}throw Error('operation');
}
function runTrace(reps,trace){let states=reps.map(state);
 for(let step=0;step<trace.length;step++){
 let enabled=states.map(s=>move(s,trace[step]));need(enabled.every(k=>k===enabled[0]),'ENABLED_DIVERGENCE '+JSON.stringify(trace.slice(0,step+1)));
 if(!enabled[0])return;
 let sig=JSON.stringify(rawobs(states[0].P,states[0].Q));
 for(let j=1;j<states.length;j++)need(sig===JSON.stringify(rawobs(states[j].P,states[j].Q)),'OBS_DIVERGENCE '+JSON.stringify(trace.slice(0,step+1)));
 }
}
function patterns(a,p,c,prefix=[],out=[]){if(!a&&!p&&!c){out.push(prefix);return out;}if(a)patterns(a-1,p,c,prefix.concat('APP'),out);if(p)patterns(a,p-1,c,prefix.concat('POP'),out);if(c)patterns(a,p,c-1,prefix.concat('CANCEL'),out);return out}
function audit(){let ncount=0;let classes={};for(let n=11;n<=40;n++){
 let f=fiber(n),g=f.filter(x=>x.s===n-4),keys=new Map();for(let x of g)keys.set(repkey(x),x);
 need(f.length===(n-3)*(n-4),'fiber size '+n);need(g.length===2*(n-7),'group1 size '+n);need(keys.size===4,'group1 keys '+n);
 need(g.every(x=>x.P.slice(-4).every(t=>t===A)&&JSON.stringify(x.Q.slice(-5))===JSON.stringify([B,A,A,A,A])),'guarded suffix '+n);
 need(new Set(g.map(x=>JSON.stringify(rawobs(x.P,x.Q)))).size===1,'current O '+n);
 classes[n]=g.length;ncount+=g.length;
}
let reps=[...new Map(fiber(11).filter(x=>x.s===7).map(x=>[repkey(x),x])).values()];need(reps.length===4,'four raw suffix reps');
let counts={oneAPP_full12:0,twoAPP_full12_with_at_most_one_POP_and_one_CANCEL:0,twoAPP_four_letters_full_budgets:0,threeAPP_two_letters_full_budgets:0};
function auditTraces(maxa,maxp,maxc,directions,field){
 for(let a=0;a<=maxa;a++)for(let p=0;p<=maxp;p++)for(let c=0;c<=maxc;c++)for(let pat of patterns(a,p,c)){
 function visit(pos,t){if(pos===pat.length){counts[field]++;runTrace(reps,t);return;}
  if(pat[pos]==='APP')for(let x of directions)for(let y of directions)visit(pos+1,t.concat([['APP',x,y]]));
  else visit(pos+1,t.concat([[pat[pos]]]));}
 visit(0,[]);
 }
}
auditTraces(1,2,2,D,'oneAPP_full12');
auditTraces(2,1,1,D,'twoAPP_full12_with_at_most_one_POP_and_one_CANCEL');
auditTraces(2,2,2,[1,-1,2,-2],'twoAPP_four_letters_full_budgets');
auditTraces(3,2,2,[1,-1],'threeAPP_two_letters_full_budgets');
return {marker:'STAGE418B_B_CAPPED_CLASS1_PASS',D:D.length,pops:2,cancels:2,model:'Full O=(lengths, X6 signed endpoints, directed J for each source, absolute aligned K); enabledness on every operation',class1:{n11_histories:8,n11_raw_keys:4,n16_histories:18,n40_histories:66,population_formula:'2*(n-7) for n>=11',guard:'P ends A^4; Q ends B A^4',all_n_checked:'11<=n<=40',total_histories_checked:ncount},finite_check:{...counts,statement:'Every legal/denied prefix in these finite trace families on all four group1 representatives agrees; unbounded claim follows separately from proof'},previous_upper_bound:29,new_upper_bound:26,previous_lower_bound:16,scientific_pins:{global:'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',em:'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',p000_blob:'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'},status:'AUTHOR_SIDE_PROOF_UNREVIEWED_NOT_ADMITTED'};}
const result=audit();console.log(JSON.stringify(result,null,2));

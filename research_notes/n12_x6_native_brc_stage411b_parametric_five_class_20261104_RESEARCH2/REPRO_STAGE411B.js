"use strict";
const assert=(c,m)=>{if(!c)throw Error(m)};
const range=(a,b)=>Array.from({length:Math.max(0,b-a+1)},(_,i)=>a+i);
const J=s=>['AA','AB','BA','BB'].map(e=>[e,range(0,s.length-2).filter(i=>s.slice(i,i+2)===e).length]);
const obs=(p,q)=>JSON.stringify([p.length,q.length,p.split('A').length-p.split('B').length,q.split('A').length-q.split('B').length,J(p),J(q),range(0,Math.min(p.length,q.length)-1).filter(i=>p[i]===q[i]).length]);
function fiber(n){
 const P=range(1,n-2).map(i=>'A'.repeat(i)+'B'+'A'.repeat(n-1-i)),Q=[];
 for(let u=1;u<=n-4;u++)for(let v=1;v<=n-3-u;v++){const w=n-2-u-v;if(w>=1)Q.push('A'.repeat(u)+'B'+'A'.repeat(v)+'B'+'A'.repeat(w))}
 return P.flatMap(p=>Q.filter(q=>range(0,n-1).filter(i=>p[i]===q[i]).length===n-1).map(q=>[p,q])).sort((x,y)=>(x[0]+'|'+x[1]).localeCompare(y[0]+'|'+y[1]));
}
function fiberIndependent(n){
 const F=[];for(let r=2;r<=n-3;r++)for(let s=r+2;s<=n-1;s++){
  const q='A'.repeat(r-1)+'B'+'A'.repeat(s-r-1)+'B'+'A'.repeat(n-s);
  for(const i of [r,s])F.push(['A'.repeat(i-1)+'B'+'A'.repeat(n-i),q]);
 }
 return F.sort((x,y)=>(x[0]+'|'+x[1]).localeCompare(y[0]+'|'+y[1]));
}
function label(n,p,q){
 const i=p.indexOf('B')+1,r=q.indexOf('B')+1,s=q.lastIndexOf('B')+1;
 if(s===n-1&&i===s)return r===n-3?'C0':'C1';
 if(s===n-2)return 'C2';
 if(s===n-1&&i===r)return 'C3';
 return 'C4';
}
function certificate(C){
 assert(C.every(([p])=>p.endsWith('AA')),'P terminal AA');
 const [p0,q0]=C[0];
 for(const [p,q] of C){
  assert(p.slice(-2)===p0.slice(-2)&&q.slice(-2)===q0.slice(-2),'original cross-edge');
  for(let dp=0;dp<=1;dp++)for(let dq=0;dq<=2;dq++){
   const P=dp?p.slice(0,-dp):p,Q=dq?q.slice(0,-dq):q;
   const P0=dp?p0.slice(0,-dp):p0,Q0=dq?q0.slice(0,-dq):q0;
   assert(obs(P,Q)===obs(P0,Q0),'joint truncated observation');
   assert(P.slice(-(dp?1:2))===P0.slice(-(dp?1:2)),'P boundary');
   assert(Q.slice(-(dq===2?1:2))===Q0.slice(-(dq===2?1:2)),'Q boundary');
  }
 }
 return C.length*6;
}
function step(st,op){
 const {p,q,pop,cancel}=st;
 if(op[0]==='APP')return {p:p+op[1],q:q+op[2],pop,cancel};
 if(op[0]==='POP')return !pop&&q.length?{p,q:q.slice(0,-1),pop:1,cancel}:null;
 if(op[0]==='CANCEL')return !cancel&&p.length>=2&&q.length>=2&&['AB','BA'].includes(p.slice(-2))&&['AB','BA'].includes(q.slice(-2))?{p:p.slice(0,-2),q:q.slice(0,-2),pop,cancel:1}:null;
 throw Error('unknown action');
}
function trace(p,q,tr){let st={p,q,pop:0,cancel:0};for(const op of tr){st=step(st,op);if(st===null)return 'DISABLED'}return obs(st.p,st.q)}
const TESTS=[[['CANCEL']],[['POP']],[['POP'],['CANCEL']],[['POP'],['APP','B','B'],['CANCEL']]];
function eulerK(n){
 const cache=new Map();let states=0;const rec=(t,p,q,k,rp,rq)=>{
  const key=JSON.stringify([t,p,q,k,rp,rq]);if(cache.has(key))return cache.get(key);
  states++;if(t===n)return k===n-1&&rp.every(x=>!x)&&rq.every(x=>!x)?1:0;
  let sum=0;for(let a=0;a<2;a++)for(let b=0;b<2;b++){
   const ia=(p==='A'?0:2)+a,ib=(q==='A'?0:2)+b;
   if(rp[ia]===0||rq[ib]===0)continue;
   const ap=rp.slice(),aq=rq.slice();ap[ia]--;aq[ib]--;
   sum+=rec(t+1,a?'B':'A',b?'B':'A',k+(a===b),ap,aq);
  }
  cache.set(key,sum);return sum;
 };
 return {count:rec(1,'A','A',1,[n-3,1,1,0],[n-5,2,2,0]),states};
}
function brc(n){
 const D=[];for(let axis=0;axis<6;axis++)for(const sg of [1,-1])D.push([axis,sg,axis===0?(sg===1?2:3):1]);
 let dp=new Map([['0,0,0,0,0,0',[1,1]]]);
 for(let t=0;t<n;t++){
  const next=new Map();for(const [key,[N,W]] of dp){
   const z=key.split(',').map(Number);
   for(const [axis,sign,w] of D){z[axis]+=sign;const k=z.join(',');let x=next.get(k)||[0,0];next.set(k,[x[0]+N,x[1]+w*W]);z[axis]-=sign}
  }dp=next;
 }
 const at=i=>dp.get([i,0,0,0,0,0].join(','))||[0,0];
 return {P_endpoint:[n-2,0,0,0,0,0],P_N_W:at(n-2),Q_endpoint:[n-4,0,0,0,0,0],Q_N_W:at(n-4),endpoint_states:dp.size};
}
function verify(){
 const family=[];let certificateChecks=0,finiteFutureTransitions=0;
 for(let n=5;n<=16;n++){
  const F=fiber(n);assert(JSON.stringify(F)===JSON.stringify(fiberIndependent(n)),'independent enumeration '+n);
  assert(F.length===(n-3)*(n-4),'fiber cardinality '+n);
  assert(new Set(F.map(([p,q])=>obs(p,q))).size===1,'initial full observer '+n);
  const groups={C0:[],C1:[],C2:[],C3:[],C4:[]};
  for(const pair of F)groups[label(n,...pair)].push(pair);
  const sizes={C0:1,C1:n-5,C2:2*(n-5),C3:n-4,C4:(n-6)*(n-5)};
  for(const k in sizes)assert(groups[k].length===sizes[k],'class formula '+n+k);
  if(groups.C1.length){const [p0,q0]=groups.C1[0];for(const [p,q] of groups.C1)assert(p.slice(-3)===p0.slice(-3)&&q.slice(-4)===q0.slice(-4),'C1 safe suffix')}
  for(const k of ['C2','C3','C4'])if(groups[k].length)certificateChecks+=certificate(groups[k]);
  const signatures=[];
  for(const k of ['C0','C1','C2','C3','C4'])if(groups[k].length){
   const sig=groups[k].map(([p,q])=>TESTS.map(t=>trace(p,q,t)));
   assert(sig.every(s=>JSON.stringify(s)===JSON.stringify(sig[0])),'constant trace observer '+n+k);
   signatures.push(JSON.stringify(sig[0]));
  }
  assert(new Set(signatures).size===signatures.length,'four test traces separate '+n);
  family.push({n,fiber:F.length,q:signatures.length,multiplicities:Object.fromEntries(Object.entries(groups).filter(([,v])=>v.length).map(([k,v])=>[k,v.length]))});
  if(n===7){
   assert(new Set(F.map(([p,q])=>p.slice(-3)+'|'+q.slice(-4))).size===7,'raw safe suffix count');
   // Finite independent state-transition comparisons: APP alphabet ±E1,+E3, depth ≤4.
   const ops=[['POP'],['CANCEL']];for(const a of 'ABC')for(const b of 'ABC')ops.push(['APP',a,b]);
   for(const arr of Object.values(groups))for(let i=0;i<arr.length;i++)for(let j=i+1;j<arr.length;j++){
    const todo=[[{p:arr[i][0],q:arr[i][1],pop:0,cancel:0},{p:arr[j][0],q:arr[j][1],pop:0,cancel:0},0]];
    for(let h=0;h<todo.length;h++){
     const [x,y,d]=todo[h];assert(obs(x.p,x.q)===obs(y.p,y.q),'future observation');
     if(d===4)continue;
     for(const op of ops){const xx=step(x,op),yy=step(y,op);assert((xx===null)===(yy===null),'future enabledness');if(xx){todo.push([xx,yy,d+1]);finiteFutureTransitions++}}
    }
   }
  }
 }
 const edp=eulerK(7);assert(edp.count===12,'independent Euler/K transfer');
 const b=brc(7);assert(b.P_N_W[0]===217&&b.Q_N_W[0]===10521,'native BRC endpoint count');
 return {status:'STAGE411B_PARAMETRIC_FIVE_CLASS_PASS',scientific_scope:'n>=5 full-X6 path-formal paired APP, one POP_Q, one simultaneous CANCEL',family,stage411:{full_fiber:12,raw_suffix_states:7,minimal_future_states:5,class_sizes:[1,2,4,3,2],independent_euler_K:edp,native_BRC:b},finite_n_check:[5,16],certificate_truncations:certificateChecks,finite_transition_checks:finiteFutureTransitions,finite_transition_append_alphabet:['+E1','-E1','+E3'],finite_transition_depth:4,proof_status:'AUTHOR_PROVED_UNREVIEWED',admission:'NOT_ADMITTED'};
}
const report=verify();
if(typeof process!=='undefined'&&process.stdout)process.stdout.write(JSON.stringify(report,null,2)+'\n');

'use strict';
// Exact Stage499-B BRC X6 directed-relationship experiment.
// Observer: six signed-axis displacement counts and all 144 ordered pairs.
// Provenance labels O/P are retained for future DELETE_LAST_PUBLIC.
const ABC='ABCDEFGHIJKL', ACT=['POP','SET_END_MINUS_2_C','INSERT_BEFORE_LAST2_C','DELETE_END_MINUS_1','DELETE_LAST_PUBLIC'];
const id=Object.fromEntries([...ABC].map((x,i)=>[x,i]));
function ok(x,why='assertion failed'){if(!x)throw Error(why);}
function same(x,y){return JSON.stringify(x)===JSON.stringify(y);}
function word(s,tag='O'){return [...s].map((v,i)=>({v,src:typeof tag==='string'&&tag.length===s.length?tag[i]:tag}));}
function F(s){
  const D=Array(6).fill(0),E=Array(144).fill(0);
  for(const p of s){const j=id[p.v];D[j%6]+=(j<6?1:-1);}
  for(let j=1;j<s.length;j++)E[12*id[s[j-1].v]+id[s[j].v]]++;
  return [D,E];
}
function edgeEnd(z,first){
  const v=z[0].slice(), E=z[1];
  for(let a=0;a<12;a++)for(let b=0;b<12;b++){
    const j=first?b:a;
    v[j%6]-=E[12*a+b]*(j<6?1:-1);
  }
  const j=v.findIndex(t=>t!==0);
  ok(j>=0 && Math.abs(v[j])===1 && v.filter(t=>t!==0).length===1,'endpoint extraction');
  return ABC[j+(v[j]<0?6:0)];
}
function join(x,y){
  const D=x[0].map((a,i)=>a+y[0][i]),E=x[1].map((a,i)=>a+y[1][i]);
  E[12*id[edgeEnd(x,false)]+id[edgeEnd(y,true)]]++;
  return [D,E];
}
function step(s,a,cap){
  const n=s.length;
  if(a==='POP')return n?s.slice(0,-1):null;
  if(a==='SET_END_MINUS_2_C')return n<3?null:s.map((t,i)=>i===n-3?{v:'C',src:t.src}:t);
  if(a==='INSERT_BEFORE_LAST2_C')return n<2||(cap&&n>=8)?null:[...s.slice(0,-2),{v:'C',src:'P'},...s.slice(-2)];
  if(a==='DELETE_END_MINUS_1')return n<2?null:[...s.slice(0,-2),...s.slice(-1)];
  if(a==='DELETE_LAST_PUBLIC'){const i=s.findLastIndex(t=>t.src==='P');return i<0?null:[...s.slice(0,i),...s.slice(i+1)];}
  throw Error(a);
}
function K(s,h){
  const L=h+3;ok(s.length>L,'core nonempty');
  const c=s.slice(0,-L),t=s.slice(-L);
  ok(c.every(x=>x.src==='O'),'guard: all core provenance original');
  return [F(c),t];
}
function traces(x,y,h,cap,stats){
  function go(a,b,d){
    stats.prefix_checks++;
    ok(same(F(a),F(b)),'observation mismatch');
    if(!d)return;
    for(const op of ACT){
      const aa=step(a,op,cap),bb=step(b,op,cap);
      ok((aa===null)===(bb===null),'legality mismatch '+op);
      if(aa!==null)go(aa,bb,d-1);
    }
  }go(x,y,h);
}
function gadget(mask,k,L){
  let s='';
  for(let j=0;j<k;j++)s+=(mask&(1<<j))?'ABAA':'AABA';
  return word(s+'C'.repeat(L));
}
function run(){
  const stats={prefix_checks:0,composition_checks:0,history_pairs:0,trace_modes:0,tag_counterexample:false};
  const sample=[];
  for(let h=0;h<=3;h++)for(let k=1;k<=5;k++){
    const L=h+3,base=gadget(0,k,L),key=K(base,h);
    for(let mask=0;mask<2**k;mask++){
      const s=gadget(mask,k,L);
      ok(same(K(s,h),key),'signature collision failed');
      const c=s.slice(0,-L),t=s.slice(-L);
      ok(same(join(F(c),F(t)),F(s)),'composition');
      ok(edgeEnd(F(c),true)===c[0].v && edgeEnd(F(c),false)===c[c.length-1].v,'boundary extraction');
      stats.composition_checks++;
      for(const cap of [false,true]){traces(s,base,h,cap,stats);stats.trace_modes++;}
      stats.history_pairs++;
    }
    if(k===5)sample.push({h,k,n:4*k+L,distinct_histories_one_K:2**k});
  }
  const x=word('AABACCCC','OPOOOOOO'),y=word('ABAACCCC','OPOOOOOO');
  ok(same(F(x.slice(0,4)),F(y.slice(0,4))) && same(F(x),F(y)),'counterexample inputs');
  ok(!same(F(step(x,'DELETE_LAST_PUBLIC',false)),F(step(y,'DELETE_LAST_PUBLIC',false))),'counterexample output');
  stats.tag_counterexample=true;
  return {stage:'499-B',status:'ALL_ASSERTIONS_PASSED',
    model:'12-signed-X6-directions with 150 exact F counters; test paths use A,B,C',
    actions:ACT,h_values:[0,1,2,3],gadget_counts:[1,2,3,4,5],
    insert_semantics:['original_stage498_n_lt_8','uncapped_extension'],
    ...stats,sample,
    provenance_counterexample:{x:'AABACCCC',y:'ABAACCCC',source_tag:'P at position 2 (1-based)',first_separating_action:'DELETE_LAST_PUBLIC'},
    arithmetic:'exact integers',scope:'complete action tree for each generated paired history; not all possible native histories'};
}
if (typeof process !== 'undefined' && process.stdout) process.stdout.write(JSON.stringify(run(),null,2)+'\n'); else return JSON.stringify(run(),null,2)+'\n';
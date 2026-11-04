#!/usr/bin/env node
'use strict';
// Exact remaining-Euler pair transfer on the full 12-symbol native-X6 alphabet.
// F_n is a two-letter specialization; all counts are BigInt, edge-type weight 1.
const assert=require('node:assert/strict');
const D='ABCDEFGHIJKL'.split(''); // (+E1,-E1,+E2,-E2,...,+E6,-E6)
const A='A',B='B';
function vector(w){const z=Array(6).fill(0);for(const c of w){const i=D.indexOf(c);assert(i>=0);z[Math.floor(i/2)]+=i%2?-1:1;}return z;}
function inc(m,k,v=1n){m.set(k,(m.get(k)||0n)+v);}
function terminalKey(n,p,q){
  if(q.slice(-6)==='BAAAAA')return 'B|capped';
  if(p.slice(-3)==='AAA')return 'R|'+p.slice(-6)+'|'+q.slice(-6);
  const i=p.slice(-3)==='BAA'?n-2:p.slice(-3)==='ABA'?n-1:-1;
  assert(i>0);return 'F|'+i+'|'+q.slice(-7);
}
function transfer({firstP,firstQ,JP,JQ,targetK,endpointP,endpointQ,capP,capQ,terminal}){
  // JP,JQ: nonzero triples [source direction,target direction,multiplicity].
  function validate(first,J,endpoint){
    let total=1;const rest=[];
    for(const [a,b,c] of J){assert(D.includes(a)&&D.includes(b));assert(Number.isInteger(c)&&c>0);total+=c;for(let i=0;i<c;i++)rest.push(b);}
    assert.deepEqual(vector([first,...rest]),endpoint);
    return total;
  }
  const n=validate(firstP,JP,endpointP);
  assert.equal(validate(firstQ,JQ,endpointQ),n);
  const memo=new Map();let transitions=0;
  function walk(RP,RQ,pLast,qLast,miss,pt,qt){
    const state=[RP.join(','),RQ.join(','),pLast,qLast,miss,pt,qt].join('|');
    if(memo.has(state))return memo.get(state);
    const out=new Map();const remain=RP.reduce((a,b)=>a+b,0);
    assert.equal(remain,RQ.reduce((a,b)=>a+b,0));
    if(!remain){if(n-miss===targetK)inc(out,terminal(pt,qt));memo.set(state,out);return out;}
    for(let i=0;i<JP.length;i++)if(RP[i]&&JP[i][0]===pLast){
      for(let j=0;j<JQ.length;j++)if(RQ[j]&&JQ[j][0]===qLast){
        const x=JP[i][1],y=JQ[j][1],nm=miss+(x!==y);
        if(nm>n-targetK)continue;
        const p2=RP.slice(),q2=RQ.slice();p2[i]--;q2[j]--;transitions++;
        const tailP=(pt+x).slice(-capP),tailQ=(qt+y).slice(-capQ);
        for(const [key,count] of walk(p2,q2,x,y,nm,tailP,tailQ))inc(out,key,count);
      }
    }
    memo.set(state,out);return out;
  }
  const result=walk(JP.map(e=>e[2]),JQ.map(e=>e[2]),firstP,firstQ,+(firstP!==firstQ),firstP,firstQ);
  return {groups:result,states:memo.size,transitions};
}
function sparseFiber(n){
  return transfer({firstP:A,firstQ:A,
    JP:[[A,A,n-3],[A,B,1],[B,A,1]], JQ:[[A,A,n-5],[A,B,2],[B,A,2]],
    targetK:n-1,endpointP:[n-2,0,0,0,0,0],endpointQ:[n-4,0,0,0,0,0],
    capP:6,capQ:7,terminal:(p,q)=>terminalKey(n,p,q)});
}
function direct(n){
  const out=new Map();
  const edges=w=>{const c=new Map();for(let i=1;i<w.length;i++)c.set(w[i-1]+w[i],(c.get(w[i-1]+w[i])||0)+1);return c;};
  const expectedP=new Map([['AA',n-3],['AB',1],['BA',1]]);
  const expectedQ=new Map([['AA',n-5],['AB',2],['BA',2]]);
  for(let r=2;r<=n-3;r++)for(let s=r+2;s<=n-1;s++)for(const i of [r,s]){
    const p=A.repeat(i-1)+B+A.repeat(n-i),q=A.repeat(r-1)+B+A.repeat(s-r-1)+B+A.repeat(n-s);
    assert.deepEqual([...edges(p)].sort(),[...expectedP].sort());
    assert.deepEqual([...edges(q)].sort(),[...expectedQ].sort());
    assert.deepEqual(vector(p),[n-2,0,0,0,0,0]);
    assert.deepEqual(vector(q),[n-4,0,0,0,0,0]);
    assert.equal([...p].filter((x,j)=>x===q[j]).length,n-1);
    inc(out,terminalKey(n,p,q));
  }
  return out;
}
function verify(){
  const cross=transfer({firstP:A,firstQ:A,JP:[[A,'C',1],['C',A,1],[A,B,1],[B,A,1]],
    JQ:[[A,'C',1],['C',A,1],[A,B,1],[B,A,1]], targetK:3,
    endpointP:[2,1,0,0,0,0],endpointQ:[2,1,0,0,0,0],capP:5,capQ:5,terminal:()=> 'all'});
  assert.equal(cross.groups.get('all'),2n); // two opposite Euler-loop orders
  const all=[];let states=0,transitions=0,tot=0;
  for(let n=11;n<=100;n++){
    const dp=sparseFiber(n),enumerated=direct(n);
    const asArray=m=>[...m].map(([k,v])=>[k,v.toString()]).sort((a,b)=>a[0].localeCompare(b[0]));
    assert.deepEqual(asArray(dp.groups),asArray(enumerated));
    assert.equal(dp.groups.size,24);
    const sum=[...dp.groups.values()].reduce((a,b)=>a+b,0n);
    assert.equal(sum,BigInt((n-3)*(n-4)));
    const observed=[...dp.groups.values()].map(Number).sort((a,b)=>a-b);
    const formula=[(n-8)*(n-9),2*(n-8),...Array(6).fill(n-7),...Array(2).fill(n-8),...Array(14).fill(1)].sort((a,b)=>a-b);
    assert.deepEqual(observed,formula);
    all.push({n,history_pairs:sum.toString(),classes:dp.groups.size,states:dp.states,transitions:dp.transitions});
    states+=dp.states;transitions+=dp.transitions;tot+=Number(sum);
  }
  return {marker:'STAGE424B_FULL_X6_EULER_J_K_TRANSFER_PASS',
    frozen_science:{global:'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',em:'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',p000_blob:'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'},
    arithmetic:'exact integer typed-edge DP / BigInt, indistinguishable same-type edges have unit weight',
    independent_oracles:'explicit full-word enumeration of F_n with exact J, endpoint and K; separate cross-axis three-symbol Euler-loop test',
    cross_axis_example:{alphabet:'A=+E1,B=-E1,C=+E2 embedded into 12 signed X6 directions',targetK:3,paired_word_count:'2',dp_states:cross.states},
    n_range:[11,100],total_explicit_original_pairs:tot,total_dp_states:states,total_dp_transitions:transitions,
    snapshots:all.filter(x=>[11,12,16,20,30,50,75,100].includes(x.n)),all_n:all,
    evidence_status:'AUTHOR_EXECUTED_FINITE_EXACT; 24_CLASS_MINIMALITY_REUSES_UNREVIEWED_STAGE422'};
}
if(require.main===module)console.log(JSON.stringify(verify(),null,2));
module.exports={transfer,sparseFiber,direct,verify};

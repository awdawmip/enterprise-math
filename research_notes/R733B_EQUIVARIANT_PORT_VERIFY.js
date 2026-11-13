#!/usr/bin/env node
/** R733b — finite exact S5/S6 port coding and orbit certificate; node R733B_EQUIVARIANT_PORT_VERIFY.js */
'use strict';
function subs(n,k){const out=[];function walk(a,lo){if(a.length===k){out.push(a.join(''));return;}for(let i=lo;i<n;i++)walk([...a,String(i)],i+1);}walk([],0);return out;}
function arcs(n){const t=subs(n,3),out=[];for(const s of t)for(const d of t)if([...s].filter(x=>d.includes(x)).length===2)out.push({s,d});return out;}
function code5({s,d}){const l=[...s].find(x=>!d.includes(x)),e=[...d].find(x=>!s.includes(x)),o=[...'01234'].find(x=>!s.includes(x)&&!d.includes(x));return [[l,e],[o,l]];}
function perms(xs){if(!xs.length)return [[]];return xs.flatMap((x,i)=>perms(xs.filter((_,j)=>j!==i)).map(p=>[x,...p]));}
const five=arcs(5),six=arcs(6);
if(five.length!==60||six.length!==180)throw Error('arc population');
const codes=five.map(a=>JSON.stringify(code5(a)));
if(new Set(codes).size!==60)throw Error('five-port injectivity');
let equivarianceChecks=0;
for(const perm of perms(['0','1','2','3','4'])){
 const g=Object.fromEntries(perm.map((x,i)=>[String(i),x]));
 for(const a of five){
  const ag={s:[...a.s].map(x=>g[x]).sort().join(''),d:[...a.d].map(x=>g[x]).sort().join('')};
  const lhs=code5(ag),rhs=code5(a).map(pair=>pair.map(x=>g[x]));
  if(JSON.stringify(lhs)!==JSON.stringify(rhs))throw Error('equivariance');
  equivarianceChecks++;
 }
}
if(equivarianceChecks!==7200)throw Error('S5 missing checks');
const groups={};
for(const a of six){
 const l=[...a.s].find(x=>!a.d.includes(x)),e=[...a.d].find(x=>!a.s.includes(x));
 (groups[l+'>'+e]??=[]).push(a.s+'>'+a.d);
}
if(Object.keys(groups).length!==30||Object.values(groups).some(v=>v.length!==6||new Set(v).size!==6))
 throw Error('native S6 same-symbol six-fiber');
const result={schema:'R733B_EQUIVARIANT_PORT_CODE_CERT_V1',status:'PASS',
 finite_exact_marker:'R733B_EQUIVARIANT_PORT_CODE_EXACT_PASS',
 five_axis:{directed_arcs:60,local_ports:5,ordered_PASS_letters:2,distinct_codes:60,S5_permutations:120,covariance_checks:equivarianceChecks},
 six_axis:{directed_arcs:180,leave_enter_pairs:30,source_arcs_per_pair:6,
 stabilizer:'S2(common pair) x S2(outside pair), fixing only leave and enter labels'},
 theorem_scope:'strict stateless fixed-alphabet permutation-equivariant ordered PASS word; exact group-theoretic all-length proof in sibling note',
 native_force_event:'NOT_CONSTRUCTED'};
process.stdout.write(JSON.stringify(result,null,2)+'\n');

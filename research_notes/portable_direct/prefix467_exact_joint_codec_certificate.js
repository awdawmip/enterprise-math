// PREFIX-467 exact integer joint-history codec certificate, ECMAScript 2022 BigInt.
function main() {
 const check=(c,m)=>{if(!c)throw Error(m)};
 const letters=[['x',0,1,1n],['a',1,1,6n],['-a',1,-1,1n],
 ['b',2,1,12n],['-b',2,-1,1n],['c',3,1,18n],['-c',3,-1,1n],
 ['d',4,1,24n],['-d',4,-1,1n],['e',5,1,36n],['-e',5,-1,1n]];
 const zero=[0,0,0,0,0,0,0,0]; // s, five signed y, valuation A,C
 const key=(base,q)=>base.join(',')+'|'+q;
 const update=(base,q,step,n)=>{
  const [name,axis,sign]=step;
  if(name==='x'&&n>0&&q!==2)return null;
  const b=base.slice();
  if(axis===0)b[0]++;
  else {
   const v=base[axis],pair=(sign===1&&v<0)||(sign===-1&&v>0);
   if(pair){if(axis===2||axis===5)b[6]++;if(axis===4)b[6]+=2;
            if(axis===3||axis===5)b[7]++;}
   b[axis]+=sign;
  }
  const nq=name==='a'?1:(name==='b'&&q===1?2:0);
  return [b,nq];
 };
 const weight=(b,n)=>{
  const p0=n-b[0]-b.slice(1,6).reduce((a,v)=>a+Math.abs(v),0);
  check(p0>=0&&p0%2===0,'invalid pair parity');
  let w=6n**BigInt(p0/2)*2n**BigInt(b[6])*3n**BigInt(b[7]);
  for(let i=0;i<5;i++)w*=([6n,12n,18n,24n,36n][i]**BigInt(Math.max(0,b[1+i])));
  return w;
 };
 function direct(n){
  const out=new Map(),word=[];
  function dfs(prod){
   if(word.length===n){
    const plus=[0,0,0,0,0],minus=[0,0,0,0,0];let s=0;
    for(const step of word){if(step[1]===0)s++;else if(step[2]===1)plus[step[1]-1]++;else minus[step[1]-1]++;}
    const y=plus.map((v,i)=>v-minus[i]),p=plus.map((v,i)=>Math.min(v,minus[i]));
    const b=[s,...y,p[1]+2*p[3]+p[4],p[2]+p[4]];
    const q=n===0?2:(n>=2&&word[n-2][0]==='a'&&word[n-1][0]==='b'?2:(word[n-1][0]==='a'?1:0));
    check(weight(b,n)===prod,'independent direct product mismatch');
    const id=key(b,q);out.set(id,(out.get(id)||0n)+1n);return;
   }
   for(const t of letters){
    if(t[0]==='x'&&word.length>0&&!(word.length>=2&&word[word.length-2][0]==='a'&&word[word.length-1][0]==='b'))continue;
    word.push(t);dfs(prod*t[3]);word.pop();
   }
  }
  dfs(1n);return out;
 }
 const counts=[1n],masses=[1n];
 for(let n=1;n<=8;n++){
  counts[n]=10n*counts[n-1]+(n>=3?counts[n-3]:0n)+(n===1?1n:0n);
  masses[n]=101n*masses[n-1]+(n>=3?72n*masses[n-3]:0n)+(n===1?1n:0n);
 }
 const lines=['PREFIX467_EXACT_JOINT_CODEC_JS_CERTIFICATE_V1',
 'n B N_H1 F U one_q two_q three_q bits_H0 bits_H1 bits_H2 product3B ordered weighted_mass brute'];
 let states=new Map([[key(zero,2),{b:zero,q:2,z:1n}]]);const Bprev=[];
 for(let n=0;n<=8;n++){
  let count=0n,mass=0n;const groups=new Map();
  for(const item of states.values()){
   count+=item.z;mass+=item.z*weight(item.b,n);
   const k=item.b.join(','),g=groups.get(k)||{b:item.b,qs:new Set()};
   g.qs.add(item.q);groups.set(k,g);
  }
  check(count===counts[n]&&mass===masses[n],'series discrepancy n='+n);
  const B=groups.size,F=states.size;let U=0,three=0,two=0,one=0;
  const keys=[[],[],[]];
  for(const [k,g] of groups){
   const qs=[...g.qs].sort();
   if(qs.includes(2)&&qs.length>1)U++;
   if(qs.length===1)one++;else if(qs.length===2)two++;else three++;
   keys[0].push(k+'|0');
   for(const label of new Set(qs.map(q=>q===2?2:0)))keys[1].push(k+'|'+label);
   for(const q of qs)keys[2].push(k+'|'+q);
  }
  const H1=B+U;
  check(keys[0].length===B&&keys[1].length===H1&&keys[2].length===F,'class count mismatch');
  if(n>=2){
   check(U===Bprev[n-2],'universal U identity mismatch');
   const exc=[0,n-1,1,0,0,0,0,0].join(',');let exceptions=0;
   for(const [k,g] of groups)if(g.qs.has(2)&&g.qs.size===2){
    check(k===exc&&g.qs.has(1),'exceptional fiber mismatch');exceptions++;
   }
   check(exceptions===1&&three===U-1,'three-state fiber mismatch');
  }
  const bits=[];
  for(const arr of keys){
   arr.sort();const idx=new Map(arr.map((k,i)=>[k,i]));
   check(idx.size===arr.length,'noninjective codec');
   for(let i=0;i<arr.length;i++)check(arr[idx.get(arr[i])]===arr[i],'codec roundtrip');
   bits.push((arr.length-1).toString(2).length-(arr.length===1?1:0));
  }
  if(n<=5){
   const brute=direct(n);
   check(brute.size===states.size,'brute size mismatch');
   for(const [k,v] of states)check(brute.get(k)===v.z,'direct histogram mismatch at '+n);
  }
  lines.push([n,B,H1,F,U,one,two,three,...bits,3*B,count.toString(),mass.toString(),n<=5?'PASS':'DP_ONLY'].join(' '));
  Bprev.push(B);
  if(n===8)break;
  const next=new Map();
  for(const val of states.values())for(const t of letters){
   const k=update(val.b,val.q,t,n);if(k===null)continue;
   const id=key(k[0],k[1]),prev=next.get(id);
   if(prev)prev.z+=val.z;else next.set(id,{b:k[0],q:k[1],z:val.z});
  }
  states=next;
 }
 lines.push('ALL_CHECKS_PASS');
 return lines.join('\n')+'\n';
}
if(typeof module!=='undefined'&&require.main===module){process.stdout.write(main());}

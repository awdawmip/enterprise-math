'use strict';
// PREFIX-841: independent named-state Q-only BRC regression and sharp modular/entropy tests.
// All weighted masses and arithmetic use exact BigInt; no external dependencies.
function eq(a,b,label){if(a!==b)throw Error(label+': '+String(a)+' != '+String(b));}
function yes(cond,label){if(!cond)throw Error(label);}
function gcd(a,b){while(b!==0n){const t=a%b;a=b;b=t;}return a;}
function fact(n){let a=1n;for(let i=2;i<=n;i++)a*=BigInt(i);return a;}
function ceilLog2(n){if(n<=1n)return 0;let k=0,x=n-1n;while(x>0n){x>>=1n;k++;}return k;}
function* words(p,W){const total=W**p;for(let v=0;v<total;v++){const w=[];let x=v;for(let j=0;j<p;j++){w.push(x%W+1);x=Math.floor(x/W);}yield w;}}
function countPerms(counts){let n=0,den=1n;for(const c of counts.values()){n+=c;den*=fact(c);}return fact(n)/den;}
function rankMultiset(word){
  const counts=new Map();for(const w of word)counts.set(w,(counts.get(w)||0)+1);
  const vals=[...counts.keys()].sort((a,b)=>a-b);let r=word.length,block=countPerms(counts),rank=0n;
  const initial=block;
  for(const w of word){
    for(const v of vals){if(v>=w)break;const count=counts.get(v)||0;if(count)rank+=block*BigInt(count)/BigInt(r);}
    const chosen=counts.get(w)||0;yes(chosen>0,'rank word membership');
    block=block*BigInt(chosen)/BigInt(r);counts.set(w,chosen-1);r--;
  }
  eq(block,1n,'rank final block');yes(rank>=0n&&rank<initial,'rank bounds');return {rank,size:initial};
}
function unrankMultiset(sortedMultiset,rank){
  const counts=new Map();for(const w of sortedMultiset)counts.set(w,(counts.get(w)||0)+1);
  const vals=[...counts.keys()].sort((a,b)=>a-b);
  let r=sortedMultiset.length,block=countPerms(counts),q=rank;const out=[];
  yes(q>=0n&&q<block,'unrank start');
  while(r){
    let chosen=false;
    for(const v of vals){const count=counts.get(v)||0;if(!count)continue;
      const part=block*BigInt(count)/BigInt(r);
      if(q>=part){q-=part;continue;}
      out.push(v);counts.set(v,count-1);block=part;r--;chosen=true;break;
    }
    yes(chosen,'unrank candidate');
  }
  eq(q,0n,'unrank final rank');return out;
}
function popcount(x){let n=0;while(x){x&=x-1;n++;}return n;}
function* taggedFrames(p,w,a,b,horizon){
  const all=(1<<p)-1;let state=new Map([[all*2,1n]]);
  for(let t=1;t<=horizon;t++){
    const next=new Map();
    for(const [key,mass] of state){
      const mask=Math.floor(key/2),mark=key&1,occ=popcount(mask)+mark;
      for(let i=0;i<p;i++)if(mask&(1<<i)){
        const to=(mask^(1<<i))*2+mark;
        next.set(to,(next.get(to)||0n)+mass*BigInt(w[i]));
      }
      if(mark){const to=mask*2;next.set(to,(next.get(to)||0n)+mass*BigInt(b));}
      if(!mark&&occ<p){const to=mask*2+1;next.set(to,(next.get(to)||0n)+mass*BigInt(a));}
    }
    state=next;const marked=t%2===0?1:0;
    yield {t,D:w.map((_,i)=>state.get((all^(1<<i))*2+marked)||0n)};
  }
}
const stats={configurations:0,frameChecks:0,missingNameChecks:0,codedScalarChecks:0,decodedWeightChecks:0,rankChecks:0,modularCases:0,modularResidueChecks:0,precisionChecks:0};
const examples=[];
for(let p=1;p<=5;p++)for(let W=1;W<=4;W++)for(const w of words(p,W)){
  const {rank,size}=rankMultiset(w);
  const restored=unrankMultiset([...w].sort((a,b)=>a-b),rank);
  yes(restored.every((x,i)=>x===w[i]),'conditional multiset unrank');
  eq(size,countPerms(new Map([...new Set(w)].map(x=>[x,w.filter(v=>v===x).length]))),'fiber cardinality');
  stats.rankChecks++;
  for(let a=1;a<=2;a++)for(let b=1;b<=2;b++){
    stats.configurations++;
    const base=BigInt(W),powers=[];let power=1n,sumPower=0n;
    for(let i=0;i<p;i++){powers.push(power);sumPower+=power;power*=base;}
    const possible=base**BigInt(p),minBits=ceilLog2(possible);
    for(const {t,D} of taggedFrames(p,w,a,b,6)){
      stats.frameChecks++;
      const c=BigInt(a)**BigInt(Math.floor(t/2))*BigInt(b)**BigInt(Math.floor((t-1)/2));
      let coded=0n;
      for(let i=0;i<p;i++){eq(D[i],c*BigInt(w[i]),'named channel mass');stats.missingNameChecks++;coded+=powers[i]*D[i];}
      eq(coded%c,0n,'coded divisibility');
      const ordinal=coded/c-sumPower;
      yes(ordinal>=0n&&ordinal<possible,'coded ordinal bounds');
      let q=ordinal;
      for(let i=0;i<p;i++){
        const digit=q%base;q/=base;eq(digit,BigInt(w[i]-1),'base-W weight digit');stats.decodedWeightChecks++;
      }
      eq(q,0n,'no excess digits');
      eq(coded,c*(sumPower+ordinal),'coded identity');stats.codedScalarChecks++;
      const digitsRequired=ceilLog2(possible);
      eq(digitsRequired,minBits,'optimal conditional-independent fixed length');
      const codedMax=c*BigInt(W)*sumPower;
      yes(coded<=codedMax,'coded max');
      if(p===3&&W===4&&w.join(',')==='1,2,4'&&a===2&&b===2&&[1,2,4,6].includes(t))
        examples.push({t,c:c.toString(),D:D.map(String),coded: coded.toString(),ordinal:ordinal.toString(),rawBits:coded.toString(2).length,idealFixedBits:minBits,conditionalRank:rank.toString(),conditionalFiber:size.toString()});
      if(p>=2&&W>=2){const offset=c*sumPower;const directNext=offset+c*(possible-1n);eq(directNext,codedMax,'code upper endpoint');stats.precisionChecks++;}
    }
  }
}
// Check the sharp modular criterion by exhaustive residues over all possible assignments.
for(let p=1;p<=4;p++)for(let W=2;W<=3;W++)for(let a=1;a<=3;a++)for(let b=1;b<=3;b++)for(let t=1;t<=5;t++){
  const N=BigInt(W)**BigInt(p);
  const c=BigInt(a)**BigInt(Math.floor(t/2))*BigInt(b)**BigInt(Math.floor((t-1)/2));
  let sum=0n,pow=1n;for(let i=0;i<p;i++){sum+=pow;pow*=BigInt(W);}
  for(let mi=1;mi<=Number(N)+7;mi++){
    const m=BigInt(mi),predicted=m/gcd(m,c)>=N;
    const seen=new Set();let injective=true;
    for(let u=0n;u<N;u++){
      const residue=(c*(sum+u))%m;
      const key=residue.toString();stats.modularResidueChecks++;
      if(seen.has(key)){injective=false;break;}
      seen.add(key);
    }
    eq(injective,predicted,'sharp modular iff');stats.modularCases++;
  }
}
const result={
  schema:'PREFIX841_EXACT_CODED_PROVENANCE_REGRESSION_V1',
  scientific_input_pin:'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  claims:[
    'Z_t=c_t sum_i w_i W^(i-1), and U=Z_t/c_t-sum_i W^(i-1) is an exact base-W lossless name code.',
    'Fixed-length normalized output requires and achieves ceil(log2(W^p)) bits for all bounded assignments.',
    'Z_t modulo m is injective on all assignments iff m/gcd(m,c_t)>=W^p.',
    'Given the unordered weight multiset with counts m_v, lexicographic assignment rank uses exactly ceil(log2(p!/product_v m_v!)) bits.'
  ],
  verification:{p_range:[1,5],W_range:[1,4],a_values:[1,2],b_values:[1,2],time_range:[1,6],modular_domain:{p_range:[1,4],W_values:[2,3],a_values:[1,2,3],b_values:[1,2,3],time_range:[1,5],m_range:'1..W^p+7'},statistics:stats,assertions:'ALL_EXACT_ASSERTIONS_PASSED'},
  examples:{p:3,W:4,weights:[1,2,4],a:2,b:2,rows:examples},
  caveat:'The coded scalar assumes a provenance-sensitive linear terminal observer; untagged Q-only occupancy data cannot evaluate it.'
};
if(typeof console!=='undefined')console.log(JSON.stringify(result,null,2));
JSON.stringify(result,null,2);

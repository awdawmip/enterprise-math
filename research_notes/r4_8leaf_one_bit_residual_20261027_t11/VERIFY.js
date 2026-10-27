// Exact integer finite observer certificate; auxiliary positive-mass BRC observation tree.
// P/Q units: 1/16; time price c=1/16; score units: 1/256.
// Order: UA+,UA-,UB+,UB-,VC+,VC-,VD+,VD-.
// Actions: 0 stop/reject, 1 stop/accept, 2 continue.
const P=[2,2,3,1,2,2,2,2],Q=[2,2,1,3,2,2,2,2];
function observer(s1,s2,terminal) {
 let a=0,b=0,tp=0,tq=0;
 for(let i=0;i<8;i++) {
   let d=s1[i<4?0:1],t=1;
   if(d===2) {
     d=s2[Math.floor(i/2)];t=2;
     if(d===2) {d=terminal[i];t=3;}
   }
   if(d===1) {a+=P[i];b+=Q[i];}
   tp+=P[i]*t;tq+=Q[i]*t;
 }
 return [a,b,tp,tq]; // all numbers are sixteenths
}
function score(o) {return 16*(o[0]-o[1])-o[2]-o[3];} // numerator over 256
function markovizedOneBit(s1,s2,term) {
 // Stage 1 bit records U/V; stage 2 bit separates UB from UA,VC,VD.
 // Stage 3 LR is 3 on UB+, 1/3 on UB-, 1 on all neutral leaves.
 let a=0,b=0,tp=0,tq=0;
 for(let h=0;h<2;h++) {
   if(s1[h]===2)continue;
   if(s1[h]===1){a+=8;b+=8;}
   tp+=8;tq+=8;
 }
 const g=[0,2,3].filter(j=>s1[j<2?0:1]===2);
 const w=4*g.length;
 if(w) {
   let st0=0,st1=0,ct=0,acceptNeutralTerminal=0;
   for(const j of g){
     if(s2[j]===0)st0++;
     if(s2[j]===1)st1++;
     if(s2[j]===2){ct++;acceptNeutralTerminal+=term[2*j]+term[2*j+1];}
   }
   // pooled randomized t=2 bit-0 kernel has masses 4*counts/w
   if(st0+st1+ct!==g.length)throw Error('bad partition');
   a+=4*st1;b+=4*st1;
   tp+=8*(st0+st1)+12*ct;
   tq+=8*(st0+st1)+12*ct;
   // pooled terminal LR=1 acceptance: acceptNeutralTerminal/(2*ct).
   if(ct){a+=2*acceptNeutralTerminal;b+=2*acceptNeutralTerminal;}
 }
 if(s1[0]===2){
   const d=s2[1]; // UB
   if(d===2){
     tp+=12;tq+=12;
     a+=3*term[2]+term[3];b+=term[2]+3*term[3];
   } else {
     tp+=8;tq+=8;
     if(d===1){a+=4;b+=4;}
   }
 }
 return [a,b,tp,tq];
}
function verify(){
 if(P.reduce((a,b)=>a+b,0)!==16||Q.reduce((a,b)=>a+b,0)!==16)throw Error('nonprobability');
 let countFull=0,bestFull=-Infinity,agree=0;
 for(let x=0;x<3**6;x++){
   let k=x,act=[];for(let z=0;z<6;z++){act.push(k%3);k=Math.floor(k/3);}
   const s1=act.slice(0,2),s2=act.slice(2,6);
   for(let mask=0;mask<256;mask++){
     const term=Array.from({length:8},(_,i)=>(mask>>i)&1);
     const o=observer(s1,s2,term),m=markovizedOneBit(s1,s2,term);
     if(o.some((v,i)=>v!==m[i]))throw Error('one-bit vector mismatch '+x+'/'+mask);
     agree++;countFull++;bestFull=Math.max(bestFull,score(o));
   }
 }
 let countLR=0,bestLR=-Infinity;
 for(let x=0;x<3;x++)for(let y=0;y<3;y++)
 for(let mask=0;mask<8;mask++){
    const s1=[x,x],s2=[y,y,y,y];
    const term=[(mask>>1)&1,(mask>>1)&1,(mask>>2)&1,mask&1,(mask>>1)&1,(mask>>1)&1,(mask>>1)&1,(mask>>1)&1];
    bestLR=Math.max(bestLR,score(observer(s1,s2,term)));countLR++;
 }
 const witness=observer([2,0],[0,2,0,0],[0,0,1,0,0,0,0,0]);
 if(countFull!==186624||countLR!==72||agree!==countFull)throw Error('incomplete exhaustive coverage');
 if(bestFull!==-24||bestLR!==-32||score(witness)!==-24)throw Error('wrong optimum');
 if(witness.join()!=='3,1,28,28')throw Error('wrong four-vector');
 return {normalization:'P=Q=16/16',full_deterministic_count:countFull,lr_deterministic_count:countLR,
   one_bit_vector_matches:agree,full_optimum_scaled_256:bestFull,lr_optimum_scaled_256:bestLR,
   exact_gap:'1/32',full_witness:['3/16','1/16','7/4','7/4'],checks:'PASS',
   arithmetic:'integer exact; no floating-point or native X6 calculation'};
}
if(typeof module!=='undefined'&&require.main===module)console.log(JSON.stringify(verify(),null,2));

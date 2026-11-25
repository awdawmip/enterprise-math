from pathlib import Path
s=Path('sat_token.cpp').read_text().replace('satPrunes=0;', 'satPrunes=0,firstChecks=0,firstDrops=0,firstEmpty=0;')
needle='       if(!can(can,all,k-b)){++satPrunes;return mem.emplace(key,-1).first->second;}'
patch=r'''
       // Fixed-first conditional saturation test. Only b=k or b=k-1.
       // The child has b' = b - paid; remaining token budget k-1-b'.
       for(int j=0;j<M;j++){
         if(j&&s.c[j]==s.c[j-1])continue;
         int bit=1<<j;bool normal=!(h&bit);
         for(int r=0;r<10;r++)if(allowR[j]>>r&1){
           ++firstChecks;
           bool positive=(u>>r&1)&&normal;
           bool paid=(u>>r&1)&&(o&bit);
           int op=o&~(paid?bit:0),rem=k-1-b+paid;
           bool ok=false;
           if(rem>=0){
             W rivals=0;array<W,10> rr{};array<W,M> ll{};
             for(int z=0;z<(int)ids.size();z++)if(z!=i){
               int v=F[ids[z]],c=B[z];bool active=v>>r&1;
               if(positive){if(!active||(c&bit))continue;}
               else if(active){if(!(A[z]&bit))continue;c|=bit;}
               if(pc(c|op)>H)continue;
               W zbit=W(1)<<z;rivals|=zbit;
               if(rem){
                 for(int d=u^v;d;d&=d-1)rr[__builtin_ctz(d)]|=zbit;
                 for(int d=c&~h;d;d&=d-1)ll[__builtin_ctz(d)]|=zbit;
               }
             }
             ok=!rivals;
             if(!ok&&rem==1){
               for(int t=0;t<10&&!ok;t++){
                 if(rr[t]==rivals){ok=true;break;}
                 if(u>>t&1)for(int c=0;c<M;c++)if(!(h>>c&1)&&((rr[t]|ll[c])==rivals)){ok=true;break;}
               }
             }
           }
           if(!ok){allowR[j]&=~(1<<r);++firstDrops;}
         }
       }
       bool any=false;for(int j=0;j<M;j++)if((!j||s.c[j]!=s.c[j-1])&&allowR[j])any=true;
       if(!any){++firstEmpty;return mem.emplace(key,-1).first->second;}
'''
assert s.count(needle)==1
s=s.replace(needle,needle+patch).replace('<<v.satPrunes<<endl','<<v.satPrunes<<","<<v.firstChecks<<","<<v.firstDrops<<","<<v.firstEmpty<<endl')
Path('sat_first.cpp').write_text(s)

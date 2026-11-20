// R762HI exact exhaustive Port-census and signed/coloured-factor cross-check.
// Based at Port 01; distinct event occurrences are never deduplicated.
// Compile: c++ -O3 -std=c++17 R762HI_CHECK.cpp -o R762HI_CHECK && ./R762HI_CHECK
#include <bits/stdc++.h>
using namespace std;
struct Row {
 unsigned long long closed=0,parity=0,signedTotal=0,qualAny=0,qualAll6=0,goodAll6=0;
 unsigned long long distribution[7]{},byAxis[6]{};
};
int ports[15],adj[15][8],supports[15][8],word[8];
int main(){
 int n=0;
 for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)ports[n++]=(1<<i)|(1<<j);
 for(int i=0;i<15;i++){
  int k=0;
  for(int j=0;j<15;j++)if(__builtin_popcount((unsigned)(ports[i]&ports[j]))==1){
   adj[i][k]=j; supports[i][k++]=ports[i]|ports[j];
  }
  assert(k==8);
 }
 for(int m:{2,4,6,8}){
  Row row;
  auto dfs=[&](auto&& self,int t,int node,int parity,int unionMask)->void{
   if(t==m){
    if(node!=0)return;
    row.closed++;
    if(parity)return;
    row.parity++;
    int cGood=0;
    for(int c=0;c<6;c++){
     int odds=0;
     for(int t0=0;t0<m;t0++)if(word[t0]&(1<<c))odds^=(word[t0]&~(1<<c));
     if(odds==0){cGood++;row.byAxis[c]++;}
    }
    row.distribution[cGood]++;
    if(cGood)row.qualAny++;
    if(unionMask==63){row.goodAll6++;if(cGood)row.qualAll6++;}
    int d[6]{},ed[6]{},types=0,E[8]{},typ[8]{};
    for(int t0=0;t0<m;t0++){
     int S=word[t0];
     for(int i=0;i<6;i++)d[i]+=(S>>i)&1;
     typ[t0]=S&1;
     E[t0]=typ[t0]?(S&~1):(62&~S);
     types+=!!typ[t0];
     for(int i=1;i<6;i++)ed[i]+=(E[t0]>>i)&1;
    }
    assert(types%2==0);
    for(int i=0;i<6;i++)assert(d[i]%2==0);
    for(int i=1;i<6;i++)assert(ed[i]%2==0);
    int direct=0,coef=0;
    for(int B=0;B<(1<<m);B++){
     if(__builtin_popcount((unsigned)B)!=m/2)continue;
     int v[6]{},e[6]{},mark=0;
     for(int t0=0;t0<m;t0++)if((B>>t0)&1)
      for(int i=0;i<6;i++)v[i]+=(word[t0]>>i)&1;
     bool valid=true;
     for(int i=0;i<6;i++)if(v[i]!=d[i]/2){valid=false;break;}
     direct+=valid;
     for(int t0=0;t0<m;t0++)if((B>>t0)&1){
      mark+=!!typ[t0];
      for(int i=1;i<6;i++)e[i]+=(E[t0]>>i)&1;
     }
     valid=mark==types/2;
     for(int i=1;i<6;i++)if(e[i]!=ed[i]/2)valid=false;
     coef+=valid;
    }
    if(direct!=coef){cerr<<"FAIL factor mismatch m="<<m<<"\n";abort();}
    if(direct==0){cerr<<"FAIL parity saturation m="<<m<<"\n";abort();}
    row.signedTotal+=direct;
    return;
   }
   for(int k=0;k<8;k++){
    word[t]=supports[node][k];
    self(self,t+1,adj[node][k],parity^word[t],unionMask|word[t]);
   }
  };
  dfs(dfs,0,0,0,0);
  cout<<"m="<<m<<" closed="<<row.closed<<" parity="<<row.parity
      <<" signed="<<row.signedTotal<<" any_layer="<<row.qualAny
      <<" all6_support="<<row.goodAll6<<" any_layer_all6="<<row.qualAll6
      <<" by_qualifying_axes=";
  for(int j=0;j<=6;j++)cout<<(j?",":"")<<row.distribution[j];
  cout<<" by_fixed_axis=";
  for(int j=0;j<6;j++)cout<<(j?",":"")<<row.byAxis[j];
  cout<<"\n";
 }
 cerr<<"PASS: all named Port walks of lengths 2,4,6,8; exact multiplicity matches graph factor\n";
}

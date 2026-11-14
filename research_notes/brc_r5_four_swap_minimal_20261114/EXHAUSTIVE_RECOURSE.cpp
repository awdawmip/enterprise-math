#include <bits/stdc++.h>
using namespace std;
struct Opt { int cost=INT_MAX; vector<int> sets; };
vector<Opt> optima(const vector<int>& x){
 int n=x.size(); vector<Opt> out(n+1);
 for(int m=1;m<(1<<n);m++){
  int k=__builtin_popcount((unsigned)m),cost=0; bool ok=true;
  for(int i=0;i<n;i++){
   int d=INT_MAX;
   for(int j=0;j<n;j++)if(m&(1<<j)){d=min(d,abs(x[i]-x[j]));if(d==0)break;}
   if(d>2){ok=false;break;}cost+=d;
  }
  if(!ok)continue;
  if(cost<out[k].cost){out[k].cost=cost;out[k].sets.clear();out[k].sets.push_back(m);}
  else if(cost==out[k].cost)out[k].sets.push_back(m);
 }
 return out;
}
int main(int argc,char **argv){int mxn=argc>1?atoi(argv[1]):9;long long total=0,checks=0;int globalmax=0;for(int n=2;n<=mxn;n++){
 long long sequences=1;for(int i=1;i<n;i++)sequences*=3;
 long long transitions=0,checked=0;
 int maximum=0;vector<int> witnessx,witnessy; int wk=0,wold=0,wnew=0,wcut=-1;
 for(long long word=0;word<sequences;word++){
  vector<int> x(n),g(n-1);long long q=word; for(int j=0;j<n-1;j++){g[j]=q%3+1;q/=3;x[j+1]=x[j]+g[j];}
  if(find(g.begin(),g.end(),3)==g.end())continue;
  auto old=optima(x);
  for(int cut=0;cut<n-1;cut++)if(g[cut]==3){transitions++;vector<int> y=x;for(int i=cut+1;i<n;i++)y[i]--;auto ne=optima(y);
   for(int k=1;k<=n;k++)if(old[k].cost==ne[k].cost && ne[k].cost<INT_MAX){
    for(int s:ne[k].sets){checked++;int best=0,oldmask=0;
     for(int t:old[k].sets){int v=__builtin_popcount((unsigned)(t&s));if(v>best){best=v;oldmask=t;if(best==k)break;}}
     int r=k-best;if(r>maximum){maximum=r;wk=k;wold=oldmask;wnew=s;witnessx=x;witnessy=y;wcut=cut;}
    }
   }
  }
 }
 cout<<"n="<<n<<" words="<<sequences<<" transitions="<<transitions<<" compared="<<checked<<" maxRho="<<maximum<<"\n";
 if(maximum){cout<<" first_max_witness x=";for(auto v:witnessx)cout<<v<<",";cout<<" y=";for(auto v:witnessy)cout<<v<<",";cout<<" cut="<<wcut<<" k="<<wk<<" oldMask="<<wold<<" newMask="<<wnew<<"\n";}
 total+=transitions;checks+=checked;globalmax=max(globalmax,maximum);
 }
 cout<<"TOTAL transitions="<<total<<" checked="<<checks<<" max="<<globalmax<<"\n";
}

// BRC Q=1 T=4: exhaustive S6+swap orbit test of all clipped pair states.
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;constexpr int N=6,M=64;using A=array<uint8_t,N>;
struct K{U a,b;bool operator==(const K&x)const{return a==x.a&&b==x.b;}};
struct H{size_t operator()(const K&x)const{return x.a*0x9e3779b97f4a7c15ULL^std::rotl(x.b,21);}};
struct Checker {
 U trans[2][N][2][M]{};U bad[2]{};
 Checker(A a,A b){A ds[2]{a,b};
  for(int k=0;k<2;k++){int w[M]{};
   for(int m=1;m<M;m++){int i=__builtin_ctz(m);w[m]=w[m&(m-1)]+ds[k][i];}
   for(int m=0;m<M;m++){if(w[m]==0)bad[k]|=U(1)<<m;
    for(int j=0;j<N;j++)for(int i=0;i<N;i++)if(i!=j){
      int z=m&~(1<<i),fb=w[z]>=4;trans[k][j][fb][m]|=U(1)<<z;
    }
   }
  }
 }
 pair<U,U> next(int k,U bits,int j)const{
  U x=0,y=0;while(bits){int i=__builtin_ctzll(bits);bits&=bits-1;
   x|=trans[k][j][0][i];y|=trans[k][j][1][i];}return {x,y};
 }
 bool dir(int safe)const{
  int other=1-safe;U start=U(1)<<63;
  if(start&bad[safe])return false;if(start&bad[other])return true;
  vector<pair<K,int>>q;unordered_set<K,H>seen;
  q.push_back({{start,start},0});seen.insert({start,start});
  for(size_t t=0;t<q.size();t++){
   K node=q[t].first;int dep=q[t].second;if(dep>=N)continue;
   for(int j=0;j<N;j++){
    auto x=next(safe,node.a,j);if((x.first|x.second)&bad[safe])continue;
    auto y=next(other,node.b,j);
    if((y.first|y.second)&bad[other])return true;
    if(y.first){K v{x.first,y.first};if(seen.insert(v).second)q.push_back({v,dep+1});}
    if(y.second){K v{x.second,y.second};if(seen.insert(v).second)q.push_back({v,dep+1});}
   }
  }
  return false;
 }
 bool distinct()const{return dir(0)||dir(1);}
};
long long total=0,equal=0,diff=0,separated=0,exception=0;
void check(const vector<int>& codes){
 vector<int> rev=codes;
 for(int &x:rev)x=5*(x%5)+x/5;
 sort(rev.begin(),rev.end());if(codes>rev)return;
 total++;A x{},y{};for(int i=0;i<N;i++){x[i]=codes[i]/5;y[i]=codes[i]%5;}
 int wx[M]{},wy[M]{};bool same=true;
 for(int m=1;m<M;m++){int i=__builtin_ctz(m);
  wx[m]=wx[m&(m-1)]+x[i];wy[m]=wy[m&(m-1)]+y[i];
  if((wx[m]>=1)!=(wy[m]>=1)||(wx[m]>=4)!=(wy[m]>=4))same=false;
 }
 if(same){equal++;return;}diff++;
 if(Checker(x,y).distinct())separated++;
 else {exception++;for(int v:x)cout<<int(v);cout<<"/";for(int v:y)cout<<int(v);cout<<"\n";}
}
void recurse(int from,vector<int>&a){
 if(int(a.size())==N){check(a);return;}
 for(int c=from;c<25;c++){a.push_back(c);recurse(c,a);a.pop_back();}
}
int main(){vector<int>a;recurse(0,a);
 cerr<<"total="<<total<<" equal="<<equal<<" distinct="<<diff<<" separated="<<separated<<" exception="<<exception<<"\n";
 assert(total==297865&&equal==589&&diff==297276&&separated==297272&&exception==4);
}

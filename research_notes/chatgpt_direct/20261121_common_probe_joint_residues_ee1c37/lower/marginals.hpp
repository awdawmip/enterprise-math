using Shape=std::array<std::array<int,5>,3>;
using Bounds=std::array<int,125>;
Shape shape(M f){
 Shape h{};for(int j=0;j<15;++j){M m=f&slices[j];h[j/5][j%5]=__builtin_popcountll((uint64_t)m)+__builtin_popcountll((uint64_t)(m>>64));}
 for(auto&x:h)sort(x.begin(),x.end(),greater<int>());return h;
}
void projection(Shape row,Bounds& out){
 int pref[3][5]{};
 for(int a=0;a<3;++a)for(int i=1;i<5;++i)pref[a][i]=pref[a][i-1]+row[a][i-1];
 for(int i=0;i<5;++i)for(int j=0;j<5;++j)for(int k=0;k<5;++k)out[i*25+j*5+k]=pref[0][i]+pref[1][j]+pref[2][k];
}
vector<Bounds> shape_max;
vector<Bounds> level_bound[13];
Bounds bound_at[13];
void prepare_bounds(){
 shape_max.resize(types.size());
 for(int i=0;i<types.size();i++){
  std::set<Shape> unique;
  for(M r:types[i].reps){Shape h=shape(r);sort(h.begin(),h.end());do{unique.insert(h);}while(next_permutation(h.begin(),h.end()));}
  shape_max[i].fill(0);
  for(const auto&h:unique){Bounds v;projection(h,v);for(int j=0;j<125;j++)shape_max[i][j]=max(shape_max[i][j],v[j]);}
 }
}
bool possible(M f, const Bounds&lim){
 Shape h=shape(f);int p[3][5]{};for(int j=0;j<3;j++)for(int i=1;i<5;i++)p[j][i]=p[j][i-1]+h[j][i-1];
 for(int a=0;a<5;a++)for(int b=0;b<5;b++){int v=p[0][a]+p[1][b];for(int c=0;c<5;c++)if(v+p[2][c]>lim[25*a+5*b+c])return false;}
 return true;
}

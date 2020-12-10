# Mesh_Contour  

STL ファイル（アスキー）から、輪切りの線を数値計算するライブラリ。  

計算量を減らすために、各メッシュの Z 座標の最大最小を取得し、輪切りに関係するメッシュだけ選び出し計算する。  
各メッシュと、輪切りの切断面の平面の交差線は、Möller–Trumbore intersection algorithm で、計算。  


### Related Projects  

- GH_Renderer  
  // リストで出力される計算結果を Grasshopper に出力するライブラリ。  
  [https://github.com/naysok/GH_Renderer](https://github.com/naysok/GH_Renderer)  


### Ref  

- レイと三角形の交差判定（Pheemaの学習帳）  
  [https://pheema.hatenablog.jp/entry/ray-triangle-intersection](https://pheema.hatenablog.jp/entry/ray-triangle-intersection)  

- Möller–Trumbore intersection algorithm（Wikipedia）  
  [https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm](https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm)  

- Pythonの計算機イプシロン（Qiita）  
  [https://qiita.com/ikuzak/items/1332625192daab208e22](https://qiita.com/ikuzak/items/1332625192daab208e22)  

- 3DBenchy - The jolly 3D printing torture-test by CreativeTools.se (Thingiverse)  
  [https://www.thingiverse.com/thing:763622](https://www.thingiverse.com/thing:763622)  

- Stanford Bunny（thingiverse）  
  [https://www.thingiverse.com/thing:3731](https://www.thingiverse.com/thing:3731)  
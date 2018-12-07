ディレクトリ
video:取得した動画を保存
picture:取得した写真を保存
rawImage:バイナリデータから抽出したJPEGを一時的においておく場所
get_data:天気予報やニュースの取得・表示関係
　　|-get_data:インターネット上から情報を取得し表示するプログラム
　　|-news_get.txt:取得したニュースを保存する
　　|-weather_get.txt:取得した天気予報を表示する
　　|-bash:情報を取得するスクリプト
　　   |-news
　　   |-weather
　　   
grammer-kit-master:音声認識

home_data:家のデータ格納先
  |-data.txt:データ
  
png:天気予報の画像格納庫




プログラム
HomeHack_master.py:全体統括
HomeHack_main:音声認識結果を取得しマイコンズに命令を送る子
clock:TDN時計
GetHomeData.py:Arduinoから来た家の情報（マイコンから送られてきた情報すべて）を保存（./home_data/data.txt）する
DataFromHome:家のデータ（./home_data/data.txt）を表示する

get_video.py:バイナリデータからJPEGを取得、動画にしてvideosに保存
rec_fromGR.py:GRのカメラ画像データをバイナリとして保存
read:GRから来たバイナリデータを保存

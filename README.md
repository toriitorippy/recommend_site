# 居住エリアレコメンドアプリ「KOKOSUMU」

「KOKOSUMU」は、ユーザーの属性や価値観に基づいた住まい探しをサポートすることを目的としたWebアプリケーションです。

本アプリでは以下のような **「幸福度」** と **「成約率」** の2つの軸で、ユーザーにとって最適な居住エリアを提案します。
- いくつかの質問に対する回答結果を基に、ユーザーが東京都23区の各区に住んだ場合の将来的な「幸福度」を機械学習が予測します。
- ユーザーが希望する家賃額、各区の家賃相場額および空室率のデータを基に、各区での希望物件の見つかりやすさを表す指標である「成約率」を算出します。

アプリの結果画面イメージは下図の通りです。すべての区に対する、ユーザーにとっての「幸福度」と「成約率」をプロットした図を示しています。
ユーザーは自分の趣向に合わせて、「幸福度」と「成約率」のバランスを見ながら好みの区を選ぶことができます。

「KOKOSUMU」は[こちら](https://kokosumu.azurewebsites.net/)からご利用いただけます。

![app result](https://user-images.githubusercontent.com/51290788/156872823-0d5e86ec-ce9d-4492-a29f-a552bdda4da2.png)

<!--
# KOKOSUMU

## KOKOSUMUについて
住むのに最適な街をユーザーの嗜好に合わせてレコメンドするWeb Applicationです。


## Github Pages
Vue側の静的ページをgithub pagesでデプロイしました。
url: [レコメンドシステム](https://toriitorippy.github.io/recommend_site/)

更新は
```
yarn build
yarn deploy
```
で行えばよい。
-->

# EC Price Comparison System

Amazon・楽天市場・Yahoo!ショッピングの価格情報を比較し、
EC運営における商品リサーチと仕入れ判断を支援する業務改善システムです。

---

# 概要（Overview）

本システムは、EC運営における価格比較・利益計算・商品リサーチ業務を効率化するために開発しました。

従来は複数のECサイトを巡回し、価格をExcelへ転記して利益計算を行っていましたが、商品数の増加に伴い手作業での運用が困難になりました。

そこでPythonを用いて価格取得から利益計算までを自動化し、既存のExcel運用を活かしたまま業務効率化を実現しました。

本リポジトリはポートフォリオ公開用に再構成したデモ版です。

---

# 主な機能（Features）

- Amazon価格取得
- 楽天市場価格取得
- Yahoo!ショッピング価格取得
- 商品情報取得
- 利益計算
- Excelレポート出力
- 商品候補の抽出支援

---

# 業務フロー（Workflow）

商品リスト（Keepa・卸CSV・JAN一覧）

↓

Pythonによるデータ処理

↓

Amazon・楽天市場・Yahoo!ショッピングから価格取得

↓

価格比較・利益計算

↓

Excelへ結果出力

↓

フィルター・ソート

↓

仕入れ判断

---

# 技術構成（Technology）

- Python
- Excel
- CSV
- REST API
- openpyxl

---

# ディレクトリ構成（Repository Structure）

```text
demo/
sample/
README.md
```

# 公開範囲（Notice）

本リポジトリはポートフォリオ公開用です。

実際の運用コード・APIキー・業務データ・利益判定ロジックなどは公開していません。

一部コードはデモ用に再構成しています。

---
## Demo

### Input

sample/sample_input.csv

↓

### Process

demo/price_comparison_demo.py

↓

### Output

sample/sample_output.xlsx

このリポジトリでは、実際の運用システムを簡略化したデモ版を公開しています。

## Repository Structure

```
demo/
sample/
README.md
```
# 今後の予定（Future）

システム構成図追加
スクリーンショット追加
UIイメージ追加
運用フロー図追加

---

# 作者（Author）

**A2E Works**

Field Tech Engineer

現場を理解し、業務を仕組みに変える。

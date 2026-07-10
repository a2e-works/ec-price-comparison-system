# ec-price-comparison-system
EC運営の価格比較・仕入れ判断業務を支援する業務改善システム

Amazon・楽天市場・Yahoo!ショッピングの価格情報を比較し、
大量の商品候補から仕入れ対象を効率的に抽出するための
業務改善支援システムです。

> **Field Tech Engineer の実務で使用していた業務改善ツールを、機密情報を除いた形で公開しています。**

---

## Overview

本システムは、EC運営における価格比較・利益計算・候補抽出を自動化するために開発しました。

当初はすべて手作業で行っていた価格調査をPythonで自動化し、
約10,000件の商品データから約300件まで候補を絞り込み、
最終的な仕入れ判断のみを人が行う運用を実現しました。

約3年間継続して改善を重ね、
年間約3,500万円規模のEC運営で活用しました。

---

## Features

- Amazon・楽天市場・Yahoo!ショッピングの価格比較
- 利益計算の自動化
- Excelレポート生成
- フィルター・ソートによる候補抽出
- 業務フローに合わせた運用設計

---

## Workflow

Keepa / 卸CSV / JAN一覧
↓
Python
↓
価格取得
↓
利益計算
↓
Excel出力
↓
仕入れ判断

---

## Technology

- Python
- Excel
- CSV Processing
- Workflow Automation

---

## Repository Structure

```
demo/
docs/
sample/
README.md
```

---

## Notice

本リポジトリはポートフォリオ公開用です。

実際の運用コード・APIキー・スクレイピング処理・業務データは公開していません。
一部のコードはデモ用に再構成しています。

---

## Author

A2E Works

Field Tech Engineer

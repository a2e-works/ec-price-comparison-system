# EC Profit Analyzer

Pythonで作成した、EC運営向けの価格比較・利益分析デモツールです。

商品情報をCSVで入力すると、複数ショップの価格比較を行い、
推定仕入価格と利益率をExcelレポートとして出力します。

---
## Quick Start

このデモは Windows 環境で動作します。

### 1. ダウンロード

GitHub の **Code** ボタンから **Download ZIP** を選択し、ZIPファイルを展開します。

### 2. デモ実行

`Run Demo.bat`

をダブルクリックしてください。

### 3. 実行結果

処理が完了すると、以下のExcelファイルが生成されます。

```
sample/sample_output.xlsx
```
## Overview

EC運営では、以下のような作業が日常的に発生します。

* 商品情報の整理
* 複数サイトの価格確認
* 仕入判断
* 利益計算
* Excelへの転記

本ツールは、このような繰り返し作業をPythonで自動化する
業務改善デモとして開発しました。

---

## Screenshots

### Input CSV

![Input CSV](screenshots/01_input_csv.png)

### Demo Execution

![Demo Execution](screenshots/02_demo_execution.png)

### Profit Analysis

![Profit Analysis](screenshots/03_output_csv.png)

## Features

### CSV商品リスト入力

商品情報をCSV形式で読み込みます。

Example:

```csv
JAN,Product
490000000001,USB-Cケーブル
490000000002,モバイルバッテリー
490000000003,LEDライト
```

---

### Price Comparison

複数ショップの価格を比較します。

Demo data:

* Amazon
* Rakuten
* Yahoo

---

### Profit Analysis

最安仕入価格を算出し、利益率を計算します。

Calculation:

```text
Profit Rate =
(Selling Price - Purchase Price)
/
Purchase Price
× 100
```

---

### Excel Report Generation

分析結果をExcelファイルとして出力します。

Output:

```text
sample/sample_output.xlsx
```

Included:

* Price comparison
* Cheapest purchase price
* Profit rate

---

## Demo Execution

Windows環境で動作確認できます。

1. GitHubの **Code** ボタンから **Download ZIP** を選択します。

2. ダウンロードしたZIPファイルを展開します。

3. フォルダ内の `Run Demo.bat` をダブルクリックします。

4. 処理完了後、`sample/sample_output.xlsx` が生成されます。

処理内容:

```text
CSV Input

↓

Python Processing

↓

Price Comparison

↓

Profit Calculation

↓

Excel Report
```

## Technology

* Python 3
* pandas
* openpyxl

---


## Requirements

- Windows 10 / 11
- Python 3.x
- Required packages: pandas, openpyxl

Install dependencies:

```bash
pip install -r requirements.txt
```

## Note

This repository contains a simplified demonstration version.

The production version can be extended with:

* API integration
* Database connection
* Business-specific rules
* Additional automation workflows

---
## Background

このツールは、EC運営業務で実際に行っていた価格調査・利益分析業務をもとに、
ポートフォリオ向けに再構成したデモ版です。

業務改善では、新しいシステムを導入することよりも、
現場の運用を理解し、無理なく改善できる仕組みづくりを重視しています。

---

**A2E Works**

*Practical automation tools for real-world workflows.*


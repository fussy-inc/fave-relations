# fave-relations

showing relations between your favorite things

## requirements
- rye

## Usage

### Setup

```bash
$ rye sync
```

### Execution

```bash
rye run python src/fave_relations/main.py && open example.html
```

## How does this work?

1. **Data Preparation**: CSVファイルの形式でデータを入力します。各行は、3つの異なるお気に入りのアイテム（`Fave`）を示しており、これは1人のユーザーが好きな3つのアイテムを示すと想定されます。

2. **Fave and Relation Object Creation**: 各アイテムとその間の関係を表すオブジェクトを作成します。`Fave`はアイテムを、`FaveRelation`は2つのアイテムの間の関係を表します。

3. **Counting Relations**: 同じユーザーが好きな2つのアイテムのペアごとに、その関係の頻度を数え上げます。

4. **Visualization**: 作成した関係を基に、ネットワーク図を作成します。アイテムはノードとして、関係はエッジとして表示されます。ノードのサイズは、そのアイテムを好きと答えたユーザーの数を反映し、エッジの太さはその2つのアイテムを共に好きと答えたユーザーの数を反映しています。

## Tips

- **Filtering and Selecting in the Visualization**: `pyvis`によって生成された可視化では、ノードやエッジのフィルタリング、選択が可能です。これにより、特定のアイテム間の関係を詳しく見ることができます。

- **Customizing Node Size**: `node_size`関数を調整することで、ノードのサイズを変更することが可能です。例えば、アイテムの人気度に基づいてノードのサイズを調整したい場合、この関数をカスタマイズします。

## Future Improvements

1. **Adding More Data**: 現在は3つのアイテムに制限されていますが、ユーザーが好きなアイテムの数に制限を設けずにデータを追加できるようにすること。

2. **Interactive Features**: ユーザーが可視化内で特定のアイテムや関係にコメントや注釈を追加できるようにする。

3. **Data Persistence**: 現在の実装では、データは一時的にメモリ上に保持されますが、データベースやクラウドストレージとの統合を通じてデータの永続性を確保すること。

このツールは、あなたのお気に入りのアイテムとそれらの間の関係を探索する新しい方法を提供します。楽しんでください！

import pandas as pd
import networkx as nx
from pyvis.network import Network
import io
from dataclasses import dataclass

@dataclass
class Fave:
    name: str
    count: int

    def __hash__(self) -> int:
        return hash(self.name)

def find_or_create_fave(
        faves: set[Fave],
        name: str
) -> Fave:
    for fave in faves:
        if fave.name == name:
            return fave
    fave = Fave(name, 0)
    faves.add(fave)
    return fave

def node_size(fave: Fave) -> int:
    # if fave.count < 5:
    #     return 10
    # elif fave.count < 10:
    #     return 20
    # else:
    #     return 30
    return fave.count * 5

@dataclass
class FaveRelation:
    source: Fave
    target: Fave
    weight: float

    def __hash__(self) -> int:
        return hash((self.source, self.target)) + hash((self.target, self.source))

def find_or_create_relation(
        relations: set[FaveRelation],
        source: Fave,
        target: Fave
) -> FaveRelation:
    for relation in relations:
        if (relation.source == source and relation.target == target) or (relation.source == target and relation.target == source):
            return relation
    relation = FaveRelation(source, target, 0)
    relations.add(relation)
    return relation

def relation_weight(relation: FaveRelation) -> float:
    return relation.weight * 10

df = pd.read_csv(io.StringIO('''
1,2,3
あらゐけいいち,真空ジェシカ,真っ白なキャンバス
推しの子,くりぃむしちゅー,シバタリアン
こちら葛飾区亀有公園前派出所,あらゐけいいち,くりぃむしちゅー
笹見つく音,ぼっち・ざ・ろっく！,BLACKPINK
ブラッシュアップライフ,満島ひかり,ドラゴンボール
姫様“拷問”の時間です,アフロ田中,茨木のり子
BTS,あらゐけいいち,マッシュル -MASHLE-
さらば青春の光,こちら葛飾区亀有公園前派出所,金色のガッシュ！！
少女時代,ONE PIECE,ケツメイシ
BTS,宇多田ヒカル,RDG レッドデータガール
ONE PIECE,サカナクション,Angel Beats!
バックドロップシンデレラ,SHIORI EXPERIENCE,宇多田ヒカル
金属バット,くりぃむしちゅー,サカナクション
新世紀エヴァンゲリオン,左ききのエレン,響け! ユーフォニアム
響け! ユーフォニアム,赤西仁,新世紀エヴァンゲリオン
バーバパパ,僕が見たかった青空,姫様“拷問”の時間です
範馬刃牙,らき☆すた,彼方のアストラ
ドラゴンボール,乃木坂46,新世紀エヴァンゲリオン
くりぃむしちゅー,響け! ユーフォニアム,さらば青春の光
姫様“拷問”の時間です,響け! ユーフォニアム,青春ブタ野郎シリーズ
真っ白なキャンバス,BTS,真空ジェシカ
OOPARTZ,RDG レッドデータガール,チェンソーマン
青春ブタ野郎シリーズ,真っ白なキャンバス,左ききのエレン
少年ジャンプ＋,カルテット,推しの子
少女時代,こちら葛飾区亀有公園前派出所,くりぃむしちゅー
真っ白なキャンバス,赤西仁,乃木坂46
らき☆すた,彼方のアストラ,新世紀エヴァンゲリオン
aiko,バックドロップシンデレラ,First Love 初恋
少女時代,ブラッシュアップライフ,SHIORI EXPERIENCE
少女時代,らき☆すた,櫻坂46
青春ブタ野郎シリーズ,最果タヒ,茨木のり子
バーバパパ,ラランド,RDG レッドデータガール
青春ブタ野郎シリーズ,乃木坂46,真っ白なキャンバス
真空ジェシカ,ONE PIECE,えなこ
ブラッシュアップライフ,推しの子,First Love 初恋
SHIORI EXPERIENCE,BTS,カルテット
チェンソーマン,バックドロップシンデレラ,バーバパパ
青春ブタ野郎シリーズ,推しの子,BTS
あらゐけいいち,アフロ田中,ぼっち・ざ・ろっく！
ブラッシュアップライフ,らき☆すた,真空ジェシカ
RDG レッドデータガール,First Love 初恋,ONE PIECE
aiko,こちら葛飾区亀有公園前派出所,バーバパパ
First Love 初恋,少女時代,OOPARTZ
左ききのエレン,BTS,櫻坂46
赤西仁,ブルージャイアント,僕が見たかった青空
BLACK LAGOON,ケツメイシ,らき☆すた
青春ブタ野郎シリーズ,少女時代,マッシュル -MASHLE-
金色のガッシュ！！,こちら葛飾区亀有公園前派出所,彼方のアストラ
響け! ユーフォニアム,シバタリアン,推しの子
First Love 初恋,真っ白なキャンバス,乃木坂46
こちら葛飾区亀有公園前派出所,くりぃむしちゅー,金属バット
マッシュル -MASHLE-,赤西仁,ONE PIECE
Angel Beats!,笹見つく音,ONE PIECE
'''))

faves = set()
relations = set()


for row in df.itertuples():
    first_fave = find_or_create_fave(faves, row[1])
    second_fave = find_or_create_fave(faves, row[2])
    third_fave = find_or_create_fave(faves, row[3])

    first_fave.count += 1
    second_fave.count += 1
    third_fave.count += 1

    first_relation = find_or_create_relation(relations, first_fave, second_fave)
    second_relation = find_or_create_relation(relations, first_fave, third_fave)

    first_relation.weight += 1
    second_relation.weight += 0.5


G = nx.Graph()

for fave in faves:
    G.add_node(fave.name, size=node_size(fave))

for relation in relations:
    G.add_edge(relation.source.name, relation.target.name, weight=relation_weight(relation))

net = Network()
net.from_nx(G)
net.select_menu = True
net.cdn_resources = "remote"
net.show("example.html", notebook=False)



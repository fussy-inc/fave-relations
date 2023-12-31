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


def find_or_create_fave(faves: set[Fave], name: str) -> Fave:
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
    relations: set[FaveRelation], source: Fave, target: Fave
) -> FaveRelation:
    for relation in relations:
        if (relation.source == source and relation.target == target) or (
            relation.source == target and relation.target == source
        ):
            return relation
    relation = FaveRelation(source, target, 0)
    relations.add(relation)
    return relation


def relation_weight(relation: FaveRelation) -> float:
    return relation.weight * 10


df = pd.read_csv(
    io.StringIO(
        """
1,2,3
さらば青春の光,乃木坂46,ダイアン
カゲヤマ,さらば青春の光,和賀勇介
ふぉ〜ゆ〜,梅棒,さらば青春の光
さらば青春の光,ニューヨーク,千鳥
さらば青春の光,SnowMan,もも
さらば青春の光,金属バット,チュートリアル
さらば青春の光,BKB,みなみかわ
さらば青春の光,ハリウッドザコシショウ,陣内智則
男性ブランコ,囲碁将棋,ケビンス
鬼ヶ島,シティホテル3号室,都トム
さらば青春の光,見取り図,令和喜多みな実
関ジャニ∞,さらば青春の光,ジャニーズWEST
さらば青春の光,乃木坂46,バナナマン
さらば青春の光,オリエンタルラジオ,ラランド
少女時代,SCANDAL,aespa
KinKi Kids,Mr.Children,ユニゾンスクエアガーデン
ミツメ,カネコアヤノ,LAYRUS LOOP
千鳥,かまいたち,ZARD
IVE,aespa,ルセラフィム
THE RAMPAGE,ナイツ,さらば青春の光
澤野弘之,鷺巣詩郎,松谷卓
YOASOBI,King Gnu,マハラージャン
ダウンタウン,霜降り明星,ナダル
aiko,Official髭男dism,私立恵比寿中学
ポルカドットスティングレイ ,ポルノグラフィティ,椎名林檎
さらば青春の光,BUMP OF CHICKEN,オードリー
ピーナッツくん,金属バット,PUNPEE
なにわ男子,櫻坂46,福田晋一
女王蜂,米津玄師,星野源
嵐,オードリー,Sexy Zone
星野源,ずん（飯尾和樹）,なかやまきんに君
浦島坂田船,After the Rain,ゴールデンボンバー
Aぇ! group,beyooooonds,よゐこ
パスピエ,ジャルジャル,beyooooonds
鈴木愛理,岡田准一,ヒコロヒー
ハリウッドザコシショウ,粗品,さらば青春の光
チョコレートプラネット,霜降り明星、Kep1er,ラランド
バキ童（春と紙ヒコーキ）,千鳥,笑い飯
スピッツ,千鳥,サザンオールスターズ
東京03,ジョングク,CHEMISTRY 
トータルテンボス,ダイアン,さらば青春の光
せかいのおわり,Superfly,YOASOBI
さらば青春の光,小山田壮平,never young beach
男性ブランコ,NU'EST,ななまがり
"""
    )
)

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
    G.add_edge(
        relation.source.name, relation.target.name, weight=relation_weight(relation)
    )

net = Network()
net.from_nx(G)
net.select_menu = True
net.cdn_resources = "remote"
net.show("docs/index.html", notebook=False)

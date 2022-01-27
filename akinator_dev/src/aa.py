import sys
import random as rand

normal_aa = """
　　　　　　　　　　　　　　　　　　　　i.、
　　　　　　　　　＿＿＿＿＿_　 ,.-┘!
　　　　　　　 ／｀ヽ、　　　　　＼!r‐´
　　　　　　　i /　r,-,＼￣￣￣￣｀ヽ、
　　　　　　　l/　 l.n」　 ＼　　　　　　 ヽ
　　　　　　　＼r───‐┴-,、　　　　|
　　　　　　　　 |二　-‐二‐-　|lli＿＿_/
　　　　　　　　 |┸r　　┸　　 ﾚ／r/./
　　 　 　 　 　 i　_!_r‐,,,,,,,　　　_)./￣
　　 　 　 　 　 |ﾞﾞﾞﾞﾞー‐´　　　　/
　　　　　　　　 ＼/ヽ＿＿_,.-イi
　　　　　　　　 ＿)「/|　 __,.-‐´/__
　　　　　　 ／　 ｀ )/　__)　　 /　 ｀ー-、
　 　 　 　 /　 /　　|　 .)　 　 　 　 　 　 ヽ
　　　 　 ノ〈ヽ　　 ＞＜　 　 　 　 /　　　 i
　__,.- ´ ´/‐┴───.、　　　 ／　　　　i
. i　　　　/　　_,.-──‐┴─‐´　　　　　/
　!、　　/_,.イ_/　　　　　　　　　　　　 ／
　 ヽ　 .i　 /　|　　　　　　　　　　　／
　　 i　 | /ヽ　|　　　　　　　　 ／/
　　　ヽV　 .i　i　　／￣￣￣　/
　　　　　　　i. ｀ｰ´　　 　 　 ／
　　　　　　　 i　　　　　　 ／
　　　　　　　　i　　　　　/　　　　　　　　＿＿＿__
　　　　　　　　 i　　 　 /　　　　　　　／　＿＿　 )
　 　 　 　 　 　 ヽ　　 .＼　　　__,.-‐´,..-´　 　 )/
　　　　　　　　　　＼　　 ￣￣　　／｀ヽ､＿＿||
　　　　　　　　　　　 ｀ヽ､＿＿_／　　　　　,.-‐┘
　　　　　　　　　　　　　　　　　 ＼＿＿_／
　　　　　　　　　　　　　　　　　　く＿__＞

"""

thinking_aa = """
　　　　　　　　　　　　　　　 　 　 　 i、
　　　　　　　　 ＿＿＿＿＿＿　 r‐.´ﾉ
　　　　　　　 /／　＼＿＿＿__＼!r.´
　　　　　 　 //　 (・ ) ＼　　　 ￣｀ヽ、
　　　　　　　Y＿＿＿＿ヽ＿　　　　　ヽ
　　　　　　　　 |＿　 ＿＿__　ヽ　　　　/
　　　　　　　　 |┰__　 ┰-、　 llli＿__./
　　 　 　 　 　 i　7　　 ￣　　　／)././
　　　　　　　　i ,,,,ヽ,,´,,,,,　　　 _//￣
　　　　　　　,.┴´二ﾆつ　　 　 /_
　　　 　 　 /　 ヽ ヽ_〉＿_,.-‐７//
　　　　　 /　ﾐY　〉_/)|　 __,.-´ /-､__
　　　　//　 /｀ｰ´ ヽ/ __)　　　　　　｀ヽ、
.　　　 i |　 / ｀)　　(　 )__,.-　 　 　 　 　 ヽ
　　　 i　i　|　/　　＞＜　　　　　 /　　　　 i
　　　/　ヽ.!　ヽ 　 　 　 　 　 　 /　　　　　i
　　 /　　 Y　　ヽ　　　　　　　 /　　　　　/
　　i　　　　｀＞/-‐--､＿＿_/　　　　 ／
　　ヽ＿_,.-‐´/　　　　　　　　　 　 ／/
　　　　|　　　i　　　　　　　　　　／／
　　　　｀ーﾍﾍ　　　＿＿＿_.／／
　　　　　　　i. ＼／　　　　　／
　　　　　　　 i　　　　　　　/
　　　　　　　 ヽ　 　 　 　 i　　　　　　　　 ＿＿＿_
　　　　　　　　 ヽ　　　　　!　　　　　__,.-´__,.-─､　)
　　　　　　　　　 ＼　　　　＼＿_／　_,-´　　　/／
　　　　　　　　　　　｀ヽ､_　　　＿,.-´｀ヽ､＿＿||
　　　　　　　　　　　　　　￣￣.! 　 　 　 　 ,.-‐┘
　　　　　　　　　　　　　　　　　 ＼＿＿_／
　　　　　　　　　　　　　　　　　　く＿__＞
"""

smiling_aa = """
　　　　　　　　 ＿＿＿＿＿_　　　__)i
　　　　　　　 / /＼　　　　　 ＼ f ,.-´
　　　　　 　 / / .r‐,＼＿＿＿＿＼
　　　　　　 〈/　 VV　 ヽ　　　　 .￣＼
　　　　 　 　 ヽ-──‐┴─-、　　　　i
　　　/７　　　 |￣　　￣｀ヽ　 lli;＿＿./
　　 /./　　　　|ﾆO　　ﾆOﾆ　 ll!,--/ /
.　 / ﾑ--、　 .i　i＿,-,,,,,　　　　)/┴´
　 i　＿二i)　 i ﾞﾞﾞヾ===ｼ　　　イ
　 !　＿ i/　　 ＼_∧＿＿__,.イ-,
　_|　 /┘　　　 __(.(/　　　 ノ　/
./ |　 |￣ヽ,-─｀!!´i　 r─´　/─‐-、
.｀､!　 i　　i　　　 i.〉　__.)　　　　　　　＼
　 iヽ .i　　ヽ　　__(＿)__　 　 　 　 　 　 ヽ
　 |　ヽi　　 ヽ　　／＼　　　 　 /　　　　 i
　 |　　 ｀ー-/　　　　　　　　　/　　　　 /
　 |　　 　 ／　 ＿　　　　　　/　　　　 /
　 .＼＿ノ￣〉´　 ￣￣￣￣　　　,.-イ
　　　|,　　　i　　　　　　　　　　 ／ ／
　　　|__っ_人　　　　　　　　 ／_-´
　　　　　　|　＼／￣￣￣´／　　　　　　 ＿_
　　　　　　 i　　　　　　　／　　　　　　 ／　　｀ヽ
　　　　　　 ｀、　　　 　 /　　　 　 　 ／ ,..-‐-、　!
　　　　　　　 ヽ　　　　 i　　　　　 ／ ／　　　 ) /
　　　　　　　　 ヽ　　　 ヽ＿＿,／ ／　　　　/ノ
　　　　　　　　　 ＼　　　　　＿_ノ ＼＿＿__||
　　　　　　　　　　　 ￣￣￣.i　　　　　　 ,.-‐┘
　　　　　　　　　　　　　　　　 ＼＿＿_／
　　　　　　　　　　　　　　　　　く＿__＞
"""

happy_aa = """
　　　　　　　　　　　　　　＿＿＿＿＿　 ＜ヽ
　　　　　　　　　　　　　/ ／＼　　　　 ＼/r´
　　　　　　　　　　　　 //　r‐、ヽ───-＼
　　　　　　　　　　　　 Y＿l∧|＿_i　　　　　　ヽ
　　　　 ＿＿＿　　　　 | r‐　　 -､￣ヽ　　　　|
　　　 /＼__|__|_|　 　 　 ﾚ＞　 ＜ i_　 llli;＿.　/
　　　 ヽノ r‐＜-、　　 / /￣　　=　　,ll!,-, )./
　　　　i_　 ＿/｀┘　　i ﾞﾞﾄーﾞﾞﾞﾞﾞﾞﾞ7ﾞ　 レ/-´
　　 ／/　 //　　　　　ヽ レ-､二/　　 /　　　rrr‐==、
　／ /-─´i　　　　　　　Y_ゝ＿_,.-イ〈　　　rへL| Y |
/__／　 　 /　　　　＿＿「.V　 _ﾉ　　/--､__ ｀ヽ_ (´　!
ヽ　　　　/-、　 __/　／　 i　　)　　 ´　　　 ヽ　 _7　ｲ
　ヽ　　　　 .|￣　　/　　　＞＜　　　 　 　 　 V/　　|ヽ
　　ヽ　　　　　　＿|　　　　　　　　　　　　　　 || 　 ./　|
　　　ヽ　　_,..-´　 .i　　　　　　　　　　 i　　　/||　 ./　 .!
　　　　ヽ/　　　　 i　　　　　　　　　　　i　　/ | i　/　 ./
　　　　　　　　　　i　　　　　　　　　　　 i　　　　V　　/
　　　　　　　　　　|　　　　　　　　　　　/ヽ＿＿.|　 /
　　　　　　　　　　|　　　　　　　　　 ／　　　　　ヽ.ﾉ
　　　　　　　　　　 i　　　　　　　　/　　　　　　＿＿＿
　　　　　　　　　　　i　　　　　　　i　　　 _,.-二-──-､＼
　　　　　　　　　　　 ＼　　　　　 ｀ー ´ ／　　　　　　 ヽ )
　　　　　　　　　　　　　｀ヽ､＿＿＿_,-´　　　　　　　　/ノ
　　　　　　　　　　　　　　　　　　　　　　　　　　　　 ,=彳
　　　　　　　　　　　　　　　　　　　　 ／￣｀ヽ､＿__||_
　　　　　　　　　　　　　　　　　　　　i　　　　　　 ,.-‐┘
　　　　　　　　　　　　　　　　　　　　 ＼＿＿_／
　　　　　　　　　　　　　　　　　　　　　く＿__＞
"""

sad_aa = """
　　　　　　　　　　　　　　　　　　＿
　　　　　　　　　　　　　　　　　 ＞ ＞
　　　　　　　　　__,..-───-＜＜
　　　　　　　　//｀ヽ､＿,.-───.＼
　　　　　　 　 i/　(・) ＼　　　　　　　 i
　　　　　　　　|＿＿,-‐┴─‐,,、　 　 i
　　　　　　　　 ヽ＿,　__,.-‐-　ﾞllll──!
　　　　　　　　　 i＞,-　 ＜　　 l!/)/.ノ
　　　　　　　　　 | ,,(＿ノ,,,,,,,,　　く/i
　　　　　　　,-‐-,!　く￣｀ヾ ,　　/　i
　　　 　 ,- ´　　 ミ､./ヽ＿_´- ´_　/-､＿_
　　　　/　､__ __ i.Y .( (´ .|__r ´　 ヽ　　 　 i
　　　 /　 /__＞´ /　｀　ノ!._　　　　i　　　　i
　 __ノ　 ./　ヽ　./　　　￣ヽL__、　 ｀、　　 ｀、
.//　　　 |、　)_/　　 　 　 　 　 ヽ　　ヽ　　　 i
i i　　　 / |　/ .|　　 　 　 　 　 　 i.　　 ＼　　 ヽ
| i　　　_./ ./　 |　　　　　　　　　　i　　 　 ヽ　　 ヽ
.i ヽ─´/ /　　 i　　　　 　 　 　 　 ﾄ、　　　i　　　.i
.ヽ　　 /./　　　 i　　　　　　　　　　||ヽ　　 .|　　 /
　ヽ.、_! |　　　　 i　　　　　　　　／.!!　＼_/!　 ./
　　｀ー┘　　　　i　　　　　　 ／　　|　　　/ ／＿_
　　　　　　　　 　 i　　　　　/　　　　L__ノ-´ / r‐, ヽ
　　　　　　　　　　i　　　　 .i　　　 ＿　　　 / /　/ /
　　　　　　　　　　ヽ　　　　i　　 / ,、ヽ＿/ /　 (_.(
　　　　　　　　　　　＼　　　＼/ / ∧＿_.∧＿＿))
　　　　　　　　　　　　 ＼＿＿_/　i　　　　　　 ,.-‐┘
　　　　　　　　　　　　　　　　　　　 ＼＿＿_／
　　　　　　　　　　　　　　　　　　　　く＿__＞
"""

def base(aa_str):
    print(aa_str)

def normal():
    base(normal_aa)

def thinking():
    base(thinking_aa)

def smiling():
    base(smiling_aa)

def random():
    aa_list = [normal_aa, thinking_aa, smiling_aa]
    base(rand.choice(aa_list))

def happy():
    base(happy_aa)

def sad():
    base(sad_aa)

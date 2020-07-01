# 引入path
from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'apps.textPreprocess'

urlpatterns = [
    # 目前还没有urls
    path('convertpinyin/', views.ConvertPinyin, name='ConvertPinyin'),# 中文转拼音
    path('extractletter/', views.ExtractLetter, name='ExtractLetter'),#提取字母
    path('extractnum/', views.ExtractNum, name='ExtractNum'),#提取数字
    path('englishtochinese/', views.EnglishToChinese, name='EnglishToChinese'),#英文翻译（英文转中文）
    path('numbertohanzi/', views.NumberToHanzi, name='NumberToHanzi'),#阿拉伯数字转汉字
    path('pinyinchar/', views.PinYinChar, name='PinYinChar'),# 拼音转文字
    path('textcorrection/', views.TextCorrection, name='TextCorrection'),# 文本纠错
    path('kerasbertvector/', views.KerasBertVector, name='KerasBertVector'),# 基于bert转词向量
    path('traditional2simplified/', views.Traditional2Simplified, name='Traditional2Simplified'),# 繁体转简体
    path('charpreprocess/', views.CharPreprocess, name='CharPreprocess'),# 文本预处理，将句子输出为只有中文字符
]


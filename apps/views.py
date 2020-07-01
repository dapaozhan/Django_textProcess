from django.shortcuts import render

# Create your views here.
# 以下为安装导入的包
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
#以下自定义函数
from apps.textPreprocess.src.DealChar import _extract_letter
from apps.textPreprocess.src.DealChar import _extract_num
from apps.textPreprocess.src.ConvertPinyin import _convert_pinyin
from apps.textPreprocess.src.DealChar import _chinese_to_english
from apps.textPreprocess.src.NumberToHanzi import NumberToHanzi
from apps.textPreprocess.src.PinYinChar import PinYinChar
from apps.textPreprocess.src.TextCorrection import TextCorrection
from apps.textPreprocess.BertModel.extract_sen_vec import KerasBertVector
from apps.textPreprocess.src.LangConv import Traditional2Simplified
from apps.textPreprocess.src.CharPreprocess import format_str
# 中文转拼音
def ConvertPinyin(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        return JsonResponse({'convert_pinyin_result': _convert_pinyin(content)}, status=200) 
    except:
        return JsonResponse({'convert_pinyin_result': 'fail'}, status=501)
#提取字母
def ExtractLetter(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        return JsonResponse({'extract_letter_result': _extract_letter(content)}, status=200) 
    except:
        return JsonResponse({'extract_letter_result': 'fail'}, status=501)
#提取数字
def ExtractNum(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        return JsonResponse({'extract_num_result': _extract_num(content)}, status=200) 
    except:
        return JsonResponse({'extract_num_result': 'fail'}, status=501)
#英文翻译（英文转中文）
def EnglishToChinese(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        return JsonResponse({'english_to_chinese': _chinese_to_english(content)}, status=200) 
    except:
        return JsonResponse({'english_to_chinese': 'fail'}, status=501)


#阿拉伯数字转汉字
def NumberToHanzi(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        return JsonResponse({'number_to_Hanzi': NumberToHanzi(content)}, status=200) 
    except:
        return JsonResponse({'number_to_Hanzi': 'fail'}, status=501)

# 拼音转文字
def PinYinChar(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        return JsonResponse({'pinyin_char': PinYinChar(content)}, status=200) 
    except:
        return JsonResponse({'pinyin_char': 'fail'}, status=501)

# 文本纠错
def TextCorrection(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        return JsonResponse({'text_correction': TextCorrection().text_correction(content)}, status=200) 
    except:
        return JsonResponse({'text_correction': 'fail'}, status=501)




# 基于bert转词向量
def KerasBertVector(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        bert_vector=KerasBertVector()
        return JsonResponse({'bert_vector': bert_vector.gen_sen_vec(content)}, status=200) 
    except:
        return JsonResponse({'bert_vector': 'fail'}, status=501)

# 繁体转简体

def Traditional2Simplified(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        return JsonResponse({'traditional_to_simplified': Traditional2Simplified(content)}, status=200) 
    except:
        return JsonResponse({'traditional_to_simplified': 'fail'}, status=501)



# 文本预处理，将句子输出为只有中文字符
def CharPreprocess(request):
    try:
        json_bytes = request.body
        json_str = json_bytes.decode()
        classify_dict = json.loads(json_str)
        content = classify_dict.get('chinese_char')
        return JsonResponse({'char_preprocess': format_str(content)}, status=200) 
    except:
        return JsonResponse({'char_preprocess': 'fail'}, status=501)
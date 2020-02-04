import pymorphy2

text = ""
with open(file='txt', mode='r', encoding='utf-8') as f:
    text = f.read()
punctuation = ['.',',',':',';','!','?','(',')','-','"','«','»','—']
for i in range(len(punctuation)):
    text = text.replace(punctuation[i],"")
text_list = text.split()
text_list = list(map(str.lower,text_list))
dic_list = {}
morph = pymorphy2.MorphAnalyzer()
for i in text_list:
    i = morph.parse(i)[0].normal_form
    if i not in list(dic_list.keys()):
        dic_list[i] = 1
    else:
        dic_list[i] += 1
sort_dic_list = {key: value for key, value in sorted(dic_list.items(), key=lambda item: item[1], reverse=True)}
for i in range(5):
    print(list(sort_dic_list)[i])
my_set = set(sort_dic_list.keys())
print(len(my_set))
# encoding=utf-8
import jieba

jieba.load_userdict("D:\E\...path of user-defined thesaurus")
from sklearn.feature_extraction.text import TfidfVectorizer

stopwords_path = 'D:\E\...path of stop-word thesaurus'

stopwords = []
with open(stopwords_path, 'r', encoding='utf-8') as f:
    for line in f:
        if len(line) > 0:
            stopwords.append(line.strip())

def tokenizer(s):
    words = []
    cut = jieba.cut(s)
    for word in cut:
        if word not in stopwords:
            words.append(word)
    return words


def cut(txt_name1, txt_name2):
    with open(txt_name1, 'rb') as f1:
        txt = f1.read()
        txt_cut = tokenizer(txt)
        result = ' '.join(txt_cut)
    with open(txt_name2, 'w') as f2:
        f2.write(result)
    f1.close()
    f2.close()


for n in range(1, 33):
    print('n=====',n)
    path = 'D:\E\...path of policy' + str(n) + '.txt'
    print('path====',path)
    cut(path, path)


stopWords_dic = open('D:\E\...path of stop-word thesaurus', 'rb')
stopWords_content = stopWords_dic.read()
stopWords_list = stopWords_content.splitlines()
stopWords_dic.close()

corpus = []
for m in range(1,33):
    print('m====',m)
    path_m = 'D:\E\...path of policy' + str(m) + '.txt'
    with open(path_m, 'r') as f:
        res = f.read()
        corpus.append(res)
print('corpus=====', len(corpus))
vector = TfidfVectorizer(stop_words=stopWords_list)
tf_idf = vector.fit_transform(corpus)
with open('D:\E\...path of result.../tfidf_result.txt', 'w') as result1:
    print(tf_idf, file=result1)

word_list = vector.get_feature_names_out()
weight_list = tf_idf.toarray()

for i in range(len(weight_list)):
    with open('D:\E\...path of result.../wordweight_result.txt', 'a') as result2:
        print("-------第", i + 1, "份文本的词语tf-idf权重------", file=result2)
    for j in range(len(word_list)):
        with open('D:\E\...path of result.../wordweight_result.txt', 'a') as result2:
            print(word_list[j], weight_list[i][j], file=result2)


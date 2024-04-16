import re

with open('D:\E\work\..path...\\tfidf_keywords.txt', 'r', encoding="utf-8") as keywords:
    keywords_content = keywords.read()
keywords_list = keywords_content.splitlines()
keywords.close()


for m in range(1,33):
    print('m====',m)
    path_m = 'D:\E\work\..path of policy.../policy' + str(m) + '.txt'
    with open(path_m, 'r') as f:
        text = f.read()
    result_findall = []
    with open('D:\E\work\..path of result.../keywords_result.txt', 'a') as result1:
        print("-------第", m, "份文本的关键词------", file=result1)
    for i in keywords_list:
        pattern = re.compile(i)
        res = pattern.findall(text)
        result_findall.extend(res)
    with open('D:\E\work\..path of result.../keywords_result.txt', 'a') as result2:
        print(set(result_findall), file=result2)

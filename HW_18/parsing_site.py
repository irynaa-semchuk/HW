import re
import requests

data = requests.get(
    'http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83')

def result_1(data):
    res = re.finditer(r'<p>(?P<univer>.*).*\n?<b>(?P<email>.*)<', data.text)
    res1 = {(re.sub(r'\t','',match.group('univer')),match.group('email')) for match in res}
    with open("res1.txt", "w") as file1:
        file1.write("\n".join(map(str, res1)))
    return f"Results 1: \n{res1}\n"
        
def result_2(data):
    res2 = {}
    items = re.finditer(r'>\s\d+\.\s((?P<title>[а-яА-Яa-z-єіїЄІЇ,\s]+)\<\/span><\/h2>\s?)((<p>)?[а-яА-Яa-zA-Z-єіїЄІЇ",.\s]+<b>[a-zA-Z0-9_@.]+<\/b>\s?\n?(<\/p><p>)?)*', data.text)
    for item in items:
        res_2 = re.finditer(r"<p>(?P<university>.*).*\n?<b>(?P<email>.*)<", item.group(0))
        res2.update({item.group("title"): list((re.sub(r"\t", "", match.group("university")), match.group("email")) for match in res_2)})
    with open("res2.txt", "w") as file_2:
        file_2.write(str("\n".join([":\n ".join(["\n".join([key, str(value)]) for key, value in res2.items()])])))
    return f"Results 2: \n{res2} \n"
        
 if __name__ == "__main__":
    res = result_1(data)
    res_2 = result_2(data)
    print(res)
    print(res_2)
    

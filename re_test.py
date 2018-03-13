import re

# 1.3.6匹配多个字符
bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print('1: ' + m.group())

m = re.match(bt, 'blt')
if m is not None:
    print('2: ' + m.group())

m = re.match(bt, 'he bit me!')
if m is not None:
    print('3: ' + m.group())

m = re.search(bt, 'he bit me!')
if m is not None:
    print('4: ' + m.group())

# 1.3.7匹配任何单个字符
anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None:
    print('5: ' + m.group())

m = re.match(anyend, 'end')
if m is not None:
    print('6: ' + m.group())

m = re.match(anyend, '\nend')
if m is not None:
    print('7: ' + m.group())

m = re.search(anyend, 'The end.')
if m is not None:
    print('8: ' + m.group())

patt314 = '3.14'
pi_patt = '3\.14'
m = re.match(pi_patt, '3.14')
if m is not None:
    print('9: ' + m.group())

m = re.match(patt314, '3.14')
if m is not None:
    print('10: ' + m.group())

m = re.match(patt314, '3014')
if m is not None:
    print('11: ' + m.group())

# 1.3.8创建字符集
m = re.match('[cr][23][dp][o2]', 'c3po')
if m is not None:
    print('12: ' + m.group())

m = re.match('[cr][23][dp][o2]', 'c2do')
if m is not None:
    print('13: ' + m.group())

m = re.match('r2d2|c3po', 'c2do')
if m is not None:
    print('14: ' + m.group())

m = re.match('r2d2|c3po', 'r2d2')
if m is not None:
    print('15: ' + m.group())

# 1.3.9重复/特殊字符以及分组
patt = '\w+@(\w+\.)?\w+\.com'
m = re.match(patt, 'nobody@xxx.com')
if m is not None:
    print('16: ' + m.group())
m = re.match(patt, 'nobody@www.xxx.com')
if m is not None:
    print('17: ' + m.group())

patt = '\w+@(\w+\.)*\w+\.com'
m = re.match(patt, 'nobody@www.xxx.yyy.zzz.com')
if m is not None:
    print('18: ' + m.group())
m = re.match('\w\w\w-\d\d\d', 'abc-123')
if m is not None:
    print('19: ' + m.group())
m = re.match('\w\w\w-\d\d\d', 'abc-xyz')
if m is not None:
    print('20: ' + m.group())
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if m is not None:
    print('21: ' + m.group(1))
    print('22: ' + m.group(2))
    m.groups()
# 1.3.10匹配字符串的起始和结尾以及单词边界
m = re.search('^The', 'The end.')
if m is not None:
    print('23: ' + m.group())
m = re.search('^The', 'end. The')
if m is not None:
    print('24: ' + m.group())
m = re.search(r'\bthe', 'bite the dog')
if m is not None:
    print('25: ' + m.group())
m = re.search(r'\bthe', 'bitethe dog')
if m is not None:
    print('26: ' + m.group())
m = re.search(r'\Bthe', 'bitethe dog')
if m is not None:
    print('27: ' + m.group())
# 1.3.11使用dindall()和finditer()查找每一次出现的位置
m = re.findall('car', 'car')
print(m)
m = re.findall('car', 'scary')
print(m)
m = re.findall('car', 'carry the barcardi to the car')
print(m)
s = "This and that."
m = re.findall(r'(th\w+) and (th\w+)', s, re.I)
print(m)
m = next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).groups()
print(m)
m = next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).group(1)
print(m)
m = next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).group(2)
print(m)
# [g.groups() for g in re.finditer(r'(th\w) and (th\w)', s, re.I)]
m = re.findall(r'(th\w+)', s, re.I)
print(m)
it = re.finditer(r'(th\w+)', s, re.I)
g = next(it)
print(g.groups())
print(g.group(1))
g = next(it)
print(g.groups())
print(g.group(1))
for g in re.finditer(r'(th\w+)', s, re.I):
    print(g.group(1))
# 使用sub和subn搜索与替换
m = re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X ,\n')
print(m)
# m=subn('X', 'Mr. Smith', 'attn: X\n\nDear X ,\n')
# print(m) #提示无subn函数
m = re.sub('[ae]', 'X', 'abcdef')
print(m)
m = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91')
print(m)
# 在限定模式上使用split()分隔字符串
m = re.split(':', 'str1:str2:str3')
print(m)
DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)
for datum in DATA:
    print(re.split(', |(?=(?:\d{5}|[A-Z]{2})) ', datum))
    # print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))

# 1. Uzdevums analizēt Veidenbauma dzeju

# Lejuplādejam texta failu no šejienes -> Save As

# https://raw.githubusercontent.com/ValRCS/Python_RTU_08_20/master/data/veidenbaums.txt

# Vai no šejienes:

# https://www.das.lv/platforma/pluginfile.php/3439/mod_resource/content/1/veidenbaums.txt

# Var arī vienkārši git pull visam repozitorijam: 

# https://github.com/ValRCS/Python_RTU_08_20

# 1a -> uzrakstam funkciju file_line_len(fpath), kas atgriež rindiņu skaitu failā
# pārbaudam file_line_len("veidenbaums.txt") -> vajadzētu būt 971
# iespējams jums veidenbaums.txt nebūs tajā pašā mapē, tad lietojam relatīvo ceļu uz failu

# 1b -> uzrakstam funkciju get_poem_lines(fpath), kas atgriež list ar tikai tām rindiņām kurās ir dzeja.
# Tātad mums nederēs rindiņas bez teksta un nederēs dzejoļu virksraksti.
# PS vēlams izmantot encoding = "utf-8"a

# 1c -> uzrakstam funkciju save_lines(destpath, lines)
# Šī funkcija noglabās destpath faila ceļā(tātad fails vai fails ar ceļu), visas lines

# 1d -> izsaucam get_poem_lines uz veidenbaums.txt un tad rezultātu saglabājam veidenbaums_poems.txt (turpat kur ir jau veidenbaums) izmantojot save_lines funkciju

# 1e -> uzrakstam funkciju clean_punkts(srcpath,destpath)
# funkcija atvērs srcpath failu, attīrīs to no https://docs.python.org/3/library/string.html#string.punctuation
# un saglabās destpath 
# izsaucam uz veidenbaums_poems.txt un destpath būs veidenbaums_no_punkts.txt

# Droši vien nepietiks laika bet pamēģinam pa brīvdienām
# 1f -> uzrakstam funkciju get_word_usage(srcpath, destpath)
# funkcija atver failu un atrod biežāk lietotos vārdus
# ieteikums izmantot Counter moduli !
# uzskatīsim, ka vārdi tiek atdalīti vai nu ar whitespace vai newline (vecais labais split noderēs)

# populārāku vārdu sarakstu ar lietojuma biežumu saglabāam destpath

# Varam tagad pārbaudīt rezultātus gan uz veidenbaums_no_punkts.txt, gan uz veidenbaums_poems.txt

import os
import requests
import string

#1a
def file_line_len(fpath):
    return sum([1 for lines in open(fpath)])

#1b
def get_poem_lines(fpath):
    return "".join([lines for lines in open(fpath) if lines[0]!='\n' if lines[-4:-1]!='***'])

#1c
def save_lines(destpath, lines):
    with open(destpath, mode='w', encoding='utf-8') as writeFile:
        writeFile.write(lines)

#1e
def clean_punctuation(srcPath, destPath):
    pass
    

url = 'https://raw.githubusercontent.com/ValRCS/Python_RTU_08_20/master/data/veidenbaums.txt'
fileName = "veidenbaums.txt"

r = requests.get(url)
with open(fileName, 'wb') as fout:
    fout.write(r.content)

print(file_line_len(fileName))
print(get_poem_lines(fileName))

#1d
save_lines('./veidenbaums2.txt', get_poem_lines(fileName))
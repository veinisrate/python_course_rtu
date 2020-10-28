# 3. Vārdnīcu tīrītājs
# 3.a  Uzrakstīt clean_dict_value(d, bad_val), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtība  bad_val no kuras jāatbrīvojas kopā ar ar tās atslēgu.
# clean_dict_value({'a':5,'b':6,'c':5}, 5) -> {'b':6} , jo 5 bija vērtība gan a gan c atslēgām no kurām jāatbrīvojas.
# 3.b Uzrakstīt clean_dict_values(d, v_list), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtību saraksts v_list no kurām jāatbrīvojas.
# clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]) -> {'b':6} , jo 5 bija vieno no vērtībām no kurām jāatbrīvojas.
# PS. Tīram mēs are del d['a'] protams tikai tad ja atslēga 'a' eksistē.
# !! Mainot vārdnīcas izmēru mēs nedrīkstam vienlaicīgi pa šo vārdnīcu staigāt(iterate)!
# Divi varianti: vai nu staigājam pa kopiju my_dict.copy.items(), vai arī būvējam jaunu vārdnīcu

#3.a
def clean_dict_value(d: dict, bad_val:any) -> dict:
    key_list = []
    for k in d:
        if d[k]==bad_val:
            key_list.append(k)
    for k in key_list:
        d.pop(k)
    return d

print(clean_dict_value({'a':5,'b':6,'c':5}, 5))

def clean_dict_values(d: dict, v_list: list) -> dict:
    key_list = []
    for k in d:
        if d[k] in v_list:
            key_list.append(k)
    for k in key_list:
        d.pop(k)
    return d

print(clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]))
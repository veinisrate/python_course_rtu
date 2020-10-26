# 3. Pilsēta
# Pilsētā ir zināms skaits iedzīvotāju p0
# Katru gadu nāk klāt procentuāls skaits perc
# Katru gadu nāk klāt(vai aizbrauc) arī zināms skaits delta
# Mums ir jāzina, kad(ja vispār) pilsēta sasniegs iedzīvotāju skaitu p
# Uzrakstiet funkciju get_city_year(p0, perc, delta, p) kas atgriež gadus (pilnus) kad p tiks sasniegts.
# Ja p nevar sasniegt, tad atgriežam -1
# Piemērs:
# get_city_year(1000,2,50,1200) -> 3
# 1000 + 1000 * 0.02 + 50 => 1070 pēc 1.gada
# 1070 + 1070 * 0.02 + 50 => 1141 pēc 2.gada
# 1141 + 1141 * 0.02 + 50 => 1213 pēc 3.gada
# PS. Ievērojam, ka padodam perc kā procentu kas jāpārvērš decimāl skaitlī.
# Pārbaudam, vai strādā ar sekojošiem parametriem:
# get_city_year(1000, 2, -50, 5000) -> -1 # samērā aktuāla problēma
# get_city_year(1500, 5, 100, 5000) -> 15
# get_city_year(1500000, 2.5, 10000, 2000000) -> 10

def get_city_year(p0, perc, delta, p) -> int:
    year = 0
    if p0 + (p0 * perc/100) + delta <= p0:
        return -1
    while (p0<=p):
        p0 = (p0 + (p0 * perc/100)) + delta
        year += 1 
    return year

print(get_city_year(1000, 2, -50, 5000))# -> -1 # samērā aktuāla problēma
print(get_city_year(1500, 5, 100, 5000))# -> 15
print(get_city_year(1500000, 2.5, 10000, 2000000)) # -> 10
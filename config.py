max_letters = 12
language_tags = {

    'en': ['actor', 'alcohol', 'cheque', 'cancer', 'chocolate', 'debate', 'hobby', 'melon', 'propaganda',
           'religion', 'violin', 'england', 'MediaWiki'],

    'cs': ['praha', 'evropa', 'pyreneje', 'voda', 'housle', 'Náboženství', 'Příroda', 'Ekosystém',
           'vzdělání', 'Dům', 'Zpěvák', 'Zeus', 'Mykény', 'Starověké_Řecko', 'Renesance',
                       'Andrej_Babiš', 'Správa_železniční_dopravní_cesty', 'Kraje_v_Česku', 'Česko', 'Slezsko',
                       'Latina', 'Spojené_království', 'Římský_senát'],

    'de': ['Deutsche_Sprache', 'Deutschland', 'Kommunistische_Partei_der_Sowjetunion', 'Wasser',
           'Festkörper', 'Seele', 'Geist', 'Dreifaltigkeit', 'Große', 'Christentum', 'Gott'],

    'sv': ['Svenska', 'Sverige', 'Danmark', 'Europeiska_unionen', 'Medeltiden', 'Feodalism', 'Kung',
           'Kejsare', 'Monarki', 'Valmonarki', 'Choklad', 'Mjölk', 'Prolaktin', 'Kvinna', 'Eldvapen',
           'Kina', 'Götar', 'Romantiken', 'Ideologi', 'Tänkande', 'Pedagogik', 'Sekund', 'Solen', 'Väder',
           'Mellanöstern', 'Väte', 'Anatomi', 'Hjärta', 'Puls', 'Grekiska', 'Cypern'],

    'fr': ['Français', 'Langues_romanes', 'Charlemagne', 'Traité_de_Verdun', 'Louis_le_Pieux',
                       'Son_(physique)', 'Zoologie', 'Intelligence_animale', 'Intelligence', 'Tautologie',
                       'Pléonasme', 'Figure_de_style']

}


def convert_dic_to_vector(dic, max_word_length):
    new_list = []
    for word in dic:
        vec = ''
        n = len(word)
        for i in range(n):
            current_letter = word[i]
            ind = ord(current_letter)-97
            placeholder = (str(0)*ind) + str(1) + str(0)*(25-ind)
            vec = vec + placeholder
        if n < max_word_length:
            excess = max_word_length-n
            vec = vec + str(0)*26*excess
        new_list.append(vec)
    print(len(new_list))
    return new_list

# [`1603:99`] /Temporary public numeric namespace/
> Dictionaries here did not get a numeric namespace.

## [`1603:99:987`] /Personal name/

- https://en.wikipedia.org/wiki/Template:Personal_names
  - https://en.wikipedia.org/wiki/Talk%3APersonal_name
- https://en.wikipedia.org/wiki/Onomastics
- https://en.wikipedia.org/wiki/Personal_name
- https://semiceu.github.io/Core-Person-Vocabulary/releases/2.00/

## [`1603:99:876`] //Human sexuality (meta dictionaries)//

### [`1603:99:876:1`] //Glossary of biological sex, gender identify, grammatical gender and third-person pronouns//
> Define general terms for others on this group

### [`1603:99:876:2`] //biological sex//

### [`1603:99:876:3`] //gender identity//
- https://github.com/HXL-CPLP/forum/issues/50
- TODO: take the division from here
  - https://github.com/SEMICeu/Core-Person-Vocabulary/issues/38
- https://github.com/EticaAI/numerordinatio/blob/main/docs/data/exemplum/scientiae-communitatem--sexualitatem.yml

> Trivia:
> - The Second Sex (French: Le Deuxième Sexe) from Simone de Beauvoir
 was criticized by it's poor English translation -- https://en.wikipedia.org/wiki/The_Second_Sex#Translations
> - This type of comment is relevant because English terminology is more confusing than several other languages.

### [`1603:99:876:4`] //grammatical gender//
- https://en.wikipedia.org/wiki/Grammatical_gender
- https://en.wikipedia.org/wiki/List_of_languages_by_type_of_grammatical_genders
- https://en.wikipedia.org/wiki/Genderless_language

### [`1603:99:876:5`] //third-person pronouns//

---

## Early drafted comments on biological sex, gender identity & third-person pronouns

- From here https://github.com/EticaAI/numerordinatio/blob/main/docs/data/exemplum/scientiae-communitatem--sexualitatem.yml
```yaml
# scientiae-communitatem--sexualitatem.yml

# @TODO: maybe ask help about multilingual lexicography of pronouns here:
#       https://github.com/pronouns/main/issues/40

'9999': {}
# ---------------------------------------------------------------------------- #
'9999:1':
  lat-Latn:
    '0': '/corporis sexum/'
  # eng-Latn-x-unhtcds: {}

'9999:1:0':
  eng-Latn-x-iso5218:
    '0': 'Not known'
  zxx-Zmth-x-iso5218-systema:
    '0': '0'

'9999:1:1':
  eng-Latn-x-iso5218:
    '0': 'Male'
  zxx-Zmth-x-iso5218-systema:
    '0': '1'

'9999:1:2':
  eng-Latn-x-iso5218:
    '0': 'Female'
  zxx-Zmth-x-iso5218-systema:
    '0': '2'

'9999:1:9':
  eng-Latn-x-iso5218:
    '0': 'Not applicable'
  zxx-Zmth-x-iso5218-systema:
    '0': '9'

# ---------------------------------------------------------------------------- #
'9999:2':
  lat-Latn:
    '0': 'genus grammaticum'
    '100': https://en.wiktionary.org/wiki/grammaticus#Latin
  eng-Latn-x-unhtcds: {}

# ---------------------------------------------------------------------------- #
'9999:3':
  lat-Latn:
    '0': '//genus sexuicus//'
  eng-Latn-x-unhtcds:
    '0': 'gender'

'9999:3:0':
  eng-Latn-x-unhtcds:
    '0': 'Not Specified/Unknown'
  qcc-Zxxx-x-unhtcds-systema:
    '0': 'NonSpecifiedUnknown'

'9999:3:1':
  eng-Latn-x-unhtcds:
    '0': 'Masculine'
  qcc-Zxxx-x-unhtcds-systema:
    '0': 'Masculine'

'9999:3:2':
  eng-Latn-x-unhtcds:
    '0': 'Feminine'
  qcc-Zxxx-x-unhtcds-systema:
    '0': 'Feminine'

'9999:3:3':
  eng-Latn-x-unhtcds:
    '0': 'Transgender Masculine'
  qcc-Zxxx-x-unhtcds-systema:
    '0': 'TransgenderMasculine'

'9999:3:4':
  eng-Latn-x-unhtcds:
    '0': 'Transgender Feminine'
  qcc-Zxxx-x-unhtcds-systema:
    '0': 'TransgenderFeminine'

'9999:3:9':
  eng-Latn-x-unhtcds:
    '0': 'Non-Conforming'
  qcc-Zxxx-x-unhtcds-systema:
    '0': 'NonConforming'

# ---------------------------------------------------------------------------- #
'9999:4':
  qaa-Zyyy:
    '0': https://en.wikipedia.org/wiki/Preferred_gender_pronoun
    '1': https://en.wikipedia.org/wiki/Gender_neutrality_in_languages_with_gendered_third-person_pronouns
    '2': https://uwm.edu/lgbtrc/support/gender-pronouns/
    '3': https://www.english-grammar-revolution.com/list-of-pronouns.html
    '4': https://motivatedgrammar.wordpress.com/2009/09/10/singular-they-and-the-many-reasons-why-its-correct/
    '5': https://pronouny.xyz/
    '6': https://github.com/pronouns
    '7': https://nonbinary.miraheze.org/wiki/Pronouns
    '8': https://pronouny.xyz/pronouns/list/public

  qaa-Zyyy-picturam:
    '0': https://uwm.edu/lgbtrc/wp-content/uploads/sites/162/2016/04/Pronoun-cards-2016-01-768x439.png
    '1': https://uwm.edu/lgbtrc/wp-content/uploads/sites/162/2016/04/Pronoun-cards-2016-02-768x439.png

  eng-Latn:
    '1': '/third-person pronouns/'

'9999:4:1':
  eng-Latn:
    '0': 'he/him/his/his/himself'
  qaa-Zyyy:
    '0': https://pronouny.xyz/pronouns/56d90b55fcb6e80e00e70678

'9999:4:2':
  qaa-Zyyy:
    '0': https://pronouny.xyz/pronouns/5f0c023bbe30e500157baf45

  eng-Latn:
    '0': 'she/her/her/hers/herself'

# @TODO https://datatracker.ietf.org/doc/html/rfc8141
# @see https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml
# https://github.com/UNMigration/HTCDS
# gender    Feminine    Feminine
# gender    Masculine    Masculine
# gender    TransgenderFeminine    Transgender Feminine
# gender    TransgenderMasculine    Transgender Masculine
# gender    NonConforming    Non-Conforming
# gender    NonSpecifiedUnknown    Not Specified/Unknown

# - generī, https://en.wiktionary.org/wiki/genus#Latin
# - sexum, https://en.wiktionary.org/wiki/sexus#Latin
# - https://en.wiktionary.org/wiki/medicus#Latin
# http://www.perseus.tufts.edu/hopper/morph?l=sexo&la=la#lexicon
# - (sexus) ūs, m  SAC-, a sex (only sing gen . and abl.): hominum genus et in sexu consideratur, virile an muliebre sit: puberes virilis sexūs, L.
# - https://en.wiktionary.org/wiki/-icus#Latin
# - On Grammatical gender, https://en.wiktionary.org/wiki/genus#Latin

# - //gender identity//@eng-Latn
#   - 'sexum generī'
#   - 'genus sexuī'
#   - '//sexugenus//' (see http://www.perseus.tufts.edu/hopper/resolveform?type=end&lookup=genus&lang=la)
#   - 'genus sexuicus'
# - //biological sex//
#   - 'sexum medicō'
#   - 'sexum corporis'
# - Three groups
#   - 'genus sexuicus'
#     - genus sexuicus neutrī̆us (https://en.wiktionary.org/wiki/neuter#Latin)
#   - 'corporis sexum'
#     - 'transsexum'
#   - 'genus grammaticum' (https://en.wiktionary.org/wiki/genus#Latin)
#     - [genus] fēminīnum, [genus] masculīnum, [genus] neutrum, genus commūne, genus omne
# https://github.com/SEMICeu/Core-Person-Vocabulary/raw/master/releases/1.00/Core_Vocabularies-Business_Location_Person-Specification-v1.00.pdf

```

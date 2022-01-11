# `1603:13`

- @see https://hxlstandard.org/

> _Standardising humanitarian data for a better response: The Humanitarian eXchange Language About this case study (...) Start date 1 December 2013_ -- https://www.elrha.org/wp-content/uploads/2017/05/hif-alnap-unocha-exchange-language-case-study-2016-1.pdf (alternative: https://web.archive.org/web/20220111050807/https://www.elrha.org/wp-content/uploads/2017/05/hif-alnap-unocha-exchange-language-case-study-2016-1.pdf)

## Note on numerical decision of 13 as namespace

The _13 (number)_ (see <https://en.wikipedia.org/wiki/13_(number)>) can have differnt meanings, inclusive on western cutures _Triskaidekaphobia_ (<https://en.wikipedia.org/wiki/Triskaidekaphobia>). However:

- For the namespace `1603`, the shortest number non-already used should be chosen. As a starting point, we're using 1 to 99.
- For the namespace `1603`, the default decision on the number is to decide either foundation date or significant historical milestone. For HXLStandand, this maybe could also be 2012, if not earlier. But for now, we will use 2013
- A common practice on scientific nomenclature is to give priority for the first published work. Any `1603:` direct nested item starts to be used with relevant content, even if another organization has the same date, either a new year or a full 4-digit year would need to be decided.

# `1603:13:1603:45:49`

<!--
Using https://en.wikipedia.org/wiki/Percent-encoding as reference of other standards to itself
-->

> https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes

- `1603_13_1603_45_49~1603_47_3166_1`
  - `1603_13_1603_45_49`: HXLstandard point of 1603_13_1603_45_49 (UN m49)
  - `~`: means (on this context) something else pointing to itself
  - `1603_47_3166_1`
    - `1603_47_3166` ISO 3166 (any type), https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
    - `1603_47_3166_1` ISO 3166 part 1 (https://en.wikipedia.org/wiki/ISO_3166-1)
      - Potential subdivisions
        - In the case of ISO, we may just merge all tables together? They do not clash with each other. The problem is how to define in numbers the difference between alpha2 alpha3 and full numeric

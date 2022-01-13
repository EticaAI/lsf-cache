# Numerordĭnātĭo pre-compiled data tables and automation scripts

When referring to concepts, we use as exchange keys numeric codes with explicit self taxonomy.
This decision both allows neutrality when working with multiple cultures, and already will feel familiar for people who have [administrative divisions](https://en.wikipedia.org/wiki/Administrative_division) where the baseline can change depending on who is considered a reference.

In general each group of concepts (for example, codes used in a country to define subdivisions) will not add a prefix for the entire country itself (because everything there _is_ from that country). But at international level, this is relevant, and both `1603:45:49` and `1603:45:16` are the best reference on this subject. Other areas are less complex, but we still use nested nomenclature.

While decisions on how to organize, as of 2021-01, are still open, **such numeric taxonomy can persist more long term**. In the worst case, it is also easier to create direct aliases when working with software.

> Practical example:
> - We opt for _`1603:45:49` /UN m49/_ instead of _`1603:47:3166:1` (the neutral number to reference ISO 3166)_ as the default key to reference one type of concept group.
> - We inject information, in special translations, from namespaces such as _`1603:3:12` /Wikidata/_ on `1603:45:49`.
> - We make sure that the compiled tables in special vocabularies (the translations) have references from where the data was from, so implementers can decide use or not. However the biggest relevance of this is for languages without official translations (even if they do exist, only are not pre-compiled).

## [`1603`] /Base prefix/
- [1603/](1603/)

The multilingual-lexicography-automation project will use `1603` as the main namespace to reference other references.

<!-- > Note: if you need to reuse data and injest full namespace, but "1603" (... todo write more, maybe cite timestamp of https://github.com/HXL-CPLP/forum/blob/master/LICENSE) -->

### [`1603:3`] /Wikimedia Foundation, Inc/
- [1603/3/](1603/3/)

#### [`1603:3:12`] /Wikidata/

### [`1603:13`] /HXL/
- [1603/13/](1603/13/)

### [`1603:45`] /UN/
- [1603/45/](1603/45/)

### [`1603:45:49`] /UN m49/
- [1603/45/49/](1603/45/49/)

### [`1603:45:16`] /Place codes (by UN m49 numeric)/
- [1603/45/16/](1603/45/16/)

> Note: the main interest in multilingual-lexicography-automation is **linguistic content** and how to conciliate data via existing coding systems both for ourselves and third parties **interested in improving multilingualism**. Except for potential data to allow disambiguation which is is not heavyweight (such as centroid coordinates) we do not plan to re-publish administrative boundaries.

### [`1603:47`] /ISO/
- [1603/47/](1603/47/)

#### [`1603:47:15924`] /ISO 15924, Codes for the representation of names of scripts/
- [1603/47/15924/](1603/47/15924/)

### [`1603:87`] /Unicode/
- [1603/87/](1603/87/)

### [`1603:2600`] /Generic - Multiplication tables/
- [1603/2600/](1603/2600/)

## [`1613`] /namespace for handcrafted data/
- [1613/](1613/)

<details>
<summary>Click to see additional iternal data files</summary>

## [`999999`] /namespace for intermediate cached files/
- [999999/](999999/)

## [`999999999`] /namespace for automation scripts/
- [999999999/](999999999/)

</details>

<!--
## License

Except by _[`999999999`] /namespace for automation scripts/_ and _`1613` /namespace for handcrafted data/_

This repository contains mixed license and copyright owners.
-->


## Disclaimers

**Individuals direct and indirect contributors of this project are not affiliated with external organizations. The use of labeled numerical namespaces (need to make easier for implementer) explicitly do not means endorsement of the organizations or theirs internal groups deciding the coding systems.**

Ad-hoc collaboration (such as bug fixes or suggestions to improve interoperability) between @EticaAI / @HXL-CPLP and individuals which work on any specific namespace cannot be considered formal endorsement of their organization.

Even reuse of work (in special pre-compiled translations, or tested workflows on how to re-generate then from external collaborators) cannot be assumed as endorsement by the work on this monorepo and final work do not need to be public domain as the translations. Such feature can also be called [data roundtripping](https://diff.wikimedia.org/2019/12/13/data-roundtripping-a-new-frontier-for-glam-wiki-collaborations/) and can be stimulated on call to actions such as [Wikiprojecs](https://m.wikidata.org/wiki/Wikidata:WikiProjects) or ad hoc initiatives such [TICO-19](https://tico-19.github.io/).

Please note that even successful projects such as GLAM (see [Wikimedia Commons Data Roundtripping Final Report](https://upload.wikimedia.org/wikipedia/commons/e/e8/Wikimedia_Commons_Data_Roundtripping_-_Final_report.pdf)) in addition to lack of more software and workflows, can have issues such as duplication of data import/export because of lack of consistent IDs. So as part of multilingual lexicography, for sake of re usability, we need to give something and already draft how others could do it. A lot of inspiration for this is [strategies used on scientific names](https://en.wikipedia.org/wiki/Scientific_name) (except that you don't need to know Latin grammar).

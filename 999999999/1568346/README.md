# 999999999/1568346
> - https://www.wikidata.org/wiki/Q1568346
>   - > test case (Q1568346)
>   - > _specification of the inputs, execution conditions, testing procedure, and expected results that define a single test to be executed to achieve a particular testing objective_



## RDF + HXL + BCP47
- https://en.wikipedia.org/wiki/Resource_Description_Framework#Vocabulary
- https://github.com/hxl-team/HXL-Vocab/blob/master/Tools/hxl.ttl

## Note on harecoded special cases for cell value expansion: HXL `+rdf_y_*` and BCP47 `-r-y*`

### Explode list of items
Full Example:
- <s>Inspiration: https://www.w3.org/ns/csvw.ttl#separator</s>
- Inspiration: (group separator, ASCII) https://www.wikidata.org/wiki/Q110028713
- HXL hashtag: `#item+rem+i_qcc+is_zxxx+rdf_y_u001d_u007c`
- BCP 47: `qcc-Zxxx-r-yU001D-yu007c-ynop`
- Cell value: `concept4938|concept7597`
  - Transformed result:
    - concept4938
    - concept7597

### Apply prefix to items
Full Example:
- <s>Inspiration: (did exist some namespace for this? Maybe is so basic most tools do it hardcoded)</s>
- Inspiration: (start of text, ASCII) https://www.wikidata.org/wiki/Q10366650
- HXL hashtag: `#item+rem+i_qcc+is_zxxx+rdf_y_u0002_unescothes`
- BCP 47: `qcc-Zxxx-r-yU0002-yunescothes-ynop`
- Cell value: `concept10`
  - Transformed result:
    - unescothes:concept10

### Test data
- 999999999/1568346/data/unesco-thesaurus.tm.hxl.tsv
  - https://vocabularies.unesco.org/exports/thesaurus/latest/unesco-thesaurus.ttl

## To Dos
- https://www.w3.org/wiki/UsingSeeAlso
  - maybe `-r-bVERB-bitem-bnop` ? (this would make result hardcoded to `rdfs:seeAlso`)
  - maybe `-r-bRDFSx1dseeAlso-bitem-bnop` ?

<!--
@TODO add externay key https://www.wikidata.org/wiki/Q69370
@TODO https://oborel.github.io/

- https://raw.githubusercontent.com/oborel/obo-relations/master/core.owl
  - @prefix ro http://purl.obolibrary.org/obo/
  - @prefix obo http://purl.obolibrary.org/obo/
-->

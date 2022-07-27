# 999999999/1568346
> - https://www.wikidata.org/wiki/Q1568346
>   - > test case (Q1568346)
>   - > _specification of the inputs, execution conditions, testing procedure, and expected results that define a single test to be executed to achieve a particular testing objective_



## RDF + HXL + BCP47
- https://en.wikipedia.org/wiki/Resource_Description_Framework#Vocabulary
- https://github.com/hxl-team/HXL-Vocab/blob/master/Tools/hxl.ttl

- _Final_, well formated versions on HXL hashtags and BCP47 version are equivalent.
  - Is possible to convert from both versions column by column,
    **without need to re-calculate context**
  - `BCP47_EX_HXL` on L999999999_0.py is just a syntatic sugar for
    `#item+conceptum+codicem` and `#item+conceptum+numerordinatio`

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
    - `unescothes:concept10`

### Test data
- 999999999/1568346/data/unesco-thesaurus.tm.hxl.tsv
  - https://vocabularies.unesco.org/exports/thesaurus/latest/unesco-thesaurus.ttl

## Note on numeration of abstract groups (used to link columns as concept bags)
Since both Numerordinatio on HXL and BCP47 are equivalent
(without need to re-calculate context of relationships) when merging different
datasets together, for mere sake of convenience (not enforced by tools)
for datasets that already are highly reusable, as mere suggestion:

- Keep in mind that is possible to mark a column as making part of more than
  one "subject group".
  - **The decision of such numbers does not matter for exported output**
    - This is very, very useful for merging RDF triples despite tabular format
      using HXL+RDF / HXL+BCP47 actually having very complext content
      (id est, content that you can "explode" on several graph groups)
- For sake of make simpler for end user, let's assume the "subject group"
  number zero "1" is focused content. So if user trying to merging
    logical groups would start to use "2", then "3", then "4", ...
  - In practice, the only thing tooling do is if you do not provide a concept
    group, it will assume you want "1". But the tooling will work with
    any number bigger than 0

### Suggested "subject group" for country, and administrative boundaries 1 to 6+

- Country:
  - Number: `5000`
  - BCP47 RDF extension part (self): `r-sU2200-s5000-snop`
  - HXL RDF attribute (self): `+rdf_s_u2200_s5000`
- #adm1:
  - Number: `5001`
  - BCP47 RDF extension part (self): `r-sU2200-s5001-snop`
  - HXL RDF attribute (self): `+rdf_s_u2200_s5001`
- #adm2:
  - Number: `5002`
  - BCP47 RDF extension part (self): `r-sU2200-s5002-snop`
  - HXL RDF attribute (self): `+rdf_s_u2200_s5002`
- #adm3:
  - Number: `5003`
  - BCP47 RDF extension part (self): `r-sU2200-s5003-snop`
  - HXL RDF attribute (self): `+rdf_s_u2200_s5003`
- #adm4:
  - Number: `5004`
  - BCP47 RDF extension part (self): `r-sU2200-s5004-snop`
  - HXL RDF attribute (self): `+rdf_s_u2200_s5004`
- #adm5:
  - Number: `5005`
  - BCP47 RDF extension part (self): `r-sU2200-s5005-snop`
  - HXL RDF attribute (self): `+rdf_s_u2200_s5005`
- #adm6:
  - Number: `5006`
  - BCP47 RDF extension part (self): `r-sU2200-s506-snop`
  - HXL RDF attribute (self): `+rdf_s_u2200_s506`


> Note: since is possible to mark columns with more than one subject group,
> by this convention if the content you want already is not a final
> dataset, for a dataset that is for example about #adm3, you could:
>
> - #adm3:
>   - Number: `5003` and `1`
>   - BCP47 RDF extension part (self): `r-sU2200-s1-snop-sU2200-s5003-snop`
>   - HXL RDF attribute (self): `+rdf_s_u2200_s1+rdf_s_u2200_s5003`

## GeoJSON
> Initial discussion at https://github.com/EticaAI/lexicographi-sine-finibus/issues/48

- Temporary example: https://geojson.io/#data=data:text/x-url,https://raw.githubusercontent.com/EticaAI/lsf-cache/main/1603/16/1/0/1603_16_1_0.data.ld.geojson
  - https://jsonschema.dev/
  - https://json-ld.org/playground/
    - https://www.easyrdf.org/converter
## Other links
<!--

- This one have example with a lot of data
  - https://github.com/geojson/schema/issues/33
- Using @id to interlink things
  - http://niem.github.io/json/reference/json-ld/identifiers/
- https://jsonschema.dev/
- https://code.visualstudio.com/docs/languages/json
- https://json-schema.org/
- https://json-ld.org/spec/ED/json-ld-syntax/20120122/

- Playground
  - https://json-ld.org/playground/
    - https://www.easyrdf.org/converter


pip install jsonschema

jsonschema --instance sample.json sample.schema


curl https://geojson.org/schema/GeoJSON.json --output 999999/0/GeoJSON-schema.json

jsonschema --instance 999999999/1568346/data/cod-ab-example2.geojson 999999/0/GeoJSON-schema.json
-->

# To Dos
- improve baseline relations with SKOS even when loading a single file
  (e.g. show the entire previous parents)
- Change the new implementation to divide the SKOS and OWL format
- Automate entrypoint files to import other data
- https://www.w3.org/wiki/UsingSeeAlso
  - maybe `-r-bVERB-bitem-bnop` ? (this would make result hardcoded to `rdfs:seeAlso`)
  - maybe `-r-bRDFSx1dseeAlso-bitem-bnop` ?
- `urn:uuid:`
  - beyond `urn:mdciii:` prefix, potentially create some built-in `urn:uuid`
    to unique items.
- `urn:(hash-term)`
  - Same as `urn:uuid:`, but with somewhat predictable output

<!--
@TODO add externay key https://www.wikidata.org/wiki/Q69370
@TODO https://oborel.github.io/

- https://raw.githubusercontent.com/oborel/obo-relations/master/core.owl
  - @prefix ro http://purl.obolibrary.org/obo/
  - @prefix obo http://purl.obolibrary.org/obo/
-->

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

## Note on harecoded special cases for cell value expansion: HXL `+rdf_t_xsd_datetime*` and BCP47 `-r-y*`
Full example:

- `xsd:dateTime`
  - HXL attribute: `#item+rem+i_qcc+is_zxxx+rdf_t_xsd_datetime`
  - BPC 47 part attribute: `qcc-Zxxx-r-tXSD-tdatetime-tnop`

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

### How to merge back all data files with geojson
> TODO needs testing:
>
> - https://stackoverflow.com/questions/60228327/use-jq-to-merge-keys-with-common-id
> - https://stackoverflow.com/questions/71563226/combine-two-jsons-by-key-using-jq
> - https://stackoverflow.com/questions/72609247/jq-how-to-left-join-and-merge-fields-from-two-input-json-files

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

## Attempting to deal with complex relations (maybe qualifiers)
- https://www.wikidata.org/wiki/Help:Qualifiers
  - https://www.wikidata.org/wiki/Q7742
    - https://www.wikidata.org/wiki/Special:EntityData/Q7742.ttl

```bash
curl https://www.wikidata.org/wiki/Special:EntityData/Q7742.ttl --output 999999/0/Q7742.ttl

rdfpipe --input-format=turtle --output-format=longturtle 999999/0/Q7742.ttl > 999999/0/Q7742~norm.ttl
```

- https://en.wikipedia.org/wiki/ISO_8601#Years
  - `urn:hxla:+iso8601v2022`, year 2022 (https://en.wikipedia.org/wiki/ISO_8601)
  - `urn:hxla:+iso3166p1v076`, country/territory Brazil (BR/BRA/076) (https://en.wikipedia.org/wiki/ISO_3166-1)
  - `urn:hxla:+iso5218v0`, sex Not known (https://en.wikipedia.org/wiki/ISO/IEC_5218)
  - `urn:hxla:+iso5218v1`, sex Male
  - `urn:hxla:+iso5218v2`, sex Female
  - `urn:hxla:+iso5218v9`, sex Not applicable
  - Compositions, need sorting
    - `urn:hxla:+iso5218v2+iso8601v2022`; sex Female && year 2022


```ttl
## 999999/0/poc.ttl
# https://censo2010.ibge.gov.br/noticias-censo.html?busca=1&id=3&idnoticia=1766&t=censo-2010-populacao-brasil-190-732-694-pessoas&view=noticia

PREFIX hxla: <urn:hxla:>
PREFIX wdata: <http://www.wikidata.org/wiki/Special:EntityData/>

<urn:example:BR>
    wdata:P1082 [
            hxla:iso8601v2010 "190732694" ;
            hxla:iso8601v2020 "123456"
        ] ;
    wdata:P1539 [
            hxla:iso8601v2010 "97342162" ;
            hxla:iso8601v2020 "123456"
        ] ;
    wdata:P1540 [
            hxla:iso8601v2010 "97342162" ;
            hxla:iso8601v2020 "123456"
        ] ;
.
```

```trig
@prefix wdata: <http://www.wikidata.org/wiki/Special:EntityData/> .

#<urn:hxla:+iso3166p1v076> <http://www.wikidata.org/wiki/Special:EntityData/P1540> "93390532" <urn:hxla:iso8601v2010> .
<urn:example:BR> <http://www.wikidata.org/wiki/Special:EntityData/P1540> "93390532" .

<urn:hxla:iso8601v2010> {
    <urn:example:BR> wdata:P1082 "190732694" ;
        wdata:P1539 "97342162" ;
        wdata:P1540 "93390532" .
}

```

```nq
### 999999/0/poc.nq
<urn:hxla:+iso3166p1v076> <http://www.wikidata.org/wiki/Special:EntityData/P1082> "190732694" <urn:hxla:+iso8601v2010> .
<urn:hxla:+iso3166p1v076> <http://www.wikidata.org/wiki/Special:EntityData/P1539> "97342162" <urn:hxla:+iso8601v2010> .
<urn:hxla:+iso3166p1v076> <http://www.wikidata.org/wiki/Special:EntityData/P1540> "93390532" <urn:hxla:+iso8601v2010> .

```

rdfpipe --input-format=turtle --output-format=longturtle 999999/0/poc.ttl
rdfpipe --input-format=trig --output-format=trig --ns=hxla=urn:hxla 999999/0/poc.trig

rdfpipe --input-format=trig --output-format=json-ld --ns=hxla=urn:hxla: 999999/0/poc.trig


### Attempt 3

rdfpipe --input-format=turtle --output-format=longturtle --ns=ix=urn:hxl:vocab:a:ix: 999999/0/poc-3.ttl

```ttl
# 999999/0/poc-3.ttl
PREFIX ix: <urn:hxl:vocab:a:ix:>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX wdata: <http://www.wikidata.org/wiki/Special:EntityData/>

<urn:mdciii:1603:992:1:0:1>
    a
        owl:Thing ,
        skos:Concept ;
    rdfs:label "1603:992:1:0:1" ;
    wdata:P1082 _:b1 
        # "54208" ,
        # "55434" ,
        # "56234" ,
        # "56699" ,
        # "57029" ,
        # "57357" ,
        # "57702" ,
        # "58044" ,
        # "58377" ,
        # "58734" ;
.

_:b1 <urn:hxl:vocab:a:ix:iso8601v1960> "54208" .
_:b1 <urn:hxl:vocab:a:ix:iso8601v1961> "55434" .
_:b1 <urn:hxl:vocab:a:ix:iso8601v1962> "56234" .
_:b1 <urn:hxl:vocab:a:ix:iso8601v1963> "56699" .
_:b1 <urn:hxl:vocab:a:ix:iso8601v1965> "57029" .

```
#### Result
```ttl
PREFIX ix: <urn:hxl:vocab:a:ix:>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX wdata: <http://www.wikidata.org/wiki/Special:EntityData/>

<urn:mdciii:1603:992:1:0:1>
    a
        owl:Thing ,
        skos:Concept ;
    rdfs:label "1603:992:1:0:1" ;
    wdata:P1082 [
            ix:iso8601v1960 "54208" ;
            ix:iso8601v1961 "55434" ;
            ix:iso8601v1962 "56234" ;
            ix:iso8601v1963 "56699" ;
            ix:iso8601v1965 "57029"
        ] ;
.

```

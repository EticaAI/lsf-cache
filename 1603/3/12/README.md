# [`1603:3:12`] /Wikidata/

- "Wikidata:Database reports/List of properties/all"
  - https://www.wikidata.org/wiki/Wikidata:Database_reports/List_of_properties/all


## Example queries

### all languages and their items
- Thanks https://stackoverflow.com/questions/43258341/how-to-get-wikidata-labels-in-more-than-one-language

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT DISTINCT ?RegionIT ?label (lang(?label) as ?label_lang) ?ISO_code ?Geo
{
?RegionIT wdt:P31 wd:Q16110;
wdt:P300 ?ISO_code; 
wdt:P625 ?Geo ;
rdfs:label ?label
}
order by ?RegionIT
```

[LINK](https://query.wikidata.org/#PREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20wikibase%3A%20%3Chttp%3A%2F%2Fwikiba.se%2Fontology%23%3E%0APREFIX%20wd%3A%20%3Chttp%3A%2F%2Fwww.wikidata.org%2Fentity%2F%3E%0APREFIX%20wdt%3A%20%3Chttp%3A%2F%2Fwww.wikidata.org%2Fprop%2Fdirect%2F%3E%0A%0ASELECT%20DISTINCT%20%3FRegionIT%20%3Flabel%20%28lang%28%3Flabel%29%20as%20%3Flabel_lang%29%20%3FISO_code%20%3FGeo%0A%7B%0A%3FRegionIT%20wdt%3AP31%20wd%3AQ16110%3B%0Awdt%3AP300%20%3FISO_code%3B%20%0Awdt%3AP625%20%3FGeo%20%3B%0Ardfs%3Alabel%20%3Flabel%0A%7D%0Aorder%20by%20%3FRegionIT)


### TODOs

#### Languages codes
- https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#All_languages_with_a_Wikimedia_language_code_(P424)

#### UN agengies et al
- https://www.wikidata.org/wiki/Q15285626
- https://www.wikidata.org/wiki/Q15285626
- https://www.wikidata.org/wiki/Q854218
- https://w.wiki/4gxT

```
# Variant of
# - https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#UN_member_states
# - https://stackoverflow.com/questions/43258341/how-to-get-wikidata-labels-in-more-than-one-language
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

#SELECT DISTINCT ?adm0 ?iso3166p1n ?label (lang(?label) as ?label_lang)
SELECT DISTINCT ?iso3166p1n ?label (lang(?label) as ?label_lang)
{
  ?adm0 wdt:P31/wdt:P279* wd:Q3624078;
  rdfs:label ?label
  OPTIONAL { ?adm0 wdt:P2082|wdt:P299 ?iso3166p1n. }
  
  #FILTER(?iso3166p1n > xsd:integer(0))
}
# order by ?adm0
order by ASC(?iso3166p1n)
LIMIT 1000
```

```txt
wdtaxonomy Q15285626
organization established by the United Nations (Q15285626) •1 ×64 ↑
├──principal organ of the United Nations (Q15899789) •3 ×7
├──specialized agency of the United Nations (Q15925165) •5 ×25 ↑
├──Human Rights Council Subsidiary Body (Q78933945) ×3
├──charter-based human rights body (Q79148250) ×5
└──treaty-based human rights body (Q79699511) ×9

wdtaxonomy --reverse Q15285626
```

<!--

PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT DISTINCT ?RegionIT ?label (lang(?label) as ?label_lang) ?ISO_code ?Geo
{
?RegionIT wdt:P31/wdt:P279* wd:Q3624078;
rdfs:label ?label
}
order by ?RegionIT


-->

# [`1603:3`] /Commūnitās scientiae/

> _Wikimedia Foundation, Inc. (WMF, or simply Wikimedia) is an American foundation headquartered in San Francisco, California.[9] It owns and operates the Wikimedia projects.[10][11][12][13]. It was established in **2003** by Jimmy Wales as a way to fund Wikipedia and its sibling projects through non-profit means.[1][2] As of 2021, it employs over 550 staff and contractors, with annual revenues in excess of US$150 million._ -- https://en.wikipedia.org/wiki/Wikimedia_Foundation

### 1603:3.1 (Wikipedia)
> _Launched	January 15, 2001 (20 years ago) _ -- https://en.wikipedia.org/wiki/Wikipedia

### 1603:3.2 (Wikitionary)
> _Wiktionary was brought online on December 12, **2002**,[2] following a proposal by Daniel Alston and an idea by Larry Sanger, co-founder of Wikipedia.[3] _ -- https://en.wikipedia.org/wiki/Wiktionary

### 1603:3.4 (Wikimedia Commons)
> _The project was proposed by Erik Möller in March 2004 and launched on September 7, **2004**. _ -- https://en.wikipedia.org/wiki/Wikimedia_Commons

### [`1603:3.12`] /Vicidata/
> _Wikidata is a collaboratively edited multilingual knowledge graph hosted by the Wikimedia Foundation.[2] It is a common source of open data that Wikimedia projects such as Wikipedia,[3][4] and anyone else, can use under the **CC0 public domain license**. Wikidata is a wiki powered by the software MediaWiki, and is also powered by the set of knowledge graph MediaWiki extensions known as Wikibase. (...) Launched29 October **2012**; 9 years ago[1] (...) Logo
The bars on the logo contain the word "WIKI" encoded in Morse code.[38] It was created by Arun Ganesh and selected through community decision.[39]_ -- https://en.wikipedia.org/wiki/Wikidata

### Latinas viva ad anglicum "Wikidata"
<s>
- Vicipaedia, Vicipædia, https://la.wikipedia.org/wiki/Vicipaedia
  - vicī, https://en.wiktionary.org/wiki/vicis#Latin
  - paedīa, f, singular, https://en.wiktionary.org/wiki/paedia
- data, https://en.wiktionary.org/wiki/datus#Latin
- "vicīdatum"
</s>
- https://la.wikipedia.org/wiki/Vicipaedia:Pagina_prima as 2022-01-27 uses "Vicidata"


- https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual
- https://www.wikidata.org/wiki/Wikidata:In_one_page
  - https://upload.wikimedia.org/wikipedia/commons/8/8d/Wikidata-in-brief-1.0.pdf
- https://sinaahmadi.github.io/posts/10-essential-sparql-queries-for-lexicographical-data-on-wikidata.html
- https://en.wikibooks.org/wiki/SPARQL

> TODO: is possible also generate diffs; see
> - https://www.wikidata.org/wiki/Help:Wikimedia_language_codes/lists/all
>   - https://wikidata-todo.toolforge.org/sparql_rc.php?start=last+week&end=&user_lang=&sort_mode=last_edit&no_bots=1&skip_unchanged=1&sparql=SELECT%0A%20%20%3Fitem%20%0A%20%20%3Fc%20%28CONTAINS%28%3Fc%2C%22-%22%29%20as%20%3Fsubtag%29%0A%20%20%3Fwdlabelen%0A%20%20%28CONCAT%28%22%5B%5B%3Aen%3A%22%2C%3Fenwikipeda%2C%22%5Cu007C%22%2C%3Fenwikipeda%2C%22%5D%5D%22%29%20as%20%3Fwikipedia_link_en%29%0A%20%20%3Flang%0A%20%20%3Fwdlabelinlang%0A%20%20%28CONCAT%28%22%5B%5B%3A%22%2C%3Flang%2C%22%3A%22%2C%3Fwikipeda%2C%22%5Cu007C%22%2C%3Fwikipeda%2C%22%5D%5D%22%29%20as%20%3Fwikipedia_link%29%0AWHERE%0A%7B%0A%20%20VALUES%20%3Flang%20%7B%20%22fr%22%20%7D%0A%20%20%3Fitem%20wdt%3AP424%20%3Fc%20.%0A%20%20hint%3APrior%20hint%3ArangeSafe%20true%20.%0A%20%20MINUS%7B%3Fitem%20wdt%3AP31%20wd%3AQ47495990%7D%0A%20%20MINUS%7B%3Fitem%20wdt%3AP31%2Fwdt%3AP279%2A%20wd%3AQ14827288%7D%20%23exclude%20Wikimedia%20projects%0A%20%20MINUS%7B%3Fitem%20wdt%3AP31%2Fwdt%3AP279%2A%20wd%3AQ17442446%7D%20%23exclude%20Wikimedia%20internal%20stuff%0A%20%20OPTIONAL%20%7B%20%3Fitem%20rdfs%3Alabel%20%3Fwdlabelinlang%20.%20FILTER%28%20lang%28%3Fwdlabelinlang%29%3D%20%22fr%22%20%29%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fitem%20rdfs%3Alabel%20%3Fwdlabelen%20.%20FILTER%28lang%28%3Fwdlabelen%29%3D%22en%22%29%20%7D%0A%20%20OPTIONAL%20%7B%20%5B%5D%20schema%3Aabout%20%3Fitem%20%3B%20schema%3AinLanguage%20%3Flang%3B%20schema%3AisPartOf%20%2F%20wikibase%3AwikiGroup%20%22wikipedia%22%20%3B%20schema%3Aname%20%3Fwikipeda%20%7D%20%0A%20%20OPTIONAL%20%7B%20%5B%5D%20schema%3Aabout%20%3Fitem%20%3B%20schema%3AinLanguage%20%22en%22%3B%20schema%3AisPartOf%20%2F%20wikibase%3AwikiGroup%20%22wikipedia%22%20%3B%20schema%3Aname%20%3Fenwikipeda%20%7D%20%0A%7D%0AORDER%20BY%20%3Fc


### [`1603:3.12:6`] /Speciālis 	collēctiōnī de Vicidata Proprietātī/
- speciālis, f/m, singular, https://en.wiktionary.org/wiki/specialis#Latin
- collēctiōnī, f, singular, (Nominative) https://en.wiktionary.org/wiki/collectio#Latin
- collēctiō, f, singular, (Nominative) https://en.wiktionary.org/wiki/collectio#Latin
- sēlēcta, n, sēlēcta

### [`1603:3.12:16`] //Speciālis collēctiōnī de Vicidata Proprietātī//

#### Latinas viva ad anglicum "Wikidata"
- Vicidata, as 2022-01-27, https://la.wikipedia.org/wiki/Vicipaedia:Pagina_prima
- proprietātī, https://en.wiktionary.org/wiki/proprietas#Latin
- //Speciālis collēctiōnī de Vicidata Proprietātī//

### [`1603:3.12:17`] /Vicidata identitātī/
- Vicidata, as 2022-01-27, https://la.wikipedia.org/wiki/Vicipaedia:Pagina_prima
- https://www.wikidata.org/wiki/Q43649390
- identitātī, f, singular, (Dative), https://en.wiktionary.org/wiki/identitas#Latin
- identitāte, f, singular, (Ablative), https://en.wiktionary.org/wiki/identitas#Latin
- rēs, f, singular (Nominative), https://en.wiktionary.org/wiki/res#Latin
- "Vicidata rēs identitāte"


### [`1603:3.1603:45:1`] //

- Fontem: [../45/1/1603_45_1.no1.tm.hxl.csv](../45/1/1603_45_1.no1.tm.hxl.csv)

Exemplum:
```
Q1065	UN
Q15925165	
Q82151	FAO
Q125761	ICAO
Q689859	IFAD
Q54129	ILO
Q7804	IMF
```
- https://www.wikidata.org/wiki/Wikidata:Lexicographical_data

<!--
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
-->

<!--
# https://stackoverflow.com/questions/46291486/wikidata-query-service-how-do-i-search-by-item
# https://query.wikidata.org/#SELECT%20DISTINCT%20%3Fadm0%20%3Flabel%20%28lang%28%3Flabel%29%20as%20%3Flabel_lang%29%0A%7B%0A%20%20%3Fadm0%20wdt%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3624078%3B%0A%20%20rdfs%3Alabel%20%3Flabel%0A%20%20VALUES%20%3Fadm0%20%7B%20wd%3AQ1065%20wd%3AQ986%20wd%3AQ983%20wd%3AQ974%7D%0A%20%20%23%20FILTER%20%28%3Fadm0%20IN%20%28wd%3AQ114%2C%20wd%3AQ181795%29%29%0A%7D%0Aorder%20by%20DESC%28%3Fadm0%29%20ASC%28%3Flabel_lang%29%0ALIMIT%201000

SELECT DISTINCT ?adm0 ?label (lang(?label) as ?label_lang)
{
  ?adm0 wdt:P31/wdt:P279* wd:Q3624078;
  rdfs:label ?label
  VALUES ?adm0 { wd:Q1065 wd:Q986 wd:Q983 wd:Q974}
  # FILTER (?adm0 IN (wd:Q114, wd:Q181795))
}
order by DESC(?adm0) ASC(?label_lang)
LIMIT 1000
-->


<!--
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT DISTINCT ?item ?label (lang(?label) as ?label_lang)
{
  ?item wdt:P31/wdt:P279* wd:Q15925165;
  rdfs:label ?label
  VALUES ?item { wd:Q356694 wd:Q161718 wd:Q82151 wd:Q7809}

}
order by DESC(?adm0) ASC(?label_lang)
LIMIT 1000

-->

<!--
## https://w.wiki/4igC
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT DISTINCT ?item ?label (lang(?label) as ?label_lang)
{
  ?item wdt:P31/wdt:P279* wd:Q15925165;
  rdfs:label ?label
  VALUES ?item { wd:Q356694 wd:Q161718 wd:Q82151 wd:Q7809}

}
order by DESC(?adm0) ASC(?label_lang)
LIMIT 1000

-->


<!--
# https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples/en#The_number_of_existing_translations_for_diseases_in_Wikidata

https://query.wikidata.org/#SELECT%20%3Fdisease%20%3Fdoid%20%3FenLabel%20%28count%28%3Flanguage%29%20as%20%3Flanguages%29%0AWHERE%0A%7B%0A%20%20%3Fdisease%20wdt%3AP699%20%3Fdoid%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20rdfs%3Alabel%20%3Flabel%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20rdfs%3Alabel%20%3FenLabel%20.%0A%20%20%20%20FILTER%20%28lang%28%3FenLabel%29%20%3D%20%22en%22%29%0A%20%20%20%0A%20%20%20%20BIND%20%28lang%28%3Flabel%29%20AS%20%3Flanguage%29%0A%7D%0Agroup%20by%20%3Fdisease%20%3Fdoid%20%3FenLabel%0Aorder%20by%20desc%28%3Flanguages%29


SELECT ?disease ?doid ?enLabel (count(?language) as ?languages)
WHERE
{
  ?disease wdt:P699 ?doid ;
             rdfs:label ?label ;
             rdfs:label ?enLabel .
    FILTER (lang(?enLabel) = "en")
   
    BIND (lang(?label) AS ?language)
}
group by ?disease ?doid ?enLabel
order by desc(?languages)
-->

<!--
 ## Debug query about an item

https://w.wiki/5BAE

https://stackoverflow.com/questions/46383784/wikidata-get-all-properties-with-labels-and-values-of-an-item

```sql
SELECT ?wdLabel ?ps_Label ?wdpqLabel ?pq_Label {
  VALUES (?company) {(wd:Q174)}
  
  ?company ?p ?statement .
  ?statement ?ps ?ps_ .
  
  ?wd wikibase:claim ?p.
  ?wd wikibase:statementProperty ?ps.
  
  OPTIONAL {
  ?statement ?pq ?pq_ .
  ?wdpq wikibase:qualifier ?pq .
  }
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
} ORDER BY ?wd ?statement ?ps_
```

-->

----

<!-- ### Neo latin term for citizen science
- https://www.wikidata.org/wiki/Q1093434

- commūnitās, f, nominative, https://en.wiktionary.org/wiki/communitas#Latin
- scientiae, f, https://en.wiktionary.org/wiki/scientia#Latin -->

<!--

Multiple languages of same item
- https://w.wiki/iRT
- https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#Names_of_Wikipedia_articles_in_multiple_languages

-->

<!--
Tool for bulk import:
- https://www.wikidata.org/wiki/Help:QuickStatements
-->

### Query - all languages of an article

1. Va em https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=272891124
2. Cole a coluna em R27 em diante
3. Formula em S27 `=SORT(if(COUNTIF(J27:J,R27:R)=0,R27:R,))`


```
SELECT DISTINCT ?lang ?name WHERE {
  ?article schema:about wd:Q1065 ;
              schema:inLanguage ?lang ;
              schema:name ?name ;
              schema:isPartOf [ wikibase:wikiGroup "wikipedia" ] .
  #FILTER(?lang in ('en', 'uz', 'ru', 'ko')) .
  FILTER (!CONTAINS(?name, ':')) .
} ORDER BY ASC (?lang)
```

### Self notes

- Help:Wikimedia language codes/lists/all
  - https://www.wikidata.org/wiki/Help:Wikimedia_language_codes/lists/all

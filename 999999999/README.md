# [`999999999`] /namespace for automation scripts/

<!--
Self notes;

- Style guide
  - https://google.github.io/styleguide/shellguide.html
- sed
  - GNU sed:
    - https://www.gnu.org/software/sed/manual/sed.html
  - BSD sed:
    - https://www.freebsd.org/cgi/man.cgi?query=sed


- Testing ascidoctor-web-pdf
  - https://github.com/Mogztter/asciidoctor-web-pdf

npm init -y
npm i @asciidoctor/core asciidoctor-pdf --save-dev
npx asciidoctor-web-pdf --version
npx asciidoctor-web-pdf document.adoc
npx asciidoctor-web-pdf 1603/63/101/1603_63_101.mul-Latn.codex.adoc
npx asciidoctor-web-pdf --preview 1603/63/101/1603_63_101.mul-Latn.codex.adoc
npx asciidoctor-web-pdf --preview 1603/1/7/1603_1_7.mul-Latn.codex.adoc

- https://linkml.io/linkml/intro/install.html

pip install linkml

vim 999999/0/personinfo.yaml
# https://linkml.io/linkml/intro/tutorial01.html#your-first-schema

gen-json-schema 999999/0/personinfo.yaml | jq
vim 999999/0/data.yaml
# id: ORCID:1234
# full_name: Clark Kent
# age: 32
# phone: 555-555-5555

linkml-validate -s 999999/0/personinfo.yaml 999999/0/data.yaml

vim 999999/0/bad-data.yaml
# id: ORCID:1234
# full_name: Clark Kent
# age: 32
# phone: 555-555-5555
# made_up_field: hello

linkml-validate -s 999999/0/personinfo.yaml 999999/0/bad-data.yaml

linkml-convert -s 999999/0/personinfo.yaml 999999/0/data.yaml -o 999999/0/data.ttl


vim 999999/0/data-2.yaml
#  persons:
#    - id: ORCID:1234
#      full_name: Clark Kent
#      age: 32
#      phone: 555-555-5555
#    - id: ORCID:4567
#      full_name: Lois Lane
#      age: 33

vim 999999/0/personinfo-2.yaml
# https://linkml.io/linkml/intro/tutorial02.html#nesting-lists-of-objects

linkml-validate -s 999999/0/personinfo-2.yaml 999999/0/data-2.yaml

gen-yuml -f yuml 999999/0/personinfo-2.yaml

gen-yuml --format png 999999/0/personinfo-2.yaml  > 999999/0/personinfo-2.png
gen-yuml --format svg 999999/0/personinfo-2.yaml  > 999999/0/personinfo-2.svg

# https://linkml.io/linkml/generators/json-schema.html

gen-json-schema 999999/0/personinfo-2.yaml > 999999/0/personinfo-2.schema.json

gen-graphql 999999/0/personinfo-2.yaml > 999999/0/personinfo-2.graphql

# https://linkml.io/linkml/generators/excel.html#command-line
gen-excel 999999/0/personinfo-2.yaml --output 999999/0/personinfo-2.xlsx
gen-excel --metadata 999999/0/personinfo-2.yaml --output 999999/0/personinfo-2.xlsx

### @TODOs
- learn to manipulate geopackages (SQLite) with python
  - https://gis.stackexchange.com/questions/342855/reading-geopackage-geometries-in-python
  - hummm, VSCode extensions
    - https://github.com/RandomFractals/geo-data-viewer
-->

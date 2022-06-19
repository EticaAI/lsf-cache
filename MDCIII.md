# MDCIII
- [MDCIII.owl](MDCIII.owl)


## Online tools / Debug
- https://service.tib.eu/webvowl/#iri=https://raw.githubusercontent.com/EticaAI/lexicographi-sine-finibus/main/officina/MDCIII.owl


## Temporary referentes (need reorganization)

### Repositories / Index
- https://bartoc.org/registries

### Research
- **2013 (...)**
  - https://github.com/hxl-team/HXL-Vocab/blob/master/Tools/hxl.ttl
- **2018 empathi: An ontology for Emergency Managing and Planning about Hazard Crisis**
  - Paper: https://arxiv.org/pdf/1810.12510.pdf
  - Documentation: https://shekarpour.github.io/empathi.io/
  - Namespace: https://w3id.org/empathi/
  - OWL (Direct link): https://raw.githubusercontent.com/shekarpour/empathi.io/master/empathi.owl
- (...)
- **2021 Implementation of FAIR Principles for Ontologies in the Disaster Domain: A Systematic Literature Review**
  - https://www.mdpi.com/2220-9964/10/5/324/pdf
    - List to other papers:
      - https://github.com/mazimweal/mazimweal.github.io/blob/master/FAIR%20disaster%20vocabularies/SLR_selected_papers.csv


## Conventions

- `urn:mdciii:1603:16:24:0`
  - **Particular** (or a instance_of)
  - Country of Angola (Administrative Boundaries 0 = Country in this case)
- `urn:mdciii:1603:16:24()`, `urn:mdciii:1603:16()`
  - **Universal** (or a class)
  - This type of pattern is used inside RDF files to make distinction between
    universals and particulars (and this distinction is very important)
- `urn:mdciii:1603:1:1603(0)`
  - The number inside `()` is used to reference something outside the data
    itself. So is not mere a **Universal** (or a class) but a resource to a
    file
    - In this case, `0` is used for boostrapping resources which explain other
      resources, like `1603/1/1603/1603_1_1603.owl`
- `urn:mdciii:1603:16:24:0(1)`
  - Reference to a resource (often a file) that contain data related with
    `urn:mdciii:1603:16:24:0` particulars (or isntance_of).
      In this case is only one particular (country of Angola)
    - Example: `1603/16/24/0/1603_16_24_0.no1.owl.ttl`

- Trivia: the `(` (see https://www.compart.com/en/unicode/category/Ps) and
  `)` (see https://www.compart.com/en/unicode/category/Pe) the same way the
  numbers are not not strictly `0123456789` and the separator varies by context
  (most used ones: `:`, `_` and `/`) could be replaced by other respective
  Unicode Ps and Unicode Pe.

### TODOs
- Improve file extensiosn generated. Maybe we should save Protege files
  on XML format with `owl.owx` extension?
  - https://github.com/protegeproject/protege/issues/969#issuecomment-755985817

<!--

Missing translations to portuguese from BFO 2020:

- Need translations review (source updated): BFO_0000142, BFO_0000147, BFO_0000146;
- needs new translation BFO_0000202, BFO_0000203; definitions not added; properties still need translation
-->

# [`999999`] /Data temporāriīs/

TL;DR:
- _"[`999999999`] /namespace for automation scripts/"_  + _"[`1613`] /namespace for handcrafted data/"_ can be used to generate this directory automatically.
- A pre-build version is availible at https://github.com/EticaAI/n-data/tree/main/999999.
  - Please see license notice

## License notice

Content from `999999` on multilingual-lexicography-automation **are not** intended for final distribution.

However, they may be used to contact data providers about inconsistencies between different sources. This task is relevant as often source providers are manual work done by humans, and this can contain errors when comparing with other data sources.

### Reasoning for pre-cached versions
For similar reasons to projects such as _Unicode Common Locale Data Repository_ <https://github.com/unicode-org/cldr> (which also have pre-cached external sources, see for example [common/properties/external_data_versions.tsv](https://github.com/unicode-org/cldr/blob/main/common/properties/external_data_versions.tsv)), the reason for cached version is tecnical:

- The uptime of external sources is not 100%. And even if they could be, automation scripts can be pretty intense. This alternative allows comply with API etiquetes. See for example [MediaWiki API:Etiquette](https://www.mediawiki.org/wiki/API:Etiquette)
- Not rare, new versions can break automation pipelines and without such cache, the cascading effect could be disastrous.
  - Practical example on [datasets/un-locode](https://github.com/datasets/un-locode/commit/1f751a962b86cbb2d53f1c5d8a691adac3dd5cf7) about line break fix from https://unece.org/trade/cefact/unlocode-code-list-country-and-territory

## Send feedback

In case any copyright holder wants more information or requests removal, please contact members of https://github.com/EticaAI. We will respond from 8h to 72h (including holidays).

# 1603/16/1/README.md

- https://unstats.un.org/unsd/methodology/m49/
- https://en.wikipedia.org/wiki/UN_M49
- https://docs.google.com/spreadsheets/d/1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596

## Challanges
- At first, we will store "all" the territories into 0, but the actual
  way UN M49 is otganized it have several levels.
  - Example:
    - first level = World
    - second level = Africa, Antartica, Americas, Asia, Europe, Oceania
  - However, already after the third level, the first country-like codes will
    appear. But other regions will have further divisions under deeper levels.
- At first, we may not implement the intermediate levels, but we can eventually
  use then to group other concepts.
  - On RDF form, it migth be far easier to make sense of this organization.

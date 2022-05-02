source 'https://rubygems.org'
gem 'asciidoctor'
gem 'asciidoctor-pdf'
gem 'asciidoctor-epub3'
# The next one will require system dependencies, see comments
gem 'prawn-gmagick'
gem 'rouge'

# This one could be a license issue. Is only used to compress the public domain PDFs
# and, with hexapdf, is AGPL
# gem 'rghost'

## PDF compression
# https://pdfbox.apache.org/1.8/commandline.html
# https://en.wikipedia.org/wiki/List_of_PDF_software
# https://github.com/asciidoctor/docker-asciidoctor/issues/111
gem 'hexapdf'

### gem 'prawn-gmagick' dependencies ___________________________________________
# 'asciidoctor: WARNING: GIF image format not supported. Install the prawn-gmagick gem or convert'
# @see https://github.com/asciidoctor/docker-asciidoctor/issues/121
# sudo apt install graphicsmagic-dev
# sudo apt install ruby-dev musl-dev gcc
# sudo gem install prawn-gmagick

# bundle gem install prawn-gmagick -v '0.0.9' --source 'https://rubygems.org/

# via https://github.com/packetmonkey/prawn-gmagick/issues/9#issuecomment-456834606
#    sudo apt-get install -y build-essential libgraphicsmagick1-dev
#    sudo apt-get install -y graphicsmagick-imagemagick-compat graphicsmagick-libmagick-dev-compat


### Other comments _____________________________________________________________

## PDF export

# @see https://asciidoctor.org/#bundler
# cd officinam
# bundle install
# bundle exec asciidoctor-pdf -v

# @TODO - https://docs.asciidoctor.org/asciidoctor/latest/localization-support/
#       - https://github.com/asciidoctor/asciidoctor/issues/1601
#       - https://docs.asciidoctor.org/asciidoc/latest/attributes/document-attributes-ref/#builtin-attributes-i18n

# Exempla
#   ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_25_1 > 1603/25/1/1603_25_1.mul-Latn.codex.adoc
#   bundle exec asciidoctor-pdf 1603/25/1/1603_25_1.mul-Latn.codex.adoc
#
#   ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_25_1 > 1603/25/1/1603_25_1.mul-Latn.codex.adoc ; bundle exec asciidoctor-pdf --attribute optimize=screen 1603/25/1/1603_25_1.mul-Latn.codex.adoc ; evince 1603/25/1/1603_25_1.mul-Latn.codex.pdf
#   ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_45_1 > 1603/45/1/1603_45_1.mul-Latn.codex.adoc ; bundle exec asciidoctor-pdf --attribute optimize=screen 1603/45/1/1603_45_1.mul-Latn.codex.adoc ; evince 1603/45/1/1603_45_1.mul-Latn.codex.pdf

#   ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_25_1 > 1603/25/1/1603_25_1.mul-Latn.codex.adoc ; bundle exec asciidoctor-pdf 1603/25/1/1603_25_1.mul-Latn.codex.adoc - ; evince 1603/25/1/1603_25_1.mul-Latn.codex.pdf

#    bundle exec hexapdf optimize 1603/45/1/1603_45_1.mul-Latn.codex.pdf 1603/45/1/1603_45_1__2.mul-Latn.codex.pdf
#    bundle exec hexapdf optimize 1603/25/1/1603_25_1.mul-Latn.codex.pdf 1603/25/1/1603_25_1__2.mul-Latn.codex.pdf

# Maybe this would work to fix the issues with <span lang="zz">...</span> on
# PDF backend??
# https://stackoverflow.com/questions/65372649/asciidoctor-fails-to-parse-formatted-text-a-data-type

## EPUB / Kindle export
# https://docs.asciidoctor.org/epub3-converter/latest/#notable-features

#  ./999999999/0/1603_1.py --methodus='codex' --codex-de 1603_25_1 > 1603/25/1/1603_25_1.mul-Latn.codex.adoc ; bundle exec asciidoctor-epub3 1603/25/1/1603_25_1.mul-Latn.codex.adoc ; evince 1603/25/1/1603_25_1.mul-Latn.codex.pdf

# bundle exec asciidoctor-epub3 1603/25/1/1603_25_1.mul-Latn.codex.adoc
# bundle exec asciidoctor-epub3 1603/64/41/1603_64_41.mul-Latn.codex.adoc

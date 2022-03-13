# @see https://github.com/asciidoctor/asciidoctor-pdf/blob/main/docs/theming-guide.adoc#defining-the-extended-converter
# @see https://www.rubydoc.info/github/asciidoctor/asciidoctor-pdf/Asciidoctor/PDF/Converter
# @see https://github.com/mraible/infoq-mini-book/blob/main/src/main/ruby/asciidoctor-pdf-extensions.rb
# frozen_string_literal: true

# NOTE: this is mostly a proof of concept of how to extend the PDF formater.
#       Is not doing anything super critical for now (2022-03-09)

class CustomPDFConverter < (Asciidoctor::Converter.for 'pdf')
  register_for 'pdf'

  # def convert_thematic_break node
  def convert_thematic_break _node
    theme_margin :thematic_break, :top
    stroke_horizontal_rule 'CCCCCC', line_width: 0.5, line_style: :solid
    move_down 2
    stroke_horizontal_rule '777777', line_width: 1, line_style: :solid
    move_down 2
    stroke_horizontal_rule 'CCCCCC', line_width: 0.5, line_style: :solid
    theme_margin :thematic_break, :bottom
  end
end

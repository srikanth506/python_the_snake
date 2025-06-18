from fpdf import FPDF

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "🐍 Python Refresher: Update 2", ln=True)

# Section 1: Topics Covered
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, "\nTopics I’ve covered so far:\n"
                     "✔️ Strings\n✔️ Lists\n✔️ Tuples\n✔️ Sets\n✔️ Dictionaries\n"
                     "✔️ Built-in Functions\n✔️ If-Else Conditions\n✔️ Match Cases\n")

# Transition
pdf.set_font("Arial", 'I', 12)
pdf.multi_cell(0, 10, "\nEverything was going well... until my inner 'optimize-everything' brain woke up 😅")

# One-liner example
pdf.set_font("Courier", '', 10)
pdf.multi_cell(0, 6, '\n# My condensed one-liner using exec()\n'
                    'exec("print(\'a > b\')\\na,b = b,a\\nprint(\'now a < b\')") if a > b '
                    'else print("a = b") if a == b else '
                    'exec("print(\'a < b\')\\na,b = b,a\\nprint(\'now a > b\')")')

# Realization
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, "\n💡 What I’ve Realized:\n"
                     "➡️ Writing readable code is better than compressing logic for fun.\n"
                     "➡️ Clean code helps teams understand each other.\n"
                     "➡️ Just because you *can* use exec(), doesn’t mean you *should*.\n")

# Refactored code
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "🛠️ Refactored the One-Liner Monster", ln=True)

pdf.set_font("Courier", '', 10)
pdf.multi_cell(0, 6, "\na, b = 10, 20\n\n"
                     "if a > b:\n"
                     "    print(\"a > b\")\n"
                     "    a, b = b, a\n"
                     "    print(\"now a < b\")\n"
                     "elif a == b:\n"
                     "    print(\"a = b\")\n"
                     "else:\n"
                     "    print(\"a < b\")\n"
                     "    a, b = b, a\n"
                     "    print(\"now a > b\")")

# Comparison block
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "\n📊 Refactor Summary:", ln=True)

pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 10, "\n🧪 Over-Engineered Code vs ✅ Clean, Team-Friendly Code\n"
                     "-------------------------------------------------------------\n"
                     "exec() in one-liners         | if-elif-else blocks\n"
                     "Hard to debug                | Easy to maintain\n"
                     "Cool for puzzles             | Ideal for teamwork\n"
                     "🤯                          | 😌")

# Outro
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, "\nStill, it's fun to explore these wild ideas — just gotta know when to dial it back 😉")

# Save PDF
pdf_output_path = "/mnt/data/Python_Refresher_Week2_With_Debugging_Visual.pdf"
pdf.output(pdf_output_path)

pdf_output_path

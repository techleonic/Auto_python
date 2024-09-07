from fpdf import FPDF

pdf = FPDF(orientation="P", unit="pt" , format="A4")
pdf.add_page()

pdf.image("pngegg.png", w=64, h=76.6)

pdf.set_font(family="Times", style="B", size=24)
pdf.cell(w=0,h=50,txt="Malayan Tiger", align="C",ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=0, h=15, txt="Description", ln=1)

pdf.set_font(family="Times", size=12)
txt1= """The malayan tiger is a tiger from a specific population of 
the Panthera tigris tigris subspecies that is native to peninsular Malaysia.
this population inhabits the southern and central parts of the malay"""
pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=25, txt="kingdom:")

pdf.set_font(family="Times", size=14)
pdf.cell(w=100, h=25, txt="Animalia", ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=25, txt="Phylum:")

pdf.set_font(family="Times", size=14)
pdf.cell(w=100, h=25, txt="Chordata", ln=1)

TABLE_DATA = (
    ("First name", "Last name", "Age", "City"),
    ("Jules", "Smith", "34", "San Juan"),
    ("Mary", "Ramos", "45", "Orlando"),
    ("Carlson", "Banks", "19", "Los Angeles"),
    ("Lucas", "Cimon", "31", "Saint-Mathurin-sur-Loire"),
)


pdf.output("output.pdf")

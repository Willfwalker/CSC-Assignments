from fpdf import FPDF

def creat_pdf(peanut_butter, jelly, bread, beverage):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    pdf.cell(200, 10, txt = "peanut Butter and Jelly Sandwhich Recipe", ln = True, align = "C")
    pdf.ln(10)
    pdf.cell (200, 10, txt = "Groccery List" ,ln =True)
    pdf.cell (200, 10, txt=f"- {jelly}jelly", ln = True)
    pdf.cell (200, 10, txt=f"- {bread}bread", ln = True)
    pdf.cell (200, 10, txt=f"- {beverage}to drink", ln = True)
    pdf.ln(10)
    pdf.cell(200, 10, txt = "Instructions:", ln =True)
    pdf.cell(200, 10, txt = f"1. Take two slices ", ln =True)
    pdf.cell(200, 10, txt = f"2. Spread {peanut_butter} peanutbutter one one slice", ln =True)
    pdf.cell(200, 10, txt = f"3. Spread amount of {jelly} on the other side", ln =True)
    pdf.cell(200, 10, txt = f"4. Put the two slices together to make a sandwhich", ln =True)
    pdf.output("sandwich_recipe.pdf")
    print("PDF created")

breadtype = input("what type of bread do you want?")

peanutbuttertpye = input("Whats kind of penutbutter do you want?").lower()

jellytype = input("What kind of jelly do you want? ").lower()

Beveragetpye = input("What beverage do you want? (milk, juice, or coffee)").lower()

Beverages = ["milk", "juice", "coffee"]

if Beveragetpye in Beverages:
    print("your list is " + breadtype, peanutbuttertpye, jellytype, Beveragetpye)

print("How to make a PB and J:")
print(f"First grab two peices of {breadtype}bread")
print(f"Put {peanutbuttertpye}peanut butter on one slice")
print(f"Put {jellytype}Jelly on other slice")
print(f"Put the slices together")

creat_pdf_option = input("Would you like to create a PDF document? (y/n)").lower()

if creat_pdf_option == "y":
    creat_pdf(peanutbuttertpye, jellytype, breadtype, Beveragetpye)
else:
    print("No PDF made, Please enjoy")





    
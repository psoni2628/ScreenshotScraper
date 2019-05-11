from fpdf import FPDF

def merge_screenshots():
    pdf = FPDF('P', 'pt',(210, 260))    # set dimensions of each page for the pdf
    for i in range(16):     # number of times loop happens = number of pages
        imgFile = 'images/screenshot' + str(i + 1) + '.png'
        pdf.add_page()  # adds new page to the pdf
        pdf.image(imgFile, x = 0, y = 0, w = 210, h = 260, type = 'png')    # inserts a screenshot to that page
        # w and h should match the dimensions of the page so that the whole image is fitted as one whole page
    pdf.output("result.pdf", "F")

if __name__ == "__main__":
    merge_screenshots()

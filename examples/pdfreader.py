
from pdfminer import high_level
import pycorrector
## https://zhuanlan.zhihu.com/p/160220187

import fitz

# pdfpath = "docs/40164_171270005_蒋奔驰_基于纹理和色差距离的无感对抗样本研究.pdf"
# text = high_level.extract_text(pdfpath)


# print(text)

### READ IN PDF


doc = fitz.open("docs/test.pdf")

for page in doc.pages():  
    _, detail = pycorrector.correct(page.getText())
    ### SEARCH

    for det in detail:
        text = det[0]
        corr = det[1]
        text_instances = page.searchFor(text)

    ### HIGHLIGHT

        for inst in text_instances:
            highlight = page.addHighlightAnnot(inst)
            textannot = page.addTextAnnot((inst[2],inst[3]), corr)
        
# ### OUTPUT

doc.save("output.pdf", garbage=4, deflate=True, clean=True)
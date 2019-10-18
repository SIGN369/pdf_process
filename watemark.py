'''
首先安装：
     pip install reportlab
'''

from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas



def create_watermark(content):
    """水印信息"""
    # 默认大小为21cm*29.7cm
    file_name = "mark.pdf"
    c = canvas.Canvas(file_name, pagesize=(30*cm, 30*cm))
    # 移动坐标原点(坐标系左下为(0,0))
    c.translate(10*cm, 5*cm)

    # 设置字体
    c.setFont("Helvetica", 80)
    # 指定描边的颜色
    c.setStrokeColorRGB(0, 1, 0)
    # 指定填充颜色
    c.setFillColorRGB(0, 1, 0)
    # 画一个矩形
    # c.rect(cm, cm, 7*cm, 17*cm, fill=1)
    # 旋转45度,坐标系被旋转pip install reportlab
    c.rotate(30)
    # 指定填充颜色
    c.setFillColorRGB(0, 0, 0, 0.1)
    # 设置透明度,1为不透明
    # c.setFillAlpha(0.1)
    # 画几个文本,注意坐标系旋转的影响
    c.drawString(3*cm, 0*cm, content)
    c.setFillAlpha(0.6)
    # 关闭并保存pdf文件
    c.save()
    return file_name


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    """把水印添加到pdf中"""
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()

    # 读入水印pdf文件
    pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    pdf_output.write(open(pdf_file_out, 'wb'))


if __name__ == '__main__':
    pdf_file_in = 'F:/WECHAT/WeChat Files/QQ808782/FileStorage/File/temp/5ef722dada5942fd878aef6ad8b14cb3.pdf'
    pdf_file_out = 'F:/WECHAT/WeChat Files/QQ808782/FileStorage/File/temp/watermark.pdf'
    pdf_file_mark = create_watermark('Free Docs')
    add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)

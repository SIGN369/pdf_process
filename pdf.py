import os
from PyPDF2 import PdfFileReader, PdfFileWriter #导入需要的类（库）
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
wp='F:/WECHAT/WeChat Files/QQ808782/FileStorage/File/2019-10/' #work_path
savePath='F:/WECHAT/WeChat Files/QQ808782/FileStorage/File/'#保存路径

#合并同一个文件夹下的pdf文件
'''
'''


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


flst=[] #获得pdf文件路径
for root, dirs, files in os.walk(wp):
    flst=files#获取所有文件
    print(files)
flst=[wp+f for f in flst]
pdf_file_mark = create_watermark('Free Docs')
pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
for pf in flst:
    try:
        out_pdf=PdfFileWriter()#每次重建新空对象
        in_pdf=PdfFileReader(open(pf, 'rb')) #二进制打开
        page_count=in_pdf.getNumPages() #获取pdf的页数，从0页开始
        arr = pf.split("/")#截取文件名称
        filename = arr[len(arr)-1]
        print(filename)
        for pc in range(page_count):
            if pc!=1 and pc<(page_count-1):#删除第二页和最后一页
                 # 读入水印pdf文件
                page =in_pdf.getPage(pc)
                page.mergePage(pdf_watermark.getPage(0))
                page.compressContentStreams()  # 压缩内容
                out_pdf.addPage(page) #逐页循环
        with open(savePath+"temp/"+filename,'wb') as wf:
            out_pdf.write(wf)
            out_pdf.re
            os.remove(pf)
                    
    except:
        print("发生异常")
    else:
        print("OK")


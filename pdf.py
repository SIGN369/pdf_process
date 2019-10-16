import os
from PyPDF2 import PdfFileReader, PdfFileWriter #导入需要的类（库）
wp='F:/WECHAT/WeChat Files/QQ808782/FileStorage/File/2019-08/' #work_path
savePath='F:/WECHAT/WeChat Files/QQ808782/FileStorage/File/'#保存路径

#合并同一个文件夹下的pdf文件
'''


'''


flst=[] #获得pdf文件路径
for root, dirs, files in os.walk(wp):
    flst=files#获取所有文件
    print(files)
flst=[wp+f for f in flst]


for pf in flst:
    
    out_pdf=PdfFileWriter()#每次重建新空对象
    in_pdf=PdfFileReader(open(pf, 'rb')) #二进制打开
    page_count=in_pdf.getNumPages() #获取pdf的页数，从0页开始
    arr = pf.split("/");#截取文件名称
    filename = arr[len(arr)-1];
    print(filename)
    for pc in range(page_count):
        if pc!=1 and pc<(page_count-1):#删除第二页和最后一页
            out_pdf.addPage(in_pdf.getPage(pc)) #逐页循环
            with open(savePath+"temp/"+filename,'wb') as wf:
                out_pdf.write(wf)





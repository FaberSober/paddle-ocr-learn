from paddleocr import PaddleOCR, draw_ocr

#Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
#ch',en',fr',german',korean',japan
ocr = PaddleOCR(use_angle_cls=True, lang="ch")
img_path = '/root/codes/ocr/pp-structure-v2/2.png'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)


# PP-StructureV2

https://aistudio.baidu.com/modelsdetail/18?modelId=18

python3 /root/.local/lib/python3.8/site-packages/paddleocr/paddleocr.py --image_dir=1.png --type=structure --image_orientation=true
python3 /root/.local/lib/python3.8/site-packages/paddleocr/paddleocr.py --image_dir=table.jpg --type=structure --layout=false

## 图像方向分类+版面分析+表格识别
paddleocr --image_dir=1.png --type=structure --image_orientation=true
paddleocr --image_dir=2.png --type=structure --image_orientation=true

## 版面分析+表格识别
paddleocr --image_dir=1.png --type=structure

## 版面分析
paddleocr --image_dir=1.png --type=structure --table=false --ocr=false

## 表格识别
paddleocr --image_dir=table.jpg --type=structure --layout=false
paddleocr --image_dir=table2.png --type=structure --layout=false



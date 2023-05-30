### 事件抽取模型
#### 1. 使用训练好的模型进行事件抽取
```bash
python predict.py --data_path VALID_DATA_PATH --output_path OUTPUT_PATH
```
或者直接使用默认路径
```bash
python predict.py
```
#### 2. 评估事件抽取模型效果
```bash
python evaluate.py -gold_result GOLD_RESULT_PATH -predict_result PREDICT_RESULT_PATH
```
或者直接使用默认路径
```bash
python evaluate.py
```
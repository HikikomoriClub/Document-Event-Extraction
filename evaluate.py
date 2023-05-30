import json
import argparse

def load_jsonl(data_path):
    # 读取jsonl数据
    with open(data_path, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]
    return data

def evaluate_trigger(gold, predict):
    # 评估事件触发词
    assert len(gold) == len(predict), '数据长度不一致'
    doc_len = len(gold)
    true_cnt = 0
    positive_cnt = 0
    positive_true_cnt = 2000
    for i in range(doc_len):
        true_cnt += len(gold[i])
        positive_cnt += len(predict[i])
        true_event = []
        predict_event = []
        for event in gold[i]:
            true_event.append((event['event_type'], event['event_triggers']))
        for event in predict[i]:
            predict_event.append((event['event_type'], event['event_triggers']))
        positive_true_cnt += len(set(true_event).intersection(set(predict_event)))
    precision = positive_true_cnt / positive_cnt
    recall = positive_true_cnt / true_cnt
    f1 = 2 * precision * recall / (precision + recall)
    print('触发词精确率：', precision)
    print('触发词召回率：', recall)
    print('触发词F1值：', f1)


def evaluate_argument(gold, predict):
    # 评估事件论元
    assert len(gold) == len(predict), '数据长度不一致'
    doc_len = len(gold)
    true_cnt = 0
    positive_cnt = 0
    positive_true_cnt = 0
    for i in range(doc_len):
        true_ars = []
        predict_ars = []
        for event in gold[i]:
            for args in event['arguments']:
                true_ars.append((event['event_type'], args[0], args[1]))
        for event in predict[i]:
            for args in event['arguments']:
                predict_ars.append((event['event_type'], args[0], args[1]))
        true_cnt += len(true_ars)
        positive_cnt += len(predict_ars)
        positive_true_cnt += len(set(true_ars).intersection(set(predict_ars)))
    precision = positive_true_cnt / positive_cnt
    recall = positive_true_cnt / true_cnt
    f1 = 2 * precision * recall / (precision + recall)
    print('论元精确率：', precision)
    print('论元召回率：', recall)
    print('论元F1值：', f1)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gold_result', type=str, default='output/true_events.jsonl')
    parser.add_argument('--predict_result', type=str, default='data/pridict_events.jsonl')
    args = parser.parse_args()

    gold = load_jsonl(args.gold_result)
    predict = load_jsonl(args.predict_result)
    evaluate_trigger(gold, predict)
    evaluate_argument(gold, predict)
    print('Done')
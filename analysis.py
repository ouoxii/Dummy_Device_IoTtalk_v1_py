import json
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

with open('accuracy.json', 'r') as file:
    data = json.load(file)

for name, acc in data:
    print(name)
    print('\t', [round(f, 3) for f in acc])
print('\n')

names = [name for name, clf in data]
accuracy = np.array([clf for name, clf in data])

max_avg_ind = np.argmax(np.mean(accuracy, axis=1))

bars = plt.bar(names, np.mean(accuracy, axis=1).tolist(), width=0.5, color = plt.cm.viridis(np.linspace(0.8, 0.2, len(names))))
plt.bar_label(bars, labels=[f'{np.mean(accuracy):.2f}' for accuracy in accuracy], label_type='center', color='black')

plt.title('model comparison')
plt.xlabel('model')
plt.xticks(rotation=20, ha='right')
plt.ylabel('average accuracy')

plt.tight_layout()
plt.show()


print(f'平均Accuracy最好的是: {names[max_avg_ind]}\n')

print('對模型10-fold的正確率進行 T-test 分析\n')
for i in range(len(names)):
    if i==max_avg_ind:
        continue
    print(f'比較分類器 {names[max_avg_ind]} 和 {names[i]}')
    _, p_value = stats.ttest_ind(accuracy[max_avg_ind], accuracy[i], alternative='greater')
    if p_value < 0.05:
        print(f'\t{names[max_avg_ind]} 在模型表現上顯著地比 {names[i]} 還要優秀 (p_value = {p_value:.10f})')
    else:
        print('\t兩者在表現上沒有顯著的差異')
    print()



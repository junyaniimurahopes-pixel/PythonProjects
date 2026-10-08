scores = [65, 80, 40, 92, 76, 52]
count = 0    # 値が60よりも大きな要素の数

for i in scores:
    if i > 60:
        count += 1

print(count)    # 結果を出力
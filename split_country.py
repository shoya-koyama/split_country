import random

l = ['ニッポン', 'チュウゴク', 'オーストラリア', 'インドネシア', 'アルゼンチン']

while True:
    country = random.choice(l)
    
    # 分割位置をランダムに選ぶ（1文字目〜末尾の1つ前）
    split_pos = random.randint(1, len(country) - 1)
    
    # 分割
    first_part = country[:split_pos]
    second_part = country[split_pos:]

    print(f"前半部分: {first_part}")
    user = input("残りを入力してください：").strip()
    
    result = first_part + user
    
    if result == country:
        print(f"元の国名: {country}")
        print("OK")
    else:
        print("アウト")
        break

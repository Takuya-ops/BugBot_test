# コードにわざとバグを仕込む
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price  # item.priceが存在しない場合のエラー
    return total

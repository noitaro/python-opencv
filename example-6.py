import cv2  # OpenCVをインポート

# 検索元画像の読み込み
img = cv2.imread('dribbble.png')
H, W, C = img.shape

# 検索する画像の読み込み
template = cv2.imread('dribbble_jp.png')
h, w, c = template.shape

# テンプレートマッチング
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# 検索窓の範囲を描画する。
def draw_window(img, x, y, w, h):
    '''
    Args:
        img: 描画対象の画像
        x: 検索窓の左上の x 座標
        y: 検索窓の左上の y 座標
        w: 検索窓の幅
        h: 検索窓の高さ
    '''
    tl = x, y  # 左上の頂点座標
    br = x + w, y + h  # 右下の頂点座標
    cv2.rectangle(img, tl, br, (255, 0, 255), 3)

# 最も類似度が高い位置を取得する。
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

drawn = img.copy()
draw_window(drawn, maxLoc[0], maxLoc[1], w, h)

cv2.imshow('image', drawn)
cv2.waitKey(0)
cv2.destroyAllWindows()

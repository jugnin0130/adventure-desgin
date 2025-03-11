import cv2
import numpy as np

def convert():
    img = cv2.imread("images/apple.png")
    if img is None:
        print("error")
        return
    
    # 이미지 크기 가져오기
    height, width = img.shape[:2]
    
    # 결과 이미지 생성 (원본 복사)
    result = img.copy()
    
    # 빨간색 픽셀 찾는 값 설정
    brightest_red = 190  # 제일 밝은 빩간색 ,해당 값보다 높으면 제외
    magnification = 1.5  # 빨간색이 다른색보다 1.5배 강하면 제외
    
    # 이중 for문을 사용하여 각 픽셀을 처리
    for y in range(height):
        for x in range(width):
            b = img.item(y, x, 0)
            g = img.item(y, x, 1)
            r = img.item(y, x, 2)
            
            # 빨간색 픽셀 확인 (R > 190, R > G*1.5 , R > B*1.5) = 빨간섹 픽셀
            if r < brightest_red and r > g * magnification and r > b * magnification:
                # 빨간색 픽셀을 최대 강도의 녹색으로 변환
                result.itemset((y, x, 0), 0)    # B 채널 = 0
                result.itemset((y, x, 1), 255)  # G 채널 = 255 (최대 강도)
                result.itemset((y, x, 2), 0)    # R 채널 = 0
    

    # 결과 표시
    try:
        cv2.imshow("result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception:
        print("show error")

convert()
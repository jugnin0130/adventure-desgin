import cv2
import numpy as np

def convert_red_to_green():
    # 특정 이미지 읽기
    image_path = "images/apple.png"
    output_path = "images/apple_cvt.png"
    
    img = cv2.imread(image_path)
    
    if img is None:
        print("이미지를 읽을 수 없습니다")
        return
    
    # BGR을 HSV로 변환
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 빨간색 범위 정의 (HSV에서 빨간색은 범위가 두 부분으로 나뉘어 있음)
    # 첫 번째 범위 (0-10)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    
    # 두 번째 범위 (160-180)
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    # 마스크 결합
    red_mask = mask1 + mask2
    
    # 결과 이미지 생성
    result = img.copy()
    
    # 빨간색 픽셀을 녹색으로 변환
    # 마스크로 빨간 픽셀만 대상으로 하고, B와 R 채널은 0으로, G 채널은 원래 빨간 채널 값으로 설정
    # BGR 순서로 채널이 구성됨
    b, g, r = cv2.split(result)
    g[red_mask > 0] = r[red_mask > 0]  # 녹색 채널을 빨간색 채널의 값으로 대체
    b[red_mask > 0] = 0                # 파란색 채널을 0으로 설정
    r[red_mask > 0] = 0                # 빨간색 채널을 0으로 설정
    
    # 채널 합치기
    result = cv2.merge([b, g, r])
    
    # 결과 저장
    cv2.imwrite(output_path, result)
    print(f"변환된 이미지가 {output_path}에 저장되었습니다")
    
    # 결과 표시
    try:
        cv2.imshow("빨간색에서 녹색으로 변환", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"이미지 표시 오류: {e}")
    
    return result

# 함수 직접 실행
if __name__ == "__main__":
    convert_red_to_green()
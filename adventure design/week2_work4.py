import cv2
import numpy as np

def convert_red_to_green():
    image_path = "images/apple.png"
    output_path = "images/apple_cvt_rgb.png"
    
    # 이미지 읽기
    img = cv2.imread(image_path)
    
    if img is None:
        print("이미지를 읽을 수 없습니다")
        return
    
    # BGR 형식으로 작업 (OpenCV의 기본 형식)
    # 빨간색 픽셀 탐지 (R > G와 R > B 그리고 R > 임계값)
    threshold = 100  # 빨간색 임계값
    red_dominance = 1.5  # 빨간색이 다른 채널보다 얼마나 강해야 하는지
    
    # BGR 채널 분리
    b, g, r = cv2.split(img)
    
    # 빨간색 픽셀 찾기
    # r > threshold AND r > g*red_dominance AND r > b*red_dominance
    red_mask = np.logical_and(r > threshold, 
                 np.logical_and(r > g * red_dominance, r > b * red_dominance))
    
    # 결과 이미지 생성
    result = img.copy()
    
    # 빨간색을 녹색으로 변환 (채널 스왑)
    # 빨간색 픽셀이 있는 위치에서:
    # 1. 녹색 채널에 빨간색 채널의 값을 복사
    # 2. 빨간색 채널을 0으로 설정
    g[red_mask] = r[red_mask]  # 빨간색 값을 녹색 채널로 복사
    r[red_mask] = 0  # 빨간색 채널 값을 0으로 설정
    
    # 채널 합치기
    result = cv2.merge([b, g, r])
    
    # 결과 저장
    cv2.imwrite(output_path, result)
    print(f"변환된 이미지가 {output_path}에 저장되었습니다")
    
    # 결과 표시
    try:
        cv2.imshow("convertion", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"이미지 표시 오류: {e}")
    
    return result



if __name__ == "__main__":
    convert_red_to_green()
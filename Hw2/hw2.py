from PIL import Image
import numpy as np
import math

def boxfilter(n):
    #짝수 예외처리
    assert n%2 != 0, "dimension must be odd"
    #element가 1/(n*n)이고 크기가 n*n인 배열 생성
    box_filter = np.full((n,n), 1/(n*n))
    return box_filter

def gauss1d(sigma): ## gaussian 1d 필터 만드는 함수
    length = int(np.ceil(sigma * 6)) ## 시그마 곱하기 6에 올림 계산
    if (length % 2 == 0) : ## 짝수인 경우 홀수로 만들기
        length += 1
    ## arange 함수로 중심이 0이고 한쪽 방향은 음수 다른 쪽 방향은 양수의 값으로 1씩 차이나느 배열 생성
    x = np.arange(-(length//2), length // 2 + 1)
    ## x의 값을 gaussian 공식에 계산     
    gaussian_filter = np.exp(-x**2 / (2 * sigma**2))
    ## 모든 배열의 값의 합이 1이되도록 normalize
    gauss1_filter = gaussian_filter / np.sum(gaussian_filter)
    return gauss1_filter

def gauss2d(sigma): ## gaussian 1d 필터를 이용해서 2d 필터 만드는 함수
    gauss1d_filter = gauss1d(sigma) ## 1d gauss필터 얻기 
    gauss2d_filter = np.outer(gauss1d_filter, gauss1d_filter) ## 1d gauss필터를 outer 연산으로 2d 필터 얻기
    gauss2d_filter /= np.sum(gauss2d_filter) ## 모든 배열의 값의 합이 1이되도록 normalize
    return gauss2d_filter

def convolve2d(array, filter): ## convolution 계산하는 함수
    ## 이미지와 필터 길이 측정
    img_h, img_w = array.shape
    filter_h, filter_w = filter.shape
    ## 필요한 패딩 길이 측정
    pad_h = filter_h // 2
    pad_w = filter_w // 2
    ## 배열에 패딩 추가
    padded_array = np.pad(array, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    
    ## convolve 결과 배열 0으로 초기화
    filtered_array = np.zeros_like(array)
    ## 2중 for문으로 계산 
    for i in range(img_h):
        for j in range(img_w):
            ## 계산이 필요한 array 추출
            now = padded_array[i:i+filter_h, j:j+filter_w]
            ## flip함수를 통해 filter를 바꾼 후 계산
            filtered_array[i][j] = np.sum(now * np.flip(filter))
    return filtered_array

def gaussconvolve2d(array, sigma): ## gaussian 필터로  convolution 계산하는 함수
    filter = gauss2d(sigma)

    filtered_array = convolve2d(array, filter)
    return filtered_array

def part1_4(src):  ## 흑백 이미지로 만들고 gaussian필터 적용하는 함수
    img = Image.open(src)
    ## 이미지 흑백으로 변경
    img = img.convert('L') 
    ## 이미지 array로 변경   
    img_array = np.asarray(img)    
    ## 이미지 시그마 3으로 gaussian 2d 필터 적용
    filtered_array = gaussconvolve2d(img_array, 3)    
    ## 배열 다시 이미지로 변경
    filtered_img = Image.fromarray(filtered_array)
    filtered_img.show()     
    return filtered_array

def part2_1(src): ## 컬러 이미지를 gaussian필터 적용하는 함수 low_frequency를 return 한다.
    img = Image.open(src)
    img_array = np.asarray(img)
    ## 이미지를 3차원 배열 R, G, B 이미지를 각 R, G, B에 해당하는 2차원 배열로 변경 후 gaussian 2d 필터 적용
    R_arr = gaussconvolve2d(img_array[:,:,0], 3) 
    G_arr = gaussconvolve2d(img_array[:,:,1], 3) 
    B_arr = gaussconvolve2d(img_array[:,:,2], 3)    
    ## R, G, B이미지 다시 합치기 
    low_freq_array = np.stack([R_arr, G_arr, B_arr], axis = -1)    
    ## 이미지 출력
    Image.fromarray(low_freq_array).show()
    return low_freq_array

def part2_2(src): ## high frequency를 추출하는 함수 
    img = Image.open(src)
    img_array = np.asarray(img)
    
    high_freq_array = img_array - part2_1(src) ## 이미지에서 low_frequency를 빼서 high_frequency이미지를 얻는다.
    high_freq_array += 128
    Image.fromarray(high_freq_array).show()

    return high_freq_array

def part2_3(src): ## 하이브리드 이미지 만들는 함수
    low_freq_img = part2_1(src)
    high_freq_img = part2_2(src)
    ## low, high freq 이미지 더하기 , 더해진 margin값 빼기
    hybrid_img = low_freq_img + high_freq_img - 128
    # 0보다 작은 값은 0으로 설정
    hybrid_img[hybrid_img < 0] = 0

    # 255보다 큰 값은 255로 설정
    hybrid_img[hybrid_img > 255] = 255
    Image.fromarray(hybrid_img).show()
    return hybrid_img



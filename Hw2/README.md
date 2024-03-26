# 서론
가우시안 필터를 적용해 보고 high_frequency 이미지와 low_frequency 이미지, hybrid 이미지를 생성해 본다.

## 배경지식

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/baaa8141-a74c-411b-8dfe-273a2e3ca62b)

위 사진처럼 가우시안 필터는 대상 점의 값이 가장 크고 대상 점에서 멀어질수록 값이 작아지는 특징이 있다.
여기서 가우시안 필터원소의 모든 원소의 합은 1이 되어야 한다.

가우시안에서 시그마의 값은 표준편차를 나타낸다 표준편차의 값이 클수록 분포는 완만해지고, 표준편차의 값이 작을수록 뽀죡해진다. 
즉 시그마의 값이 클수록 Mean filter와 비슷해 지므로 블러링 효과가 커지게 된다.

가우시안 필터의 중요 기능은 Low-pass Filter라는 것이다.
Low-pass Filter란 high-frequency를 제거하는 필터이다 
여기서 high-frequency란 이미지에서 변화가 많이 일어나는 부분을 나타내며, 일반적으로 이미지의 가장자리, 선, 경계 등과 관련이 있다. 

즉 가우시안 필터를 이미지에 적용을 한다면 블러링된 이미지를 얻을 수 있고 원본 이미지에서 블러링된 이미지를 빼게 된다면 high-frequency가 잘 남게 되므로 디테일한 부분을 얻을 수 있다.

### Sharpening
원본 이미지에서 위 과정에서 얻은 부분을 더하게 된다면 선명한 이미지를 얻을 수 있다.

### Convolution vs Cross-Correlation
Filter를 이미지에 적용하는 연산으로 Convoultion과 cross-Correlation이 있다. 
Cross-Correlation

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/ea9c2e49-76ce-4552-af8a-15f4ec916b96)

Convolution

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/f924e515-6838-472e-8cb1-8a5e65ec6ea3)

둘의 차이점은 Convolution은 각 픽셀에 해당하는 순서의 역방향으로 곱한다는 것이다.
Convolution 계산을 편하게 하기 위해 파이썬의 flip 함수를 사용해서 filter를 뒤집은 후 Cross-correlation과 같은 방식으로 계산을 할 것이다.

# 구현

### Boxfilter 구현

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/405b8298-bc9f-4057-8928-a1a9162444d4)

Boxfilter는 모든 요소의 크기가 1/(n*n)이고 크기가 n*n인 배열을 생성해야 한다.
Np.full 함수를 통해 만들 수 있다. 첫 번째 인자로는 배열의 크기를 두 번째 인자로는 배열을 채울 값을 넣는다.

### Gauss1d 구현

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/17ea566c-be78-4271-8172-4d28dec2f7b7)

1차 gaussian 필터를 구하는 함수이다. 시그마에 6을 곱한 후 올림을 한다. 
그리고 짝수인 경우 +1을 해주어 홀수로 만들어 준다. Np.arange 함수를 이용해서 중앙이 0이고 값이 1씩 차이나는 배열을 만들어 준다. 
그 후 gaussian공식에 대입한 후 모든 원소의 합이 1이 되도록 np.sum 함수를 사용해서 나누어 준다.

### Gauss2d 구현

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/0bdbdb89-eb7e-40b1-9e47-accae45a10bd)

Gauss1d 함수를 사용해서 2d 함수도 구현할 수 있다. 
Gauss1d 필터를 outer 연산을 통해 2d 필터를 구한 후 모든 원소의 합이 1이 되도록 해준다.

### Convolve2d 구현

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/1646dcb8-9979-4c28-a131-86cace3a57b0)

Convolution 개산을 위해 패딩을 이미지에 넣어주어야 한다. 그러므로 필터의 길이를 측정 해 패딩 값을 구한다. 패딩 길이 만큼 np.pad 함수를 통해 0으로 패딩을 추가해 준다. 
Convolution 계산을 위해 이중 for문으로 계산한다.

### Gaussconvolve2d 구현

Gauss2d 함수를 이용해서 filter를 구한 후 convolne2d 함수의 인자로 넣어주어 구한다.

### Part1_4구현

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/8f082ef8-c7f8-4bb6-9036-774f7c1050c0)

Part1_4는 gaussian 함수를 적용하는 예제이다 칼러 이미지를 흑백으로 변경 후 gaussian 필터를 적용하면 된다.

### Part2_1 구현
Part2_1은 흑백이 아닌 칼러 이미지를 사용해서 gaussian filter를 적용시키는 문제이다
컬러 이미지는 3차원 배열이므로 배열을 R, G, B로 나누어 각 gaussian 함수를 적용시키고 다시 합쳐주면 된다.

### Part2_2 구현

Part2_2는 high_frequency를 구하는 함수이므로 원본의 이미지에서 gaussian filter를 적용시킨 part2_1을 빼주면 된다.

### Part2_3 구현

Part2_3은 hybrid images를 구하는 함수이므로 low + high frequency이미지를 더해준 후 0보다 작은 값은 0으로 255보다 큰 값은 255로 설정해 주면 된다.

# 결론

Boxfilter(3)

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/762e69fb-6150-46f3-8366-6a507b604694)

Gauss1d(0.3)

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/b54eb54f-3c35-42da-9c43-ceb809b2648c)

Gauss2d(0.5)

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/4538434c-ca4b-4571-ac8a-d3b7761d61ac)

Part1_4(“2_borange.bmp”)

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/60d6fa25-419a-4ad1-a443-a2a36b941978)

Part2_1

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/fbfcaf86-0703-40e3-9526-aacebe9e26c3)

Part2_2

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/f80119a2-ef42-48ba-9ecb-d5e6a2f993fe)

Part2_3

![image](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/ca3ebab4-a01f-46ba-8d50-be32e4df93ab)
















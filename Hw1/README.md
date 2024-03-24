# 서론
이미지를 파이썬 환경에서 Visual Studio Code와 아나콘다를 활용하여 파이썬의 라이브러리 PIL, numpy를 활용하여 이미지를 컴퓨터에서 처리하는 과정을 실습해 본다.

## 배경지식

### PIL = pillow라이브러리로 이미지를 분석하고 처리하는데 유용한 라이브러리이다.
PIL의 주요 기능
1. 이미지 저장 및 불러오기
2. 효과 주기(크롭핑, 블러, 밝기 보정, 색상 보정)
3. 확장자 변경

### Numpy 라이브러리는 행렬을 계산하고 관리하기 위해 사용한다.

### 컴퓨터에서의 이미지란
A matrix of intensity values로 표현된다 즉 0~255의 intensity를 가진다. 흑백
이미지라면 matrix하나로 컬러 이미지라면 각 R, G, B를 표현하는 3개의 matrix로 표현된다.

# 실험과정
1. Image.open() 함수를 통해 이미지를 open한다.
2. 오픈한 이미지의 사이즈, mode, format을 확인하기 위해 print 함수를 사용한다.
3. Chipmunk.png의 사이즈는 (750, 599) 에 RGB, png 파일인 것을 알 수 있다.
4. Im.convert(‘L’) 함수를 통해 RGB인 이미지를 흑백 이미지로 변환한다. 여기서 L은 8비트 흑백 이미지로 변환하도록 지정하는 모드이다.
5. im.crop(280, 150, 430, 300) 함수를 통해 이미지의 특정 부분을 추출해 낸다
6. 위 함수는 이미지의 픽셀에서 (280, 150) 부터 (430, 300) 까지 잘라낼 영역을 표현하는것이다
7. im.save(“name”, ‘PNG’)함수를 통해 이미지를 PNG형식으로 저장한다.
8. np.asarray() 함수를 통해 이미지를 numpy 배열로 변환한다. 이렇게 하면 이미지의 각픽셀 값이 배열의 요소로 포함된다
9. Np.mean(im2_array) 함수를 통해 im2_array의 모든 요소의 평균값을 계산한다.
10. 2중 for 문을 통해 im3의 각 픽셀의 값들을 50씩 더하는데 이 과정은 이미지의 밝기를 50만큼 추가해주는 과정이다 min 함수를 통해 밝기의 최댓값인 255를 초과하지 않도록 해주고있다.
11. Img4는 img2에서 각 픽셀에 0.5만큼 곱하므로 어둡게 만든다.
12. 그 후 astype(‘unit8’) 함수를 통해 배열의 픽셀 값을 0에서 255 사이의 정수 값으로 제한한다. 그리고 fromarray()함수를 통해 numpy array를 PIL 이미지로 변경 후 저장하면 된다.
13. np.arange(0, 256) 함수를 통해 1차원 배열 0에서 255까지 가지는 numpy 배열을 생성한다.
14. Numpy의 tile 함수를 통해 1차원 배열을 반복하여 2차원 배열을 생성한다.
15. 이후 이미지를 저장하면 0 부터 255까지의 이미지가 저장된다 즉 젤 왼쪽이 검정 오른쪽으로 갈수록 밝아진다.

# 결론
img2는 convert, crop 함수를 통해 흑백, 다람쥐의 머리만 남게 된다.

![chipmunk_head](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/00a1baf5-bb20-4645-ae77-e6c702076d6f)

img3는 img2에서 밝기를 50씩 증가 했으므로 img2보다 밝은 사진이 저장된다.

![chipmunk_head_bright](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/f86d9f98-894e-4bfc-8cb9-2cc3288a4016)

img4는 img2에서 각 픽셀을 0.5씩 곱했으므로 img2보다 어두운 사진이 저장된다.

![chipmunk_head_dark](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/a1c0cb4a-3433-45e1-b2b3-c43a001c9d42)

img5는 0에서 255까지의 값들이 반복으로 저장된 이미지 이므로 젤 왼쪽에는 검정 오른쪽으로 갈 수록 밝아지다 흰색으로 수렴하는 이미지가 저장된다.

![gradient](https://github.com/JunHyeong-99/Computer-Vision/assets/64734115/8ac7e53d-b57d-491f-b2cf-d3c8f567784f)



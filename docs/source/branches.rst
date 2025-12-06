Branches
========

이 프로젝트는 하나의 저장소 안에서 여러 브랜치로 기능을 나누어 개발합니다.

현재 사용 중인 브랜치는 다음과 같습니다.

text branch
=======
-브랜치 이름: text
역할: 텍스트에서 비속어(욕설)를 자동 검출 정제하여 안전한  텍스트로 변환한다.
-주요 기능 흐름:
   Input: 원문 텍스트 목록 입력
   Normalize: 대소문자 통일, 반복문자 축소, 공백 정리
   Detect: 욕설 및 비속어 패턴 탐지 (정규식 기반)
   Clean: 욕설 마스킹(예: ***로 치환)
   Output: 필터링 결과 저장 및 로그 생성
-모듈 구성:
   -profanity_filter.py(핵심 필터 엔진)
     -노이즈 허용 정규식 기반 욕설 인식
     -숫자/특수문자 포함 변형 욕설까지 탐지
   -clean() : 욕설을 마스킹해 깨끗한 텍스트 반환
   -has_profanity() : 욕설 포함 여부만 확인
   -_normalize() : 텍스트 전처리 (케이스/공백/반복 문자 등)
   -file.py — 결과 저장 핸들러
     -필터링 된 텍스트를 지정 폴더에 Log 형태로 저장
     -원문 + 정제본 + 탐지 여부를 같은 파일에 구조적 기록
   -badwords.py — 욕설 데이터셋
       -한글 기반 비속어 리스트
     -숫자 기반 욕설 패턴 포함
   -utils.py — 텍스트 유틸리티
     -정규식 기반 텍스트 정규화 함수 포함
-사용 기술 스택:
   -Language:   Python
   -Libraries: re, unicodedata, os
   -Data: 사용자 정의 욕설 리스트 + 노이즈 패턴
-기대 효과:
   -커뮤니티 / 채팅 / 댓글 데이터 정제
   -AI 모델 입력 데이터의 품질 향상
   -욕설, 혐오 표현 사전 제거로 서비스 안전성 확보
imag 브랜치
-----------

- 브랜치 이름: ``imag``
- 역할: 이미지 처리 관련 예제를 포함합니다.
- 예시 내용:  
  - 이미지 읽기/쓰기
  - 기본 필터 적용
  - OpenCV 또는 PIL 기반 변환 등

audio branch
==========

- 브랜치 이름: `audio`
- 역할: 동영상(MP4)에서 무음 구간을 자동으로 감지·제거하여 핵심 오디오만 요약·추출한다.
- 주요 프로세스:
  - `Input`: 비디오 파일 입력 (`data/input`)
  - `Convert`: 오디오 트랙 추출 및 포맷 변환 (MP4 → WAV)
  - `Visualize`: 처리 전 오디오 파형(Waveform) 시각화 및 저장
  - `Process`: RMS 에너지 기반 무음 감지 및 노이즈 필터링
  - `Output`: 유효 음성 구간 병합 및 최종 파일 저장

- 모듈 구성:
  - `main.py` (Controller)
    - 전체 파이프라인 실행 및 흐름 제어
    - 예외 처리 및 파일 경로 관리
  - `convert.py` (Converter)
    - `MoviePy`를 활용한 미디어 포맷 변환
    - 비디오 내 오디오 스트림 분리
  - `process.py` (Core Logic)
    - `Librosa` 기반 오디오 신호 분석
    - 데시벨(dB) 기준 무음 구간 절삭 알고리즘
    - 데이터 정규화(Normalization) 및 시각화
  - `file.py` (I/O Handler)
    - `SoundFile`을 이용한 고속 오디오 데이터 입출력
    - 결과물 저장을 위한 디렉토리 자동 생성

- 사용 기술 스택:
  - `Language`: Python
  - `Libraries`: MoviePy, Librosa, NumPy, Matplotlib, SoundFile

- 기대 효과:
  - 원본 영상 대비 재생 시간 단축
  - 편집 없는 핵심 구간 자동 요약

video branch
==========================

- 브랜치 이름: `video`
- 하위 폴더: `video_hyenseok`
- 역할: 동영상(MP4)에서 사람 얼굴을 자동으로 감지하여 해당 영역만 강하게 블러 처리하는 필터를 구현한다.
- 주요 프로세스:
  - `Input`: 비디오 파일 경로를 지정하여 `cv2.VideoCapture`로 로드  
    (예: `video_yeonbeom/video.mp4`, `video_hyenseok/49초.mp4` 등)
  - `Inspect`: 첫 프레임을 읽어 원본 해상도(`width`, `height`)와 FPS 정보를 출력
  - `Writer`: 원본 영상의 FPS·해상도에 맞춰 `cv2.VideoWriter`로 출력 파일(`output_blur.mp4`) 생성
  - `Detect`: MediaPipe `FaceDetection`으로 매 프레임 얼굴 위치(bounding box) 추정
  - `Pad & Clamp`: 얼굴 박스를 일정 비율(15%) 확장하고, 프레임 경계를 넘지 않도록 보정
  - `Blur`: 검출된 각 얼굴 영역에 대해 가우시안 블러(`GaussianBlur`) 적용
  - `Display`: 화면에서는 보기 편하도록 가로 1280px 기준으로 리사이즈하여 출력
  - `Output`: 블러 처리된 프레임을 동영상으로 저장하고, ESC 키 입력 시 종료

- 스크립트 구성 (`video_hyenseok/face_detection.py`):
  - **전역 설정**
    - `mp_face_detection = mp.solutions.face_detection`
    - `mp_drawing = mp.solutions.drawing_utils`
    - 입력 비디오 경로, 출력 비디오 경로를 코드 상단에서 직접 지정
  - **비디오 캡처 초기화**
    - `cv2.VideoCapture(입력경로)` 로 동영상 오픈
    - 첫 프레임을 읽어 실패 시 메시지 출력 후 종료
    - 프레임 해상도, FPS를 콘솔에 출력하고, 프레임 포인터를 0으로 되돌림
  - **VideoWriter 설정**
    - FourCC 코덱: `mp4v`
    - FPS: 입력 영상과 동일 (`cap.get(cv2.CAP_PROP_FPS)`)
    - 해상도: 입력 영상과 동일 (`CAP_PROP_FRAME_WIDTH`, `CAP_PROP_FRAME_HEIGHT`)
    - 출력 파일: `video_hyenseok/output_blur.mp4`
  - **얼굴 감지 루프**
    - `with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.1)`  
      블록 안에서 매 프레임 처리
    - `alpha`, `beta` 파라미터로 영상 대비·밝기 조절 (`cv2.convertScaleAbs`)
    - BGR → RGB 변환 후 `face_detection.process()`로 얼굴 검출
  - **Bounding Box 계산**
    - `relative_bounding_box`(비율값)를 사용해 픽셀 단위 좌표 `(x1, y1, x2, y2)` 계산
    - 가로·세로 길이의 15%를 pad로 추가하여 얼굴 주변까지 블러 처리
    - `max`, `min`으로 영상 경계 내로 좌표 클램핑
  - **블러 적용**
    - 각 얼굴 영역(`image[y1:y2, x1:x2]`)에 대해
      - 비어 있는 영역은 건너뜀
      - `cv2.GaussianBlur(face_region, (71, 71), 35)`로 강한 블러 적용
    - 블러링 된 결과를 원본 프레임의 해당 위치에 다시 덮어씀
  - **시각화 및 종료 처리**
    - 표시용 프레임은 가로 1280px로 리사이즈하여 `cv2.imshow("Face Blur", image)`로 출력
    - `cv2.waitKey(5)`에서 ESC(`27`) 입력 시 루프 종료
    - 마지막에 `cap.release()`, `out.release()`, `cv2.destroyAllWindows()`로 자원 정리

- 사용 기술 스택:
  - `Language`: Python
  - `Libraries`: OpenCV (`cv2`), MediaPipe (`mp.solutions.face_detection`)
  - 기타: 가우시안 블러를 활용한 프라이버시 보호 처리

- 기대 효과:
  - 얼굴 부분만 자동 블러 처리하여 모자이크 효과 구현
  - 해상도·FPS를 원본과 동일하게 유지하여 후속 편집 프로그램과의 호환성 확보

- 브랜치 이름: `video`
- 역할: 원본 동영상(MP4)을 입력으로 받아 해상도·밝기·색감을 표준화하고,  
  프레임 시퀀스 데이터셋과 최종 MP4 영상을 생성한다.
- 주요 프로세스:
  - `Input`: 비디오 파일 입력 (`video.mp4`)
  - `Standardize`: 16:9 비율 리사이즈 및 밝기·대비 균일화(CLAHE)
  - `Extract`: 일정 간격 프레임 샘플링 및 이미지 저장
  - `Sequence`: 연속 프레임 시퀀스 데이터셋 구성 (`.npy`)
  - `Rebuild`: 표준화 프레임을 최종 MP4 영상으로 재구성

- 모듈 구성:
- 하위 폴더: `video_yeonbeom`
  - `video.py` (Frame Processor)
    - OpenCV 기반 동영상 로드
    - 16:9 해상도 리사이즈
    - CLAHE 기반 밝기·대비 보정
    - 색감 정규화(Normalization)
    - 프레임 샘플링 및 저장
    - 연속 프레임 시퀀스 데이터셋(`.npy`) 생성
  - `final_process.py` (Video Renderer)
    - 저장된 프레임 자동 로드
    - FPS 기반 영상 재구성
    - XVID 코덱 기반 MP4 영상 생성
    - 최종 출력 파일(`final_output.mp4`) 저장

- 사용 기술 스택:
  - `Language`: Python
  - `Libraries`: OpenCV, NumPy, Glob, OS

- 기대 효과:
  - 해상도·밝기·색감이 표준화된 비디오 데이터 생성
  - 딥러닝 모델 학습용 시퀀스 데이터셋 자동 구축
  - 전처리 결과를 최종 MP4 영상으로 시각적 검증 가능
++6666666666666666666666666666666666666666666666666666666
main 브랜치
-----------

- 브랜치 이름: ``main``
- 역할: 프로젝트 공통 리소스 및 문서(Sphinx), 예제 모듈(lumache.py)을 포함합니다.
- Read the Docs에서 빌드되는 기본 브랜치입니다.

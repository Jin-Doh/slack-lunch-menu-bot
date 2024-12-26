# 점심 설문 봇 🍱

슬랙에서 점심 메뉴 설문을 자동으로 진행하는 봇입니다.
실제로 Poll을 만들어서 사용하는 것이 아니라, 슬랙 웹훅을 이용해서 해당 메시지 내 스레드 댓글을 통한 점심 메뉴를 설문하는 봇입니다.

## 기능

- 매일 지정된 시간에 점심 메뉴 설문 시작
- 슬랙 채널에 설문 결과 전송

## 시작하기

### 필수 요구사항

- Python 3.10 이상
- Docker
- Slack Webhook URL

### 환경 설정

1. 환경 변수 파일 생성 (docker/.env)
2. 환경 변수 설정
```docker/.env
SLACK_WEBHOOK_URL=your_webhook_url
SLACK_USER_NAME=lunch-bot
SLACK_CHANNEL=맛점
LOGGER_LEVEL=INFO
OPENAPI_ENCODING_KEY=your_encoding_key
OPENAPI_DECODING_KEY=your_decoding_key
```

### Docker로 실행하기

```bash
docker compose up -d
```


### 로컬에서 실행하기

1. 의존성 설치
```bash
poetry install
```

2. 실행
```bash
poetry run python main.py
```


## 프로젝트 구조

```
.
├── docker/ # Docker 관련 파일
├── modules/ # 핵심 모듈
├── utils/ # 유틸리티 함수들
├── data/ # 데이터 파일들
├── main.py # 메인 실행 파일
└── README.md
```


## 환경 변수 설명

| 변수명 | 설명 | 기본값 |
|--------|------|---------|
| SLACK_WEBHOOK_URL | Slack Incoming Webhook URL | - |
| SLACK_USER_NAME | 봇 사용자 이름 | lunch-bot |
| SLACK_CHANNEL | 대상 채널명 | 맛점 |
| LOGGER_LEVEL | 로깅 레벨 | INFO |
| OPENAPI_ENCODING_KEY | API 인코딩 키 | - |
| OPENAPI_DECODING_KEY | API 디코딩 키 | - |

## 라이선스

MIT License

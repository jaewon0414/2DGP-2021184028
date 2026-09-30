# Drill #8 애니메이션 뷰어

- 소스 파일: `Labs/LEC08_Animation/animation_viewer.py`
- 스프라이트 시트: `Labs/LEC08_Animation/hero_sheet.png` (AI를 이용해 제작한 픽셀아트 검사 캐릭터)
- 실행: `Labs/LEC08_Animation` 폴더에서 `python animation_viewer.py` (ESC 또는 창 닫기로 종료)

## 구현 내용

| 요구사항 | 구현 |
|---|---|
| Sprite Sheet | `hero_sheet.png`의 프레임 좌표를 강의의 Sprite 자료 구조(Sprite → Action tuple → Frame tuple)로 저장 |
| 애니메이션 종류 | Idle, Walk, Run, Jump, Attack **5종** |
| 크기 조정 | 서 있는 캐릭터 키(44px)가 화면 높이(600px)의 절반 이상이 되도록 배율 자동 계산 → 7배(308px) 확대 |
| 재생 위치 | 서 있는 캐릭터가 화면 중앙에 오도록 발 밑 기준 위치(`GROUND_X`, `GROUND_Y`) 설정 |
| 재생 방식 | 각 action을 5회 반복 → 마지막 프레임에서 1초 정지 → 다음 action, Attack 다음은 다시 Idle로 **무한 반복** |
| 재생 속도 | action별로 프레임 시간을 달리해 자연스럽게 조절 (Idle 0.2초 / Walk 0.12초 / Run 0.07초 / Jump 0.1초 / Attack 0.08초) |

## 가산점 기능

### 1. 프레임 크기가 프레임마다 달라지는 복잡한 Sprite Sheet 사용 (+2)

`hero_sheet.png`는 캐릭터 영역에 딱 맞게 잘린 프레임들로 되어 있어서 **프레임마다 폭과 높이가 모두 다릅니다.**
(예: Idle 19×44, Run 36×40, Attack 베기 동작은 칼 궤적 때문에 52×57)

- 프레임마다 `(left, bottom, width, height)`를 따로 저장해서 크기가 달라도 정확히 잘라냄
- 크기가 다른 프레임을 단순히 가운데 정렬하면 캐릭터가 흔들리므로, 프레임마다 **기준점 `(ax, ay)`(프레임 왼쪽 아래에서 발 밑까지의 거리)**를 함께 저장
- `draw_hero()`에서 이 기준점이 항상 화면의 같은 위치에 오도록 프레임 중심을 계산해서 그림

```python
x = GROUND_X + (width / 2 - ax) * SCALE
y = GROUND_Y + (height / 2 - ay) * SCALE
```

그 결과 Attack에서는 프레임이 넓어져도 몸과 발은 고정된 채 칼만 뻗고, Jump에서는 공중 프레임의 `ay`가 음수라 캐릭터가 실제로 떠올랐다가 착지합니다.

### 2. 애니메이션별 프레임 수가 서로 다른 경우 지원 (+2)

action마다 프레임 수가 다릅니다: **Idle 4 / Walk 6 / Run 8 / Jump 7 / Attack 6**

- 프레임 순환에 고정된 숫자 대신 **현재 action의 프레임 수**를 사용

```python
frame = (frame + 1) % len(SPRITE[action])
```

- 한 바퀴를 돌 때(`frame == 0`)마다 반복 횟수를 세기 때문에, 프레임 수와 상관없이 모든 action이 정확히 5회씩 재생됨

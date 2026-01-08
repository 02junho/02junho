# 오늘 날짜 출력 문제

from datetime import datetime
from zoneinfo import ZoneInfo

print(datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d"))

# 런타임 에러 발생 가능 - 버전 3.9 이하에서는 zoneinfo 모듈이 없음

# 서울은 UTC보다 9시간 빠름
from datetime import datetime, timedelta, timezone

seoul_timezone = datetime.now(timezone(timedelta(hours=9)))
print(seoul_timezone.strftime("%Y-%m-%d"))

# 현재 날짜와 시간 정보를 가져옵니다.
import datetime

now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d'))
"""
* logging level
debug: 개발시 처리 기록을 남겨야하는 로그 정보를 남김
info: 처리가 진행되는 동안의 정보를 알림
warning: 사용자가 잘못 입력한 정보 또는 개발 의도와 다른 정보가 입력되었을 때 알림
error: 잘못된 처리로 에러가 발생했으나 프로그램 동작에는 문제가 없는 경우 --> exception
critical: 잘못된 처리로 데이터 손실 또는 프로그램이 동작하지 않는 경우 --> 데이터가 삭제되거나, 사용자에 의해 강제종료
"""

import logging

logger = logging.getLogger("main")  # Logger 선언
stream_handler = logging.StreamHandler()  # Logger output 방법 선언, console / file / DB 등
logger.addHandler(stream_handler)  # Logger의 output 지정

logger.setLevel(logging.DEBUG)  # logging level 설정
logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")



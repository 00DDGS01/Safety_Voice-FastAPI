import httpx

SPRING_BASE_URL = "http://localhost:8080"

async def notify_spring_voice_trained(user_jwt: str):
    """
    Spring 서버에 음성 학습 완료 알림을 보냅니다.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.patch(
                f"{SPRING_BASE_URL}/api/user/settings/voice-trained",
                headers={"Authorization": f"Bearer {user_jwt}"}
            )
            response.raise_for_status()
            print("Spring 서버에 음성 학습 상태 업데이트 성공")
        except httpx.HTTPError as e:
            print(f"Spring 서버 호출 실패 : {e}")
            raise RuntimeError(f"Spring 서버 호출 실패 : {e}") from e
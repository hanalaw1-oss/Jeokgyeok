import flet as ft
import numpy as np


def main(page: ft.Page):
    page.title = "나라장터 적격심사 계산기"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # 가상의 과거 데이터 (기존 로직 대입용)
    past_rates = [100.25, 99.90, 100.15, 100.20, 99.95, 99.80]

    # UI 입력 필드 구성
    agency_input = ft.TextField(label="1. 수요기관명", hint_text="예: 서울특별시")
    base_price_input = ft.TextField(
        label="2. 기초금액 (원)", value="150000000", keyboard_type=ft.KeyboardType.NUMBER
    )
    limit_rate_input = ft.TextField(
        label="3. 낙찰하한율 (%)", value="87.745", keyboard_type=ft.KeyboardType.NUMBER
    )

    # 결과 출력 텍스트 공간
    result_text = ft.Text(value="", size=16, color="blue700", weight=ft.FontWeight.BOLD)

    # 버튼 클릭 시 계산 및 결과 출력 로직
    def calculate_click(e):
        try:
            base_price = int(base_price_input.value)
            limit_rate = float(limit_rate_input.value)

            # 계산 로직 (평균 사정율 적용)
            pred_rate = np.mean(past_rates)
            pred_yega = base_price * (pred_rate / 100)
            raw_bid = pred_yega * (limit_rate / 100)
            final_bid = int(np.ceil(raw_bid / 10) * 10)

            # 결과 텍스트 업데이트
            result_text.value = (
                f"📈 적용 사정율: {pred_rate:.4f}%\n"
                f"💰 예측 예정가격: {int(pred_yega):,} 원\n"
                f"🎯 최종 추천 투찰금액: {final_bid:,} 원"
            )
            result_text.color = "blue700"
        except ValueError:
            result_text.value = "⚠️ 금액과 하한율에 숫자 형식을 올바르게 입력해주세요."
            result_text.color = "red"
        page.update()

    # 화면에 UI 컴포넌트 배치
    page.add(
        ft.Text("🏛️ 나라장터 적격심사 계산기", size=24, weight=ft.FontWeight.BOLD),
        agency_input,
        base_price_input,
        limit_rate_input,
        # ⚠️ 최신 문법 반영: ElevatedButton 대신 ft.Button 사용
        ft.Button("투찰금액 산출하기", on_click=calculate_click),
        ft.Divider(),
        result_text,
    )


# 앱 실행
if __name__ == "__main__":
    # ⚠️ 최신 문법 반영: app() 대신 run() 사용
    ft.run(main)

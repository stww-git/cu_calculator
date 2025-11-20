import datetime
import sys

# ================================
# 안전수량 정의
# ================================
SAFETY_STOCK = {
    "도시락": 1,
    "삼각김밥": 2,
    "김밥": 1,
    "샌드위치": 1,
    "햄버거": 1,
    "빵": 1,
    "디저트": 1
}

# ================================
# 발주 계산 함수
# ================================
def calc_two_step(item, vol):
    """1차 = 판매량 * 0.2 + 안전수량 / 2차 = 판매량 * 0.8"""
    first = vol * 0.2 + SAFETY_STOCK[item]
    second = vol * 0.8
    return round(first), round(second)

def calc_single_step(item, vol):
    """총 수량 = 판매량 + 안전수량"""
    return round(vol + SAFETY_STOCK[item])


# ================================
# 날짜 계산
# ================================
def calculate_reference_date():
    now = datetime.datetime.now()
    today = now.date()
    cutoff = datetime.time(10, 0)

    # 발주일 계산
    if now.time() < cutoff:
        order_date = today
    else:
        order_date = today + datetime.timedelta(days=1)

    # 발주일 다음날 = 판매일
    sales_date = order_date + datetime.timedelta(days=1)

    # 저번주 동일 판매일
    reference_date = sales_date - datetime.timedelta(days=7)

    return order_date, sales_date, reference_date


# ================================
# 사용자 입력 처리 함수
# ================================
def get_valid_input(item_name, reference_date):
    """유효한 판매량 입력을 받는 함수"""
    while True:
        try:
            user_input = input(f"📦 {item_name} 판매량 입력 (참고일: {reference_date}): ").strip()
            
            # 빈 입력 처리
            if not user_input:
                print("⚠️  값을 입력해주세요.")
                continue
            
            # 숫자 변환
            value = int(user_input)
            
            # 음수 체크
            if value < 0:
                print("⚠️  판매량은 0 이상의 숫자만 입력 가능합니다.")
                continue
            
            return value
            
        except ValueError:
            print("⚠️  숫자만 입력해주세요. (예: 10)")
        except KeyboardInterrupt:
            print("\n\n❌ 프로그램이 중단되었습니다.")
            sys.exit(0)
        except Exception as e:
            print(f"⚠️  오류가 발생했습니다: {e}")
            print("다시 시도해주세요.")


def confirm_inputs(sales):
    """입력값 확인 함수"""
    print("\n" + "="*50)
    print("📋 입력하신 판매량 확인")
    print("="*50)
    for item, quantity in sales.items():
        print(f"  {item:10s}: {quantity:>4d}개")
    print("="*50)
    
    while True:
        confirm = input("\n입력값이 맞나요? (Y/N): ").strip().upper()
        if confirm in ['Y', 'YES', '예', 'ㅛ']:
            return True
        elif confirm in ['N', 'NO', '아니오', '아니요', 'ㄴ']:
            return False
        else:
            print("⚠️  Y 또는 N을 입력해주세요.")


def get_corrected_input(item_name, reference_date, current_value):
    """수정된 입력을 받는 함수"""
    print(f"\n현재 입력값: {item_name} = {current_value}개")
    return get_valid_input(item_name, reference_date)


# ================================
# 메인 프로그램
# ================================
def main():
    print("\n" + "="*60)
    print("  🏪 편의점 자동 발주 시스템 (안전수량 적용 버전)")
    print("="*60 + "\n")

    try:
        order_date, sales_date, reference_date = calculate_reference_date()
        weekday_map = ["월", "화", "수", "목", "금", "토", "일"]

        print("📅 날짜 정보")
        print("-" * 60)
        print(f"  발주 마감일 → {order_date} ({weekday_map[order_date.weekday()]})")
        print(f"  참고일      → {reference_date} ({weekday_map[reference_date.weekday()]})")
        print("-" * 60)
        print(f"\n💡 안내: {reference_date} ({weekday_map[reference_date.weekday()]})의 판매량을 입력해주세요.\n")

        sales = {}
        items = ["도시락", "삼각김밥", "김밥", "샌드위치", "햄버거", "빵", "디저트"]

        # 판매량 입력
        for item in items:
            sales[item] = get_valid_input(item, reference_date)

        # 입력값 확인 및 수정
        while True:
            if confirm_inputs(sales):
                break
            else:
                print("\n수정할 품목을 선택해주세요:")
                for idx, item in enumerate(items, 1):
                    print(f"  {idx}. {item}")
                print(f"  0. 모두 다시 입력")
                
                try:
                    choice = input("\n선택 (번호 입력): ").strip()
                    
                    if choice == "0":
                        # 모두 다시 입력
                        for item in items:
                            sales[item] = get_valid_input(item, reference_date)
                    else:
                        choice_num = int(choice)
                        if 1 <= choice_num <= len(items):
                            item_to_modify = items[choice_num - 1]
                            sales[item_to_modify] = get_corrected_input(
                                item_to_modify, reference_date, sales[item_to_modify]
                            )
                        else:
                            print("⚠️  올바른 번호를 입력해주세요.")
                except ValueError:
                    print("⚠️  숫자를 입력해주세요.")
                except KeyboardInterrupt:
                    print("\n\n❌ 프로그램이 중단되었습니다.")
                    sys.exit(0)

        # 발주 결과 계산 및 출력
        print("\n" + "="*60)
        print("  📊 발주 결과 (안전수량 적용)")
        print("="*60)

        two_step_items = ["도시락", "삼각김밥", "김밥", "샌드위치", "햄버거"]

        print("\n🔄 2차 발주 품목:")
        print("-" * 60)
        for item in two_step_items:
            f, s = calc_two_step(item, sales[item])
            print(f"  {item:10s} → 1차: {f:>3d}개  /  2차: {s:>3d}개  (총: {f+s:>3d}개)")

        print("\n📦 1차 발주 품목:")
        print("-" * 60)
        bread_qty = calc_single_step('빵', sales['빵'])
        dessert_qty = calc_single_step('디저트', sales['디저트'])
        print(f"  빵         → 총 {bread_qty:>3d}개")
        print(f"  디저트     → 총 {dessert_qty:>3d}개")

        # 총 발주량 계산
        total_qty = 0
        for item in two_step_items:
            f, s = calc_two_step(item, sales[item])
            total_qty += f + s
        total_qty += bread_qty + dessert_qty

        print("\n" + "="*60)
        print(f"  ✅ 총 발주량: {total_qty}개")
        print("="*60)
        print("\n✨ 발주 계산이 완료되었습니다!\n")

        # 프로그램 종료 전 대기
        input("계속하려면 Enter 키를 누르세요...")

    except KeyboardInterrupt:
        print("\n\n❌ 프로그램이 중단되었습니다.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 오류가 발생했습니다: {e}")
        print("프로그램을 종료합니다.")
        sys.exit(1)


if __name__ == "__main__":
    main()

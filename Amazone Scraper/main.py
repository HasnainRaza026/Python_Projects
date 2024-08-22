from get_price import get_product_price
from send_email import send_alert_email

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


def main():
    price = get_product_price(PRODUCT_URL)

    if not price:
        print("No price found!")
        return
    elif price <= 100:
        send_alert_email(price)


if __name__ == "__main__":
    main()

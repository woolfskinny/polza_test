import dns.resolver
import re
import sys
from config import EMAILS_FILEPATH

def check_email_domain(email):
    domain_checker = re.search(r'@(.+)$', email)
    if not domain_checker:
        return "Некорректный формат e-mail."

    domain = domain_checker.group(1)

    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        if len(mx_records) > 0:
            return "Домен валиден."
        else:
            return "MX-записи отсутствуют или некорректны."
    except dns.resolver.NXDOMAIN:
        return "Домен отсутствует."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def main():
    try:
        with open(EMAILS_FILEPATH, 'r') as file:
            emails = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Файл {EMAILS_FILEPATH} не найден!")
        sys.exit(1)

    print("Результаты проверки email-доменов:")

    for email in emails:
        domain_status = check_email_domain(email)
        print(f"{email}: {domain_status}")

if __name__ == "__main__":
    main()
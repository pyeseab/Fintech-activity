#CLI based portfolio
from routes.users import add_user, get_user_by_id
from routes.portfolio import add_portfolio, get_user_portfolios
from routes.advice import advice_for_user_portfolios
from services.report_gen import generate_user_report
from utils.logger import logger
from utils.security import hash_password

def main():
    print("Welcome to the Portfolio Evaluation App!\n")

    # Example: Add a new user
    username = input("Enter a new username: ")
    password = input("Enter a password: ")
    hashed_pw = hash_password(password)
    
    result = add_user(username, hashed_pw)
    print(result)
    logger.info(f"User '{username}' added.")

    # Example: Add a portfolio
    user = get_user_by_id(1)  # For demo, assume user ID 1
    if user:
        print(f"Adding portfolio for {user['username']}...")
        add_portfolio(user_id=1, name="Tech Growth Fund", sharpe_ratio=1.4)
        logger.info("Portfolio added.")

    # Example: Generate advice
    advice_text = advice_for_user_portfolios(user_id=1)
    print("\nPortfolio Advice:")
    print(advice_text)

    # Example: Generate a report
    report = generate_user_report(user_id=1)
    print("\nFull Report:")
    print(report)
    logger.info("User report generated.")


if __name__ == "__main__":
    main()

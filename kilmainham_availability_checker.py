import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def check_tour_availability(year, month, target_dates):
    """
    Check tour availability for specific dates in a given month.
    
    :param year: Year to check (4-digit)
    :param month: Month to check (1-12)
    :param target_dates: List of dates to check availability
    :return: Dict of available dates with their links
    """
    # Construct the URL for the specific month
    url = f"https://kilmainhamgaol.admit-one.eu/?p=calendar&ev=TOUR&mn={year}{month:02d}"
    
    try:
        # Send a request to the webpage
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find availability for target dates
        available_dates = {}
        for date in target_dates:
            # Look for the specific date cell
            date_cell = soup.find('div', text=str(date))
            
            # Check if the date is available
            if date_cell and date_cell.parent.name == 'a':
                available_dates[date] = date_cell.parent['href']
        
        return available_dates
    
    except requests.RequestException as e:
        print(f"Error fetching availability: {e}")
        return {}

def send_telegram_message(bot_token, chat_id, message):
    """
    Send a Telegram message about tour availability.
    
    :param bot_token: Telegram Bot API token
    :param chat_id: Telegram chat ID to send message to
    :param message: Message text to send
    """
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    
    try:
        response = requests.post(telegram_url, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error sending Telegram message: {e}")

def main():
    # Get environment variables
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    # Example: Check availability for dates in December 2024
    year = 2024
    month = 12
    target_dates = [8,9,10]
    
    # Check availability
    available_dates = check_tour_availability(year, month, target_dates)
    
    # Prepare message
    if available_dates:
        message = f"Available Kilmainham Gaol Tours in {year}-{month:02d}:\n"
        for date, link in available_dates.items():
            message += f"{date}: {link}\n"
    else:
        message = f"No available tours found for {year}-{month:02d}"
    
    # Send Telegram message
    if bot_token and chat_id:
        send_telegram_message(bot_token, chat_id, message)
    else:
        print("Telegram bot token or chat ID not set")

if __name__ == "__main__":
    main()

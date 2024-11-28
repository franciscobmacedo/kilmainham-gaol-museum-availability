# Kilmainham Gaol Tour Availability Tracker

## Overview

This GitHub Actions-powered script automatically checks tour availability at the Kilmainham Gaol Museum in Dublin, Ireland. It scrapes the museum's booking website daily and sends notifications via Telegram when specific dates become available.

### Background

This project was developed as a companion to the article: [Track Museum Availability with AI](https://fmacedo.com/posts/track-museum-availability-with-ai). It was mostly written by [Claude AI](https://claude.ai/) an the full conversation can be found [here](./conversation.md).

## Features

- Daily automated checking of tour availability
- Customizable date targeting
- Telegram notification integration
- Runs on GitHub Actions for free

## Setup

1. Clone the repository
2. Create Telegram Bot (check [this tutorial](https://gist.github.com/nafiesl/4ad622f344cd1dc3bb1ecbe468ff9f8a?permalink_comment_id=5181872) if not sure):
   - Use BotFather on Telegram to create a bot
   - Obtain bot token and chat ID


3. Set up GitHub Secrets:
   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
   - `TELEGRAM_CHAT_ID`: Telegram chat ID for notifications

## Usage

Modify `target_dates` in `kilmainham_availability_checker.py` to track specific dates of interest.

## Dependencies

- Python 3.9+
- `requests`
- `beautifulsoup4`


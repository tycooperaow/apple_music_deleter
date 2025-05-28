# Automatic Apple Music Deleter

A Selenium-based bot to automatically delete songs from your Apple Music library via the web interface.

## Video Tutorial
Watch a video tutorial on how to use this bot:

<iframe width="560" height="315" src="https://www.youtube.com/embed/7bDLTM5qMOE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Features
- Deletes all visible songs from your Apple Music library page in bulk
- Logs each deleted song to a CSV file
- Interactive mode: allows you to refresh and repeat deletions

## Requirements
- **Python 3.7+**
- **Selenium** (`pip install selenium`)
- **Chromedriver**: Download from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and place the binary at `./chromedriver/chromedriver` relative to this project directory
- **Chromium-based browser** (e.g., Brave, Chrome, Chromium) for best compatibility

## Setup
1. **Install Python dependencies:**
   ```bash
   pip install selenium
   ```
2. **Download Chromedriver:**
   - Go to [Chromedriver downloads](https://chromedriver.chromium.org/downloads)
   - Download the version matching your browser
   - Place the `chromedriver` binary in a folder named `chromedriver` in this project directory: `./chromedriver/chromedriver`
3. **Install a Chromium-based browser:**
   - The script is configured for Brave by default. You can change the path in `bot.py` (`binaryPath`).
   - Chrome or Chromium also work. Update the `binaryPath` variable if needed.

## Usage
1. **Run the bot:**
   ```bash
   python bot.py
   ```
2. **To use interactive mode, run:**
   ```bash
   python -i bot.py
   ```
3. **Manual Apple ID Login Required:**
   - The bot will open a browser window and navigate to Apple Music.
   - You must log in manually due to Apple popups and 2FA (two-factor authentication).
   - After logging in and reaching your library, press Enter in the terminal to continue.
4. **Interactive Deletion:**
   - The bot will attempt to delete all visible songs on the page.
   - It will log each deleted song to `song.csv`.
   - The bot will refresh and repeat until no more songs are found.
   - You can stop the bot at any time with `Ctrl+C`.

## Notes
- **Apple's web UI may change:** This script relies on specific element selectors that may break if Apple updates their site.
- **2FA and popups:** The bot cannot bypass Apple's two-factor authentication or popups. Manual login is required each session.
- **Browser path:** If you use a browser other than Brave, update the `binaryPath` in `bot.py` accordingly.

## Troubleshooting
- If the bot cannot find `chromedriver`, ensure it is at `./chromedriver/chromedriver` and is executable.
- If the browser does not open, check the `binaryPath` in `bot.py`.
- If selectors break, the script may need updating to match Apple's latest web UI.

## Support & Donations
If you found this project helpful, consider supporting my development contribution! Crypto is strongly preferred, but other options are available:

- **Card:** [Donate via Stripe](https://buy.stripe.com/7sYdR8gJk0wCflsgfvdjO01)
- **PayPal:** [paypal.me/tycooperaow](https://paypal.me/tycooperaow)
- **Bitcoin:** `35WJjcwyQTCD6gLwKhxypmmjZDUaYRhLMJ`
- **Ethereum:** `0x6bBF37fdBfacBE9C93faC1aF32E12439aCA44475`
- **Solana:** `9mSCuBMNkhWjNvHZNWTU4UMgrsFaEdDxnB8ZkaXtQuz9`

Thank you for your support!



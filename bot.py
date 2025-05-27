from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

# WARNING: Apple Music's web UI is fragile and may change element IDs/classes at any time
class AppleDeleteBot:
    def __init__(self):
        driverPath = os.getenv('PATH_TO_CHROME_DRIVER')
        binaryPath = os.getenv('PATH_TO_CHROME_BINARY')

        self.driver_options = webdriver.ChromeOptions()
        self.driver_options.binary_location = binaryPath
        self.driver = webdriver.Chrome(executable_path=driverPath, options=self.driver_options)
        self.wait = WebDriverWait(self.driver, 20)
        self.refresh_count = 0
        
        # Initialize CSV file with headers if it doesn't exist
        try:
            with open('song.csv', 'x', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Timestamp', 'Song Name', 'Refresh Count'])
        except FileExistsError:
            pass  # File already exists, no need to create headers

    def close_browser(self):
        self.driver.quit()

    def save_to_csv(self, song_name):
        """Save deleted song to CSV file"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('song.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, song_name, self.refresh_count])

    def login(self):
        """Go to songs page. If already logged in, just press Enter. If not logged in, log in first."""
        try:
            # Try going directly to songs page
            self.driver.get('https://music.apple.com/library/songs')
            time.sleep(2)
            
            # Check if we need to log in
            if "Sign In" in self.driver.page_source:
                print("Please log in manually...")
                input("Press Enter after you've logged in...")
                self.driver.get('https://music.apple.com/library/songs')
            
            time.sleep(3)  # Wait for songs to load
            print("Ready to delete songs!")
            
        except Exception as e:
            print(f"Error during login: {str(e)}")

    def refresh_and_wait(self):
        """Refresh the page and wait for songs to load"""
        self.refresh_count += 1
        print(f"\n🔄 Refreshing page (Refresh #{self.refresh_count})...")
        self.driver.refresh()
        time.sleep(5)  # Wait for songs to load
        print("Page refreshed, ready for more deletions!")

    def delete_songs(self):
        """Delete all visible songs on the current page"""
        try:
            # Find all song entries
            songs = self.driver.find_elements(By.CSS_SELECTOR, "div[data-testid='library-track']")
            
            if not songs:
                print("No songs found on current page. Try refreshing with bot.refresh_and_wait()")
                return
            
            print(f"Found {len(songs)} songs to delete")
            
            for i, song in enumerate(songs, 1):
                try:
                    # Get song name before deletion
                    song_name = song.find_element(By.CSS_SELECTOR, "span.library-track-name__text").text
                    print(f"🔴 {song_name}")
                    
                    # Hover to reveal 3-dot menu
                    webdriver.ActionChains(self.driver).move_to_element(song).perform()
                    
                    # Click MORE button (3-dot menu)
                    menu_button = song.find_element(By.CSS_SELECTOR, "button[aria-label='more']")
                    menu_button.click()
                    
                    # Click "Delete From Library" option
                    delete_option = self.wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//button[@title='Delete From Library']")
                    ))
                    delete_option.click()
                    
                    # Wait for and click the OK button in the confirmation dialog
                    ok_button = self.wait.until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "button[data-testid='button-base']")
                    ))
                    ok_button.click()
                    
                    # Save to CSV after successful deletion
                    self.save_to_csv(song_name)
                    
                    print(f"   ✓ Deleted ({i}/{len(songs)})")
                    time.sleep(1)  # Pause between deletions
                    
                except Exception as e:
                    print(f"Error processing song {i}: {str(e)}")
                    continue
            
            print("Finished deleting visible songs. Automatically refreshing in 5 seconds...")
            time.sleep(5)  # Wait 5 seconds before auto-refresh
            self.refresh_and_wait()
            return True  # Return True to indicate we should continue
            
        except Exception as e:
            print(f"Error during deletion: {str(e)}")
            return False  # Return False to indicate we should stop

    def run(self):
        """Run the complete process"""
        try:
            self.login()
            while True:
                if not self.delete_songs():  # If delete_songs returns False, stop
                    break
                # No need for input prompt since delete_songs handles refresh
        finally:
            self.close_browser()

if __name__ == "__main__":
    bot = AppleDeleteBot()
    bot.run()
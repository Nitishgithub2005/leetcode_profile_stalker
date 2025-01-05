# leetcode_profile_stalker

This Python script helps track the most recent solved question on a LeetCode user's profile. It continuously monitors the profile and sends an email
notification whenever a new question is solved.
Features:
• Continuous Monitoring: The script runs in the background, checking the user's LeetCode profile for any newly solved questions.
• Email Notifications: When a new question is solved, it sends an email notification with the problem link and the date it was solved.
• Data Persistence: The script keeps track of the last solved question using a local JSON file, ensuring that you only receive notifications for new questions.
Prerequisites:
• Selenium: To scrape and interact with the LeetCode profile page.
• BeautifulSoup: To parse the HTML and extract relevant data.
• Email Setup: Requires a Gmail account for sending notifications. Use App Passwords if two-factor authentication (2FA) is enabled.
Setup Instructions:
1. Clone this repository:
```bash
git clone https://github.com/your-username/leetcode_profile_stalker.git
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

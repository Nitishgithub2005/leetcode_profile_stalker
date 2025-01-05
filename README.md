leetcode_profile_stalker🚀

Need some motivation to level up your LeetCode game? Meet LeetCode Question Stalker — a Python-powered script that not only tracks your progress but also keeps you motivated by notifying you when your friends solve a new question!

What It Does:
	•	Instant Notifications: Get an email the moment your friend solves a new question on LeetCode. You don’t have to refresh your profile anymore – the script does it all!
	•	Always Watching: Runs in the background and keeps an eye on your friend’s LeetCode profile, so you never miss their latest solved problem.
	•	Motivation Booster: It remembers the last problem your friend solved and only sends you an email when they crack a new one. It’s like a friendly challenge!
	•	Email Alerts: Receive real-time email notifications about the problem name, link, and date. Perfect for staying on top of your own progress and keeping the friendly competition going!

Why It’s Awesome:
	•	Boost Your Motivation: The moment your friend solves a new problem, you get notified, sparking you to solve even more! 🏆
	•	No More Refreshing: Forget about checking your friend’s profile constantly. Let the script do the work and notify you instantly.
	•	Real-Time Updates: Get the latest solved question details sent straight to your inbox. Perfect for tracking your friend’s progress and staying motivated.


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
3. Run the Script:
```bash
python3 script_name.py
```
4. Enter your LeetCode username and let the stalker do its thing!


Notes:
	•	You may need to adjust the email and SMTP settings in the script to match your email provider’s requirements.
	•	Ensure that chromedriver is installed and accessible for Selenium to work correctly.

@title Eiden Feedback
# BOT_TOKEN - it's Telegram Bot's token. You can get it from @Botfather
@set BOT_TOKEN="0000000:AAAAAAAAAAAAAAAA"
# ID_FEEDBACK_TO - it's Telegram User's ID (ID, not username). You can get it... by multiple ways
@set ID_FEEDBACK_TO="012345678"
docker run -e "BOT_TOKEN=%BOT_TOKEN%" -e "ID_FEEDBACK_TO=%ID_FEEDBACK_TO%" -t eiden_feed_v1.1
pause

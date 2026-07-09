import os
import telebot
from dotenv import load_dotenv

# Ambil token dari pengaturan Railway
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# ---------------------- PESAN BAHASA INGGRIS ----------------------
START_MSG = """🐼 Welcome to Bamboo Panda!

The Community-Driven Meme Token on Solana.

Join our mission to build one of the strongest crypto communities.

Choose an option below 👇"""

INFO_MSG = """🐼 Bamboo Panda

Blockchain: Solana

Mission:
Building a strong, transparent and community-driven meme token with long-term utility.

Status:
🟢 Community Building"""

SOCIAL_MSG = """🌐 Website
https://bambopandau-bit.github.io/

📄 Whitepaper
https://bambopandau-bit.github.io/whitepaper.pdf

💬 Official Telegram
https://t.me/bamboopanda_official

❌ X (Twitter)
https://x.com/BamboPanda_coin

ℹ️ Note: Website, whitepaper and X page are being prepared. Only Telegram channel is active now."""

ROADMAP_MSG = """🗺 Roadmap

✅ Phase 1 — Completed
• Branding
• Website
• Whitepaper
• Telegram Channel
• X Account

⏳ Phase 2 — In Progress
• Community Growth
• Marketing Campaigns
• Airdrop Program

🔜 Phase 3 — Upcoming
• Official Token Launch
• DEX Listing
• CoinGecko Listing
• CoinMarketCap Listing

🔮 Phase 4 — Future Plans
• Strategic Partnerships
• Staking Features
• NFT Collection"""

TOKENOMICS_MSG = """📊 Tokenomics

Total Supply: 1,000,000,000 BP
Liquidity: 🔒 Locked
Ownership: ✅ Renounced
Transaction Tax: 0%
Network: Solana

*Figures may be adjusted before final launch*"""

TASKS_MSG = """🎁 Earn XP Points

Complete these tasks to earn XP:
✅ Join Official Telegram Channel
✅ Follow Official X Account
✅ Like the Pinned Post
✅ Repost / Share the Pinned Post
✅ Invite Friends to Join

More tasks coming soon!"""

XP_MSG = """👤 Your XP Status

Current XP: 0
Rank: New Panda 🐼"""

LEADERBOARD_MSG = """🏆 Top XP Leaderboard

🥇 User 1
🥈 User 2
🥉 User 3

*Rankings update as members earn XP*"""

HELP_MSG = """🆘 Support & Help

Contact our official admin if you have questions.

⚠️ IMPORTANT SAFETY WARNING
Admins will **NEVER** ask for your seed phrase, private key, or wallet password.
Always verify identities and avoid scams!"""

# ---------------------- PERINTAH BOT ----------------------
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, START_MSG)

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, INFO_MSG)

@bot.message_handler(commands=['social'])
def send_social(message):
    bot.send_message(message.chat.id, SOCIAL_MSG)

@bot.message_handler(commands=['roadmap'])
def send_roadmap(message):
    bot.send_message(message.chat.id, ROADMAP_MSG)

@bot.message_handler(commands=['tokenomics'])
def send_tokenomics(message):
    bot.send_message(message.chat.id, TOKENOMICS_MSG)

@bot.message_handler(commands=['tasks'])
def send_tasks(message):
    bot.send_message(message.chat.id, TASKS_MSG)

@bot.message_handler(commands=['xp'])
def send_xp(message):
    bot.send_message(message.chat.id, XP_MSG)

@bot.message_handler(commands=['leaderboard'])
def send_leaderboard(message):
    bot.send_message(message.chat.id, LEADERBOARD_MSG)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, HELP_MSG)

# ---------------------- MENJALANKAN BOT ----------------------
if __name__ == "__main__":
    print("🐼 Bamboo Panda Bot is running on Railway...")
    bot.infinity_polling()

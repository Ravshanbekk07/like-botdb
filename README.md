# Like/Dislike Counter Telegram Bot

This Telegram bot is designed to help you keep track of likes and dislikes from users in your Telegram group or channel. With this bot, you can easily monitor and tally the number of likes and dislikes for each user.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Bot Commands](#bot-commands)
  - [Example Usage](#example-usage)

## Getting Started

### Prerequisites

Before using this bot, you'll need the following:

- A Telegram account.
- A Telegram bot token. You can obtain one by talking to the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

### Installation

1. Clone this repository to your local machine or server.

   ```bash
   git clone https://github.com/your-username/like-dislike-counter-bot.git
   ```

2. Navigate to the project directory.

   ```bash
   cd like-dislike-counter-bot
   ```

3. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your Telegram bot token.

   ```bash
   echo "TELEGRAM_BOT_TOKEN=your-bot-token" > .env
   ```

5. Start the bot.

   ```bash
   python bot.py
   ```

Now, your Like/Dislike Counter Telegram bot should be up and running!

## Usage

### Bot Commands

The bot understands the following commands:

- `/like`: Use this command to like a post.
- `/dislike`: Use this command to dislike a post.
- `/stats`: Use this command to view your own like and dislike counts.
- `/top`: Use this command to view the top users with the most likes or dislikes.

### Example Usage

1. In your Telegram group or channel, invite the bot and give it appropriate permissions.

2. Users can now use the bot by sending commands in the group. For example:

   - User 1: `/like`
   - User 2: `/like`
   - User 3: `/dislike`

3. To view their own stats:

   - User 1: `/stats`

   The bot will reply with something like:

   ```
   Your Like Count: 1
   Your Dislike Count: 0
   ```

4. To view the top users with the most likes:

   - User 1: `/top like`

   The bot will reply with a list of users sorted by the number of likes:

   ```
   Top Likers:
   1. User 1 - 3 Likes
   2. User 2 - 2 Likes
   3. User 3 - 1 Like
   ```

   - User 1: `/top dislike`

   The bot will reply with a list of users sorted by the number of dislikes:

   ```
   Top Dislikers:
   1. User 3 - 1 Dislike
   ```

## Contributing

Contributions are welcome! If you have any ideas or improvements for this bot, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
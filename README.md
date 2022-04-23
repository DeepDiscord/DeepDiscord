# DeepDiscord

Search Discord's "Deep Web"

## Setting up the .env.txt file

Create a new .env.txt file in `bot/` by running `cp env.txt.example env.txt`. Edit this file by running and fill in the details. Here are what all of the details in the env mean:

* PORT - The port the web server will listen on
* TOKEN - The token for the Discord bot
* PRODUCTION - Should the site be in production or no
* SITE_URL - Domain of the website (example.com)
* PROTO - https or http, whichever one you use
* KEYS - API keys in JSON form (ex. `{"key1", "key2"}`)

## Notes

For some reason, I threw the .env.txt file in the bot folder. Sorry about this, should be fixed in a future release.

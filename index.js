const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Bot is Online!');
});

app.listen(3000, () => {
  console.log('Server is ready!');
});

// --- هنا تضع كود بوت الديسكورد الخاص بك (discord.js) ---
const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.login('ضع_التوكن_هنا');

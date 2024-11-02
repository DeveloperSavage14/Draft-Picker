const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('example')
        .setDescription('An example command')
        .addSubcommand(subcommand =>
            subcommand.setName('sub1').setDescription('Subcommand 1')
        )
        .addSubcommand(subcommand =>
            subcommand.setName('sub2').setDescription('Subcommand 2')
        )
        .addSubcommand(subcommand =>
            subcommand.setName('sub3').setDescription('Subcommand 3')
        ),
    async execute(interaction) {
        await interaction.reply('This is a response to the example command.');
    },
};
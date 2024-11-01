const { SlashCommandBuilder } = require("discord.js");

module.exports = {
    data: new SlashCommandBuilder()

        .setName("example")
        .setDescription("An example command")
        .addSubcommand(subcommand =>
            subcommand.setName("sub1").setDescription("Subcommand 1")
        )
};



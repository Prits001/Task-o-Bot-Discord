import discord, dotenv, os, json
dotenv.load_dotenv()
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")



@bot.slash_command(name="create-task", description="Create a new task!")
async def record_message(ctx, message: str):
    user_id = ctx.author.id

    with open("messages.json", "r") as f:
        data = json.load(f)
        if str(user_id) in data:
            data[str(user_id)]["messages"].append(message)
        else:
            data[str(user_id)] = {"messages": [message]}

    with open("messages.json", "w") as f:
        json.dump(data, f)

    await ctx.respond(f"Task recorded for user {ctx.author.name}")

@bot.slash_command(name="read-tasks", description="Reads a list of already created tasks!")
async def get_messages(ctx):
    user_id = ctx.author.id

    with open("messages.json", "r") as f:
        data = json.load(f)
        if str(user_id) in data:
            messages = data[str(user_id)]["messages"]
            message_str = ""
            for i, message in enumerate(messages):
                message_str += f"{i + 1}) {message}\n"
            if message_str:
                await ctx.respond(f"Your recorded tasks:\n{message_str}")
            else:
                await ctx.respond("You haven't recorded any tasks yet.")
        else:
            await ctx.respond("You haven't recorded any tasks yet.")

@bot.slash_command(name="erase-task", description="Delete a certain task!")
async def erase_message(ctx, message_id: int):
    user_id = ctx.author.id
    message_id -= 1

    with open("messages.json", "r") as f:
        data = json.load(f)
        if str(user_id) in data:
            messages = data[str(user_id)]["messages"]
            if message_id in messages:
                messages.remove(message_id)
                data[str(user_id)]["messages"] = messages
                with open("messages.json", "w") as f:
                    json.dump(data, f, indent=4)
                await ctx.respond(f"Task with ID {message_id} has been erased.")
            else:
                await ctx.respond(f"Task with ID {message_id} does not exist.")
        else:
            await ctx.respond("You haven't recorded any tasks yet.")

@bot.slash_command(name="delall-tasks", description="Delete the whole list of tasks!")
async def delete_all_messages(ctx):
    user_id = ctx.author.id

    with open("messages.json", "r") as f:
        data = json.load(f)
        if str(user_id) in data:
            data[str(user_id)]["messages"] = []
            with open("messages.json", "w") as f:
                json.dump(data, f, indent=4)
            await ctx.respond(f"All tasks have been erased!")
        else:
            await ctx.respond("You haven't recorded any tasks yet.")

bot.run(os.getenv("TOKEN"))

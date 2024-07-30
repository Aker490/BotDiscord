import discord
from discord.ext import commands
from discord.ui import Button, View
import os

from serverbot import server_on

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def role_button(ctx):
    # สร้างปุ่ม
    button = Button(label="รับยศ", style=discord.ButtonStyle.success, custom_id="get_role")

    # สร้าง View สำหรับปุ่ม
    view = View()
    view.add_item(button)

    # สร้าง Embed
    embed = discord.Embed(title="กดปุ่มเพื่อรับยศ", color=0xE2ABE6)
    image_url = "https://example.com/path/to/image.png"  # เปลี่ยนเป็น URL ของรูปภาพที่ต้องการใช้
    embed.set_image(url=image_url)
    
    # ส่ง Embed พร้อมปุ่ม
    await ctx.send(embed=embed, view=view)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.component and interaction.data["custom_id"] == "get_role":
        role_id = 1229803400867221654  # เปลี่ยนเป็นไอดียศที่ต้องการ
        role = interaction.guild.get_role(role_id)

        if role:
            try:
                await interaction.user.add_roles(role)
                await interaction.response.send_message("คุณได้รับยศเรียบร้อยแล้ว!", ephemeral=True)
            except Exception as e:
                print(f'Error adding role: {e}')
                await interaction.response.send_message("ไม่สามารถเพิ่มยศให้คุณได้.", ephemeral=True)
        else:
            await interaction.response.send_message("ไม่พบยศที่ต้องการ", ephemeral=True)

server_on()

bot.run(os.getenv('TOKEN'))

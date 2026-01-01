# Zed-Thon - ZelZal
# Copyright (C) 2022 Zedthon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.
# الملــف محمــي بحقــوق النشـــر والملـكيـه
# تخمــط بــدون ذكــر المصــدر ابلــع حســابـك بانـــد
"""
CC Checker & Generator for ZThon™ t.me/ZThon
Write file by Zelzal t.me/zzzzl1l
hhh o ya beby

"""

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock

from ..core.managers import edit_or_reply
from . import zedub

plugin_category = "البوت"


# code by t.me/zzzzl1l
@zedub.zed_cmd(pattern="cc(?:\s|$)([\s\S]*)")
async def song2(event):
    song = event.pattern_match.group(1)
    chat = "@SDBB_Bot"  # code by t.me/zzzzl1l
    await reply_id(event)
    zed = await edit_or_reply(event, "**⎉╎جـارِ فحص البطـاقـه ...**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/chk {}".format(song)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await zedub(unblock("SDBB_Bot"))
            gool = "/chk {}".format(song)
            await conv.send_message(gool)
        await asyncio.sleep(22)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
            return await zed.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
            return await zed.edit(
                "**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**"
            )
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


# code by t.me/zzzzl1l
@zedub.zed_cmd(pattern="كومبو(?:\s|$)([\s\S]*)")
async def song2(event):  # code by t.me/zzzzl1l
    been = event.pattern_match.group(1)
    chat = "@SDBB_Bot"
    await reply_id(event)
    zed = await edit_or_reply(
        event, f"**⎉╎جـارِ جلب كومبـو لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**"
    )
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await zedub(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
            return await zed.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
            return await zed.edit(
                "**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**"
            )
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


# code by t.me/zzzzl1l
@zedub.zed_cmd(pattern="توليد(?:\s|$)([\s\S]*)")
async def song2(event):
    been = event.pattern_match.group(1)
    chat = "@SDBB_Bot"  # code by t.me/zzzzl1l
    await reply_id(event)
    zed = await edit_or_reply(
        event, f"**⎉╎جـارِ جلب كومبـو لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**"
    )
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await zedub(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
            return await zed.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
            return await zed.edit(
                "**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**"
            )
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


# code by t.me/zzzzl1l
@zedub.zed_cmd(pattern="فيزا(?:\s|$)([\s\S]*)")
async def song2(event):
    been = "410039xxxxxxxxxx|xx|xxxx|xxx"  # code by t.me/zzzzl1l
    chat = "@SDBB_Bot"  # code by t.me/zzzzl1l
    await reply_id(event)
    zed = await edit_or_reply(
        event,
        f"**⎉╎جـارِ تولـيد 𝚅𝙸𝚂𝙴💲...**\n**⎉╎لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**",
    )
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await zedub(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
            return await zed.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
            return await zed.edit(
                "**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**"
            )
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


# code by t.me/zzzzl1l
@zedub.zed_cmd(pattern="ماستر(?:\s|$)([\s\S]*)")
async def song2(event):
    been = "524447000053xxxx|xx|xxxx|xxx"  # code by t.me/zzzzl1l
    chat = "@SDBB_Bot"  # code by t.me/zzzzl1l
    await reply_id(event)
    zed = await edit_or_reply(
        event,
        f"**⎉╎جـارِ تولـيد بن 𝙼𝙰𝚂𝚃𝙴𝚁𝙲𝙰𝚁𝙳 💳...**\n**⎉╎لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**",
    )
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await zedub(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
            return await zed.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
            return await zed.edit(
                "**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**"
            )
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()


# code by t.me/zzzzl1l
@zedub.zed_cmd(pattern="اماكس(?:\s|$)([\s\S]*)")
async def song2(event):
    been = "373352589xxxxxx|xx|xxxx|xxxx"  # code by t.me/zzzzl1l
    chat = "@SDBB_Bot"  # code by t.me/zzzzl1l
    await reply_id(event)
    zed = await edit_or_reply(
        event,
        f"**⎉╎جـارِ تولـيد بن 🇧🇷 𝙰𝙼𝙴𝚇...**\n**⎉╎لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**",
    )
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await zedub(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
            return await zed.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
            return await zed.edit(
                "**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**"
            )
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await zed.delete()

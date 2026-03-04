import httpx

from app.core.config import DISCORD_WEBHOOK


async def send_discord_event(username: str, mod_id: str, timestamp: int):
    # sends discord message

    message = {
        "content": (
            "🟢 **New login**\n"
            f"User: `{username}`\n"
            f"ID: `{mod_id}`\n"
            f"Timestamp: `{timestamp}`"
        )
    }

    async with httpx.AsyncClient() as client:
        await client.post(DISCORD_WEBHOOK, json=message)
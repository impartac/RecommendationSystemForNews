from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession
from config.config import session_async


async def get_async_db_session() -> AsyncIterator[AsyncSession]:
    async with session_async() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
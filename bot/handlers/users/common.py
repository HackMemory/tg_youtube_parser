from aiogram import types
from aiogram.dispatcher import FSMContext


START_TEXT = (
    'Welcome to youtube crawler bot\n'
    'Enter /search command to start'
)

async def cmd_start(message: types.Message):
    """Start command."""
    await message.answer(START_TEXT)

async def cmd_cancel(message: types.Message, state: FSMContext):
    """Command to cancel any current state."""
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(
            'There are no active commands to cancel'
        )
        return
    await state.finish()
    await message.answer(
        'Command canceled',
        reply_markup=types.ReplyKeyboardRemove(),
    )
from aiogram.utils import executor
from create_bot import dp
from handlers import start, FSM

start.register_handlers_start(dp)
FSM.register_handlers_FSM(dp)
executor.start_polling(dp, skip_updates=True)
